"""Solver under test. THE AGENT EDITS THIS FILE ONLY.

Baseline: random restarts of a frequency-seeded homophonic key, improved by
greedy single-symbol changes, scored by the frozen language model. It is
weak on purpose. Replace or extend it; keep the interface.

Required interface (called by ciphers.py):

    def solve(cipher: str, deadline: float) -> list[str]

Return a list of candidate plaintexts, best first, uppercase A to Z.
Respect the deadline (a float from time.time()). Never print to stdout.
"""

import random
import time

import ciphers

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Rough English letter frequencies, used only to seed random keys.
FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def _decode(cipher, key):
    return "".join(key[s] for s in cipher)


def _hillclimb(cipher, rng, deadline, rounds=20000):
    symbols = sorted(set(cipher))
    # Seed: frequent cipher symbols get frequent letters, with noise.
    by_count = sorted(symbols, key=lambda s: (-cipher.count(s), s))
    key = {}
    pool = list(FREQ * 3)  # repeat so homophones stay frequency-plausible
    for s in by_count:
        key[s] = pool.pop(rng.randrange(len(pool))) if pool else rng.choice(LETTERS)
    best_score = ciphers.LM.logperchar(_decode(cipher, key))
    best_key = dict(key)
    for _ in range(rounds):
        if time.time() >= deadline:
            break
        s = rng.choice(symbols)
        old = key[s]
        key[s] = rng.choice(LETTERS)
        score = ciphers.LM.logperchar(_decode(cipher, key))
        if score > best_score:
            best_score = score
            best_key = dict(key)
        else:
            key[s] = old
    return best_score, _decode(cipher, best_key)


def solve(cipher, deadline):
    """Return candidate plaintexts, best first."""
    rng = random.Random(0)
    best = None
    best_score = float("-inf")
    while time.time() < deadline - 0.05:
        score, text = _hillclimb(cipher, rng, deadline)
        if score > best_score:
            best_score, best = score, text
    return [best] if best else [cipher.translate(str.maketrans(
        {s: LETTERS[i % 26] for i, s in enumerate(sorted(set(cipher)))}))]


if __name__ == "__main__":
    ciphers.report(solve)
