# Zodiac killer cipher messages

Research report. All facts checked on 17 September 2026.

The Zodiac killer murdered five known victims in northern California between
December 1968 and October 1969. From July 1969 he sent taunting letters to
Bay Area newspapers. Four letters contained ciphers. Two are solved. Two are
not.

## Summary

| Cipher | Mailed | Characters | Distinct symbols | Status |
| --- | --- | --- | --- | --- |
| Z408 | 31 July 1969 | 408 | 54 | Solved August 1969 |
| Z340 | 8 November 1969 | 340 | 63 | Solved December 2020 |
| Z13 | 20 April 1970 | 13 | 8 | Unsolved |
| Z32 | 26 June 1970 | 32 | about 10 | Unsolved |

In this table, "solved" means that the Federal Bureau of Investigation (FBI)
verified the decryption, or that the solution is accepted without dispute.

## Z408: the first cipher

On 31 July 1969 the killer mailed three letters. Each went to a different
newspaper: the *San Francisco Chronicle*, the *San Francisco Examiner*, and
the *Vallejo Times-Herald*. Each letter held one third of a 408-character
cipher. The writer claimed the cipher held his identity. He threatened more
killings unless the papers printed it.

The cipher is a homophonic substitution. Each plaintext letter can map to
several cipher symbols. This defeats simple frequency counts. Z408 uses 54
distinct symbols.

Donald and Bettye Harden of Salinas solved it in early August 1969. Neither
was a cryptologist. Bettye Harden guessed that the message would contain the
word "kill". That guess gave them a start. Word patterns finished the work.

The plaintext opens: "I like killing people because it is so much fun." It
calls man "the most dangerous anamal [sic] of all". It says the victims
"will become my slaves" in the afterlife. The writer refuses to give his
name. He wants to keep collecting slaves. The text echoes Richard
Connell's story "The Most Dangerous Game" (1924).

The final 18 characters decode to gibberish: `EBEORIETEMETHHPITI`. Most
researchers treat them as filler. The killer needed 18 more symbols to
complete the three equal parts. The name claim was a hoax.

## Z340: the second cipher

On 8 November 1969 the killer mailed a greeting card to the *Chronicle*.
The card held a cipher of 340 characters, set in 17 columns and 20 rows.
It uses 63 distinct symbols. Zodiac demanded front-page publication.

### Why it resisted attack

Plain homophonic solvers failed for 51 years. The reason: the cipher has two
layers. The killer first substituted symbols for letters. He then wrote the
symbols into the grid in an unusual order. Solvers who read the grid row by
row saw shuffled text. The message stayed hidden.

Two encoding errors made the text harder still. The killer misaligned parts
of his own scheme.

### How it fell

Three men solved it: David Oranchak (United States, software engineer),
Sam Blake (Australia, mathematician), and Jarl Van Eycke (Belgium,
programmer). Van Eycke wrote the solver AZdecrypt. Oranchak ran the
zodiackillerciphers.com project and the "Let's Crack Zodiac" video series.

The decisive steps:

1. Blake generated about 650,000 candidate rearrangements of the grid. He
   used Mathematica during Melbourne's 2020 lockdown.
2. One family of rearrangements scored well. It is a 1,2-decimation: read
   one step down, then two steps right, wrapping around the grid edges.
3. The grid splits into three horizontal segments of 9, 9, and 2 rows. The
   decimation applies within the first two segments.
4. The plaintext string `LIFEIS` sits in the second segment outside the
   decimation. Van Eycke spotted this quirk.
5. Oranchak supplied guessed phrases ("HOPE YOU ARE", "TRYING TO CATCH ME",
   "THE GAS CHAMBER") to AZdecrypt. It solved the first segment.
6. The last two rows decode with the same key, without transposition. Some
   words in them read in reverse.
7. The team notified the FBI on 5 December 2020. The FBI Cryptanalysis and
   Racketeering Records Unit confirmed the solution. Oranchak announced it
   on 11 December 2020.

The team described the work in a 2024 paper on arXiv (2403.17350).

### The plaintext

The message, with the killer's spelling kept:

> I hope you are having lots of fun in trying to catch me that wasn't me on
> the TV show which brings up a point about me I am not afraid of the gas
> chamber because it will send me to paradice all the sooner because I now
> have enough slaves to work for me where everyone else has nothing when
> they reach paradice so they are afraid of death I am not afraid because I
> know that my new life is life will be an easy one in paradice death

The message denies that Zodiac appeared on a television talk show. It
contains no name and no location. After 51 years, the payoff was taunts.
That outcome matches the Z408 hoax.

## Z13: the name cipher

On 20 April 1970 the killer wrote to the *Chronicle*. The letter opens
"My name is—," followed by 13 cipher characters. Eight distinct symbols
appear.

Proposed readings include:

- "Alfred E. Neuman", the *Mad* magazine mascot (Craig P. Bauer).
- "Dr. Eat a Torpedo", derived with the Z340 key (Ryan Garlick). This may
  mock a public dare by D. C. B. Marsh, then president of the American
  Cryptogram Association, who asked Zodiac to encipher his name.
- In 2021 Fayçal Ziraoui, a French engineer, claimed solves for both Z13
  and Z32. Researchers rejected them for lack of verifiable evidence.

No reading can be confirmed. The cipher is far too short. See the section
on unicity distance below.

## Z32: the bomb cipher

On 26 June 1970 the killer wrote again to the *Chronicle*. He enclosed a
Phillips 66 road map of the San Francisco Bay Area. At Mount Diablo he drew
a crosshair marked 0, 3, 6, 9. He noted that 0 must be set to magnetic
north. A 32-character cipher accompanied the map. He claimed it located a
buried bomb set to kill schoolchildren.

The July 1970 "Little List" letter added a hint: "The Mt. Diablo code
concerns Radians + # inches along the radians." In 1981 Gareth Penn noted
that three Zodiac attack sites align along one radian from Mount Diablo.
No bomb was ever found.

A security firm, Praetorian, published a possible solution tied to the map.
The community did not accept it. As with Z13, the short length blocks
verification.

## Why Z13 and Z32 may never be solved

A cipher can hide a message only while it is longer than its unicity
distance. That distance is the number of characters needed for one
solution to stand out from all others. For a 26-letter homophonic cipher,
it is roughly 20 to 30 characters. Z13 has 13 characters. Z32 has 32, but
its key comes from a separate map code with more unknowns than the message
itself.

The result: hundreds of candidate readings fit each cipher. Each reading
can be made to spell a name or a place. No test can single out the true
one. Oranchak's own assessment is that it is practically impossible to
determine whether any proposed solution is correct. The FBI-confirmed Z340
solution carries statistical weight that a 13-character text cannot reach.

## Other cipher material

- An August 1973 letter mailed from Albany, New York, contained a short
  code. FBI cryptanalysts decoded it as a threat against a medical center.
  Handwriting analysis did not confirm Zodiac as the writer. Most
  researchers treat the letter as disputed.
- No other confirmed Zodiac ciphers exist. Many "solutions" circulate
  online. None has official or broad community acceptance.

## Tools and research community

- AZdecrypt: homophonic substitution solver by Jarl Van Eycke. It produced
  the final Z340 reading.
- zkdecrypto: an earlier open-source solver used in long-running attacks on
  Z340.
- zodiackillerciphers.com: Oranchak's project. It hosts the wiki of
  statistical observations and the full cipher images.
- "Let's Crack Zodiac": Oranchak's video series. It documents the search
  history and the Z340 solution.

## Sources

- [Wikipedia: Zodiac Killer](https://en.wikipedia.org/wiki/Zodiac_Killer) —
  dates, mailings, plaintext quotes, Z13 and Z32 context.
- [arXiv 2403.17350: The Solution of the Zodiac Killer's 340-Character
  Cipher](https://arxiv.org/abs/2403.17350) — the solvers' paper.
- [Wolfram Blog: The Solution of the Zodiac Killer's 340-Character
  Cipher](https://blog.wolfram.com/2021/03/24/the-solution-of-the-zodiac-killers-340-character-cipher/) —
  construction details, decimation, segments, solve timeline.
- [Let's Crack Zodiac — Episode 5 — The 340 Is
  Solved!](https://www.youtube.com/watch?v=-1oQLPRE21o) — account by the
  solver.
- [Zodiac Killer Ciphers wiki: Encyclopedia of
  observations](https://zodiackillerciphers.com/wiki/index.php?title=Encyclopedia_of_observations) —
  symbol counts and statistics.
- [History.com: The Zodiac
  Ciphers](https://www.history.com/articles/the-zodiac-ciphers-what-we-know) —
  mailing dates and overview.
- [SJSU thesis: Heuristic Search Cryptanalysis of the Zodiac 340
  Cipher](https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1055&context=etd_projects) —
  Z340 symbol count and search background.
