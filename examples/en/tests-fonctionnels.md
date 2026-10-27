# Manual functional tests — FactAtlas v1.1.0

These are requests and acceptance criteria, not researched reports. Perform genuine research before supplying facts. Run every case in French and English, and also use [bilingual scenarios](tests-bilingues.md).

| Case | Request | Expected behavior |
|---|---|---|
| Historical company | `FactAtlas NeXT --mode INVESTIGATION --lang en` | Company + digital technology; timeline, catalogue, acquisition, scoped conflicting figures. |
| Engine | `FactAtlas BMW N54 --mode TECHNIQUE --lang en` | Exact code, variants, equipped vehicles, market specifications, sourced defects/recalls, no fabricated failure rates. |
| Watch | `FactAtlas Audemars Piguet Royal Oak 5402ST --lang en` | Separate collection/reference/movement, catalogue and qualified historical prices. |
| Brand | `FactAtlas Rolex --lang en` | Establish brand versus legal entity, rights, history and ranges. |
| Monument | `FactAtlas Château de Chillon --mode HISTORIQUE --lang en` | Heritage sources, construction phases, attribution, listings, legends separated from facts. |
| Country | `FactAtlas Switzerland --mode INVESTIGATION --lang en` | Dated population/indicators, units/scopes, checked governance. |
| Place | `FactAtlas Genève --lang en` | City/canton disambiguated, explicit statistical boundaries. |
| Comparison | `FactAtlas BMW N54 vs BMW N55 --mode COMPARAISON --lang en` | Normalized codes/variants/measurement standards. |
| Wikipedia | Subject with accessible relevant article | Article as index, cited originals opened, decisive facts directly sourced. |
| Offline | NeXT without web access | Explicit limitation, no invented document or online verification. |
| Discrepancy | Two sources disagree about same indicator | Value/unit/date/definition table, reasoned choice or abstention, status. |
| Model routing | Same task in ChatGPT UI and Codex | Actual availability/effort advice, no claimed switch. |
| Scores | Missing evidence | Distinct confidence/coverage, published weights, correct arithmetic, explicit gaps. |

Accept only reports starting with identity followed by an exactly four-sentence overview; key sources near claims; gaps remain partial/missing; advertised specifications separated from independent tests. Score scripts validate arithmetic only.
