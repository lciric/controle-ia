# Rapport — dépôt d'empreintes sur l'Open Science Framework (v1)

Développeur neuf, consigne `docs/notes/g0-deux-semaines-v1/consigne-developpeur-osf-v1.md` ; décision de Lazar
« go OSF » (5 novembre 2026 vers 15:55 UTC). Écrit le 2026-11-05 entre 15:59 et 16:15 UTC (`date -u`).
Rien n'a été commis ni poussé par moi, aucun `.sha256` créé, aucun fichier existant modifié, aucun dépôt réel fait,
aucune clé affichée.

## 1. Fichiers produits et empreintes SHA-256

| fichier | sha256 | lignes |
|---|---|---|
| `scripts/osf_depot_v1.py` | `8f03f62d0ffe2df4a239ef2d1316a7ceeac691f5b5e5c8017a302d719f61d729` | 521 |
| `tests/test_osf_depot_v1.py` | `25f2cb9fd179394fc1fd0a65c38240d6684d48c792bedbc593be0283a78fc656` | 278 |
| `docs/notes/g0-deux-semaines-v1/rapport-osf-depot-v1.md` | (ce fichier ; empreinte dans la réponse finale) | |

Tests : `python -m pytest -q tests/test_osf_depot_v1.py` → **8 passés** (5,6 s). Suite complète lancée à 16:10 UTC
(`python -m pytest -q -x --ignore=tests/test_osf_depot_v1.py`) ; résultat rendu dans la réponse finale.

Ce que le test couvre (R5, cas sain et artefact à chaque garde) :
- `manifeste` sur un arbre factice (dépôt git jetable, trois dossiers, un fichier scellé chacun, un `.json` ignoré) :
  cas sain par l'arbre de travail et par `--ref main` ; déterminisme (second appel = même fichier) ; aucun `.sha256`
  écrit ; artefacts : fichier `.md` sans compagnon → refus, rien écrit (puis `--ignorer-non-scelles` l'exclut en le
  listant dans le manifeste et sur la sortie) ; fichier scellé mais non commis → refus ; fichier altéré après
  scellement → arrêt dur, même avec l'option.
- `deposer` contre un faux serveur HTTP local (interface v2 et service de fichiers factices, en mémoire) : cas sain
  (projet créé privé, deux téléversements, relecture conforme, date rendue par l'interface) ; second dépôt du même
  manifeste → « rien de nouveau », aucune requête PUT ni POST ; manifeste différent sous le même nom → refus (R12) ;
  `--public` rend public un projet existant ; artefact : réponse illisible (HTML au lieu de JSON) → arrêt, **une seule**
  requête vue par le serveur (aucune nouvelle tentative), aucun projet créé ; erreur 401 de l'interface → statut et
  corps imprimés, sans en-tête d'autorisation ; `OSF_TOKEN` absent → rien n'est tenté.
- Le jeton des essais est factice (`monkeypatch`) ; chaque essai vérifie qu'il n'apparaît dans aucune sortie.
  Le script masque de toute façon le jeton dans tout ce qu'il imprime (défense en profondeur).

## 2. Sortie de l'essai à blanc réel (`deposer --a-blanc`)

Une seule requête, `GET https://api.osf.io/v2/users/me/` avec le jeton lu par le nom `OSF_TOKEN` (déjà exporté
dans l'environnement de la session ; jamais passé sur la ligne de commande) :

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-05T16:09:30Z
$ python3 scripts/osf_depot_v1.py deposer --a-blanc
Lazar Ciric
code de sortie : 0
```

Le jeton marche. Rien n'a été créé sur l'Open Science Framework.

## 3. Essai de `manifeste` sur `main` (écrit hors du dépôt, dans le brouillon de session, pour ne rien laisser dans
`livrables/` sans scellement)

- Strict (`--ref main`) : **refus**, 1 fichier — `docs/decisions/decision-sparks-D3-D4-D5-v1.md`, dont le compagnon
  porte le chemin complet au lieu du nom de base (`verifier-arbre` du dépôt le signale déjà ; défaut préexistant, parmi
  82 problèmes connus de l'arbre). Je n'ai pas touché ce compagnon : le corriger est une modification d'un fichier
  existant, à décider par la mère (resceller avec le nom de base, même empreinte, ou exclure).
- Avec `--ref main --ignorer-non-scelles` : **118 fichiers** (51 `prereg/`, 56 `docs/decisions/`, 11 `docs/verdicts/`),
  1 exclu, listé dans le manifeste (`exclus`) et imprimé ; `main` = `a364e947e4c6354c4f0bff37aa784dfffed89351`.
  Manifeste `dd87b23ebc03dbb6b6d00aeeadc6685174aad04cccf72f93b72332a113e061c6`, LISEZMOI
  `d9b508239b8f3471b3491c4ad784aa30fb54881aece894e8fb2c0c642d43760e` ; un second appel rend le même fichier
  (ni heure ni chemin d'écriture dans le manifeste).
- Avec `--ref main --ref prep/sparks-exp7-nul-v12` : mêmes 118 fichiers, aucun préenregistrement propre à la branche
  (ses fichiers scellés de `prereg/` sont ceux de `main`) ; la référence et son commit sont consignés.
- Seuls les `*.md` scellés des trois dossiers entrent (consigne) : les `.json` de `prereg/` et les `.tar` de
  `docs/verdicts/` n'y sont pas ; extension possible en v2 si Lazar le veut.

Branches `prep/*` : le script lit toute référence git par `--ref` (répétable, `main` d'abord) ; chaque entrée porte
`source` (la référence) et `commit` (dernier commit de la référence qui a touché le fichier) ; un même fichier à même
empreinte sur deux références n'est listé qu'une fois (première source gardée). Les branches à inclure sont celles
que nommera la mère ; sur cette machine existent localement `prep/sparks-exp7-nul-v1` à `v12` et `prep/r1-relance-v4`.

## 4. Commande exacte du dépôt (jouée par la mère)

```
cd /home/user/controle-ia-travail
export OSF_TOKEN   # déjà dans l'environnement de la session ; ne jamais l'écrire sur une ligne de commande
# 1. manifeste, sans réseau (ajouter --ref prep/… pour chaque branche retenue ; --ignorer-non-scelles tant que le
#    compagnon de decision-sparks-D3-D4-D5-v1.md n'est pas corrigé)
python3 scripts/osf_depot_v1.py manifeste --ref main --ignorer-non-scelles
# 2. scellement (R6) des deux fichiers produits, par la mère
PYTHONPATH=src python3 -m controle_ia.scellement sceller livrables/osf-manifeste-v1/manifeste-v1.json livrables/osf-manifeste-v1/LISEZMOI.md
# 3. dépôt (projet privé par défaut ; --public pour le rendre public, décision de Lazar)
python3 scripts/osf_depot_v1.py deposer
python3 scripts/osf_depot_v1.py deposer --public
```

`deposer` imprime : l'heure de lancement (`date -u`), « projet créé » ou « projet réutilisé » avec l'identifiant, la
visibilité, pour chaque fichier « téléversé » ou « déjà déposé avec la même empreinte, rien de nouveau », puis la
relecture depuis l'interface : identifiant du projet, adresse, date de dépôt (`date_created`) et dernière
modification, empreinte SHA-256 relue, empreinte locale, verdict CONFORME ou ÉCART (ÉCART = arrêt, code 1),
identifiant du fichier. Un manifeste différent sous le même nom est refusé (R12 : `--sortie …-v2.json`, nouveau
nom) ; seul `LISEZMOI.md` peut être remplacé, sur option explicite `--remplacer-lisezmoi` (l'ancienne version reste
dans l'historique du fichier).

## 5. Ce qu'un tiers vérifie, et comment

1. **Adresse publique** : `https://osf.io/<identifiant du projet>/` (imprimée par `deposer`), fichiers
   `manifeste-v1.json` et `LISEZMOI.md` dans le stockage `osfstorage`. Le projet doit être public pour qu'un tiers
   y accède (sinon seul Lazar, ou un contributeur ajouté, voit la date).
2. **Date** : la date de dépôt affichée par l'Open Science Framework pour `manifeste-v1.json` (métadonnées du fichier,
   champ `date_created` de l'interface). Elle est posée par le tiers, pas par nous.
3. **Empreinte** : l'empreinte SHA-256 du manifeste affichée par l'interface (métadonnées, `hashes.sha256`) ; le tiers
   télécharge le fichier et recalcule `sha256sum manifeste-v1.json` ; les deux doivent coïncider avec celle que la
   mère consigne dans `registres/etat.md` et dans la passation.
4. **Un document donné** : dans le dépôt (copie expurgée publique `lciric/controle-ia`, ou le dépôt de travail sur
   accès), `git show <commit>:<chemin> | sha256sum` doit donner l'empreinte inscrite au manifeste pour ce chemin ;
   le `.sha256` compagnon, lui aussi dans le dépôt, la répète. Si elle coïncide, le document est identique à celui
   qui existait à la date de dépôt du manifeste : antériorité et intégrité, rien de plus (le LISEZMOI déposé le dit).

## 6. Réserves et faits à consigner par la mère

- Pendant mon travail, la session mère a commis deux instantanés de l'arbre contenant des versions intermédiaires de
  mes fichiers (`14863030` à 16:08:09, `2fa5a9df` à 16:09:45 UTC). Je n'ai rien commis. La version finale du script
  sur disque (empreinte ci-dessus) diffère du dernier instantané (champ `nom` au lieu de `sortie` dans le manifeste,
  pour que l'empreinte ne dépende pas du chemin d'écriture) : un nouvel instantané est nécessaire.
- Les champs de l'interface que le script lit (`filter[title]` avec égalité stricte côté script, `links.upload` du
  fournisseur `osfstorage`, `attributes.extra.hashes.sha256`, `date_created`, `date_modified`, création par
  `POST /v2/nodes/` avec `category: project`) sont ceux de l'interface v2 telle que je la connais ; seul
  `GET /v2/users/me/` a été joué en vrai. Le premier dépôt réel est donc aussi l'essai de ces champs : s'il échoue, le
  script imprime statut et corps de la réponse (sans en-tête) et s'arrête sans rien retenter.

## 7. Trois risques

1. **Interface non jouée au-delà de l'essai à blanc.** Un nom de champ ou un format de réponse différent de ce que
   j'attends arrête le premier dépôt réel (c'est voulu : aucun repli silencieux), mais peut laisser un projet créé
   sans fichier, ou un fichier téléversé sans relecture. Le script est idempotent : le relancer après correction ne
   crée rien en double ; la mère doit tout de même vérifier à la main dans l'interface après le premier dépôt.
2. **Un fichier dans un projet n'est pas une inscription figée.** L'Open Science Framework permet de supprimer un
   fichier ou un projet, et un projet privé ne prouve rien à un tiers tant qu'il n'est pas public ; un sceptique peut
   objecter que l'horodatage d'un fichier supprimable vaut moins qu'une « registration » (gel du projet, identifiant
   pérenne, suppression impossible). Nœud pour Lazar : rendre le projet public et, à terme, geler une registration du
   manifeste ; cette v1 ne le fait pas.
3. **La vérification du tiers passe par le dépôt git.** Le manifeste pointe des chemins et des commits du dépôt de
   travail privé ; un tiers ne peut recalculer les empreintes que sur la copie expurgée publique, qui doit garder ces
   fichiers octet pour octet et des commits retrouvables — ou sur un accès accordé. Une expurgation qui altère un
   fichier scellé rendrait l'empreinte invérifiable (pas fausse). Défaut préexistant du même ordre : le compagnon
   mal nommé de `decision-sparks-D3-D4-D5-v1.md`, exclu du manifeste tant qu'il n'est pas corrigé.
