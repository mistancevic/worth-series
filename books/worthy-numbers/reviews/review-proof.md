# Worthy Numbers: final proof report

Checked: book-text.md plus all eleven rendered pages (01.png to 11.png).

## Summary

- Arithmetic: every sum and every PD recomputes correctly, with one rounding error (skyr PD on page 8).
- Cross-references and contents: all correct. Page 5 points to page 8 (PD) and page 8 points to page 5 (claims). The contents page numbers 3 to 10 match the page footers.
- Food values: the same everywhere. Granola is 450 kcal and 9 g per 100 g, milk 1.5% is 47 kcal and 3.4 g per 100 ml, and skyr is 63 kcal and 11 g per 100 g.
- House rules: no em or en dashes, no "floor", "lamp" or "corridor", no question marks, no -ly intensifiers ("rarely" and "only" are not intensifiers). "Chef Mealan" is spelled correctly everywhere. There are two passive constructions (pages 4 and 6).
- Spelling: UK spelling throughout ("glycaemic", "fibre"). "carbohydrate" is always singular. Units and numbers follow one format: "60 g", "200 ml", "2,800", "1,700", "1.5%".
- Must fix before print: page 9 "150 G", page 8 "about 18", page 11 "Chef / Mealan" line break, page 11 heading comma collision.

## Global (all pages)

1. **Straight quotes and apostrophes.** Every apostrophe and quote mark is the straight typewriter form: maker's (p3), can't / IT CAN'T (p4), "High protein" (p5 heading), won't (p6), I'm (p10). Printed books normally use typographic marks. Correction: ' → ’ and "…" → “…” throughout, including the uppercase "IT CAN'T" label on page 4.

## Page 1

Clean.

## Page 2

Clean. Contents rows and page numbers match the footers on pages 3 to 10.

## Page 3

Clean. Checked: 450 × 0.6 = 270, 18 → 10.8, 3 → 1.8, 60 → 36, 20 → 12, 9 → 5.4, 0.3 → 0.18, shown as 0.2 (acceptable rounding).

## Page 4

1. **Passive voice.** Current: "The letter is made for one job: comparing products of the same kind." Correction: "The letter does one job: comparing products of the same kind."
2. **Serial comma, inconsistent.** Current: "how much you eat, what you eat it with, or what your day needs." The rest of the book drops the comma before the last item ("Spain and Switzerland", "protein, fat and fibre", "sleep and recovery"). Correction: "how much you eat, what you eat it with or what your day needs."
3. **Capital after a label.** Current box text: "IT CAN'T / Tell you whether your lunch fits your day." The box text continues the label's sentence, so the capital T reads wrong. Correction: "tell you whether your lunch fits your day." (or keep the capital if the house treats each box as its own line; the "IT HELPS" box starts a new sentence, so the two boxes behave differently).
4. **Layout: early line break.** The first paragraph breaks before "An updated formula…" although "An" fits on the line above, and "most of" ends a short line with "these countries." alone below. It looks like a hard return. Correction: remove the forced break (or `text-wrap: pretty`) so the paragraph wraps normally.

## Page 5

Arithmetic checked: bar 13 g × 4 = 52 kcal of 250 = 20.8%, so "20%" holds. Skyr 200 g = 126 kcal ("about 125") and 22 g × 4 = 88 kcal = 69.8% ("About 70%"). Bar lengths and the 12% and 20% markers sit at the right positions.

1. **Unclear chart label.** Current: "12% · 20% marked". Correction: "lines at 12% and 20%".
2. **Label inconsistency (query).** The bar row reads "20%: High protein", while the skyr row reads only "About 70%", although skyr also qualifies. A reader may conclude skyr does not qualify. Correction: "About 70%: High protein".
3. **Capitalisation of "about".** Left label "About 70%" has a capital, while the right-hand labels "about 13 g protein", "about 125 kcal" and "about 22 g protein" are lower case. Correction: "about 70%" (or apply item 2, where the capital is fine at the start of the label).

## Page 6

1. **Passive voice.** Current: "Protein is built from amino acids, and some of them only food can give you." Correction: "Protein consists of amino acids, and some of them only food can give you."
2. **Layout: chart label misaligned.** The PDCAAS "1.0" axis label sits about 15 px left of its marker, while the DIAAS "1.0" label sits centred under its marker. The two 1.0 markers also sit about 7 px apart vertically. Correction: centre the PDCAAS "1.0" label under its marker and line up both 1.0 markers at the same x position.
3. **Layout: cramped bottom.** The "Use it" box ends about 40 px above the footer, much closer than on pages 3, 4, 5 and 7. Correction: tighten the chart padding or the paragraph spacing so the box clears the footer like the other pages do.

## Page 7

Clean. Checked: 60 × 15 ÷ 100 = 9 (low), 60 × 30 ÷ 100 = 18 (medium), and the bars and the 10 and 20 markers sit at the right positions on the scale. "glycemicindex.com" keeps the US spelling because it is a URL. That is correct.

## Page 8

Arithmetic checked: granola 9 ÷ 450 × 100 = 2. 12% of energy = 3 g per 100 kcal = PD 3, and 20% = PD 5. 180 ÷ 2,800 × 100 = 6.43, so 6.4. Chicken 150 g plus cooked rice 200 g comes to about 52 g protein in 508 kcal, so PD about 10.

1. **Rounding error.** Current: "about 18 / skyr". Skyr is 11 ÷ 63 × 100 = 17.46, which rounds to 17, not 18. Page 5 also gives 22 g in 126 kcal = 17.5. Correction: "about 17", and move the skyr dot to 17 on the scale (or use "about 17.5" and place the dot there).
2. **Rice weight (query).** Current: "chicken 150 g, rice 200 g". PD about 10 holds only for cooked rice. With 200 g of dry rice the plate comes to about PD 6. Correction: "chicken 150 g, rice 200 g cooked".
3. **Layout: chart label off-centre.** "about 10" and "chicken 150 g, rice 200 g" are left-aligned at the target line instead of centred on their dot, unlike the granola and skyr labels. Correction: centre both labels on the dot at 10. The longer line still fits between the target marker and the skyr label.

## Page 9

Arithmetic checked: as poured, 270 + 94 = 364 kcal and 5.4 + 6.8 = 12.2 g, so PD 3.35, shown as 3.4. With skyr, + 94.5 kcal and + 16.5 g gives 458.5 kcal (459) and 28.7 g, so PD 6.26, shown as 6.3. Protein share: 48.8 ÷ 364 = 13.4% (13%) and 114.8 ÷ 458.5 = 25.0% (25%). Carbohydrate: granola 36 g against about 10 g from the milk and 6 g from the skyr, so "Most carbohydrate comes from the granola" holds.

1. **Unit in capitals.** Current rendered label: "WITH 150 G SKYR". The uppercase style turns the gram symbol into "G", which is a different unit. Correction: keep the unit in lower case ("WITH 150 g SKYR") by excluding it from the text transform, or set the label in sentence case.
2. **Missing "of".** Current: "With 150 g skyr". The body text says "150 g of skyr". Correction: "With 150 g of skyr".
3. **Table punctuation.** The "Claim" row has full stops ("With skyr, 25% of the energy is protein. As poured, 13%."), while every other row is a fragment without a full stop. Correction: "With skyr, 25% of the energy is protein; as poured, 13%" (no final full stop).
4. **Sentence starting with a figure.** Current: "6.3 is close to the example target of 6.4, so this bowl fits." Correction: "PD 6.3 is close to the example target of 6.4, so this bowl fits."
5. **Layout: card text not aligned.** In the two cards at the top, the second line sits lower in the blue card ("459 kcal · 28.7 g protein" at about y 547) than in the white card ("364 kcal · 12.2 g protein" at about y 540). Correction: align the eyebrow, PD figure and kcal line baselines across both cards.

## Page 10

1. **Stranded "I".** Rendered line: "B2B and B2B2C software products as a product manager. I / founded several startups…". A one-letter word at the end of a line reads badly. Correction: a non-breaking space between "I" and "founded".
2. **Compound modifier (optional).** Current: "an event planning app". Correction: "an event-planning app".

The photo is a placeholder in this proof, so the photo itself was not checked.

## Page 11

Arithmetic checked: 125 ÷ 1,700 × 100 = 7.35, shown as PD 7.4.

1. **Name split across lines.** Rendered: "…sleep and recovery. Chef / Mealan supports you on that journey." Correction: a non-breaking space in "Chef Mealan" (apply it to every instance in the book).
2. **Layout: heading collision.** The comma after "LIVE THE DAY," descends into the top of the "S" in "COUNTS" on the line below. Correction: increase the heading line height slightly, or nudge the second line down, so the comma clears the S.
3. **Widow.** Rendered: "…and you get your code within a / day." Correction: a non-breaking space in "a day", or rebalance the paragraph so "day." does not sit alone on the last line.
4. **Layout: cramped rule.** The thin divider under the red "Get your personal code" box sits almost on the box border (about 4 px gap). Correction: add space above the divider to match the gap below it.
5. **Source text only (no render issue).** In book-text.md the full stop after "chefmealan.com/worthy-numbers" sits on its own line. The render shows "worthy-numbers. Leave" correctly, so check only that the period does not end up inside the link target.
