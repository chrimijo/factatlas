# Tests fonctionnels manuels — FactAtlas v1.1.0

Ces cas servent à valider le comportement du Skill. **Ils ne sont pas des fiches ni des résultats factuels** ; faire une vraie recherche avant de renseigner des valeurs.

| Cas | Requête | Attendu |
|---|---|---|
| 1 — Société historique | `FactAtlas NeXT --mode INVESTIGATION` | Classification entreprise + technologies ; chronologie, catalogue, acquisition ; chiffres divergents définis par leur périmètre. |
| 2 — Moteur | `FactAtlas moteur BMW N54 --mode TECHNIQUE` | Code moteur exact, variantes, modèles équipés, spécifications par marché, défauts et rappels **sourcés**, pas de taux de panne inventé. |
| 3 — Montre | `FactAtlas Audemars Piguet Royal Oak 5402ST` | Référence distincte de collection et calibre ; catalogue, mouvement et prix historiques correctement qualifiés. |
| 4 — Marque | `FactAtlas Rolex` | Clarifier/établir périmètre marque vs personne morale, droits, chronologie, gammes. |
| 5 — Monument | `FactAtlas château de Chillon --mode HISTORIQUE` | Sources patrimoniales, phases de construction, attributions, classements ; légende séparée des faits. |
| 6 — Pays | `FactAtlas Suisse --mode INVESTIGATION` | Population et indicateurs datés, unités et périmètres ; gouvernance vérifiée à la date. |
| 7 — Lieu | `FactAtlas Genève` | Désambiguïsation ville vs canton, chiffres sur périmètre explicite. |
| 8 — Comparaison | `FactAtlas BMW N54 vs BMW N55 --mode COMPARAISON` | Tableau normalisé des codes et variantes ; aucune comparaison de puissances provenant de normes non homogènes. |
| 9 — Wikipédia | `FactAtlas [sujet avec article Wikipédia]` | Article consulté si accessible, références examinées, textes originaux ouverts, faits importants sourcés directement. |
| 10 — Sans internet | `FactAtlas NeXT` dans environnement sans Web | Limite clairement annoncée, aucun document inventé et pas de mention « vérifié en ligne ». |
| 11 — Contradiction | Deux sources donnent chiffres différents pour même indicateur | Tableau avec unité/date/définition ; arbitrage motivé ou abstention ; statut du différend. |
| 12 — Modèle | Même demande ChatGPT UI puis Codex | Recommandation adaptée à l'effort/disponibilité ; ne jamais affirmer avoir changé de modèle. |
| 13 — Scores | Fiche avec données manquantes | Confiance distincte de couverture, pondérations publiées, moyennes correctes, limites documentaires visibles. |

## Critères d'acceptation

- La fiche commence par identité, puis exactement quatre phrases introductives.
- Les références documentaires principales sont attachées aux faits ; aucune citation inventée.
- Les rubriques non documentées restent marquées absentes/partielles, non complétées automatiquement.
- Les cas d'usage techniques distinguent données annoncées et mesures indépendantes.
- Le script de contrôle des scores est purement arithmétique ; la vérification des preuves reste humaine/agentique.

Pour chacun des cas ci-dessus, exécuter en français puis en anglais ; appliquer aussi [les tests bilingues](tests-bilingues.md). Chaque module doit conserver le même périmètre et les mêmes exigences de preuve.
