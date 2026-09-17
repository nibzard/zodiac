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

## Experiment 3 — parallel restart pool (commit 6688ca3)

Idea: fork-pool of four workers, each running independent SA restart
chains inside the same time slice; merge their decode pools.

Run (budget 300): synth_score 4.2000, z340_gap 0.4745 (unchanged),
recovered 6/20. Kept. Per length (9 s slices): 340 → 5/5 rank 1,
100 → 1/5, 32 and 13 → 0/5. All non-hits are absent from the list
(synth_score 4.2 = 14 absent x 6 / 20 exactly).

Bug found on the way: the rewritten greedy swap polish reverted with
apply(s1, key[s1]) AFTER the swap had already written key[s1] — a
no-op. Every rejected swap stayed applied and the bookkept score
drifted from the real key, so polished output scored -4.3 nats/char.
Capturing the letters before the move fixes it; 80k-iteration
restarts then crack synth340_0 in 2/10 trials, matching the old
closure code.

Parameters: shallow restarts everywhere (80k/60k/40k/25k by length);
deep 400k chains only for >=50 symbols and >=400 characters (Z408
class), where they reach edit distance 6 and shallow ones stall.

Phase 2 preview (Z408 replay, offline, no crib): deep 400k-iteration
restarts decode the real 408-symbol cipher to edit distance 6/408
against the confirmed solution in data/ (-1.037 vs -0.850 nats/char).
80k restarts stall near edit distance 262. Substitution search is
validated at full Zodiac key sizes.

Next: length 100 is the live gap (4 of 5 instances absent). Plan:
iterated local search — perturb the best pooled key (randomize a
fraction of symbols) and re-anneal from it at low temperature, so
late restarts start inside the basin instead of from scratch.

## Experiment 4 — iterated local search (commit 4c118a3, discarded)

Idea: after a first restart, re-anneal from the worker's best key
with a third of its symbols randomized, at low start temperature.

Run (budget 300): synth_score 5.1000 (worse than 4.2000), z340_gap
0.4788, recovered 3/20. Discarded, reverted.

Diagnosis: length 340 lost its 5/5 — crack rate there comes from
restart diversity (each 80k restart ~20% independent chance), and
ILS chains collapse onto one attractor. Length 100 did not improve
either: offline, the four failing instances stay absent and the best
decode still trails the truth by ~0.7 nats/char.

Measurement that explains the length-100 wall: the polished optimum
of synth100_0 differs from the true key in 29 of 31 symbols while
scoring only 0.7 nats/char worse. The fluent-junk plateau is wide;
the truth is an isolated deep point. Local moves and perturbations
cannot cross it. Next: a fundamentally different search — beam over
KEYS, symbols ordered by frequency, partial decode scored only on
windows whose five positions are all assigned (each window scored
exactly once, when its rarest symbol is assigned).
