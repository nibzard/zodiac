# Attack plan for the Zodiac ciphers

This plan combines two sources:

- `farnese-letter.md` — Simon Klee's recovery of a 1542 papal cipher.
- `/home/agent/clojure-llm/autoresearch-principles.md` — the distilled
  Karpathy `autoresearch` pattern.

Written 17 September 2026. Targets: Z13 and Z32, the two unsolved ciphers.

## Part 1: what the Farnese letter teaches

The Farnese solve is a blueprint. Six lessons transfer to the Zodiac case.

1. **Search the key and the reading together.** An outer simulated-annealing
   loop changed letter-to-code assignments. An inner beam search found the
   best way to cut and read the digits. Neither works alone. For the Zodiac
   ciphers, the "reading" is not code length. Every symbol maps to one
   character. The unknown reading is the *order*: row, column, diagonal, or
   decimation. The Z340 solve came from exactly this dimension. So the
   search space is `key × reading order`, searched jointly.
2. **Score with a domain-matched language model.** The Farnese model trained
   on 1540s Italian, normalized to the clerk's spelling habits (`tute`,
   `v` folded into `u`). The Zodiac model must train on the killer's own
   words: his confirmed letters plus the two solved plaintexts. Normalize
   the same way he wrote: ignore case, ignore spaces, keep his misspellings
   probable. Blend with a large period American-English corpus, because the
   in-domain corpus is only a few thousand words. Use back-off smoothing,
   as with the Farnese five-gram model.
3. **Starve the search of freedom.** The first Farnese runs had optional
   word codes and several nulls. The search used them to explain away
   digits and produced garbage with high scores. The fix was to tighten:
   one code per letter, at most one null, no word codes. Lesson for Z13
   and Z32: every added degree of freedom (nulls, homophones, wildcards,
   multiple reading rules) multiplies the number of plausible readings.
   Start with the tightest design that can express the known Z408 and Z340
   constructions.
4. **Let controls decide what is true.** The Farnese checks were: solve each
   half of the text separately and compare keys; solve synthetic ciphers
   built with invented keys; solve shuffled ciphertext as a floor. The same
   controls, run at lengths 13 and 32, turn "unsolvable" from an opinion
   into a measurement.
5. **Check the source document.** Several Farnese readings died on the
   manuscript page. A nearest-neighbor glyph classifier compared each
   disputed digit with the clerk's other forms. The Zodiac ciphers have
   known transcription disputes. The same check applies: classify each Z13
   and Z32 symbol against the symbol inventory of Z408 and Z340, written by
   the same hand.
6. **Report status with care.** The Farnese article separates a stable key
   from an unverified text. Any Zodiac output must do the same: state what
   is measured, what is assumed, and what is conjecture.

## Part 2: the hard limit

The Farnese key search worked on 6,331 digits. Split the letter in half and
3,165 digits per half still recovered the same key. The signal survived
division because the text was long.

Z13 has 13 characters. Z32 has 32. A homophonic cipher over 26 letters needs
roughly 20 to 30 characters before one solution separates from the crowd.
That is the unicity distance. Both ciphers sit at or below it.

So the plan does not promise a name or a location. It promises three
measured outputs:

- A solver, validated by replaying Z408 and Z340 blind.
- A recovery-versus-length curve from synthetic ciphers. This shows exactly
  where recovery collapses.
- The full ensemble of high-scoring decodes for Z13 and Z32, with a count of
  how many distinct readings sit within noise of the best.

If the ensemble is large, the honest result is a quantified impossibility
statement. That is still a result. The Farnese epistemology demands it.

## Part 3: the autoresearch wrapper

Karpathy's pattern gives the overnight loop that builds the solver. The
nouns change; the invariants do not.

| autoresearch (pretraining) | This project |
| --- | --- |
| `train.py` (agent edits) | `solve.py`: key search plus decoder |
| `prepare.py` (frozen) | `ciphers.py`: transcriptions, language model, synthetic generator, scoring |
| `val_bpb` | `synth_score`: mean log-rank of the true plaintext across synthetic tests (lower is better) |
| 5-minute training budget | 5-minute search budget per run |
| VRAM soft cap | replay guard: Z340 blind-replay gap must not worsen |
| `results.tsv` | same schema: `commit`, `synth_score`, `z340_gap`, `status`, `description` |

### Why `synth_score` is the right metric

The agent may rewrite the whole solver. The metric must ignore solver
internals and measure one thing: does the true plaintext outrank the false
ones? Log-rank is continuous, so it improves even when exact recovery is
impossible at length 13. It is invariant to everything the agent is allowed
to change. It cannot be gamed without also gaming the science.

### Repo layout

```
zodiac-autoresearch/
├── ciphers.py     # FROZEN: transcriptions, language model, synthetic
│                  # generator, scoring, search budget
├── solve.py       # agent edits this file only
├── program.md     # agent instructions (human edits)
├── results.tsv    # untracked log of every run
└── README.md
```

### Loop protocol

1. Read `program.md`, `ciphers.py`, and the current `solve.py`.
2. Change `solve.py` with one experimental idea. Commit.
3. Run `uv run solve.py > run.log 2>&1`.
4. Grep `^synth_score:\|^z340_gap:` from `run.log`. If empty, inspect the
   log tail and fix the crash.
5. Append a row to `results.tsv`.
6. If `synth_score` improved and `z340_gap` did not worsen, keep the commit.
   Otherwise reset to the previous commit.
7. Repeat until interrupted. Do not stop to ask.

### program.md draft

```markdown
# program.md — Zodiac cipher solver loop

## Setup
- Work on branch `autoresearch/<tag>`.
- Read `program.md`, `ciphers.py`, `solve.py`. The repo is small.
- You edit `solve.py` only. Never edit `ciphers.py`. It holds the
  transcriptions, the language model, the synthetic generator, and the
  scoring. If you think the scoring is wrong, stop and say so in the run
  description instead of changing it.
- First run of a session is a no-edit baseline. It fills the first
  `results.tsv` row.

## What you may change
- Search algorithm, proposal moves, annealing schedule, beam width,
  reading-order generator, initialization, restarts, priors over keys.
- Anything inside `solve.py`.

## What you may not change
- `ciphers.py`, the metric, the time budget, the test instances.

## Output format
- The run must print exactly these lines to stdout:
  `synth_score: <float>`  (mean log-rank of true plaintext, lower better)
  `z340_gap: <float>`     (blind replay score gap, lower better)

## Logging
- Append to `results.tsv` (untracked), tab-separated:
  commit, synth_score, z340_gap, status, description
- Status is one of: keep, discard, crash.

## Loop
- Edit, commit, run, grep, log, keep or revert. Redirect output; never tee.
- A run over 10 minutes is a failure. Kill it and log it as crash.
- Tie-breaker: on near-equal `synth_score`, prefer the simpler `solve.py`.

## Never stop
- Once the loop begins, do not pause to ask the human. If ideas run out,
  re-read `ciphers.py`, combine past near-misses, or try a more radical
  search design. Run until interrupted.

## Crash policy
- Fix simple crashes (syntax, imports) and retry once.
- Log repeated crashes and move on to a different idea.
```

## Part 4: phases

Phase order follows the Farnese discipline: replay the known before
attacking the unknown.

- **Phase 0 — Baseline.** Run the stub solver. Confirm the harness works.
- **Phase 1 — Z408 replay.** Recover the 1969 plaintext from the 408
  ciphertext alone, with no crib. This validates the substitution search.
- **Phase 2 — Z340 replay.** Recover the 2020 plaintext blind. This forces
  the solver to invent the transposition search: reading orders,
  decimations, segment splits. The target is the known solution without
  peeking. `z340_gap` becomes the replay guard from here on.
- **Phase 3 — Length curve.** Generate synthetic ciphers from Zodiac-style
  plaintext with random keys at lengths 13, 32, 100, 200, and 340. Measure
  recovery and log-rank at each length. Find where the curve collapses.
  This phase produces the first publishable number.
- **Phase 4 — Ensembles for Z13 and Z32.** Run the tightened solver on the
  real ciphers. Keep every decode within a fixed score margin of the best.
  Count distinct readings. Report the distribution, not a favorite.
- **Phase 5 — External constraints.** The only route past the unicity limit
  is information from outside the ciphertext:
  - Z13: constrain decodes to candidate name lists (suspects, aliases,
    hoaxes such as "Alfred E. Neuman"). Report each candidate's rank and
    the score margin, as likelihood ratios against the ensemble floor.
  - Z32: require decodes consistent with the map hint — a radian value and
    an inch count from Mount Diablo, with zero set to magnetic north. Look
    up the 1970 declination for the Bay Area. Each candidate angle maps to
    a checkable point on the Phillips 66 map. This is a semantic filter no
    32-character text can satisfy by accident.
  - Glyph check: classify every Z13 and Z32 symbol against the Z408 and
    Z340 inventories with a nearest-neighbor classifier, as the Farnese
    work did with digits. A single misread symbol changes the whole
    hypothesis space at this length.

## Part 5: success criteria

| Outcome | Meaning |
| --- | --- |
| Z340 blind replay succeeds | The solver machinery is sound |
| Length curve published | The information limit is measured, not assumed |
| Z13 ensemble small and stable | A candidate reading deserves external checks |
| Z13 ensemble large | Z13 is a hoax or too short; say so with numbers |
| Z32 decode consistent with the map | The one result that could count as a solve |

The final report copies the Farnese status section: separate the stable
parts from the unverified parts, and state who has confirmed what. No one
has confirmed anything yet.
