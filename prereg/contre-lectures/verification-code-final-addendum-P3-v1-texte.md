# Vérification finale du module de l'addendum de P3, angle « texte final face au code » (VF1)

**Verdict : scellable après corrections.** Les corrections de CB1, CB3, CB2 et GB6 sont faites et justes. La suite passe
(165 sur 165). Les 51 mutants de CB2 sont tués. Le module lit et compare bien les empreintes citées. Restent cinq écarts
mineurs entre des phrases normatives du texte final et le code (VF1-01 à VF1-05). Tous se corrigent **dans le texte**, sans
toucher au module ni à son empreinte. Sept points pour information suivent.

- Relecteur : sous-agent neuf (R2). Je n'ai écrit ni le texte, ni le module, ni ses tests, ni les corrections. Date :
  2026-10-20 (UTC).
- Angle : texte final face au code. (1) corrections des constats CB1, CB3, CB2 et GB6 ; (2) chaque phrase normative
  changée depuis le brouillon 3, avec la ligne de code qui l'applique ; (3) lecture des lignes d'empreintes du texte ;
  (4) suite complète une fois.
- Rien n'a été écrit hors de `verification-finale/texte/` et de ce rapport. Dépôt de travail en lecture seule : aucun
  fichier nouveau ni modifié (contrôle par `find -newer` et `git --no-optional-locks status` : vide ; HEAD
  `5bc8856f462b37bff80e2f5089018ab3d9a919ff`). Un `git status` lancé au début a pu poser un verrou transitoire
  `.git/index.lock` (date du dossier `.git` changée à 05:03:34) ; l'index n'a pas changé. Aucune commande Vast.ai. Rien lu
  sous `runs/`, `diag/`, `donnees/` ni `traces/` du dépôt.
- Original intact : empreintes du module et des tests de `final-b4/` vérifiées au début et à la fin (`sha256sum -c`,
  `texte/empreintes-original-debut.txt`). Tous mes lancements portent `-B`, `PYTHONDONTWRITEBYTECODE=1` et
  `-p no:cacheprovider`. Aucun cache dans `final-b4/`.

## Ce qui a été lu (avec empreintes)

| fichier | sha256 |
|---|---|
| texte final `P3-addendum-lecture-complementaire-v1-brouillon6.md` (lu en entier) | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` |
| brouillon 3 (diff complet avec le texte final) | `30a99398313dc3752d4b0eca0c75335103b58b81b23d48cee07e854ff66b130b` |
| module `final-b4/complements_p3_v1.py` (2 289 lignes, lu en entier) | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` |
| tests `final-b4/test_complements_p3_v1.py` (en-tête, aides, tests des gardes et de la précision 17) | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` |
| notes `final-b4/NOTES-CORRECTIONS-CB1.md` | `d2e5d4e65793721455092468f54a6a40241498ef7d4249f36b0a706d4201a096` |
| CB1 `rapports/contre-lecture-code-b3-1.md` | `89e1f02b41d62ee7388955d0c23bfbb8b54f2f9e2ea3fa299758f17c0b58e57f` |
| CB3 `rapports/contre-lecture-code-b3-3.md` | `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605` |
| CB2 `rapports/revue-b3-2/rapport-gabarit.md` (section « Preuve du verrou ») | `15732375cccdaeea19189d2508ef1dba5b46b80e9bfc6f1fd23b92e11c04feec` |
| CB2 essais `revue-b3-2/sondes/test_sondes_b3_2.py`, `test_sondes_b3_2_verrou_mutable.py` | `7d012f30…7468`, `69e3ee88…c8f6` |
| CB2 mutants `revue-b3-2/mutants_b3_2.py` (identique à `final-b4/essais/mutants_b3_2.py`) | `b5b7a3fa77291b31604945f1705a427d3803a585fb627000858a5f53328e58bb` |
| traitement `traitement-R2-addendum-P3-v1.md` (sections GB6 et « Code ») | `0d39c03ca759b02bcfc29a5881562a6de94e42fe3e22521a2676636306bdb6b3` |
| banc de CB3 `revue-b3-3/essai_07.log`, `essai_07b_import.log` | `063661ac…9fb7`, `baaf517e…75c7` |
| `verser_addendum_v1.sh` | lu (copie du texte, scellement, contrôle des empreintes) |

Code gelé lu (dépôt, lecture seule) : `premier_test_ia/lecture.py` (l. 92-433), `statistiques.py` (détections, corrélation),
`conditions.py` (en entier), `environnements/propositions.py` (l. 100-140), `sondes/temoins.py` (l. 182-208),
`manifeste.py` (graines, écriture et vérification des résultats), `prereg.py` (en entier), `harnais/validation_reelle.py`
(l. 60-80, 214-240). Empreintes citées par le texte et vérifiées sur disque : brouillon 1 `8efa72dd…`, brouillon 2
`3dfc8a30…`, rapport R2 `cb165339…`, vérification du brouillon 2 `6d3a8a59…`, archive CB2 `738979da…`, CB1 et CB3 :
toutes égales.

## Ce qui a été lancé (comptes)

| quoi | résultat | journal (sous `verification-finale/texte/`) |
|---|---|---|
| (4) suite complète, une fois, sur une copie (`copie-suite/`, empreintes égales à l'original) | **165 passed in 1009.45s (0:16:49)** | `suite-complete.log` (`4f3bda6c…987d`) |
| (3) lignes d'empreintes lues dans le texte final rempli, dépôt jouet, vraie `exiger_garde_1` | **10 cas sur 10 conformes** (2 sains, 8 artefacts) | `essai-empreintes-citees.log` (`c13be9f6…b7dd`) ; script `outils/essai_empreintes_citees.py` |
| (1) les 8 essais de CB2, inchangés, sur le module final | 5 essais qui prouvaient un défaut **échouent** (défaut corrigé) ; 2 essais de propriété passent ; l'essai d'empreinte échoue (module changé, attendu) | `essais/cb2/sondes-cb2-sur-final.log` (`8245a471…f2e`) |
| (1) les 51 mutants de CB2, un par un, sélection `-k`, sur une copie | **51 tués sur 51** ; premier échec = test attendu pour chacun | `mutants/run.log`, `mutants/resultats.jsonl` (`a8c43bb1…a6e`), `mutants/<id>/pytest.log` |
| (2) essais des écarts texte–code | **6 sur 6 reproduits** | `essais/vf/sondes-vf.log` (`8bfc5b0f…f227`), `essais/vf/sondes-vf-2.log` (`7b4a88f5…659c`) |
| (1) relevé des lignes des deux gardes neuves de la ronde finale | lignes 532, 540, 546 et 2261 exécutées par leurs tests | `essais/trace-cible.log`, `essais/lignes-executees-cible.json` |

Témoin des mutants : la suite complète passe sur la copie non mutée ; chaque sélection `-k` passe donc sans mutation.
Une machine partagée (charge moyenne de 4 par moments) : jamais plus de deux processus lourds à la fois.

## Constats (le plus grave d'abord)

Aucun bloquant, aucun majeur. Les cinq mineurs sont des phrases normatives du texte final que le code n'applique pas à la
lettre. Aucun ne permet une promotion, un changement d'issue ou l'omission d'une réserve due. Chacun est reproduit.

### VF1-01 — mineur — précision 17 : le code ajoute des « non lu » même quand tous les contrôles sont faits

- **Où** : texte, précision 17 (l. 396-397) : « seuls les contrôles non faits deviennent « non lus » ». Code :
  `_executer_entree`, l. 1766-1769 : après une `GardeArret` hors d'un calcul, **chaque** cible de `VISEES[analyse]` reçoit
  un contrôle « non lu » (« entrée entière »), que ses contrôles aient été faits ou non. Le test
  `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` (l. 1794-1795) fige ce comportement.
- **Problème** : quand l'échec survient après tous les contrôles, aucun contrôle n'est « non fait ». Le code ajoute
  pourtant `reserve_<analyse>_non_lue` sur chaque cible établie. La recommandation au verdict dit alors « non contrôlée par
  l'addendum » pour une conclusion contrôlée. Sens prudent (une réserve en plus, jamais en moins), mais phrase fausse
  transmise au verdict R13.
- **Reproduit** (`essais/vf/test_vf_texte.py`, deux essais) :
  - A1, échec simulé dans la permutation du placebo, après les sept contrôles : cinq contrôles ajoutés « A1 (entrée
    entière) », `reserve_A1_non_lue` sur P3-P3, P3-P4, T3, T1, T4 ; recommandation : « P3-P3/tromperie-lineaire-c7 : non
    contrôlée par l'addendum (réserves : reserve_A1_non_lue) ; la conclusion reste établie ; le verdict cite qu'elle n'a
    pas été contrôlée », à côté de la ligne « non robuste » ;
  - A8, valeur non finie ajoutée au descriptif après le contrôle « début de l'action » (fait, favorable) : un
    `reserve_A8_non_lue` ajouté sur P3-P3 (chemin que la précision 17 et les notes nomment).
- **Correction** (texte, recommandée ; le module ne change pas) : réécrire la précision 17 : « Une entrée qui tombe en
  échec garde les contrôles déjà faits, réserves contraires comprises ; l'addendum n'efface jamais une réserve qu'il a
  calculée. Chaque cible visée par l'analyse reçoit en plus un contrôle « non lu » (entrée entière), même si ses contrôles
  ont tous été faits. » Autre voie : changer le code pour n'ajouter que les contrôles réellement manquants ; elle change
  l'empreinte du module et rouvre la vérification.

### VF1-02 — mineur — garde 15 (graines) contrôlée après la création du manifeste

- **Où** : texte, plan point 3 (l. 236-237) et liste d'arrêt (l. 303) : « Gardes 1 à 10 et 12 à 16 … avant la création du
  manifeste ». Code : `executer` crée le manifeste l. 2224 ; `exiger_graines` (garde 15, l. 1912-1926) n'est appelée que
  dans `preparer_donnees` (l. 1984), via `analyser_addendum` (l. 2235), donc après.
- **Problème** : écart d'ordre. Un arrêt à cette garde serait écrit dans la sortie et consommerait le seul passage
  (garde 9). Sans effet sur un run réel : `creer_manifeste` dérive les graines par `manifeste.graines(cles, entropie)`,
  la même fonction que la garde ; elle ne peut pas se déclencher.
- **Reproduit** (`test_garde_15_graines_controlees_apres_la_creation_du_manifeste`, remplaçants pour tout ce qui précède,
  `exiger_graines` réelle) : ordre relevé `… garde 9, creer_manifeste, garde 15 (graines), sortie écrite` ; arrêt écrit
  « garde 15 : graines de l'addendum autres que celles de leurs clés (R9) ».
- **Correction** (texte) : ajouter à la garde 15 : « les graines contrôlées sont celles du manifeste : ce contrôle se fait
  juste après sa création, au début de la fonction pure ; un arrêt y est écrit (précision 1) » ; et au plan, point 3 :
  « gardes 1 à 10 et 12 à 16, sauf les graines de la garde 15 ».

### VF1-03 — mineur — précision 8 non appliquée au cas « aucune » de l'audit de symétrie

- **Où** : texte, précision 8 (l. 375) : « sans aucune réserve possible, le déclencheur est faux ». Code : `synthese`,
  l. 1833-1834 : `toutes` exige `bool(possibles)`, `aucune` ne l'exige pas.
- **Problème** : zéro réserve possible, trois conclusions établies, audit R4 déclenché : le déclencheur vaut vrai, motif
  « aucune réserve déclenchée… », lecture « addendum suspect de propreté ». Inatteignable sur un run réel : chaque cible
  établie est visée par une analyse qui écrit toujours un contrôle (A1 pour P3-P3, P3-P4, T1, T3, T4 ; A2 pour T2 ; A6
  pour P3-P1), ou un « non lu » d'entrée entière.
- **Reproduit** (`test_precision_8_aucune_reserve_possible_et_declencheur_vrai`) : `reserves_possibles 0`,
  `conclusions_etablies 3`, `declencheur True`.
- **Correction** (texte, sans code) : « 8. Audit de symétrie : sans aucune réserve possible, « toutes » est faux ; le cas
  « aucune » ne peut pas se présenter sans réserve possible, chaque conclusion établie étant visée par au moins une
  analyse. » (Ou, dans le code, `aucune = bool(possibles) and …` ; cela change l'empreinte.)

### VF1-04 — mineur — garde 12 : « par les fonctions gelées » ; le code recalcule par sa propre aire vectorisée

- **Où** : texte, garde 12 (l. 330-332) : « recalculés sur le run source par les fonctions gelées ». Code :
  `exiger_coherence`, l. 658 : `aires_par_rangs` (fonction du module) et `np.quantile`.
- **Problème** : écart de lettre. Numériquement sans conséquence : la version vectorisée égale `aire_sous_courbe` à 1e-12
  près (test ; CB1 : écart maximal 2,2e-16 sur 2 947 cas), et les règles communes la permettent.
- **Reproduit** : lecture du code (l. 658), aucun appel de `aire_sous_courbe` ni de `detection` dans `exiger_coherence`
  (l. 644-669).
- **Correction** (texte) : « recalculés sur le run source par l'aire vectorisée du module (égale à `aire_sous_courbe` à
  1e-12 près, test) et le quantile 0,95 de `np.quantile` ».

### VF1-05 — mineur — plan point 9 : chiffres sans chemin ni empreinte versés, mesurés sur l'ancien module

- **Où** : texte, plan point 9 (l. 270-273) : « 426,5 s, dont A1 327,5 s et A4 63,2 s ; … environ 650 Mo, dont 560 Mo …
  (revue de pannes du module, journal `essai_07.log`) ».
- **Problème** : les chiffres sont justes (égaux à `revue-b3-3/essai_07.log` : 426,5 s, A1 327,5 s, A4 63,2 s, 647 Mo ;
  `essai_07b_import.log` : 564 Mo). Mais le journal n'a ni chemin ni empreinte dans le texte (R6), et
  `verser_addendum_v1.sh` ne le verse pas. La correction CB3-03 demandait « le chemin et l'empreinte du journal ». Le banc a
  été fait sur le module du brouillon 3 (`daf95459…`), pas sur le module final ; le texte ne le dit pas.
- **Reproduit** : `grep` du texte (aucun chemin ni empreinte pour `essai_07.log`) ; liste des fichiers copiés par
  `verser_addendum_v1.sh` (aucun journal de `revue-b3-3/`).
- **Correction** (texte et versement) : écrire « banc de la contre-lecture CB3 sur le module `daf95459…` (rapport
  `prereg/contre-lectures/contre-lecture-code-b3-3-addendum-P3-v1.md`, sha256 `8aa42a89…` ; journaux `essai_07.log`
  sha256 `063661ac4a75e4f00caf0ee404189e6ffc54f1c7395d6a775647870854939fb7` et `essai_07b_import.log` sha256
  `baaf517eb27fc9eb4d5865cae962daa21e99d1cd7d1252079b874076eeb475c7`) », et verser ces deux journaux.

### VF1-06 — information — liste des tests : « gardes 1 à 16 », mais l'énumération s'arrête à la garde 11

- **Où** : texte, l. 350-354 : « gardes 1 à 16 ci-dessus (entropie ; … ; moitié des entrées en échec) ».
- **Correction** : ajouter « cohérence de la lecture (12) ; localisation (13) ; mesures relues et découpe des textes
  (14) ; arrêts de forme (15) ; manifeste illisible (16) ». Les tests existent (garde 12, l. 1149 ; 13, l. 1161 ; 14,
  l. 1010-1011 et 1035 ; 15, l. 609, 877, 3158-3161, 3166 ; 16, l. 3088).

### VF1-07 — information — garde 15 : forme du nom et chemin du préenregistrement

- **Où** : texte, garde 15 (l. 338) : « nom du run d'addendum hors de la forme `AAAAMMJJ-HHMMSS-nom` ». Code, l. 75 et
  2006-2009 : `^[0-9]{8}-[0-9]{6}-addendum-p3$` (plus strict : le plan, point 2, écrit bien `…-addendum-p3`) ; et le chemin
  du préenregistrement passé à la commande est contrôlé sous le nom « garde 15 », que la garde 15 ne nomme pas. Le test
  l. 3158 refuse `20261020-130000-autre`, que la lettre de la garde 15 accepterait.
- **Correction** (texte) : « nom du run d'addendum hors de la forme `AAAAMMJJ-HHMMSS-addendum-p3` ; préenregistrement passé
  à la commande autre que celui-ci ».

### VF1-08 — information — section « Contre-lecture » et titre

- « tous acceptés dans ce brouillon 3 » (l. 429) et « tous acceptés dans ce brouillon 3 » (l. 431) : à écrire « dans le
  brouillon 3 ».
- La relecture externe du brouillon 6 par Gemini (requête 006, GB6-01 à GB6-05 : quatre acceptés, GB6-02 refusé) n'est
  pas citée ; le traitement l'a (dernière section). L'ajouter à l'entrée « Relecture externe par Gemini ».
- Titre « v1, brouillon 6 » (l. 1) : à remplacer par le titre final avant le scellement.

### VF1-09 — information — traçabilité de l'état du texte relu par le correcteur

- Les notes citent le texte final `77bc2fe0d62aac4384712ee77c28fa6b77a30d47092b3d327120186d60d24e5c` (« état final ») et
  l'état précédent `503daf12…`. Le texte qui m'est donné est `411eb334…` (modifié à 04:28). Aucun fichier `77bc2fe0…`
  n'est conservé ; je ne peux pas dire ce qui a changé entre les deux. Ma vérification porte sur `411eb334…`.
- **Correction** : la session écrit, dans le traitement, ce qui a changé de `77bc2fe0…` à l'état scellé (sans doute les
  seules entrées « Contre-lecture 3 » et « 4 »).

### VF1-10 — information — précision 15 appliquée aux seuls intervalles calculés par le module

- La part des tirages où l'écart est négatif ou nul est rapportée pour A1, A2 (b), A3, A4 (a), A4 (b) (l. 357, 1109,
  1219). Elle ne l'est pas pour les intervalles des fonctions gelées (A2 (a), A2 (c), A4 (c), A5, A6, A7 (ii)), qui ne rendent
  pas leurs tirages. **Correction** (texte) : « pour les intervalles que calcule le module ».

### VF1-11 — information — précision 1 : une fenêtre entre la création du manifeste et l'écriture de l'arrêt

- `executer`, l. 2228-2233 : `reference` (dont `verifier(chemin_l)`) est construit après `creer_manifeste` (l. 2224) et
  hors du `try` (l. 2234). Une garde levée là laisserait un manifeste sans sortie. Pratiquement inatteignable : le même
  fichier vient d'être vérifié l. 2216.
- **Reproduit** (`essais/vf/test_vf_texte_2.py`) : `verifier` simulé en échec : ordre `creer_manifeste,
  verifier(chemin_l)`, aucune sortie écrite.
- **Correction** : aucune avant le scellement (changer le code changerait l'empreinte) ; à noter au traitement.

### VF1-12 — information — règles du code non écrites, sans portée

- Garde 14 : lignes exactement vides du fichier des textes ignorées (l. 2177-2178) ; une ligne illisible porte le message
  « garde 4 » (l. 2182) alors que le texte la range sous la garde 14. Garde 16 : « hors de forme » = pas un objet, ou
  `config` ou `preenregistrement` qui n'est pas un objet (l. 2075-2077). Précision 13 : le motif de `_nettoyer` est recopié
  (`_NETTOYAGE`, l. 146) pour ramener les positions au texte brut ; une garde exige l'égalité au texte nettoyé (l. 804).
  Docstring du module : « (brouillon 4) » (l. 3). Rien à changer avant le scellement.

## (1) Corrections des constats CB1, CB3, CB2 et GB6

| constat | correction attendue | où dans le module final | état | preuve |
|---|---|---|---|---|
| CB1-01 / CB3-01 (majeurs) | découpe sur le seul saut de ligne ; ligne illisible : arrêt avec numéro, sans texte | `charger_textes` l. 2164-2183 | **faite, juste** | tests l. 1035 et `test_garde_4_textes_de_bout_en_bout` (suite) ; message sans texte (lecture) |
| CB1-02 (majeur) | deux listes ; « non robuste » / « non contrôlée » ; lectures gelées de A7 | `synthese` l. 1849-1862 ; constantes l. 114-120 | **faite, juste** (VF1-01 à part) | essais CB2 « recommandation » : échouent désormais |
| CB1-03 | « toutes » sur les seuls contrôles contraires ; « non lu » compté à côté | l. 1831-1833, 1836 | **faite, juste** (VF1-03 à part) | lecture ; texte des critères l. 290-295 |
| CB1-04 | arrêts ajoutés écrits au texte | gardes 12 à 16, précision 2 | **faite** ; écarts résiduels VF1-02, VF1-04, VF1-07 | table (2) |
| CB1-05 | silences écrits | précisions 1 à 15 | **faite** ; VF1-03 (précision 8), VF1-10 | table (2) |
| CB1-06 | chaque garde éprouvée (R5) | `GARDES_R5`, tests nommés | **faite** (relevé complet par l'angle « pannes » ; deux gardes neuves relevées ici : l. 532, 2261 exécutées) | `essais/trace-cible.log` |
| CB1-07 / CB3-06 | aucun cache | `final-b4/` | **faite** | `find` : rien |
| CB3-02 | garde 10 et localisation avant le manifeste | `executer` l. 2219-2221 | **faite, juste** | ordre relevé (essai VF1-02) : `familles_attention`, `localisation` ×2 avant `creer_manifeste` |
| CB3-03 | mémoire et durée mesurées, chemin et empreinte | texte, plan 9 | **chiffres justes ; chemin et empreinte manquants** | VF1-05 |
| CB3-04 | graines clé par clé | `exiger_graines` l. 1923-1926 | **faite, juste** (placement : VF1-02) | test l. 877 (suite) ; essai VF1-02 |
| CB3-05 | dépôt non superficiel | garde 3 l. 2144-2145 | inchangé, juste (lancement : session) | lecture |
| CB2-06 (verrou de fin non recalculé) | recalcul et comparaison | `exiger_verrou` l. 1877-1893 | **faite, juste** | essai CB2 « verrou mutable » : arrêté (« verrou unidirectionnel … ≠ conclusions recalculées ») ; V1-V3 tués |
| CB2-11 (drapeaux bruts non recoupés) | recoupement là où la table consulte | `exiger_drapeaux_recoupes` l. 522-547, `_contraste_selon_les_etats` l. 505-519 | **faite, juste** : mêmes règles que `lecture.lire` (`conforme`, T3 par les états ; T1 et T4 `bas > plancher_quantile` ; T2 `bas > 0` ; P3-P1 `calculable et bas > 0`, `lecture.py` l. 242) | essai CB2 « drapeaux bruts » : arrêt garde 7 |
| CB2-09 (réserve effacée par un échec) | réserve calculée jamais effacée | `_executer_entree` l. 1755-1770 | **faite** (la réserve reste) ; **mais** « non lu » ajouté à tort : VF1-01 | essai CB2 « efface » : échoue désormais ; essai VF1-01 |
| CB2-01 à CB2-05 (mutants survivants) | un test tue chaque mutant | tests nommés | **faite** : 51 sur 51 tués | table des mutants |
| CB2, recommandation (non lue, forme du coût) | lecture gelée à la lettre | l. 1855-1862 | **faite, juste** | essais CB2 : échouent désormais |
| GB6-01 | critère lexical du manifeste illisible | `_pourrait_concerner` l. 2048-2054, `_manifestes` l. 2057-2085, l. 102-103 | **faite, juste** (zéro octet si illisible par le système ; écartés comptés et rapportés l. 2232-2233, 2278) | lecture ; test l. 3088 (suite) |
| GB6-03 | garde 13 à 1e-9 ; fenêtre `[c − L, c)` | l. 99, 706-719 ; l. 1076 | **faite, juste** | lecture ; test l. 1161 (suite) |
| GB6-04 | verrou de fin sur la liste recalculée | l. 1877-1896 | **faite, juste** | essai CB2 « verrou mutable » |
| GB6-05 | règle de sensibilité nommée, filtre pour `T2_propre` | l. 1388, 1399-1406 | **faite, juste** | lecture |

Les huit essais de CB2, relancés **sans modification** sur le module final : `test_verrou_conclusions_relatives_aux_drapeaux_bruts_de_la_lecture`,
`test_recommandation_dit_non_robuste_pour_une_reserve_non_lue`, `test_recommandation_forme_du_cout_sans_sa_lecture_gelee`,
`test_entree_en_echec_efface_une_reserve_contraire_deja_calculee` et `test_analyse_qui_allonge_les_conclusions_etablies_n_est_pas_arretee`
échouent (chaque défaut prouvé ne se reproduit plus) ; `test_verrou_aucune_sortie_hors_descriptif_sur_cible_non_etablie_tous_scenarios`
et `test_A8_saturation_…` passent (propriétés tenues) ; `test_empreintes_…` échoue (autre module, attendu).

## (2) Phrases normatives changées depuis le brouillon 3, face au code

| texte final | code | état |
|---|---|---|
| Plan 3 : gardes 1 à 10 et 12 à 16 avant le manifeste, avec le recalcul de l'issue | `executer` l. 2209-2222 (commande, gardes 1, 2, 3, 4, textes, 5-8 avec 6, 12, 10, 13, 9), manifeste l. 2224 | conforme, **sauf graines de la garde 15 : VF1-02** |
| Plan 3 : seule la garde 11 après les analyses | `synthese` l. 1815-1822 | conforme |
| Plan 6 : recommandation, deux listes, lectures gelées de A7, « non contrôlée » | l. 1849-1862 | conforme (VF1-01 en amont) |
| Plan 9 : durée et mémoire | hors code ; `essai_07.log` | chiffres égaux au journal ; **VF1-05** |
| Critères : audit de symétrie (« toutes » par contrôle contraire ; « aucune » quel que soit le nombre de « non lu ») | l. 1827-1848 | conforme |
| Liste d'arrêt, en-tête : gardes 1 à 10 et 12 à 16 avant le manifeste | comme le plan 3 | VF1-02 |
| Garde 11 : une réserve générale par cible établie ; entrée en échec si un de ses calculs l'est | l. 960-963, 996, 1239, 1815-1822 | conforme (non calculable ≠ échec) |
| Garde 12 : aires et quantiles des jeux, à 1e-9, par les fonctions gelées | l. 644-669, 98 ; avant le manifeste l. 2218 | conforme sauf « fonctions gelées » : **VF1-04** |
| Garde 13 : pré-coût et coût égaux à `lecture._localisation` à 1e-9 | l. 678-719, 99 ; avant le manifeste l. 2220-2221 | conforme (lignes exigées égales en plus) |
| Garde 14 : mesures relues = tables ; découpe sur le seul saut de ligne ; ligne illisible : arrêt, numéro, sans texte | l. 427-433 ; l. 2164-2183 | conforme ; message « garde 4 », lignes vides ignorées : VF1-12 |
| Garde 15 : nom du run ; chemin du module ; paramètres de tirage par la ligne de commande ; graines clé par clé | l. 2006-2007 ; 2023-2025 ; 2250-2262 et 2273 ; 1912-1926 | conforme sur le fond ; **VF1-02** (moment), VF1-07 (nom plus strict, chemin du préenregistrement) |
| Garde 16 : critère lexical, 64 octets, hors de forme = illisible, zéro octet si illisible, compté et rapporté | l. 2048-2085, 102-103, 2232-2233, 2278 | conforme |
| Tests : « gardes 1 à 16 » | tests présents pour 12 à 16 | énumération incomplète : VF1-06 |
| P1 arrêt après le manifeste écrit (`arret`), puis propagé | l. 2234-2241 | conforme ; fenêtre l. 2228-2233 : VF1-11 |
| P2 garde 9 par la commande | l. 2194-2195 | conforme |
| P3 A4 (b) : effectif minimal général en plus | l. 1298-1299 → l. 314 | conforme |
| P4 A7 (iii) corrélation non définie → « non lu » | l. 1578-1582 (`correlation_rangs` rend None sous 3 paires ou série constante) | conforme |
| P5 A7 (i) un contrôle par jeu « au-dessus » et par prédicteur ; sinon « marge non contrôlée » | l. 1530-1542 | conforme |
| P6 A8 action de trois jetons au plus : « dans les trois premiers » ; nombre rapporté | l. 1620-1622, 1666 | conforme |
| P7 A2 (c) fenêtre `[c − L, c)` contre le champ entier | l. 1076, 1141 | conforme |
| P8 sans réserve possible, déclencheur faux | l. 1833-1834 | **VF1-03** |
| P9 A5 règle (2) sans la condition de la ligne ACTION ; sans ACTION = invalide ; sensibilité descriptive ; filtre pour `T2_propre` | l. 809-829, 1383-1388, 1399-1406 | conforme |
| P10 garde 2 : empreinte de P3 par `verifier` | l. 2109 | conforme |
| P11 garde 1 : `exiger_code_cite` sur le commit cité ; P3 par `exiger_lecture_sous_prereg` | l. 2038 ; 2108 | conforme |
| P12 clés de graines, `default_rng(graine_entiere(…))`, `generateur` pour les coûts | l. 1899-1909, 252-253, 1464 | conforme |
| P13 fonctions privées importées | l. 1039, 705, 775, 781, 804, 814-815, 825 | conforme (copie gardée du motif : VF1-12) |
| P14 A6 : P3-P2 ou mention non calculable → « non lu » | l. 1484-1485 | conforme |
| P15 part des tirages ≤ 0 en descriptif | l. 357, 1109, 1219 | VF1-10 |
| P16 verrou de fin recalculé, cibles des contrôles lus et des réserves, clés interdites | l. 1868-1896 ; appel l. 1974 | conforme |
| P17 échec après un contrôle contraire : réserve gardée ; seuls les non faits « non lus » | l. 1755-1770 | réserve gardée ; **VF1-01** |
| P18 garde 7 : drapeaux consultés recoupés ; non consultés non lus | l. 522-547, 501 | conforme (règles égales à `lecture.lire` l. 242, 308, 323, 336, 341, 355) |

**Règles absentes** : aucune règle du texte final n'est sans code. **Règles ajoutées** (code sans texte) : VF1-07 (chemin du
préenregistrement, nom plus strict), VF1-12 (lignes vides, définition de « hors de forme »). Le contrôle « run source
décisif en mode réel » de `exiger_run_source_decisif` double celui de `lecture.exiger_lecture_sous_prereg` : sans portée.

## (3) Lignes d'empreintes du module et des tests

- Expressions lues (l. 76-77) : ``Module de l'addendum \(sha256\) : `([0-9a-f]{64})` `` et ``Tests du module \(sha256\) :
  `([0-9a-f]{64})` ``. Les lignes 13 et 14 du texte final sont en espaces et apostrophe ASCII (contrôle octet par octet) :
  elles correspondent. La première occurrence est celle de l'en-tête ; l'entrée « Contre-lecture 4 » (« module final
  (sha256 … ) ») ne correspond pas à l'expression.
- Comparaison (l. 2027-2037) : empreinte du fichier exécuté (`Path(__file__)`, après contrôle du chemin l. 2023-2025) et
  du fichier des tests à son chemin versé.
- Essai sur une copie du texte final aux marqueurs remplis (empreintes réelles, 165 tests, traitement ; valeurs factices
  pour la contre-lecture 4 ; seul changement voulu : le commit cité est celui du dépôt jouet). `prereg.problemes` : aucun
  problème. Cas sain : la vraie `exiger_garde_1` passe et rend `2b16179d4451…` et `7605c2051e85…`. Artefacts, tous arrêtés
  avec le bon motif : module modifié ; tests modifiés ; tests absents ; empreintes échangées dans le texte ; empreinte
  hors de forme (majuscules) ; marqueurs laissés (refus de `sceller_prereg`, puis refus de la garde 1 sur un texte scellé
  de force : « marqueurs de gabarit restants », « contre-lecture 4 sans ses deux empreintes ») ; module exécuté hors de son
  chemin (« garde 15 »). Retour au sain : passe. **10 sur 10.**

## (4) Suite complète

Commande, depuis `/home/user/controle-ia-travail`, sur `verification-finale/texte/copie-suite/` (copie octet pour octet) :
`PYTHONPATH=src …/venv-gpu-neuf/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=…/basetemp-suite
…/copie-suite/test_complements_p3_v1.py`. Résultat : **165 passed in 1009.45s (0:16:49)**, égal au nombre écrit en tête
des tests et à celui des notes.

## Table des mutants (51, liste de CB2 inchangée, module final)

Lanceur `outils/mutants_vf.py` : copie de `final-b4/essais/mutants_b4.py`, chemins seuls changés vers mon dossier ; V1,
V2, V3 aux motifs adaptés au verrou réécrit (même règle mutée), les 48 autres tels quels ; 51 motifs uniques vérifiés.
Colonne « CB2 » : résultat de la revue d'origine sur le module de départ (`revue-b3-2/mutants-resultats.jsonl` : 20
lancés, 5 tués, 15 survivants).

| id | famille | règle mutée | CB2 | statut (module final) | test qui le tue |
|---|---|---|---|---|---|
| V1 | verrou ouvert | exiger_verrou n'arrête plus un contrôle lu sur une cible non établie | survit | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` |
| V2 | verrou ouvert | exiger_verrou appelé avec toutes les cibles possibles | survit | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` |
| V3 | verrou ouvert | exiger_verrou accepte une réserve sur une conclusion non établie | survit | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` |
| V4 | verrou ouvert | P3-P4 établie sans la ligne « critères 2 et 3 » | tué | tué | `test_conclusions_etablies_table_fermee` |
| V5 | verrou ouvert | clé interdite `au_dessus_du_plancher` retirée | tué | tué | `test_garde_du_verrou_sain_et_artefacts` |
| V6 | verrou ouvert | issue recopiée non comparée | tué | tué | `test_issue_primaire_inchangee_et_garde_de_la_copie` |
| V7 | verrou ouvert | instantané de la lecture non comparé | tué | tué | `test_issue_modifiee_pendant_l_addendum_arrete` |
| C1 | cible fausse | A1 : témoin contre honnête vise T3 | survit | tué | `test_A1_sain` |
| C2 | cible fausse | A1 : saboteur contre témoin vise P3-P3 | survit | tué | `test_A1_sain` |
| C3 | cible fausse | A1 : saboteur contre mention vise P3-P3 | survit | tué | `test_A1_sain` |
| C4 | cible fausse | A7 : saboteur contre témoin vise P3-P3 | survit | tué | `test_A7_sain` |
| C5 | cible fausse | A7 : saboteur contre mention vise P3-P3 | survit | tué | `test_A7_sain` |
| C6 | cible fausse | entrée A4 en échec : T1 plus « non lu » | non lancé | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` |
| C7 | cible fausse | entrée A3 en échec : T3 plus « non lu » | non lancé | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` |
| C8 | cible fausse | entrée A7 en échec : P3-P4 et T3 plus « non lus » | non lancé | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` |
| N1 | niveau changé | A2 (a) à 80 % | non lancé | tué | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` |
| N2 | niveau changé | `T2_propre` à 80 % | non lancé | tué | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` |
| N3 | niveau changé | A2 (b) à 80 % | non lancé | tué | `test_A2_sain` |
| N4 | niveau changé | A4 (a) à 80 % | non lancé | tué | `test_A4_sain` |
| N5 | niveau changé | A4 (b) à 80 % | non lancé | tué | `test_A4_sain` |
| N6 | niveau changé | A4 (c) à 80 % | non lancé | tué | `test_A4_sain` |
| N7 | niveau changé | A6 à 80 % | non lancé | tué | `test_A6_sain` |
| N8 | niveau changé | A1 : T1 à 97,5 % | non lancé | tué | `test_A1_sain` |
| N9 | niveau changé | A7 (ii) à 95 % fixe | non lancé | tué | `test_A7_artefact_forme_du_cout` |
| J1 | moyenne sur les jetons | A2 (c) par la moyenne des jetons | survit | tué | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` |
| J2 | agrégation changée | A2 (b), sonde à attention notée au maximum | survit | tué | `test_A2_fenetres_d_une_sonde_a_attention_par_ses_logits` |
| R1 | réserve mal câblée | A8 saturation : les deux conditions exigées | non lancé | tué | `test_A8_regles_de_reserve_par_condition` |
| R2 | réserve mal câblée | A8 début : une seule condition suffit | non lancé | tué | `test_A8_regles_de_reserve_par_condition` |
| R3 | réserve mal câblée | A4 (a) : « et » au lieu de « ou » | non lancé | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` |
| R4 | réserve mal câblée | A4 (a) : condition du quantile observé retirée | non lancé | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` |
| R5 | réserve mal câblée | A6 : réserve même si la borne était déjà > 0 | non lancé | tué | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` |
| L1 | réserve non lue omise | A1 : calcul en échec lu favorable | non lancé | tué | `test_A1_calculs_en_echec_non_lus` |
| L2 | réserve non lue omise | A3 : contrastes en échec lus favorables | non lancé | tué | `test_toute_exception_autre_que_garde_arrete` |
| L3 | réserve non lue omise | A4 (a) : échec lu favorable | non lancé | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` |
| L4 | réserve non lue omise | A4 (b) : échec lu favorable | non lancé | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` |
| L5 | réserve non lue omise | A6 P3-P1 non calculable lu favorable | non lancé | tué | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` |
| L6 | réserve non lue omise | A7 (i) séparation non calculable lue favorable | non lancé | tué | `test_A7_formes_marge_et_correlations` |
| L7 | réserve non lue omise | A7 (ii) échec lu favorable | non lancé | tué | `test_A7_formes_marge_et_correlations` |
| L8 | réserve non lue omise | A8 début non lu écrit favorable | non lancé | tué | `test_A8_regles_de_reserve_par_condition` |
| L9 | réserve non lue omise | A8 saturation omise si échec | non lancé | tué | `test_A8_regles_de_reserve_par_condition` |
| L10 | réserve non lue omise | A8 poids maximal non défini lu favorable | non lancé | tué | `test_A8_regles_de_reserve_par_condition` |
| G1 | garde affaiblie | garde 7 : valeur non numérique acceptée | non lancé | tué | `test_garde_jamais_eprouvee_cas_sain_et_artefact[garde 7 : valeur de jeu non numérique]` |
| G2 | garde affaiblie | 5 % de tirages dégénérés au lieu de 1 % | non lancé | tué | `test_degenerescences_au_dela_de_1_pourcent` |
| G3 | garde affaiblie | A7 (ii) : 50 actions au lieu de 10 | non lancé | tué | `test_A7_formes_marge_et_correlations` |
| G4 | garde affaiblie | A4 (b) : une paire suffit | non lancé | tué | `test_A4_degenere` |
| G5 | seuil changé | A7 (iii) : 0,90 au lieu de 0,50 | survit | tué | `test_A7_formes_marge_et_correlations` |
| G6 | seuil changé | A8 : poids maximal 0,99 | survit | tué | `test_A8_regles_de_reserve_par_condition` |
| G7 | seuil changé | A8 : trois premiers 0,80 | survit | tué | `test_A8_regles_de_reserve_par_condition` |
| G8 | seuil changé | A8 : deux premiers jetons | survit | tué | `test_A8_regle_stricte_des_trois_premiers_jetons_et_segments` |
| G9 | seuil changé | A2 (b) : 10 répliques | tué | tué (par une `IndexError` du test, réplique 17 absente ; la garde 15 des paramètres le tuerait aussi) | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` |
| G10 | seuil changé | A2 (a) et A5 : seuil 0,45 | survit | tué | `test_A2a_et_A5_seuil_de_l_aire_du_cout` |

Tués : **51 sur 51** ; les 15 survivants de CB2 sont tous tués. Chaque premier échec est le test attendu ; les échecs sont
des assertions ou des arrêts du module (`GardeArret` du verrou pour V2), jamais une erreur d'import. Je n'ai pas construit
de mutants neufs (angle d'une autre vérification).

## Fichiers (tous sous `verification-finale/texte/`, sauf ce rapport)

- `copie-suite/` (copie de la suite) ; `suite-complete.log` ; `basetemp-*` (dossiers temporaires de pytest).
- `copie-texte/`, `jouet/`, `outils/essai_empreintes_citees.py` (`60a32810…e44a`), `essai-empreintes-citees.log`.
- `essais/base/` (copie du module et des tests), `essais/cb2/` (essais de CB2 inchangés et leur journal), `essais/vf/`
  (`test_vf_texte.py` `1d949cd6…653e`, `test_vf_texte_2.py` `090b505c…bb7a`, journaux), `essais/trace-cible.log`.
- `mutants/` (base, journaux par mutant, `resultats.jsonl`, `run.log`, `table-rapport.md`) ; `outils/mutants_vf.py`
  (`440b1387…bcd`), `outils/mutants_b3_2.py` (copie de la liste de CB2, `b5b7a3fa…58bb`), `outils/trace_vf.py`.
