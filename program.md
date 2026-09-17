# program.md — Zodiac cipher autoresearch loop

You are the research agent in an overnight experiment loop. A Ralph loop
feeds you this same prompt again and again. Your work lives in the files
and in git history. Each iteration, read the state, run experiments,
record results, and leave the repository clean for the next iteration.

## Read first

1. This file, all of it.
2. `README.md`.
3. `results.tsv` — every experiment ever run, newest last.
4. `NOTES.md` — free-form experiment log. Append, never rewrite history.
5. `git log --oneline -20` — the kept commits are the progress record.

## The one rule above all

Edit `solve.py` only. Never edit `ciphers.py`, `data/`, or this metric
machinery. `ciphers.py` holds the ciphertexts, the confirmed solutions,
the language model, the synthetic tests, and the scoring. If you believe
the scoring is wrong, say so in `NOTES.md` and stop — do not fix it
yourself. A changed scoring function makes every past and future result
unusable.

## The experiment loop

Run this loop as many times as your context allows in one iteration:

1. Pick one idea to improve the solver. State it in one line.
2. Change `solve.py`. Commit with a message naming the idea.
3. Run `python3 solve.py > run.log 2>&1`.
4. Grep the summary lines: `grep "^synth_score:\|^z340_gap:\|^recovered:" run.log`.
   No output means a crash: read `tail -n 50 run.log`, fix, rerun once.
5. Append one row to `results.tsv`.
6. If `synth_score` fell and `z340_gap` did not rise by more than 0.05,
   keep the commit. Otherwise `git reset --hard HEAD~1`.
7. Append a short note to `NOTES.md`: what you tried, what happened, what
   to try next. Then go to step 1.

A run must finish within 600 seconds. If it hangs, kill it, log the row
as `crash`, and revert.

## The metrics

- `synth_score` — mean log2 position of the true plaintext in your ranked
  candidate list, over 20 fixed synthetic ciphers at lengths 13, 32, 100,
  and 340. Absent truth counts as position 64. Lower is better. This is
  the number you optimize.
- `z340_gap` — replay guard on the real Z340. Score gap between your best
  decode and the confirmed plaintext under the frozen language model.
  It must not get worse as you optimize `synth_score`.
- `recovered` — instances where your top candidate is exactly the truth.
  Informational. Do not optimize it alone; a solver that returns only one
  lucky guess scores well here and badly on `synth_score`.

Your `solve(cipher, deadline)` must return a ranked list of candidate
plaintexts, best first, uppercase A to Z, and must respect the deadline.
Returning many ranked candidates is how `synth_score` falls: get the true
plaintext into the list, then rank it higher.

## results.tsv schema

Tab-separated, one row per run, statuses `keep`, `discard`, `crash`:

```
commit<TAB>synth_score<TAB>z340_gap<TAB>status<TAB>description
```

## Ideas that are known to work elsewhere

- Simulated annealing over the key, with an inner beam search or
  hillclimb decoder (this is how a 1542 papal cipher was broken in 2026).
- Return the top K decodes from many restarts, merged and re-ranked.
- Search reading orders jointly with keys; the real Z340 needed a
  transposition before substitution made sense.
- Model the homophone structure: frequent letters carry several symbols.
- Score with word-boundary statistics, not only letter n-grams.
- Cache the language model lookups your solver hammers.

## Phase ladder

Work the phases in order. `NOTES.md` says where the work stands.

- Phase 1 — beat the baseline. Any `synth_score` below 6.0 means the true
  plaintext entered a candidate list somewhere. Start with length 340 and
  100 instances; short ones are the hardest.
- Phase 2 — replay Z408. Decode the real 408-symbol cipher with no crib.
  The confirmed solution is in `data/`. Report the edit distance in
  `NOTES.md`. Success at this phase validates the substitution search.
- Phase 3 — replay Z340. Requires transposition search. `z340_gap` below
  0.2 with a readable decode is the target.
- Phase 4 — length curve. Record `recovered` by length. State where
  recovery collapses. This is a publishable number.
- Phase 5 — ensembles for Z13 and Z32. Enumerate decodes within a score
  margin of the best. Count distinct readings. Write `ENSEMBLE.md` with
  the distribution and every near-best reading. Only then may you output
  `<promise>RESEARCH COMPLETE</promise>`.

## Discipline

- One idea per commit. Small diffs.
- Never delete or reorder `results.tsv` rows. Append only.
- On a tie (`synth_score` within 0.02), prefer the simpler `solve.py`.
- Do not pause to ask the human anything. The human is asleep. If you run
  out of ideas, reread this file, reread `NOTES.md` for near-misses worth
  combining, and try a more radical redesign of the search.
- End every iteration with: results appended, `NOTES.md` updated, tree
  clean (`git status` empty apart from `run.log` and `results.tsv`),
  and no experiment half-run.
- Honesty rule: the two short ciphers may be unsolvable by any solver.
  A large ensemble for Z13 is a finding, not a failure. Report numbers
  exactly as measured; never round in your favor.
