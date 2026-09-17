# Experiment log

Append only. One block per experiment batch.

## Baseline (human setup, 2026-09-17)

Committed stub: random restarts, frequency-seeded key, greedy single-symbol
hillclimb, one candidate returned. ZODIAC_BUDGET=30 smoke run:
synth_score 6.0000, z340_gap 0.7911, recovered 0/20. The truth never
entered a candidate list. Next agent: return top-K candidates from many
restarts, then attack length-100 and length-340 instances first.

## Experiment 1 — incremental 5-gram SA (commit 495f0d1)

Idea: compile the frozen LM into int-keyed tables, score SA moves
incrementally over only the windows touching the changed symbol (cached
per-position gram codes), pool distinct decodes across restarts, return
top 64 ranked by the same LM. ~69k applies/s at length 340.

Run (budget 300): synth_score 5.1000, z340_gap 0.4745, recovered 3/20.
Kept. Length 340 cracks 4/5 at rank 1 in 9 s (one run had 3/5; restart
timing variance). Length 100 and 32 fail completely: the truth is NOT in
any candidate list.

Diagnosis (offline checks): at length 100 the truth outscores my best
decode by ~0.65 nats/char (-1.42 vs -2.08), so the truth IS the optimum
and the search is what fails. Temperature sweeps at length 100
(t0 0.6..5, iters 60k..300k) all score 6.0 — key-move SA cannot hold the
basin when symbols average ~3 occurrences. The same sweep at 340 was
never needed; signal per symbol is strong there.

Next: prefix beam search over symbol assignments. States are
(score, prefix, last-4 code); the assignment of a symbol is just the
prefix letter at its last occurrence, so no key storage is needed.
Dedupe states by (last-4, letters at future-relevant positions) with
itemgetter keys; that is exact Viterbi-style pruning for the best
decode. The truth's prefix should lead the beam at 100/32; for 13 it
gives the honest ensemble Phase 5 needs. Keep SA as filler for leftover
time and as the long-cipher engine.
