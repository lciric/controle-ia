# Contre-lecture courte et différentielle du code de T0.7, de `dc4cab9d` à `8ae9fc44`, et de l'ordre d'exécution de l'étape A (variante B, brouillon 3) — v3

Contre-lecteur neuf (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, modèle Fable 5.2) : je n'ai écrit ni le
module, ni l'ordre, ni les contre-lectures v1 et v2. Interdits communs v2 (`1ee3b370…`, empreinte vérifiée, lus en entier, règle 9
comprise). Pièces lues, empreintes vérifiées : contre-lecture différentielle v2 (`dd794e2e…`), rapport complémentaire 4 du
développeur (`57b4f7f6…`), ordre brouillon 3 (`b053a220…`), script de l'instance (`99e4c926…`), ligne GO-2026-11-10-06 de
`registres/go.md` de `main`. Code lu par `git diff dc4cab9d 8ae9fc44` et dans un arbre détaché à moi. Heures par `date -u`, le
10 novembre 2026, de 10:02 à 10:30 UTC.

## Verdict

1. **`CODE-T07` est inscriptible au commit `8ae9fc44df4599af1e036e979af46aa8fa8f6185`** : DF-01 à DF-04, DF-06 et DF-08 sont
   réglés, chacun avec cas sain et artefact, sans repli silencieux ; aucun défaut bloquant dans le code ; les 18 empreintes du
   rapport 4 (§ 6) sont égales à mon recalcul ; les comptes d'essais du développeur sont retrouvés (324 passés, 1 sauté, 3 échecs
   attendus), en deux processus successifs (constat E-1).
2. **L'ordre brouillon 3 est contre-lisible** (séquence, gardes, destruction par identifiant, devis sous le plafond, dix marqueurs),
   **mais il n'est pas exécutable tel quel** : deux défauts bloquent son scellement (O-1 : la ligne d'essais attendue ne peut pas
   être celle de la session ; O-2 : un fichier de sortie de plus de 90 Mo arrête le script après l'étape A sans rien pousser,
   sur une instance sans accès), trois sont à corriger (O-3 à O-5). Aucun ne touche les 18 fichiers de `CODE-T07` : ils se
   règlent dans le script (nom neuf, R12) et dans un brouillon 4.

## 1. Défauts de la contre-lecture v2, un par un

| id | état | cas sain / artefact (R5) | ce que j'ai vu à `8ae9fc44` |
|---|---|---|---|
| DF-01 | **réglé** | oui / oui | `repli_etapes_v1.repli` : `exiger_configuration`, puis `lecture_v2.ouvrir(…, "A", …)` (lignes, sceaux, GO, refus de 7a, `CODE-T07`, garde adaptée ; refus journalisé `REFUS-T07`, code 2) **avant** `recalculer` ; recalcul sous `activations-repli-<date>/`, renommé `activations/` après la garde d'équivalence ; rapport scellé à côté, avec l'empreinte des `*.npy` ; reprise seulement sur un rapport couvrant (sceau, run, manifeste de 7b, garde, empreinte) ; relance R11 sous un nom neuf. `repli-recalcul`, `repli-seul`, `etape-a-apres-repli` passent tous par là. Essais : garde puis recalcul puis reprise ; ligne manquante → rien calculé, puis relance ; course refusée avant tout calcul ; équivalence en échec puis relance ; reprise refusée (sans rapport, activation retouchée) ; identité à dose 0, texte décodé, clé ; les deux commandes. Réserves C-1 à C-3 (texte, mineur). |
| DF-02 | **réglé** | oui / oui | `ouvrir` : `CODE-T07` exigée à l'étape B quand `code_t07_exige` est vrai, contrôle remonté avant le bloc d'étape (joué en A et en B) ; passe à blanc : ligne absente ou non conforme → `RefusPasse`, code 2, avant tout ; `controler_code` : `git diff --quiet <commit> -- src/controle_ia` et `git status --porcelain --untracked-files=all` vides, sinon refus. Essais : étape B refusée après retouche puis saine ; passe à blanc absente, conforme, retouchée ; paquet importé changé après C7 ; fichier non suivi. Réserve C-4 (à porter à l'ordre de l'étape B). |
| DF-03 | **réglé** | oui / oui | `etape_a` : jeu `JD` ou `JC` présent avant le rejeu du contrôle 9 et absent après (`rejouer_controle_9` retire la clé d'un jeu vidé), concept lu → `GardeArret` nommée, `arret.json`, code 3. Essai : arrêt nommé, un seul `arret.json`. |
| DF-04 | **réglé** | oui / oui | `passe_blanc_v1.octets_notation` : sceau de `mesures-t06.npz` vérifié, seule la colonne `jetons_notes` lue, 4 × largeur × jetons notés, × 2 copies, contre 0,8 de la mémoire disponible ; mesures illisibles ou absentes → motif d'arrêt écrit, `tient` faux. Essai : besoin écrit et tenue ; 40 Gio → arrêt ; mesures absentes → arrêt. Réserve C-5 (mineur). |
| DF-05 | non fait | — | déclaré par le développeur (mineur, non demandé) ; reste ouvert. |
| DF-06 | **réglé** | — | `raises=AssertionError` (CT-01), `raises=jp.JournalFautif` (deux essais) ; les trois sortent « XFAIL » à mon rejeu. |
| DF-07 | porté à l'ordre | — | le script joue la passe à blanc avant l'étape A, au même commit et à la même configuration, et s'arrête si son code n'est pas 0 ; la règle du rejeu et le nom du journal restent à écrire au brouillon 21. Le journal `journal-verification-v2.txt` est bien dans le dossier des jeux v2 sur `main`. |
| DF-08 | **réglé** | — | résumés des répétitions v5 et repli v3 : `entropie_manifeste` = [1]. |

Aucun repli silencieux trouvé dans le différentiel : chaque branche d'échec lève une garde nommée ou rend un code 2 ou 3 avec motif ;
une panne hors garde dans `repli-seul` (code 1) est traitée par le script comme un nœud (traces poussées, arrêt).

## 2. Constats sur le code (aucun bloquant)

| id | gravité | constat | suite proposée |
|---|---|---|---|
| C-1 | à porter au texte (brouillon 21) | La garde d'ouverture du repli écrit une ligne `OUVERTURE-T07` `etape-A/<run>` : c'est elle, et non plus l'étape A, qui devient la « première ouverture ». Le périmètre des jeux (`sondes_lues`, G5) se ferme donc **avant** le recalcul et la passe à blanc, et reste fermé si le repli finit en nœud R11 sans qu'aucune sonde n'ait rien lu ; `CODE-T07` doit être antérieure à cet instant. Aujourd'hui `main` porte les lignes de J-D et de J-A, pas celle de J-C : un lancement avant son scellement l'exclut pour de bon. | Écrire la règle au brouillon 21 et au préalable P3 de l'ordre. |
| C-2 | mineur | Entre `dossier.rename(act)` et le scellement du rapport, une panne laisse `activations/` sans rapport couvrant : la relance est refusée (R12), jamais silencieuse, mais il faut un geste manuel. | Écrire et sceller le rapport dans le dossier daté avant de le renommer. |
| C-3 | mineur | Le nombre de relances R11 n'est tenu que par la boucle du script (deux essais) ; la commande seule en accepte autant qu'on en lance. Docstring de `lecture_v2` : `etape-a-apres-repli … RAPPORT`, argument que l'analyseur n'a pas. | Texte ; docstring à la prochaine version. |
| C-4 | à porter à l'ordre de l'étape B | Avec DF-02, l'étape B (et toute passe à blanc) doit tourner dans un arbre dont `src/controle_ia/` égale C7 et qui est propre : un clone à la tête de `main`, où d'autres branches auront été fusionnées, sera refusé. | Jouer l'étape B à S7 (tête détachée), `PYTHONDONTWRITEBYTECODE=1`. |
| C-5 | mineur | La passe à blanc juge les deux besoins de mémoire (jeux, notation) l'un après l'autre, chacun contre 0,8 du disponible ; s'ils coexistent dans l'étape A, c'est leur somme qu'il faudrait juger. Non vérifié. `git status` ne voit pas un fichier ignoré par `.gitignore` sous `src/controle_ia/` hors de `t07/`. | À dire au brouillon 21 ou à vérifier à la prochaine version. |

## 3. Ordre d'exécution, brouillon 3, et script `etape_a_t07_variante_b_v1.sh`

Conforme : séquence (minuterie, machine, code S7 et C7, registres de `main`, sortie de 7b par refspec et fichiers nommés, paquets,
modèle, essais, `CODE-T07`, branche neuve, repli garde d'abord, passe à blanc, étape A, fin) ; `lecture-sondes-t06.json` jamais
listé ni extrait (motif d'exclusion, liste nommée de `donnees/<run>/`, fonction `interdit`, deux contrôles de présence) ; clone de
la seule branche `main` ; destruction par l'identifiant créé (R10), par la fille et par la minuterie ; `GO_ID=GO-2026-11-10-06`
devant la création ; plafond 20 USD, minuterie à création + 12 h (≤ 15,6 USD de carte, ≤ 17,7 USD tout compris), compte rendu à
10 USD, arrêt à cumul + un quart d'heure ≥ 20 ; dix marqueurs, une occurrence chacun (compté) ; `bash -n` sans erreur ; passage
du script en base64 comme l'amorce de T0.6 (`lancer_t06_v13.sh`). Simulation de l'étape 3 du script sur le registre actuel de
`main` : deux chemins cités, aucun interdit, aucun sous `src` ni `tests`.

| id | gravité | constat | correction proposée |
|---|---|---|---|
| O-1 | **bloquant pour l'ordre** | `LIGNE_ESSAIS_T07` ne peut pas être la ligne de la session. L'essai `tests/test_t07_lecture_v2.py` (l. 911) lit `061ac380:scripts/controle_lecture_t06_v1.py` et se saute si le commit manque ; `061ac380` n'est ancêtre ni de `main`, ni de C7, ni de `935262b1` : dans le clone `--single-branch --branch main` de l'instance il manquera, et la ligne sera « 323 passed, 2 skipped, 3 xfailed » (au mieux), d'où l'arrêt de code 2 à l'étape 6, **après** les paquets et le modèle (≈ 0,5 à 2 h payées, création neuve sur écrit de la mère). Les autres sauts dépendent aussi des fichiers extraits ; la répétition locale ne joue qu'un fichier (20 essais). | Mesurer la ligne dans un clone qui rejoue l'extraction du script (branche unique, clone partiel, mêmes motifs, Python 3.11) ; jouer les essais **avant** la descente du modèle. |
| O-2 | **bloquant pour l'ordre**, tant que la taille n'est pas bornée | `pousser` arrête sur tout fichier de plus de 90 Mo, branche déclarée non prête : si une sortie de l'étape A dépasse ce seuil, rien de l'étape A n'est poussé (ni scores, ni registre, ni journal des ouvertures), l'instance passe à « stopped », et le mode « args » ne laisse aucun accès au disque ; l'étape A ne se relance pas sous le texte. Or `scores-actions-t07.npz` est écrit par `np.savez` sans compression : par action notée, 200 scores de plancher pour chaque sonde lue, les deux de T7-P6 et chaque direction de concept (ordre de grandeur, à vérifier : une dizaine de groupes, soit quelques milliers de nombres par action) ; le devis parle de « scores et sondes ≤ 2 Go ». Aucune estimation de taille n'est faite avant l'étape A. | Borner la taille avant l'étape A (nombre d'actions notées, lu par la passe à blanc, × tableaux) et arrêter **avant** si elle dépasse ; ou découper dans le script en morceaux scellés (comme C11 de l'amorce de T0.6), jamais un arrêt après l'étape A sans poussée. |
| O-3 | à corriger | § 10.6 et § 4.7 : « la minuterie la garantit à `ECH` » est faux après la fin du script : la minuterie est un sous-processus du conteneur, que l'état « stopped » demandé par le script éteint. Après « stopped », seule la fille détruit ; le disque court (≤ 0,08 USD de l'heure) sans borne si la session tombe. La minuterie n'écrit pas le code HTTP de ses `DELETE` (sortie jetée) : son échec serait muet ; l'amorce v11 de T0.6 l'écrivait. La clé de l'instance pour `DELETE` n'est pas répétée ici (réel seulement). | Corriger le texte ; échéance côté session (rappel daté de la fille ou de la mère) ; journaliser chaque essai de la minuterie. |
| O-4 | à corriger | `DEPENSE_ANTERIEURE_USD` est défini « sous cette ligne » ; GO-2026-11-10-06 borne la dépense totale **sous GO-2026-11-10-04 et sous elle** à 20 USD. | `ANT0` = dépense inscrite sous les deux lignes ; P8 de même. |
| O-5 | à corriger | Le script recopie de `main` tout `registres/*.md`, dont `registres/index-bras-attaque-v1.md` (non ouvert par moi) ; l'ordre interdit pourtant tout ce qui touche au bras d'attaque (§ 2.3). | L'exclure des motifs et de la boucle de l'étape 3. |
| O-6 | mineur | En-tête du script : « brouillon 2 ». § 4.4 : un écart d'encodage du script imprime « ÉCART » sans arrêter la suite du bloc (le lanceur de T0.6 sortait en code 2). La recopie des journaux du script des jeux n'a jamais tourné avec un journal présent (répétition : « journaux du script : 0 »). | Au brouillon 4 et à la version neuve du script. |

## 4. Essais rejoués

Arbre détaché `/home/user/wt-t07-cl3` à `a4352e6a` (`src` et `tests` égaux à `8ae9fc44`, différence vide vérifiée), extraction
partielle prescrite (sans `docs/sources/` ni `docs/notes/bras-attaque/`), `PYTHONDONTWRITEBYTECODE=1`, un processus à la fois ;
arbre retiré à la fin par son chemin exact (code 0).

| run | heures (UTC) | résultat |
|---|---|---|
| les 14 fichiers `tests/test_t07_*.py`, un processus | 10:03:11 à 10:22:59 | 311 passés, 1 sauté, 3 échecs attendus, **13 erreurs**, 1 186 s (machine partagée) ; les 13 erreurs sont les essais du repli (`test_t07_repli_etapes_v1.py`, 9 ; `test_t07_repli_recalcul_v1.py`, 4), tous sur `docs/sources/invites-2606.08892-v1/index.json` absent de l'arbre prescrit |
| les deux fichiers du repli, dossier d'invites posé | 10:23:47 à 10:25:35 | **13 passés**, 107 s |
| total | | **324 passés, 1 sauté, 3 échecs attendus** : égal au compte du développeur |
| saut et échecs attendus, nommés | 10:25 à 10:26 | saut : `test_t07_lecture_v1.py` l. 504 (branche `origin/prep/t06-candidat8-v1` non récupérée) ; échecs attendus : CT-01, CT-11, cas sain de (xv) |

**E-1, écart déclaré à la lettre de la consigne** : l'arbre prescrit exclut `docs/sources/`, et les 13 essais du repli, cœur de
DF-01, ne peuvent pas y tourner. J'ai posé dans mon arbre, par `git show a4352e6a:<chemin>`, les 68 fichiers nommés du seul dossier
`docs/sources/invites-2606.08892-v1/` (2,2 Mo ; le même que le contre-lecteur de la v2 et que le script de l'instance extraient),
rejoué les deux fichiers, puis retiré ces fichiers avant de retirer l'arbre. Aucune commande git d'écriture pour cela ; rien
d'autre sous `docs/sources/`. Le compte de 324 est donc celui de deux processus successifs, pas d'un seul.

## 5. Empreintes recalculées pour `CODE-T07`

Commit `8ae9fc44df4599af1e036e979af46aa8fa8f6185` ; arbre `src/controle_ia` à ce commit : `013a273b4d47c45e20355b754bd82489f90181f0`
(égal au rapport 4). `git ls-tree` de `src/controle_ia/t07/` : 18 fichiers `*.py`, aucun autre fichier. sha256 de `git show
<commit>:<chemin>`, et des fichiers de l'arbre extrait (égaux) ; **les 18 sont égales à la table du rapport 4, § 6** :

| fichier | sha256 |
|---|---|
| `src/controle_ia/t07/__init__.py` | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/t07/code_t07_v1.py` | `52f44ce039d63813cf406b4827d3bf369f2523831dd58f01101a49520cdf01ec` |
| `src/controle_ia/t07/controle_jeux_v1.py` | `27cf1fba9584f41632af4b352b048ecf46e8cc53695499385dd8c8eddc92a3ae` |
| `src/controle_ia/t07/criteres_v1.py` | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` |
| `src/controle_ia/t07/donnees_p3_t07_v1.py` | `acf02303b98157411dd30881d19ec9457423afdc7c27ef4e9342823234030cf4` |
| `src/controle_ia/t07/garde_adaptee_v1.py` | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` |
| `src/controle_ia/t07/journal_p3bis_v1.py` | `f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73` |
| `src/controle_ia/t07/lecture_v1.py` | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` |
| `src/controle_ia/t07/lecture_v2.py` | `39c56e4b11d915775b47242b63ab1d1c2f56218b38ffc7621d9c3d83bff296f9` |
| `src/controle_ia/t07/lectures_t07_v1.py` | `05328122cdeeedc49b92985df3d9ec41ae668ede8771de3248a10ae3696b4abd` |
| `src/controle_ia/t07/mahalanobis_v1.py` | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` |
| `src/controle_ia/t07/passe_blanc_v1.py` | `ff84d2450d5b4a4b39db8ca7d042805a8efd8261349d0608de0e65442fdab578` |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` |
| `src/controle_ia/t07/registre_v1.py` | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` |
| `src/controle_ia/t07/repli_etapes_v1.py` | `26a6b52151a29f3b65ba4c48027a3ed70890f71fc262ca16bba3e51531dfaff2` |
| `src/controle_ia/t07/repli_recalcul_v1.py` | `9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d` |
| `src/controle_ia/t07/repli_v1.py` | `7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a` |
| `src/controle_ia/t07/sondes_neuves_v1.py` | `d4d354e769de279235a202b1ac803b6b508bb12a374f48d0352db13daaab9bc7` |

Recoupées aussi, égales au rapport 4 (§ 7) : le script de l'instance (`99e4c926…`), les deux scripts de répétition, les six
fichiers d'essais touchés, l'ordre brouillon 3 (`b053a220…`), et les sceaux des pièces des répétitions `variante-b-v2`, `v5` et
`repli-v3` (journal de l'instance : garde, repli « recalcul fait », passe à blanc tenue, étape A code 0, trois poussées).

## 6. Interdits

Tenus. Aucun `lecture-sondes-t06.json` ouvert, ceux des essais compris ; aucune donnée de 7a, aucune branche interdite, aucun
fichier du bras d'attaque ni de l'étiqueteur, ni `scripts/extraire_mesures_epreuve_t06_v1.py`, ni texte d'action de P3 ; aucune
valeur de clé, ni `env` ni équivalent ; aucun appel externe, aucune dépense ; aucune valeur numérique de sonde de 7a sous mes yeux.
Règle 9 : recherches par `git grep` sur des fichiers nommés, `grep` sur des fichiers nommés ; un seul `find`, sur le dossier
`docs/sources/` que j'avais moi-même posé dans mon arbre, pour le vider. Git : la création, l'extraction partielle et le retrait
de mon arbre, prescrits ; aucune autre écriture git. Écarts déclarés : E-1 (ci-dessus) ; des listes de noms de fichiers lues par
`git ls-tree` sur des dossiers nommés non interdits (`src/controle_ia/t07/`, `docs/sources/invites-2606.08892-v1/`,
`donnees/t07-jeux-synthetiques-v2/`) et par `ls registres/`. Aucun refus de permission ni de classifieur.
