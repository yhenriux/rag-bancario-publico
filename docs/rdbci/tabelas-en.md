# Editable tables and frames

This file contains the seven tables and frames from the article and supplements. Values preserve published results.

Frame 1 Document retrieval configurations

| Code | Retrieval | Documentary decision |
|---|---|---|
| A | Semantic retrieval of original passage | Without additional contextual header |
| B | Semantic retrieval with complete contextual header | Title section type product and audience |
| C | B retrieval with filtering | Product and audience prepared for the question |
| Bp | Semantic retrieval with reduced contextual header | Product and audience |
| L | BM25 lexical retrieval | Term matching |

Source: study preparation, 2026.

Table 1 Anchor ranking and retrieval by set

| Set / configuration | Recall@1 | Recall@3 | Recall@5 | Recall@10 | MRR@10 |
|---|---:|---:|---:|---:|---:|
| Pilot / A | 71.9% | 90.6% | 90.6% | 90.6% | 0.844 |
| Pilot / B | 65.6% | 90.6% | 90.6% | 100.0% | 0.812 |
| Pilot / C | 71.9% | 90.6% | 96.9% | 100.0% | 0.849 |
| Pilot / Bp | 65.6% | 90.6% | 96.9% | 96.9% | 0.825 |
| Pilot / L | 62.5% | 93.8% | 93.8% | 100.0% | 0.820 |
| Second set / A | 75.0% | 87.5% | 87.5% | 100.0% | 0.830 |
| Second set / B | 62.5% | 100.0% | 100.0% | 100.0% | 0.792 |
| Second set / C | 50.0% | 87.5% | 87.5% | 87.5% | 0.667 |
| Second set / Bp | 75.0% | 87.5% | 100.0% | 100.0% | 0.844 |
| Second set / L | 87.5% | 100.0% | 100.0% | 100.0% | 0.917 |

Source: published rankings and assisted references. Denominators: sixteen pilot questions and eight second-set questions. MRR@10 is mean reciprocal first-anchor rank within ten passages.

Table 1a Retrieval and initial access by bank

| Bank / set / configuration | N | Recall@1 | Recall@3 | Recall@5 | MRR@10 |
|---|---:|---:|---:|---:|---:|
| Inter / pilot / A | 8 | 87.5% | 100.0% | 100.0% | 0.938 |
| Inter / pilot / B | 8 | 87.5% | 100.0% | 100.0% | 0.938 |
| Inter / pilot / C | 8 | 100.0% | 100.0% | 100.0% | 1.000 |
| Inter / pilot / Bp | 8 | 87.5% | 100.0% | 100.0% | 0.938 |
| Inter / pilot / L | 8 | 75.0% | 100.0% | 100.0% | 0.875 |
| Inter / second set / A | 4 | 100.0% | 100.0% | 100.0% | 1.000 |
| Inter / second set / B | 4 | 75.0% | 100.0% | 100.0% | 0.875 |
| Inter / second set / C | 4 | 75.0% | 100.0% | 100.0% | 0.875 |
| Inter / second set / Bp | 4 | 100.0% | 100.0% | 100.0% | 1.000 |
| Inter / second set / L | 4 | 100.0% | 100.0% | 100.0% | 1.000 |
| Bradesco / pilot / A | 8 | 56.2% | 81.2% | 81.2% | 0.750 |
| Bradesco / pilot / B | 8 | 43.8% | 81.2% | 81.2% | 0.688 |
| Bradesco / pilot / C | 8 | 43.8% | 81.2% | 93.8% | 0.698 |
| Bradesco / pilot / Bp | 8 | 43.8% | 81.2% | 93.8% | 0.713 |
| Bradesco / pilot / L | 8 | 50.0% | 87.5% | 87.5% | 0.766 |
| Bradesco / second set / A | 4 | 50.0% | 75.0% | 75.0% | 0.661 |
| Bradesco / second set / B | 4 | 50.0% | 100.0% | 100.0% | 0.708 |
| Bradesco / second set / C | 4 | 25.0% | 75.0% | 75.0% | 0.458 |
| Bradesco / second set / Bp | 4 | 50.0% | 75.0% | 100.0% | 0.688 |
| Bradesco / second set / L | 4 | 75.0% | 100.0% | 100.0% | 0.833 |

Source: subsequent calculations on frozen rankings. N is the number of eligible questions in the stratum. Recall@10 and bank-level coverage are included in the data report.

Table 2 Discordant questions within the first five positions

| Set / comparison | Eligible | First wins | Second wins | Ties |
|---|---:|---|---|---:|
| Pilot / B × A | 8 | 0 | 1 (B05) | 7 |
| Pilot / B × Bp | 8 | 0 | 1 (B05) | 7 |
| Pilot / C × B | 16 | 1 (B05) | 0 | 15 |
| Second set / B × A | 4 | 0 | 0 | 4 |
| Second set / B × Bp | 4 | 0 | 0 | 4 |
| Second set / C × B | 8 | 0 | 1 (BF04) | 7 |

Source: subsequent analysis of frozen rankings. Counts are identical for recall@5 and coverage@5. First and second refer to configuration order in the comparison.

Frame 2 Diagnostics and documentary interventions

| Occurrence | Record used | Intervention |
|---|---|---|
| Specific product loses its broader-category relation | BF04 and exclusion trail | Record hierarchy and test expanded selection |
| Candidate reduction favors a reference | B05 and ranking by configuration | Examine filtering by question class |
| Reference absent from early ranks | Anchors and ten published ranks | Review description segmentation and passage competition |
| Input budget removes evidence | Effective input list | Combine rule and condition or adjust priority |
| Evaluator misjudges known controls | Two published calibration rounds | Exclude adequacy from main measures |

Source: study preparation, 2026. The budget row describes a control mechanism; effective-context records indicate whether it occurred in this execution.

Table A1 Initial rank recall and coverage by question

| ID | Bank | Class | N | A | B | C | Bp | L |
|---|---|---|---:|---|---|---|---|---|
| I01 | Inter | direct | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I02 | Inter | direct | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| I03 | Inter | condition | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I04 | Inter | condition | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I05 | Inter | exception | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I06 | Inter | exception | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I07 | Inter | ambiguity | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I08 | Inter | ambiguity | 3 | 2/1/1 | 2/1/1 | 1/1/1 | 2/1/1 | 2/1/1 |
| I09 | Inter | insufficient evidence | 0 | NA | NA | NA | NA | NA |
| I10 | Inter | insufficient evidence | 0 | NA | NA | NA | NA | NA |
| B01 | Bradesco | direct | 1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 |
| B02 | Bradesco | direct | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 8/0/0 |
| B03 | Bradesco | condition | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| B04 | Bradesco | condition | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B05 | Bradesco | exception | 1 | 1/1/1 | 6/0/0 | 4/1/1 | 2/1/1 | 1/1/1 |
| B06 | Bradesco | exception | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B07 | Bradesco | ambiguity | 2 | NR/0/0 | 3/1/1 | 3/1/1 | 5/1/1 | 1/1/1 |
| B08 | Bradesco | ambiguity | 2 | 2/0.5/0 | 2/0.5/0 | 2/0.5/0 | 2/0.5/0 | 1/1/1 |
| B09 | Bradesco | insufficient evidence | 0 | NA | NA | NA | NA | NA |
| B10 | Bradesco | insufficient evidence | 0 | NA | NA | NA | NA | NA |
| IF01 | Inter | direct | 4 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF02 | Inter | condition | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF03 | Inter | exception | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF04 | Inter | ambiguity | 1 | 1/1/1 | 2/1/1 | 2/1/1 | 1/1/1 | 1/1/1 |
| IF05 | Inter | insufficient evidence | 0 | NA | NA | NA | NA | NA |
| BF01 | Bradesco | direct | 1 | 7/0/0 | 3/1/1 | 3/1/1 | 4/1/1 | 3/1/1 |
| BF02 | Bradesco | condition | 1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 1/1/1 |
| BF03 | Bradesco | exception | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| BF04 | Bradesco | ambiguity | 2 | 1/1/1 | 1/1/1 | NR/0/0 | 1/1/1 | 1/1/1 |
| BF05 | Bradesco | insufficient evidence | 0 | NA | NA | NA | NA | NA |

Source: diagnosis of published rankings and assisted reference dossiers, 2026.

Table B1 Anchor retrieval and coverage within the first five positions

| Configuration | Pilot recall (16) | Pilot coverage (16) | Second-set recall (8) | Second-set coverage (8) |
|---|---:|---:|---:|---:|
| A | 90.625% | 87.500% | 87.500% | 87.500% |
| B | 90.625% | 87.500% | 100.000% | 100.000% |
| C | 96.875% | 93.750% | 87.500% | 87.500% |
| Bp | 96.875% | 93.750% | 100.000% | 100.000% |
| L | 93.750% | 93.750% | 100.000% | 100.000% |

Source: calculations on published rankings and assisted references. Parenthesized numbers indicate eligible questions.