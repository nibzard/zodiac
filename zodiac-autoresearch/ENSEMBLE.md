# ENSEMBLE.md — near-best decode ensembles for Z13 and Z32

Phase 5 report. Method: exact A* enumeration of the position tree
under the frozen five-gram language model, with repeated-symbol
constraints enforced. Every future n-gram term is non-positive, and
a backward dynamic program over (position, last four letters) gives
an admissible upper bound on the achievable future score, so the
first complete decode found is the global optimum and the search
stops only when no remaining state can reach within the margin of
the best. The enumeration is therefore exact for each stated
margin: the listed sets are complete, not samples.

Scores: 'internal' is the solver's folded laddered logprob (carries
a fixed per-position offset relative to the frozen model);
'per char' is LM.logperchar of the frozen model, the same measure
the harness uses. Neither cipher has a confirmed solution, so these
are model-relative ensembles, not accuracy measurements.

## Z13 (13 characters, 8 symbols)

Distinct readings within a total-score margin of the best:

| Margin (nats) | Distinct readings |
| --- | --- |
| 1 | 2 |
| 2 | 9 |
| 4 | 52 |
| 8 | 1007 |

Best internal score: -25.80. All 52 readings within
4 nats (the report margin), best first:

| Rank | Internal | Per char | Reading |
| --- | --- | --- | --- |
| 1 | -25.80 | -1.2794 | OGICALANATION |
| 2 | -26.43 | -1.3279 | SSIBILITISIST |
| 3 | -27.09 | -1.3791 | SOUGHTHEHOUSE |
| 4 | -27.12 | -1.3812 | THEREWEWERETW |
| 5 | -27.38 | -1.4016 | ULDBEDEPENDUP |
| 6 | -27.48 | -1.4088 | SHAKEHEREWASR |
| 7 | -27.62 | -1.4200 | ENTWEWERESTER |
| 8 | -27.63 | -1.4204 | RTODIVISITORS |
| 9 | -27.70 | -1.4257 | ONTHEDECEPTOC |
| 10 | -27.86 | -1.3679 | INTHEDETECTIT |
| 11 | -28.05 | -1.4530 | RVETOGOTOVERT |
| 12 | -28.11 | -1.4577 | ERMANANDNAMED |
| 13 | -28.12 | -1.4579 | NCESAYAWAKENW |
| 14 | -28.28 | -1.4707 | AVETOGOTOBEAT |
| 15 | -28.32 | -1.4734 | RRESTATETHERE |
| 16 | -28.45 | -1.4833 | HATWEWEREDTHR |
| 17 | -28.48 | -1.4858 | AKEHEREWEREAW |
| 18 | -28.83 | -1.5126 | OFTHEMERESTOR |
| 19 | -28.83 | -1.4422 | ANSWEREBELSAB |
| 20 | -28.89 | -1.5175 | NEACTITSTRANS |
| 21 | -28.93 | -1.5205 | RPASSISTSTART |
| 22 | -28.94 | -1.5209 | THESTATETHETE |
| 23 | -29.03 | -1.5280 | ETHWEWERETHER |
| 24 | -29.06 | -1.5308 | MURDEREREARMR |
| 25 | -29.08 | -1.5324 | OPOFEVEREDOOR |
| 26 | -29.12 | -1.5349 | RIGHTITATAGRA |
| 27 | -29.16 | -1.5379 | ACKTODOTOOKAT |
| 28 | -29.19 | -1.5403 | OUNDITITISNOT |
| 29 | -29.20 | -1.5415 | THEREWEHERETH |
| 30 | -29.20 | -1.5417 | NSIBILITISINT |
| 31 | -29.24 | -1.5441 | IVETOGOTONEIT |
| 32 | -29.27 | -1.5469 | NGOUTITATIONA |
| 33 | -29.34 | -1.5517 | NMOSTITUTIONU |
| 34 | -29.36 | -1.5533 | HITENINANOTHA |
| 35 | -29.38 | -1.5549 | FNOBILITISOFT |
| 36 | -29.41 | -1.5574 | DTODIVIDINODD |
| 37 | -29.45 | -1.5606 | OUWHEREWETWOW |
| 38 | -29.47 | -1.4915 | ATHISISTSWHAT |
| 39 | -29.48 | -1.5632 | TOTHEREPEATTP |
| 40 | -29.50 | -1.5647 | NMOREDETECONT |
| 41 | -29.62 | -1.5028 | INTOEFERENTIR |
| 42 | -29.65 | -1.5759 | CHESTATETHECE |
| 43 | -29.65 | -1.5760 | DHAVENEVERADV |
| 44 | -29.65 | -1.5760 | AFEWEWERENEAR |
| 45 | -29.66 | -1.5763 | USSEEHEREASUR |
| 46 | -29.69 | -1.5788 | SVISIBILITISL |
| 47 | -29.71 | -1.5806 | AVETOGOTONEAT |
| 48 | -29.73 | -1.5819 | RCONSISTSPORT |
| 49 | -29.75 | -1.5840 | ICHWEWERETHIR |
| 50 | -29.76 | -1.5847 | OFTHESEMENTOM |
| 51 | -29.79 | -1.5866 | EITWASALANTEL |
| 52 | -29.79 | -1.5869 | ATEWAYANADEAN |

Top 20 of the 1007 readings within 8 nats:

| Rank | Internal | Per char | Reading |
| --- | --- | --- | --- |
| 1 | -25.80 | -1.2794 | OGICALANATION |
| 2 | -26.43 | -1.3279 | SSIBILITISIST |
| 3 | -27.09 | -1.3791 | SOUGHTHEHOUSE |
| 4 | -27.12 | -1.3812 | THEREWEWERETW |
| 5 | -27.38 | -1.4016 | ULDBEDEPENDUP |
| 6 | -27.48 | -1.4088 | SHAKEHEREWASR |
| 7 | -27.62 | -1.4200 | ENTWEWERESTER |
| 8 | -27.63 | -1.4204 | RTODIVISITORS |
| 9 | -27.70 | -1.4257 | ONTHEDECEPTOC |
| 10 | -27.86 | -1.3679 | INTHEDETECTIT |
| 11 | -28.05 | -1.4530 | RVETOGOTOVERT |
| 12 | -28.11 | -1.4577 | ERMANANDNAMED |
| 13 | -28.12 | -1.4579 | NCESAYAWAKENW |
| 14 | -28.28 | -1.4707 | AVETOGOTOBEAT |
| 15 | -28.32 | -1.4734 | RRESTATETHERE |
| 16 | -28.45 | -1.4833 | HATWEWEREDTHR |
| 17 | -28.48 | -1.4858 | AKEHEREWEREAW |
| 18 | -28.83 | -1.5126 | OFTHEMERESTOR |
| 19 | -28.83 | -1.4422 | ANSWEREBELSAB |
| 20 | -28.89 | -1.5175 | NEACTITSTRANS |

Reading: the near-best set grows by a factor of 4.5, 5.8 and 19.4
per 2-nat step, accelerating. No reading stands out; the best leads
the tenth by 2.1 nats internal (0.08 per char). Internal order and
per-char order can swap by a place or two (rank 10 has the better
per-char value than rank 4) because the folded ladder charges
backoffs as if every lookup started at order 5, and how far a
lookup ladders depends on the decode. With 8 symbols over 13
characters the cipher sits far below the unicity distance, and the
ensemble confirms it: under this model Z13 admits a wide band of
equally plausible readings, and any claimed solution needs
information beyond letter statistics.

## Z32 (32 characters, 29 symbols)

Distinct readings within a total-score margin of the best:

| Margin (nats) | Distinct readings |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 4 | 4 |
| 8 | 468 |

The four readings within 4 nats (the report margin), best first:

| Rank | Internal | Per char | Reading |
| --- | --- | --- | --- |
| 1 | -23.03 | -0.4332 | ORSANFRANCALIFPLEASERUSHTOEDITOR |
| 2 | -26.47 | -0.5409 | REDITORVALLEJOCALIFPLEASERUSHTOE |
| 3 | -26.78 | -0.5505 | EARPHOTOELECTORSFCHRONICLESANFRA |
| 4 | -26.79 | -0.5510 | EACHVBATVBATVBATVBATBUSGOESANFRA |

Top 20 of the 468 readings within 8 nats:

| Rank | Internal | Per char | Reading |
| --- | --- | --- | --- |
| 1 | -23.03 | -0.4332 | ORSANFRANCALIFPLEASERUSHTOEDITOR |
| 2 | -26.47 | -0.5409 | REDITORVALLEJOCALIFPLEASERUSHTOE |
| 3 | -26.78 | -0.5505 | EARPHOTOELECTORSFCHRONICLESANFRA |
| 4 | -26.79 | -0.5510 | EACHVBATVBATVBATVBATBUSGOESANFRA |
| 5 | -27.18 | -0.5630 | ONSANFRANCALIFPLEASERUSHTOEDITIN |
| 6 | -27.38 | -0.5121 | SANFRANCISCOCALIFPLEASERUSHTOEDA |
| 7 | -27.48 | -0.5723 | ORSANFRANCALIFPLEASERUSHTOEDITFR |
| 8 | -27.53 | -0.5454 | SANFRANCISCOCALIFPLEASERUSHTOTRA |
| 9 | -27.59 | -0.5759 | EACHVBATVBATVBATVBATBUSGOESBANDA |
| 10 | -27.60 | -0.5474 | SICKIAMAFRANCALIFPLEASERUSHTOEDI |
| 11 | -27.65 | -0.5776 | ONSANFRANCALIFPLEASERUSHTOEDITAN |
| 12 | -27.76 | -0.5812 | ORSANFRANCALIFPLEASERUSHTOEDITBR |
| 13 | -27.83 | -0.5833 | ONSANFRANCALIFPLEASERUSHTOEDITON |
| 14 | -27.86 | -0.5844 | ANCISCOCHRONICLEIWANTYOUHAVEBEEN |
| 15 | -27.90 | -0.5854 | SANFRANCISCOCALIFPLEASERUSHTOBEA |
| 16 | -28.00 | -0.5888 | REDISCOCHRONICLESANFRANCHRONICLE |
| 17 | -28.02 | -0.5891 | ROFTHEIRPLEASERUSHTOEDITORSFCHRO |
| 18 | -28.07 | -0.5622 | ORSANFRANCALIFPLEASERUSHTOELECTR |
| 19 | -28.14 | -0.5931 | SANFRANCISCOCALIFPLEASERUSHTOSTA |
| 20 | -28.16 | -0.5938 | INEXCEPTOCTPLEASERUSHTOEDITORSAN |

Reading: Z32 behaves oppositely to Z13. The best decode leads the
runner-up by 3.44 nats, and within 2 nats it is the ONLY reading.
The dominant decode reads '...SAN FRANC[ISCO]... CALIF[ORNIA]...
PLEASE RUSH TO EDITOR...' in its rotation, and several of the next
readings are cyclic rotations of the same phrase or variants
involving VALLEJO, the SF Chronicle and 'PHOTOELECT...'. This
overlaps the content of long-published unconfirmed proposals
(San Francisco area locations and newspaper addressing). Note the
model bias: the corpus contains 'Rush to Editor' ten times,
'San Francisco' eight times, 'Vallejo' ten times and 'Chronicle'
nineteen times (data/zodiac-letters.txt), so domain phrasing is
exactly what the model rewards. That agreement is between the
model and a public hypothesis, not a confirmation.

## Findings

- Z13: wide ensemble, no dominant reading. Ambiguity is a property
  of the cipher, not of the search (enumeration is exact).
- Z32: one dominant reading, 3.44 nats clear of the field, with
  rotations of the same content filling the near-best band.
- The two ciphers bracket the unicity distance from both sides:
  at 13 characters the near-best set explodes; at 32 characters
  with 29 symbols the model already commits to one reading.
- Exact enumeration code lives outside the repository (a /tmp
  tool); the solver itself is unchanged.
