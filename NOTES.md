# Experiment log

Append only. One block per experiment batch.

## Baseline (human setup, 2026-09-17)

Committed stub: random restarts, frequency-seeded key, greedy single-symbol
hillclimb, one candidate returned. ZODIAC_BUDGET=30 smoke run:
synth_score 6.0000, z340_gap 0.7911, recovered 0/20. The truth never
entered a candidate list. Next agent: return top-K candidates from many
restarts, then attack length-100 and length-340 instances first.
