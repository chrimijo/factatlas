# Recommandation de modèle, effort et environnement

**Cette section est un routeur de recommandation, non un mécanisme de changement de modèle.** Les capacités, noms, plans et autorisations varient ; vérifier ce que l'environnement expose réellement. Ne jamais inventer un sélecteur, un plan, un effort actif ou un outil web.

## Règles

1. Identifier **sujet + complexité + mode**, puis si possible l'environnement : `ChatGPT UI`, `ChatGPT mobile`, `Codex`, `inconnu`.
2. Évaluer la difficulté : STANDARD simple ; TECHNIQUE exige détails, variantes et normes ; INVESTIGATION exige triangulation et arbitrage ; COMPARAISON exige normaliser plusieurs périmètres ; HISTORIQUE complexe nécessite archives et chronologies.
3. Recommander l'effort de raisonnement : **Medium** par défaut pour un dossier simple, **High** pour technique pointue, finances, contradictions, comparaison ou documentation dispersée. Extra High seulement si disponible, réellement pertinent et demandé/autorisé.
4. Sur ChatGPT, privilégier le **meilleur modèle de raisonnement généraliste accessible** (exemple de la v1.0.0 : GPT-6, uniquement si effectivement proposé ; pas une garantie de disponibilité). Sur Codex, privilégier un modèle puissant disponible pour les tâches d'investigation documentaire et de fichiers (exemple : GPT-6 ou GPT-6 Astra si proposé). **Ne pas supposer** qu'un nom de modèle est disponible sur tous les comptes.
5. Si l'environnement ne permet pas au Skill de changer le modèle, **afficher la recommandation** et poursuivre avec le modèle actif. Si le modèle actif est inconnu, écrire « modèle actif non vérifiable ici ».
6. Une grande fenêtre de contexte et une forte capacité de raisonnement ne remplacent ni la navigation web ni la vérification de documents originaux.

## Matrice de recommandation

| Cible / demande | Raisonnement recommandé | Recherche complémentaire indispensable |
|---|---|---|
| Personnalité, marque, lieu — STANDARD | Medium | Archives de base et preuves primaires pour faits déterminants |
| Monument — HISTORIQUE | Medium ou High selon sources | Inventaires patrimoniaux, archives, publications savantes |
| Société — finances, acquisitions, actionnariat | High | Bilans, registres, contrats/communiqués, documents réglementaires |
| Moteur, machine, technologie — TECHNIQUE | High | Manuels, codes, bulletins de service, homologations et rappels |
| Montre — références multiples | High | Catalogues fabricant, calibres, registres, ventes datées |
| Pays — chiffres et politique | High | Instituts statistiques, lois, données multilatérales, dates |
| COMPARAISON multi-objets | High | Table de critères normalisés, correspondance références et périodes |
| INVESTIGATION avec divergences majeures | High ; effort supérieur uniquement si disponible et utile | Réconciliation manuelle des périmètres et sources originales |

## Entête d'exécution

Afficher compactement : `Module(s)` ; `Mode` ; `Interface` (si connue) ; `Modèle conseillé` ; `Effort conseillé` ; `Modèle actif` **uniquement si connu** ; `Recherche web possible/vérifiée` selon outils.

Le choix du modèle reste au contrôle de l'utilisateur/de la plateforme. Pas de relance systématique demandant validation ; utiliser les moyens existants.

## Localisation v1.1.0

Appliquer [la politique linguistique](langues.md) : langue détectée ou `--lang fr|en` prioritaire ; rapport, sources, statuts, audit et limitations entièrement localisés. Rechercher aussi en anglais et dans les langues originales pertinentes, vérifier les originaux, préserver noms propres et citations, signaler les traductions. Version anglaise : [English](en/routage-modeles.md).

Libellés du rapport français : « modèle conseillé », « effort conseillé : moyen/élevé », « modèle actif non vérifiable ici ». Conserver les identifiants réels et, si nécessaire, les noms littéraux des options Medium/High de l’interface. Placer cette configuration après la fiche d’identité initiale.
