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

## Experiment 5 — suffix-block key beam (discarded)

Idea: beam over the KEY (not the prefix) for lengths 30 to 199.
Symbols assigned in frequency order; every contiguous suffix block of
every window scored once, when its last symbol is assigned; beam
width 4096 on the first 45 percent of the slice, SA fills the rest.

Run (budget 300): synth_score 4.2000 (tie), z340_gap 0.4745,
recovered 6/20. Discarded per the keep rule; reverted.

Diagnosis: the true key's beam state dies by step 5 of 31 at width
4096 (survives to step 4 even at 32768). The truth's early letters
are deeply uncompetitive while few blocks are scored — junk partials
flood the beam and width buys only one or two steps per 8x. Same
myopia wall as the position beam, one level up. Deterministic beams
are dead for length 100; three search families tried (SA restarts,
ILS, two beams) all fail the same four instances. Length-100 recovery
within 9 s stays an open problem.

Search attention now moves to Phase 3 (Z340 transposition replay),
which the ladder requires before the Phase 5 ensembles.

## Phase 3 findings — Z340 transposition structure (offline R&D)

No solve.py change yet; solver untouched since experiment 5. What the
offline work established:

- The Z340 replay window is 120 s (budget 300, synthetic share 0.6).
  z340_gap = truth logperchar minus the best logperchar over ALL
  returned candidates. Truth scores -2.0841 per char; the current
  solver's fluent-junk plateau sits near -2.49 (gap ~0.41).
- Reading-order family swept with deep 400k restarts: plain rows and
  near-rows variants dominate shallow sweeps; all clean column orders
  trail by 2+ nats. Rows-family scores are near-duplicates (row-local
  context intact), so that signal is not evidence of correctness.
- Alignment check against the confirmed solution (read-only): the
  true order class is the 9-9-2 row-band split with a (1,2)-decimation
  walk inside each 9-row band (row = k mod 9, col = 2k mod 17, torus
  wrap), tail two rows read straight. Segment 1 (rows 0-8) is EXACT
  under this order (0 key conflicts); the tail is near-exact (4); the
  middle band has 51 conflicts from Zodiac's encryption quirks
  (skipped cells along the readable text, a moved letter; matches the
  public 2020 solution writeups).
- Deep SA on the exact-class member still plateaus at gap +0.41: the
  key basin is narrow even with the right order, because the corpus
  does NOT contain the Z340 solution text (grep 0; unlike Z408 whose
  solution is in the corpus). The truth is not LM-favored the way
  suite truths are.
- Word-boundary scoring built from the corpus: segmentation DP over
  dictionary words of length >= 4 separates the truth from fluent
  junk by ~570 points (junk wins with short words allowed). Usable as
  a search guide, not yet wired in.
- Crib dragging with corpus n-grams: pattern-fit filtering is nearly
  uninformative at 63 symbols (733k survivors for the top 5000 zodiac
  10-grams; English-background phrases like SHERLOCKHOLMES poison
  greedy accumulation, 0/49 key agreement). The corpus does contain
  12-char runs of the solution ("INGTOCATCHME", "EVERYONEELSE..."),
  so a validator that fills unassigned symbols by frequency and
  scores the full decode under the LM should separate the true crib;
  that engineering is pending.

Next for phase 3: survivor validation by frequency-fill + full-decode
LM score, then extension of winning partial keys by annealing with
the crib frozen.

## Phase 4 — recovery by length (current solver, commit 6688ca3)

9 s slices, four fork workers, budget-300 run plus offline reruns.
Recovered = top candidate is exactly the true plaintext.

- Length 340: 5/5 recovered. Every crack lands at rank 1 (the truth
  is the LM optimum once found).
- Length 100: 1/5 recovered (synth100_1; restart luck, ~1-2 percent
  per restart chain). The other four: truth absent from all
  candidates. Best decodes trail the truth by ~0.7 nats per char and
  differ from the true key in 26-31 of ~30 symbols.
- Length 32: 0/5. On two of five instances the search finds decodes
  that OUTSCORE the truth (synth32_2: -46.8 vs -43.4; synth32_4:
  -51.5 vs -43.7): at 32 characters the truth is not the LM optimum,
  so score ranking alone cannot put it first even if found.
- Length 13: 0/5. Unicity distance; only ensemble methods apply.

Collapse point: recovery falls from 5/5 to 1/5 between 340 and 100
characters (about 10 versus 3 occurrences per symbol), and to 0/5 at
32. This matches the unicity-distance estimate of roughly 20 to 30
characters for homophonic substitution.

## Phase 5 — exact near-best ensembles for Z13 and Z32

No solve.py change; solver untouched. Offline tool (in /tmp) runs A*
over the position tree with a backward-DP admissible bound that
relaxes repeated-symbol constraints, so enumeration of every decode
within a margin of the optimum is exact.

- Z13: 2/9/52/1007 distinct readings at margins 1/2/4/8 nats. No
  dominant reading; best leads tenth by 2.1 nats (0.08 per char).
- Z32: 1/1/4/468 at the same margins. One dominant reading,
  3.44 nats clear; within 2 nats it is the only reading. Content is
  address-like ('SAN FRANC...', 'CALIF', 'PLEASE RUSH TO EDITOR',
  VALLEJO, SF CHRONICLE variants). Corpus check: 'Rush to Editor'
  appears 10 times in data/zodiac-letters.txt, so the model reward
  is domain phrasing, not independent evidence.
- Report written: ENSEMBLE.md (this commit). Report margin is 4
  nats; margin 8 given as counts plus top 20. Z13 margin 12 was
  attempted and abandoned (enumeration did not finish; margin 8 is
  the report ceiling).

Search attention returns to Phase 3 (z340_gap target under 0.2):
crib-drag survivor validation by frequency-fill plus full-decode LM
score, then annealing with winning cribs frozen.

## Post-loop R&D — Jev semantic judgments (offline, solver untouched)

The TypeSafe AI model Jev (a non-generating decision model; returns
typed judgments with probabilities) was tested as a corpus-free
coherence judge. All runs offline against saved pools and ensembles;
no change to solve.py, ciphers.py, or any metric. Raw outputs in
/tmp/jev_*.json; API key never stored in the repository.

Discrimination, five truth/junk pairs (synth32_2, synth32_4,
synth100_0, synth100_1, z340; four-level coherence Score):
truth 2.73 to 2.93 (top level in every case), junk 1.31 to 2.39.
Z340 pair: truth 2.93 versus our decode 1.50, where the frozen
5-gram gap is only 0.48 — the semantic separation is about three
times wider and does not depend on the corpus containing the
solution. Measured noise floor: one identical string (synth100_1,
truth found at rank 1) scored 2.87 and 2.39 in one request, so
deltas under ~0.5 are not decisive.

Ensemble re-rank of the exact margin-8 enumerations:

- Z13, 1007 readings, name-ness Noul under the 'My name is —'
  context: maximum 0.48, median 0.20, best-to-50th margin 0.16.
  The LM-best reading falls to Jev rank 16. Independent
  confirmation of the Phase 5 finding: no reading stands out, by
  letter statistics or by semantic judgment.
- Z32, 468 readings, reference/instruction Noul: the San
  Francisco / Chronicle / rush-to-editor family (288 readings)
  reaches 0.81; the best non-family reading reaches 0.67
  (HEZODIACSPEAKINGINEWYEARPHOTOELE). The degenerate repetitive
  reading the LM ranks 4 (EACHVBATVBAT...SANFRA) drops to 0.40.
  Confound, stated plainly: Jev's training data plausibly includes
  the public Zodiac literature, so its preference for the family
  is recognition, not independent evidence.

Negative results, reported as measured:

- synth_score simulation (Jev re-rank of all 64 candidates on all
  20 suite instances): 4.2000 to 4.2000, no change. All six
  in-list truths already sit at rank 1; ordering cannot help the
  14 absent ones. Jev inside solve.py has no metric value in the
  current regime.
- Short strings defeat semantic judgment too: top junk decodes of
  the 13-char synthetics score 0.84 to 0.94 on the meaningfulness
  Noul. Coherence discrimination grows with length.
- Z340 pools under Jev: plain order max 2.14, reordered (the
  9-9-2 decimation) max 2.31, both far under the truth's 2.93.
  No false positives: the arbiter reports no readable decode, and
  none exists in those pools. The Z340 blocker is search, not
  selection.

Where Jev could still pay off: Jev-guided search on the reordered
Z340 (perturb the top-coherence pool members, re-anneal, re-judge;
the frozen LM cannot reward the truth because the corpus lacks it,
but a coherence judge can), and crib-survivor validation where
n-gram scoring is poisoned by background phrases.
