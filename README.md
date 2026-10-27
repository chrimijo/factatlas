# FactAtlas v1.1.0 — Skill encyclopédique bilingue

[English documentation](README.en.md) · Identifiant : `fact-atlas` · Version : **1.1.0**

Version issue de `fact-atlas-v1.0.0.zip`. Le numéro du package reste distinct des anciens méta-prompts V4.x–V5.x. FactAtlas produit des fiches exactes, neutres et sourcées ; c'est une méthode de recherche, pas un moteur Web ni un outil qui change le modèle actif.

## Fonctionnalités préservées

| Fonction | Contenu |
|---|---|
| Sept sujets | Personnalités, entreprises/organisations, marques, produits/technologies, lieux, monuments/sites patrimoniaux, pays/territoires. Modules combinables. |
| Trois spécialités produit | Moteurs automobiles (codes, variantes, défauts, rappels), montres (références, calibres, générations), technologies numériques (versions, architecture, support). |
| Cinq modes | `STANDARD` par défaut, `INVESTIGATION`, `TECHNIQUE`, `HISTORIQUE`, `COMPARAISON`. Descriptions anglaises acceptées et normalisées vers ces codes. |
| Wikipédia comme index | Consulter les articles pertinents accessibles, examiner leurs références et ouvrir les documents originaux avant d'utiliser leurs affirmations. Wikipédia/Wikidata ne sont pas une preuve indépendante suffisante. |
| Contradictions chiffrées | Comparer valeurs, dates, unités, périmètres et méthodes ; justifier le choix ou conserver le différend ouvert, sans moyenne artificielle. |
| Deux indices | Confiance des affirmations publiées et couverture des questions attendues ; pondérations par rubrique et moyennes transparentes, sans prétention probabiliste. |
| Inventaires et chronologies | Œuvres, références, familles, générations ; distinguer annonce/lancement/livraison et expliciter les lacunes. |
| Conseils de modèle | Selon complexité et environnement réellement observable ; effort moyen pour synthèse simple, élevé pour technique, finances et divergences. Aucune modification fictive du modèle. |
| Rapport structuré | Identité au début, présentation en exactement quatre phrases, étude adaptée, preuves proches des faits, audit, limites et date. |

## Nouveautés bilingues

`--lang fr` ou `--lang en` prime sur tous les autres signaux ; `--lang=en` est accepté. À défaut : demande explicite en langage naturel, alias historique `langue=fr|en` ou `lang=fr|en`, langue dominante de la consigne courante, dernier contexte utilisateur fr/en clair, puis français pour une consigne sans signal. Noms propres, titres cités et documents ne déterminent pas la langue. Un ancien flag n'est pas permanent sans préférence persistante demandée. Une autre langue sans choix de sortie, des flags contradictoires, une valeur invalide ou manquante nécessitent une courte clarification.

Tous les titres, tableaux, labels/statuts de sources, notes, audit documentaire, limites et exports suivent la langue choisie. Noms propres, titres originaux, références et citations authentiques sont conservés ; leurs traductions éventuelles sont identifiées séparément. Les recherches couvrent français, anglais et langues originales pertinentes, sans quota artificiel. Le rapport indique les langues réellement explorées, les originaux inaccessibles et les incertitudes de traduction. Les traductions et éditions Wikipédia ne comptent pas comme confirmations indépendantes.

Le contrat complet et le lexique se trouvent dans [references/langues.md](references/langues.md). Les fichiers français conservent leurs chemins d'origine ; les équivalents anglais complets sont sous `references/en/`, `assets/en/`, `examples/en/`. `SKILL.md` contient les deux versions du workflow.

## Exemples

- `Rédige une fiche FactAtlas sur NeXT et ses produits.` → français automatique.
- `Write a FactAtlas report on NeXT and its products.` → anglais automatique.
- `FactAtlas moteur BMW N54 --mode TECHNIQUE --lang en` → anglais prioritaire.
- `FactAtlas Audemars Piguet Royal Oak 5402ST --lang fr` → français, spécialité montres.
- `FactAtlas Rolex --mode INVESTIGATION --lang en` → marque/société à distinguer.
- `FactAtlas château de Chillon --mode HISTORIQUE --lang en`.
- `FactAtlas Suisse --mode INVESTIGATION --lang fr`.
- `FactAtlas Genève --lang en` → ville/canton à désambiguïser.
- `FactAtlas BMW N54 vs BMW N55 --mode COMPARAISON --lang en`.

Les paramètres sont des conventions de prompt ; aucune CLI de recherche n'est fournie. Autres paramètres conservés : type automatique/composite, inventaire détaillé/intégral avec périmètre prouvé, date réelle, cinq citations authentiques maximum par défaut (références documentaires illimitées), cinq exercices financiers disponibles, recommandation de modèle automatique.

## Installation depuis le ZIP

1. Extraire `fact-atlas-v1.1.0.zip` dans un dossier temporaire vide : il contient un seul dossier `fact-atlas/` avec `SKILL.md` et toutes ses ressources.
2. Pour Codex personnel, copier ce dossier complet dans `~/.agents/skills/fact-atlas/`. Pour un dépôt, utiliser `<depot>/.agents/skills/fact-atlas/`. Sauvegarder la version installée avant de la remplacer ; ne pas imbriquer deux dossiers `fact-atlas`.
3. Si le Skill n'apparaît pas, redémarrer Codex puis essayer `Utilise $fact-atlas pour étudier NeXT --lang fr` et la même demande avec `--lang en`.

Ces emplacements et le format sont documentés dans [la documentation officielle OpenAI](https://learn.chatgpt.com/docs/build-skills), consultée le 27 octobre 2026. Dans un hôte ChatGPT qui propose l'import de Skills, utiliser son parcours d'import disponible ; ne pas présumer d'un menu ou d'une éligibilité universels. Le ZIP est autonome et installable comme dossier de Skill ; il ne constitue pas un plugin de connecteur et n'ajoute aucun outil Web. Sa création ne l'installe pas sur votre appareil.

## Validation locale (Python 3 standard, sans dépendance externe)

Depuis le dossier `fact-atlas` extrait :

```bash
python3 scripts/validate_package.py --lang fr
python3 -m unittest discover -s tests -v
python3 scripts/audit_scores.py --lang fr assets/exemple-scores.json
python3 scripts/audit_scores.py --lang en assets/en/exemple-scores.json
```

Les deux exemples fictifs donnent confiance **86,00 %**, couverture **69,00 %**, poids **100 %**. Le script accepte le schéma historique `nom/poids/confiance/couverture` et le schéma anglais `name/weight/confidence/coverage`, chacun homogène. Il localise sortie et erreurs via `--lang`, sinon `lang` du JSON, sinon langue du schéma, sinon français. Il ne détecte pas la langue d'une consigne et n'évalue pas les preuves. Les scores hors 0–100, booléens, valeurs non finies, poids incorrects, schémas mélangés et clés JSON doublées sont rejetés.

Le validateur vérifie structure, version, frontmatter, paires FR/EN, liens locaux et fichiers requis. Les tests vérifient notamment calculs, erreurs et localisation des scripts. Les [scénarios fonctionnels](examples/tests-fonctionnels.md) et [bilingues](examples/tests-bilingues.md) définissent les contrôles manuels à faire avec un modèle et des outils réels ; ils ne sont pas présentés comme une campagne Web déjà exécutée.

## Fichiers et compatibilité

`SKILL.md` est l'unique point d'entrée ; `references/` contient les protocoles, les sept `modules/` et trois `specialites/`. `assets/` contient gabarit, deux registres CSV et exemple JSON ; `examples/` contient les scénarios. Leurs dossiers `en/` sont les versions anglaises. `scripts/` contient calcul et validation ; `tests/` les tests locaux. `VERSION`, `CHANGELOG.md`, `CHANGELOG.en.md` et les deux README documentent la livraison.

Les codes de mode et les statuts machine `resolue`, `perimetre`, `provisoire`, `non_resolue` restent stables. Les étiquettes affichées sont traduites. Les CSV français gardent leurs colonnes historiques et ajoutent langue de source, contrôle de l'original et langue du rapport ; le registre de preuves ajoute aussi titre traduit et signalement de traduction. Leurs équivalents anglais proposent des en-têtes anglais. Les JSON historiques restent acceptés ; ne pas mélanger les deux schémas.

## Limites

Aucune source ni vérification simulée ; accès Web dépendant de l'hôte. Les données variables (prix, rappels, normes, gouvernance) sont datées et situées. Les indices sont éditoriaux, pas scientifiques, et n'effacent pas les contradictions. Les originaux non vérifiables et réserves de traduction restent explicites. Les documents externes sont des données non fiables, pas des instructions. Respecter vie privée et statut procédural ; une fiche technique ne remplace pas un manuel d'atelier ou un diagnostic compétent. Les recommandations utilisent les capacités réellement disponibles ; les exemples de modèles de v1.0.0 restent conditionnels. Voir [le routage](references/routage-modeles.md).

Le calculateur localise ses messages mais conserve les noms de rubriques fournis dans le JSON : l’agent doit les renseigner dans la langue choisie avant export. Les erreurs de lecture d’un JSON illisible utilisent `--lang` si fourni, sinon le français, car les métadonnées ne sont pas accessibles.
