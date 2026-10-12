# Knowledge organization in banking RAG: evidence retrieval from Brazilian public documents

## Abstract

Introduction: Document organization influences which evidence reaches the generation stage in RAG systems. Objective: To examine how contextual headers and product and audience filters change banking evidence retrieval. Methodology: A diagnostic, quantitative, exploratory case study using 27 public pages from two Brazilian banks and 62 passages, compared across five retrieval configurations. Twenty pilot questions and ten questions from new rule families in a second set use anchors, short reference passages prepared with artificial intelligence assistance. Results: Within the first five positions, filtering retrieves the reference for one of sixteen eligible pilot questions where unfiltered retrieval leaves it out. For one of eight eligible questions in the second set, filtering excludes both anchors because the catalogue lacks the relation between Aeternum and the card category. A deterministic check documents the dependence of the gain on inferred attributes. In the second set, lexical retrieval and retrieval with complete headers find all anchors within three positions; lexical retrieval provides the best initial access. Conclusion: The data support diagnosis of ranking and reference exclusion. The small sample and shared preparation limit generalization; semantic answer adequacy remains outside the evaluated scope.

Keywords: Knowledge representation; Information retrieval; Metadata; Artificial intelligence; Documentation.

## Organização do conhecimento em RAG bancário: recuperação de evidências em documentos públicos brasileiros

## Resumo

Introdução: A organização documental influencia quais evidências chegam à etapa de geração em sistemas RAG. Objetivo: Examinar como cabeçalhos contextuais e filtros de produto e público alteram a recuperação de evidências bancárias. Metodologia: Estudo de caso diagnóstico, quantitativo e exploratório, com 27 páginas públicas de dois bancos brasileiros e 62 trechos, comparados em cinco configurações de busca. Vinte perguntas do piloto e dez de famílias novas no segundo conjunto utilizam âncoras, passagens curtas preparadas como referência com assistência de inteligência artificial. Resultados: Nas primeiras cinco posições, o filtro recupera a referência em uma das dezesseis perguntas elegíveis do piloto que a busca sem filtro deixa de fora. Em uma das oito perguntas elegíveis do segundo conjunto, exclui as duas âncoras por ausência da relação entre Aeternum e cartão no catálogo. Uma verificação determinística documenta a dependência do ganho em relação a campos inferidos. No segundo conjunto, as buscas lexical e com cabeçalho completo recuperam todas as âncoras em três posições; a lexical apresenta o melhor acesso inicial. Conclusão: Os dados permitem diagnosticar ordenação e exclusão de referências. A amostra pequena e a preparação compartilhada limitam a generalização; a adequação semântica das respostas permanece fora do alcance avaliado.

Palavras-chave: Representação do conhecimento; Recuperação da informação; Metadados; Inteligência artificial; Documentação.

## 1 Introduction

A banking rule can be publicly available and still be difficult to find when a customer needs it. Documentation combines general rules, specific products, conditions, and exceptions. In retrieval-augmented generation (RAG), retrieval selects the evidence a model receives to formulate an answer. Organizing this documentation affects both passage ranking and inclusion in the candidate set. This article examines the retrieval stage.

The RAG literature describes contextual enrichment, lexical and semantic retrieval, filtering, and answer evaluation. Knowledge organization provides concepts for examining relations between the categories used in these operations. A specific product, such as the Aeternum card, can have its own name in a catalogue and also require a link to the card category. When the catalogue supports filtering, this relation directly affects access to evidence. Hierarchical relations are an established issue; the purpose here is to diagnose their manifestation in a retrieval implementation and document a way to check the mechanism.

The research question is: how do contextual headers and product and audience filters change the ranking and coverage of reference evidence in a collection of Brazilian public banking documents? The gap delimited by the consulted literature concerns the connection, within this scope, between document description, candidate exclusion, and diagnosis by question. The study provides a traceable analysis of these mechanisms, with short references linked to their source passages. The literature was selected for this problem, without claiming a systematic review or demonstrating an absence of studies on the topic.

The implemented design is a diagnostic, quantitative, exploratory case study. It contains 27 pages from Inter and Bradesco, 62 passages, twenty pilot questions, and ten questions from new families in a second set. Five configurations examine semantic retrieval, contextual enrichment, filtering, and lexical retrieval. Questions, attributes, and references share preparation assisted by artificial intelligence. This dependence limits interpretation of the comparisons and motivates a subsequent sensitivity analysis of two cases.

The initial protocol also planned to evaluate generated answers. The automatic evaluator fell below the calibration criterion, and generation remained partial. The decision to conclude the documentary analysis occurred after rankings for both sets and 56 answers were available. The article reports observed results and their limitations; Appendix B of the supplement retains the earlier planning and records for this module. The audience includes Information Science and information retrieval researchers, as well as professionals who organize document collections. The contribution is to make the path between labels, selection, ranking, and evidence found in this collection open to examination.

## 2 Knowledge organization and retrieval evaluation

### 2.1 Description categories and relations

Metadata describe documents or passages and help users locate them. Title, section, type, product, and audience constitute the description used in this study. Applicability attributes delimit the situation in which a rule applies, including age, channel, period, amount, and conditions of use. Product and audience enter the filter; other attributes remain in the text and reference dossiers. Compatibility in these two fields therefore covers part of applicability.

Hjørland (2016a) distinguishes organization processes, such as classification and indexing, from the systems of concepts and relations used in those processes. This perspective frames catalogue preparation and its use in retrieval as decisions that require examination together. In this study, a category can change passage representation and also operate as a selection requirement.

Hjørland (2016b) discusses diversity of meanings and the need to evaluate semantic tools in their domains of use. Tudhope and Binding (2016) argue for the continued relevance of thesauri, emphasizing semantic relations and linked data applications. This discussion recommends evaluating the usefulness of relations for a concrete task. The Aeternum-to-card relation is tested here only in a known case; its suitability for other queries requires classification criteria and new evidence.

ISO 25964-1 provides recommendations for developing and maintaining thesauri for information retrieval (International Organization for Standardization, 2011). The Simple Knowledge Organization System (SKOS) distinguishes concept labels and supports relations between broader and narrower concepts (Miles; Bechhofer, 2009). These references help distinguish a product name, its category, and the relation required by a query. The study implements literal selection by labels, without a formal thesaurus. The Aeternum-to-card relation receives a subsequent demonstration in the case where its absence excludes references.

The selection policy also needs to handle unknown values. Here, a field unspecified in the source retains the candidate, potentially increasing noise. Excluding every incomplete record could remove relevant rules. The choice expresses an evidence access policy that must accompany catalogue quality. Wilson (1999) situates searching in the context of information needs; within this scope, broad questions can require product identification before determining whether a condition applies. Consultation of Wilson covers the abstract and bibliographic metadata.

### 2.2 Retrieval enrichment and the financial domain

Lewis et al. (2020) combine retrieval and generation for knowledge-intensive tasks. The implementation examined here selects passages from the fixed collection; the generator receives these texts and does not consult additional websites. The multilingual-e5-large-instruct model belongs to the multilingual representation family described by Wang et al. (2024). BM25 ranks by term matching, frequency, and document length (Robertson; Zaragoza, 2009). Relative performance depends on queries and the collection, supporting retention of lexical retrieval as a comparison baseline.

Ford (2024) describes adding model-generated context before indexing and combining semantic retrieval with BM25. In this research, a contextual header is descriptive text added to a passage by deterministic rules. This header is distinct from the query instruction required by the E5 retriever. Semantic and lexical strategies are compared separately; their fusion in hybrid retrieval remains a design extension.

Dadopoulos et al. (2025) report improved answer quality with model-generated metadata, accompanied by retrieval losses in some comparisons. They also observe a retrieval decrease in a comparison combining file selection and query rewriting, discussing excessive restriction and rewriting effects. Their filter operates by file and includes other changes. This antecedent motivates separating retrieval and generation and examining selection losses, with caution when attributing an effect to one operation.

FinanceBench provides company-related questions with answers and evidence for evaluating financial question answering systems (Islam et al., 2023). Its domain differs from the customer help and product pages studied here. OmniEval combines GPT-4 case generation, human annotation, rule-based metrics, and fine-tuned evaluators to examine retrieval and generation in finance (Wang et al., 2025). These resources demonstrate the role of references and validation in financial evaluation; their results do not certify the local evaluator or this collection's references.

### 2.3 References ranking and judgment

Information retrieval evaluation relates a collection, queries, and relevance references. Measures at different ranking cutoffs distinguish early evidence access from retrieval at later positions (Manning; Raghavan; Schütze, 2008). Here, anchors are short passages prepared as references and identified by document, position, and hash. Recall measures the proportion of these anchors found; coverage checks whether a set specified in the dossier is complete. The first anchor's rank describes initial access and can coexist with other missing references.

Joren et al. (2025) examine context sufficiency. Sufficiency asks whether there is enough information to answer; applicability asks whether that information holds for the person and situation described. Coverage of the anchors selected in this study represents a documentary dossier criterion, whose semantic sufficiency remains dependent on the breadth of these references.

Zheng et al. (2023) describe position, verbosity, and self-favoring biases in evaluators based on language models. Using Qwen3-8B for generation and judgment introduces an additional risk to examine; this study does not estimate its magnitude. Calibration was performed and fell below the established threshold, so semantic scores were excluded. Technical diagnostics check execution and identifiers; assessing preservation of meaning, conditions, and expected action requires additional validation.

RAGAS distinguishes context relevance, faithfulness to context, and answer relevance through automated metrics (Es et al., 2024). ARES trains evaluators with synthetic data and uses a human-annotated sample to correct estimation errors (Saad-Falcon et al., 2024). These procedures help situate the difference between finding references and validating answers. This study calculates anchor retrieval, with semantic adequacy excluded after insufficient calibration. Neither system was executed in this analysis.

Shared preparation of questions, attributes, and dossiers can repeat interpretations and favor the source selected as a reference. Fixing files before generation protects chronology, while independent evaluation is needed to examine the validity of those interpretations. Subsequent analysis of inferred attributes makes part of this dependence visible, without retrospectively establishing independence.

## 3 Implemented method

### 3.1 Sources and selection criteria

The study is documentary, quantitative, and exploratory. The collection contains 27 official Inter and Bradesco pages about accounts, cards, and associated services. Inclusion requires public access, domain relevance, preservation of the consulted version, and usable extraction. Empty pages, access errors, and redirects outside the registered domain receive documented exclusion reasons. Collection covers public sources, without access to authenticated accounts, customer data, or internal documents.

Banco do Brasil and Caixa are included in initial selection and excluded after two limited rounds. Caixa routes produce circular redirects; the Banco do Brasil terms and extraction trail remains incomplete. These exclusions delimit execution, without establishing a general prohibition on collection.

Operational checking of policies, available terms, and access rules accompanies each batch. The record distinguishes the project's internal authorization and a redistribution license. Originals and prompts reproducing the texts remain in the researcher's private package. The public repository publishes addresses, hashes, positions, original questions, and derived indicators. Public access to the pages does not constitute the banks' express consent to reproduce their content.

The initial collection contains seventeen documents. Expansion examines thirteen addresses, produces eleven downloads, and retains ten extractions. Two collection failures and one empty extraction are recorded. After an environment pause, source recovery preserves 23 files with their earlier hashes and identifies changes in four. Inputs are reconstructed from this recovered version, whose differences are recorded before extended generation.

### 3.2 Assisted extraction and cataloguing

Extraction preserves source and positions. The extractor uses the body when the main element is empty or contains only a banner; when it identifies a main container, it selects its content and reduces menus. Checking is assisted by AI, without independent visual review or optical character recognition.

Segmentation uses up to 320 tokens per passage and an overlap of 48 tokens. Tokens are processing units that can correspond to word parts. Overlap preserves a shared region between adjacent passages. The recovered collection yields 62 passages. Earlier records remain in the history; this article's results use segments from the inputs fixed for the current execution.

Deterministic rules associate expressions in titles with products and expressions in the text with audiences. Audience occurrences receive source positions. Unknown values remain explicit. Expressions of conditions and exceptions are catalogued as documentary candidates, subject to content interpretation. The public catalogue contains labels and positional references, with complete texts preserved in the private package.

The main filter compares categories literally, without expanding their hierarchical relations. Metadata for the main results remain fixed. The subsequent demonstration of a relation between categories is recorded separately and uses an already observed case. This separation preserves the original comparison and identifies the intervention as subsequent analysis.

### 3.3 Questions and references

A family groups questions depending on the same rule. The pilot set contains twenty questions from fourteen families; the second set contains ten questions from ten new families. Each bank contributes two questions per class in the pilot and one per class in the second set. The five classes are direct, condition, exception, ambiguity, and insufficient evidence. Original experimental questions are in Portuguese; English examples are translations for reporting. The sample is below the initial target because preparation avoids multiplying paraphrases merely to reach a count without increasing rule diversity.

ChatGPT/Codex assists with questions and dossiers before generation. Each dossier specifies expected action, requirements, and anchors identified by document, position, and hash. These short references measure location and coverage; their breadth over the propositions needed for an answer requires separate evaluation.

Questions without support undergo lexical searching across the entire collection and assisted checking. Absence is relative to the collection. Fictional products not found are identified as such, avoiding their interpretation as actual services.

Question product and audience fields include explicit terms, normalizations, and domain inferences prepared with ChatGPT/Codex assistance. Conta You is associated with individuals; credit analysis with cards; debit card replacement with accounts and individuals. Execution does not use an attribute extractor validated on real questions. The subsequent audit records these decisions without changing inputs or rankings. Because field preparation and reference selection share assistance, this dependence can favor the filter.

All pilot families are excluded from the second set. The cash machine withdrawal rule used in the earlier technical test is also excluded. Additional-card benefits and Aeternum annual fee exemption form distinct families in the same document. Rule separation therefore retains residual document dependence, considered when interpreting the sample and intervals.

### 3.4 Retrieval configurations

All configurations restrict candidates to the bank specified in the question: eighteen Inter passages or 44 Bradesco passages before product and audience filtering. Frame 1 summarizes the operations. The no-document configuration, S, belongs only to the complementary generation module and has retrieval marked not applicable. The header changes the representation used for indexing; selected original texts, identifiers, titles, addresses, and positions form the generator's input, without the experimental header.

Frame 1 Document retrieval configurations

| Code | Retrieval | Documentary decision |
|---|---|---|
| A | Semantic retrieval of original passage | Without additional contextual header |
| B | Semantic retrieval with complete contextual header | Title section type product and audience |
| C | B retrieval with filtering | Product and audience prepared for the question |
| Bp | Semantic retrieval with reduced contextual header | Product and audience |
| L | BM25 lexical retrieval | Term matching |

Source: study preparation, 2026.

The multilingual-e5-large-instruct retriever runs on the central processing unit with 32-bit precision. BM25 uses k1 = 1.2 and b = 0.75. Configuration Bp, with description restricted to product and audience, already belongs to the original protocol and inputs fixed before pilot generation. It examines the additional title, section, and type fields included in B. Its differences do not isolate each attribute's effect.

### 3.5 Measures and diagnostic analysis

Anchor recall at cutoff k is the number of distinct anchors found within the first k passages divided by the dossier total. Anchors repeated in overlapping passages count once. Means weight each eligible question equally. Coverage equals one when at least one anchor set specified in the dossier is complete, and zero otherwise. Questions without references and configuration S receive not-applicable values. Appendix A of the supplement's matrix includes all thirty questions; means use sixteen in the pilot and eight in the second set.

Diagnostic analysis uses recall at positions 1, 3, 5, and 10, each anchor's position within the ten published ranks, and the mean reciprocal rank of the first anchor, termed MRR@10. A question with no anchor within this limit receives reciprocal rank zero; a question without references receives not applicable. MRR@10 measures access to the first reference, while recall and coverage examine the set. This analysis follows ranking fixation and uses frozen files, preserving original results.

The B minus A and B minus Bp comparisons cover condition and exception questions. C minus B covers eligible questions with prepared attributes. Counts indicate how many questions each configuration outperforms the other on, and how many tie. The main presentation uses discordant cases and descriptive measures. Earlier bootstrap intervals and the ten-percentage-point criterion remain in Appendix B of the supplement as analytical history, since the sample offers little discrimination for inference.

Diagnosis distinguishes exclusion of a passage containing a reference from leaving an anchor without any passage containing it. It also checks evidence selected after any removals due to the input budget. Rankings retain ten positions, and context starts with up to five passages. Ranking and effective context are separate files, enabling identification of selection and technical-limit effects.

The subsequent dependence check covers B05 and BF04. It removes only fields that the existing audit classified as assisted inference. In B05, both fields are removed and selection is exactly equivalent to B, without an additional filter; in BF04, the explicit card field remains and selection is equivalent to the original C. This check is deterministic: equivalence follows from the selection policy already defined. It documents case dependence on the fields used, with validity restricted to the mechanism. Classification independence and accuracy remain unevaluated.

### 3.6 Chronology and complementary module

Rankings for both sets are available from preparation onward. The method and hashes are published before pilot generation. Families are separated, with residual document dependence. The second set retains the final identifier in historical files and does not constitute external validation or a blinded set.

The later decision to conclude the documentary study retains 56 answers as a partial module. The evaluator correctly judged ten and seventeen of twenty controls across two rounds, below the criterion of nineteen, and automatic adequacy was disabled. There was no independent human judgment. Appendix B of the supplement presents generation budget, parameters, controls, diagnostics, and provenance gaps. AI tools used in the method and text are declared in section 8.

## 4 Results

### 4.1 Reference retrieval and ranking

The comparison covers thirty questions in five configurations, totaling 150 pairs. The audit checks positions, hashes, and links between 43 anchors and 62 passages. The six insufficient-evidence questions remain in the matrix with not-applicable measures. Table 1 adds narrower cutoffs and initial rank to the results at five positions.

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

In the pilot, C and Bp reach recall@5 of 96.9%; BM25, 93.8%; A and B, 90.6%. Within ten positions, B, C, and L retrieve all anchors, while A remains at 90.6% and Bp reaches 96.9%. In the second set, B, Bp, and L reach 100% within five positions; A and C remain at 87.5%. The first-position cutoff distinguishes configurations: L achieves 87.5%, A and Bp 75%, B 62.5%, and C 50%. L also has the highest MRR@10 in this set, at 0.917.

Pilot coverage@5 is 87.5% for A and B and 93.8% for C, Bp, and L; in the second set it coincides with recall@5. The mean weights questions equally, even when their anchor counts differ. Appendix B of the supplement retains exact values, and the public files support recalculation.

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

All twelve eligible Inter questions, eight in the pilot and four in the second set, have recall@5 of 100% in every configuration. Differences at this cutoff are concentrated in the twelve eligible Bradesco questions. For Inter, early cutoffs still distinguish configurations: in the pilot, C has recall@1 of 100%, A, B, and Bp 87.5%, and L 75%; in the second set, A, Bp, and L have 100%, and B and C 75%. Stratification exposes the ceiling and concentration of the comparative signal, without treating banks as representative populations.

### 4.2 Comparisons and discordant cases

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

B05 and BF04 are the only cases where C and B differ in recall@5 and coverage@5 in their respective sets. This statement covers the five-position cutoff. In the pilot, I08 shows a C gain in recall@1, C and B recall tie at positions 3 and 10, and published list order differs for seventeen of twenty questions. In the second set, BF04 distinguishes recall at all four cutoffs and order differs for nine of ten questions. Thus, the two cases exhaust outcome differences at five positions, while ranking changes occur for other questions, including those without references.

In the pilot, B loses to A and Bp on B05 among the eight condition and exception questions; the other seven tie. In the second set, all four pairs in these classes tie in each comparison. Case counts show the empirical basis of the differences. With eight questions, changing one binary outcome changes the mean by 12.5 percentage points; the earlier ten-point criterion does not distinguish a robust effect from a single question.

### 4.3 Filtering inferred attributes and category relations

B05 asks: “I lost my Bradesco debit card. Is replacement included in free essential services?” The dossier uses the passage delimiting free provision and listing loss among its exceptions. Resolution No. 3,919, Article 2, I, b, contextualizes this distinction for demand deposit accounts (Brasil, 2010). Consultation of the regulation is subsequent and serves discussion; it does not alter the collection, anchors, or case judgment. The experiment locates the banking reference without estimating a fee or judging the generated answer.

B05's anchor appears sixth in B and fourth in C. The gain within five positions consists of moving it into the selection cutoff. The filter uses account and individual, both inferred during preparation of the question, which mentions a debit card and omits audience. In the sensitivity check removing these fields, selection returns exactly to ranking B and recall@5 falls from one to zero. The account label differs from the question's card term and matches the target page's category. This association is plausible for account services, but shares dossier preparation and was not independently annotated. The advantage depends on this classification; the deterministic check does not estimate its accuracy in real queries.

BF04 asks: “I have investments at Bradesco. Is my card's annual fee waived?” The question omits the card name and requires clarification. A, B, Bp, and L locate the two selected Aeternum anchors within five positions. C excludes both: the question uses card and the catalogue uses Aeternum without a link to the broader category. Removing inferences does not change this case, because card is explicit in the question. The failure remains and identifies a loss associated with the absent relation in literal selection.

The subsequent intervention adds Aeternum to the card category and reapplies selection to B's frozen ranking. Both anchors return within the first five positions. This procedure checks the mechanism in a known case without measuring gains on independent data. C's main result remains unchanged; the demonstration is recorded separately in files and discussion.

## 5 Discussion

### 5.1 Scope of headers and filters

Contextual description and filtering operate at different points. The header changes the representation used to rank passages; the filter can prevent a reference from entering the list. B05 identifies a ranking change conditional on inferred attributes. BF04 identifies an exclusion that persists when only explicit question attributes are used. Both explain a concrete operation, with scope limited to prepared references and observed cases.

The BF04 loss revisits an established knowledge organization problem: relating a specific description to the broader category used in a query. SKOS and thesauri provide ways to express concept relations, while the executed demonstration only adds product-to-category membership. It does not implement or validate a complete controlled vocabulary. The empirical interest lies in making visible the consequence of using a catalogue without this relation as an exclusion requirement. B's header also contains Aeternum; in C, the same catalogue additionally participates in a decision excluding the passage.

Header effects depend on the question. In B05, B loses within five positions a reference retained by Bp. The reference exists within B's first ten results, so its rank and cutoff explain the observed loss. The B–Bp comparison combines title, section, and type in a joint ablation and does not identify which component causes the shift. In the second set, both reach the ceiling at five positions but differ at the first and third. Examining cutoffs and anchors by question avoids interpreting that ceiling as equivalent ranking.

### 5.2 What BM25 performance indicates

BM25 is competitive in this collection. In the pilot, it outperforms A and B in recall@3 and recall@5, while C and Bp have higher recall@5. In the second set, B and L retrieve all anchors within three positions. L has the highest recall@1, at 87.5%, and MRR@10, at 0.917; B reaches 62.5% and 0.792 in these measures. These results retain lexical retrieval as a relevant alternative before assuming a need for enrichment or semantic retrieval.

The collection provides eighteen or 44 candidates per bank, contains short product documentation, and uses questions close to the rules supporting their preparation. Lexical matching can suffice under some of these conditions. Short anchors and few candidates also favor the observed ceiling. The analysis does not measure latency costs between strategies or support extrapolation to larger collections, terms distant from the source, or customer queries collected in real use. Hybrid retrieval is a hypothesis for another evaluation, without demonstrated improvement in this study.

### 5.3 Interventions and reference validity

Frame 2 gathers actions arising from diagnostics or control mechanisms. A corrective action in a known case requires subsequent testing with new questions and sources to evaluate its breadth. The matrix and individual positions also enable challenges to the references themselves: a passage can contain an anchor and still omit information required for complete interpretation.

Frame 2 Diagnostics and documentary interventions

| Occurrence | Record used | Intervention |
|---|---|---|
| Specific product loses its broader-category relation | BF04 and exclusion trail | Record hierarchy and test expanded selection |
| Candidate reduction favors a reference | B05 and ranking by configuration | Examine filtering by question class |
| Reference absent from early ranks | Anchors and ten published ranks | Review description segmentation and passage competition |
| Input budget removes evidence | Effective input list | Combine rule and condition or adjust priority |
| Evaluator misjudges known controls | Two published calibration rounds | Exclude adequacy from main measures |

Source: study preparation, 2026. The budget row describes a control mechanism; effective-context records indicate whether it occurred in this execution.

B05's sensitivity check exposes the influence of inferred fields and supports critical analysis of the observed benefit. It does not resolve dependence between questions, catalogue, and dossiers. A justified extension is to test an extraction rule defined before new cases or add independent annotation. Shared use of Qwen3-8B as generator and evaluator, below-threshold calibration, and unavailable earlier raw outputs reinforce the need for specific validation of semantic evaluation. Excluding this evaluation from conclusions prevents treating structural validity as competence to judge answers.

## 6 Limitations and availability

The collection was selected by convenience and partially covers products, channels, and audiences from two banks. Exclusions reflect technical difficulties and a limited collection cycle. Four of 27 pages changed during recovery; hashes and private snapshots identify the version used. New collection can produce different texts and results.

Questions, metadata, and references share ChatGPT/Codex assistance. The implemented design does not establish the separation of independent teams initially planned. Short anchors represent selected passages, with uncertain coverage of all propositions a specialist would require. Different families can share a document. Results and sensitivity remain conditional on this preparation, the small sample, and the ten published positions.

The generation module was interrupted and does not provide a balanced quality comparison. There was no independent human evaluation, annotator agreement, or reader comprehension testing. Synthetic controls check literal preservation in delimited situations. The gap in earlier raw outputs is described in Appendix B of the supplement, without reconstruction from presumed data.

The public repository publishes code, original questions, positional references, hashes, rankings, and derived reports. Using these files and Python's standard library, third parties can reproduce metrics from frozen rankings, including individual ranks and measures by bank. Rerunning original retrieval requires texts, indexes, models, and environment versions. Originals, passages, indexes, prompts, and 56 answers remain in the researcher's private package because redistribution is not licensed. No DOI deposit has been made. Materials for recalculating metrics accompany the submission in an anonymized data file. The public repository address is disclosed to editors in the separate title page.

## 7 Conclusions

The diagnostic study connects document representation, candidate selection, and reference location in a public collection from two Brazilian banks. Within five positions, filtering outperforms unfiltered retrieval for one pilot question and loses for one second-set question. Sensitivity shows the dependence of the gain on inferred fields; the hierarchical demonstration explains exclusion in the known case. Narrower cutoffs highlight BM25's competitiveness and differences hidden by the ceiling at five positions.

The contribution is an auditable analysis of mechanisms and references, with documentary scope. Readers can examine the matrix, challenge anchors and attributes, repeat calculations, and reuse the diagnostic procedure on another collection. New, independently prepared questions are needed to evaluate intervention generalization and the correctness of generated answers.

## 8 Declarations

### 8.1 Artificial intelligence use and responsibility

ChatGPT/Codex assists with design discussion, source research and interpretation, programming, question and reference preparation, assisted analysis, writing, revision, and English translation. An exact interface model identifier was not retained in a verifiable record. E5 and Qwen revisions and parameters are documented in the supplement. Qwen3-8B generates answers and participated in earlier calibration controls; E5 generates retrieval representations. Published code calculates measures and diagnostics. The tools do not assume authorship. Intellectual responsibility, author review, and publication approval belong to the researcher.

## References

BRASIL. Conselho Monetário Nacional. **Resolução nº 3.919, de 25 de novembro de 2010**. Altera e consolida as normas sobre cobrança de tarifas pela prestação de serviços. Consulted consolidated text, version v7, provided by Banco Central do Brasil. Available at: https://normativos.bcb.gov.br/Lists/Normativos/Attachments/49514/Res_3919_v7_P.pdf. Accessed: 12 Oct. 2026.

DADOPOULOS, M.; LADAS, A.; MOSCHIDIS, S.; NEGKAKIS, I. **Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering**. arXiv, 2025. Preprint arXiv:2510.24402, version 1. Available at: https://arxiv.org/html/2510.24402v1. Accessed: 11 Oct. 2026.

ES, S.; JAMES, J.; ESPINOSA ANKE, L.; SCHOCKAERT, S. RAGAs: Automated Evaluation of Retrieval Augmented Generation. In: **Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations**. Association for Computational Linguistics, 2024. p. 150–158. DOI: 10.18653/v1/2024.eacl-demo.16. Available at: https://aclanthology.org/2024.eacl-demo.16/. Accessed: 12 Oct. 2026.

FORD, D. **Introducing Contextual Retrieval**. Anthropic, 19 set. 2024. Available at: https://www.anthropic.com/engineering/contextual-retrieval. Accessed: 11 Oct. 2026.

HJØRLAND, B. Knowledge Organization (KO). **Knowledge Organization**, v. 43, n. 6, p. 475–484, 2016a. DOI: 10.5771/0943-7444-2016-6-475. Available at: https://www.imrpress.com/journal/KO/43/6/10.5771/0943-7444-2016-6-475. Accessed: 12 Oct. 2026.

HJØRLAND, B. Does the Traditional Thesaurus Have a Place in Modern Information Retrieval? **Knowledge Organization**, v. 43, n. 3, p. 145–159, 2016b. DOI: 10.5771/0943-7444-2016-3-145. Available at: https://www.imrpress.com/journal/KO/43/3/10.5771/0943-7444-2016-3-145. Accessed: 12 Oct. 2026.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO 25964-1:2011: Information and documentation: Thesauri and interoperability with other vocabularies: Part 1: Thesauri for information retrieval**. Geneva: ISO, 2011. Public scope description. Available at: https://www.iso.org/standard/53657.html. Accessed: 12 Oct. 2026.

INTFLOAT. **multilingual-e5-large-instruct**. Hugging Face, [s. d.]. Model revision 274baa43b0e13e37fafa6428dbc7938e62e5c439. Available at: https://huggingface.co/intfloat/multilingual-e5-large-instruct. Accessed: 12 Oct. 2026.

ISLAM, P. et al. **FinanceBench: A New Benchmark for Financial Question Answering**. arXiv, 2023. Preprint arXiv:2311.11944. Available at: https://arxiv.org/abs/2311.11944. Accessed: 12 Oct. 2026.

JOREN, H.; ZHANG, J.; FERNG, C.; JUAN, D.; TALY, A.; RASHTCHIAN, C. **Sufficient Context: A New Lens on Retrieval Augmented Generation Systems**. In: INTERNATIONAL CONFERENCE ON LEARNING REPRESENTATIONS, 2025. **Anais [...]**. OpenReview, 2025. Available at: https://openreview.net/forum?id=Jjr2Odj8DJ. Accessed: 12 Oct. 2026.

LEWIS, P. et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**. In: **Advances in Neural Information Processing Systems**, v. 33, 2020. Available at: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html. Accessed: 12 Oct. 2026.

MANNING, C. D.; RAGHAVAN, P.; SCHÜTZE, H. **Introduction to Information Retrieval**. Cambridge: Cambridge University Press, 2008. Available at: https://nlp.stanford.edu/IR-book/. Accessed: 12 Oct. 2026.

MILES, A.; BECHHOFER, S. (ed.). **SKOS Simple Knowledge Organization System Reference**. W3C Recommendation, 18 ago. 2009. Available at: https://www.w3.org/TR/skos-reference/. Accessed: 12 Oct. 2026.

QWEN TEAM. **Qwen3-8B-GGUF**. Hugging Face, [s. d.]. Model revision 7c41481f57cb95916b40956ab2f0b139b296d974. Available at: https://huggingface.co/Qwen/Qwen3-8B-GGUF. Accessed: 12 Oct. 2026.

ROBERTSON, S.; ZARAGOZA, H. The Probabilistic Relevance Framework: BM25 and Beyond. **Foundations and Trends in Information Retrieval**, v. 3, n. 4, p. 333–389, 2009. DOI: 10.1561/1500000019. Available at: https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf. Accessed: 12 Oct. 2026.

SAAD-FALCON, J.; KHATTAB, O.; POTTS, C.; ZAHARIA, M. ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems. In: **Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies**. Association for Computational Linguistics, 2024. v. 1, p. 338–354. DOI: 10.18653/v1/2024.naacl-long.20. Available at: https://aclanthology.org/2024.naacl-long.20/. Accessed: 12 Oct. 2026.

TUDHOPE, D.; BINDING, C. Still Quite Popular After all Those Years: The Continued Relevance of the Information Retrieval Thesaurus. **Knowledge Organization**, v. 43, n. 3, p. 174–179, 2016. DOI: 10.5771/0943-7444-2016-3-174. Available at: https://www.imrpress.com/journal/KO/43/3/10.5771/0943-7444-2016-3-174. Accessed: 12 Oct. 2026.

WANG, L. et al. **Multilingual E5 Text Embeddings: A Technical Report**. arXiv, 2024. Preprint arXiv:2402.05672. Available at: https://arxiv.org/abs/2402.05672. Accessed: 12 Oct. 2026.

WANG, S.; TAN, J.; DOU, Z.; WEN, J. OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain. In: CONFERENCE ON EMPIRICAL METHODS IN NATURAL LANGUAGE PROCESSING, 2025, Suzhou. **Proceedings [...]**. Association for Computational Linguistics, 2025. p. 5726–5751. DOI: 10.18653/v1/2025.emnlp-main.292. Available at: https://aclanthology.org/2025.emnlp-main.292/. Accessed: 11 Oct. 2026.

WILSON, T. D. Models in information behaviour research. **Journal of Documentation**, v. 55, n. 3, p. 249–270, 1999. DOI: 10.1108/EUM0000000007145. Available at: https://doi.org/10.1108/EUM0000000007145. Accessed: 12 Oct. 2026.

ZHENG, L. et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In: **Advances in Neural Information Processing Systems**, v. 36, 2023. Datasets and Benchmarks Track. Available at: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html. Accessed: 12 Oct. 2026.
