# Proposition — nœud N-014 — texte des papiers dans le dépôt privé (sorties de l'extraction de T0.5) — v1

Rédigée le 2026-10-07 vers 05:10 UTC par la session de mise en œuvre, à la suite de la contre-lecture 1 de la procédure d'extraction (remarque CL-23, `docs/procedures/T0.5-extraction-v1/contre-lecture/rapport-contre-lecture-1-v1.md`). C'est un nœud : il touche une règle scellée et le contenu du dépôt. Il n'a pas de défaut. Annoncé à Lazar dans la session le 2026-10-07 vers 04:55 UTC.

## Décision

Faut-il admettre, par exception à la section 9 de la règle de sélection (`docs/procedures/T0.5-selection-papiers-v1.md`, 8f43dcae… : « Les licences des papiers varient : rien de leur texte n'entre dans le dépôt »), les sorties de l'extraction de T0.5 dans le dépôt privé ?

Ces sorties sont :
- les énoncés, réécrits depuis l'introduction de chaque papier par l'invite H.9 ;
- les citations courtes qui appuient les cibles (au moins 20 caractères, une phrase en général) ;
- les cibles et les classifications ;
- les avis des contre-vérificateurs, qui peuvent citer l'énoncé.

## Enjeu

- **Irreproductibles** : chaque sous-agent produit une version différente. Une perte oblige à tout refaire : un nouveau tirage des sorties, peut-être après avoir vu des avis.
- **Fragiles hors du dépôt** : le disque de la session est éphémère ; il est repris quand la session se termine ou reste inactive.
- **Seul chemin vers la machine de calcul** : la revalidation (P-007) et le pilote lisent leurs tâches depuis le dépôt cloné sur l'instance. La copie directe vers une instance n'est pas possible depuis la session (N-012 : la clé ne le permet pas).
- **Ce que la règle protège** : les licences des papiers varient ; le dépôt est privé et ne doit jamais être publié.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a) exception limitée** | les fichiers de `donnees/<run>/` de l'extraction (archives, détails, tâches), scellés, sont copiés tels quels dans le dépôt privé ; le dépôt reste privé ; tout papier ou livrable public n'en cite que ce que permettent les licences | persistance, chemin direct vers l'instance, contrôle par empreintes | des extraits de papiers entrent dans l'historique du dépôt, ce qui n'est pas réversible sans réécrire l'historique |
| (b) chiffré | les mêmes fichiers, chiffrés, dans le dépôt ; clé gardée par toi, transmise à l'instance par une variable d'environnement | la règle est tenue au sens strict | une clé à garder (perte = perte des données) ; mécanique en plus sur l'instance ; aucun gain de confidentialité réel dans un dépôt déjà privé |
| (c) aucune exception | les sorties restent hors du dépôt | règle tenue sans effort | perte probable à la fin de la session ; revalidation et pilote sans chemin pour leurs tâches tant qu'aucun moyen de copie vers l'instance n'existe |

## Recommandation

**(a)**, confiance ≈ 75 %. Le dépôt est privé ; les extraits sont courts et nécessaires au contrôle et à l'instance ; l'empreinte de chaque fichier est déjà consignée dans le dépôt.

**En attendant ta réponse** :
- l'extraction tourne ; ce qui porte du texte des papiers reste dans `donnees/<run>/`, hors du dépôt ;
- seules les empreintes, les codes et les compteurs entrent dans le dépôt ;
- la revalidation et le pilote attendent ta décision pour recevoir leurs tâches.
