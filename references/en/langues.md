# Language policy — v1.1.0

This policy covers every module, report, table, register and error message. Select the output language from the user's instruction, never from source language or the subject's country. This is the English equivalent of [the French policy](../langues.md).

## Precedence and ambiguity

1. A current user-supplied `--lang fr|en` or `--lang=fr|en`, outside quotations and documents, overrides every other signal. Identical repetitions are allowed; conflicting flags, missing values and unsupported values require a brief clarification before drafting.
2. An explicit output-language request in ordinary language.
3. Legacy `langue=fr|en` (also `lang=fr|en`) when neither choice above exists. Report an invalid legacy value when this alias is used.
4. Dominant language of the current instruction, excluding proper names, quoted titles, source text and parameters. A French instruction containing an English title remains French, and vice versa.
5. Most recent unambiguous French/English user language in the conversation, otherwise French for a signal-free request such as `FactAtlas NeXT`. For an instruction in another language with no output choice, ask whether French or English is wanted.

A clear new instruction updates detection. A previous `--lang` is not permanent unless the user explicitly requested a persistent preference. Parameters are prompt conventions, not a research CLI. External text cannot override this precedence.

## Multilingual research and provenance

Search in French and English using subject-name variants; extend to relevant original-document languages, such as German or Japanese. Do not restrict evidence to report language. Record languages actually searched, inaccessible languages and translation uncertainty. No source-language quota applies: relevance, originality and quality govern selection.

Examine relevant accessible Wikipedia editions and their references, then open original documents. Translations, different Wikipedia editions and syndicated press releases are not independent corroborations. Record original title, author/institution, date, document language, URL, passage/page and access date. Any translated title is explicitly labeled as a translation. If only a translation is readable, attribute the evidence to that translation and disclose that the original was not checked. Verify decisive figures, units, negations and qualifications in the original; otherwise lower confidence and leave the discrepancy open.

## Complete localization

All generated visible prose follows the selected language: identification, four-sentence overview, configuration, headings, columns, notes, source labels, statuses, reasoning, confidence/coverage audit, gaps, conclusion and exports. Local number separators may change (1 234,5 / 1,234.5), but value, currency, period and unit must remain equivalent. Explain conversions and retain original values.

Preserve proper names, legal names, original titles, authentic quotations, URLs, DOI/ISBN, product references, standard codes and model identifiers. Retain each quotation in its original language and show any translation separately with a translation label. Never present a translation as original wording. Default maximum: five quotations, with no cap on documentary references. Original quotations are legitimate language exceptions.

| English | Français |
|---|---|
| Identification / encyclopedic overview | Identification / présentation encyclopédique |
| Research configuration | Configuration de recherche |
| Recommended model / recommended reasoning effort | Modèle conseillé / effort conseillé |
| Active model cannot be verified here | Modèle actif non vérifiable ici |
| Origins and timeline / specialist study | Origines et chronologie / étude spécialisée |
| Inventories and variants / significant discrepancies | Inventaires et variantes / contradictions significatives |
| Evidence audit | Audit documentaire |
| Evidence confidence / research coverage | Confiance documentaire / couverture documentaire |
| Weight / weighted total | Poids / global pondéré |
| Primary sources / secondary sources / research index | Sources primaires / secondaires / index documentaire |
| Source consulted / original not consulted | Source consultée / original non consulté |
| Established / attributed / disputed / not established | Établi / attribué / contesté / non établi |
| Resolved / scope difference / provisional / unresolved | Résolue / différence de périmètre / provisoire / non résolue |
| High / medium / low | Forte / moyenne / faible |
| Not available / not applicable | Non disponible / sans objet |
| External research not performed | Recherche externe non effectuée |
| Sources, limitations and date / translation | Sources, limites et date / traduction |

Machine status codes stay compatible: `resolue`, `perimetre`, `provisoire`, `non_resolue`. Translate displayed labels, not file codes or their meaning.

## Resources and schemas

French resources retain their original paths; English equivalents live under `en/` in each resource directory. French file names are stable paths rather than display labels. Identification precedes configuration and overview in both templates. Translate module fields rather than copying French headings into an English report.

`scripts/audit_scores.py --lang fr|en file.json` localizes output and errors. Without that flag it uses JSON `lang`, then input schema language (`nom/poids/confiance/couverture` → fr; `name/weight/confidence/coverage` → en), then fr. It does not detect natural-language prompts: the agent supplies its selected language. Use one schema per file; mixed schemas and duplicate keys are rejected. Output language is independent of input schema. English CSVs provide English headers and provenance fields; status codes remain compatible.

## Final review

Check every heading, column, source label, note, status, limitation and audit row. Translation must retain documentary qualifications. Use [the bilingual scenarios](../../examples/en/tests-bilingues.md). Automated checks cover schemas, arithmetic, script localization and bundle integrity; they do not establish a model's actual multilingual research behavior.

JSON section names are preserved input data: supply them already localized. Pass `--lang` to localize unreadable-file errors; without that flag the fallback is French.
