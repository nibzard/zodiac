"""Solver under test. THE AGENT EDITS THIS FILE ONLY.

Deep-restart simulated annealing over the symbol-to-letter key, run in
parallel worker processes. The frozen five-gram language model from
ciphers.py is compiled once into integer-keyed tables; a move rescores
only the n-gram windows that touch the changed symbol, through cached
per-position gram codes. Distinct decodes across restarts are pooled and
returned ranked by the same language model.

The internal score carries one constant offset per early text position
relative to the frozen LM (an artifact of folding the backoff ladder
into flat tables). The offset is the same for every decode of the same
length, so ranking order matches the frozen LM exactly.

A wide numpy prefix beam is available for experiments (ZBEAM=1); it is
off by default because its width needs exceed the per-instance time
slice at lengths below 300.

Required interface (called by ciphers.py):

    def solve(cipher: str, deadline: float) -> list[str]
"""

import math
import os
import random
import sys
import time
from operator import itemgetter as _itemgetter

import ciphers

try:
    import numpy as _np
except ImportError:
    _np = None

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

_LOG_BO = math.log(ciphers.LM.backoff)
# Four backoffs, then the frozen unseen-unigram branch.
_FLOOR = 4 * _LOG_BO + math.log(0.5 / ciphers.LM.char_total)
_M26 = [26 ** k for k in range(6)]


def _compile():
    """Fold the stupid-backoff ladder into flat int-keyed tables.

    A gram of order n reached while scoring position i is charged (5-n)
    backoffs as if every ladder started at order 5. That adds a fixed
    offset per position (0 for i >= 4), identical across decodes.
    """
    tabs = {}
    for n in range(1, 6):
        pen = (5 - n) * _LOG_BO
        tab = {}
        for gram, cnt in ciphers.LM.counts[n].items():
            code = 0
            for ch in gram:
                code = code * 26 + (ord(ch) - 65)
            tab[code] = math.log(cnt / ciphers.LM.totals[n][gram[:-1]]) + pen
        tabs[n] = tab
    return tabs


_T = _compile()
_T5 = _T[5]

# Letter pool for seeding random keys, from corpus unigram counts.
_SEED = []
for _i, _ch in enumerate(LETTERS):
    _SEED.extend([_i] * max(1, ciphers.LM.counts[1].get(_ch, 0) // 1000))

# Diagnostics only; never printed to stdout.
_STATS = {"restarts": 0, "applies": 0}

# (iters, t_start, t_end, p_change) per length class. Deep chains beat
# many shallow ones only for big key spaces: at 54 symbols and length 408
# (Z408) 400k-iteration restarts reach edit distance 6 where 80k-iteration
# restarts stall at 262. Suite-length ciphers recover best from many
# shallow restarts (~20% of 80k restarts crack a length-340 instance).
_PARAM_TABLE = {
    "long": (80000, 6.0, 0.05, 0.55),
    "mid": (60000, 5.0, 0.05, 0.55),
    "short": (40000, 3.0, 0.03, 0.55),
    "tiny": (25000, 2.0, 0.02, 0.55),
}
_DEEP = (400000, 6.0, 0.05, 0.55)


def _params_for(L, S):
    if S >= 50 and L >= 400:
        return _DEEP
    if L >= 200:
        return _PARAM_TABLE["long"]
    if L >= 80:
        return _PARAM_TABLE["mid"]
    if L >= 30:
        return _PARAM_TABLE["short"]
    return _PARAM_TABLE["tiny"]


def _score(dec):
    """Total laddered logprob of a decode given as letter ints."""
    tot = 0.0
    g = 0
    T1, T2, T3, T4, T5 = _T[1], _T[2], _T[3], _T[4], _T5
    for i in range(len(dec)):
        d = dec[i]
        if i < 5:
            g = g * 26 + d
            m = i + 1
        else:
            g = (g % _M26[4]) * 26 + d
            m = 5
        if m == 5:
            v = T5.get(g)
            if v is None:
                v = T4.get(g % _M26[4])
                if v is None:
                    v = T3.get(g % _M26[3])
                    if v is None:
                        v = T2.get(g % _M26[2])
                        if v is None:
                            v = T1.get(g % 26)
                            if v is None:
                                v = _FLOOR
        else:
            v = _T[m].get(g)
            k = m
            while v is None and k > 1:
                k -= 1
                v = _T[k].get(g % _M26[k])
            if v is None:
                v = _FLOOR
        tot += v
    return tot


def _sa_restart(cs, rng, iters, t0, t_end, pchg, stop_at):
    """One annealing restart plus greedy polish. Returns (score, bytes).

    Self-contained so a fork-pool worker can run it directly on the
    pickled symbol-id list.
    """
    L = len(cs)
    S = max(cs) + 1
    occ = [[] for _ in range(S)]
    for i, s in enumerate(cs):
        occ[s].append(i)
    # hot[s] / cold[s]: positions whose gram window touches symbol s, with
    # the base-26 place value the symbol carries in that window's packed
    # gram code. Cold covers the first four positions, whose grams are
    # shorter than five and need a different ladder start.
    hot = []
    cold = []
    for s in range(S):
        w = {}
        for p in occ[s]:
            for j in range(p, min(L, p + 5)):
                w[j] = w.get(j, 0) + _M26[j - p]
        hot.append([(j, w[j]) for j in sorted(w) if j >= 4])
        cold.append([(j, w[j]) for j in sorted(w) if j < 4])

    key = [0] * S
    dec = [0] * L
    gc = [0] * L
    tv = [0.0] * L

    t5get = _T5.get
    t4get = _T[4].get
    t3get = _T[3].get
    t2get = _T[2].get
    t1get = _T[1].get
    expf = math.exp
    tabs = _T
    m26 = _M26

    def apply(s, letter):
        """Set symbol s to letter; update caches; return the score delta."""
        old = key[s]
        diff = letter - old
        if diff == 0:
            return 0.0
        key[s] = letter
        delta = 0.0
        for j, w in hot[s]:
            nc = gc[j] + diff * w
            v = t5get(nc)
            if v is None:
                v = t4get(nc % m26[4])
                if v is None:
                    v = t3get(nc % m26[3])
                    if v is None:
                        v = t2get(nc % m26[2])
                        if v is None:
                            v = t1get(nc % 26)
                        if v is None:
                            v = _FLOOR
            delta += v - tv[j]
            gc[j] = nc
            tv[j] = v
        for j, w in cold[s]:
            nc = gc[j] + diff * w
            k = j + 1
            v = tabs[k].get(nc)
            while v is None and k > 1:
                k -= 1
                v = tabs[k].get(nc % m26[k])
            if v is None:
                v = _FLOOR
            delta += v - tv[j]
            gc[j] = nc
            tv[j] = v
        for p in occ[s]:
            dec[p] = letter
        return delta

    def load_key():
        """Rebuild dec/gc/tv caches from the current key."""
        for i in range(L):
            dec[i] = key[cs[i]]
        g = 0
        for i in range(L):
            d = dec[i]
            if i < 5:
                g = g * 26 + d
                m = i + 1
            else:
                g = (g % m26[4]) * 26 + d
                m = 5
            if m == 5:
                v = t5get(g)
                if v is None:
                    v = t4get(g % m26[4])
                    if v is None:
                        v = t3get(g % m26[3])
                        if v is None:
                            v = t2get(g % m26[2])
                            if v is None:
                                v = t1get(g % 26)
                            if v is None:
                                v = _FLOOR
            else:
                v = tabs[m].get(g)
                k = m
                while v is None and k > 1:
                    k -= 1
                    v = tabs[k].get(g % m26[k])
                if v is None:
                    v = _FLOOR
            gc[i] = g
            tv[i] = v

    bag = list(_SEED)
    rng.shuffle(bag)
    for s in sorted(range(S), key=lambda s: -len(occ[s])):
        key[s] = bag.pop() if bag else rng.randrange(26)
    load_key()
    score = sum(tv)
    best_score = score
    best_dec = dec[:]
    T = t0
    rate = (t_end / t0) ** (1.0 / max(1, iters))
    rnd = rng.random
    rr = rng.randrange
    for it in range(iters):
        if not it & 255 and time.time() >= stop_at:
            break
        T *= rate
        if rnd() < pchg:
            s = rr(S)
            nl = rr(26)
            old = key[s]
            if nl == old:
                continue
            d = apply(s, nl)
            if d >= 0.0 or rnd() < expf(d / T):
                score += d
                if score > best_score:
                    best_score = score
                    best_dec = dec[:]
            else:
                apply(s, old)
        else:
            s1 = rr(S)
            s2 = rr(S)
            if s1 == s2:
                continue
            a = key[s1]
            b = key[s2]
            if a == b:
                continue
            d = apply(s1, b) + apply(s2, a)
            if d >= 0.0 or rnd() < expf(d / T):
                score += d
                if score > best_score:
                    best_score = score
                    best_dec = dec[:]
            else:
                apply(s1, a)
                apply(s2, b)
    # Greedy polish to the local optimum.
    for _ in range(8):
        improved = False
        for s in range(S):
            base = key[s]
            for letter in range(26):
                if letter == base:
                    continue
                d = apply(s, letter)
                if d > 0.0:
                    score += d
                    base = letter
                    improved = True
                else:
                    apply(s, base)
        for s1 in range(S):
            for s2 in range(s1 + 1, S):
                a = key[s1]
                b = key[s2]
                if a == b:
                    continue
                d = apply(s1, b) + apply(s2, a)
                if d > 0.0:
                    score += d
                    improved = True
                else:
                    apply(s1, a)
                    apply(s2, b)
        if not improved or time.time() >= stop_at:
            break
    if score > best_score:
        best_score = score
        best_dec = dec[:]
    return _score(best_dec), bytes(best_dec)


def _worker(args):
    """Pool worker: loop restarts until stop_at, return (score, bytes)."""
    cs, seed, params, stop_at = args
    iters, t0, t_end, pchg = params
    rng = random.Random(seed)
    out = []
    while time.time() < stop_at - 0.05:
        sc, decb = _sa_restart(cs, rng, iters, t0, t_end, pchg, stop_at)
        out.append((sc, decb))
    return out


_MP = None


def _get_pool():
    global _MP
    if _MP is None:
        import multiprocessing as mp
        nw = min(4, os.cpu_count() or 1)
        _MP = mp.get_context("fork").Pool(nw)
    return _MP


def solve(cipher, deadline):
    """Return candidate plaintexts, best first."""
    L = len(cipher)
    syms = sorted(set(cipher))
    S = len(syms)
    ids = {s: i for i, s in enumerate(syms)}
    cs = [ids[ch] for ch in cipher]

    pool = {}
    params = _params_for(L, S)

    if os.environ.get("ZBEAM") == "1" and _np is not None:
        if L >= 300:
            W, Wl, T = 60000, 3000, 120
        elif L >= 80:
            W, Wl, T = 150000, 4000, 60
        elif L >= 30:
            W, Wl, T = 150000, 6000, 40
        else:
            W, Wl, T = 100000, 8000, 26
        diag = None
        _di = os.environ.get("ZBEAM_DIAG")
        if _di is not None and _di.isdigit():
            _k = int(_di)
            if 0 <= _k < len(ciphers.SUITE_INSTANCES):
                diag = _np.frombuffer(
                    ciphers.SUITE_INSTANCES[_k][2].encode(), dtype=_np.uint8) - 65
        _beam_np(cs, L, W, Wl, T, deadline - 1.2, pool, diag)

    stop_at = deadline - 0.15
    nw = min(4, os.cpu_count() or 1)
    try:
        mp_pool = _get_pool() if nw > 1 else None
    except Exception:
        mp_pool = None
    if mp_pool is not None:
        import multiprocessing as mp
        tasks = [(cs, 0xC0FFEE + i, params, stop_at) for i in range(nw)]
        try:
            for res in mp_pool.imap_unordered(_worker, tasks):
                for sc, decb in res:
                    if sc > pool.get(decb, float("-inf")):
                        pool[decb] = sc
                _STATS["restarts"] += len(res)
            mp_pool = None
        except Exception:
            mp_pool = None
    if mp_pool is None and not pool:
        res = _worker((cs, 0xC0FFEE, params, stop_at))
        _STATS["restarts"] += len(res)
        for sc, decb in res:
            if sc > pool.get(decb, float("-inf")):
                pool[decb] = sc

    ranked = sorted(pool.items(), key=lambda kv: -kv[1])
    out = []
    for decb, _sc in ranked[:64]:
        out.append("".join(LETTERS[b] for b in decb))
    return out


# ---------------------------------------------------------------------------
# Opt-in wide numpy beam (ZBEAM=1), kept for experiments.

_BYTES = [bytes([i]) for i in range(26)]
_FINAL_KEEP = 512  # full decodes kept from the last beam position

_DENSE = None
_FLOOR_BASE = math.log(0.5 / ciphers.LM.char_total)


def _dense():
    """Dense per-order conditional logprob tables, indexed by gram code."""
    global _DENSE
    if _DENSE is not None:
        return _DENSE
    tabs = []
    for n in range(1, 6):
        arr = _np.full(26 ** n, _np.nan, dtype=_np.float32)
        for gram, cnt in ciphers.LM.counts[n].items():
            code = 0
            for ch in gram:
                code = code * 26 + (ord(ch) - 65)
            arr[code] = math.log(cnt / ciphers.LM.totals[n][gram[:-1]])
        tabs.append(arr)
    _DENSE = tabs
    return tabs


def _ladder_vec(D, g, s, floor):
    """Vectorized stupid-backoff ladder, orders s down to 1."""
    v = D[s - 1][g]
    for k in range(s - 1, 0, -1):
        miss = _np.isnan(v)
        if not miss.any():
            break
        v[miss] = D[k - 1][g[miss] % (26 ** k)] + (s - k) * _LOG_BO
    miss = _np.isnan(v)
    if miss.any():
        v[miss] = floor
    return v


def _beam_np(cs, L, W_early, W_late, T, stop_at, pool, diag=None):
    """Wide numpy beam: dense-table terms, selection before materialization.

    Width decays geometrically from W_early to W_late over T positions; the
    cold start (a run of never-seen symbols) needs the wide head, and once
    symbols repeat the score signal narrows the beam on its own.
    """
    D = _dense()
    ar = _np.arange(26, dtype=_np.int64)
    prev = [-1] * L
    last_seen = {}
    for i, s in enumerate(cs):
        prev[i] = last_seen.get(s, -1)
        last_seen[s] = i
    sc = _np.zeros(1, dtype=_np.float64)
    code = _np.zeros(1, dtype=_np.int64)
    pre = _np.zeros((1, L), dtype=_np.uint8)
    ratio = (W_late / W_early) ** (1.0 / max(1, T))
    for i in range(L):
        if time.time() >= stop_at:
            return False
        m = i if i < 4 else 4
        s = m + 1
        floor = s * _LOG_BO + _FLOOR_BASE
        j = i + 1
        Wj = max(W_late, int(W_early * ratio ** j))
        p = prev[i]
        if p >= 0:
            lt = pre[:, p]
            g = code * 26 + lt
            sc = sc + _ladder_vec(D, g, s, floor)
            if m == 4:
                code = (code % 17576) * 26 + lt
            else:
                code = code * 26 + lt
            pre[:, i] = lt
        else:
            g = code[:, None] * 26 + ar[None, :]
            terms = _ladder_vec(D, g, s, floor)
            child = (sc[:, None] + terms).ravel()
            n = child.size
            K = min(Wj, n)
            if K < n:
                idx = _np.argpartition(child, n - K)[n - K:]
                idx = idx[_np.argsort(child[idx])[::-1]]
            else:
                idx = _np.argsort(child)[::-1]
            pari = idx // 26
            lti = idx - pari * 26
            sc = child[idx]
            pre = pre[pari]
            pre[:, i] = lti.astype(_np.uint8)
            if m == 4:
                code = (code[pari] % 17576) * 26 + lti
            else:
                code = code[pari] * 26 + lti
        if diag is not None:
            eq = (pre[:, :j] == diag[None, :j]).all(axis=1)
            w = int(eq.sum())
            pos = int(_np.flatnonzero(eq)[0]) if w else -1
            print(f"diag pos {i} width {pre.shape[0]} truth-in-beam {w} "
                  f"rank {pos}", file=sys.stderr)
    order = _np.argsort(sc)[::-1][:64]
    for k in order:
        pb = bytes(pre[k])
        pool[pb] = _score(pb)
    return True


def _fill(c, g, m, tabs, m26):
    """Ladder-fill one cached term: order m+1 down, suffix lookups."""
    k = m + 1
    v = tabs[k].get(g)
    while v is None and k > 1:
        k -= 1
        v = tabs[k].get(g % m26[k])
    if v is None:
        v = _FLOOR
    c[g] = v
    return v


def _beam_search(cs, L, W, stop_at, pool):
    """Pure-Python beam fallback with exact future-state dedupe."""
    prev = [-1] * L
    last_seen = {}
    for i, s in enumerate(cs):
        prev[i] = last_seen.get(s, -1)
        last_seen[s] = i
    fpos = [()] * (L + 1)
    getters = [None] * (L + 1)
    latest = {}
    for j in range(1, L + 1):
        latest[cs[j - 1]] = j - 1
        fp = tuple(pos for s, pos in latest.items() if last_seen[s] >= j)
        fpos[j] = fp
        getters[j] = _itemgetter(*fp) if len(fp) > 1 else None

    C1, C2, C3, C4 = {}, {}, {}, {}
    tabs = _T
    m26 = _M26
    beam = [(0.0, b"", 0)]
    for i in range(L):
        if time.time() >= stop_at:
            return False
        m = i if i < 4 else 4
        c = (C1, C2, C3, C4)[m - 1]
        cget = c.get
        children = []
        app = children.append
        p = prev[i]
        if p >= 0:
            for nsc, pre, code in beam:
                lt = pre[p]
                g = code * 26 + lt
                v = cget(g)
                if v is None:
                    v = _fill(c, g, m, tabs, m26)
                if m == 4:
                    code2 = (code % m26[3]) * 26 + lt
                else:
                    code2 = code * 26 + lt
                app((nsc - v, pre + _BYTES[lt], code2))
        else:
            for nsc, pre, code in beam:
                base = code * 26
                for lt in range(26):
                    g = base + lt
                    v = cget(g)
                    if v is None:
                        v = _fill(c, g, m, tabs, m26)
                    if m == 4:
                        code2 = (code % m26[3]) * 26 + lt
                    else:
                        code2 = code * 26 + lt
                    app((nsc - v, pre + _BYTES[lt], code2))
        children.sort()
        j = i + 1
        if j == L:
            beam = children[:_FINAL_KEEP]
            break
        keep = []
        fp = fpos[j]
        if fp:
            gett = getters[j]
            seen = set()
            add = seen.add
            for ch in children[: 3 * W]:
                key = (ch[2],) + gett(ch[1]) if gett else (ch[2], ch[1][fp[0]])
                if key not in seen:
                    add(key)
                    keep.append(ch)
                    if len(keep) >= W:
                        break
            if not keep:
                keep = children[:W]
        else:
            keep = children[:W]
        beam = keep
    for nsc, pre, _code in beam[:64]:
        pool[pre] = _score(pre)
    return True


if __name__ == "__main__":
    ciphers.report(solve)
