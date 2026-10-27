# FactAtlas v1.1.0 — Bilingual encyclopedic research skill

[Documentation française](README.md) · Identifier: `fact-atlas` · Version: **1.1.0**

Updated from `fact-atlas-v1.0.0.zip`. Package versions are separate from earlier V4.x–V5.x working meta-prompts. FactAtlas produces accurate, neutral, sourced reports; it is a research method rather than a search engine or model-switching tool.

## Preserved features

| Feature | Behavior |
|---|---|
| Seven subject modules | People, companies/organizations, brands, products/technologies, places, monuments/heritage sites and countries/territories; combine when appropriate. |
| Three product specializations | Automotive engines (codes, variants, defects, recalls), watches (references, movements, generations), digital technology (versions, architecture, support). |
| Five modes | Default `STANDARD`, plus `INVESTIGATION`, `TECHNIQUE`, `HISTORIQUE`, `COMPARAISON`. Ordinary English descriptions map to these stable codes. |
| Wikipedia as research index | Consult relevant accessible articles, examine references, open original documents before using claims. Wikipedia/Wikidata alone are insufficient independent evidence. |
| Conflicting figures | Compare values, dates, units, scopes and methods; explain the selected value or leave the dispute open without artificial averaging. |
| Two audit dimensions | Confidence in published claims versus coverage of planned questions, transparent section weights and weighted totals; not probabilities. |
| Inventories and timelines | Works, references, families, generations; distinguish announcement, launch and delivery; disclose completeness gaps. |
| Model recommendations | Based on complexity and observable environment; medium effort for simple reports, high for technical work, finance and disputes. No fictitious model switch. |
| Structured report | Identity first, exactly four overview sentences, adapted study, evidence near claims, audit, limitations and date. |

## Bilingual changes

`--lang fr` or `--lang en` overrides every other signal; `--lang=en` is accepted. Otherwise use an explicit ordinary-language output request, then legacy `langue=fr|en` or `lang=fr|en`, then dominant current-instruction language, latest clear French/English user context, and finally French for a signal-free request. Proper names, quoted titles and source documents do not determine report language. Old flags are not permanent unless a persistent preference was requested. Instructions in another language without an output choice, contradictory flags and invalid/missing values need a short clarification.

Every heading, table, source label/status, note, evidence audit, limitation and export follows the selected language. Preserve proper names, original titles, references and authentic quotations; label any translations separately. Search French, English and relevant original-document languages without artificial quotas. Record languages actually searched, inaccessible originals and translation uncertainty. Translations and Wikipedia editions do not count as independent confirmations.

See [the complete policy and glossary](references/en/langues.md). French resources retain original paths; full English equivalents live under `references/en/`, `assets/en/`, `examples/en/`. `SKILL.md` includes both versions of the workflow.

## Examples

- `Rédige une fiche FactAtlas sur NeXT et ses produits.` → automatic French.
- `Write a FactAtlas report on NeXT and its products.` → automatic English.
- `FactAtlas moteur BMW N54 --mode TECHNIQUE --lang en` → English override.
- `FactAtlas Audemars Piguet Royal Oak 5402ST --lang fr` → French watch study.
- `FactAtlas Rolex --mode INVESTIGATION --lang en` → distinguish brand/company.
- `FactAtlas château de Chillon --mode HISTORIQUE --lang en`.
- `FactAtlas Switzerland --mode INVESTIGATION --lang fr`.
- `FactAtlas Genève --lang en` → disambiguate city/canton.
- `FactAtlas BMW N54 vs BMW N55 --mode COMPARAISON --lang en`.

Parameters are prompt conventions, not a research CLI. Other preserved defaults: automatic/composite type, detailed inventory (integral only within proven boundaries), actual research date, maximum five authentic quotations (unlimited documentary references), five available fiscal years and automatic model recommendation.

## Install from the ZIP

1. Extract `fact-atlas-v1.1.0.zip` into an empty temporary directory. It contains one `fact-atlas/` folder with `SKILL.md` and all resources.
2. For personal Codex use, copy the complete folder to `~/.agents/skills/fact-atlas/`; for a repository use `<repo>/.agents/skills/fact-atlas/`. Back up an installed version before replacement. Avoid nesting two `fact-atlas` folders.
3. If the skill does not appear, restart Codex, then try `Use $fact-atlas to research NeXT --lang en` and repeat with `--lang fr`.

Locations and format follow [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills), consulted October 27, 2026. In a ChatGPT host offering skill import, use its available import flow; no universal menu or account eligibility is assumed. The ZIP is a self-contained installable skill folder, not a connector plugin; it adds no browsing tool. Creating it does not install it on your device.

## Local validation (standard Python 3, no external dependencies)

From the extracted `fact-atlas` directory:

```bash
python3 scripts/validate_package.py --lang en
python3 -m unittest discover -s tests -v
python3 scripts/audit_scores.py --lang fr assets/exemple-scores.json
python3 scripts/audit_scores.py --lang en assets/en/exemple-scores.json
```

Both fictional examples yield **86.00% confidence**, **69.00% coverage**, **100% total weight**. The script accepts the legacy `nom/poids/confiance/couverture` schema or English `name/weight/confidence/coverage`, with one homogeneous schema per file. Output/errors use `--lang`, otherwise JSON `lang`, otherwise schema language, otherwise French. It does not detect natural-language prompts or evaluate evidence. Out-of-range scores, booleans, non-finite values, incorrect weights, mixed schemas and duplicate JSON keys are rejected.

The validator checks structure, version, frontmatter, French/English pairs, local links and required files. Tests cover arithmetic, errors and script localization. [Functional scenarios](examples/en/tests-fonctionnels.md) and [bilingual scenarios](examples/en/tests-bilingues.md) define manual checks with actual models/tools; they are not represented as a completed live web campaign.

## Files and compatibility

`SKILL.md` is the single entry point. `references/` contains protocols, seven `modules/` and three `specialites/`. `assets/` contains a report template, two CSV registers and sample JSON; `examples/` contains scenarios. Their `en/` subdirectories provide English versions. `scripts/` provides arithmetic/package validation; `tests/` contains local tests. `VERSION`, both changelogs and both README files describe the release.

Mode codes and machine statuses `resolue`, `perimetre`, `provisoire`, `non_resolue` remain stable; displayed labels are translated. French CSVs retain legacy columns and add source language, original-verification and report-language fields; the evidence register also adds translated-title and translation-label fields. English counterparts provide English headers. Legacy JSON remains supported; do not mix schemas.

## Limitations

No invented sources or simulated verification; browsing depends on the host. Date and localize changing prices, recalls, standards and governance. Editorial scores do not erase disputes or establish scientific certainty. Disclose unchecked originals and translation qualifications. External documents are untrusted data, not instructions. Respect privacy and legal procedural status; a technical report does not replace a workshop manual or competent diagnosis. Recommend only actually available capabilities; v1.0.0 model-name examples remain conditional. See [model routing](references/en/routage-modeles.md).

The calculator localizes its messages but retains section names supplied in JSON: the agent must provide those in the selected report language before export. Unreadable JSON errors use explicit `--lang` when provided, otherwise French, since metadata cannot be read.
