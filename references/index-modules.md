# Index de modules et désambiguïsation

## Typologie

| Indice trouvé | Module prioritaire | Combinaisons possibles |
|---|---|---|
| Individu, biographie, parcours, œuvres | `modules/personnalites.md` | entreprise, œuvres/produits |
| Société, groupe, fondation, organisation | `modules/entreprises.md` | marque, produits, pays |
| Nom commercial, gamme, enseigne, logo | `modules/marques.md` | entreprise, produit |
| Modèle, référence, technologie, composant | `modules/produits.md` | moteur, montre, technologie |
| Ville, site naturel, région, quartier | `modules/lieux.md` | monument, pays |
| Édifice, site protégé, construction | `modules/monuments.md` | lieu, pays |
| État souverain, territoire, nation | `modules/pays.md` | lieu, gouvernement |

## Sous-module Produit

- Code moteur, cylindrée, famille mécanique : `specialites/moteurs-automobiles.md`.
- Modèle horloger, référence de montre, calibre : `specialites/montres.md`.
- Logiciel, plateforme, électronique, IT : `specialites/technologies-numeriques.md`.
- Autres produits : tronc commun `modules/produits.md`, rubriques adaptées au secteur.

## Réflexes de périmètre

- BMW peut viser le constructeur, le groupe juridique, la marque de véhicules ou la gamme de produits ; **BMW N54 est un moteur**, pas une société.
- Rolex : distinguer la société, la marque et une référence Submariner ; les séries d'une montre ne se confondent pas avec les générations du calibre.
- NeXT : entreprise et marque portant le même nom, stations matérielles, NEXTSTEP, OPENSTEP, WebObjects.
- « Genève » peut être ville, canton ou aire urbaine : ne pas mélanger statistiques.
- « Suisse » : pays et Confédération ; séparer indicateurs fédéraux et cantonaux.
- « Château de Chillon » : monument précis situé à Veytaux ; le lac, la commune et le château ont des périmètres différents.

Séparer systématiquement identité **juridique**, **commerciale**, **géographique**, **technique** et **historique**. Déterminer les dates de validité ; intégrer les relations mère-fille, changement de nom ou succession de produit, sans fusion abusive.

## Localisation v1.1.0

Appliquer [la politique linguistique](langues.md) : langue détectée ou `--lang fr|en` prioritaire ; rapport, sources, statuts, audit et limitations entièrement localisés. Rechercher aussi en anglais et dans les langues originales pertinentes, vérifier les originaux, préserver noms propres et citations, signaler les traductions. Version anglaise : [English](en/index-modules.md).
