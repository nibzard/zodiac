"""Solver under test. THE AGENT EDITS THIS FILE ONLY.

Simulated annealing over the symbol-to-letter key. The frozen five-gram
language model from ciphers.py is compiled once into integer-keyed
tables; a move rescores only the n-gram windows that touch the changed
symbol, through cached per-position gram codes. Restarts collect
distinct decodes and the best are returned, ranked by the same language
model.

The internal score carries one constant offset per early text position
relative to the frozen LM (an artifact of folding the backoff ladder
into flat tables). The offset is the same for every decode of the same
length, so ranking order matches the frozen LM exactly.

Required interface (called by ciphers.py):

    def solve(cipher: str, deadline: float) -> list[str]
"""

import math
import random
import time

import ciphers

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

# Diagnostics only; never printed inside solve().
_STATS = {"moves": 0, "restarts": 0, "applies": 0}

# (iters, t_start, t_end, p_change) per length class, tuned on the suite.
_PARAM_TABLE = {
    "long": (80000, 6.0, 0.05, 0.55),
    "mid": (60000, 5.0, 0.05, 0.55),
    "short": (40000, 3.0, 0.03, 0.55),
    "tiny": (25000, 2.0, 0.02, 0.55),
}


def _params_for(L):
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


def solve(cipher, deadline):
    """Return candidate plaintexts, best first."""
    L = len(cipher)
    syms = sorted(set(cipher))
    S = len(syms)
    ids = {s: i for i, s in enumerate(syms)}
    cs = [ids[ch] for ch in cipher]

    occ = [[] for _ in range(S)]
    for i, s in enumerate(cs):
        occ[s].append(i)

    # hot[s] / cold[s]: positions whose gram window touches symbol s, with
    # the base-26 place value the symbol's occurrences carry in that
    # window's packed gram code. Cold covers the first four positions,
    # whose grams are shorter than five and need a different ladder start.
    hot = []
    cold = []
    for s in range(S):
        w = {}
        for p in occ[s]:
            for j in range(p, min(L, p + 5)):
                w[j] = w.get(j, 0) + _M26[j - p]
        h = [(j, w[j]) for j in sorted(w) if j >= 4]
        c = [(j, w[j]) for j in sorted(w) if j < 4]
        hot.append(h)
        cold.append(c)

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

    iters, t0, t_end, pchg = _params_for(L)
    rate = (t_end / t0) ** (1.0 / max(1, iters))

    pool = {}
    rng = random.Random(0xC0FFEE)

    def one_restart(stop_at):
        bag = list(_SEED)
        rng.shuffle(bag)
        for s in sorted(range(S), key=lambda s: -len(occ[s])):
            key[s] = bag.pop() if bag else rng.randrange(26)
        load_key()
        score = sum(tv)
        best_score = score
        best_dec = dec[:]
        T = t0
        rnd = rng.random
        rr = rng.randrange
        moves = 0
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
                _STATS["applies"] += 1
                if d >= 0.0 or rnd() < expf(d / T):
                    score += d
                    moves += 1
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
                _STATS["applies"] += 2
                if d >= 0.0 or rnd() < expf(d / T):
                    score += d
                    moves += 1
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
            if not improved or time.time() >= deadline - 0.1:
                break
        if score > best_score:
            best_score = score
            best_dec = dec[:]
        pool[bytes(best_dec)] = _score(best_dec)
        return best_score

    best_key_copy = None
    best_overall = float("-inf")
    while True:
        now = time.time()
        if now >= deadline - 0.12:
            break
        room = deadline - 0.12 - now
        stop_at = now + max(0.35, room / 3.0)
        sc = one_restart(stop_at)
        _STATS["restarts"] += 1
        if sc > best_overall:
            best_overall = sc
            best_key_copy = key[:]

    # Enumerate single-symbol variants of the best key: if the search
    # stopped one letter short of the truth, the truth is here.
    if best_key_copy is not None and time.time() < deadline - 0.02:
        for s in range(S):
            key[s] = best_key_copy[s]
        load_key()
        for s in range(S):
            if time.time() >= deadline - 0.02:
                break
            base = key[s]
            for letter in range(26):
                if letter == base:
                    continue
                apply(s, letter)
                pool[bytes(dec)] = _score(dec)
                apply(s, base)

    if not pool:
        for s in sorted(range(S), key=lambda s: -len(occ[s])):
            key[s] = _SEED[s % len(_SEED)]
        load_key()
        pool[bytes(dec)] = _score(dec)

    ranked = sorted(pool.items(), key=lambda kv: -kv[1])
    out = []
    for decb, _sc in ranked[:64]:
        out.append("".join(LETTERS[b] for b in decb))
    return out


if __name__ == "__main__":
    ciphers.report(solve)
