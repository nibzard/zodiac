"""Frozen evaluation harness for the Zodiac cipher autoresearch loop.

DO NOT EDIT. The agent under test edits solve.py only.

Loads the four Zodiac ciphertexts, the two confirmed solutions, and the
language-model corpus; trains a character five-gram model with stupid
backoff; generates fixed synthetic homophonic ciphers at several lengths;
and scores the solver defined in solve.py.

When solve.py runs as a script (python3 solve.py), these summary lines are
printed to stdout (program.md greps them):

    synth_score: <float>   mean log2 position of the true plaintext in the
                           solver's ranked candidate list (absent counts as
                           position 64); lower is better, 0 is perfect
    z340_gap: <float>      LM score gap of best Z340 replay decode, lower is better
    recovered: <int>/<int> synthetic instances where the true plaintext ranked first

Interface the solver in solve.py must provide:

    def solve(cipher: str, deadline: float) -> list[str]

Return candidate plaintexts, best first, uppercase A to Z. Return at least
one candidate. Respect the deadline (a float from time.time()).
"""

import math
import os
import random
import re
import time

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
BUDGET = float(os.environ.get("ZODIAC_BUDGET", "300"))  # seconds, whole run
SYNTH_SHARE = 0.6  # fraction of the budget given to the synthetic suite
SUITE = [13, 32, 100, 340]  # plaintext lengths
INSTANCES = 5  # per length; fixed seeds, so the suite never changes
ORDERS = 5  # character ngram order of the language model

# --------------------------------------------------------------------------
# Data loading and integrity checks


def _read(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return fh.read()


def _clean(text):
    """Normalize to the alphabet the ciphers use: A to Z, nothing else."""
    return re.sub(r"[^A-Z]", "", text.upper())


CIPHERS = {name: _read(name).strip() for name in
           ("z340.raw", "z408.raw", "z13.raw", "z32.raw")}
SOLUTIONS = {"z340.raw": _clean(_read("z340-solution.txt")),
             "z408.raw": _clean(_read("z408-solution.txt"))}

for _name, _want in (("z340.raw", (340, 63)), ("z408.raw", (408, 54)),
                     ("z13.raw", (13, 8)), ("z32.raw", (32, 29))):
    _text = CIPHERS[_name]
    assert len(_text) == _want[0], (_name, len(_text))
    assert len(set(_text)) == _want[1], (_name, len(set(_text)))
for _name in SOLUTIONS:
    assert len(SOLUTIONS[_name]) == len(CIPHERS[_name]), _name

_POOL = (_clean(_read("zodiac-letters.txt"))
         + _clean(_read("english-background.txt")))

# --------------------------------------------------------------------------
# Language model: character 5-gram counts with stupid backoff


class FiveGram:
    """P(next char | up to four previous chars), stupid backoff 0.4."""

    def __init__(self, texts, orders=ORDERS, backoff=0.4):
        self.orders = orders
        self.backoff = backoff
        self.counts = {n: {} for n in range(1, orders + 1)}
        for text in texts:
            for n in range(1, orders + 1):
                table = self.counts[n]
                for i in range(n - 1, len(text)):
                    gram = text[i - n + 1:i + 1]
                    table[gram] = table.get(gram, 0) + 1
        # Total count per context, per order, for fast normalization.
        self.totals = {}
        for n in range(1, orders + 1):
            tot = {}
            for gram, c in self.counts[n].items():
                ctx = gram[:-1]
                tot[ctx] = tot.get(ctx, 0) + c
            self.totals[n] = tot
        self.char_total = sum(self.counts[1].values())

    def _prob(self, gram):
        prob = 1.0
        for n in range(len(gram), 0, -1):
            g = gram[-n:]
            hits = self.counts[n].get(g, 0)
            if hits:
                return prob * hits / self.totals[n][g[:-1]]
            prob *= self.backoff
        # Unseen even as a unigram cannot happen for cleaned A-Z input.
        return prob * 0.5 / self.char_total

    def logperchar(self, text):
        """Mean natural-log probability per character. Higher is better."""
        text = _clean(text)
        if not text:
            return -99.0
        total = 0.0
        for i in range(len(text)):
            start = max(0, i - self.orders + 1)
            total += math.log(self._prob(text[start:i + 1]))
        return total / len(text)


def _corpus():
    letters = _clean(_read("zodiac-letters.txt"))
    # Weight the killer's own words against the larger background text.
    return [letters] * 5 + [_POOL]


LM = FiveGram(_corpus())

# --------------------------------------------------------------------------
# Fixed synthetic suite: homophonic ciphers of the known Zodiac design


def _synth(length, seed):
    """One synthetic cipher: random plaintext, cyclic homophonic key."""
    rng = random.Random(seed)
    start = rng.randrange(0, len(_POOL) - length)
    plain = _POOL[start:start + length]
    alphabet = sorted(set(plain))
    rng.shuffle(alphabet)
    symbols = list("0123456789abcdefghijklmnopqrstuvwxyz!#$%&*+?@^~")
    rng.shuffle(symbols)
    counts = {c: plain.count(c) for c in alphabet}
    # Every letter gets one symbol; the most frequent third gets two more,
    # which mirrors the homophone counts of Z408 and Z340.
    key = {c: [symbols.pop()] for c in alphabet}
    busy = sorted(alphabet, key=lambda c: -counts[c])[:max(1, len(alphabet) // 3)]
    for c in busy:
        key[c].append(symbols.pop())
        if symbols:
            key[c].append(symbols.pop())
    out = [key[c][rng.randrange(len(key[c]))] for c in plain]
    return "".join(out), plain


SUITE_INSTANCES = []
_seed = 1000
for _len in SUITE:
    for _k in range(INSTANCES):
        SUITE_INSTANCES.append((f"synth{_len}_{_k}",) + _synth(_len, _seed))
        _seed += 1

# --------------------------------------------------------------------------
# Scoring


def _normalize(cands, cap=4096):
    out = []
    seen = set()
    for c in (_clean(x) for x in cands):
        if c and c not in seen:
            seen.add(c)
            out.append(c)
            if len(out) >= cap:
                break
    return out


MISSING = 64  # rank recorded when the truth is absent from the candidate list


def rank_of_truth(solver, cipher, true_plain, deadline):
    """Position of the true plaintext in the solver's ranked candidates."""
    cands = _normalize(solver(cipher, deadline))
    if not cands:
        return MISSING
    for pos, cand in enumerate(cands, start=1):
        if cand == true_plain:
            return pos
    return MISSING


def evaluate(solver):
    """Run the synthetic suite and the Z340 blind replay. Returns metrics."""
    start = time.time()
    suite_time = BUDGET * SYNTH_SHARE
    logs = []
    recovered = 0
    for idx, (name, cipher, plain) in enumerate(SUITE_INSTANCES):
        slice_end = start + suite_time * (idx + 1) / len(SUITE_INSTANCES)
        rank = rank_of_truth(solver, cipher, plain, slice_end)
        if rank == 1:
            recovered += 1
        logs.append(math.log2(rank))
    synth_score = sum(logs) / len(logs)

    replay_deadline = start + BUDGET
    cands = _normalize(solver(CIPHERS["z340.raw"], replay_deadline))
    true_score = LM.logperchar(SOLUTIONS["z340.raw"])
    if cands:
        best = max(LM.logperchar(c) for c in cands)
        z340_gap = true_score - best
        prefix = cands[0][:24]
    else:
        z340_gap = 9.9
        prefix = ""
    return {"synth_score": synth_score, "z340_gap": z340_gap,
            "recovered": recovered, "total": len(SUITE_INSTANCES),
            "prefix": prefix}


def report(solver):
    """Evaluate a solver and print the summary lines program.md greps."""
    m = evaluate(solver)
    print(f"synth_score: {m['synth_score']:.4f}")
    print(f"z340_gap: {m['z340_gap']:.4f}")
    print(f"recovered: {m['recovered']}/{m['total']}")
    print(f"best_340_prefix: {m['prefix']}")
