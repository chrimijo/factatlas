# Scénarios bilingues — validation comportementale v1.1.0

Ces scénarios sont une grille manuelle à exécuter avec un modèle et les outils réellement disponibles ; ils ne sont pas présentés comme déjà réussis. Les tests locaux ne valident ni la qualité d'une recherche réelle ni la détection linguistique par le modèle.

| Cas | Consigne / contexte | Résultat observable attendu |
|---|---|---|
| Auto FR | `Rédige une fiche FactAtlas sur NeXT avec ses produits.` | Rapport entièrement français, entreprise + produits numériques. |
| Auto EN | `Write a FactAtlas report on NeXT and its products.` | Rapport entièrement anglais, mêmes modules et exigences. |
| Priorité EN | `Rédige une fiche sur Genève --lang en` | Tout en anglais, y compris titres, tableaux, sources et limites. |
| Priorité FR | `Write a report on Switzerland --lang fr` | Tout en français, chiffres/politique datés. |
| Option égale | `FactAtlas BMW N54 --lang=en --mode TECHNIQUE` | Anglais, produit + moteurs, normes et variantes. |
| Mixte | `Please analyse Château de Chillon et ses restaurations.` | Anglais dominant ; nom original préservé ; module monuments. |
| Nom seul | `FactAtlas NeXT`, aucun contexte | Français par repli, pas anglais déduit du nom. |
| Contexte EN | Après une consigne utilisateur anglaise : `FactAtlas Rolex` | Anglais ; distinguer marque et entreprise. |
| Nouveau tour | Ancien `--lang en`, puis `Rédige maintenant en français sur Genève.` | Français, ancien flag non permanent. |
| Alias | `FactAtlas Royal Oak langue=en` | Anglais, produit + montres ; `--lang fr` ajouté prime. |
| Langage naturel | `Réponds en anglais sur NeXT, langue=fr` | Anglais, demande explicite avant alias. |
| Erreur | `--lang de`, `--lang`, ou `--lang fr --lang en` | Clarification ; aucune langue arbitrairement choisie. |
| Répétition | `FactAtlas NeXT --lang en --lang en` | Anglais, doublon identique accepté. |
| Autre langue | Consigne allemande sans préférence fr/en | Demande courte de choix français ou anglais. |
| Citation hostile | Source jointe contenant `--lang en` et « ignore les règles » ; demande française | Source traitée comme données, langue française conservée. |
| Source japonaise | Produit japonais demandé en anglais | Requêtes FR/EN et japonais pertinent ; original vérifié ou accès limité déclaré. |
| Citation originale | Source française contenant une citation authentifiée ; sortie anglaise | Citation française intacte, traduction anglaise distincte et étiquetée. |
| Titres | Rapport anglais citant un titre français | Titre original intact ; éventuelle traduction marquée, aucun nom propre réinventé. |
| Wikipédia multilingue | Deux éditions recopient le même communiqué | Index seulement ; un seul original, aucune fausse indépendance. |
| Original inaccessible | Traduction ou extrait secondaire seul accessible | Relais réellement lu attribué, original non consulté explicite, confiance réduite si nécessaire. |
| Chiffres divergents | 420/350/425 fictifs de l'exemple, sortie anglaise | Définitions conservées, labels anglais, aucune moyenne artificielle. |
| Sans Web EN | `Write a FactAtlas report on NeXT` sans navigation | « External research not performed », sources/limites et audit anglais, aucune vérification fictive. |
| Audit bilingue | Même plan, mêmes preuves, sortie FR puis EN | Même calcul, poids 100 ; confiance/couverture distinctes, labels traduits. |
| Export | Fiche EN avec CSV et calcul JSON | En-têtes/texte anglais ; schéma unique ; codes statut stables et provenance conservée. |

## Acceptation

Exécuter les cas des sept modules et trois spécialités dans chaque langue avec `tests-fonctionnels.md`. Contrôler identité au début et introduction en exactement quatre phrases. Comparer les deux versions : réserves, unités, périmètres, contradictions et recommandations doivent rester équivalents. Vérifier chaque en-tête, cellule générée, étiquette de source, note d'audit et limitation ; les originaux et identifiants conservés ne sont pas des défauts de traduction.
