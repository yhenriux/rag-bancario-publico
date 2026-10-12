# Supplementary method and provenance

This supplement preserves the question matrix, earlier statistical planning, and technical records accompanying partial generation. The collection, questions, anchors, and original rankings remain fixed. Unavailable earlier raw calibration outputs remain an identified provenance gap.

## Appendix A Question by configuration matrix

The matrix gives the question identifier (ID), bank, class, number of distinct anchors (N), and five configurations for thirty questions. Each configuration cell contains the first anchor's rank within ten published positions, recall@5, and coverage@5, in that order. NR means no anchor retrieved within the limit; NA means a question without references. An anchor can rank sixth and have recall@5 equal to zero. Initial rank does not certify semantic sufficiency. JSON files contain individual anchor positions and results at all four cutoffs.

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

## Appendix B Complementary method and analytical history

These procedures contextualize the change in scope and do not constitute confirmatory results of the documentary study.

### B.1 Environment budget and resumption

The retriever is multilingual-e5-large-instruct, running on the central processing unit with 32-bit precision. The generator is Qwen3-8B in GGUF Q4_K_M format, executed through llama.cpp b11557. Quantization compresses weight representation. Revisions, hashes, and installed versions form part of the execution record. Hashes identify file bytes and enable change checks, while content validity depends on specific evaluation.

The server uses an 8,192-token context, eight threads, a batch of 512, and a micro-batch of 128. Internal weight repacking and the global prompt cache remain disabled under the environment's memory limit. The session cache retains consecutive inputs. Public records describe earlier technical attempts. Partial answers from those attempts, unavailable after the pause, are excluded from the current analysis.

Input allows up to 4,096 tokens and output up to 512. Retrieval records ten ranks; prepared context starts with up to five passages. When input exceeds its limit, the executor removes the last passage and records the removal. Main generation uses temperature zero, seed 42, and repetition penalty one. Technical controls show no need for an additional penalty.

The stability plan uses seeds 43 and 44, temperature 0.7, top_p 0.8, and top_k 20 in A, B, and C. Rounding by bank and class selects ten questions, 50% of the pilot. The planned budget combines 120 main and sixty additional answers, totaling 180. The second set plans sixty main answers, which were not generated. The executor saves each combination and reuses partial records only when inputs, parameters, and execution environment identity match earlier records.

### B.2 Fidelity calibration and provenance

Twelve synthetic controls check monetary values, percentages, dates, and source identifiers. Each case uses the main policy and two stability seeds, totaling 36 outputs and 144 required items. Checking searches for explicit equivalents, records output limits and input truncation, and detects blocks of at least twenty tokens repeated three times. It evaluates literal preservation of known items under delimited conditions.

A repetition penalty can affect evidence tokens. Execution uses a neutral penalty and checks items under all three seed policies. Transformers behavior does not certify another runtime's behavior. Records therefore retain effective llama.cpp parameters, its executable, and returned tokens. Fidelity controls are repeated under the configuration adopted for current execution.

Calibration requires at least nineteen correct judgments out of twenty controls and structural validity of all outputs. The plan allows one instruction correction and a second round. Published reports record ten correct judgments in the first round and seventeen in the second. Controls include numerical errors, fabricated sources, incompatible audiences, omitted conditions, ambiguity, and lack of evidence. Second-round performance remains below threshold and ends calibration, with automatic adequacy disabled for banking answers.

Calibration precedes operational memory adjustments. The decision to exclude the evaluator remains valid for current execution. Earlier raw outputs were not recovered after the pause; this gap accompanies public reports. The study does not reopen evaluator selection using banking answers. There was no independent human judgment, agreement calculation between people, or assignment of semantic scores to technical failures.

Generation retains 56 pilot answers against a target of 180; the sixty planned second-set answers were not generated. Interruption determines subset composition. Diagnostics of the 56 saved answers detect no execution failures, output-limit termination, degenerate repetition, or identifiers cited outside the received evidence. In the 36 current controls, all 144 required items are preserved, without truncation or degenerate repetition. These results describe technical integrity and literal preservation; semantic correctness remains without validated evaluation.

Code checks verify resumption and rejection of conflicting final controls. Calibration reports and technical records remain public. Answer diagnostics check failure, output limit, truncation, repetition, and bracketed citations. A valid identifier belongs to input evidence; validity does not demonstrate support for an assertion. The interrupted subset includes different seeds for some inputs, without a composition supporting general stability estimation. Banking answers receive no scores attributed to human judgment.

### B.3 Earlier sample sizing and intervals

Confirmatory sizing in the original protocol uses discordant pairs. Parameters are discordance q = 0.25, difference of interest Δ = 0.10, power 80%, β = 0.20, and α* = 0.05 divided by three. Equation 1 yields 258.98 pairs and establishes a threshold of 260 eligible condition and exception families. This calculation belongs to earlier planning and contextualizes the distance between its target and the implemented sample.

EQUACAO_PODER

The alternative precision plan requires approximately 97 independent pairs for a ten-percentage-point half-width in a normal 95% interval, with discordance 0.25. Illustrative simulations with two thousand repetitions examine discordances 0.10, 0.25, and 0.40. The second set contains four condition and exception families, below power and precision targets. Intervals describe variation in the sample and do not expand its representativeness.

B minus A and B minus Bp use condition and exception questions. C minus B uses questions with prepared attributes, including assisted inferences. The 95% and 98.33% percentile intervals come from the same five thousand family resamples, stratified by bank, with seed 2026. The report indicates whether the point estimate reaches ten percentage points and whether its absolute magnitude reaches that value. All comparisons remain exploratory.

Table B1 Anchor retrieval and coverage within the first five positions

| Configuration | Pilot recall (16) | Pilot coverage (16) | Second-set recall (8) | Second-set coverage (8) |
|---|---:|---:|---:|---:|
| A | 90.625% | 87.500% | 87.500% | 87.500% |
| B | 90.625% | 87.500% | 100.000% | 100.000% |
| C | 96.875% | 93.750% | 87.500% | 87.500% |
| Bp | 96.875% | 93.750% | 100.000% | 100.000% |
| L | 93.750% | 93.750% | 100.000% | 100.000% |

Source: calculations on published rankings and assisted references. Parenthesized numbers indicate eligible questions.

In the pilot, B minus A and B minus Bp have a recall difference of −12.5 percentage points across eight condition and exception questions. Both 95% and 98.33% percentile intervals range from −42.86 to zero points. C minus B has a difference of 6.25 points across sixteen eligible questions. Its 95% interval ranges from zero to 21.43 points; its 98.33% interval ranges from zero to 25. Coverage comparisons have the same estimates and intervals.

In the second set, B minus A and B minus Bp have zero differences across four condition and exception questions and zero-to-zero intervals. This follows from the absence of observed differences and does not establish general equivalence. C minus B has a difference of −12.5 points across eight eligible questions, with both intervals from −37.5 to zero. The historical ten-point criterion mechanically identifies the negative 12.5-point differences and leaves the 6.25-point gain below threshold. Within this sample, this classification does not establish empirical relevance or confirmatory support.

Intervals are percentiles of resamples of observed families. In the small sample, a single discordant family can be absent from a repetition, producing a zero bound. Zero-to-zero intervals arise when observed pairs tie; they do not demonstrate population equivalence. The article prioritizes counts and diagnosis by question. All five thousand resamples, seed 2026, and bank stratification remain in historical reports to reproduce the earlier analysis.

## Scope of bibliographic consultation

Limited consultation of abstract and bibliographic metadata refers specifically to Wilson (1999). Dadopoulos et al. (2025) was consulted in full text, focusing on method and retrieval and generation comparisons. ISO 25964-1 is cited using its public scope description; the complete paid standard was not accessed. SKOS is used conceptually, without a claim that the implementation conforms to it.

Published versions of Lewis et al. (2020) and Joren et al. (2025) are identified as conference proceedings. Joren's OpenReview address was identified, but direct access encountered browser verification; the authors' arXiv version identifies ICLR 2025 publication on its first page. OmniEval's definitive page gives pages 5726–5751. The Contextual Retrieval page credits Daniel Ford for research and writing; the engineering address is used.

Hjørland's articles on knowledge organization and thesauri and Tudhope and Binding's discussion were consulted in publisher PDFs, focusing on concepts and positions about semantic relations. RAGAS and ARES were consulted in ACL PDFs. Their citation situates the separation between context and answer evaluation; neither tool was executed in the experiment.

CMN Resolution No. 3,919 was checked in the v7 version published by Banco Central do Brasil, consulted on 12 October 2026. Article 2, I, b retains the exception for loss. The v7 reference documents the consolidated text consulted; the filename's version number alone does not certify the current legal status of every provision. Regulatory consultation complements discussion and does not alter the banking corpus.

The public ISO description supports the limited statement about the standard's purpose. Restricted consultation of Wilson remains declared. OmniEval retains pages 5726–5751 from its definitive source. Equation 1 remains a native editable Word equation with two square roots and one fraction.
