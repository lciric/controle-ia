# Copie expurgée du dépôt, pour des évaluateurs — v1

Rédigé le 2026-10-07 par la session, sur la décision de Lazar (« a » : décision 2 du compte rendu du README ; R-104, R-105). Rien n'a été poussé ailleurs que dans ce dépôt : la copie n'existe que sous forme de paquet git, remis à Lazar.

## 1. Ce que c'est

- **Source** : ce dépôt au commit `b7ce54bf3d66cb9d505fe293f016b38225f4255c`.
- **Copie** : un dépôt git d'un seul commit, `f7e5bf6ebc347d6821b4f41ae8f5c38b55f737f5`, branche `main`, auteur « controle-ia (copie expurgée) », date du commit source. Cet identifiant est reproductible : `scripts/depot_expurge.py`, relancé sur le même commit source dans un dossier neuf, redonne le même commit (vérifié le 2026-10-07).
- **Paquet remis à Lazar** : `controle-ia-expurge-b7ce54b.bundle`, 10 278 768 octets, sha256 `1204992c9409ada77bbc3ade81be6591ac4ff12fce8d84d0220698454b5d29de`. Les octets du paquet ne sont pas reproductibles (compression de git) ; le commit qu'il contient l'est. Le paquet porte `HEAD` et `main` : un `git clone` simple suffit.
- **Contenu** : 2 116 fichiers suivis, soit les 2 115 gardés du dépôt et `EXPURGE.md`.
- **Bilan complet** : `bilan-b7ce54b.json` (chaque fichier retiré, son empreinte, sa taille et son motif) ; `EXPURGE-b7ce54b.md`, la page en anglais jointe à la copie.
- **Garde des archives** : avant d'écrire le paquet, le script vérifie qu'aucun fichier retiré ne survit dans une archive gardée. Il cherche dans les zip, les tar et les paquets git, à toute profondeur, par empreinte et par chemin. Une archive d'un format qu'il n'examine pas l'arrête. Ici, 53 fichiers de ces formats ont été examinés, fichiers Word et NumPy compris. La garde est éprouvée sur un cas sain et sur des artefacts : une copie cachée dans un zip, dans un tar imbriqué et dans l'historique d'un paquet git, et une archive compressée d'un format non examiné. Quatre mutations du script ont été rejouées, et les tests les voient toutes (`tests/test_depot_expurge.py`, 6 tests).
- **Quatre constructions écartées**, jamais remises :
  - `895ce28` retirait à tort les gabarits adaptés que le code charge, et nos fichiers de vérification (un `*` traversait les dossiers). La suite de tests lancée dans la copie a donné 1 échec.
  - `f3ba1c4` retirait les transcriptions d'origine des invites de arXiv 2606.07054, qu'un test de TRACE-lite compare aux gabarits : 1 échec.
  - `11886b1` passait les tests, mais elle retirait l'ancien paquet git à la racine alors qu'une copie identique restait dans `livrables/premier-rendu-v1.zip`, et la page EXPURGE le disait omis. Son paquet ne portait pas non plus `HEAD`, si bien qu'un clone simple échouait. Les deux défauts ont été trouvés en essayant les consignes de la section 5 et en parcourant les zip gardés.
  - `b3b2082` a été arrêtée par la nouvelle garde, sur la feuille de style de la proposition publique (dans son zip). Elle est identique à celle de la proposition EA Funds retirée. C'est notre propre feuille de style, et elle est aussi gardée en fichier : la garde ne compte désormais que les contenus que la copie n'a plus. Aucun paquet n'a été écrit.

## 2. Ce qui est retiré, et pourquoi

188 fichiers, 392,3 Mo :

| nombre | motif |
|---|---|
| 119 | copies de PDF d'arXiv de tiers |
| 33 | fichiers de travail des lecteurs et d'un relecteur : pages extraites des PDF de tiers |
| 4 | texte complet ou extrait d'un papier de tiers (dont deux archives d'une contre-vérification) |
| 4 | fichiers de travail des relecteurs de la procédure d'extraction |
| 2 | pages de cartes de modèles (site tiers) |
| 26 | candidature à un autre fonds (EA Funds), confidentielle |

Les sorties de l'extraction (`donnees/`) ne sont pas encore suivies par git ; le motif est prévu pour le jour où elles le seront.

Les empreintes compagnons `.sha256` des fichiers retirés restent : `verifier-arbre` les signale comme orphelines dans la copie, ce qui est attendu et dit dans `EXPURGE.md`.

**L'ancien paquet git reste**, à `livrables/controle-ia-v1.bundle` et en copie dans `livrables/premier-rendu-v1.zip`. Ses cinq commits du 2026-10-04 (84 chemins) ne contiennent aucun fichier visé par l'expurgation ni aucune clé. Je l'ai vérifié à part, puis la garde des archives l'a confirmé.

## 3. Ce qui reste, à savoir

- **Invites gardées exprès** : les invites transcrites de arXiv 2606.08892 (18) et de arXiv 2606.07054 (7), et les 6 gabarits adaptés de ce dernier, parce que le code et ses tests les chargent après vérification de leurs empreintes. Le README de la copie le dit, avec la source. Si Lazar préfère les retirer aussi, les tests qui les chargent échoueront.
- **À relire par Lazar avant de partager** :
  - les registres (`registres/`), tels quels. Ils citent ses messages mot pour mot, mentionnent des instances hors programme sur son compte et donnent les montants de la candidature à EA Funds (remarque K-20 de la vérification du README) ;
  - le brouillon de message aux auteurs de FakeLab (`livrables/premier-rendu-v1/message-fakelab-v1.md`), une demande d'accès à leur environnement, à envoyer par lui.
- **Métadonnées et extraits de tiers** :
  - les réponses de l'API d'arXiv qui ont servi à la sélection scellée des papiers (`diag/20261006-134235-t05-corpus/api-page-0*.xml` : titres, auteurs et résumés de 3 405 papiers) ;
  - les résultats de recherche web de la première antériorité (`docs/sources/anteriorite-web-20261004/`), qui ne contiennent que des extraits courts.

  À ma connaissance, arXiv diffuse ces métadonnées sous licence CC0. Je ne l'ai pas vérifié depuis la session, car le site d'aide d'arXiv n'est pas joignable.
- **Courtes citations** de papiers dans les rapports de lecture, pour vérification ; aucune page entière.
- **Archives restantes** : 35 archives `.tar` (fichiers de travail de nos relecteurs, recalculs des verdicts, essais de l'amorce), parcourues le 2026-10-07. Aucune ne contient de page extraite d'un papier : j'ai cherché par noms de fichiers et par marqueurs de pages, puis lu les fichiers signalés. Un seul PDF reste : notre proposition (`livrables/proposition-publique-v1/`).
- **Aucun jeton ni aucune clé**. La recherche par motifs a couvert tous les fichiers, les membres des archives zip et tar, et les 81 objets de l'ancien paquet. Elle n'a trouvé que des valeurs factices de tests (« FAUX_CLE_… », « SECRET-HIDDEN-ORGANISM-INSTRUCTION »).

## 4. Tests dans la copie

Suite complète lancée dans la copie (commit `f7e5bf6`), avec l'environnement Python du dépôt : 650 tests réussis, en 463 secondes.

`verifier-arbre` sur une reconstruction neuve : 162 problèmes, tous des empreintes orphelines. Ce sont exactement les compagnons gardés des fichiers retirés (même ensemble, vérifié par script), ce qui est attendu.

## 5. Pour la mettre en ligne (geste de Lazar, ou GO de type « dépôt distant »)

```
git clone controle-ia-expurge-b7ce54b.bundle controle-ia-evaluation
cd controle-ia-evaluation && git log -1 --format=%H      # f7e5bf6ebc347d6821b4f41ae8f5c38b55f737f5
# créer sur GitHub un dépôt PRIVÉ vide (par exemple controle-ia-evaluation), puis :
git remote set-url origin https://github.com/lciric/controle-ia-evaluation.git
git push -u origin main
```

Ces consignes ont été essayées le 2026-10-07 avec un dépôt distant factice, local : clone, identifiant et envoi réussis, et le dépôt factice porte `f7e5bf6` sur `main`.

**Accès des évaluateurs, à vérifier dans GitHub au moment de les inviter** (la documentation de GitHub n'était pas joignable depuis la session) : sur un dépôt de compte personnel, un collaborateur invité peut, à ma connaissance, aussi pousser, car il n'y a pas de rôle en lecture seule. La lecture seule demande un dépôt d'organisation, avec le rôle Read. Autre voie : envoyer le paquet lui-même, ou une archive du contenu (`git archive --format=zip -o controle-ia-evaluation.zip main`, dans le clone ; essayé : 2 116 fichiers).

La session peut le faire elle-même sur un GO de type « dépôt distant » consigné dans `registres/go.md`, si ses accès à GitHub le permettent.
