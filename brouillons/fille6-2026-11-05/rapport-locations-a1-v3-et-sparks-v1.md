# Fille 6 — locations A1-v3 et SPARKS-EXP7-NUL — v1

Le 5 novembre 2026 (heures relevées par `date -u`). Les deux locations partent sur le mot direct de Lazar, écrit dans la session vers 15:38 UTC : « ’autorise la location Vast de l’ordre A1-v3 v3 (GO-2026-11-05-03 et GO-2026-11-04-06), puis la création SPARKS (GO-2026-11-04-04). Lance. »

## A1-v3, troisième course, texte v4 (ordre v3, `12648dcd…`)
- **Préalable 1** refait à 15:39:27 : seulement les trois instances R8.
- **Location** en deux passes : d'abord la vérification seule, puis la location réelle.
  - Garde de main acceptée (registre `ff73dcf0…`).
  - Offre 52708522 (GTX 1080), 0,0617 USD/h ; coût de la machine au plus 5,02 USD.
- **Instance 59286520**, étiquette `a1-v3-troisieme-v1`.
  - T0 : 2026-11-05T15:39:57Z.
  - Signe de vie attendu avant 16:09:57Z.
  - Échéance : 2026-11-09T00:49:57Z.
  - Contrôles à 16:19:57Z et à 2026-11-09T01:09:57Z.
- `JETON_VAR=CONTROLE_IA_GITHUB_TOKEN_2`.
- **Écart déclaré au préalable 4** (R-1567) : l'échéance du jeton ne peut pas se mesurer à travers le mandataire de la session.

## SPARKS-EXP7-NUL, session 1 (ordre v3 et ordre v1 ; GO-2026-11-04-04)
- **CODE** `78671d93…` ; **LANCE** `0d163bdc…` ; arbre à part `/home/user/arbre-sparks-lance-v12`.
- **A.1** : GO valide (lignes 242 et 245, échéance 18 novembre) ; rien n'est imputé à ce GO dans `depenses.md`.
- **A.2** : marqueur du quatrième tir v11 conforme (addendum, l. 606).
- **A.3** : LANCE^ = CODE ; le diff ne porte que l'addendum, son `.sha256` et `go.md` ; `git status` vide.
- **A.4** :
  - compagnon OK ;
  - `exiger_prereg_scelle` → `c0305919…` ;
  - « LANCEMENT CONFORME : code 78671d9362c8, addendum c030591917a0 » ;
  - **361 passed**, égal au nombre des essais du code v12 sur main.
- **A.5** :
  - vastai 1.8.3 ; les trois variables sont présentes ;
  - aucune branche `*0d163bdcea56*` ;
  - inventaire : les trois R8 et 59286520 ; aucun marqueur.
- **Offres** (requête de l'ordre) :
  - rang 1, 58974394 : refusé par `depense projeter` (50,81 USD > 40 ; stockage à 0,1425 USD/h pour 120 Go) ;
  - **rang 2, 58393573** : PRIX_CARTE 0,201389 USD/h, PRIX_STOCKAGE 0,032877 USD/h (`storage_cost` 0,2 × 120 ÷ 730) ;
  - `depense projeter` : 16,86 USD ≤ 40 (`egalite_lots: false`, 18 copies).
- **Création jouée telle qu'imprimée** à 16:03:18 ; `apres-creation` : « CRÉÉE : instance **59288960** » ; `cree_le` 2026-11-05T16:03:20Z.
- **Écarts déclarés** :
  - (1) échéance du jeton : comme R-1567 ;
  - (2) `CONTROLE_IA_GITHUB_TOKEN` pris de `_2`, par son nom (R-1563) ;
  - (3) les essais ont tourné dans un environnement virtuel neuf (`requirements-cpu.txt` de LANCE), parce que pytest manquait.
