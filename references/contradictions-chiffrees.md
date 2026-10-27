# Protocole obligatoire — chiffres divergents

Quand **deux valeurs ou davantage paraissent incompatibles pour un même fait**, ne pas les fusionner ni choisir silencieusement.

## Phase 1 — Déterminer s'il existe une vraie contradiction

Consigner pour **chaque** valeur :

| Champ | Exigence |
|---|---|
| Valeur et unité | Nombre original, séparateurs et unité, devise, unité de mesure |
| Objet mesuré | Définition opérationnelle exacte, version ou référence concernée |
| Période | Date de mesure, année civile/exercice, date d'annonce/livraison |
| Périmètre | Groupe/société, brut/net, région, modèle, conditions d'essai, marché |
| Méthode | Comptabilisation, estimation, protocole, arrondi, taux de change |
| Source | Auteur, document, page/table si possible, date de publication et d'accès |
| Statut | Audité, officiel, déclaration, estimation, secondaire, non sourcé |

Vérifier s'il s'agit d'un changement au cours du temps, d'une valeur nominale versus valeur réalisée, d'une devise différente, d'une échelle différente ou d'une actualisation comptable.

## Phase 2 — Affichage et arbitrage

1. Présenter un tableau de **toutes les valeurs divergentes pertinentes** et leurs sources.
2. Expliquer les divergences attribuables au périmètre. Ne pas les appeler fausses contradictions si les définitions diffèrent.
3. Si les valeurs prétendent décrire exactement le même objet et périmètre, arbitrer selon : qualité de la preuve originale, méthode explicite, indépendance, correction datée, précision du périmètre et cohérence des autres documents.
4. **Justifier textuellement la valeur retenue**, en indiquant l'objectif : « pour le coût total d'acquisition comptabilisé, retenir X ; pour la trésorerie décaissée, Y ».
5. Si les preuves ne permettent pas de départager, **ne pas arbitrer** ; conserver une plage ou les valeurs, en attribuant chaque source, sans construire de moyenne artificielle.
6. Dégrader l'indice de confiance des affirmations affectées et la couverture de la rubrique lorsque l'absence de documents empêche de répondre complètement.

## Statuts du registre

- `resolue` : contradiction réelle tranchée avec preuve solide.
- `perimetre` : différences expliquées par objets, périodes, unités ou règles distincts.
- `provisoire` : valeur préférée sur preuves disponibles, sans clôture du différend.
- `non_resolue` : preuves insuffisantes ou contradictoires, aucune valeur privilégiée.

Utiliser `assets/registre-contradictions.csv` si des divergences majeures apparaissent. Chaque arbitrage important peut recevoir une **qualification de confiance propre** (forte/moyenne/faible avec justification), distincte des indices de la fiche entière.

## Exemples didactiques (non vérifiés ici)

- Acquisition d'une société : prix payé aux actionnaires, trésorerie nette déboursée et coût comptable total peuvent être différents **sans se contredire**.
- Puissance moteur : puissance mécanique au vilebrequin (kW/ch) et puissance aux roues, normes DIN/SAE et versions marché ne sont pas interchangeables.
- Montre : prix catalogue neuf, estimation d'enchère, résultat d'une vente et prix demandé en annonce ne sont pas comparables sans définition.
- Population d'une ville : commune, agglomération et aire métropolitaine ont des périmètres différents.

Ne pas recopier les chiffres des exemples comme s'ils avaient été vérifiés pour un dossier réel.

## Localisation v1.1.0

Appliquer [la politique linguistique](langues.md) : langue détectée ou `--lang fr|en` prioritaire ; rapport, sources, statuts, audit et limitations entièrement localisés. Rechercher aussi en anglais et dans les langues originales pertinentes, vérifier les originaux, préserver noms propres et citations, signaler les traductions. Version anglaise : [English](en/contradictions-chiffrees.md).
