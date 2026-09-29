# zodiac-autoresearch

An autoresearch loop (Karpathy pattern) pointed at the unsolved Zodiac
ciphers. The method borrows from Simon Klee's 2026 break of a 1542 papal
cipher: joint search over key and reading order, a domain-matched
language model, and controls that decide what counts as true.

## Files

| File | Role | Who edits |
| --- | --- | --- |
| `solve.py` | The solver under test | Agent, freely |
| `ciphers.py` | Ciphertexts, solutions, language model, synthetic suite, scoring | Nobody, frozen |
| `data/` | Cipher transcriptions, confirmed solutions, corpus | Nobody, frozen |
| `program.md` | Agent instructions | Human only |
| `results.tsv` | Every run ever made | Agent, append only |
| `NOTES.md` | Experiment log | Agent, append only |

## Run one experiment

```
python3 solve.py
```

Prints `synth_score`, `z340_gap`, and `recovered`. One run costs five
minutes at the default budget; `ZODIAC_BUDGET=30 python3 solve.py` for a
quick check. Baseline at commit time: `synth_score 6.0`, `z340_gap 0.79`.

## Run the loop with Ralph

From this directory, in Claude Code:

```
/ralph-loop "Read zodiac-autoresearch/program.md and follow it exactly.
Continue the experiment loop from the current state. Do not ask for
permission. Output <promise>RESEARCH COMPLETE</promise> only when the
Phase 5 report ENSEMBLE.md exists." --max-iterations 40
```

Or from inside the directory, with `zodiac-autoresearch/` dropped from
the path. Stop early with `/cancel-ralph`. Each iteration is one pass of
the loop in `program.md`; state survives in git, `results.tsv`, and
`NOTES.md`.

## Why the two short ciphers may stay unsolved

Z13 has 13 characters and Z32 has 32. Both sit at or below the unicity
distance of a homophonic cipher (roughly 20 to 30 characters). The loop's
success criterion for them is a measured ensemble of near-best decodes,
not a name. See `program.md`, Phase 5, and `../zodiac-autoresearch-plan.md`.

## Data integrity

`ciphers.py` asserts the published symbol counts on import: Z340 340/63,
Z408 408/54, Z13 13/8, Z32 32/29, and the two solution lengths. Provenance
and cross-checks are documented in `data/sources.md`.
