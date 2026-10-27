# Evidence audit: two separate dimensions

**Evidence confidence (0–100)** evaluates evidence supporting claims actually published: directness, authenticity, independent corroboration, currency, transparent methods and unresolved contradictions.

**Research coverage (0–100)** measures how much of the relevant information planned before research has been adequately documented. Do not inflate coverage by silently removing difficult questions. These are structured editorial assessments, not statistical probabilities. A report can have 95% confidence and 40% coverage.

## Procedure

1. Define relevant sections and weights before research; weights sum to 100. Explain departures from the standard plan.
2. List expected research points per section and mark validated, partial or absent/disputed. Where appropriate: coverage = (validated + 0.5 × partial) / expected × 100. Explicitly weight points if importance varies. Remove inapplicable points from the denominator and disclose the adjustment.
3. Judge confidence only for presented claims, using direct primary evidence, independence, methods, currency and contradictions. Explain criteria and penalize uncorroborated statements or fragile decisions. There is no automatic source-to-truth formula.
4. Mark sections unscored when an estimate cannot be defended. Never invent a score.
5. Calculate confidence and coverage separately: Σ(section weight × section score) / Σ(section weight), with consistent rounding. Never extrapolate missing sections as if scored.
6. Ensure reported totals match the published table and weights total 100. Update scores when a decision is reopened.

| Section | Weight % | Confidence % | Coverage % | Main limitation |
|---|---:|---:|---:|---|
| Identification | … | … | … | … |
| Technical/history/finance | … | … | … | … |
| **Weighted total** | **100** | **…** | **…** | Assessment |

`../../assets/en/exemple-scores.json` contains fictional test data. `../../scripts/audit_scores.py` checks arithmetic and weights, never source quality. It requires a score for every section: when a judgment is impossible, omit a forced global score and explain the gap. Pass `--lang en` for English messages; the French JSON schema remains accepted. Apply [language policy](langues.md) to headings, notes and limitations.
