# P3-bis — relecture courte de l'écart du brouillon 11 au candidat 1 (marqueur `CANDIDAT_RELU`) — v1

- Date : 2026-11-11, de 13:06 à 13:15 UTC (`date -u`).
- Relecteur : agent neuf, **Claude Fable 5.2** (`claude-fable-5-2`). Je n'ai écrit ni P3-bis, ni son code, ni sa chaîne,
  ni aucune de leurs contre-lectures, ni aucun de leurs couples. Le rédacteur du candidat 1 est un autre modèle
  (Claude Opus 5.5, R-2342).
- **T0.7 non lu** : ni son texte, ni ses brouillons, ni ses notes, ni son code, hormis
  `src/controle_ia/t07/plancher_v2.py`, que P3-bis importe. Aucun `diag/` ni `runs/` ouvert ; aucune donnée lue ;
  processeur seulement ; aucune dépense ; aucun appel de modèle ; `git` en lecture seule (`show`, `diff`, `ls-tree`,
  `archive` vers le bac à sable) ; aucun commit.
- Texte de départ (dernier texte contre-lu) : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon11.md`
  (`409c37ed4aa4f149…`, égal à son compagnon ; contre-lecture 4 `90847ae2d017c6e1…`).
- Texte relu : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat1.md`
  (`9a56a657b1fad1e23b0cc11e41831f066eed48674159dbc55c2a869aa56c4271`, égal à son compagnon).

## Verdict

**« Relu, conforme ».** Le candidat 1 (`9a56a657…`) est, à l'octet, le brouillon 11 auquel on applique les 40 couples du
brouillon 12, les 37 couples RA puis les 27 couples C1 du texte. Les 31 couples qui touchent une section gelée sont
tous rattachés à leur décision et n'y changent rien d'autre. « Hypothèse » et « Prédiction chiffrée et signe attendu »
sont égales à l'octet au brouillon 11. Les quatre marqueurs remplis renvoient à des pièces que j'ai retrouvées et
recalculées. La place de la phrase « date tenue » est prête.

Aucun couple de correction exigé. Aucun nœud. Cinq notes, dont une formulation que la mère peut resserrer si elle le
veut (N-1, couple proposé, facultatif).

**Portée** : ce verdict vaut pour le texte `9a56a657…` seul. La version qui remplira `CHAINE_P3BIS`, `CANDIDAT_RELU` et
la phrase « date tenue » est un texte neuf : son écart à `9a56a657…` reste à contrôler par programme (N-4).

## 1. Couples réappliqués par mon programme (textes à l'octet)

Programme écrit par moi, sans import des scripts des rédacteurs (annexe A) : chaque « ancien » doit apparaître
exactement une fois dans le texte courant, puis est remplacé.

| étape | couples | résultat |
|---|---|---|
| brouillon 11 (`409c37ed…`) + couples du brouillon 12 (`a8a93037…`, 40 : CL4-C01 à C17, B12-01 à B12-23) | 40, tous à une occurrence | **= brouillon 12 (`07b16063…`) à l'octet** |
| brouillon 12 + RA (`41f8c885…`, 35 couples sur le texte, options RA-23 et RA-24 comprises) | 35, tous à une occurrence | texte intermédiaire `52ed766b…` |
| + C1 (`b2cd422e…`, 27 couples sur le texte) | 27, tous à une occurrence | **= candidat 1 (`9a56a657…`) à l'octet** |
| configuration brouillon 1 (`8ab04d54…`) + RA-35 | 1 | = configuration brouillon 2 (`3f8d0042…`) à l'octet |
| configuration brouillon 2 + C1-28 | 1 | = configuration du candidat 1 (`612b0c6c…`) à l'octet |

Les 37 couples RA et les 28 couples C1 sont donc tous employés (35 + 1 + 1 et 27 + 1). Empreintes vérifiées avant
lecture : script du candidat `8dba350f…`, journal `e4decfce…`, rapport du code `0f57e202…`, contre-lecture courte du
code `03f1bb59…` ; tous les compagnons `.sha256` du dossier et des pièces du candidat sont justes.

## 2. Sections gelées

Sept sections gelées : « Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil », « Plan
d'analyse », « Critères de lecture gelés », « Liste d'arrêt ». Mon programme (annexe B) situe chaque couple dans sa
section réelle au moment où il s'applique et la compare à la section que le couple déclare.

- Les 102 couples du texte tombent dans la section qu'ils déclarent ; **aucun couple déclaré « non gelé » ne touche une
  section gelée**. (B12-17 s'accroche au titre « ## Devis » pour insérer avant lui : hors section gelée.)
- **31 couples gelés** : 5 du brouillon 12 (CL4-C05, C08, C10 au plan ; C07, C09 à la liste d'arrêt : écrits par la
  contre-lecture 4, déjà relus à l'octet, R-2237) et **26 au candidat 1** (24 RA, 2 C1), comme le texte le déclare.
  La table « du 12 au candidat 1 » nomme les 26.
- Empreintes des sections (12 premiers caractères) :

| section | brouillon 11 | brouillon 12 | candidat 1 |
|---|---|---|---|
| Hypothèse | `2bb1c2246620` | égale | **égale** |
| Prédiction chiffrée et signe attendu | `30ca8bfce46d` | égale | **égale** |
| Métrique | `8feed020d3d5` | égale | `0ab27d04d7ba` |
| Seuil | `26064e6f8e10` | égale | `336bd5f15965` |
| Plan d'analyse | `b5aea8b53705` | `bb4555f80abb` | `a3a0b7dbc9ad` |
| Critères de lecture gelés | `65ae5d2f6e59` | égale | `1172140ba92e` |
| Liste d'arrêt | `7ec700910665` | `49ee441cc9a5` | `65cbb244fc29` |

Comme le texte entier égale les couples appliqués, tout écart d'une section gelée appartient à l'un des 31 couples
(27 blocs de lignes changés, comptés par programme, annexe C).

### Rattachement de chaque couple gelé du candidat 1

| couples | section | ce qui change | décision | justifié ? |
|---|---|---|---|---|
| RA-06, RA-08 | Métrique | l'état décisif E est calculé par `lecture_p3bis_v2` sous la règle (a'), et non plus recopié de `lecture-p3.json` | R-2296 (1) | oui |
| RA-07 | Métrique | plancher de 800 directions, les 200 premières celles de P3 ; règle (a') décisive ; ancienne règle sur 200, information | R-2296 (1), (2) ; R-2320 | oui |
| RA-09 | Métrique | PB-13 sous la règle (a'), 800 directions | R-2296 (« même définition de « au-dessus » ») ; R-2320 (« PB-13 à aligner ») | oui |
| RA-10 | Métrique | PB-9 comparé par nom sur les 430 sondes de P3 ; directions 200 à 799 déclarées neuves | R-2320 (« PB-9 reste éprouvable ») | oui |
| RA-11, RA-12 | Seuil | « au-dessus » = borne basse de la différence appariée D strictement positive, 800 directions | R-2296 (1) ; R-2320 | oui |
| RA-13 | Seuil | ancienne règle rapportée, jamais décisive ; réserve R-R si les issues diffèrent | R-2296 (2) | oui |
| RA-14, RA-15 | Plan | 800 sondes par plancher, 1 600 notées en ligne | R-2320 | oui |
| RA-16, RA-17, RA-18 | Plan | module `lecture_p3bis_v2`, ses sorties, module d'ouverture v3 pour `fermer` | R-2296 (3) | oui |
| RA-19 | Plan | essai différentiel de fermeture rejoué au commit du code (règle écrite au texte : arbre gelé changé) | R-2296 (3) | oui |
| RA-20 | Plan (point 10) | puissance et aire minimale détectable refaites sous (a') | R-2296 (3) ; R-2320 ; R-2299 (perte de puissance) | oui (N-1 : un mot) |
| C1-16 | Plan (point 2) | marqueur `LONGUEURS_P3BIS` rempli | marqueur défini au brouillon 11 ; phase 1, R-2295 | oui (remplissage, aucune règle) |
| RA-21, RA-22 | Critères | champs lus dans la lecture de la règle (a') | R-2296 | oui |
| RA-23, RA-24, RA-26 | Critères | PB-6, PB-5, PB-7 (phrases descriptives) lus sous la règle (a') | R-2296 (« même définition de « au-dessus » ») ; options acceptées par la mère, R-2337 | oui (N-2) |
| RA-25, RA-28 (seconde part) | Critères | les deux réserves d'audit jointes au nul de P3, hors des guillemets de la phrase gelée | R-2299 | oui |
| RA-27, RA-28 (première part) | Critères | cinquième réserve gelée R-R | R-2296 (2) | oui |
| C1-17 | Critères | le lecteur du verdict exige la commande `lecture_p3bis_v2` et `resultat.etat_decisif.regle`, sinon « non lisible », nœud | **R-2340 (CLP-05)** ; R-2296 | oui |
| RA-29 | Liste d'arrêt | gardes de la lecture complémentaire v2 | R-2296 (3) | oui |

### Rien d'autre n'a changé (par programme, annexe C)

- **Hypothèse, prédiction, signe** : les deux sections sont égales à l'octet au brouillon 11.
- **Niveaux** : dans les sections gelées, aucune occurrence de « 95 % », « 97,5 % », « 0,95 », « 0,025 »,
  « 2 000 tirages », « strictement » n'est perdue ; les seules occurrences neuves sont dans les couples ci-dessus. Le
  quantile reste 0,95, le niveau 95 % (97,5 % pour A contre H), 2 000 tirages par blocs de tâches.
- **Jeu décisif et sonde décisive** : « saboteur-temoin » (4 et 1 occurrences) et
  `tromperie-difference_moyennes-c15` (1 et 2 occurrences) inchangés ; au code du commit `5e457525`,
  `JEU_DECISIF` et `SONDE_P_ATTENDUE` sont ceux de la v1, importés.
- **Issues** : la table des issues (lignes 1 à 5) est égale ; toutes les phrases entre guillemets des sections gelées
  du brouillon 11 se retrouvent au candidat (seul écart : une majuscule et un retour à la ligne dans « Non au-dessus »,
  « Seuil », déclaré E-5) ; `issue_mecanique` est la fonction de la v1, qui ne lit que E′ (`ISSUE_PAR_ETAT` inchangé).
  Les phrases neuves entre guillemets sont : la réserve R-R, les deux réserves d'audit, « non lisible », et des noms.
- **Mots retirés par les couples gelés** : uniquement « 200 », « 400 », les noms `lecture_p3bis_v1`,
  `ouverture_p3bis_v2` (pour `fermer`), `statistiques.detection`, les champs `resultat.etats_des_jeux[p][…]` de
  `lecture-p3.json`, l'ancienne définition de « au-dessus », « quatre » (réserves, devenu « cinq ») et le marqueur.

### Pièces citées par les couples gelés, vérifiées (R6)

- `t07/plancher_v2.py` au commit `5e457525` : blob `dce61796bbbeba257b3cd2ea31207f8de43c9d77`, égal au blob du commit
  C7 `b4cd9953…` (ancêtre de `main`) ; sha256 `a0f80e68…` : justes.
- Code du commit `5e457525` : `COMMANDE` = `python -m controle_ia.premier_test_ia.lecture_p3bis_v2`, écrite au champ
  `commande` du manifeste ; `etat_decisif` porte `regle` et `lecture` (dont `plancher_quantile`) ; `regle_ancienne_200`,
  `jeux_regle_a` (clés `saboteur-honnete`, `temoin-honnete`, `mention-honnete`, `saboteur-mention`), `issue_mecanique`,
  R-R, `identite_pb9` existent ; `N_PLANCHER` = 800, 200 pour l'ancienne règle ; renvois de lignes justes
  (`statistiques.py` l. 96-125, `lecture.py` l. 231 et l. 286-288).
- Essai de fermeture v3 : script `785cb20b…` au commit `5e457525` ; sortie `93756286…` : 18 lignes « CONFORME », dernière
  ligne « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME », jouée au commit `5e457525`, arbre propre, code 0.
- Note de dimensionnement `1613d5bd…` : les 18 chiffres de RA-20 s'y retrouvent (0,0100 [0,0037 ; 0,0216] ;
  0,0200 [0,0115 ; 0,0323] ; 0,0417 [0,0271 ; 0,0609] ; 0,680 ; 0,6567 ; 0,362, 0,619, 0,912 arrondis à 0,36, 0,62, 0,91 ;
  ≈ 0,662 à 0,682 ; ≈ 0,735 et 0,785, « non simulé »).
- Audit `57f16378…` : les deux réserves citées par RA-28 s'y trouvent **mot pour mot**, au § 7 (recherche par
  programme ; je n'ai lu de ce rapport que ces deux phrases).

## 3. Marqueurs remplis

| marqueur | valeur du texte | pièce | contrôle |
|---|---|---|---|
| `TESTS_ATTENDUS_P3BIS` | 531 | `docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/essais-cibles-p2-sortie-brute-v1.txt` au commit `dfb1ed7b` (`git show`) | sha256 `8d57da16…` = compagnon ; dernière ligne « 531 passed in 1018.40s (0:16:58) » ; rapport de phase 1 : Python 3.11.18, commit du code `a1de3915` |
| `LONGUEURS_P3BIS` | A = T = B | `longueurs-mesurees-p3bis-v1.json` (`4e5093bc…`), `longueurs-attendues-p3bis-v1.json` (`7c94d43c…`), même commit | empreintes = compagnons ; 60 tâches distinctes ; **A = T = B recalculé** sur les quatre mesures ; résumé recalculé par moi = fichier des longueurs attendues |
| `EMPREINTE_CONSIGNES_P3BIS` | `7d35576d65c0…` | `brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-brouillon2.md` | sha256 recalculé égal ; égal à `consignes_sha256` de la configuration du candidat ; ce sont les consignes mesurées par la phase 1 |
| `EMPREINTE_CONFIG_P3BIS` | `512d5b72210c…` | `…-candidat1-pieces/P3-bis-temoin-positif-config-v1-candidat1.json` (`612b0c6c…`) | **recalculé par `manifeste.config_canonique` : `512d5b72210c6d8976967b67b9f7a89f9397ce6cc10b2bd8c1b8c26e134e9273`** ; seuls écarts au brouillon 1 : `n_plancher` 200 → 800 et `consignes_sha256` ; écarts à la configuration de P3 (`702303e9…`) : les six que le texte écrit, aucun autre |

Compléments vérifiés :
- **N reste 531 au commit du code `5e457525`** : la liste `scripts/essais-cibles-p3bis-v2.txt` (`3ecf3cda…`, 30 fichiers)
  et ses trente fichiers sont égaux entre `a1de3915` et `5e457525` ; dans `src/`, `tests/`, `scripts/`, les
  `requirements-*.txt`, `pyproject.toml` : **quinze ajouts, aucune modification**. Voir N-3.
- **Programme du bloc 7** : extrait par moi de `controles_avant_depense_p3bis_v1.sh` et `_v2.sh` au commit `5e457525` :
  `857fbde3…` dans les deux ; il ne lit pas `n_plancher` : la mesure faite avec la configuration brouillon 1 vaut pour
  celle du candidat (écart E-4 du rédacteur, fondé).
- Marqueurs restants au candidat : `CHAINE_P3BIS` et `CANDIDAT_RELU`, une occurrence chacun (`grep`).

## 4. Phrase « date tenue » (P-11)

Prête. Section « Décisions pour Lazar », alinéa « Candidat 1 » (l. 2227-2230) : la date n'est pas encore tenue ; la
place et la forme sont écrites (« date tenue : défaut échu, R-… », ou les mots de Lazar recopiés), à écrire par la
version qui remplit `CHAINE_P3BIS` et `CANDIDAT_RELU`, avant S. L'échéance est juste : R-2021 est datée du 2026-11-09 à
16:03 UTC, plus 48 heures. P-11 (table des préalables) et CL4-13 disent la même chose. La phrase gelée du plan (point 8)
est conditionnelle (« sans mot de Lazar sous 48 heures…, elle tient ») : elle reste vraie après le défaut, sans couple
gelé. La date `2026-11-20T12:00:00Z` est aussi la constante `DATE_RENDEZ_VOUS` du code au commit `5e457525`.
À ma lecture (13:09 UTC), le défaut n'est pas échu.

## 5. Notes (aucune ne bloque)

- **N-1 — « niveau tenu » (RA-20, plan, point 10).** La note `1613d5bd…` et R-2320 disent « ne dépasse le nominal de
  façon établie à aucun k » ; au plafond, l'intervalle [0,0115 ; 0,0323] contient le nominal 0,025. « Niveau tenu » dit
  un peu plus que la pièce. Les chiffres et intervalles sont écrits à côté, la pièce est citée : le lecteur n'est pas
  trompé. **Couple facultatif** (section gelée « Plan d'analyse », une occurrence au candidat) : ancien
  `**niveau tenu** — 0,0100` ; nouveau `**aucun dépassement établi du niveau** — 0,0100`. S'il est appliqué, il entre
  dans l'écart à contrôler de N-4. Le verdict ne dépend pas de ce couple.
- **N-2 — PB-5, PB-6, PB-7 sous la règle (a').** RA-23, RA-24 et RA-26 changent la source de trois phrases
  descriptives. R-2296 ne les nomme pas ; elle fixe « même définition de « au-dessus » », et la mère a accepté les
  options (R-2337). Aucune issue n'en dépend (l'issue ne lit que E′). Pour information de Lazar.
- **N-3 — N = 531 sous Python 3.11 est compté au commit `a1de3915`**, pas au commit du code `5e457525`. Le texte le
  dit et le fonde sur l'invariance de la liste et de l'arbre (vérifiée ici) ; le développeur retrouve 531 sous Python
  3.13 au commit `da683900`, dont `5e457525` ne diffère que par sept compagnons et un fichier d'essais hors liste
  (vérifié). Le bloc 8 des contrôles recompte N au commit S. Je n'ai pas rejoué la liste. R-2337 écrit « 30 neufs »,
  le texte « 31 » : le texte a raison (quatre fichiers ; l'écart est déclaré au rapport du code).
- **N-4 — texte suivant.** Le remplissage de `CHAINE_P3BIS`, de `CANDIDAT_RELU` et de la phrase « date tenue » fera un
  texte neuf, que cette relecture ne couvre pas. Contrôle suffisant : par programme, ce texte égale `9a56a657…` plus
  des couples tous hors sections gelées (les sept empreintes de section du tableau du § 2 inchangées, sauf « Plan
  d'analyse » si N-1 est appliqué).
- **N-5 — `ouverture_p3bis_v2 ouvrir` (plan, point 6, inchangé depuis le brouillon 11).** La chaîne v2 joue
  `lectures-fermees` par `ouverture_p3bis_v3` ; le texte nomme la v2 pour la garde d'ouverture. Les deux modules ont la
  même source hors de trois blocs (contre-lecture courte du code, `03f1bb59…`) : aucun effet. À savoir au moment
  d'ouvrir.

## Ce que je n'ai pas fait

- Je n'ai pas rejoué les essais (ni les 531, ni les 31 neufs), ni l'essai de fermeture, ni la chaîne.
- Je n'ai pas relu les 71 couples non gelés pour leur fond ; je les ai réappliqués et situés hors des sections gelées.
- Je n'ai pas vérifié les renvois du texte à T0.7 (section « Concordance »), par consigne.
- Je n'ai lu le rapport du code et la contre-lecture courte du code que pour leurs constats (CLP-04 à CLP-09) et leurs
  comptes ; l'audit de P3 que pour les deux phrases citées.

## Pour le marqueur `CANDIDAT_RELU`

Texte de départ : brouillon 11, `409c37ed4aa4f149…`. Texte relu : candidat 1, `9a56a657b1fad1e2…`. Rapport : ce
fichier, `brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat1-relecture-courte-v1.md`, empreinte dans son compagnon
`.sha256`. Relecteur : Claude Fable 5.2, agent neuf. Verdict : « relu, conforme ».

## Annexes — mes programmes (bac à sable `…/scratchpad/relu-p3bis-c1/`, recopiés ici pour qu'ils se rejouent)

Lancés depuis la racine du dépôt par `.venv/bin/python <script> <dossier de sortie>`.

### Annexe A — reappliquer.py (`12a3e8f3ef0a8c757982b3ee7c3d388b3ec0643648ef93dea379bc3f3bdbe13e`)

```python
# Relecteur CANDIDAT_RELU : réapplication indépendante des couples (aucun import des scripts des rédacteurs)
import json, hashlib, sys
B="brouillons/P3-bis-temoin-positif-v1/"
def h(b): return hashlib.sha256(b).hexdigest()
def lire(p): return open(p,"rb").read()
def appliquer(texte, couples, nom):
    for c in couples:
        a=c["ancien"].encode(); n=c["nouveau"].encode()
        k=texte.count(a)
        if k!=1:
            print(f"  !! {nom} {c['id']}: {k} occurrences de l'ancien"); 
            if k==0: continue
        texte=texte.replace(a,n,1)
    return texte
b11=lire(B+"P3-bis-preenregistrement-v1-brouillon11.md")
b12=lire(B+"P3-bis-preenregistrement-v1-brouillon12.md")
c1=lire(B+"P3-bis-preenregistrement-v1-candidat1.md")
cb12=json.load(open(B+"P3-bis-preenregistrement-v1-brouillon12-couples-v1.json"))
ra=json.load(open("docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/couples-proposes-p3bis-regle-a-v1.json"))
cc1=json.load(open(B+"P3-bis-preenregistrement-v1-candidat1-pieces/P3-bis-preenregistrement-v1-candidat1-couples-c1-v1.json"))
print("b11",h(b11)[:8],"b12",h(b12)[:8],"c1",h(c1)[:8])
t=appliquer(b11,cb12,"B12"); print("b11+B12 == b12 :", t==b12, h(t)[:8])
fich=set(c.get("fichier") for c in ra+cc1); print("fichiers visés:",fich)
md=B+"P3-bis-preenregistrement-v1-brouillon12.md"
t2=appliquer(b12,[c for c in ra if c["fichier"]==md],"RA"); print("apres RA",h(t2)[:8])
t3=appliquer(t2,[c for c in cc1 if c["fichier"]==md],"C1"); print("b12+RA+C1 == candidat1 :", t3==c1, h(t3))
open(sys.argv[1]+"/b12_ra.md","wb").write(t2)
# options
print("RA options:",[c["id"] for c in ra if c.get("option")])
# autres fichiers
for f in fich-{md}:
    src=lire(f); cs=[c for c in ra if c["fichier"]==f]; r=appliquer(src,cs,"RA-cfg"); cs2=[c for c in cc1 if c["fichier"]==f]; r=appliquer(r,cs2,"C1-cfg")
    print(f, "->",h(r)[:8], [c["id"] for c in cs+cs2]); open(sys.argv[1]+"/cfg_reappliquee.json","wb").write(r)
# défaire
t=c1
for c in reversed([c for c in cc1 if c["fichier"]==md]+[]):
    assert t.count(c["nouveau"].encode())>=1,c["id"]
```

### Annexe B — sections.py (`e80561d36c4be23f636fc4f4931546acb287e491df845095d4db7f67446aeba5`)

```python
import json, hashlib, re, sys
B="brouillons/P3-bis-temoin-positif-v1/"
GEL=["## Hypothèse","## Prédiction chiffrée et signe attendu","## Métrique","## Seuil","## Plan d'analyse","## Critères de lecture gelés","## Liste d'arrêt"]
def lire(p): return open(p,"rb").read().decode()
def sections(t):
    # découpe par titres de niveau 2 ; rend dict titre -> texte
    pos=[(m.start(),m.group(0).strip()) for m in re.finditer(r"(?m)^## .*$",t)]
    d={}
    for i,(p,ti) in enumerate(pos):
        fin=pos[i+1][0] if i+1<len(pos) else len(t)
        assert ti not in d, ti
        d[ti]=(p,fin)
    return d
def section_de(t,off):
    for ti,(a,b) in sections(t).items():
        if a<=off<b: return ti
    return "(avant la première section)"
b11=lire(B+"P3-bis-preenregistrement-v1-brouillon11.md"); b12=lire(B+"P3-bis-preenregistrement-v1-brouillon12.md"); c1=lire(B+"P3-bis-preenregistrement-v1-candidat1.md")
md=B+"P3-bis-preenregistrement-v1-brouillon12.md"
lots=[("B12",json.load(open(B+"P3-bis-preenregistrement-v1-brouillon12-couples-v1.json"))),
 ("RA",json.load(open("docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/couples-proposes-p3bis-regle-a-v1.json"))),
 ("C1",json.load(open(B+"P3-bis-preenregistrement-v1-candidat1-pieces/P3-bis-preenregistrement-v1-candidat1-couples-c1-v1.json")))]
t=b11; gel=[]
for nom,cs in lots:
    for c in cs:
        if c.get("fichier",md)!=md: continue
        off=t.index(c["ancien"]); s=section_de(t,off); s2=section_de(t,off+len(c["ancien"])-1)
        g = s in GEL
        decl=c.get("section_gelee")
        ok = (bool(decl)==g) and s==s2
        print(f"{c['id']:8} gelée={g!s:5} déclarée={decl!s:40.40} section réelle={s[:45]:45} {'OK' if ok else '!! ECART'} | {c.get('decision','')[:60]}")
        if g: gel.append((c["id"],s,c))
        t=t.replace(c["ancien"],c["nouveau"],1)
assert t==c1
print(len(gel),"couples en sections gelées")
s11=sections(b11); s12=sections(b12); sc=sections(c1)
for g in GEL:
    x=b11[slice(*s11[g])]; y=b12[slice(*s12[g])]; z=c1[slice(*sc[g])]
    print(g, "| b11==b12:",x==y,"| b12==c1:",y==z,"| b11==c1:",x==z, hashlib.sha256(z.encode()).hexdigest()[:8])
json.dump([(i,s,c) for i,s,c in gel],open(sys.argv[1]+"/gel.json","w"),ensure_ascii=False,indent=1)
```

### Annexe C — gele_fond.py (lit gel.json écrit par B) (`76b0da3313e5ad120c3fb0517555cd1d7a2d6222359eb3b9599637bb657821cd`)

```python
import json, re, difflib, sys
B="brouillons/P3-bis-temoin-positif-v1/"
GEL=["## Hypothèse","## Prédiction chiffrée et signe attendu","## Métrique","## Seuil","## Plan d'analyse","## Critères de lecture gelés","## Liste d'arrêt"]
def lire(p): return open(p,"rb").read().decode()
def sec(t,ti):
    m=re.search(r"(?m)^"+re.escape(ti)+r"\s*$",t); a=m.start(); n=re.search(r"(?m)^## ",t[m.end():]); return t[a:m.end()+n.start()]
b11=lire(B+"P3-bis-preenregistrement-v1-brouillon11.md"); c1=lire(B+"P3-bis-preenregistrement-v1-candidat1.md")
g=json.load(open(sys.argv[1]+"/gel.json"))
print("### 1. Mots retirés par chaque couple gelé (ancien -> nouveau, au mot)")
for i,s,c in g:
    a=re.findall(r"\S+",c["ancien"]); n=re.findall(r"\S+",c["nouveau"])
    sm=difflib.SequenceMatcher(None,a,n,autojunk=False)
    ret=[" ".join(a[i1:i2]) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag in("delete","replace")]
    pure = c["ancien"] in c["nouveau"]
    print(f"{i:8} insertion pure={pure!s:5} retirés={ret}")
print("### 2. Lignes des sections gelées du brouillon 11 absentes du candidat (toute ligne retirée ou modifiée)")
tot=0
for ti in GEL:
    x=sec(b11,ti).split("\n"); y=sec(c1,ti).split("\n")
    sm=difflib.SequenceMatcher(None,x,y,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag!="equal":
            tot+=1; print(f"[{ti}] {tag} b11 l.{i1+1}-{i2} ({i2-i1} lignes) -> c1 l.{j1+1}-{j2} ({j2-j1} lignes)")
print("blocs changés:",tot)
print("### 3. Phrases entre guillemets « … » des sections gelées du brouillon 11 : toutes présentes au candidat ?")
for ti in GEL:
    x=sec(b11,ti); y=sec(c1,ti)
    qx=re.findall(r"«[^«»]*»",x); qy=re.findall(r"«[^«»]*»",y)
    from collections import Counter
    cx,cy=Counter(qx),Counter(qy)
    perdues=[q for q in cx if cy[q]<cx[q]]; neuves=[q for q in cy if cy[q]>cx[q]]
    print(f"[{ti}] {len(qx)} -> {len(qy)} ; perdues: {perdues} ; neuves: {len(neuves)}")
    for q in neuves: print("    +",q[:230].replace("\n"," "))
print("### 4. Jetons de niveau, de jeu et de sonde dans les sections gelées (b11 -> c1)")
for tok in ["95 %","0,95","97,5 %","0,025","2 000 tirages","saboteur-temoin","tromperie-difference_moyennes-c15","« vu »","« non vu »","« non tranché »","« échec »","PB-1","PB-2","0,70","300","1 %","200","800","strictement"]:
    print(f"{tok:36}", [ (sec(b11,ti).count(tok), sec(c1,ti).count(tok)) for ti in GEL])
```

