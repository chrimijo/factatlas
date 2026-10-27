# Mandatory protocol for conflicting figures

When two or more values appear incompatible for the same fact, never merge them or silently pick one.

## 1. Establish whether the disagreement is real

For every value record:

| Field | Required detail |
|---|---|
| Value and unit | Original number, separators, measurement unit and currency |
| Measured object | Exact operational definition, version and reference |
| Period | Measurement date, calendar/fiscal year, announcement/delivery date |
| Scope | Group/company, gross/net, region, model, test conditions, market |
| Method | Accounting, estimate, protocol, rounding, exchange rate |
| Source | Author, original document, page/table, publication/access dates, language |
| Evidence status | Audited, official, statement, estimate, secondary, unsourced |

Check changes over time, nominal versus realized values, different currencies/scales and accounting restatements. Check decisive wording and numbers in original-language documents; translation uncertainty cannot silently settle a dispute.

## 2. Display and adjudicate

1. Show all relevant divergent values and their sources in a table.
2. Explain scope-based differences without claiming comparable measurements when definitions differ.
3. For the same object and scope, assess original evidence quality, explicit method, independence, dated corrections, scope precision and consistency with other documents.
4. Explain the selected value and purpose: total recorded acquisition cost may use X, cash outflow Y.
5. If evidence is insufficient, retain the attributed values or a justified range; do not create an artificial average.
6. Lower confidence for affected claims; lower coverage where unavailable documents prevent a complete answer.

## Register status codes and displayed English labels

- `resolue`: resolved with strong evidence.
- `perimetre`: scope difference explained by object, period, unit or rules.
- `provisoire`: provisional preference without closing the dispute.
- `non_resolue`: unresolved, no preferred value.

Use `../../assets/en/registre-contradictions.csv`. Important decisions may have their own high/medium/low confidence qualification and rationale, separate from report-wide scores. Machine codes remain stable; display labels follow report language.

## Illustrative distinctions, not verified case facts

Shareholder price, net cash outflow and acquisition accounting cost differ. Crankshaft and wheel power, DIN/SAE standards and market versions differ. Watch list prices, auction estimates, realized sales and asking prices differ. Municipal, urban and metropolitan populations differ. Never import example figures into a real report.
