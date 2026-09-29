# Data provenance

All files fetched 17 September 2026.

## Ciphertexts

- `z340.raw`, `z408.raw`, `z13.raw`, `z32.raw` — the four Zodiac cipher
  transcriptions from David Oranchak's project wiki
  (`oranchak.com/zodiac/wiki/cipher_N.txt`, now offline; retrieved through
  the Internet Archive Wayback Machine, 2020 snapshots). Z340 was
  cross-checked character by character against an independent transcription
  embedded in `github.com/n1k0m0/Zodiac-340-Transposition-Reverser`
  (itself sourced from `zodiackillerciphers.com`): exact match.
- Integrity checks (enforced by `ciphers.py` at import):
  Z340 = 340 symbols, 63 unique; Z408 = 408 symbols, 54 unique;
  Z13 = 13 symbols, 8 unique; Z32 = 32 symbols, 29 unique. All four match
  the counts published on the Zodiac Killer Ciphers wiki.

## Solutions

- `z340-solution.txt` — the FBI-confirmed plaintext from Oranchak, Blake,
  and Van Eycke, "The Solution of the Zodiac Killer's 340-Character
  Cipher", arXiv:2403.17350. This is the text the cipher actually decodes
  to, misspellings kept (`FAN`, `BRINGO`, `BECAASE`, `PARADLCE`, `SOOHER`,
  `WORV`, `VNOW`, `PARADICE`). 408 of 408 characters accounted for.
- `z408-solution.txt` — the 1969 Harden solution, from the letters
  collection in `github.com/DrDub/zodiac-killer-ciphers` (a public mirror
  of Oranchak's project data). The trailing 18 characters
  (`EBEORIETEMETHHPITI`) are filler; they are kept so the length is 408.
- `z408-solution-aca.txt` — the American Cryptogram Association archive
  copy of the same solution, kept for cross-reference. It differs in a few
  characters of the trailing filler.

## Language-model corpus

- `zodiac-letters.txt` — concatenated text of the Zodiac correspondence,
  from `github.com/DrDub/zodiac-killer-ciphers`, `letters/*.txt`
  (confirmed and disputed items as labeled there). This is the in-domain
  corpus; the harness trains on it five times over to weight it against
  the background text.
- `english-background.txt` — "The Sign of the Four" by Arthur Conan Doyle,
  Project Gutenberg ebook 2097, public domain. Background English only;
  it carries no information about the ciphers.

## Licence and use

The cipher transcriptions and solutions are factual records of public
documents. The corpus file is public domain. This repository is for
cryptanalytic research on an open, 56-year-old case.
