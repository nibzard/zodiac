"""Live demo server: streams a real cipher-solver run to the browser.

Serves a single page plus Server-Sent Events:
  - /events   SSE stream: best-decode ticks, pool candidates, Jev judgments
  - /target   POST {"id": "..."} switches the cipher under attack
  - /static/* data pack for the ensemble / cliff / discrimination panels

The search runs the real research machinery (solve.py annealing, imported
read-only) in a fork pool; one in-process display chain streams the raw
annealing text so you watch gibberish organize. Jev coherence judgments
(TypeSafe AI) are optional: without TYPESAFE_API_KEY the coherence panel
shows the threshold line only.
"""
import json
import math
import os
import queue
import random
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REPO = "/home/agent/zodiac/zodiac-autoresearch"
DEMO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
import ciphers  # noqa: E402
import solve  # noqa: E402

PORT = int(os.environ.get("DEMO_PORT", "8408"))
LET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ---------------------------------------------------------------- targets
def _readable_truth():
    txt = open(os.path.join(REPO, "data/z340-solution.txt")).read().upper()
    return "".join(ch for ch in txt if ch.isalpha())

def _reordered():
    cipher = ciphers.CIPHERS["z340.raw"]
    rows = [cipher[r * 17:(r + 1) * 17] for r in range(20)]
    band = lambda r0: "".join(rows[r0 + k % 9][(2 * k) % 17] for k in range(9 * 17))
    return band(0) + band(9) + cipher[306:]

_z340_truth = _readable_truth()
TARGETS = {}
for _n, _c, _t in ciphers.SUITE_INSTANCES:
    if _n in ("synth340_0", "synth100_1", "synth32_2"):
        TARGETS[_n] = {"cipher": _c, "truth": _t, "label": _n + " (synthetic, truth known)"}
TARGETS["z340"] = {"cipher": ciphers.CIPHERS["z340.raw"], "truth": _z340_truth,
                   "label": "Z340 real, plain order"}
TARGETS["z340r"] = {"cipher": _reordered(), "truth": _z340_truth,
                    "label": "Z340 real, 9-9-2 reordered (true order class)"}
DEFAULT = "synth340_0"

# ---------------------------------------------------------------- state
class State:
    def __init__(self):
        self.lock = threading.Lock()
        self.target_id = DEFAULT
        self.pool = {}          # decode bytes -> internal score
        self.judged = {}        # decode text -> jev score
        self.restarts = 0
        self.best_lm = float("-inf")
        self.history = []       # (t, lm_perchar) of running best
        self.subs = []          # subscriber queues
        self.alarm = None

    def switch(self, tid):
        with self.lock:
            self.target_id = tid
            self.pool.clear()
            self.judged.clear()
            self.restarts = 0
            self.best_lm = float("-inf")
            self.history = []
            self.alarm = None

S = State()

def emit(kind, data):
    dead = []
    for q in list(S.subs):
        try:
            q.put_nowait((kind, data))
        except queue.Full:
            dead.append(q)
    for q in dead:
        if q in S.subs:
            S.subs.remove(q)

def editdist(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

# ------------------------------------------------- display annealer (streamed)
M26 = solve._M26
FLOOR = solve._FLOOR

def anneal_stream(cs, rng, iters, t0, t_end, pchg, tid, truth):
    """One annealing chain; push a decode snapshot every ~2k iterations."""
    L, S_ = len(cs), max(cs) + 1
    occ = [[] for _ in range(S_)]
    for i, s in enumerate(cs):
        occ[s].append(i)
    hot, cold = [], []
    for s in range(S_):
        w = {}
        for p in occ[s]:
            for j in range(p, min(L, p + 5)):
                w[j] = w.get(j, 0) + M26[j - p]
        hot.append([(j, w[j]) for j in sorted(w) if j >= 4])
        cold.append([(j, w[j]) for j in sorted(w) if j < 4])
    key = [0] * S_
    bag = list(solve._SEED)
    rng.shuffle(bag)
    for s in sorted(range(S_), key=lambda s: -len(occ[s])):
        key[s] = bag.pop() if bag else rng.randrange(26)
    dec = [key[s] for s in cs]
    gc, tv = [0] * L, [0.0] * L
    tabs = solve._T

    def load():
        g = 0
        for i in range(L):
            d = dec[i]
            g = (g * 26 + d) if i < 5 else ((g % M26[4]) * 26 + d)
            v = tabs[5].get(g)
            k = 5
            while v is None and k > 1:
                k -= 1
                v = tabs[k].get(g % M26[k])
            if v is None:
                v = FLOOR
            gc[i], tv[i] = g, v

    def apply(s, letter):
        old = key[s]
        diff = letter - old
        if diff == 0:
            return 0.0
        key[s] = letter
        delta = 0.0
        for j, w in hot[s]:
            nc = gc[j] + diff * w
            v = tabs[5].get(nc)
            k = 5
            while v is None and k > 1:
                k -= 1
                v = tabs[k].get(nc % M26[k])
            if v is None:
                v = FLOOR
            delta += v - tv[j]
            gc[j], tv[j] = nc, v
        for j, w in cold[s]:
            nc = gc[j] + diff * w
            k = j + 1
            v = tabs[k].get(nc)
            while v is None and k > 1:
                k -= 1
                v = tabs[k].get(nc % M26[k])
            if v is None:
                v = FLOOR
            delta += v - tv[j]
            gc[j], tv[j] = nc, v
        for p in occ[s]:
            dec[p] = letter
        return delta

    load()
    score = sum(tv)
    best, best_dec = score, dec[:]
    T = t0
    rate = (t_end / t0) ** (1.0 / max(1, iters))
    expf, rnd, rr = math.exp, rng.random, rng.randrange
    for it in range(iters):
        T *= rate
        if rnd() < pchg:
            s = rr(S_)
            nl = rr(26)
            old = key[s]
            if nl == old:
                continue
            d = apply(s, nl)
            if d >= 0.0 or rnd() < expf(d / T):
                score += d
                if score > best:
                    best, best_dec = score, dec[:]
            else:
                apply(s, old)
        else:
            s1, s2 = rr(S_), rr(S_)
            if s1 == s2:
                continue
            a, b = key[s1], key[s2]
            if a == b:
                continue
            d = apply(s1, b) + apply(s2, a)
            if d >= 0.0 or rnd() < expf(d / T):
                score += d
                if score > best:
                    best, best_dec = score, dec[:]
            else:
                apply(s1, a)
                apply(s2, b)
        if not it % 2048:
            txt = "".join(LET[b] for b in dec)
            emit("tick", {"target": tid, "iter": it,
                          "lm": round(score / L, 3), "text": txt})
    return best_dec

def display_loop():
    rng = random.Random(0x5EED)
    while True:
        tid = S.target_id
        t = TARGETS[tid]
        cs = [sorted(set(t["cipher"])).index(ch) for ch in t["cipher"]]
        L, S_ = len(cs), len(set(cs))
        iters, t0, t_end, pchg = solve._params_for(L, S_)
        dec = anneal_stream(cs, rng, iters, t0, t_end, pchg, tid, t["truth"])
        with S.lock:
            S.pool[bytes(dec)] = solve._score(list(dec))
            S.restarts += 1

# ------------------------------------------------- fork-pool search thread
def _task(a):
    cs, seed, params, stop_at = a
    rng = random.Random(seed)
    out = []
    while time.time() < stop_at:
        out.append(solve._sa_restart(cs, rng, *params, stop_at))
    return out

def search_loop(pool):
    n = 0
    while True:
        tid = S.target_id
        t = TARGETS[tid]
        syms = sorted(set(t["cipher"]))
        ids = {s: i for i, s in enumerate(syms)}
        cs = [ids[ch] for ch in t["cipher"]]
        params = solve._params_for(len(cs), len(syms))
        stop = time.time() + 5.0
        tasks = [(cs, 0xD00D + n * 4 + i, params, stop) for i in range(4)]
        n += 1
        try:
            for res in pool.imap_unordered(_task, tasks):
                for sc, decb in res:
                    with S.lock:
                        if sc > S.pool.get(decb, float("-inf")):
                            S.pool[decb] = sc
                        S.restarts += 1
        except Exception as e:  # keep the demo alive no matter what
            emit("warn", {"msg": str(e)[:120]})
            time.sleep(2)

# ------------------------------------------------- periodic pool broadcast
def broadcast_loop():
    while True:
        time.sleep(2.0)
        tid = S.target_id
        t = TARGETS[tid]
        with S.lock:
            ranked = sorted(S.pool.items(), key=lambda kv: -kv[1])[:10]
            restarts = S.restarts
        if not ranked:
            continue
        rows = []
        for decb, sc in ranked:
            txt = "".join(LET[b] for b in decb)
            lm = ciphers.LM.logperchar(txt)
            d = editdist(txt, t["truth"]) if t["truth"] else None
            rows.append({"text": txt, "lm": round(lm, 4), "dist": d,
                         "jev": S.judged.get(txt)})
            with S.lock:
                if lm > S.best_lm:
                    S.best_lm = lm
                S.history.append((time.time(), lm))
                S.history = S.history[-400:]
        emit("pool", {"target": tid, "restarts": restarts, "rows": rows,
                      "best_lm": round(max(r["lm"] for r in rows), 4)})

# ------------------------------------------------- Jev judge thread
def jev_loop():
    try:
        from typesafe_sdk import TypeSafeClient, Score
        client = TypeSafeClient(model="jev-latest")
    except Exception:
        emit("warn", {"msg": "Jev disabled (no SDK or API key)"})
        return
    LEVELS = [
        "Random letters with no English structure, like keyboard mash",
        "English-looking fragments but no meaningful word or phrase can be read",
        "One or more meaningful English words or names appear, misspellings allowed",
        "A coherent meaningful English phrase, sentence or passage, misspellings allowed",
    ]
    while True:
        time.sleep(6.0)
        tid = S.target_id
        t = TARGETS[tid]
        with S.lock:
            ranked = sorted(S.pool.items(), key=lambda kv: -kv[1])[:40]
        todo = []
        for decb, _sc in ranked:
            txt = "".join(LET[b] for b in decb)
            if txt not in S.judged and txt not in [x[0] for x in todo]:
                todo.append((txt, len(todo)))
            if len(todo) == 6:
                break
        if not todo:
            continue
        items = [{"id": j, "text": txt} for j, (txt, _) in enumerate(todo)]
        q = {f"s{j}": Score(instructions=(
            f"Rate how far the letter string at `items[{j}].text` reads as "
            "intentional English written by a person."), criteria=LEVELS)
             for j in range(len(items))}
        try:
            r = client.system_one(
                {"context": "Candidate decodings of a historical cipher, from a solving program.",
                 "items": items}, q)
        except Exception as e:
            emit("warn", {"msg": "jev: " + str(e)[:100]})
            continue
        for j, (txt, _) in enumerate(todo):
            sc = r.scores[f"s{j}"].score
            with S.lock:
                S.judged[txt] = sc
            d = editdist(txt, t["truth"]) if t["truth"] else None
            emit("jev", {"text": txt, "jev": sc, "dist": d, "target": tid})
            if sc >= 2.6 and (S.alarm is None or sc > S.alarm[1]):
                with S.lock:
                    S.alarm = (txt, sc)
                emit("alarm", {"text": txt, "jev": sc, "dist": d})

# ------------------------------------------------- HTTP
class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, "text/html; charset=utf-8",
                       open(os.path.join(DEMO, "index.html"), "rb").read())
        elif self.path == "/static/pack.json":
            self._send(200, "application/json",
                       open(os.path.join(DEMO, "static/pack.json"), "rb").read())
        elif self.path == "/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            q = queue.Queue(maxsize=256)
            S.subs.append(q)
            try:
                self.wfile.write(b"data: " + json.dumps({
                    "kind": "init",
                    "targets": [{"id": k, "label": v["label"]} for k, v in TARGETS.items()],
                    "current": S.target_id,
                    "restarts": S.restarts,
                    "alarm": S.alarm and {"text": S.alarm[0], "jev": S.alarm[1]}}).encode() + b"\n\n")
                self.wfile.flush()
                while True:
                    try:
                        kind, data = q.get(timeout=15)
                    except queue.Empty:
                        self.wfile.write(b": ping\n\n")
                        self.wfile.flush()
                        continue
                    self.wfile.write(b"data: " + json.dumps(
                        {"kind": kind, **data}).encode() + b"\n\n")
                    self.wfile.flush()
            except Exception:
                pass
            finally:
                if q in S.subs:
                    S.subs.remove(q)
        else:
            self._send(404, "text/plain", b"not found")

    def do_POST(self):
        if self.path == "/target":
            n = int(self.headers.get("Content-Length", 0))
            try:
                tid = json.loads(self.rfile.read(n)).get("id")
            except Exception:
                tid = None
            if tid in TARGETS:
                S.switch(tid)
                emit("reset", {"target": tid})
                self._send(200, "application/json", b'{"ok":true}')
            else:
                self._send(404, "application/json", b'{"ok":false}')
        else:
            self._send(404, "text/plain", b"not found")

def main():
    import multiprocessing as mp
    pool = mp.get_context("fork").Pool(4)
    threading.Thread(target=search_loop, args=(pool,), daemon=True).start()
    threading.Thread(target=display_loop, daemon=True).start()
    threading.Thread(target=broadcast_loop, daemon=True).start()
    if os.environ.get("TYPESAFE_API_KEY"):
        threading.Thread(target=jev_loop, daemon=True).start()
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), H)
    print(f"demo on http://localhost:{PORT}", flush=True)
    srv.serve_forever()

if __name__ == "__main__":
    main()
