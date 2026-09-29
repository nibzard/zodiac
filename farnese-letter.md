---
title: The Farnese letter
author: Simon Klee
source: https://simonklee.dk/farnese-letter
published: 2026-09-16
fetched: 2026-09-17
---

# The Farnese letter

In April 1542 a letter left Rome for the court of Charles V in Spain. On its first page the Italian stops in the middle of a line and digits begin:

![Folio 70r: handwritten Italian gives way to the first ten cipher digits on the same line](https://simonklee.dk/static/writing/farnese-letter/fig/opening.png)

*Figure 1. The opening of the cipher, f. 70r. Archivio Apostolico Vaticano (AAV), Segr. Stato, Spagna 1A, photograph supplied through [DECODE record 92](https://de-crypt.org/decrypt-web/RecordsView/92). Detail enlarged from the photograph.*

Read with the key recovered below, the first ten digits group like this:

    73  4  57  4  9  03  5
     d  o   p  o  ·   l  a

*Dopo la*, "after the". The `9` stands for nothing: it is a null. The difficulty is deciding where each code ends. `73` is *d*, but `7 3` is also two letters, *n m*. Even with the key, a run of digits can be read more than one way.

How do you find the key when you do not know where one code ends and the next begins? And once you have it, how do you tell the writer's words from a plausible guess?

## The letter

The sender was Cardinal Alessandro Farnese, grandson of Paul III and, at twenty-one, head of the papal secretariat. The recipient was Giovanni Poggio, bishop of Tropea and nuncio, the Pope's ambassador, at the Emperor's court.^([1](#fn:1)) The letter opens in ordinary Italian: Poggio will have heard by word of mouth from Giovanni Ricci da Montepulciano about *la materia della pace*, the peace between the Emperor and France, so Farnese will not repeat it. Montepulciano had returned from Spain in February with the Emperor's terms and had left Rome for Spain again in late March.^([2](#fn:2))

Montepulciano's name is also on a cipher key. Aloys Meister's 1906 study of papal cryptography prints, among the old ciphers of the papal secretariat, a key headed *Cifra ultima con Mons. Poggio mandata per il Montepulciano*: the latest cipher with Poggio, sent by Montepulciano. Meister dates it 1538–42.^([3](#fn:3))

The letter fills eight pages on four leaves, 70r to 73v in the archive's numbering: *r* for the front of a leaf, *v* for the back. Page 70r is cleartext for most of its length. Then the digits take over in the middle of a line and fill the whole of pages 70v to 72r. On 72v they surround a cleartext passage about church business and news from Ancona, "fresh and from a good source". The cipher ends on 73r, and the rest of that page is clear. Page 73v is clear and dated *Da Roma alli X\[?\] di Aprile 1542*: the day is a Roman numeral beginning with X whose remaining strokes lie under a flourish, still unread. What is in clear is the frame; the instructions are in cipher.^([4](#fn:4))

![Folio 70r: Italian prose followed by four lines of cipher](https://simonklee.dk/static/writing/farnese-letter/fig/page-70r.jpg) ![Folio 70v: a full page of cipher digits](https://simonklee.dk/static/writing/farnese-letter/fig/page-70v.jpg)

*Figure 2. Ff. 70r and 70v. AAV, Segr. Stato, Spagna 1A, through [DECODE record 92](https://de-crypt.org/decrypt-web/RecordsView/92), public previews. The change from prose to digits comes near the foot of 70r. The cipher continues across the next page.*

Ludwig Cardauns cited this volume in his 1912 collection of the nuncios' reports, but his selected correspondence does not include this letter.^([5](#fn:5)) In July 2019 George Lasry set the text as Part 5 of the Vatican Challenge on MysteryTwister, a site of cipher puzzles: key unknown, plaintext unknown, language probably Italian. In their study, published online in 2020, Lasry, Beáta Megyesi and Nils Kopal still listed the Spagna 1A material as unsolved. Their digit-frequency analysis placed it in a separate cluster. They compared another part of the collection, IA-1, with Meister's Poggio key, without success, and thought this letter, IA-2, used a different key.^([6](#fn:6)) On 16 September 2026, the challenge page still displayed zero solves.^([7](#fn:7))

The search began with a public transcription, now distributed with the DECODE record and the challenge. Its header credits EHum, dates the transcription 9 January 2016, and records about six and a half hours' work on the eight pages. The transcription contains 6,577 cipher digit positions: 44 recorded as `?`, unreadable, and 207 with a mark above them, mostly dots. There is no consistent word division. The [full ciphertext](https://simonklee.dk/farnese-letter/ciphertext.md) is reproduced as text, with its page and line breaks. The counts and searches below used this public transcription. I checked it against the larger photographs later.^([8](#fn:8))

## What the counts show

In the public transcription, digit `7` makes up 17.5 percent of the text and `1` only 3.1. A few pairs are far more common than chance: `80` occurs 349 times, `57` 317, `27` 263, `03` 258, `73` 220. Doubled digits are nearly absent: `00` six times, where independent digits would give about 117; `11` three times; `44` twice. And the digits alternate between two groups, `4 5 6 8` and `0 1 2 7 9`, with `3` belonging to neither: after `73`, for instance, the next digit is `6`, `8`, `4` or `5` in 93 percent of cases.^([9](#fn:9))

![Digit pairs in the ciphertext](https://simonklee.dk/static/writing/farnese-letter/fig/bigrams.png)

*Figure 3. How often each digit follows each other digit in the public transcription. The five pairs in bold turned out to be the codes for t, p, c, l and d. The pale diagonal is the avoidance of doubles. Author's computation from EHum's 2016 transcription.*

That looks like consonants and vowels taking turns. But it does not decide whether `73` is one code or two frequent neighbors, and no fixed rule of cutting, such as pairs at even positions or certain digits always beginning a pair, gave a consistent result.

The papal ciphers of the 1540s used several designs. In some, one digit stands for several letters and the reader chooses. In some, pairs spell syllables. One 1545 key writes the vowels as pairs and the consonants as single digits.^([10](#fn:10)) I tried these designs with earlier versions of the search, without obtaining readable Italian.^([11](#fn:11)) The design that fitted was a simple one also printed in Meister's collection: every letter has one code, of one or two digits, and the reader tells them apart by context.

![Meister's key no. 7, for Alessandro Vitelli, 1546](https://simonklee.dk/static/writing/farnese-letter/fig/meister-179.png)

*Figure 4. A key of that design: Meister no. 7, for Alessandro Vitelli, dated by Meister to 1546. Single digits for some letters, pairs for the rest, one null, a few words. Aloys Meister, Die Geheimschrift (1906), [p. 179](https://archive.org/details/diegeheimschrift00meis/page/n195/mode/1up); Getty Research Institute copy, digitized by Internet Archive. Cropped from the printed edition.*

## The search

I searched for the key and the code boundaries together. An outer search changed the assignments of letters to codes. For each candidate key, an inner decoder searched for a good way to divide the digits and read them. The outer search could then compare keys by how well their readings scored.^([12](#fn:12))

To judge those readings, I trained a character model that estimates the probability of each letter from the four before it: a five-gram model. It trained on about 4.9 million letters. Most came from Machiavelli, Castiglione, and Vasari on Wikisource. About 720,000 came from Italian-looking lines extracted from the OCR of Cardauns's *Nuntiaturberichte aus Deutschland* I.7, which includes correspondence of the Farnese secretariat from 1541–44. That volume does not print this letter.^([13](#fn:13)) I lower-cased the text, stripped accents, folded *v* into *u*, deleted *h*, and collapsed doubled letters. These were guesses about the clerk's habits, and they turned out to match: the letter writes *tute*, *esendo*, *facia*; its key has one code for *u* and *v* and none for *h*.

A letter sequence absent from the corpus still needed a chance. The model blended the counts for a four-letter context with estimates from shorter contexts, down to individual letter frequencies. This smoothing let it score unfamiliar names and damaged words without ruling them out altogether.^([14](#fn:14))

### Reading a candidate key

The decoder walks the digits from left to right. Under the key eventually recovered, the opening has these two possible paths, among others:

```
Digits       7 3 4 5 7 4
One path     73  4  57  4    d o p o
Another      7 3 4  57  4    n m o p o
```

The first path consumes `73` at once and emits *d*; the second consumes `7` and `3` separately and emits *n m*. Each emitted letter adds its base-10 log probability to the path's score. The letters that follow can favor one path over the other, so the decoder keeps several partial readings alive.

Each partial reading is a *state*, which records the position in the digits, the last four emitted symbols, and the score so far. If two paths reach the same position with the same language-model context, their possible continuations are identical: only the better-scoring path needs to survive. Among different contexts, the decoder keeps the eight best at each position. This is a beam search. It is an approximation: a path discarded early cannot recover when later letters would have made it convincing.

In the successful searches, I set aside the digits with a dot or comma above them and cut the text at those places and at unreadable digits. Each fragment began with a fresh language-model context. The key received the sum of its best surviving fragment scores, including penalties for nulls and digits it could not decode. The dotted codes would come back once the letters were known.^([15](#fn:15))

### Changing the key

The outer search began with random assignments, favoring codes that occurred more often. It could swap two assignments, move one to an unused code, or turn off an optional unit such as a null. It accepted any improvement. It could also accept a worse key, with a chance that fell as the run went on. This is simulated annealing. Accepting worse moves lets the search escape a key that beats its immediate neighbors but is still wrong. I repeated the search from fresh random keys. Each repetition is a *restart*.^([16](#fn:16))

The first search to produce recognizable Italian gave this opening, with underscores marking the null:

    dopo_lapartitadelmontepinmcian_il_manon

*Dopo la partita del Montepulciano*, "after Montepulciano's departure". The cleartext on the same page mentions his departure. Further along were *prepararsi contra … del turco*, *cento naui*, *ungaria*, *ridolfo gonzaga*, *forteza di luzara*, *mons. di granuela*.

Much of the rest was still garbage. This search had been allowed a pool of optional word codes, and it used them to explain away inconvenient digits. Searches that were allowed several nulls declared three frequent digits meaningless. Allowing two codes per letter also gave high scores for worse text. Yet four of the first search's six restarts had given the same codes to the same eighteen letters, the whole alphabet the clerk used. The letter assignments were stable even while the extra codes spoiled the reading.^([17](#fn:17))

I tightened the search to one code per letter, at most one null, and no word codes. I also retrained the Italian model with word spaces removed. A model trained on *del quale* expects a boundary after the *l*, but the decoder presents it with `delquale`. The unspaced model learns the letter sequences across those boundaries. With these changes, the search reached the same letter key from two of three restarts. The third stopped at a worse key.

*Table 1. Settings for the tightened search.^([15](#fn:15))*

| Setting in the tightened search | Value                                                                           |
|---------------------------------|---------------------------------------------------------------------------------|
| Candidate codes                 | Single digits and pairs occurring at least three times in the scored fragments  |
| Breaks in the input             | 203 above-dot/comma tokens and 44 unreadable tokens; one belongs to both groups |
| Input after those cuts          | 219 scored fragments; 6,331 retained digits^([18](#fn:18))                      |
| Beam width                      | Eight states per digit position                                                 |
| Proposal attempts per restart   | 500,000                                                                         |
| Penalty per null                | 1; emits no letter and preserves context                                        |
| Penalty per undecodable digit   | 4, when neither the single digit nor the available pair has a code              |

The penalties discourage a key from improving its score by leaving text unread. Scores below divide the penalized total by the retained-digit count. Nearer zero is better. They rank the keys found under these settings, rather than measuring the probability that a reading is correct.

![The recovered key](https://simonklee.dk/static/writing/farnese-letter/fig/key.png)

*Figure 5. The recovered key. The single digits 4, 5, 6 and 8 are the vowels o, a, i and e that the pairs table showed taking turns with the rest. Author's reconstruction.*

### Checking the key

Could the same key be recovered without the opening name? I split the text after its third cipher page and solved each half on its own, from random assignments. Every restart recovered the same eighteen letters and the null.

I also enciphered known Italian with two invented keys of the same design: one synthetic cipher was clean; the other had digits substituted or marked unreadable. Finally, I shuffled the real ciphertext and searched that. These controls used the tightened search settings.

*Table 2. Recovery and control runs.^([19](#fn:19))*

| Input                                                                     | Result                                                     |     Score per retained digit |
|---------------------------------------------------------------------------|------------------------------------------------------------|-----------------------------:|
| Whole letter                                                              | Same eighteen letters and null in two of three restarts    | −0.783; third restart −1.150 |
| First and second halves, solved separately                                | Same letters and null in all twelve restarts, six per half |              −0.777 / −0.785 |
| Clean synthetic cipher                                                    | Letters and null recovered in all three restarts           |                       −0.630 |
| Synthetic cipher with digit substitutions and 44 digits marked unreadable | Letters and null recovered in all three restarts           |                       −0.692 |
| Shuffled real ciphertext                                                  | Best of two restarts                                       |                       −1.351 |

The synthetic tests did not recover the word code for *et*, which the letter-only search could not express. Their Italian also later proved to overlap in part with the model's training text. All the controls share the Italian model and its habits, so the check I trust most is the split: either half of the letter alone yields the letter key and null.

Lasry and his coauthors reported that, in their project, variable-length homophonic keys (those allowing several codes for a letter) had required matching plaintext or an already documented key. The simpler, monoalphabetic key used here came out of the digits.^([20](#fn:20))

## Dots and the null

With the letters fixed, the decoded text around repeated dotted pairs revealed their meanings. A `27` with the dot on its `7` sat where *Marchese* has its *che*, and wherever the sense wanted *che*, "that". A `72` dotted the same way sat where *carichi*, "burdens", has its *chi*; a `57`, where *non si vede*, "one does not see", has its *non*. With the dot on the first digit instead, the same pairs gave *qua*, *que* and *qui*.

![The dotted codes](https://simonklee.dk/static/writing/farnese-letter/fig/dots.png)

*Figure 6. The dot on the first digit gives qua, que, qui; on the second, che, chi, non. Three more dotted pairs are titles: Sua Santità, Sua Maestà, Vostra Signoria, written here as the cleartext abbreviates them. Author's reconstruction.*

The search alphabet had also included *q*, which the cipher does not need as a separate letter. In the tightened full-text run it occupied `81`. The decoded contexts gave that code the reading *et*, "and". The null `9` is not a consistent word divider. It ends some words and not others, appears inside words (*tu·te* for *tutte*, the dot marking the null), and is used in *con*, written `27 4 9 7`. It can prevent misreadings: `8 9 0` reads *e s*, where `80` would be read as *t*.^([21](#fn:21))

## What the digits say and what the model wants

Recovering the key does not settle the text. The sequence `0 5 7 8 0 5` occurs four times in the letter. Under the key it has two Italian readings.

![One sequence, two readings](https://simonklee.dk/static/writing/farnese-letter/fig/ambiguity.png)

*Figure 7. The digits 0 5 7 8 0 5 under the key: santa or spesa. Author's diagram.*

My first reading, in three of the four places, was *la santa \[impresa\]*, the holy enterprise, with a word supplied. The surrounding argument calls for *la spesa*, the expense, every time: the Pope will contribute what he can to the expense; the ships may not be ready in the year the expense is for; he will pay his share of the expense against the Turk.^([22](#fn:22))

### Reading through errors

Some passages suggested errors in the digits themselves. In Montepulciano's name, the transcription gave `2`, which the key reads as *r*, where the name needed *u*. I wrote a second decoder to compare literal readings with readings that required small changes to the transcription. The key, now including the dotted codes, stayed fixed.

The key search had cut the text at unreadable and dotted digits. This decoder worked through the cipher on each page, keeping the language context across unreadable places. It preserved the transcriber's qualifications: `2?` meant a doubtful `2`, `1/2` offered two readings, and `?` meant an unreadable digit. Dots, commas, and dashes above the digits were retained too.

At each position, the program compared the next digit or pair with the codes in the fixed key. An exact match cost nothing. Where nothing matched, it could propose a different digit or a changed above-mark. It could also drop a digit, supply the missing half of a pair, or insert a single-digit letter code. I assigned different costs to these operations so that filling a known hole was easier than contradicting a digit the transcriber had read without qualification.

*Table 3. Edit costs in the fixed-key decoder.^([23](#fn:23))*

| Proposed operation                                              | Cost in base-10 log units |
|-----------------------------------------------------------------|--------------------------:|
| Keep the digit, or the first offered alternative                |                         0 |
| Fill an unreadable `?`                                          |                       0.3 |
| Choose the second offered alternative                           |                       0.5 |
| Substitute a listed look-alike for a digit marked uncertain     |                         1 |
| Substitute a listed look-alike for a digit not marked uncertain |                         3 |
| Substitute a digit outside the list                             |                         6 |
| Supply or ignore an above-dot                                   |                         3 |
| Ignore an above-comma / above-dash                              |                     2 / 1 |
| Insert or drop a digit                                          |                         5 |

The look-alike list included such confusions as `1` with `2`, `3` with `5` or `7`, and `0` with `8` or `9`. These were hand-set costs, not measured error probabilities.

The score combined the two kinds of evidence:

```
reading score = sum of letter log probabilities − sum of edit costs
```

Code divisions and edits were searched together. A changed digit might join the next one into a pair, changing both the number of letters emitted and the context for the letters after them. As before, the decoder kept several partial readings alive and recorded the choices behind each one.

At the disputed digit in Montepulciano, keeping `2` emits *r* without an edit cost. Choosing `1` emits *u* but subtracts three from the score. That choice also changes the model's predictions for the following letters, until the changed letter has passed out of its four-letter context. The gain in the Italian score was enough for *u* to win. The edit list records:

```
Source   Change   Letter   Context
2        2>1      u        elmontep [u] lcian il
```

This repairs the middle of the name, but its final *o* is still absent. Another proposal supplied the dot that turns `72`, *b*, into `7̇2`, *que*, giving *in quele di Ungaria*, "in those \[affairs\] of Hungary", in place of *in ble di Ungaria*.

The same scoring rule could damage a passage that already read correctly. On 71r it proposed reading an `8` as the null `9` and regrouping the nearby digits, turning *a le sue sei galere*, "his own six galleys", into *al tuti galere*. I refused that change. The model judged short letter sequences. It did not know how many ships the Pope had or follow the argument about paying for them. A gain large enough to pay for an edit could still produce the wrong reading.

The edit list tied each proposal to its source digits and surrounding text. I could accept or reject a reading and locate the disputed digits in the photographs.

*Table 4. Changes proposed by the decoder.^([23](#fn:23))*

| Type of proposed change                                                | Value |
|------------------------------------------------------------------------|------:|
| Fills of unreadable digits                                             |    44 |
| Other proposed operations, including choices of an offered alternative |   126 |
| Other operations divided by the public transcription's digit count     |  1.9% |

The totals include rejected proposals. Whether an apparent error belonged to the transcriber, the clerk, or the reader still required checking against the page.

## The edition

The [edited text](https://simonklee.dk/farnese-letter/edition/plaintext.md), the *edition* from here on, uses square brackets for conjectural letters. A [digit-by-digit alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment.txt) behind it records what brackets cannot show: ignored dots, dropped digits, digits read as the null. The alignment makes departures visible; it does not make the readings true.^([24](#fn:24))

To test the conjectures, I gave the key to two readers, each a fresh run of the GPT-6 Astra language model, together with the digits of one page decoded literally under it: 72r for one and 71v for the other, the two pages with the most departures. Each was asked for a continuous reading and an account of every place where it left the literal decode. Each recovered its page's argument and many of the edition's words, and each caught something the edition had wrong.

On 72r the edition had left a gap and supplied *\[che potrà\]* on no digits at all. The reader found that the twenty digits behind that gap read *verà la magior piena* exactly, "the greater flood will come". With the lost verb recovered, the supplement was unnecessary. On 71v the edition had the Emperor *knowing* that the Pope's forces are small in themselves, *S.M.tà s\[a\] che*, at the cost of one `2` read as `5` and two digits read as nulls. The reader's *o\[l\]tre che*, "besides the fact that", needs one ignored dot and one missing digit, and fits a sentence that goes on to say the forces are also divided. Both were adopted. The readers were independent of the edition, not of the key or the transcription. Like the edition, they had never seen the page.^([25](#fn:25))

## The page

I checked the disputed readings against photographs of the manuscript. In Montepulciano's name, the decoder wanted a *u* where the transcription gave `2`, the code for *r*. On the page, the disputed digit is a single stroke with a foot: the clerk's `1`, which gives *u*.

![Detail of Montepulciano's name on 70r, showing the hooked 1 transcribed as 2](https://simonklee.dk/static/writing/farnese-letter/fig/montepulciano.png)

```
Transcription   57  2  03  27
Page            57  1  03  27
Reading          p  u   l   c
```

*Figure 8. F. 70r, second cipher line. AAV, Segr. Stato, Spagna 1A, through DECODE record 92; enlarged detail. The name was already a plausible correction from the Italian. The photograph shows why the digit was misread.*

The clerk often joins one digit to the next. The top bar of a `7` runs into the preceding digit. The foot of a `1` can make it look like a `2`. In a small pilot, I showed four short strips to three vision models. They made roughly 12–18 percent digit errors, often on those same confusions. That pilot was too small, and its scoring too different, to establish a character-error-rate comparison with the public transcription.^([26](#fn:26))

I needed a way to compare a doubtful digit with the clerk's other examples. I wrote a program that first straightened each cipher line and removed the handwriting's slant. It looked for cuts in the white gaps and the thin joins between digits, then fitted the transcription to those cuts. Each transcribed digit became a provisional label on a small image. A `2` in the transcription meant "this image is an example of a 2", even where that label would later prove wrong.

A seven-neighbor classifier compared each image with examples from other lines. It used their shapes and proportions to find the seven closest matches, then combined their labels to propose a digit. Leaving out the current line kept a digit from being compared with itself or a neighboring piece of the same joined stroke.

![The disputed glyph in Montepulciano and its seven nearest reference glyphs](https://simonklee.dk/static/writing/farnese-letter/fig/neighbors.png)

*Figure 9. The glyph transcribed as `2` in Montepulciano, followed by its seven nearest matches from other lines. These are the straightened, normalized images used for comparison. The labels come from the public transcription. Author's analysis of AAV, Segr. Stato, Spagna 1A, ff. 70r–73r, photographs supplied through DECODE record 92.*

The classifier agreed with the transcription on 90.5 percent of the glyphs, and on 98.9 percent of the two glyphs in three that it read confidently. Those figures measure agreement with the old labels. To find transcription errors, I needed the disagreements.^([27](#fn:27))

For each suspect, a review sheet put the digit in its line of handwriting, beside the seven matches and a reference sheet of the clerk's forms from `0` to `9`. I checked the ink and recorded the reading, the reason, and how certain it was. I examined all 196 ranked suspects and all flagged differences in the number of digits this way. Where the classifier doubted a digit the edition had left alone, my reading mostly sided with the transcriber: a smear could flatten a `3` into the shape of a `5`, or the next digit's stroke could give a `7` the base of a `2`.^([28](#fn:28))

Some errors were in the number of digits. On 71v the transcription repeated the five digits that read *anco*, "also". The photograph has them once.

![Detail of 71v showing the single group transcribed twice as anco anco](https://simonklee.dk/static/writing/farnese-letter/fig/anco.png)

```
Transcription   5 7 2 7 4  5 7 2 7 4
Page            5 7 2 7 4
Reading         a n  c  o
```

*Figure 10. F. 71v, fourth cipher line. AAV, Segr. Stato, Spagna 1A, through DECODE record 92; enlarged detail. The edition had already dropped the second *anco* as a repetition by the clerk. The repetition was in the transcription.*

The check found five such doubled groups, totaling 21 digits not on the page, as well as fourteen omitted digits and two swapped pairs. Some of the extra digits had supplied words for the edition: *sendosi \[c\]osì firmat\[o\]* became *sendosi firmat\[o\]*, "having been agreed", with no *così*, "thus".^([29](#fn:29))

On 70v, a dot and two hooked `1`s closed a gap in the account of the naval expenses. The transcription had missed the dot over the `7` and read both `1`s as `2`s.

![Detail of 70v showing the dotted che code and the digits for vi va](https://simonklee.dk/static/writing/farnese-letter/fig/che-vi-va.png)

```
Transcription   27   2 6 9 2 5
Page            27̇  1 6 9 1 5
Reading         che u i · u a
```

*Figure 11. F. 70v, third cipher line. AAV, Segr. Stato, Spagna 1A, through DECODE record 92; enlarged detail. With `1` standing for both u and v, this reads *che vi va*: the full phrase is *della spesa che vi va dentro*, "of the expense that goes into it". The dot in the reading row marks the null `9`.*

Other corrections confirmed letters the edition had supplied. In *è s\[t\]ato* on 70r and *aiu\[t\]o* on 72r the transcription has `0 8` where the page has `80`, the code for *t*. The *s* of *stato* still has no digit behind it: the page has the null `9` there, so the edition now reads *è \[s\]tato*. Other bracketed letters, *ris\[p\]osta* and *sol\[d\]o* among them, stand on the page as the edition read them. Some letters the edition had supplied turn out to be on the page: the *n* of *Massimi\[li\]a\[no\]* is a `7` the transcription read as `9`; the *c* of *ues\[c\]ou\[o\]*, *vescovo*, bishop, is a `2` the transcription skipped, completing `27`; the *i* of *Dor\[ia\]* is a `6` dropped at a line end.

On 72r the edition had *conte\[n\]ti* with a supplied *n*. The page has a `7` where the transcription has `4`, and *contenti* is exact. On 70v the conjecture *\[ca\]pitarà il bisogno* is withdrawn: the transcription's `8` is a `1`, and the edition now reads *\[d\]'ovunche più sarà il bisogno*, "wherever the need will be greater". The initial *d* remains conjectural. Other checks went the other way. On 73r the edition had *\[ne\]l qual luogo* by changing a `6`, but the `6` is plain and the text reads *il qual luogo*. On 70r the `2` the edition read as `3` for *contra \[l\]'armata* has the clerk's usual `2` form: if *l* was meant, the clerk miswrote it.

One correction changed who had asked for a public announcement. Under the archive stamp on 72r, the corrected digits give *la S.M.tà \[h\]a voluto*, "His Majesty has wished", where the edition had read *S.S.tà*, His Holiness. The Emperor had asked for the Hungarian subsidy to be offered publicly at Speyer, in the Pope's name.

The castle's name remains conjectural. Where the edition had supplied *\[Poviglio\]* from the Gonzaga genealogy, the corrected digits give *a pore in · pui ·*, with the dots here marking nulls. The edition now reads *a porre in P\[o\]ui\[glio\]*, "to settle in Poviglio". The missing letters still come from the proposed historical identification.^([30](#fn:30))

I also checked the dots wherever the edition added or ignored one. In *risposta*, the mark transcribed above a `7` was the top bar of the `5` before it. Other apparent dots belonged to strokes from the line above. In *Marchese*, the dot was real but on the wrong digit of the pair: the clerk had written *qua* where the name needs *che*.^([29](#fn:29))

The corrections judged sure or probable went into a new transcription. Unresolved readings stayed open. I then aligned the edition against those corrected digits.^([31](#fn:31))

*Table 5. Source digits consumed by the edition's alignment. Both the transcription and the edited reading changed after the page check.^([32](#fn:32))*

| How the edition reads the digits            | Before the page check | After |
|---------------------------------------------|----------------------:|------:|
| Digits in the transcription                 |                 6,577 | 6,562 |
| Read exactly under the key, including nulls |                 6,216 | 6,358 |
| Read with a recorded departure              |                   300 |   170 |
| Left in gaps                                |                    61 |    34 |

Blots, the archive stamp, and smears along the page edges leave some digits and dots unread. I have not checked every glyph the classifier accepted, and substitutions between unlike digits still need another look. The day of the month also remains unread.

A contemporary copy in clear could help with the remaining readings. The Archivio Apostolico Vaticano searched the index to a register cited by Cardauns, but found no entry for an April 1542 letter from Farnese to Poggio.^([33](#fn:33))

## What Farnese put in cipher

The summary below follows the proposed decipherment. Its quotations translate the edited Italian. Gaps and conjectures remain in the edition.

After Montepulciano's departure, the imperial ambassador in Rome, the Marqués de Aguilar, has been with the Pope and brought him Andrea Doria's advice on arming against the Turkish fleet, and a request for help.^([34](#fn:34))

The Pope will hold back nothing within his means, at sea or in Hungary, wherever the need turns out to be greater. But nobody yet knows whether the greater danger will come by land or by sea, and he will not decide where to spend, "so as not to fall into the error of spending in vain in one place that needed it less, and then be unable to help the other." He leaves that to the Emperor's prudence.^([35](#fn:35))

He has two doubts about the plan to arm a hundred ships. He argues that a mixed fleet of galleys and sailing ships has never done well. And a hundred ships would take so long to fit out that they would hardly serve this year, the year the money is for. He will pay his share anyway, beyond his own six galleys.^([36](#fn:36))

The soldiers on his ships must be his own. The Papal State is full of good soldiers used to going to war. Unless he keeps them employed, no edict in the world will stop them taking pay from whoever offers it, to the disturbance of his own state and no advantage to the Emperor. He means, too, to stay neutral so that he can broker the peace, and to give nobody grounds to say he pays for anything but defense against the Turk.^([37](#fn:37))

Then there are the other commitments. The Hungarian subsidy, which Charles V asked for at Lucca, was settled in Rome with the imperial minister Granvelle. At the Emperor's request, the bishop of Modena, Giovanni Morone, has now offered it publicly, in the Pope's name, at the Diet of Speyer, the assembly of the German estates then in session. The enclosed extract from Modena's letter shows that those at the Diet are not content and ask for much more. Ancona, Civitavecchia, the other ports and the guard of Lombardy also need money. The Pope cannot yet say what more he will give on either side.^([38](#fn:38))

Finally, Ridolfo Gonzaga, son of Gianfrancesco, is said to have taken a commission from someone whose name is still unread. He gathered infantry at Luzzara, his brother Massimiliano's castle in Mantuan territory, then moved to his own castle in the territory of Parma and began to fortify it, either because the Marchese del Vasto, the governor of Milan, was preparing to remove him by force or for some design of his own. Whether this is mere rashness on Ridolfo's part or has something larger behind it is not yet clear. The Pope's legate has orders to stop him, by force if necessary, and troops have moved into Parma. *Vederassi il successo*: we shall see how it goes.^([39](#fn:39))

Morone's surviving reports independently confirm a public presentation of papal aid at Speyer on 23 March and complaints that the offer was too small. They corroborate the decipherment's account, although the particular enclosed extract has not been identified.^([40](#fn:40)) The Pope and the Emperor had met at Lucca in September 1541, two weeks after the Turks took Buda.^([41](#fn:41))

The Gonzaga genealogy also fits. Gianfrancesco's sons included Massimiliano, who held Luzzara, and Rodolfo, associated with Poviglio in the Parma territory. A published archival inventory describes a 1546 letter to Rodolfo as "signore di Poviglio". That supports the proposed castle name without supplying its missing letters.^([30](#fn:30))

The peace Montepulciano was carrying did not come. Francis I declared war on Charles V in July 1542. By the end of that month Montepulciano was back in Italy. On 30 July the nuncio Girolamo Verallo reported Ferdinand's statement that *la pratica della pace era exclusa*: the negotiation for peace was finished.^([42](#fn:42))

## Status of the decipherment

This is a candidate reading. The key is stable: either half of the letter alone yields the same letters and null. The page check examined the disputed readings and the classifier's suspects, not every glyph.

No other cryptanalyst has yet verified or challenged the solution. On 15 September I sent the key and plaintext to MysteryTwister, whose team checks Level X solutions by hand.^([7](#fn:7))

## Sources and research materials

The notes identify the evidence for individual claims, including the article's own computations and proposed readings. References to printed books use their printed page numbers; manuscript references use folios. Cipher-line numbers count only lines containing cipher. English translations follow the cited Italian passages. The edition supplies word division, punctuation, and some spelling; its brackets and alignment record uncertain readings. Online catalog and challenge statuses were checked on 16 September 2026.

### Manuscript and transcription

- **Archivio Apostolico Vaticano (AAV), Segr. Stato, Spagna 1A, ff. 70r–73v.** Letter identified here as Alessandro Farnese to Giovanni Poggio, Rome, April 1542; day unresolved. [DECODE record 92](https://de-crypt.org/decrypt-web/RecordsView/92), identifier `ASV/i1025/SdS/Spain/IA/2`. Older references use ASV, Archivio Segreto Vaticano. The April date is the reading of this letter's dateline, rather than the wider date range assigned to the archival bundle.
- **EHum.** Transcription of `ASV_i1025_SdS_Spain_IA-2`, 9 January 2016. [Public original](https://mysterytwister.org/media/challenges/add/ASV_i1025_SdS_Spain_IA-2.txt); [complete transcription, including the transcriber's header](https://simonklee.dk/static/writing/farnese-letter/transcription/public.txt); [ciphertext appendix and notation](https://simonklee.dk/farnese-letter/ciphertext.md). This is the input to the key search. The [manuscript-corrected transcription](https://simonklee.dk/static/writing/farnese-letter/transcription/transcription_ms.txt) is a later research product, used for the edition's final alignment.

### Published sources

- **Borrelli, Luciano, ed.** "Biblioteca trentina \[parte seconda\]." *Studi trentini di scienze storiche*, Sezione prima, 68, no. 2 (1989): 185–214. [Digitized article](https://heyjoe.fbk.eu/index.php/stusto/article/download/3801/3802).
- **Cardauns, Ludwig, ed.** *Berichte vom Regensburger und Speierer Reichstag 1541, 1542. Nuntiaturen Verallos und Poggios. Sendungen Farneses und Sfondratos 1541–1544*. *Nuntiaturberichte aus Deutschland nebst ergänzenden Aktenstücken*, I. Abteilung, vol. 7. Berlin, 1912. [Digitized edition](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag). Cited below as Cardauns, with document number and printed page.
- **Cascella Alcaraz, Sara.** "Una cifra imperial en Roma (1543)." *Estudios Románicos* 34 (2025): 63–73. [doi:10.6018/ER.613381](https://doi.org/10.6018/ER.613381).
- **Fabbrici, Gabriele.** "Geografia politica della pianura reggiana fra XVI e XVII secolo. Note introduttive." In *Corti e diplomazia nell'Europa del Seicento: Correggio e Ottavio Bolognesi (1580–1646)*, edited by Blythe Alice Raviola, 51–66. Mantova: Universitas Studiorum, 2014. [Cited page 61](https://www.google.it/books/edition/Corti_e_diplomazia_nell_Europa_del_Seice/aMrcBAAAQBAJ?hl=it&gbpv=1&pg=PA61).
- **Gairdner, James, and R. H. Brodie, eds.** *Letters and Papers, Foreign and Domestic, of the Reign of Henry VIII*. Vol. XVII, 1542. London: Her Majesty's Stationery Office, 1900. [British History Online, pp. 286–300](https://www.british-history.ac.uk/letters-papers-hen8/vol17/pp286-300).
- **Gayangos, Pascual de, ed.** *Calendar of State Papers, Spain*. Vol. 6, part 2, 1542–1543. London: Her Majesty's Stationery Office, 1895. [British History Online, pp. 1–13](https://www.british-history.ac.uk/cal-state-papers/spain/vol6/no2/pp1-13).
- **Lämmer, Hugo, ed.** *Monumenta Vaticana historiam ecclesiasticam saeculi XVI illustrantia: ex tabulariis Sanctae Sedis apostolicae secretis*. Freiburg im Breisgau: Herder, 1861. [Digitized edition](https://archive.org/details/monumentavatica01laemgoog).
- **Lasry, George.** "The Vatican Challenge — Part 5." *MysteryTwister*, 7 July 2019. [Challenge page](https://mysterytwister.org/challenges/level-x/the-vatican-challenge-part-5); [challenge PDF](https://mysterytwister.org/media/challenges/pdf/mtc3-lasry-13-Vatikanmuseum-05-en.pdf).
- **Lasry, George, Beáta Megyesi, and Nils Kopal.** "Deciphering papal ciphers from the 16th to the 18th Century." *Cryptologia* 45, no. 6 (2021): 479–540. First published online 23 June 2020. [doi:10.1080/01611194.2020.1755915](https://doi.org/10.1080/01611194.2020.1755915).
- **Litta, Pompeo.** "Gonzaga di Mantova," tavola XVI, "Marchesi di Luzzara estinti nel 1794." In *Famiglie celebri di Italia*. Milano, sheet dated 1835. [BnF/Gallica, view 26](https://gallica.bnf.fr/ark:/12148/btv1b8452245b/f26.item).
- **Luzio, Alessandro.** *L'Archivio Gonzaga di Mantova*. Vol. II, *La corrispondenza familiare, amministrativa e diplomatica dei Gonzaga*. Verona: Officine grafiche A. Mondadori, 1922. [Digitized edition](https://www.accademianazionalevirgiliana.org/biblioteca/monumenta/2_mon.pdf).
- **Megyesi, Beáta, Nils Blomqvist, and Eva Pettersson.** "The DECODE Database: Collection of Historical Ciphers and Keys." In *Proceedings of the 2nd International Conference on Historical Cryptology* (2019), 69–78. [Open proceedings PDF](https://ep.liu.se/ecp/158/008/ecp19158008.pdf).
- **Meister, Aloys.** *Die Geheimschrift im Dienste der päpstlichen Kurie von ihren Anfängen bis zum Ende des XVI. Jahrhunderts*. Paderborn: Ferdinand Schöningh, 1906. [Digitized edition](https://archive.org/details/diegeheimschrift00meis).
- **Pastor, Ludwig von.** *Geschichte der Päpste seit dem Ausgang des Mittelalters*. Vol. V, *Paul III. (1534–1549)*. Freiburg im Breisgau: Herder, 1909. [Digitized edition](https://archive.org/details/geschichtederp05past). Dates and pages below refer to this 1909 edition.

Individual entries in the *Dizionario Biografico degli Italiani* are cited by their named authors, volumes, years, and online entry titles in the notes. Their online text does not supply printed page breaks. Methodological references and the signed institutional history of Buda are likewise given in full at the relevant notes.

### Research data and illustrations

The [edition appendices](https://simonklee.dk/farnese-letter/edition/README.md) contain the [key tables](https://simonklee.dk/farnese-letter/edition/key.md), [machine-readable key](https://simonklee.dk/static/writing/farnese-letter/edition/key.txt), [edited Italian text](https://simonklee.dk/farnese-letter/edition/plaintext.md), and [digit-by-digit alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment.txt). The [automatic reading](https://simonklee.dk/static/writing/farnese-letter/edition/reading.txt) preserves the decoder's proposals, including those rejected in the edition. The [transcription appendix](https://simonklee.dk/farnese-letter/transcription/README.md) includes the public and corrected texts and the individual manuscript decisions. The [results supplement](https://simonklee.dk/farnese-letter/results/README.md) reports the search and control results, model details, and independent rereadings. The [earlier alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment-before.txt) supplies the before-check figures in table 5. These are the article's research outputs, not an independently transmitted plaintext.

The [figure source register](https://simonklee.dk/farnese-letter/fig/SOURCES.md) records source images, folios, crop coordinates, transformations, and figure data. The public previews and the full-resolution manuscript photographs are different files; the latter were supplied through DECODE with restricted access and are not reproduced in full here. The reproduced details and processed glyphs are identified individually in the register.

### Notes

1.  Stefano Andretta, "FARNESE, Alessandro," *Dizionario Biografico degli Italiani* (DBI) 45 (1995), [online entry](https://www.treccani.it/enciclopedia/alessandro-farnese_%28Dizionario-Biografico%29/), opening and the paragraph beginning *In questo periodo*: born 7 October 1520; appointed to the papal general secretaryship on 1 January 1538, assisted by Marcello Cervini. Giampiero Brunelli, "POGGIO (Poggi), Giovanni," DBI 85 (2016), [online entry](https://www.treccani.it/enciclopedia/giovanni-poggio_%28Dizionario-Biografico%29/), records Poggio's appointment as bishop of Tropea on 4 October 1541 and as nuncio to Charles V on 10 October. Both entries accessed 16 September 2026.

2.  Farnese to Verallo, Rome, 18 February 1542, Cardauns, no. 96, pp. 199–201, especially [200–201](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n123/mode/2up): *Sono otto giorni che m. Gio. Montepulciano tornò di Spagna*. This places the return about 10 February. The subsequent passage says the terms will be proposed in France but does not identify Ricci as the messenger. Gigliola Fragnito, "RICCI, Giovanni," DBI 87 (2016), [online entry](https://www.treccani.it/enciclopedia/giovanni-ricci_%28Dizionario-Biografico%29/) (accessed 16 September 2026), gives the next departure as 28 March, as does Pastor, V, [p. 471 n. 4](https://archive.org/download/geschichtederp05past/page/n518.jpg), citing Serristori's report of 29 March (Florence, Med. 3264). Serristori's report itself has not been inspected here. The [edited cleartext on 70r](https://simonklee.dk/farnese-letter/edition/plaintext.md#070r) prints *alli XXV del \[passato\]*, but the photograph has further numeral strokes after the *V*; the [public transcription](https://simonklee.dk/static/writing/farnese-letter/transcription/public.txt) retains them as `XXV14^-`. The numeral may read *xxviij* (28). The edition's shortened *XXV* is not a secure reading and does not establish a conflict with the published chronology.

3.  Meister (1906), section II, no. 2, [pp. 176–177](https://archive.org/details/diegeheimschrift00meis/page/n192/mode/2up). The printed heading reads *\[Zwischen 1538 und 1542.\] Cifra ultima con Mons. Poggio mandata per il Montepulciano*. The date is Meister's editorial dating. He gives the collection's manuscript source as "Rom, Bibl. Chigi M II 49 f. 85–148 und f. 168" on p. 176; this is the source of the comparative keys, not of the letter.

4.  AAV, Segr. Stato, Spagna 1A, ff. 70r–73v, DECODE 92. Compare the [public transcription](https://simonklee.dk/static/writing/farnese-letter/transcription/public.txt) with the edition's [70r](https://simonklee.dk/farnese-letter/edition/plaintext.md#070r), [72v](https://simonklee.dk/farnese-letter/edition/plaintext.md#072v), and [73v](https://simonklee.dk/farnese-letter/edition/plaintext.md#073v). The phrase about the Ancona news is *freschi et di bon loco*. The edited cleartext contains supplements and omissions; it is not a diplomatic transcription.

5.  Cardauns, pp. 437–441: the archival citation "Rom A. V. Spagna vol. 1 A f. 52–54 Or." is on [p. 437 n. 2](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n244/mode/2up). On [p. 439](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n245/mode/2up) he states that he selects passages concerning German affairs from the fragmentarily surviving correspondence of 1542. This selection does not include the April letter. Its omission does not establish that he attempted to decipher these leaves.

6.  Lasry, Megyesi, and Kopal (2021; online 2020), §5.5, pp. 501–502. Their comparison with Meister 176/2 concerns IA-1. On p. 502 they write: "The ciphertexts in the second part (IA-2) seem to belong to another key." Table 3, p. 496, places *Segr. Stato Spagna-1A* in cluster 16; that result concerns the collection, rather than this letter's digit counts alone.

7.  Lasry (2019), challenge PDF, [pp. 4–5](https://mysterytwister.org/media/challenges/pdf/mtc3-lasry-13-Vatikanmuseum-05-en.pdf#page=4), for the unknown key and plaintext and the tentative language identification. The [live challenge page](https://mysterytwister.org/challenges/level-x/the-vatican-challenge-part-5) gives the publication date as 7 July 2019 and displayed "0 solves" when checked on 16 September 2026. This is the site's recorded status. The author submitted the present result on 15 September; external verification was pending on 16 September.

8.  EHum's [transcription header](https://simonklee.dk/static/writing/farnese-letter/transcription/public.txt) records eight times totaling 393 minutes (6 h 33 min). Megyesi, Blomqvist, and Pettersson (2019), §4.1, [p. 73](https://ep.liu.se/ecp/158/008/ecp19158008.pdf#page=5), explain that the date field records submission and that working time excludes breaks and quality checks. The [transcription appendix](https://simonklee.dk/farnese-letter/transcription/README.md) records the counts: 113 cipher lines, 6,577 digit-position tokens, 44 unreadable tokens, and 207 above-marked tokens (178 dots, 25 commas, four dashes). DECODE's separate record-creation date, 18 October 2016, is not the transcription date.

9.  Author's calculations from the public transcription. The [counting rules and figure data](https://simonklee.dk/farnese-letter/fig/SOURCES.md#digit-pair-counts) specify overlapping windows, treatment of unreadable positions and alternative readings, and the joining of cipher lines and folios across intervening cleartext. There are 6,492 readable two-position windows. Digit percentages use all 6,577 positions as their denominator. The expectation for `00` is an independence comparison using the observed frequency of `0`, not a fitted model of the cipher. After the 220 occurrences of `73`, the next token is `6`, `8`, `4`, or `5` in 204 cases (92.7 percent); one next token is unreadable.

10. Meister (1906), no. 1, [p. 176](https://archive.org/details/diegeheimschrift00meis/page/n192/mode/1up), for single-digit polyphones; no. 2, [p. 177](https://archive.org/details/diegeheimschrift00meis/page/n193/mode/1up), for syllables such as *ca ce ci co* = `21 22 23 24`; and no. 4, pp. 177–178, the 1545 Mignanello key, for vowels `11 13 15 17 19` and single-digit consonant codes, most with two possible readings. These features can coexist in a key. No. 7, p. 179 (figure 4), supplies the comparison with a mixed-length monoalphabetic design.

11. The [exploratory-search summary](https://simonklee.dk/farnese-letter/results/README.md#exploratory-searches) describes the structure tests, unsuccessful searches, and Mignanello-type vowel-pair test. These used several predecessor implementations. Their negative results describe the searches made, not an exhaustive exclusion of those designs.

12. Lasry, Megyesi, and Kopal, §6.10, pp. 522–524, already describe probabilistic variable-length decoding with Italian five-grams, logarithmic scores, and spelling normalization, explicitly for a cipher "for which the key is known" (p. 522). Here the outer search also changes the unknown key.

13. The [corpus account](https://simonklee.dk/farnese-letter/results/README.md#training-corpus) identifies Machiavelli's *Il Principe*, *Lettere*, *Discorsi sopra la prima Deca di Tito Livio*, and *Istorie fiorentine*; Castiglione's *Il libro del Cortegiano*; and Vasari's *Vite* (1550). The complete corpus contains 4,954,638 normalized letters, including 729,754 from Cardauns; withholding 200 rows leaves 4,899,793 training letters, including 721,950 from Cardauns. A language heuristic selects Italian-looking lines, rather than identifying each letter's author. The Wikisource metadata does not establish the underlying print edition for every work. The [corpus audit](https://simonklee.dk/farnese-letter/results/README.md#training-corpus) records metadata contamination, duplicate literary text, and sixteen held-out rows also present in training; this is not a deduplicated or independently held-out corpus.

14. Normalization also folds `j/y` to `i`, `k` to `c`, `w` to `u`, and `x` to `s`. The [language model](https://simonklee.dk/farnese-letter/results/README.md#language-model) blends each context's observed distribution with shorter-context estimates, using weight `total/(total + distinct_next_symbols)`; the base is uniform. Unspaced training removes word spaces, retaining beginning/end-of-row sentinels. The C solver uses a dense table of 3,200,000 float32 base-10 log probabilities.

15. The [search account](https://simonklee.dk/farnese-letter/results/README.md#key-search) specifies the beam decoder, input preparation, and annealing settings. The tightened search used the unspaced model, no word units, 500,000 proposal attempts, three restarts, and random seed 11. The candidate-code threshold is applied to the scored fragments. Invalid proposals are skipped but still advance the cooling schedule. Above-comma tokens are treated as dotted for these cuts; the four above-dashes do not trigger cuts.

16. S. Kirkpatrick, C. D. Gelatt Jr., and M. P. Vecchi, "Optimization by Simulated Annealing," *Science* 220, no. 4598 (1983): 671–680, especially pp. 672–673, [doi:10.1126/science.220.4598.671](https://doi.org/10.1126/science.220.4598.671) ([scan](https://www.physics.rutgers.edu/~pchandra/physics681/optimization.pdf#page=2)). This is the general method. Table 1 summarizes the cipher-specific settings; the [search account](https://simonklee.dk/farnese-letter/results/README.md#key-search) gives the move probabilities and cooling schedule: swaps, 45%; moves to unused codes, 45%; deactivation of optional units, 10%. A worse key is accepted with probability `exp(Δ/T)`, where `Δ` is the change in total score and `T` falls geometrically from 30 toward 0.5.

17. The [search results](https://simonklee.dk/farnese-letter/results/README.md#recovery-and-controls) include the first successful run, which produced the quoted opening and the common eighteen-letter key in restarts 0, 3, 4, and 5, alongside the three-null, homophone, and tightened searches. These are exploratory runs with changing model inventories, rather than a controlled language-performance test.

18. The retained-digit count includes 26 digits in fragments shorter than three, which the decoder does not score. The scored fragments contain 6,305 digits. The whole-letter scores divide by 6,331, matching the saved runs.

19. The [control results](https://simonklee.dk/farnese-letter/results/README.md#recovery-and-controls) report both halves at seeds 11 and 23, the clean and noisy synthetic ciphers, and the shuffled ciphertext. The clean and noisy cases use different invented keys. Retained-digit denominators are 2,591 and 3,740 for the halves, 6,165 and 6,119 for the synthetic cases, and 6,331 for the shuffle. Deterministic reruns reproduced the recorded keys and scores. Training overlap is documented in the corpus account cited above.

20. Lasry, Megyesi, and Kopal, §5.3, p. 498: "In this project, the recovery of keys for variable-length homophones could only be achieved from matching plaintexts or by finding the key in the sources (e.g., Meister), based on characteristics identified via statistical analysis." The authors also report plaintext-assisted recovery of variable-length monoalphabetic examples F6 and P1 (pp. 499, 501). Their account does not establish a general limit on ciphertext-only recovery or priority for the present result.

21. [Recovered key, regular codes](https://simonklee.dk/farnese-letter/edition/key.md#regular-codes) and [dotted codes](https://simonklee.dk/farnese-letter/edition/key.md#dotted-codes), with contextual examples; [machine-readable key](https://simonklee.dk/static/writing/farnese-letter/edition/key.txt). These assignments are the article's reconstruction. The [unresolved marks](https://simonklee.dk/farnese-letter/edition/key.md#unresolved-marks-and-proposed-corrections) include dotted signs whose meanings remain unknown. The [edition's alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment.txt) records the use of each assignment, including nulls, and the departures needed at individual occurrences.

22. The exact sequence occurs on f. 70v twice and f. 71r twice; [line and token locators](https://simonklee.dk/farnese-letter/fig/SOURCES.md#ambiguous-segmentation). See the [edition's reading note](https://simonklee.dk/farnese-letter/edition/plaintext.md#notes-on-the-reading) and the [saved automatic reading](https://simonklee.dk/static/writing/farnese-letter/edition/reading.txt), which preserves the rejected *santa* readings. The choice between *santa* and *spesa* is contextual: both segmentations use the same key without changing a digit.

23. Costs for a digit and its mark add together; candidate code matches costing more than 6.5 are rejected. Paths reaching the same digit position with the same four-letter context are merged, and the decoder keeps up to 64 contexts before advancing. It records the steps needed to trace the winning reading back to its digits. A literal null carries the context through unchanged at no cost; a title code resets the context without spelling its abbreviation into the language model. The [automatic reading](https://simonklee.dk/static/writing/farnese-letter/edition/reading.txt) records the fixed-key decoder's results under the edit costs in table 3, with source digits above decoded units and changed units marked. Its folio 70r edit list includes the Montepulciano substitution; folio 71r includes the rejected galley reading. Its final tally has 165 edited units containing 170 operations: 44 fills and 126 other operations; `126/6577 = 1.916%`. An operation count is not a measured transcription-error rate, and rejected proposals remain in this output.

24. [Editorial conventions](https://simonklee.dk/farnese-letter/edition/plaintext.md) and [alignment notation](https://simonklee.dk/static/writing/farnese-letter/edition/alignment.txt). The alignment procedure finds a least-cost alignment of an already supplied edited text. Bracketed supplied letters receive a reduced cost, and gaps can absorb digits without cost. Its alignment therefore records how the edition can account for the digits; it is not an independent test of the edition's correctness.

25. The [rereading supplement](https://simonklee.dk/farnese-letter/results/README.md#blind-rereads) includes the 72r and 71v input packets and responses and describes the adopted corrections. Both successful readers were fresh GPT-6 Astra runs. Their packets shared the language-model-selected strict segmentation as well as the key and transcription, omitted unreadable tokens and short fragments, and used the first listed alternative readings. They did not contain manuscript images or the edition. Thus their independence is limited to the subsequent reading task.

26. The [pilot account](https://simonklee.dk/farnese-letter/results/README.md#vision-pilot) describes four strips totaling 55 reference digits and runs of `grok-4.6`, `gpt-6-astra`, and `gemini-3.1-pro` at `#high`. The scoring allowed fractional alternatives and free crop-edge extras; its reference largely followed the public transcription. Prompts, responses, and the restricted-image crops are not included. This account supports a reported pilot, not a reproducible comparative benchmark.

27. The [glyph-classification account](https://simonklee.dk/farnese-letter/results/README.md#glyph-classification) describes line leveling, slant removal, cuts, and token-to-ink alignment. Neighbor selection excludes references from the current line. The evaluation gives 90.549% agreement on 6,497 labeled glyphs and 98.885% on 4,485 glyphs with vote share at least 0.9 (69.03% of the set). PCA and segmentation use the full dataset; line exclusion applies to the neighbor lookup. These are agreement rates against provisional transcription labels. Figure 9's [processing record](https://simonklee.dk/farnese-letter/fig/SOURCES.md#nearest-neighbor-strip) specifies the features, distances, and source glyphs.

28. [Manuscript-check account](https://simonklee.dk/farnese-letter/transcription/README.md#manuscript-check), [individual decisions](https://simonklee.dk/static/writing/farnese-letter/transcription/decisions.tsv), [correction ledger](https://simonklee.dk/static/writing/farnese-letter/transcription/corrections.tsv), and [dot decisions](https://simonklee.dk/static/writing/farnese-letter/transcription/dot_decisions.tsv). All 196 classifier suspects have entries in the decision ledger. Applying sure or probable corrections at the original transcription's positions produces the [corrected transcription](https://simonklee.dk/static/writing/farnese-letter/transcription/transcription_ms.txt).

29. The [correction ledger](https://simonklee.dk/static/writing/farnese-letter/transcription/corrections.tsv) identifies each change by folio, cipher line, and original token position. The five doubled groups are 71v L04 p30–34, L05 p21–23, L09 p46–51, L20 p42–45, and 72r L07 p27–29: lengths `5 + 3 + 6 + 4 + 3 = 21`. There are fourteen inserted digits and 29 deletions overall, giving `6577 − 29 + 14 = 6562`. The [manuscript-check account](https://simonklee.dk/farnese-letter/transcription/README.md#manuscript-check) discusses the individual readings, including the two swapped pairs and the Emperor's title on 72r; the [dot ledger](https://simonklee.dk/static/writing/farnese-letter/transcription/dot_decisions.tsv) records *risposta* at 70v L05 p26–27 and *Marchese* at 73r L01 p57–58. The duplicated-digit count is the sum of the correction rows.

30. Litta, "Gonzaga di Mantova," [tavola XVI](https://gallica.bnf.fr/ark:/12148/btv1b8452245b/f26.item), entries *Gianfrancesco*, *Massimiliano*, and *Rodolfo*, connects both sons to Gianfrancesco and Laura Pallavicino. Their entries discuss the dispute over Luzzara and associate Rodolfo with the *castello di Poviglio nel parmigiano*. The sheet reads *Stampata nel 1835*; the BnF copy is NE-49 (A)-FOL, Gallica view 26 of 34. Fabbrici (2014), p. 61, also identifies Massimiliano as Gianfrancesco's son and successor at Luzzara. Borrelli (1989), [p. 195, no. 592](https://heyjoe.fbk.eu/index.php/stusto/article/download/3801/3802#page=13), describes a letter of Leoncino to "Rodolfo Gonzaga, signore di Poviglio," Mantua, 15 February 1546, with capitulations for the sale of Poviglio to Nicolò d'Arco: Guastalla, Biblioteca Maldottiana, Fondo Davolio Marani, 12 n. 72. This is the published inventory's description; the underlying manuscript has not been inspected here. Luzio (1922), [p. 262](https://www.accademianazionalevirgiliana.org/biblioteca/monumenta/2_mon.pdf#page=262), places Poviglio among the Gonzaga possessions in the Parmense. These sources support the contextual identification, not the absent letters in *P\[o\]ui\[glio\]*.

31. The bracket check has a known omission: on 71r the *u* in *sua parte*, "his share", is unbracketed although it needs `1` and the corrected transcription offers `3/7`. The alignment lists `3/7>1`, but wrongly treats it as a choice between recorded alternatives.

32. The "before" column describes the pre-manuscript-check edition against the public transcription, preserved in the [earlier alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment-before.txt), final totals: `5847 + 369 = 6216` exact tokens and nulls; `260 + 18 + 22 = 300` tokens in edited units, read as nulls, or dropped. The "after" column uses the revised edition and corrected digits, [current alignment](https://simonklee.dk/static/writing/farnese-letter/edition/alignment.txt), final totals: `5993 + 365 = 6358` exact tokens and nulls; `154 + 10 + 6 = 170` tokens in the departure categories. Both tokens of an edited pair enter that category even if only one was altered. Supplied letters consume no source tokens and therefore do not increase these counts.

33. Marco Grilli, Segretario della Prefettura, Archivio Apostolico Vaticano, email to the author, 16 September 2026; private correspondence. The report concerns index 1017 for Segr. Stato, Principi 14A, the register Cardauns cited as Principi 14. It does not report a folio-by-folio examination of the register and does not establish that no copy survives. The email itself is not reproduced here.

34. AAV, Spagna 1A, ff. 70r–70v; edited decipherment, [70r](https://simonklee.dk/farnese-letter/edition/plaintext.md#070r) and [70v](https://simonklee.dk/farnese-letter/edition/plaintext.md#070v), from *Dopo la partita* to *secondo che V.S. scri\[u\]e per le sue*. The letter says a copy of Doria's written summary accompanies it; that enclosure has not been identified here. For Aguilar's identification as Juan Fernández Manrique de Lara y Pimentel and his Roman embassy, see Cascella Alcaraz (2025), pp. 63–64. For Andrea Doria's imperial naval command, Edoardo Grendi, "DORIA, Andrea," DBI 41 (1992), [online entry](https://www.treccani.it/enciclopedia/andrea-doria_%28Dizionario-Biografico%29/), the 1528 *asiento* paragraph (accessed 16 September 2026).

35. AAV, Spagna 1A, ff. 70v–71r; [edition, 70v](https://simonklee.dk/farnese-letter/edition/plaintext.md#070v), *acciò che non si cadesse in questo errore di spender in vano in un luogo che manco lo ricercasse, et non poter di poi supplir a l'altro dove fusse maggior il pericolo*. The English quotation translates this passage.

36. AAV, Spagna 1A, f. 71r; [edition](https://simonklee.dk/farnese-letter/edition/plaintext.md#071r), *armar le cento navi* through *sua parte che \[l\]i toccherà*. The judgment about mixed fleets is the Pope's argument as reported in the letter. *Navi* is rendered as sailing ships in contrast to *galere*; the six galleys are explicit in the decipherment.

37. AAV, Spagna 1A, ff. 71r–71v; [edition, 71r](https://simonklee.dk/farnese-letter/edition/plaintext.md#071r), *Ma quanto a le fanterie*, continuing on [71v](https://simonklee.dk/farnese-letter/edition/plaintext.md#071v) to *per la difesa dal Turco*.

38. AAV, Spagna 1A, ff. 71v–72r; [edition, 71v](https://simonklee.dk/farnese-letter/edition/plaintext.md#071v), *tra le quali è lo aiuto di Ungaria*, continuing on [72r](https://simonklee.dk/farnese-letter/edition/plaintext.md#072r). The corrected reading *la S.M.tà \[h\]a voluto* attributes the request for a public offer to the Emperor. The enclosed *capitulo* has not been identified as a separate witness. Speyer is named in the cleartext on [73r](https://simonklee.dk/farnese-letter/edition/plaintext.md#073r), *della \[dieta\] di Spira*. Massimo Firpo, "MORONE, Giovanni," DBI 77 (2012), [online entry](https://www.treccani.it/enciclopedia/giovanni-morone_%28Dizionario-Biografico%29/) (accessed 16 September 2026), confirms his bishopric and attendance at Speyer in 1542. Granvelle here is Nicolas Perrenot: Gayangos (1895), no. 2, pp. 2–7, especially [p. 3 and its identifying note](https://www.british-history.ac.uk/cal-state-papers/spain/vol6/no2/pp1-13), and no. 6, pp. 10–11, addressed to him as the Emperor's *Garde-sceaux*.

39. AAV, Spagna 1A, ff. 72v–73r; [edition, 72v](https://simonklee.dk/farnese-letter/edition/plaintext.md#072v), *Il Signor Ridolfo Go\[n\]zaga*, continuing on [73r](https://simonklee.dk/farnese-letter/edition/plaintext.md#073r) to *Vederassi il successo*. The unidentified employer and conjectural castle name remain open; this summary does not independently establish the troop movements. For the identification of the Marchese del Vasto as Alfonso d'Avalos, governor of Milan from 1538, see Gaspare De Caro, "AVALOS, Alfonso d', marchese del Vasto," DBI 4 (1962), [online entry](https://www.treccani.it/enciclopedia/avalos-alfonso-d-marchese-del-vasto_%28Dizionario-Biografico%29/), the paragraph beginning *Alla morte del Caracciolo* (accessed 16 September 2026).

40. Morone to Farnese, Speyer, Lämmer, no. CCXXXVIII, pp. 419–423, especially [p. 420](https://archive.org/details/monumentavatica01laemgoog/page/420/mode/2up): *Alli XXIII. hebbi audientia publica* and *esposi la mente di N. S. sopra l'aiuto contra il Turcho*. The response acknowledges his proposal in the Pope's name. Lämmer's heading dates the report 28 March; Cardauns, p. 127 n. 1, refers to it as 29 March. The presentation's date, 23 March, is explicit in the text. Morone's report of 30 March, Cardauns, no. 63, pp. 127–130, at [128, lines 6–17](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n87/mode/2up), says *Quanto al aiuto contra il Turcho tutti si aggravano parendoli poco*; the majority wanted 5,000 infantry without conditions and 2,000 cavalry. These passages establish the presentation and dissatisfaction, not Charles V's personal instruction or the identity of the letter's enclosure. Earlier discussions with the Emperor at Lucca and then Granvelle are attested in Farnese to Verallo, 7/10 January 1542, Cardauns, no. 93, pp. 192–195, at [193](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n119/mode/2up). That passage does not independently establish the precise Roman settlement described in the decipherment.

41. Pastor, V (1909), pp. 456–458, especially [457](https://archive.org/download/geschichtederp05past/page/n504.jpg): Charles V arrived and met Paul III on 12 September 1541; extended discussions began the next day. Károly Magyar, "Buda in the Turkish Era," *The Castle of Buda*, signed institutional account credited to the Budapest History Museum and HAS Research Centre for the Humanities, [part 1, final paragraph](https://budavar.abtk.hu/en/the-history-of-the-site/buda-in-the-turkish-era.html) (accessed 16 September 2026), dates the Ottoman occupation to 29 August. The interval to their first meeting was fourteen days.

42. Gairdner and Brodie (1900), p. 287, [no. 492, "The War"](https://www.british-history.ac.uk/letters-papers-hen8/vol17/pp286-300), calendars Francis I's proclamation against the Emperor, dated Ligny, 12 July 1542, from a copy at Simancas. For Ricci's return to Rome on 22 July, see Fragnito, "Ricci," and Pastor, V, [p. 472](https://archive.org/download/geschichtederp05past/page/n519.jpg). The quotation is in Verallo to Farnese, Nuremberg, 29/30 July, Cardauns, no. 112, pp. 229–233, at [231, the 30 July continuation](https://archive.org/details/berichte-vom-regensburger-und-speierer-reichstag/page/n138/mode/2up): *la Mtà del re mi ha communicato* that Montepulciano had returned and *la pratica della pace era exclusa*. Verallo is reporting Ferdinand's account. Ricci's mission had failed; papal mediation continued, with new peace legates appointed on 7 August (Pastor, p. 472).
