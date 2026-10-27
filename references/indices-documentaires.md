# Indices documentaires — deux dimensions distinctes

## Sens des scores

**Confiance documentaire** (0–100) : qualité des preuves qui soutiennent les affirmations effectivement publiées. Considérer : proximité de la source, authenticité, corroboration indépendante, date, transparence de méthode et contradictions non résolues.

**Couverture documentaire** (0–100) : proportion de questions pertinentes **prévues dans le plan de recherche** qui ont reçu une réponse documentée suffisante. Ne pas accroître la couverture en supprimant silencieusement des questions difficiles.

Les nombres sont une **évaluation éditoriale structurée**, pas une probabilité statistique. Un dossier peut avoir 95 % de confiance mais 40 % de couverture.

## Procédure concrète

1. Avant recherche, définir les rubriques utiles au sujet et leur **poids** (somme 100). Justifier les exceptions au modèle standard.
2. Pour chaque rubrique, dresser la liste des points de recherche attendus, puis documenter : trouvé/validé, partiellement documenté, absent/contesté. Si possible, établir `couverture = (points validés + 0,5 × points partiels) / points attendus × 100`, pondérer les points si des importances différentes sont explicites. Ne pas considérer « sans objet » comme manquant : retirer ce point du dénominateur et le signaler.
3. Pour confiance, évaluer **les affirmations réellement présentées** : preuve primaire directe, indépendance, méthode, fraîcheur, contradiction. Consigner le jugement en critères explicites ; pénaliser les déclarations non corroborées ou les arbitrages fragiles. Aucune formule absolue n'existe pour transformer automatiquement une source en vérité.
4. Signaler les sections pour lesquelles l'estimation ne serait pas défendable ; ne pas inventer de score.
5. Calculer chaque global par moyenne pondérée : `Σ(poids_section × score_section) / Σ(poids_section)`, **séparément** pour confiance et couverture, puis arrondir de façon cohérente. Ne pas extrapoler les sections manquantes comme si elles étaient notées.
6. Vérifier que les scores annoncés correspondent à la table publiée et que les poids totalisent 100. Mettre à jour scores si un arbitrage est rouvert.

## Format minimal

| Rubrique | Poids % | Confiance % | Couverture % | Limite principale |
|---|---:|---:|---:|---|
| Identification | … | … | … | … |
| Technique/histoire/finance | … | … | … | … |
| **Global pondéré** | **100** | **…** | **…** | Synthèse |

`assets/exemple-scores.json` est un exemple **fictif à usage de test**. `scripts/audit_scores.py` vérifie les moyennes et les poids, **pas** la qualité des sources. Le script exige une note pour chaque section ; si le jugement n'est pas possible, ne pas afficher de score global forcé et expliquer la lacune.

## Localisation v1.1.0

Appliquer [la politique linguistique](langues.md) : langue détectée ou `--lang fr|en` prioritaire ; rapport, sources, statuts, audit et limitations entièrement localisés. Rechercher aussi en anglais et dans les langues originales pertinentes, vérifier les originaux, préserver noms propres et citations, signaler les traductions. Version anglaise : [English](en/indices-documentaires.md).
