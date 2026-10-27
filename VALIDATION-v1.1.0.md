# Validation — FactAtlas v1.1.0

## Français

Créée le 27 octobre 2026 à partir de l’archive originale `fact-atlas-v1.0.0.zip` retrouvée localement.

- Archive autonome : **57 fichiers**, un seul dossier `fact-atlas/`, un seul point d’entrée `SKILL.md`.
- Les 27 fichiers de v1.0.0 ont tous un successeur au même chemin ; sept modules et trois spécialités conservés avec leurs équivalents anglais.
- Validation réalisée **après extraction dans un répertoire temporaire indépendant** : CRC ZIP, chemins sûrs, absence de doublons, absence de caches, identité binaire avec les sources livrées.
- Validateur officiel du skill-creator : **réussi**. PyYAML utilisé seulement pour ce contrôle externe ; aucune dépendance externe n’est requise par les scripts livrés.
- Validateur du package en français et anglais : **réussi**, structure, paires linguistiques, version et liens locaux.
- Tests automatiques : **24 réussis** ; calcul, schémas FR/EN et rétrocompatibilité, entrées invalides, erreurs localisées, provenance CSV, ordre du gabarit et détection d’une traduction manquante.
- Exemples de calcul exécutés dans les deux langues : **86,00 % de confiance**, **69,00 % de couverture** ; poids total **100 %**. Données fictives, pas un audit de sources réelles.
- Les scénarios fonctionnels et bilingues sont inclus comme grilles de recette manuelle ; **aucune campagne de recherche Web par un modèle, ni installation dans un compte, n’a été exécutée**. La détection et la restitution linguistiques par un modèle restent à éprouver dans l’hôte cible.

Utilisation : `FactAtlas NeXT --lang fr` ou `FactAtlas NeXT --lang en`. Sans option, l’agent applique la détection et les priorités documentées dans le Skill.

## English

Built October 27, 2026 from the locally recovered original `fact-atlas-v1.0.0.zip`.

- Self-contained archive: **57 files**, one `fact-atlas/` root and one `SKILL.md` entry point.
- All 27 original paths retained; seven subject modules and three specializations preserved with English equivalents.
- Validated after extraction into an independent temporary directory: ZIP CRC, safe paths, no duplicates/caches, byte equality with delivered sources.
- Official skill-creator validation: **passed**. PyYAML was used only by this external check; shipped scripts require no external dependencies.
- Package validation in French and English: **passed**, including structure, language pairs, version and local links.
- **24 automated tests passed**: arithmetic, schema compatibility, invalid data, localized errors, CSV provenance, template order and detection of missing translation.
- Both fictional score examples executed: **86.00% confidence**, **69.00% coverage**, **100% weight**. These are arithmetic fixtures, not real evidence audits.
- Functional/bilingual scenarios are included for manual model evaluation. **No live model web-research campaign or account installation was performed**; model-driven detection/localization still needs target-host evaluation.

Use `FactAtlas NeXT --lang fr` or `FactAtlas NeXT --lang en`; without a flag the agent applies the documented detection precedence.

## SHA-256

- v1.0.0 source: `c652d8f00ce6c95ab8f9aae331d44f3c86d67f1e2b4d9067809bb7cbc47d4808`
- v1.1.0 ZIP: `946f0c8d4d42f415834d6ee80526a02597ede58da8d11e388184cffeeb520385`
