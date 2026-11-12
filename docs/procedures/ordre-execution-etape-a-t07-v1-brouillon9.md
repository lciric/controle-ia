# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 9

> **VARIANTE B** (décision de la mère, R-2112) : l'étape A ne se joue pas sur l'instance de 7b. Une instance **A100 neuve**,
> créée par la fille après la course de 7b et la poussée de ses résultats, clone le code de T0.7, récupère la sortie de 7b par
> refspec explicite, joue les essais figés **avant** la descente du modèle, borne la taille des sorties, **recalcule les
> activations** (repli, garde d'équivalence), puis joue la passe à blanc et l'étape A, pousse ses sorties sur une branche neuve
> (fichiers lourds en morceaux scellés) et demande l'état « stopped » ; la fille la détruit par son identifiant. **Ligne de GO :
> GO-2026-11-10-06** (mot de Lazar, R-2115), non cumulée avec GO-2026-11-10-04 : **20 USD au total sous les deux lignes**.
> Script de l'instance : **`scripts/etape_a_t07_variante_b_v4.sh`** (brouillon 8 ; v3 aux brouillons 6 et 7), neuf arguments (**brouillon 6** : un script v3 est
> **exigé** — le v2, `e68d3306…`, appelle `lecture_v2`, qui refuse la configuration v7 ; empreinte du v3 au marqueur de la
> ligne (A) ; § 0 ter, § 13, S-12). **Brouillon 6 (remède (a'), R-2285, R-2298, R-2304)** : commandes `lecture_v4`,
> configuration v7 (800 directions, règle (a)), plancher neuf des sondes figées de P3 réextrait au début de l'étape A,
> devis relevé (+ 0,23 h attendu, + 0,66 h au pire), `ANT0` ≤ 3,6 USD.
> **Brouillon 7 (R-2305, R-2306, R-2309)** : script v3 **écrit** (`a19c594d…`, commit `7e23a554` de `prep/t07-plancher-v3-v1`),
> répété en jouet (17 verdicts sur 17) ; configuration v8 (palier « carte » à 10⁻³ et 10⁻²) ; contrôle avant l'ouverture à la
> passe à blanc ; `SRC7` = commit de `main` qui fusionne la branche finale du code ; `ATT` mesurée à C7 (marqueur).
> **Brouillon 8 (R-2311 à R-2313)** : script **v4** (`4b17d1f0…`, commit `a621dcd3`), qui joue `lecture_v4
> controle-avant-ouverture` à l'étape 8, avant toute ouverture ; répétition jouet v4 (10 verdicts sur 10) ; arrêt technique
> d'un bras de la réextraction (CLC-P3-04) ; nombre de lignes des mesures de 7b lu avant la création (P14 : un entier, aucune colonne lue) ; couples VC3-C et VC3-D.
> **Brouillon 9 (R-2315)** : couples VF4-A à VF4-E de la vérification finale, tels qu'écrits (P14 : le seul nombre de lignes
> des mesures de 7b, un entier ; aucune colonne lue ; R-2314 (4)) ; `a621dcd3` est le dernier commit contre-lu (P13 (iii), `SRC7`).

- **Statut** : **brouillon 9**, écrit le 2026-11-11 à partir de 05:39 UTC (`date -u`) par le rédacteur des brouillons 6 à 8
  (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout
  rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2315. **Brouillon 9 = brouillon 8**
  (`24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e`, gardé tel quel, R12) **+ les couples VF4-A à VF4-E de la vérification
  finale, tels qu'écrits** (lus dans son § 4 par le script
  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9-appliquer-v1.py` et appliqués d'abord et seuls : ils donnent
  `8413f56e8f14090718149a9bd8078e8dd4e59a2339015ea21408afa92ecd4759`, l'empreinte calculée par le vérificateur, contrôlée par le script avant tout
  autre couple) **+ les couples O9-01 à O9-07** (mentions d'état : `a621dcd3` dernier commit contre-lu, brouillon 8 contre-lu,
  VF4-06) ; **tout le reste est égal à l'octet au brouillon 8** (vérifié par le script : couples défaits → brouillon 8). Ce
  qui change et pourquoi : § 0 sexies. **Contre-lu** : le brouillon 8 et les couples VF4-A à VF4-E, par la vérification finale, `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md` (`26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257`, Claude Fable 5.2, R-2315 : texte et ordre « après corrections », aucun nœud ; code `7e23a554..a621dcd3` « sans défaut bloquant ») ;
  les seules mentions d'état des couples O9 ne sont pas contre-lues ; à sceller avec le candidat 5 de T0.7.
- **Brouillon 8** (statut gardé pour mémoire) : **brouillon 8**, écrit le 2026-11-11 à partir de 04:59 UTC (`date -u`) par le rédacteur des brouillons 6 et 7
  (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout
  rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2313. **Brouillon 8 = brouillon 7**
  (`d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916`, gardé tel quel, R12) **+ les couples O8-01 à O8-25**, dont **VC3-C et VC3-D de la vérification
  courte du candidat 3, tels qu'écrits** (lus dans son § 4 par le script
  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8-appliquer-v1.py`) ; **tout le reste est égal à l'octet au
  brouillon 7** (vérifié par le script : couples défaits → brouillon 7). Ce qui change et pourquoi : § 0 quinquies. **Non
  contre-lu** : à contre-lire (R2) avec le candidat 4 de T0.7 avant son scellement (contre-lu depuis, brouillon 9 : `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md`, `26efc4df…`, R-2315).
- **Brouillon 7** (statut gardé pour mémoire) : **brouillon 7**, écrit le 2026-11-11 à partir de 04:09 UTC (`date -u`) par le rédacteur du brouillon 6 et du
  candidat 2 de T0.7 (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2309
  (mêmes interdits et mêmes chemins que la consigne `d29c7858…`, aux noms près). **Brouillon 7 = brouillon 6**
  (`92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca`, gardé tel quel, R12) **+ les couples O7-01 à O7-24** du script
  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7-appliquer-v1.py`, chacun avec un « ancien » présent une fois ;
  **tout le reste est égal à l'octet au brouillon 6** (vérifié par le script : les couples défaits dans l'ordre inverse
  redonnent le brouillon 6 octet pour octet). Ce qui change et pourquoi : § 0 quater. **Non contre-lu** : à contre-lire (R2)
  avant son scellement, avec le candidat 3 de T0.7.
- **Brouillon 6** (statut gardé pour mémoire) : **brouillon 6**, écrit le 2026-11-11 à partir de 03:00 UTC (`date -u`) par un **rédacteur neuf** (Claude Opus
  5.5, `claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), qui n'a écrit ni T0.7 (brouillons,
  candidat 1), ni son module, ni les brouillons 1 à 5 de cet ordre, ni leurs contre-lectures, ni les notes de l'erreur de
  première espèce ; il écrit aussi le candidat 2 de T0.7 (ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de
  P3-bis). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md` (`d29c78585ee578127304d840851fa7017c6e756324f47caa9c401a84ee553eae`, vérifiée par `sha256sum -c` avant lecture). **Brouillon 6 = brouillon 5**
  (`d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b`, gardé tel quel, R12) **+ les couples O6-01 à O6-37**
  du script `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6-appliquer-v1.py`, chacun avec un « ancien » présent une
  fois ; **tout le reste est égal à l'octet au brouillon 5** (vérifié par le script : les couples défaits dans l'ordre inverse
  redonnent le brouillon 5 octet pour octet). Ce qui change et pourquoi : § 0 ter. **Non contre-lu** : à contre-lire (R2)
  avant son scellement ; le script v3 de l'instance (§ 13, S-12) reste à écrire, répéter en jouet et contre-lire.
- **Brouillon 5** (statut gardé pour mémoire) : **brouillon 5**, écrit le 2026-11-10 à partir de 16:12 UTC (`date -u`) par le
  rédacteur du brouillon 4, qui
  applique la contre-lecture R2 du brouillon 4 (`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`,
  `88ea9f0661e07a7840b10c060f1488a479efa9d01e82bbdbb643b72329c74704`, Fable 5.2) : ses **douze couples tels qu'écrits**
  (`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1-couples.json`,
  `cf2e4c982133e2ad662c7e67bd5eafe80ae783e32ec98e6cda42f524d1643fa5`), par le script
  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5-appliquer-v1.py` (empreinte du texte après les douze seuls :
  `f3256fd603e3d2c330245c9c4850b9a84064603bb9daee4fad46f7d8b9915de5`, vérifiée), puis les retouches **déclarées** D-1 à D-10
  de ce script (R-2258 : en-tête ; `ATT` retrouvée sous Python 3.11.17 ; réserve CLE-12 ; S-8 à S-11 en réserve pour une v3
  du script ; sources). Remplace le brouillon 4 (`d5047be2a1cc371917bc09352f66cd59f6a7d8b5d4f2c43e32d3c98a36f6d72c`, gardé
  tel quel, R12). **Brouillon 4** : écrit le 2026-11-10 à partir de 15:14 UTC (`date -u`) par un sous-agent développeur **neuf**
  de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` (Claude Opus 5.5, `claude-opus-5-5`), qui n'a écrit ni T0.7, ni son
  module, ni le script v2, ni les brouillons 1 à 3 de cet ordre, ni leurs contre-lectures (il a lu T0.7 : exclu ensuite de tout
  rôle de lecteur de P3-bis). Consigne de la mère : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-essai-degeneres-ordre-b4-t07-v1.md`
  (`a3e326e46bf00e6392a52e42204ab20e52dd3a3ecddec8e8b10bf26c79be1696`, vérifiée par `sha256sum`). Remplace le brouillon 3
  (`b053a2207006c49d7aca8d8e5975d7539857474d98591368088cda1fc2a1b484`, gardé tel quel, R12) ; les brouillons 1 et 2 restent tels
  quels. Porte : la contre-lecture courte v3 (`d0fe90538160779ea6386a9f3a622ca0636575631254a76a5bec857915e4e8c6`, O-1 à O-6) ;
  le rapport complémentaire 5 (`e58be6c9051d928e3818175ace1dbfd2db6afd2c6e725d7278032dbe13a90e90`, script v2, point 8) ; la
  contre-lecture courte de l'option (c) (`7a32746203bf9b467898dbf82a04f32428bf9bd886f93902f82b57d9b0c719e6`, CLC-03, CLC-08) ;
  la contre-lecture orchestrée du brouillon 22 de T0.7 (`prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md`,
  `47537dfa7d4f97d0266f72eb3d791996d2ea0aa8f35a098a721c1d72ab251a60` : GARDES-CODE-01, CONCORDANCE-01 et CLO-08) ; le registre
  R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249. **La ligne d'essais attendue (`ATT`) est mesurée** dans un clone fait
  comme celui de l'instance (§ 11 bis). **Contre-lu** (R2, brouillon 4, `88ea9f06…`) : « scellable après corrections », aucun constat bloquant ; douze couples
  appliqués ; `ATT` retrouvée sous Python 3.11.17 (§ 11 bis). Le script v2 n'est pas modifié et **reste celui de l'ordre**
  (R-2255, R-2258) : ce que je propose d'y changer est au
  § 13 (une version v3 est une décision de la mère).
- **Texte qui régit l'étape** : le préenregistrement scellé de T0.7, **désigné par sa ligne `SCELLEMENT-T07`** du registre
  `registres/scellements-v1.md` de `main` (P5 ; jamais par une empreinte écrite dans cet ordre) : « Calcul et dépense » (variante
  B : « instance A100 SXM4 80 Go ≤ 1,30 USD de l'heure […] recalcul des activations (point 8, repli) ») ; « Écrits exigés par
  P3-bis » (b) 2 « Variante B » (même code, même configuration, même règle de `sondes_lues`) ; liste d'arrêt (ligne « instance
  d'étiquette `t06…` ou `t07…` déjà sur le compte », CLO-08, R-2249) ; lignes de registre **`GO-LECTURE-T07`** (extrait scellé de
  la ligne du GO cité pour la variante B) et **`CODE-T07`** (DS-3 bis (a), R-2104 ; fichier `CODE-T07-v2.json` au commit C7,
  R-2231).
- **Autorisation** : **GO-2026-11-10-06** (calcul, Lazar ; R-2115 ; `registres/go.md` de `main`) : extension de
  GO-2026-11-10-04 à la variante B ; **dépense totale sous GO-2026-11-10-04 et sous GO-2026-11-10-06 ≤ 20 USD** (O-4) ; instance
  A100, **la H200 seulement après un mot de Lazar** ; échéance le **2026-11-23** ; périmètre : recalcul des activations depuis la
  sortie poussée de 7b, puis passe à blanc et étape A. La délégation GO-2026-10-20-07 (≤ 10 USD par lancement) ne couvre pas le
  pire cas du devis (§ 6).
- **Exécutante** : la fille porteuse des clés (Vast.ai, GitHub, Hugging Face), session `<<ID_SESSION_FILLE>>` ; journal
  `journal-etape-a-t07-b-v1.md`, une ligne datée par geste (`date -u`).

## 0. Objet

Après la fin normale de 7b et la poussée vérifiée de ses résultats : créer une instance A100 neuve qui joue, sans autre geste de la
fille que la surveillance, le script `scripts/etape_a_t07_variante_b_v2.sh` (§ 5) : minuterie ; clone partiel de la seule
branche `main` au commit de scellement S7 ; **registres nommés** de `main` et fichiers qu'ils citent ; **périmètre des jeux**
contrôlé contre l'argument `PERIMETRE` (C-1) ; sortie de 7b par refspec explicite (fichiers nommés) ; paquets ; **essais figés**
(dernière ligne égale à `ATT`, **avant** le modèle, O-1) ; **taille des sorties bornée** (O-2) ; modèle ; puis, **dans cet ordre** :
**`CODE-T07`** (inscrite par la mère avant la création, contrôlée sur l'instance), **repli** (garde d'ouverture d'abord, puis
recalcul et garde d'équivalence), **passe à blanc**, **étape A** ; poussées sur une branche neuve (légers d'abord, fichiers de plus
de 90 Mo en morceaux scellés) ; état « stopped » demandé. La fille vérifie la poussée et **détruit l'instance par son
identifiant** (R10). Ni épisode, ni étape B, ni lecture d'un résultat.

## 0 bis. Ce qui change depuis le brouillon 3

| Point | Source | Réglé par le script v2 (`e68d3306…`) | Porté par cet ordre | Reste |
|---|---|---|---|---|
| **O-1** ligne d'essais | `d0fe9053…` ; `e58be6c9…` § 8 ; CLC-03 | essais joués à l'étape 6, **avant** la borne de taille et le modèle (étape 8) ; mode de mesure `ARRET_APRES_ESSAIS` (essai local seulement) | `ATT` **mesurée** dans un clone fait comme celui de l'instance, à la branche qui porte l'essai GARDES-CODE-01 (§ 11 bis) ; conditions de validité contrôlées par la fille (P12) ; commande de remesure écrite | essais joués **après** les paquets : un écart coûte le démarrage, le clone, les paquets et les essais, soit ≈ 0,6 h attendue et 1,85 h au pire (§ 6), ≤ 2,4 USD de carte, plus le téléchargement des paquets ; interpréteur : ligne **retrouvée sous Python 3.11.17** par la contre-lecture R2 de cet ordre (`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`, § 3 : même ligne, mêmes deux sauts, mêmes quatre échecs attendus, aucun avertissement ; `torch` 2.14.1 en construction processeur) ; restent la construction carte de `torch` et le git de l'image (§ 13, S-1, S-2) ; `8cb539f9` atteignable depuis `main` (fusion « ours », R-2229) : l'essai du miroir passe à la mesure |
| **O-2** taille des sorties | `d0fe9053…` | étape 7 : borne haute calculée **avant toute ouverture** (§ 5 bis), au-dessus de 2 000 000 000 octets → code 2, rien d'ouvert ; tout fichier de plus de 90 000 000 octets découpé en morceaux de 50 000 000 octets scellés, manifeste scellé, recomposition vérifiée sur l'instance, poussée par lots de 10 | § 5 bis (calcul écrit) ; § 4.6 (vérification des morceaux sans rien rapatrier) ; § 9 (recomposition avant l'étape B) | borne non confrontée à une sortie réelle (répétition jouet seulement) |
| **O-3** minuterie | `d0fe9053…` | chaque `DELETE` journalisé avec son code HTTP ; la minuterie meurt avec le conteneur à l'état « stopped » (dit par le script) | § 4.7 corrigé : après « stopped », **seule la fille détruit** ; rappel daté à `ECH` (fille et mère) | `DELETE` réel avec la clé de l'instance non répété (API locale seulement) |
| **O-4** dépense antérieure | `d0fe9053…` | — | `ANT0` = dépense inscrite sous **GO-2026-11-10-04 et GO-2026-11-10-06** ; P8 de même ; échéance de la minuterie bornée par `20 − ANT0` (§ 4.4) | — |
| **O-5** registres | `d0fe9053…` ; `e58be6c9…` § 3 | registres **nommés** (`scellements-v1.md`, `.ouvertures.md`, `ouvertures-p3bis-v1.md`, `prealables-p3bis-v1.md`, `go.md`) ; `registres/index-bras-attaque*` hors de l'extraction et refusé par `interdit()` | le clone de la fille n'extrait plus `/registres/*.md` mais des registres nommés (§ 4.1) | chemins de 7a cités par un registre : non refusés par `interdit()` (§ 13, S-3) ; contrôle de la fille au § 4.1 |
| **O-6** | `d0fe9053…` | en-tête « brouillon 4 » | § 4.4 : un écart d'encodage du script **arrête le bloc** (aucune création) | recopie des journaux du script des jeux : jouée par la mesure avec un journal présent par jeu (§ 11 bis), pas encore sur une instance |
| **C-1 et option (c)** | `d0fe9053…` C-1 ; R-2166 ; `e58be6c9…` § 5 | argument `PERIMETRE` exigé, ni plus ni moins que les lignes de `main` ; passage « sans concepts » répété (code 0, phrases non lues) | marqueur `PERIMETRE_T07` ; P3 et § 4.1 : périmètre recalculé du registre et comparé ; règle de fermeture écrite | décision de la mère : attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07` avant la création (P3) |
| **Règle de C7** | R-2231 ; R-2241 Q-5 | contrôles `C7` ancêtre de S7, `git diff --quiet C7 S7 -- src tests`, S7 ancêtre de `main` | P6 et P9 : `src/` de C7 égal à `37485ce5`, `tests/` de C7 égal à celui de S7, `CODE-T07` cite `CODE-T07-v2.json` au commit C7 | — |
| **Filtre d'inventaire** | CLO-08, CLO-09, R-2249 | — | § 4.2 et P10 : étiquettes `t06…` et `t07…` seules | étiquettes des autres tâches (§ 13, S-5) |
| **GARDES-CODE-01** | `47537dfa…` ; R-2249 | — | essai `tests/test_t07_tirages_degeneres_v1.py` versé avant C7 (P9) ; compté dans `ATT` | fusion dans `main` par la mère |
| **CLC-08** | `7a327462…` | non réglé (l. 362 du script) | § 7 : la fille lit le motif dans `repli-<n>.err` avant de conclure « ligne manquante » | § 13, S-4 |

## 0 ter. Ce qui change depuis le brouillon 5 (brouillon 6 : remède (a'))

Sources : mot de Lazar R-2285 (« (a') le remède, plus davantage de directions dans le plancher : un seuil du texte à changer :
go ») ; R-2298 (`n_plancher` = 800, notation par lots, réextraction des sondes figées de P3) ; R-2304 (code rendu, commit
`0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, configuration v7, `garde_principale` = « rapportee », repli) ; rapport du code du plancher v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md` (`cb31edc844c6bc4ee285219a819d2943fd140bf9d70f56d1da2e9e031520db92`),
§ 8 (devis) et § 9, point 5 (ce que l'ordre doit dire).

| Point | Où | Brouillon 5 | Brouillon 6 | Source |
|---|---|---|---|---|
| Commandes du module | § 5, étapes 8, 11, 12, 13 ; § 9 | `lecture_v2` (`empreinte-config`, `repli-seul`, `passe-blanc`, `etape-a-apres-repli`) | **`lecture_v4`** (mêmes sous-commandes ; `repli-recalcul` **refusé** par la v4, code 2, jamais appelé) ; étape B par `lecture_v4 etape-b` seule | R-2304 ; rapport, § 2 et § 9.5 |
| Script de l'instance | encadré, § 1, ligne (A), P9, P13, § 5, § 11, § 13 | v2, `e68d3306…`, celui de l'ordre | **v3 exigé** (`scripts/etape_a_t07_variante_b_v3.sh`, empreinte au marqueur `SHA_SCRIPT_V3_T07`) : le v2 appelle `lecture_v2` (l. 302, 357, 367, 372), qui refuse la v7 (« n_plancher 800 ≠ 200 ») ; changements exigés au § 13, S-12 ; **écart déclaré** : la consigne ne nomme pas le script ; sans lui, les commandes `lecture_v4` ne seraient pas jouées | constat de ce rédacteur (script lu, configuration v7 rejouée) |
| `CUBLAS_WORKSPACE_CONFIG` | § 5, étape 13 ; S-12 | posé par le module (`setdefault`) | **`:4096:8` exporté pour le processus de l'étape A** (le module le pose aussi avant tout calcul sur la carte) | rapport, § 9.5 |
| Processeur hôte | § 1 (machine), § 4.3, § 5 (étape 13) | — | **préférence d'hôte EPYC** (processeur de P3) ; à défaut, `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour l'étape A, **non éprouvé, déclaré** | rapport, § 5 et § 9.5 |
| Modèle de P3 | P13 ; § 4.1 ; § 5, étape 8 | — | révision de P3 (`0e9e39f2…`) au cache local (la réextraction ne télécharge jamais) : révision de 7b relevée ; le v3 précharge celle de P3 si elle diffère | rapport, § 9.5 |
| Dépense antérieure (P8) | P8 ; § 6 | `ANT0` ≤ 4,5 USD (pire cas 15,5 USD) | **`ANT0` ≤ 3,6 USD** (pire cas 16,4 USD) | rapport, § 8 ; R-2304 |
| Devis, minuterie, marge | § 6 ; § 4.4 ; § 7 | 3,0 à 4,5 h ; 7,9 à 10,9 h ; 5,2 à 7,1 USD ; 11,6 à 15,5 USD ; borne 39 240 s ; marge 1,1 h | **3,2 à 4,7 h ; 8,6 à 11,6 h ; ≈ 5,5 à 7,4 USD ; ≈ 12,5 à 16,4 USD ; borne 41 616 s (11,56 h) ; marge ≈ 0,45 h** (réserve CLE-12 aggravée) ; sous 20 USD | rapport, § 8 ; R-2304 |
| Configuration | § 1 ; marqueur `EMPREINTE_CONFIG_T07` | base v4 (`3d19b08c…`) | **v7**, chemin final `prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json` (fichier `3701407c…`, canonique attendue `4ff92c8e…`) ; mêmes six chemins | R-2304 |
| Code (C7, `CODE-T07`) | § 1 ; P6 ; P9 ; P13 ; ligne (A) ; § 4.1 ; § 5, étape 9 | `src/` de C7 égal à `37485ce5` ; dix-huit modules | `src/` de C7 égal à celui de `SRC7` (marqueur `COMMIT_SRC_CONTRE_LU_T07` : dernier commit contre-lu du code du remède (a'), fusionné dans `main`, fixé par la mère) ; **vingt-six modules** de `src/controle_ia/t07/` (huit neufs) dans `CODE-T07-v2.json` | R-2304 ; consigne (C7 et `CODE-T07` laissés à la mère) |
| Sorties de l'étape A non lues par la fille | § 2.5 | — | plus `planchers-figees-t07.npz` et `reextraction-p3-t07.json` | rapport, § 2 |
| Ligne d'essais `ATT`, P12 | ligne (A), P12, § 11 bis | `346 passed, 2 skipped, 4 xfailed` (arbres `79230a58…`, `744a9e16…`) | **texte inchangé** ; le code neuf change les arbres de S7 (cinq fichiers d'essais neufs) : « ATT valable pour S7 » sera absent et la mère **remesure** `ATT` par le § 11 bis avant la création (chemin prévu par P12) ; durée : 61 essais neufs, 63 à 76 s chez le développeur (rapport, § 6), dans la marge de la ligne « Essais » du § 6 (non ajoutée, déclaré) | constat de ce rédacteur |
| Taille des sorties (§ 5 bis) | § 5 bis ; § 13, S-13 | ordre de grandeur à `P` = 200 | **texte inchangé** ; à `P` = 800 la formule lit `n_plancher` de la v7 ; elle ne compte ni `planchers-figees-t07.npz` (≈ 5,2·10⁷ octets) ni les 2 × 200 directions de P3 notées en descriptif : S-13 | constat de ce rédacteur |

Tout le reste est égal à l'octet au brouillon 5 (vérifié par programme, statut).

## 0 quater. Ce qui change depuis le brouillon 6 (brouillon 7 : corrections du code, script v3)

Sources : contre-lecture du code du plancher v3 et décisions de la mère (R-2305 : CLP3-01 à CLP3-03, notes 05, 07, 10) ;
R-2306 (questions du brouillon 6 tranchées : script v3 écrit par le développeur ; `SRC7` ; `ATT` à C7) ; R-2309 (corrections
rendues, commit `7e23a554aca040016a08fe510504adec172c6998`, configuration v8, script v3, répétition jouet v3) ; rapport du code v2, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v2.md` (`71cc3b89c2df3c8f511796af0e3597844fb8fd1ec37735f0cbeae21d7b5ca231`).

| Point | Où | Brouillon 6 | Brouillon 7 | Source |
|---|---|---|---|---|
| Script de l'instance | encadré ; § 1 ; ligne (A) ; P13 ; § 11 ; § 12 ; § 13 | v3 à écrire ; marqueur `SHA_SCRIPT_V3_T07` | **écrit** : `scripts/etape_a_t07_variante_b_v3.sh`, `a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560`, commit `7e23a554` ; marqueur **rempli** ; S-12 et S-13 réglés | R-2306, R-2309 ; rapport v2, § 5 |
| Répétition jouet | § 1 ; § 11 | à faire | **17 verdicts sur 17 conformes** (un bras établi et un bras arrêté compris) | rapport v2, § 5 |
| Configuration | § 1 | v7 (`4ff92c8e…`), chemin final `…-v7.json` | **v8** (`0f32c6de…`), chemin final `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` : palier « carte » 10⁻³ (témoin) et 10⁻² (directions) ; v7 refusée par la v4 | R-2305 (CLP3-01), R-2309 |
| Passe à blanc | § 5, étape 12 | — | **contrôle avant l'ouverture** (CLP3-03) : sceaux de P3, principales, témoin, directions de P3, révision du modèle de P3 au cache hors ligne ; une faute refuse la passe (code 2) et l'étape A ne part pas | R-2305 ; rapport v2, § 4 |
| Modèle de P3 au cache | § 5, étape 8 | préchargé si la révision diffère | plus : **contrôlé au cache hors ligne** (`revision_au_cache`) | rapport v2, § 5 |
| Fautes de calcul de la réextraction ; état des figées | § 5, étape 13 | — | `MemoryError`, `TypeError`, `AttributeError`, `IndexError` : arrêt du seul bras (note 07) ; état des figées affiché par `etape-a-apres-repli` (note 10) | R-2305 |
| Étape B | § 9 | `lecture_v4 etape-b` seule | plus : `n_plancher` directions exigées par plancher décisif (note 05) | R-2305 |
| `SRC7` (C7) | § 1 ; P13 ; § 12 | dernier commit contre-lu du code, fusionné | **commit de `main` qui fusionne la branche finale du code** (arbre `src/`), fixé par la mère ; marqueur `COMMIT_SRC_CONTRE_LU_T07` laissé à la mère | R-2306 |
| `ATT` (P12) | ligne (A) ; P12 ; § 4.1 ; § 11 bis ; § 12 | `346 passed, 2 skipped, 4 xfailed`, arbres `79230a58…` et `744a9e16…` | **mesurée à C7** par la mère (marqueur neuf `ATT_C7_T07`) ; le contrôle compare les arbres de S7 à ceux de C7 (P9 les égale) | R-2306 |
| Taille des sorties | § 5 bis ; § 13, S-13 | constat (formule incomplète) | réglé par le script v3 : ≈ 1,87·10⁹ octets, sous 2·10⁹ | rapport v2, § 5 |

Devis (§ 6), P8 et minuterie : inchangés (le rapport v2 garde le § 8 de la v1). Tout le reste est égal à l'octet au brouillon 6
(vérifié par programme, statut).

## 0 quinquies. Ce qui change depuis le brouillon 7 (brouillon 8 : dernier tour du code, script v4)

Sources : R-2311 (contre-lecture courte des corrections, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/contre-lecture-courte-corrections-plancher-v3-v1.md` (`6f3769116d2432be4f5b…`, Claude Fable 5.2, R-2311 : sans défaut bloquant)) ; R-2312 (vérification courte du candidat 3 et de l'ordre 7, `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md`, `cfeeae9c…`, « après corrections », aucun nœud ; couples VC3-C et VC3-D) ; R-2313 (rapport du code v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v3.md` (`be2c86e215a1…`) ; code final `a621dcd3b929ce3ebd615fa852d4a7f5c103071d`).

| Point | Où | Brouillon 7 | Brouillon 8 | Source |
|---|---|---|---|---|
| Script de l'instance | encadré ; § 1 ; ligne (A) ; P13 ; § 5 ; § 11 ; § 12 ; § 13 | v3, `a19c594d…` | **v4**, `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6` (commit `a621dcd3`) : le v3 plus `lecture_v4 controle-avant-ouverture` à l'étape 8 et les formes sûres sous `set -u` ; le v3 reste intact | R-2311 (CLC-P3-02, -05), R-2313 |
| Contrôle avant l'ouverture | § 5, étape 8 | contrôle du cache seul avant le repli ; contrôle entier à la passe à blanc, après la garde d'ouverture | contrôle **entier** à l'étape 8, avant l'empreinte, `CODE-T07`, la branche, le repli et sa garde d'ouverture ; faute → code 2, rien d'ouvert | CLC-P3-02 |
| Répétition jouet | § 11 | v3, 17 sur 17 | **v4, 10 sur 10** (artefact « témoin retiré » arrêté à l'étape 8) | R-2313 |
| P12 (`ATT`) | § 3 | « elle vaut pour S7 parce que … » | **couple VC3-C tel qu'écrit** : `ATT` liée au commit de la mesure ; remesure à S7 si un fichier lu hors de `src/` et `tests/` change | R-2312 |
| P13 (`SRC7`) | § 3 | `SRC7` fixé par la mère | **couple VC3-D tel qu'écrit** : la mère écrit que l'arbre `src/` de `SRC7` est celui du dernier commit contre-lu, ou nomme les fichiers qui diffèrent | R-2312 |
| Nombre de lignes des mesures de 7b | P14 (neuf) ; § 5 bis | — | **nombre de lignes** (forme du tableau) lu par la mère sur processeur avant la création, par un script qui n'imprime qu'un entier ; aucune colonne lue, aucune ventilation ; ≤ ≈ 7 378, sinon aucune création (nœud) | CLC-P3-07 ; R-2314 (4) |
| Arrêt technique d'un bras | § 5, étape 13 ; § 7 ; § 8 | — | motif qui ne commence pas par `GardeArret` : arrêt technique, réserve, nœud de Lazar avant l'étape B ; la fille rapporte l'état des bras | CLC-P3-04 |
| Réserves neuves | § 13 (S-14 à S-17) ; § 11 bis | — | bash < 4.4 non éprouvé (refus d'un classifieur rapporté, non contourné) ; branche « autre révision » non éprouvable hors ligne ; morceau de poids tronqué non vide admis ; suite `tests/test_t07_*` rejouée entière par la mère à C7 | R-2313 |
| Mentions « en cours » | § 1 ; P13 ; § 12 | contre-lecture courte des corrections « en cours » | rendue, citée | R-2311 |

Devis (§ 6), P8 et minuterie : inchangés. Tout le reste est égal à l'octet au brouillon 7 (vérifié par programme, statut).

## 0 sexies. Ce qui change depuis le brouillon 8 (brouillon 9 : vérification finale)

Source : R-2315 (vérification finale, `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md` (`26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257`, Claude Fable 5.2, R-2315 : texte et ordre « après corrections », aucun nœud ; code `7e23a554..a621dcd3` « sans défaut bloquant »)) ; R-2314 (4) (P14 restreint par la mère).

| Point | Où | Brouillon 8 | Brouillon 9 | Source |
|---|---|---|---|---|
| P14 | encadré ; § 0 quinquies ; § 3, P14 ; § 5 bis ; § 7 | la mère compte les actions notées de 7b, colonne `jetons_notes` lue | **le seul nombre de lignes** (forme du tableau, lu à son en-tête), un entier ; aucune colonne chargée, aucune valeur, aucune ventilation ; il majore `n` ; au-delà d'environ 7 378 lignes, aucune création (nœud) : **couples VF4-A à VF4-E tels qu'écrits** | R-2314 (4) ; R-2315 (VF4-01) |
| Dernier commit contre-lu (`SRC7`) | encadré ; § 1 ; § 12 | différentiel `7e23a554..a621dcd3` sans contre-lecture | **`a621dcd3` dernier commit contre-lu** (vérification finale, mandat B : « sans défaut bloquant ») ; la mère écrit l'égalité de l'arbre `src/` de `SRC7` avec celui de `a621dcd3` (P13 (iii), VC3-D) | R-2315 |
| Contre-lecture de l'ordre | statut | brouillon 8 non contre-lu | brouillon 8 contre-lu, « après corrections », aucun nœud | R-2315 |
| Préchargement de la révision de P3 | § 3, P13, colonne « sinon » | « le v3 précharge » | le v4 de même (VF4-06) | R-2315 |

Notes de la vérification finale sans geste ici (rien avant le scellement, R-2315) : **VF4-08** (une faute hors de `FAUTES_DU_BRAS` sort de `lecture_v4 controle-avant-ouverture` en code 1, non 2 ; le script v4 arrête quand même en code 2, rien d'ouvert) ; **VF4-09** (motif recopié au journal : tête de 600 octets de l'erreur ; le fichier entier reste sur l'instance) ; **VF4-10** (S-14 à S-16 confirmées). Un script d'un entier pour P14 est proposé au § 4 de la vérification finale (lecture de l'en-tête du tableau ; non versé). Devis (§ 6), P8, minuterie, script v4, ligne (A) et marqueurs : inchangés. Tout le reste est égal à l'octet au brouillon 8 (vérifié par programme, statut).

## 1. Cadre

| Élément | Valeur |
|---|---|
| Code de T0.7 | **C7** : commit de `main` dont `src/` égale celui de `SRC7` (ligne (A) ; **brouillon 7** (R-2306) : `SRC7` est le commit de `main` qui fusionne la branche finale du code du remède (a') (vingt-six modules ; à ce jour **`a621dcd3…`** sur `prep/t07-plancher-v3-v1` (brouillon 8 ; `7e23a554…` au brouillon 7), non fusionnée ; **dernier commit contre-lu** (brouillon 9 : vérification finale, `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md` (`26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257`, Claude Fable 5.2, R-2315 : texte et ordre « après corrections », aucun nœud ; code `7e23a554..a621dcd3` « sans défaut bloquant »)) ; contre-lecture courte des corrections, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/contre-lecture-courte-corrections-plancher-v3-v1.md` (`6f3769116d2432be4f5b…`, Claude Fable 5.2, R-2311 : sans défaut bloquant) ; rapport du code v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v3.md` (`be2c86e215a1…`)) : `src/` de C7 égal à son arbre `src/`, fixé par la mère (P13, (iii)) ; **brouillon 6** : dernier commit contre-lu du code du remède (a'), vingt-six modules de `src/controle_ia/t07/`, `lecture_v4` compris, fusionné dans `main`, fixé par la mère, R-2304 ; au brouillon 5 : `37485ce50601b7d7ff9035bc34c734ec689ca731`, arbre `744a9e16…`, dix-huit modules) et dont `tests/` égale celui de S7, fixé après la fusion du code neuf et de ses essais (brouillon 6 ; au brouillon 5 : des essais CLC-04 et GARDES-CODE-01, R-2231, R-2241 Q-5 et Q-6, R-2249) ; **S7** : commit de scellement de T0.7, descendant de C7, `git diff --quiet C7 S7 -- src tests`, ancêtre de `main` ; contrôlés par la fille (§ 4.1) et sur l'instance |
| Script de l'instance | **brouillon 8** : `scripts/etape_a_t07_variante_b_v4.sh`, sha256 `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6` (commit `a621dcd3b929ce3ebd615fa852d4a7f5c103071d` de `prep/t07-plancher-v3-v1`, à fusionner dans `main` avec le code ; rapport du code v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v3.md` (`be2c86e215a1…`), § 2 et § 4 : le v3 plus l'étape 8 qui joue `lecture_v4 controle-avant-ouverture` avant l'empreinte, `CODE-T07`, la branche, le repli et sa garde d'ouverture, et les formes sûres sous `set -u` ; le v3 reste intact) ; **répété en jouet** (`scripts/repetition_jouet_variante_b_t07_v4.py`, `8b0e9590…` ; journal `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v4-journal.txt` (`98412f28c9d0dc446db86d73d51e1aa1ae3615545d242b5478e8de8bb9fb265c`) et résumé `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v4-resume.json` (`c36839fe2016ccea200ee5fa28c7a7116f457821d576ee93b88fbfb4d4b4f2e2`), scellés : **10 verdicts sur 10**, l'artefact « témoin retiré » arrêté en code 2 à l'étape 8 sans rien ouvrir) ; **brouillon 7** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 `a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560` (433 lignes ; commit `7e23a554aca040016a08fe510504adec172c6998` de `prep/t07-plancher-v3-v1`, à fusionner dans `main` avec le code ; rapport du code v2, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v2.md` (`71cc3b89c2df3c8f511796af0e3597844fb8fd1ec37735f0cbeae21d7b5ca231`), § 5 : S-12 (1) à (5) et S-13 appliqués, S-1, S-3, S-4, S-8 à S-11 non appliqués) ; **répété en jouet de bout en bout** (`scripts/repetition_jouet_variante_b_t07_v3.py`, `d8dde1fb…` ; journal `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v3-journal.txt` (`3d1421e72a7484566866e3a2169a7f00c5849f6a78ee936586e19a3e6d108b72`) et résumé `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v3-resume.json` (`691b98cfb3eb474b947376de69ece37dc0a178596b8aed14ffbe7b8d99e69529`), scellés : **17 verdicts sur 17 conformes**) ; contre-lecture courte des corrections rendue depuis (R-2311) ; **brouillon 6** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 au marqueur de la ligne (A) (`SHA_SCRIPT`) ; **à écrire** : le v2 plus les changements du § 13, S-12 (commandes `lecture_v4`, `CUBLAS_WORKSPACE_CONFIG`, révision de P3, variables du processeur hôte), répété en jouet et contre-lu avant que la mère remplisse le marqueur (décision de la mère) ; **au brouillon 5** : `scripts/etape_a_t07_variante_b_v2.sh`, sha256 `e68d3306…` (commit `04bc14a2`, sur `main`) ; répété en jouet (rapport complémentaire 5, § 5, passage 4 ; rejoué par la contre-lecture `7a327462…`, § 2) ; il appelle `lecture_v2` (l. 302, 357, 367, 372), qui refuse la configuration v7 |
| Arguments | `S7 C7 RUN6 CFG BR BR7B 'ATT' ECH PER` (neuf, dans cet ordre) |
| Configuration | `CFG` (ligne (A)), copiée sous `prereg/` et scellée dans S7 ; **brouillon 7** : **configuration v8**, chemin final **`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`** (copie octet pour octet, faite par la mère au scellement de T0.7, de `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json`, sha256 du fichier `e31c7a79dc1b…`, avec son compagnon) : la v7 avec les seules tolérances du palier « carte » resserrées, `carte_sonde` 10⁻³ et `carte_directions` 10⁻² (R-2305, CLP3-01 ; vérifié par programme) ; mêmes six chemins cités ; seule `lecture_v4` au commit `7e23a554` l'accepte (elle refuse la v7, « tolérances fixées d'avance ») ; **brouillon 6** : **configuration v7**, chemin final **`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`** (copie octet pour octet, faite par la mère au scellement de T0.7, de `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json`, sha256 du fichier `3701407cf96f…`, avec son compagnon) : la v5 du candidat 1 plus `methode_plancher` « difference_appariee_percentile », `n_plancher` 800 et la clé `plancher_figees` (`reextraction_p3_v1`, `n_p3` 200, tolérances 10⁻⁶, 10⁻², 10⁻¹, `garde_principale` « rapportee »), rien d'autre (R-2304) ; seule `lecture_v4` l'accepte (`lecture_v2` et `lecture_v3` la refusent) ; au brouillon 5 : base `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json`, `3d19b08c…`, `code_t07_exige` vrai ; empreinte canonique `<<EMPREINTE_CONFIG_T07>>` (attendue : `0f32c6de1a6b…` pour la v8, brouillon 7 ; `4ff92c8e…` pour la v7 au brouillon 6 ; `lecture_v4 empreinte-config`), revérifiée sur l'instance ; **chemins qu'elle cite** (lus par le script, étape 2) : les six de la v4, **inchangés dans la v7** (vérifié par programme ; § 11 bis), contrôlés par la fille (P12) |
| Périmètre des jeux | `PER` (ligne (A)) : lignes `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC`, `SCELLEMENT-CONCEPTS-T07` présentes à `main` à la création, séparées par des virgules (`JD,JA` à l'écriture de cet ordre), ou `aucun` |
| Course lue | 7b : run `RUN6`, branche `BR7B` (`calcul/t06-confirmation-7b-v1`, ou `-v2`, `-v3`), lue par refspec explicite |
| Machine | une **A100 SXM4 80 Go**, ≤ 1,30 USD de l'heure ; filtre de la chaîne de T0.6 (`session_v7.filtre_recherche`, `1609a4bf` : `reliability>=0.98`, `inet_down>=500`, `cuda_max_good>=13.0`) ; ≥ 16 cœurs, ≥ 128 Go de mémoire vive ; **brouillon 6** : **préférence d'hôte EPYC** (processeur de P3 et de sa régénération R-679, AMD EPYC 7513 : vise le palier « identique » de la sonde linéaire refaite par la réextraction ; § 4.3) ; à défaut, `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour le processus de l'étape A (**non éprouvé, déclaré** ; § 5, étape 13) ; **disque 100 Go** (modèle ≈ 16 Go, paquets ≈ 10 Go, activations recalculées ≈ 31,5 Go, sorties ≤ 2 Go et leurs morceaux) ; image `python:3.11-bookworm` ; étiquette `t07-b-v1` ; mode « args » (aucun serveur SSH) ; **H200 seulement après un mot de Lazar**, hors de cet ordre |
| Dossier de la fille | `/home/user/etape-a-t07-b-v1/` (neuf ; `-v2` à une reprise) |
| Branche de sortie | **`donnees/t07-etape-a-v1`**, absente du dépôt distant avant la première poussée (contrôlé par le script) ; sinon `-v2` ; jamais `main`, jamais une branche `calcul/…` |
| Dépôt | `https://github.com/lciric/controle-ia-travail.git`, en dur dans le script hors essai ; jamais `lciric/controle-ia` |
| Échéances | création après la poussée vérifiée de 7b et les préalables du § 3, au plus tard le **2026-11-22 à 12:00Z** ; **minuterie** : destruction par l'identifiant à `ECH` = création + `HMAX` (≤ 12 h, § 4.4), tant que le conteneur vit ; la fille détruit dès la poussée vérifiée |

## 2. Embargos et chemins interdits

1. **Jamais** la fille ni l'instance n'ouvrent, n'affichent, ne copient, ne hachent ni ne passent à un outil un
   `lecture-sondes-t06.json` (de 7b, de 7a, d'aucun run) ni son compagnon. Sur l'instance, la branche de 7b est lue par refspec
   explicite dans un **clone partiel** (`--filter=blob:none`) : seuls les fichiers **nommés** sont extraits (`runs/<run>/manifeste.json`,
   `diag/<run>/episodes-t06.json`, `diag/<run>/distillation-t06.json`, `diag/<run>/arret.json` s'il existe, et, dans
   `donnees/<run>/`, adaptateurs, mesures, textes, manifeste et morceaux du sous-ensemble) ; `diag/<run>/` n'est jamais listé ; le
   contenu de `lecture-sondes-t06.json` **n'est jamais descendu** ; le script s'arrête s'il le trouve dans l'arbre.
2. **Jamais** `donnees/lecture-b-7a-quarantaine-v1`, la branche `essai/t06-explo-v3`, ni `diag/`, `runs/`, `donnees/` de 7a
   (`20261109-070232-t06-reel`) ; clones de la **seule branche `main`** (`--single-branch`), `git fetch` par refspec explicite ;
   un registre qui citerait un chemin de 7a arrête la fille avant la création (§ 4.1 ; § 13, S-3).
3. **Jamais** `scripts/extraire_mesures_epreuve_t06_v1.py`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
   `docs/notes/bras-attaque/`, `registres/index-bras-attaque*` (O-5 : ni dans le clone de la fille, ni sur l'instance),
   l'étiqueteur ; **règle 9** : aucune recherche récursive sur un arbre qui contient un chemin interdit sans l'exclure (`git grep`
   avec exclusions) ; jamais `verifier-arbre`.
4. **Aucune lecture de résultat de 7b** : `lecture-cout-t06.json`, `resume.json`, `distillation-t06.json`, `episodes-t06.json`,
   `run.err` jamais affichés (le module de T0.7 lit ce qu'il lui faut ; la fille, rien).
5. **Aucune lecture des sorties de l'étape A** (`scores-actions-t07.npz`, ses morceaux, `sondes-t07.json`, `ouverture-t07.json`,
   `notation-t07.json`, `sondes-neuves-t07.npz`, ses morceaux, `planchers-figees-t07.npz`, `reextraction-p3-t07.json` (brouillon 6), `temoins-lexicaux-t07.json`, manifeste du run de T0.7) : hachées
   ou comptées, jamais affichées. Peuvent être lus, sans donnée décisive : le rapport du repli, la sortie de la passe à blanc,
   `taille-estimee.json`, le motif d'un `repli-<n>.err`, et les champs `octets`, `morceaux[].fichier`, `morceaux[].octets` et
   `morceaux[].sha256` des manifestes `*.morceaux.json` (§ 4.6) ; la fille n'en recopie que les champs du § 8.
6. **Aucune sortie de P3-bis lue ni citée** : seul le module lit, par sa garde, les registres de P3-bis (présence, date, sceau).
7. **Secrets** : clés par leur nom (`HF_TOKEN`, jeton GitHub) ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
   `/proc/*/environ` ; jamais affichés `creation-brute.json`, `offres.json`, `instances.json` ; garde des secrets à 0 avant tout
   envoi de texte.

## 3. Préalables bloquants (vérifiés par la fille, écrits au journal avec l'heure)

| # | Préalable | Où | Sinon |
|---|---|---|---|
| P1 | **Course 7b** : fin normale, branche `BR7B` poussée, rapatriement vérifié (compte rendu de la fille de 7b) ; **l'instance de 7b est détruite** selon son ordre (étiquette `t06-v2` : elle bloquerait P10) | compte rendu ; § 4.2 | attente |
| P2 | **`RUN-CONFIRMATION-T06`** au registre de `main`, chemin `runs/<RUN6>/manifeste.json` ; **le même fichier** sur `BR7B` (empreinte égale) | § 4.1 | attente |
| P3 | **Périmètre des jeux** (C-1, option (c)) : au plus une ligne chacune parmi `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC` et `SCELLEMENT-CONCEPTS-T07` ; `PER` égale exactement l'ensemble des lignes présentes à `main` ; fichiers, compagnons et journaux du script des jeux sur `main`. **Règle de fermeture** : la première ligne `OUVERTURE-T07` de l'étape A de ce run, écrite par la **garde du repli** (avant tout recalcul), ferme le périmètre ; une ligne inscrite après est exclue pour de bon. **Option (c)** : sans `SCELLEMENT-CONCEPTS-T07`, l'étape A va au bout « sans concepts » (phrases non lues, aucune direction ni tâche de plancher de concept ; T7-P9 « non lue », réserve R15 à l'étape B) ; la mère dit par un écrit daté, recopié au journal avant la création, si elle attend `-JC` et les concepts | § 4.1 | attente (décision de la mère) |
| P4 | **`GO-LECTURE-T07`** : une ligne ; son extrait scellé est une ligne de `registres/go.md` et nomme `GO` (ligne (A)) ; non révoquée, non échue ; aucune ligne `GO-ETAPE-A-T07`, ou, si elle existe, la garde lira l'une ou l'autre (écrit au journal) | § 4.1 | rien |
| P5 | **`SCELLEMENT-T07`** : une ligne, égale à `<<LIGNE_SCELLEMENT_T07>>` (c'est elle qui désigne le texte scellé de T0.7) | § 4.1 | arrêt, nœud |
| P6 | **`CODE-T07`** : une ligne, inscrite par la mère avant la création, citant **`registres/code-t07/CODE-T07-v2.json`** (**brouillon 6** : vingt-six modules de `src/controle_ia/t07/` au commit C7, huit neufs ; non encore écrit ; écrit par `python -m controle_ia.t07.code_t07_v1 ecrire <clone> C7 registres/code-t07/CODE-T07-v2.json`, scellé ; R-2231) dont le champ `commit` est C7 ; `CODE-T07-v1.json` reste versé, jamais cité | § 4.1 | rien |
| P7 | `SCORES-T07`, `SONDES-T07` absentes ; `VERDICT-P3BIS` et le journal de P3-bis relevés (présence, date), jugés par la garde | § 4.1 | arrêt, nœud |
| P8 | **Engagement** de dépense sous `GO` au registre des dépenses (mère) ; **`ANT0` = dépense déjà inscrite sous GO-2026-11-10-04 et sous GO-2026-11-10-06** (O-4) ; **`20 − ANT0` ≥ pire cas du devis** (§ 6 : **16,4 USD**, brouillon 6 ; 15,5 USD au brouillon 5), soit **`ANT0` ≤ 3,6 USD** (4,5 USD au brouillon 5) | § 4.1 | rien (au-delà : devis neuf, mot de Lazar) |
| P9 | **Code** (R-2231) : C7 ancêtre de S7 ; `src/` de C7 égal à celui de `SRC7` (brouillon 6 ; `37485ce5` au brouillon 5) ; `git diff --quiet C7 S7 -- src tests` ; S7 ancêtre de `main` ; essais CLC-04 (`tests/test_t07_ouvrir_reel_concepts_v1.py`) et GARDES-CODE-01 (`tests/test_t07_tirages_degeneres_v1.py`) présents à S7 ; script de l'instance à son empreinte (§ 1) | § 4.1 | arrêt |
| P10 | `vastai` 1.8.3 ; `HF_TOKEN` et le jeton GitHub présents (par le nom) ; **inventaire : aucune instance d'étiquette `t06…` ni `t07…`** (CLO-08 : une instance d'une autre tâche du programme — P3-bis, T0.8, pièces HD ou R du texte de validité de l'adaptateur — n'interdit ni ne retarde la création) | § 4.2 | attente (`t06…` de 7b non détruite) ; arrêt (autre) |
| P11 | **Heure** : création au plus tard le 2026-11-22 à 12:00Z | `date -u` | nœud |
| P12 | **Ligne d'essais `ATT`** (O-1) valable pour S7 (**brouillon 7**, R-2306 : `ATT` est **mesurée à C7** par la mère, commande du § 11 bis, tête au commit C7, après la fusion du code ; valeur au marqueur de la ligne (A) ; elle vaut pour S7 si `src/` et `tests/` de S7 égalent ceux de C7 (P9 ; le contrôle du § 4.1 compare les arbres de S7 à ceux de C7 : il redit P9 et ne lie pas `ATT` au commit de la mesure) **et** si les fichiers que les essais lisent hors de `src/` et de `tests/` (extraction partielle du script : `docs/notes/g0-deux-semaines-v1/`, `brouillons/T0.7-*`, `prereg/*`, chemins cités par la configuration) sont les mêmes à S7 ; la mère écrit, avec la valeur de `ATT`, le commit de la mesure et ses arbres `src/` et `tests/` (écrit daté, recopié au journal par la fille), et **remesure à S7** après le scellement si un de ces fichiers a changé entre C7 et S7 ; un écart ne coûte qu'un arrêt de code 2 à l'étape 6, avant le modèle ; au brouillon 6, ci-après) : arbre `tests/` de S7 = `79230a584e8675f1771fd4f0a9315de71c2bcbdc`, arbre `src/` de S7 = `744a9e16f1635ff402e798b4ac868a57311e44b8` (ceux de la mesure, § 11 bis) ; la configuration `CFG` cite les six chemins de la v4 ; sinon `ATT` est **remesurée** par la commande du § 11 bis à S7, avant la création | § 4.1 | remesure (mère), puis seulement création |
| P13 | **Brouillon 6 (remède (a'))** : (i) **révision du modèle** du manifeste de `RUN6` (`config.agent.revision`, lue sur `BR7B`, rien d'autre affiché) comparée à celle de P3, `0e9e39f249a16976918f6564b8830bc894c89659` (la réextraction lit le modèle de P3 au cache local et ne télécharge jamais : modèle absent → bras arrêté) ; (ii) **script v3** présent sur `main` à l'empreinte `SHA_SCRIPT` (brouillon 7 : `a19c594d…`, répété en jouet, 17 verdicts sur 17 ; contre-lecture courte des corrections rendue depuis, R-2311 ; **brouillon 8** : script v4, `4b17d1f0…`, répété en jouet, 10 verdicts sur 10 ; § 13, S-12) ; (iii) **`SRC7`** fixé par la mère (brouillon 7 : commit de `main` qui fusionne la branche finale du code ; la mère écrit avec lui, par un écrit daté recopié au journal, que son arbre `src/` est celui du dernier commit contre-lu de cette branche — `git diff --quiet <dernier commit contre-lu> SRC7 -- src` —, ou nomme les fichiers de `src/` qui diffèrent et la contre-lecture qui les couvre) | § 4.1 | (i) égale : rien ; autre : écrit au journal, le v3 précharge la révision de P3 (§ 5, étape 8 ; brouillon 9 : le v4 de même, VF4-06) ; (ii), (iii) absents : rien |
| P14 | **Brouillon 8 (CLC-P3-07 ; R-2314 (4))** : **nombre de lignes des mesures de 7b** (forme du tableau : premier axe du tableau `jetons_notes` de `donnees/<RUN6>/mesures-t06.npz` de 7b, sceau vérifié, lu à l'en-tête du tableau ; **aucune colonne chargée, aucune valeur lue, aucune ventilation par condition** : la longueur des actions est un prédicteur de la base « mots et coût », la mère n'en voit aucune valeur) **lu par la mère sur processeur**, par un script qui **n'imprime qu'un entier**, seul écrit au journal ; ce nombre majore `n` du § 5 bis (actions à `jetons_notes` > 0, que seul le script de l'instance compte, étape 7) ; il doit tenir sous **≈ 7 378** (borne S-13 : total des sorties ≤ 2·10⁹ octets aux nombres du § 5 bis) | mère, avant la création | au-delà : aucune création (nœud ; la mère ne lit pas la colonne pour départager ; la borne arrêterait l'instance en code 2 après les paquets et les essais, § 5 bis) |

## 4. Étapes et commandes (session de la fille)

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc commence par la ligne (A)**. Les clés passent par leur nom.

**(A)** :

```bash
W=/home/user/etape-a-t07-b-v1; M=$W/main; J=$W/journal-etape-a-t07-b-v1.md; GO=GO-2026-11-10-06; GO4=GO-2026-11-10-04; PLAF=20; ANT0=<<DEPENSE_ANTERIEURE_USD>>; RUN6=<<RUN_T06_7B>>; BR7B=<<BRANCHE_7B>>; C7=<<COMMIT_CODE_T07>>; S7=<<COMMIT_SCELLEMENT_T07>>; CFG=<<CHEMIN_CONFIG_T07>>; PER=<<PERIMETRE_T07>>; ATT='<<ATT_C7_T07>>'; BR=donnees/t07-etape-a-v1; SCRIPT=scripts/etape_a_t07_variante_b_v4.sh; SHA_SCRIPT=4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6; SRC7=<<COMMIT_SRC_CONTRE_LU_T07>>; REV_P3=0e9e39f249a16976918f6564b8830bc894c89659; URL=https://github.com/lciric/controle-ia-travail.git; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
```

### 4.1 Préalables depuis `main` (lecture seule)

```bash
# (A) — registres NOMMÉS (O-5) : jamais le motif /registres/*.md, qui extrairait registres/index-bras-attaque*
mkdir -p "$W" && git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$M" && git -C "$M" sparse-checkout set --no-cone '/registres/scellements-v1.md' '/registres/go.md' '/registres/depenses.md' '/registres/ouvertures-p3bis-v1.md' '/registres/prealables-p3bis-v1.md' '/registres/go-extraits/' '/registres/code-t07/' "/$SCRIPT" && git -C "$M" checkout -q main && git -C "$M" rev-parse HEAD; j "main $(git -C "$M" rev-parse HEAD)"
REG="$M/registres/scellements-v1.md"; for k in RUN-CONFIRMATION-T06 SCELLEMENT-JEUX-T07-JD SCELLEMENT-JEUX-T07-JA SCELLEMENT-JEUX-T07-JC SCELLEMENT-CONCEPTS-T07 GO-LECTURE-T07 GO-ETAPE-A-T07 SCELLEMENT-T07 CODE-T07 SCORES-T07 SONDES-T07 VERDICT-P3BIS; do printf '%s %s\n' "$k" "$(grep -c "^| $k |" "$REG")"; done
P=; for k in JD JA JC CONCEPTS; do c=SCELLEMENT-JEUX-T07-$k; [ "$k" = CONCEPTS ] && c=SCELLEMENT-CONCEPTS-T07; [ "$(grep -c "^| $c |" "$REG")" = 1 ] && P="$P,$k"; done; P=${P#,}; [ -n "$P" ] || P=aucun; [ "$P" = "$PER" ] && echo "PERIMETRE conforme ($PER)" || echo "ÉCART : PERIMETRE $PER, registre $P"
awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); print $4 }' "$REG" "$M/registres/prealables-p3bis-v1.md" 2>/dev/null | grep -E '20261109-070232-t06-reel|lecture-sondes-t06|bras-attaque|mode-tenu-a-l-ecart|lecture-b-7a|extraire_mesures_epreuve' | wc -l
LR=$(grep '^| RUN-CONFIRMATION-T06 |' "$REG"); PR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$PR" = "runs/$RUN6/manifeste.json" ] && git -C "$M" fetch -q origin "refs/heads/$BR7B:refs/remotes/origin/$BR7B" && [ "$(git -C "$M" show "refs/remotes/origin/$BR7B:$PR" | sha256sum | cut -d' ' -f1)" = "$HR" ] && echo "RUN-CONFIRMATION-T06 conforme à $BR7B"
git -C "$M" show "refs/remotes/origin/$BR7B:runs/$RUN6/manifeste.json" | python3 -I -c 'import json,sys; r=json.load(sys.stdin)["config"]["agent"]["revision"]; print("révision de 7b égale à celle de P3" if r == sys.argv[1] else "révision de 7b autre que celle de P3 (P13)")' "$REV_P3"
LA=$(grep '^| GO-LECTURE-T07 |' "$REG"); PA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$(sha256sum < "$M/$PA" | cut -d' ' -f1)" = "$HA" ] && [ "$(cut -d' ' -f1 "$M/$PA.sha256")" = "$HA" ] && [ "$(grep -c '^| GO-' "$M/$PA")" = 1 ] && grep -qxF -- "$(grep '^| GO-' "$M/$PA")" "$M/registres/go.md" && grep -q "^| $GO |" "$M/$PA" && echo "GO-LECTURE-T07 conforme ($GO)"
[ "$(grep '^| SCELLEMENT-T07 |' "$REG")" = "$(cat "$W/ligne-scellement-t07.txt")" ] && echo "SCELLEMENT-T07 inchangée"
LC=$(grep '^| CODE-T07 |' "$REG"); PC=$(printf '%s\n' "$LC" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HC=$(printf '%s\n' "$LC" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$PC" = registres/code-t07/CODE-T07-v2.json ] && [ "$(sha256sum < "$M/$PC" | cut -d' ' -f1)" = "$HC" ] && [ "$(cut -d' ' -f1 "$M/$PC.sha256")" = "$HC" ] && [ "$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["commit"])' "$M/$PC")" = "$C7" ] && echo "CODE-T07 conforme (CODE-T07-v2.json, C7)"
grep -cE "$GO4|$GO" "$M/registres/depenses.md"
git -C "$M" merge-base --is-ancestor "$C7" "$S7" && git -C "$M" diff --quiet "$SRC7" "$C7" -- src && git -C "$M" diff --quiet "$C7" "$S7" -- src tests && git -C "$M" merge-base --is-ancestor "$S7" HEAD && [ -n "$(git -C "$M" ls-tree "$S7" -- tests/test_t07_ouvrir_reel_concepts_v1.py)" ] && [ -n "$(git -C "$M" ls-tree "$S7" -- tests/test_t07_tirages_degeneres_v1.py)" ] && [ "$(sha256sum < "$M/$SCRIPT" | cut -d' ' -f1)" = "$SHA_SCRIPT" ] && echo "code et script conformes"
[ "$(git -C "$M" rev-parse "$S7:tests")" = "$(git -C "$M" rev-parse "$C7:tests")" ] && [ "$(git -C "$M" rev-parse "$S7:src")" = "$(git -C "$M" rev-parse "$C7:src")" ] && [ "$(git -C "$M" show "$S7:$CFG" | python3 -I -c 'import json,sys
def f(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str): yield x["chemin"]
        for v in x.values(): yield from f(v)
    elif isinstance(x, list):
        for v in x: yield from f(v)
print(" ".join(sorted(set(f(json.load(sys.stdin))))))')" = "diag/20261019-230011-p3-reel/sondes-figees.json donnees/20261007-082440-t05-extraction/taches-entrainement.json donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz donnees/T0.7-faits-repe-v1/facts_true_false.csv donnees/T0.7-models-under-pressure-v1/training/train.jsonl runs/20261019-230011-p3-reel/manifeste.json" ] && echo "ATT valable pour S7"
```

Attendus : `1` pour `RUN-CONFIRMATION-T06`, `GO-LECTURE-T07`, `SCELLEMENT-T07`, `CODE-T07` ; `0` ou `1` pour chaque ligne de
jeux et pour les concepts, et « PERIMETRE conforme » ; `0` pour `SCORES-T07`, `SONDES-T07` ; `GO-ETAPE-A-T07` et
`VERDICT-P3BIS` relevés (comptes seulement ; le journal de P3-bis `registres/ouvertures-p3bis-v1.md` n'est ni affiché ni lu par la fille, § 2.6 : seule sa présence se relève, par `[ -f "$M/registres/ouvertures-p3bis-v1.md" ] && echo présent || echo absent`) ; **`0`** pour le compte des chemins interdits ou de 7a cités par un registre (sinon nœud : le script de
l'instance ne refuse pas un chemin de 7a, § 13, S-3) ; les messages « conforme », « inchangée », « code et script conformes », « révision de 7b égale à celle de P3 » (brouillon 6, P13 ;
l'autre message est écrit au journal, sans arrêt),
« ATT valable pour S7 » ; au moins une ligne d'engagement, et `ANT0` = somme des dépenses inscrites sous les deux lignes.
`ligne-scellement-t07.txt` : la ligne `SCELLEMENT-T07` (P5), écrite à l'octet par la fille au début. « ATT valable » absent :
P12, remesure par la mère (§ 11 bis), nouvelle valeur de `ATT` écrite au journal par un écrit daté de la mère. La branche de 7b
est lue **par refspec**, dans un clone partiel, et seul le manifeste y est lu (empreinte, jamais affiché).

### 4.2 Outil et inventaire (filtre `t06…` et `t07…` seulement : CLO-08, R-2249)

```bash
# (A)
vastai --version; date -u +%FT%TZ; for v in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN; do [ -n "${!v:-}" ] && echo "$v présent" || echo "$v ABSENT : aucune création"; done
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; print([(i.get("id"), i.get("label"), i.get("actual_status")) for i in (d or []) if str(i.get("label") or "").startswith(("t06", "t07"))])'
```

Seuls l'identifiant, l'étiquette et l'état des instances `t06…` et `t07…` sont imprimés. **Attendu : liste vide.** Une instance
d'une autre tâche du programme (P3-bis, T0.8, pièces HD ou R du texte de validité) n'est pas imprimée et n'interdit ni ne
retarde la création (liste d'arrêt de T0.7, CLO-08 ; écrits gelés (b) 1 et 2). Une instance `t06…` (celle de 7b, `t06-v2`, non
encore détruite) : attente de sa destruction selon son ordre, puis inventaire refait. Une instance `t07…` : arrêt, compte rendu
(une seconde instance de cette étape ne se crée jamais sans écrit de la mère).

### 4.3 Recherche de l'offre

```bash
# (A)
timeout -k 5 120 vastai search offers 'num_gpus=1 rentable=true gpu_name=A100_SXM4 reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=100 dph_total<=1.3' -o dph_total --storage 100 --raw > "$W/offres.json" 2>"$W/offres.err"; echo "code $?"
python3 -I -c 'import json,sys; o=json.load(open(sys.argv[1])); o=o.get("offers", o) if isinstance(o, dict) else o; o=[x for x in o if x.get("gpu_name")=="A100 SXM4" and x.get("num_gpus")==1 and float(x.get("dph_total",9))<=1.3 and float(x.get("gpu_ram",0))>=79000 and 0<=float(x.get("storage_total_cost",9))<=0.08 and 0<=float(x.get("inet_down_cost",9))<=0.05 and 0<=float(x.get("inet_up_cost",9))<=0.05]; o=sorted(o, key=lambda y: (0 if "EPYC" in str(y.get("cpu_name") or "") else 1, float(y.get("dph_total",9)))); x=o[0] if o else None; print("aucune offre" if x is None else "id=%s carte=%s prix_h=%.4f stockage_h=%s machine=%s cuda=%s cpu=%s offres=%d" % (x["id"], x["gpu_name"], float(x["dph_total"]), x.get("storage_total_cost"), x.get("machine_id"), x.get("cuda_max_good"), x.get("cpu_name"), len(o)))' "$W/offres.json"
```

**Brouillon 6** : parmi les offres retenues, un hôte dont `cpu_name` porte « EPYC » passe d'abord (prix croissant dans chaque groupe ; champ absent : hôte non EPYC) ; `cpu` imprimé et écrit au journal ; sans offre EPYC, la moins chère est prise et le script v3 pose `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour l'étape A (non éprouvé, déclaré ; § 5, étape 13). Une offre n'est retenue que si son stockage est ≤ 0,08 USD de l'heure et son téléchargement, dans les deux sens, ≤ 0,05 USD par Go (bornes du devis, § 6 ; garde d'offre de la chaîne de T0.6, `src/controle_ia/t06/session_v2.py` l. 104-109) ; un champ absent écarte l'offre. Au plus **trois** recherches, espacées d'au moins 30 minutes ; vides : compte rendu, nœud (aucune autre carte sans mot). Le prix
horaire relevé (`prix_h`, carte et disque compris) entre au relevé de dépense (§ 6) et à la borne de la minuterie (§ 4.4) ;
`offres.json` n'est jamais affiché.

### 4.4 Création, une fois

```bash
# (A) ; OFFRE = l'id de la ligne imprimée au § 4.3 ; PRIX_H = son prix_h
B64=$(base64 -w0 < "$M/$SCRIPT") && [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$SHA_SCRIPT" ] || { echo "ÉCART : encodage du script : aucune création"; j "ÉCART : encodage du script"; exit 2; }
HMAX=$(python3 -I -c 'import sys; p,a=map(float,sys.argv[1:3]); print(max(0, min(43200, int((20.0 - a - 1.2 - 0.1) / p * 3600))))' "$PRIX_H" "$ANT0"); [ "$HMAX" -ge 41616 ] || { echo "ÉCART : borne de la minuterie $HMAX s < pire cas du devis : aucune création (nœud)"; exit 2; }
TC=$(date +%s); ECH=$((TC + HMAX)); j "création demandée, TC=$TC, échéance de la minuterie $ECH (HMAX=$HMAX s)"
GO_ID=$GO timeout -k 10 300 vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 100 --cancel-unavail --label t07-b-v1 --env "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" --entrypoint bash --args -c "echo $B64 | base64 -d > /root/etape-a-t07-b.sh && bash /root/etape-a-t07-b.sh $S7 $C7 $RUN6 $CFG $BR $BR7B '$ATT' $ECH $PER" > "$W/creation-brute.json" 2>&1; echo "code $?"
python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); print("succès :", d.get("success"), "; identifiant :", d.get("new_contract"))' "$W/creation-brute.json"
```

`GO_ID=$GO` en tête : la garde de calcul de la session exige un GO valide de `registres/go.md` dans la commande. **O-6** : un écart
d'encodage du script, ou une borne de minuterie sous le pire cas du devis (41 616 s = 11,56 h, § 6 ; brouillon 6 ; 39 240 s = 10,9 h au brouillon 5), **arrête le bloc** : aucune
création. **O-4** : `HMAX` = la plus petite de 12 h et de la durée que paie `20 − ANT0 − 1,20 (téléchargement) − 0,10 (disque
après l'arrêt)` au prix relevé. L'identifiant imprimé devient `ID` (écrit au journal) ; `creation-brute.json` n'est jamais
affiché. Création incertaine (code ≠ 0 sans identifiant) : inventaire (§ 4.2) avant tout autre geste ; **aucune seconde
création** sans écrit de la mère. **Rappel daté à `ECH`** (O-3) : la fille l'écrit au journal, le pose dans sa session et **envoie aussitôt à la mère, avant la première surveillance, l'identifiant, `TC`, `HMAX` et `ECH` en date UTC** (sans ce message, la mère ne connaît ni l'instance ni l'échéance si la session de la fille tombe ; à défaut d'identifiant, l'instance se retrouve par son étiquette `t07-b-v1`, § 4.2) ; la mère
le pose aussi dans la sienne (inventaire du § 4.2 à `ECH`, destruction par l'identifiant si l'instance est encore là).

### 4.5 Surveillance (toutes les 15 minutes ; aucun couperet de temps)

```bash
# (A) ; ID, TC et PRIX_H du journal
timeout -k 5 120 vastai logs "$ID" --tail 400 2>/dev/null | grep -E '^[0-9TZ:-]+ T07 |^T07 REFUS' | tail -n 20
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>/dev/null); printf '%s' "$out" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; d=d[0] if isinstance(d, list) else d; print("état :", d.get("actual_status"), "/", d.get("intended_status"))'
python3 -I -c 'import sys,time; p,tc,ant=map(float,sys.argv[1:4]); h=(time.time()-tc)/3600; c=ant+p*h+1.2; print(f"cumul sous GO-2026-11-10-04 et GO-2026-11-10-06 ≈ {c:.2f} USD (carte et disque {p*h:.2f}, téléchargement borné 1,20, antérieur {ant:.2f}) ; projeté + 15 min {c+p/4:.2f}")' "$PRIX_H" "$TC" "$ANT0"
```

Seules les lignes `… T07 …` du script sont lues (jamais d'état de sonde, d'aire ni de score : le script n'en imprime aucun).
Attendu, dans l'ordre : minuterie lancée (PID, échéance) ; carte ; code conforme ; cinq lignes « registre … » (recopié de main ou
absent) ; une ligne par élément du périmètre (présent, journaux du script ; ou « absente, hors du périmètre ») ; registres
recopiés, périmètre `PER` ; sortie de 7b extraite ; **essais : code 0, ligne égale à `ATT`** ; **taille estimée … ≤ borne**
(octets, morceaux prévus) ; disque libre ; modèle au cache local ; configuration et empreinte ; `CODE-T07 conforme` ; repli, essai
1, code 0 (« recalcul fait ») ; « poussé » ; passe à blanc code 0 ; « poussé » ; étape A code 0, run ; « poussé » (légers) ;
« découpé (O-2) » et « poussé … morceaux » s'il y a des fichiers de plus de 90 Mo ; « poussé » (traces) ; `FIN` ; « fin, code
0 ; état « stopped » demandé : HTTP 200 ». Une ligne `ARRET` : § 7. Une ligne `MINUTERIE` : l'échéance est atteinte (§ 4.7). Une ligne `T07 REFUS` (sans date : le script est sorti avant sa minuterie et sans demander l'état « stopped », l. 27, 34 et 42), ou aucune ligne `T07` trente minutes après l'état « running » : destruction par l'identifiant (§ 4.7), compte rendu, nœud.

### 4.6 Vérification de la poussée (sans rien rapatrier des sorties)

```bash
# (A)
git -C "$M" ls-remote origin "refs/heads/$BR"; git -C "$M" fetch -q --filter=blob:none origin "refs/heads/$BR:refs/remotes/origin/$BR" && git -C "$M" log --format=%s "$S7..origin/$BR" | head -n 20 && git -C "$M" diff --stat "$S7" "origin/$BR" -- src tests | tail -n 1
R7=refs/remotes/origin/$BR; for f in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- replis-t07 passes-blanches-t07 runs diag donnees | grep -v '\.sha256$' | grep -v 'lecture-sondes-t06' | grep -v '\.morceau-[0-9][0-9][0-9]$'); do a=$(git -C "$M" show "$R7:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R7:$f.sha256" 2>/dev/null | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f" || echo "ÉCART $f"; done
for m in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- donnees | grep '\.morceaux\.json$'); do git -C "$M" show "$R7:$m" | python3 -I -c 'import json,subprocess,sys
m = json.load(sys.stdin); r, ref, base, nom = sys.argv[1:5]
def g(*a):
    p = subprocess.run(["git", "-C", r, *a], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""
noms = set(g("ls-tree", "-r", "--name-only", ref, "--", base).split())
ok = all(base + "/" + x["fichier"] in noms and (g("show", ref + ":" + base + "/" + x["fichier"] + ".sha256").split() or [""])[0] == x["sha256"] for x in m["morceaux"]) and sum(x["octets"] for x in m["morceaux"]) == m["octets"]
print("OK" if ok else "ÉCART", nom, len(m["morceaux"]), "morceaux")' "$M" "$R7" "$(dirname "$m")" "$m"; done
git -C "$M" show "$R7:registres/scellements-v1.md" | grep -E '^\| (SCORES|SONDES)-T07 \|' | cut -d'|' -f2,3
```

Attendu : les commits de la branche (garde et repli, passe à blanc, étape A légers, morceaux par lots s'il y en a, traces),
**aucun changement sous `src` ni `tests`**, `OK` pour chaque fichier léger **ajouté par l'instance** (jamais un fichier venu de
`main` ou de 7b ; les activations ne sont jamais poussées ; le rapport du repli est
`donnees/<run>/activations/rapport-repli-t07.json`), `OK` pour chaque manifeste de morceaux (chaque morceau nommé présent dans l'arbre, son compagnon égal à l'empreinte que le
manifeste écrit, somme des tailles écrites égale à la taille du fichier ; **aucun morceau descendu** : le clone est partiel, seuls
l'arbre, les manifestes et les compagnons sont lus ; `git ls-tree -l` n'est pas employé, il descendrait chaque morceau pour en
donner la taille), et les deux lignes `SCORES-T07`, `SONDES-T07` (clé et date seulement). L'empreinte de chaque morceau et la
recomposition se vérifient avant l'étape B (§ 9).

### 4.7 Arrêt et destruction par l'identifiant (R10), inventaire final

```bash
# (A)
timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"; j "destruction demandée ($ID)"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
```

Dès la poussée vérifiée (§ 4.6), ou sur un `ARRET` une fois ses traces poussées, ou à l'atteinte du plafond (§ 6). **O-3,
corrigé** : le script demande de lui-même l'état « stopped » à sa fin (`FIN` ou `ARRET`) ; **la minuterie, sous-processus du
conteneur, meurt alors avec lui** : elle ne garantit la destruction que si l'instance tourne encore à `ECH`. Après « stopped »,
**seule la fille détruit** ; le disque reste facturé (≤ 0,08 USD de l'heure) jusqu'à la destruction : rappel daté à `ECH`
(§ 4.4), et, si la session de la fille tombe, la mère fait détruire par l'identifiant écrit au journal. Une ligne
`MINUTERIE : DELETE, essai n : HTTP c` au journal de l'instance dit l'essai de destruction et son code ; « cinq DELETE sans
succès » : destruction par la fille, aussitôt. Du **seul identifiant créé** ; jamais `pkill`, `killall`, ni un geste sur une
autre instance ; inventaire du § 4.2 après.

## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v4.sh` : le v3, lui-même le v2, `e68d3306…`, et les changements du § 13, S-12 ; plus l'étape 8 du brouillon 8)

0. **Arguments et minuterie** : neuf arguments ; `ECH` dans [maintenant, maintenant + 24 h] ; `PERIMETRE` parmi `JD`, `JA`, `JC`,
   `CONCEPTS` ou `aucun` ; `ATTENDU` « - » refusé hors mesure ; variables d'essai refusées hors essai ; minuterie : `DELETE` de
   l'instance par son identifiant (`CONTAINER_ID`, API de Vast) à `ECH`, cinq essais journalisés avec leur code HTTP (O-3).
1. **Machine** : outils, jetons par leur nom, carte visible (`nvidia-smi`).
2. **Code** : clone partiel de la seule branche `main`, extraction partielle (motifs fixes, registres nommés, chemins cités par la
   configuration ; `diag/*/lecture-sondes-t06.json*` exclu ; ni `docs/notes/bras-attaque/` ni `registres/index-bras-attaque*`),
   commit S7 ; gardes : tête = S7, C7 ancêtre, `git diff --quiet C7 S7 -- src tests`, S7 ancêtre de `main`.
3. **Registres nommés de `main`** (O-5 : `scellements-v1.md`, `scellements-v1.md.ouvertures.md`, `ouvertures-p3bis-v1.md`,
   `prealables-p3bis-v1.md`, `go.md`) et **fichiers qu'ils citent** avec leurs compagnons (hors du run de 7b ; un fichier suivi à
   S7 hors de l'extraction partielle y est d'abord ajouté) ; chemin interdit cité → arrêt ; **périmètre** (C-1) : chaque ligne de
   jeux et la ligne des concepts au plus une fois, présentes **exactement** comme `PERIMETRE` le dit (sinon arrêt, « rien n'est
   ouvert »), fichiers et compagnons présents, **journaux du script** du dossier de chaque jeu recopiés ; `src/` et `tests/`
   inchangés (contrôlé).
4. **Sortie de 7b**, par refspec explicite, fichiers nommés seulement (§ 2.1) ; `arret.json` de 7b recopié s'il existe (la garde
   le lit) ; fichiers cités par la configuration de 7b recopiés de `main`.
5. **Environnement** : `python3 -m venv`, `pip install -r requirements-gpu.txt` de S7 (borne 3 600 s) ; torch voit la carte.
6. **Essais figés** `tests/test_t07_*.py` (liste et empreintes dans les traces), **avant le modèle** (O-1) : code 0 **et**
   dernière ligne, durée retirée, égale à `ATT` ; sinon arrêt de code 2 (aucun modèle descendu, rien d'ouvert) ; `src/` et
   `tests/` non écrits par les essais (contrôlé).
7. **Taille des sorties de l'étape A** estimée et bornée **avant toute ouverture** (O-2, § 5 bis) : au-dessus de la borne →
   arrêt de code 2, nœud, rien d'ouvert ; estimation impossible → arrêt.
8. **Modèle** descendu au cache local (`precharger_modele`, révision figée du manifeste de 7b, `HF_TOKEN`) ; **brouillon 6** : si
   elle n'est pas celle de P3 (`0e9e39f2…`, lue dans `runs/20261019-230011-p3-reel/manifeste.json`, `config.agent`), le v3
   précharge aussi celle de P3 (échec → arrêt de code 2, rien d'ouvert ; la réextraction ne télécharge jamais) ; **brouillon 7** : puis la révision
   de P3 est **contrôlée au cache hors ligne** (`revision_au_cache`, `HF_HUB_OFFLINE=1` ; absente ou incomplète → code 2,
   rien d'ouvert ; rapport v2, § 5, point 4) ; **brouillon 8** (script v4, CLC-P3-02 ; rapport v3, § 2) : ce contrôle isolé
   est remplacé par **`lecture_v4 controle-avant-ouverture . CFG`** (`HF_HUB_OFFLINE=1`, lecture seule), qui le comprend, dans les deux
   modes, **avant** l'empreinte de la configuration, `CODE-T07`, la branche, le repli et sa garde d'ouverture journalisée : contrôles de
   configuration de la v4, sceaux des quatre entrées de P3, principales, témoin et directions de P3 au fichier léger, révision
   du modèle de P3 au cache (mode réel ; index lu sous garde, morceaux annoncés tous présents, tailles non nulles : CLC-P3-03) ;
   faute → code 2, motif au journal (« ARRET : contrôle avant l'ouverture (réextraction de P3) : … : rien n'est ouvert »),
   rien d'ouvert ni de poussé ; passé : une ligne au journal ; tout le reste
   lit hors ligne ; empreinte canonique de la configuration par `lecture_v4 empreinte-config` (brouillon 6 ; `lecture_v2` au
   brouillon 5, qui refuse la v7).
9. **`CODE-T07`** (vingt-six modules au brouillon 6) : `python -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md` (commit cité ancêtre de la
   tête, fichiers du module importé égaux à la liste, tout `src/controle_ia/` égal au commit cité et arbre de travail propre,
   DF-02 ; `PYTHONDONTWRITEBYTECODE=1`) ; non conforme → arrêt ; le même contrôle est rejoué par la garde du repli, la passe à
   blanc et l'étape A.
10. **Branche neuve** (absente du distant, sinon arrêt R12) ; poussées par chemins explicites : **légers d'abord** (aucun fichier
    de plus de 90 000 000 octets dans l'index), puis chaque fichier plus lourd **découpé** (`split -b 50000000`, morceaux scellés,
    recomposition vérifiée contre le fichier et son compagnon, manifeste `<fichier>.morceaux.json` scellé, original déplacé hors
    du dépôt), poussé par lots de 10 morceaux (O-2).
11. **Repli** (`lecture_v4 repli-seul`, brouillon 6 ; `lecture_v2` au brouillon 5 ; DF-01 ; `repli-recalcul`, refusé par la
    v4 (code 2), n'est jamais appelé) : **garde d'ouverture de l'étape A d'abord** (journalisée ; refus → code 2, rien
    n'est calculé, l'instance s'arrête ; cette ouverture **ferme le périmètre des jeux**, C-1) ; puis recalcul **sous un nom
    daté**, identité à dose 0, rejeu en forçage, garde d'équivalence ; réussite → `activations/`, rapport scellé à côté ; code 3
    (R11) → **une** relance sous un nom daté neuf ; second échec → nœud ; poussée « garde, repli ».
12. **Passe à blanc** : `lecture_v4 passe-blanc` (brouillon 6 : `passe_blanc_v2`, configuration v7 ; `lecture_v2` au brouillon 5 ;
    **brouillon 7** : **contrôle avant l'ouverture**, CLP3-03, `reextraction_p3_v1.controler_avant_ouverture`, joué juste après
    le contrôle de configuration et avant tout calcul : sceaux des quatre entrées de P3, principales de P3 égales à la
    configuration, témoin, directions de P3 et graine de la seconde garde, révision du modèle de P3 au cache lue hors ligne ; une
    faute refuse la passe, code 2, rien d'écrit, et l'étape A ne part pas ; le résultat est écrit dans la sortie de la passe à
    blanc, lisible par la fille, § 2.5 ; rapport v2, § 4) (`CODE-T07` d'abord ; mémoire de la notation jugée) ; sortie poussée quelle que
    soit son issue ; code ≠ 0 → arrêt, l'étape A ne part pas.
13. **Étape A** : `lecture_v4 etape-a-apres-repli` (brouillon 6 ; `lecture_v2` au brouillon 5), lancée avec
    **`CUBLAS_WORKSPACE_CONFIG=:4096:8` exporté pour ce processus** (le module le pose aussi par `setdefault` avant tout calcul
    sur la carte) et, sur un hôte dont le processeur n'est pas un EPYC (`/proc/cpuinfo`, écrit au journal), avec
    `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` (**non éprouvé, déclaré**) ; **réextraction des jetons d'entraînement des deux
    sondes figées de P3 avant toute autre extraction** (réglages de P3, modèle de P3 au cache local, gardes d'identité,
    800 directions neuves ; `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés et poussés avec les sorties ; un
    bras arrêté n'arrête pas l'étape A : texte de T0.7, liste d'arrêt) ; planchers notés par lots (`plancher_v3`) ; **brouillon 7** : une faute de calcul de la réextraction (`MemoryError`,
    `TypeError`, `AttributeError`, `IndexError`) arrête le seul bras (note 07) ; `etape-a-apres-repli` affiche l'état du
    plancher de chaque sonde figée, « établi » ou « échec », sans aire ni score (note 10) ; **brouillon 8** (CLC-P3-04) : la première ligne de
    `etape-a.txt`, écrite au journal par le script (chemin des scores, sondes lues, état des bras ; aucun score), est rapportée
    par la fille (§ 8) ; un bras arrêté (« échec ») dont le **motif ne commence pas par `GardeArret`**
    (`diag/<run-t07>/reextraction-p3-t07.json`, `par_sonde`, champs `etat` et `motif` ; motif d'un bras seul : `<type> : …` ;
    arrêt des deux bras : `réextraction impossible : <type> : …`, qui ne commence donc jamais par `GardeArret`) est un **arrêt
    technique** (texte de T0.7, liste d'arrêt) : la mère lit ces deux seuls champs après l'étape A (aucun score, aucune aire,
    aucun écart), écrit la réserve et revient à Lazar (nœud, R4) avant toute étape B (rapport du
    repli relu et couvrant ; garde d'ouverture rejouée, `CODE-T07`
    comprise ; garde d'identité remplacée par la garde d'équivalence) ; sorties, registre (`SCORES-T07`, `SONDES-T07`) et journal
    des ouvertures poussés (légers, puis morceaux) ; code ≠ 0 → nœud, aucune relance sous ce texte ; `lecture-sondes-t06.json`
    absent de l'arbre (contrôlé) ; `FIN` ; « stopped » demandé ; la fille détruit.

## 5 bis. Taille des sorties de l'étape A (O-2), calcul fait par le script avant toute ouverture

Borne haute, nombres en `float64`, `np.savez` sans compression ; entrées lues sur l'instance sans rien ouvrir de décisif :
`n` = actions notées (`jetons_notes > 0` de `mesures-t06.npz` de 7b, sceau vérifié), `s` = octets des clés d'une action (`cle`,
`condition`, `tache`, `pas`), `d` = largeur des activations (en-tête du premier morceau du sous-ensemble de 7b, sceau vérifié),
`P` = `n_plancher`, `couches`, `L` = sondes lues au plus, `K` = concepts neufs appris (`JD`, `JC` du périmètre), `p6` = 1 si `JA`
et `JC` sont au périmètre, `C` = concepts des phrases (si `CONCEPTS` est au périmètre), `D` = `C × couches` :

- `F = L(1+P) + 8·couches + 5·couches·K + 2·p6·(1+P) + D(1+P) + K + 1` nombres par action ;
- `scores-actions-t07.npz` ≤ `n × (8F + s) + 5·10⁶` octets ;
- `sondes-neuves-t07.npz` ≤ `8 × [couches·K·(d²+d) + couches·K·(22d+64) + 2·p6·(d²+d) + (K+2·p6)·P·2d + D·d] + 5·10⁶` ;
- autres sorties : 5·10⁷ ; **total ≤ 2·10⁹ octets** (`BORNE`), sinon arrêt de code 2 avant toute ouverture (nœud) ;
- fichier de plus de 9·10⁷ octets (`SEUIL`) : morceaux de 5·10⁷ (`MORCEAU`), lots de 10 (`LOT`) ; nombre de morceaux prévu écrit
  dans `taille-estimee.json` (lisible par la fille, § 2.5).

Ordre de grandeur (non mesuré, pour juger la borne ; aucune donnée de 7b) : à `d` = 4 096, `couches` = 3, `P` = 200, `K` = 2,
`p6` = 1, la part des sondes neuves est d'environ 1,1·10⁹ octets, dominée par les matrices `d × d` ; la marge restante sous la
borne dépend de `n`, inconnu avant 7b. Un dépassement arrête l'instance après les paquets et les essais (≈ 0,3 à 1,2 h payées),
avant le modèle : § 13, S-6.

**Brouillon 7** (S-13, script v3 ; rapport v2, § 5, point 6) : la borne compte aussi `nf × n_p3` nombres par action (directions
de P3 notées en descriptif ; `nf` sondes figées nommées) et `planchers-figees-t07.npz` (`nf × P × 8 × (d + 1) + 2·10⁶` octets),
écrits dans `taille-estimee.json` ; ordre de grandeur réel (non mesuré ; `d` = 4 096, `couches` = 3, `P` = 800, `K` = 2,
`p6` = 1, `C` = 2, `L` = 4, `nf` = 2, `n_p3` = 200, ≈ 5 760 actions) : **≈ 1,87·10⁹ octets, sous la borne de 2·10⁹** (marge
≈ 0,13·10⁹ ; à `n` plus grand d'environ 30 %, la borne arrête avant toute ouverture, code 2).

**Brouillon 8** (CLC-P3-07 ; R-2314 (4)) : la marge de la borne correspond à environ **7 378 actions notées** au plus ; la mère ne
compte pas `n` : elle lit sur processeur, avant la création, le seul **nombre de lignes** des mesures de 7b (forme du tableau,
un entier ; aucune colonne lue), qui majore `n` (P14), et ne crée pas au-delà.

## 6. Devis de la variante B (A100, essais, recalcul des activations puis étape A) et dépense

| Phase | Attendu (h) | Pire cas (h) | Source |
|---|---|---|---|
| Création, démarrage, image | 0,10 | 0,30 | E2 (R-1689 : démarrage en file 17 min) |
| Clone partiel, registres, sortie de 7b | 0,10 | 0,45 | E2 (R-1687) ; borne du clonage de l'amorce de T0.6 (900 s) ; clone de la mesure : 104 Mo extraits (§ 11 bis) |
| Paquets (`requirements-gpu.txt`) | 0,15 | 0,50 | amorce de T0.6 (installation bornée à 3 600 s) ; **supposé** |
| Essais de T0.7 (17 fichiers) | 0,25 | 0,60 | **mesuré** : 716,0 s dans le clone de la mesure (§ 11 bis), machine partagée |
| Taille bornée | 0,01 | 0,05 | lecture de deux en-têtes |
| Modèle (≈ 16 Go) | 0,10 | 1,00 | `inet_down` ≥ 500 Mb/s : ≈ 0,07 h ; pire : débit dix fois plus bas |
| Repli : recalcul et garde d'équivalence | 0,10 | 0,40 | brouillon 19 : 576 épisodes × 0,45 s ≈ 0,07 h ; écriture de 31,5 Go ; une relance R11 au pire |
| Passe à blanc | 0,10 | 0,20 | estimation de la passe (échantillon) |
| Étape A | 2,00 à 3,50 | 4,00 à 7,00 | brouillon 19, « Calcul et dépense » ; pire : hôte deux fois plus lent |
| Poussées (légers, morceaux) | 0,10 | 0,40 | sorties ≤ 2 Go (borne du § 5 bis), lots de 500 Mo |
| **Brouillon 6** : réextraction de P3 (modèle de P3 au cache, extraction des 2 069 exemples d'entraînement à la couche 15, témoins et principale refaits, seconde garde, 800 directions par sonde figée) | 0,12 | 0,29 | rapport du code du plancher v3 (`cb31edc8…`), § 8 ; R-679 (extraction en 78,5 s) |
| **Brouillon 6** : notation des planchers par lots (≈ 12,5 planchers de 800 directions, ≈ 1,3 million de jetons par couche) et contrôle en ligne | 0,09 | 0,32 | id., § 4 et § 8 (mesuré sur quatre cœurs, mise à l'échelle supposée linéaire) |
| **Brouillon 6** : poussée des scores en plus (≈ 0,46 Go) | 0,02 | 0,05 | id., § 8 |
| **Total** | **3,2 à 4,7** (3,0 à 4,5 au brouillon 5) | **8,6 à 11,6** (7,9 à 10,9 au brouillon 5 ; 11,56 h au pire exact) | + 0,23 h attendu, + 0,66 h au pire (rapport, § 8 ; rien retiré au devis) |

- **Coût** (≤ 1,30 USD de l'heure, carte et disque de 100 Go compris dans `dph_total`) : attendu **≈ 4,2 à 6,1 USD** (brouillon 6 ; 3,9 à 5,9
  au brouillon 5) ; pire cas ≈ 11,1 à 15,0 USD (10,3 à 14,2 au brouillon 5) ; plus le téléchargement, borné à 24 Go × 0,05 USD = **1,20 USD**, et le disque après l'arrêt jusqu'à la
  destruction (≤ 0,08 USD de l'heure, ≤ 1 h). **Attendu ≈ 5,5 à 7,4 USD ; pire cas ≈ 12,5 à 16,4 USD** (brouillon 6 : devis du brouillon 5, ≈ 5,2 à 7,1 et ≈ 11,6 à 15,5 USD, plus 0,30 USD attendu et 0,86 USD au pire, rapport du code, § 8, arrondis vers le haut ; calcul direct : 5,5 à 7,4 et 12,4 à 16,3 USD) : **sous 20 USD**.
- **Plafond** : **20 USD sous GO-2026-11-10-04 et GO-2026-11-10-06 ensemble** (O-4 ; `PLAF`, ligne (A)) : la part disponible
  pour cette instance est `20 − ANT0` ; P8 exige qu'elle couvre le pire cas (`ANT0` ≤ 3,6 USD au brouillon 6 ; 4,5 USD au brouillon 5). La minuterie est bornée par
  `HMAX` (§ 4.4) : si le `DELETE` de la minuterie aboutit (jamais répété avec la clé d'une instance réelle, O-3), la carte ne dépasse pas `20 − ANT0 − 1,30` tant que le conteneur vit ; s'il échoue cinq fois, ou après l'état « stopped » (disque ≤ 0,08 USD de l'heure, sans minuterie), le plafond ne tient que par la destruction faite par la fille (§ 4.7) ou, si sa session est tombée, par la mère au rappel de `ECH` (§ 4.4) : à `ANT0` = 0 et 1,30 USD de l'heure, la marge à `ECH` est de 3,2 USD (2,4 h de carte ou 40 h de disque) ; à `ANT0` = 3,6 USD (borne de P8 au brouillon 6), de 0,1 USD (au brouillon 5 : à `ANT0` = 4,5 USD).
- **Relevé** : bloc du § 4.5 (`PRIX_H` = `prix_h` du § 4.3, `ANT0` sous les deux lignes) ; **compte rendu** à Lazar à 10 USD
  (aucun arrêt) ; **arrêt** dès que le cumul plus un quart d'heure de carte atteint `PLAF` : destruction par l'identifiant
  (§ 4.7), nœud, aucune relance sans un mot de Lazar sur un devis neuf. La facture, si connue, fait foi. Dépense inscrite sous
  `GO` (la mère vérifie la somme sous les deux lignes).

## 7. Arrêts

- Préalable manquant, empreinte différente, chemin interdit ou de 7a cité par un registre, `ATT` non valable pour S7 sans
  remesure, recherche vide, création incertaine : rien n'est créé (ou plus rien) ; compte rendu.
- Ligne `ARRET` du script : **code 2 avant la branche** (machine, code, registres, périmètre, sortie de 7b, environnement,
  **essais** — ligne différente de `ATT` : après les paquets, avant le modèle —, **taille au-dessus de la borne**, modèle,
  `CODE-T07`, branche présente) : rien d'ouvert, rien de poussé ; **code 3** (refus de la garde au repli, repli après relance,
  passe à blanc, découpage, étape A) : traces poussées si la branche existe. **CLC-08** : un repli en code 2 est journalisé
  « ligne manquante : attente » **quel que soit son motif** ; la fille lit d'abord la première ligne de
  `traces/t07-etape-a-b-v1/repli-<n>.err` sur la branche poussée (motif du refus, sans donnée décisive) ; une création neuve
  n'a lieu que sur un écrit de la mère (même GO, devis inchangé), quand la cause est levée, **et après que la mère a recopié à l'octet, dans le journal des ouvertures de `main`, toute ligne `OUVERTURE-T07` ou `REFUS-T07` poussée par l'instance arrêtée** (texte de T0.7, « Accord au code », point 19 : sans elle, la relance fixerait un autre instant de fermeture) ; `PER` de la relance se recalcule au § 4.1, et le module écarte de lui-même une ligne de jeu postérieure à cette première ouverture. **Instance perdue (hôte, minuterie) entre la ligne « CODE-T07 conforme » et la poussée « garde, repli »** : la ligne d'ouverture a pu être écrite sans être poussée ; nœud, aucune relance sans un écrit de la mère qui fixe l'instant de fermeture. Dans tous les cas : la fille relève la
  ligne, vérifie ce qui est poussé (§ 4.6), **détruit** (§ 4.7), compte rendu, nœud de la mère.
- **Brouillon 8** : contrôle avant l'ouverture en échec à l'étape 8 (code 2) : rien n'est ouvert ni poussé ; la fille détruit
  (§ 4.7), compte rendu ; création neuve sur un écrit de la mère quand la cause est levée. **Arrêt technique d'un bras**
  (CLC-P3-04 ; § 5, étape 13) : l'étape A va au bout ; la mère écrit la réserve et revient à Lazar (nœud, R4) avant toute
  étape B. P14 non tenu (plus d'environ 7 378 lignes aux mesures de 7b) : aucune création, nœud.
- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.
- **Réserve CLE-12** (acceptée par la mère, R-2258 ; dite à Lazar comme information) : une minuterie qui tombe pendant l'étape A
  détruit une étape ouverte : nœud de dépense (écrit (b) 6 de T0.7), relance seulement sur un mot de Lazar. La marge entre le
  pire cas du devis (**11,56 h**, § 6 ; brouillon 6) et 12 h est d'environ **0,45 h** (**aggravée** au brouillon 6 par la
  réextraction et la notation des planchers à 800 directions, R-2304 ; 1,1 h au brouillon 5 ; moins quand `HMAX` < 12 h, § 4.4 :
  à `ANT0` = 3,6 USD et 1,30 USD de l'heure, `HMAX` ≈ 11,6 h, marge ≈ 0,05 h) ; la durée réelle de l'étape A
  **n'a jamais été mesurée** (la passe à blanc n'estime que l'extraction). Allonger la minuterie dépasserait le plafond de
  20 USD fixé par Lazar.

## 8. Compte rendu de la fille (nombres seuls, ≤ 400 mots)

`vastai --version` ; P1 à P12 (valeurs ; `PER` ; `ANT0` sous les deux lignes ; « ATT valable pour S7 ») ; recherche (offre, prix,
cuda) ; identifiant, `TC`, `HMAX`, `ECH` ; lignes `T07` (machine, code, registres, périmètre, sortie de 7b, **essais : code et
ligne**, **taille estimée : octets et morceaux prévus**, disque libre, modèle, configuration, `CODE-T07`, repli : actions et écart
maximal de la garde, passe à blanc : issue, frontière, mémoire, durée estimée, étape A : code et run, **état des bras de la réextraction** (« établi » ou « échec », ligne du journal ; brouillon 8),
**contrôle avant l'ouverture de l'étape 8** (passé ou motif ; brouillon 8),
**morceaux poussés**, fin et
code HTTP de « stopped ») ; tête de la branche, commits, `OK` / `ÉCART` (fichiers légers et manifestes de morceaux) ; dépense
relevée ; destruction, inventaire final ; écarts. **Ni score, ni aire, ni contenu des sorties de l'étape A.** Journal (garde des
secrets à 0) envoyé à la mère.

## 9. Ce qui suit, et ce que cet ordre ne fait pas

- **Suite (mère)** : recopier **à l'octet**, dans le registre et le journal des ouvertures de `main`, les lignes `SCORES-T07`,
  `SONDES-T07` et `OUVERTURE-T07` écrites sur l'instance, après avoir vérifié que le journal de P3-bis de `main` ne porte aucune
  ligne datée avant la fin de l'étape A qui manquait à la copie de l'instance (sinon nœud ; G2, G4) ; inscrire la dépense et
  vérifier la somme sous GO-2026-11-10-04 et GO-2026-11-10-06 ; rappel daté à `ECH` levé.
- **Avant l'étape B** (son propre ordre) : pour chaque fichier découpé, recomposition par la commande écrite dans son manifeste
  (`cat <fichier>.morceau-[0-9][0-9][0-9] > <fichier> && sha256sum -c <fichier>.sha256`), chaque morceau à l'empreinte de son
  compagnon, empreinte du fichier recomposé égale à celle de la ligne `SCORES-T07` ou `SONDES-T07` (sans rien ouvrir d'autre) ;
  **C-4** : étape B jouée à S7 (tête détachée ; brouillon 6 : `lecture_v4 etape-b` seule, la v2 et la v3 refusent la v7 ; brouillon 7 :
  l'étape B exige de chaque sonde notée un plancher décisif de `n_plancher` directions, tableau et nombre écrit, sinon arrêt,
  note 05 ; la v4 refuse aussi la v7), `PYTHONDONTWRITEBYTECODE=1`, arbre propre (`CODE-T07` contrôlée aux deux étapes).
- **Ne fait pas** : aucun épisode ; aucune étape B ; aucune lecture de sortie ; aucune modification du code, du texte, de la
  configuration ou de la chaîne de T0.6 ; aucune fusion ; aucune écriture sur `main` ; aucun contact externe ni appel de modèle ;
  aucune H200.

## 10. Jugés par la contre-lecture R2 du brouillon 4 (`88ea9f06…`)

Issues (contre-lecture, § 1 à § 6 ; décisions de la mère, R-2258) : aucun constat bloquant ; CLE-01 à CLE-08, CLE-10 et CLE-11
appliqués par les couples 1 à 12 ; CLE-09 relève du candidat de T0.7 (aucun couple dans cet ordre) ; **CLE-12 accepté avec
réserve** (§ 7). Points tels qu'ils étaient soumis :

1. La ligne `GO-LECTURE-T07` pour cette instance (variante B), dont l'extrait cite GO-2026-11-10-06 ; la borne `HMAX` de la
   minuterie (O-4) et l'exigence `ANT0` ≤ 4,5 USD (P8) contre le plafond commun de 20 USD.
2. `ATT` : mesurée sous Python 3.13.16 et le paquet local (§ 11 bis), **retrouvée sous Python 3.11.17** par la contre-lecture
   (même ligne, § 11 bis) ; l'instance joue Python 3.11 et `requirements-gpu.txt`
   (mêmes versions figées de `numpy`, `scipy`, `pytest`, `torch` en construction carte) ; conditions de validité de P12 ; risque
   résiduel § 13, S-2.
3. P10 : lecture stricte de la ligne d'arrêt corrigée (CLO-08) pour la variante B : **toute** instance `t06…` ou `t07…` bloque la
   création, celle de 7b comprise (« autre que celle de 7b » ne vaut que pour l'étape annexe sur l'instance de 7b, abandonnée).
4. P3 : la mère décide avant la création d'attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07` ; la garde du
   repli ferme le périmètre avant tout recalcul (C-1).
5. Borne de taille (§ 5 bis) et seuils de découpage : proposés par le script, non confrontés à une sortie réelle.
6. Lecture des manifestes de morceaux (tailles, noms) par la fille, et du motif d'un `repli-<n>.err` (§ 2.5).
7. Seuil de compte rendu (10 USD) et marge d'un quart d'heure : proposés.

## 11. Répétitions du script de l'instance (mode jouet)

Le script v1 a été répété au brouillon 3 (`99e4c926…`, trois passages). Le **script v2** (`e68d3306…`) est répété par
`scripts/repetition_jouet_variante_b_t07_v2.py` (rapport complémentaire 5, § 5, passage 4, 12:08 à 12:17 UTC, commit `16f59d63` :
**douze verdicts conformes** — normal (`PERIMETRE=JD,JA,JC,CONCEPTS`) code 0 ; « sans concepts » (`PERIMETRE=JD,JA,JC`, ligne
absente de `main`) code 0, phrases non lues ; branche déjà poussée → code 2 ; périmètre faux → code 2 avant tout repli ; mesure
« 20 passed » ; découpage O-2 en morceaux scellés, recomposition égale ; minuterie saine (« HTTP 200 ») et en échec (cinq
« HTTP 500 », destruction laissée à la session)) ; **rejoué** par la contre-lecture courte de l'option (c) (`7a327462…`, § 2 :
12 verdicts conformes ; artefact du contre-lecteur : script sans `registres/go.md` → refus de la garde du repli). Non répétés
(réel seulement) : Vast, paquets, modèle, carte, `DELETE` avec la clé de l'instance. **Pas de répétition neuve dans ce
brouillon** (la consigne ne la demande pas ; le script est inchangé). **Brouillon 6** : le script v3 (§ 13, S-12) est à répéter en jouet (même répétition, configuration v7, commandes `lecture_v4`, un bras de réextraction établi et un bras arrêté) avant que la mère remplisse `SHA_SCRIPT_V3_T07` ; non fait ici. **Brouillon 7** : **fait** par le développeur du code (`scripts/repetition_jouet_variante_b_t07_v3.py`, `d8dde1fb104ee2e61083f13dde226ef05341b33b6518f8aebe0bb93f20c34ce9`, commit `68882c2d` ; passage du 2026-11-11 de 03:34:57 à 03:53:24 UTC, configuration v8 jouet ; journal `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v3-journal.txt` (`3d1421e72a7484566866e3a2169a7f00c5849f6a78ee936586e19a3e6d108b72`) et résumé `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v3-resume.json` (`691b98cfb3eb474b947376de69ece37dc0a178596b8aed14ffbe7b8d99e69529`), scellés) : **17 verdicts sur 17 conformes** — les douze de la v2 et cinq neufs (deux bras établis ; un bras arrêté par la garde d'identité, l'étape A au bout ; journal du v3 : `CUBLAS_WORKSPACE_CONFIG`, processeur, révision de P3 ; taille comptant les planchers des figées ; contrôle avant l'ouverture à la passe à blanc) ; constat : sur un processeur non EPYC, `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` mettent, en jouet sur processeur, les gardes au palier « processeur » (en réel, la passe avant tourne sur la carte) ; marqueur `SHA_SCRIPT_V3_T07` rempli (ligne (A)). **Brouillon 8** : répétition jouet **v4** (`scripts/repetition_jouet_variante_b_t07_v4.py`, `8b0e9590befafef97d96450def60138e6c835df90ee5ecf7e00a608f373737ba`, commit `be3191c9` ; passage du 2026-11-11 de 04:41:45 à 04:44:39 UTC ; journal `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v4-journal.txt` (`98412f28c9d0dc446db86d73d51e1aa1ae3615545d242b5478e8de8bb9fb265c`) et résumé `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/repetition-jouet-v4-resume.json` (`c36839fe2016ccea200ee5fa28c7a7116f457821d576ee93b88fbfb4d4b4f2e2`), scellés) : **10 verdicts sur 10** — passage normal (processeur Intel : contrôle de l'étape 8 avant l'empreinte, `CODE-T07`, le repli, la passe à blanc et l'étape A ; `CUBLAS_WORKSPACE_CONFIG` lu dans le processus), passage EPYC (`CPU_ESSAI` ; tableau `ENV_CPU` vide sous `set -u`), artefact « témoin retiré » (code 2 à l'étape 8 : ni empreinte, ni `CODE-T07`, ni branche, ni repli, ni ouverture), branche déjà poussée (code 2 après le contrôle, sans repli), découpage, `CPU_ESSAI` refusée hors essai ; la ligne (A) porte le v4.

## 11 bis. Mesure de `ATT` dans un clone fait comme celui de l'instance (O-1)

- **Quand, où** : le 2026-11-10, de 15:17:26 (clone) à 15:29:36 (fin des essais) UTC (`date -u`), dans le bac à sable du sous-agent, après la partie 1 de la
  consigne (essai GARDES-CODE-01 commité et poussé), **sur la branche `prep/t07-essai-degeneres-v1`**, tête
  `2c8ab779ca6df361d562e120ba34045be675853a` (partie de `06deda58` de `main` ; seul ajout : `tests/test_t07_tirages_degeneres_v1.py`).
- **Méthode** : script de mesure du sous-agent (bac à sable, non versé ; empreinte `98beca19097036d64fbec4f6779183f0e899afe9c21f6ba755164b6324b3aec1`), qui recopie **les étapes 2,
  3 et 6 du script v2** : `git clone -q --filter=blob:none --no-checkout --single-branch --branch <branche> https://github.com/lciric/controle-ia-travail.git`
  (clone partiel à branche unique : seuls les objets atteignables depuis la branche) ; mêmes motifs d'extraction partielle,
  mêmes registres nommés, mêmes chemins cités par la configuration (v4 : `diag/20261019-230011-p3-reel/sondes-figees.json`, `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `donnees/T0.7-faits-repe-v1/facts_true_false.csv`, `donnees/T0.7-models-under-pressure-v1/training/train.jsonl`, `runs/20261019-230011-p3-reel/manifeste.json`) ; tête au commit mesuré ; registres
  recopiés et fichiers qu'ils citent (`donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`, `…/intention-autres-modes-v2.jsonl`,
  `prereg/T0.8-base-A-mots-et-cout-v1.md`) ; périmètre `JD,JA` (journaux du script : un par jeu, recopiés) ; puis, depuis le
  dépôt, `TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -rsxX -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp=<bac>/essais-tmp -o tmp_path_retention_policy=failed`,
  dernière ligne, durée retirée (`sed -E 's/ in [0-9.]+s.*$//'`).
- **Écarts à l'instance, déclarés** : branche mesurée au lieu de `main` (S7 = C7 = H = sa tête ; même atteignabilité que `main` à
  `06deda58`, plus l'essai) ; étape 4 (sortie de 7b) et étape 5 (paquets) non jouées (aucune course 7b ; interpréteur local
  **Python 3.13.16**, `numpy` 2.4.6, `scipy` 1.17.1, `pytest` 9.1.1, `torch` 2.14.1 en construction processeur, contre Python 3.11
  et `requirements-gpu.txt` sur l'instance) ; aucun jeton posé (le mandataire de la session porte l'accès) ; registres de `main` à
  `06deda58` (les lignes inscrites plus tard ajoutent des fichiers cités ; aucun essai de T0.7 ne lit le registre de `main`).
- **Résultat** : code 0, **`ATT` = `346 passed, 2 skipped, 4 xfailed`** (17 fichiers ; durée 716,0 s). Sauts et échecs attendus, nommés :
  - sautés (2) : `tests/test_t07_lecture_v1.py:504` (branche `origin/prep/t06-candidat8-v1` non récupérée, déclaré) ;
    `tests/test_t07_lecture_v2.py:911` (commit `061ac380` absent du clone, déclaré) — les deux tiennent au clone à branche unique,
    comme sur l'instance (O-1) ;
  - échecs attendus (4) : `test_CT01_action_sans_caractere_de_mot_temoin_en_echec_sans_arret` et
    `test_CT11_dates_du_journal_non_decroissantes` (`tests/test_t07_corrections_cl1_v1.py`),
    `test_journal_cas_sain_lignes_et_refus_lus` (`tests/test_t07_lecture_v2.py`), `test_garde_refusee_rien_calcule_puis_relance`
    (`tests/test_t07_repli_etapes_v1.py`) ;
  - **l'essai du miroir de `familles_v2` passe** (`8cb539f9` atteignable depuis la branche, donc depuis `main` à `06deda58` :
    fusion « ours », R-2229 ; CLC-03 levé) ; les essais du repli passent (`docs/sources/invites-2606.08892-v1/` extrait) ;
  - compte recoupé : 344 essais dans les quinze fichiers de `37485ce5` (CLO-04), plus 3 de l'essai CLC-04 et 5 de l'essai
    GARDES-CODE-01 = 352 = 346 + 2 + 4 ; aucun avertissement dans la ligne ; `essais.err` vide ; `src/` et `tests/` non écrits ;
  - pièces (bac à sable, non versées, empreintes relevées avant suppression) : `essais.txt` `2b506a189c696b4f4aad86cdc26a7fc2e36c3b95863c3916831ac351c83947b1`,
    `essais-liste.txt` (17 fichiers et leurs empreintes) `bd49a36795b15228a9cfde88b411b98ae842223e35fbb75e57eebe04dcb26415`,
    journal de la mesure `d15f94b8622c3d4c3bce542738329810f2ad001e91104975bdbd493192cb7a6b`.
- **Mesure de la contre-lecture R2 sous Python 3.11.17** (`88ea9f06…`, § 3 ; de 15:46:49 à 16:03:50 UTC, heures qu'elle
  rapporte) : clone `--shared` du dépôt local aux motifs des étapes 2 et 3 du script, tête `709d16fc` (arbres `tests/`
  `79230a58…` et `src/` `744a9e16…`), versions figées de `requirements-cpu.txt` (`torch` 2.14.1 en construction processeur),
  commande exacte de l'étape 6 : **code 0, `346 passed, 2 skipped, 4 xfailed`** (1 019,6 s), mêmes deux sauts et mêmes quatre
  échecs attendus, aucun avertissement, liste des essais `bd49a367…` égale à celle de la mesure ci-dessus. Les deux mesures se
  complètent (atteignabilité depuis une seule branche : la première ; interpréteur de l'instance : la seconde) ; aucune ne joue
  la construction carte de `torch` ni le git de l'image (S-1, S-2).
- **Brouillon 8** (R-2313) : la suite `tests/test_t07_*` **entière** est rejouée par la mère à C7 (au commit final `a621dcd3`,
  elle a été arrêtée à 29 % faute de disque, sans échec ; `tests/test_t07_plancher_v3_*` y passent, 92 sur 92) ; sa dernière
  ligne, durée retirée, est la valeur du marqueur `ATT_C7_T07` (P12, couple VC3-C).
- **Brouillon 7** (R-2306) : `ATT` se **mesure à C7**, avant la création, par la commande ci-dessous, la tête au commit C7 au
  lieu de S7 (S7 en hérite par P9) ; la valeur va au marqueur `ATT_C7_T07` de la ligne (A) ; la mesure ci-dessus (brouillon 5)
  ne vaut plus (cinq fichiers d'essais neufs ; rapport v2, § 7 : 530 passés, 23 sautés, 3 `xfail` dans l'arbre du développeur,
  extraction réduite, non comparable).
- **Commande de remesure** (si P12 échoue) : la même, avec `--branch main` et la tête au commit S7 (méthode exacte du script :
  `ESSAI_LOCAL=1 ARRET_APRES_ESSAIS=1` ne peut pas tourner sans course 7b ni dépôt local dont `main` porte S7), soit, depuis un
  dossier neuf : `git clone -q --filter=blob:none --no-checkout --single-branch --branch main https://github.com/lciric/controle-ia-travail.git d && git -C d sparse-checkout init --no-cone`,
  motifs de l'étape 2 du script v2 (l. 102-131 : `REGISTRES`, `MOTIFS`, `NOMMES`, `CITES` tirés de `CFG` à S7) passés à
  `git -C d sparse-checkout set --no-cone --stdin` (l. 132), `git -C d checkout -q <S7>`, recopie des registres nommés et des fichiers
  qu'ils citent, journaux du script des jeux (étape 3, l. 141-166, hors chemins de 7a), puis la commande pytest ci-dessus depuis `d`.

## 12. Marqueurs (à remplir par la mère ; une occurrence chacun)

Remplis à ce brouillon : `GO_VARIANTE_B_T07` = **GO-2026-11-10-06** (R-2115) ; le plafond, **20 USD**, est celui de cette ligne,
commun avec GO-2026-11-10-04 (`PLAF`) ; **`LIGNE_ESSAIS_T07`** = `ATT` mesurée (§ 11 bis), valable sous P12.

| Marqueur (sans chevrons) | Où | Valeur |
|---|---|---|
| `ID_SESSION_FILLE` | en-tête | identifiant de la session fille |
| `EMPREINTE_CONFIG_T07` | § 1 | empreinte canonique de la configuration de T0.7 scellée |
| `LIGNE_SCELLEMENT_T07` | § 3 | la ligne `SCELLEMENT-T07` exacte |
| `DEPENSE_ANTERIEURE_USD` | ligne (A) | dépense déjà inscrite sous GO-2026-11-10-04 **et** GO-2026-11-10-06 (attendu `0`) |
| `RUN_T06_7B` | ligne (A) | run de 7b |
| `BRANCHE_7B` | ligne (A) | branche poussée par 7b (`calcul/t06-confirmation-7b-v1`, ou suivante) |
| `COMMIT_CODE_T07` | ligne (A) | C7 (R-2231) |
| `COMMIT_SCELLEMENT_T07` | ligne (A) | S7 |
| `CHEMIN_CONFIG_T07` | ligne (A) | chemin de la configuration scellée dans S7 |
| `PERIMETRE_T07` | ligne (A) | lignes de jeux et de concepts présentes à `main` à la création (`JD,JA` à l'écriture de cet ordre), ou `aucun` |
| `SHA_SCRIPT_V3_T07` (**neuf au brouillon 6 ; rempli au brouillon 7**) | ligne (A) | sha256 de `scripts/etape_a_t07_variante_b_v3.sh` sur `main`, écrit, répété en jouet et contre-lu (§ 13, S-12) : **`a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560`** (commit `7e23a554`) ; **brouillon 8** : script v4, **`4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6`** (commit `a621dcd3`), à la ligne (A) |
| `ATT_C7_T07` (**neuf au brouillon 7**) | ligne (A) | ligne d'essais attendue (`ATT`), mesurée par la mère à C7 après la fusion du code (§ 11 bis, tête au commit C7) ; P12 |
| `COMMIT_SRC_CONTRE_LU_T07` (**neuf au brouillon 6**) | ligne (A) | **brouillon 7** (R-2306) : commit de `main` qui fusionne la branche finale du code du remède (a') (vingt-six modules ; à ce jour `7e23a554aca040016a08fe510504adec172c6998` sur `prep/t07-plancher-v3-v1`, non fusionnée ; **brouillon 8** : commit final `a621dcd3b929ce3ebd615fa852d4a7f5c103071d`, contre-lecture courte des corrections rendue, R-2311 ; la mère écrit l'égalité des arbres `src/`, P13 (iii) ; **brouillon 9** : `a621dcd3b929ce3ebd615fa852d4a7f5c103071d` est le dernier commit contre-lu, vérification finale, `26efc4df…`, R-2315) : `src/` de C7 égal à son arbre `src/` ; au brouillon 6 : dernier commit contre-lu du code du remède (a') (vingt-six modules ; à ce jour `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, non fusionné, contre-lecture en cours), dont `src/` est celui de C7 après fusion (R-2304) |

## 13. Constats sur le script v2 (non modifié ; correction proposée pour une v3, décision de la mère)

| id | gravité | constat | correction proposée (v3, décision de la mère) | ce que fait cet ordre en attendant |
|---|---|---|---|---|
| S-1 | à corriger si l'environnement change | L'étape 6 compare **toute** la dernière ligne de `pytest` (durée seule retirée) à `ATT` : un compte d'avertissements (« , 1 warning ») ou d'erreurs de collecte change la ligne sans changer les essais ; l'arrêt tombe après les paquets (≈ 0,2 à 0,7 h payées, ≤ 1 USD), avant le modèle. La mesure (Python 3.13) n'en a aucun. | retirer `, N warning(s)` avant la comparaison, ou comparer en plus la liste triée des essais non passés (`essais-sauts.txt`) à une liste scellée | `ATT` mesurée sans avertissement ; P12 ; écart → compte rendu, remesure, création neuve sur écrit de la mère |
| S-2 | risque résiduel, réduit | Mesure sous Python 3.13.16 (bac à sable), **retrouvée sous Python 3.11.17** par la contre-lecture R2 (§ 11 bis) ; l'instance joue Python 3.11 (image `python:3.11-bookworm`) et `requirements-gpu.txt` (mêmes versions figées, `torch` en construction carte). Restent la construction carte de `torch` et le git de l'image, qu'aucune mesure ne joue. | rien de plus avant le lancement (R-2255, R-2258) | déclaré (§ 10.2) |
| S-3 | à corriger | `interdit()` (l. 141) ne refuse pas un chemin de 7a (`20261109-070232-t06-reel`) cité par un registre ; aucun registre n'en cite aujourd'hui (trois lignes au commit `2c8ab779`). | ajouter `*20261109-070232-t06-reel*` au motif de `interdit()` | § 4.1 : compte des chemins interdits ou de 7a cités par un registre, `0` exigé avant la création |
| S-4 | mineur (CLC-08) | l. 362 : un repli en code 2 est journalisé « refus de la garde (ligne manquante : attente …) » quel que soit son motif. | libellé neutre : « refus de la garde (motif : repli-<n>.err) », ou première ligne du motif | § 7 : la fille lit le motif dans `repli-<n>.err` |
| S-5 | hors du script (concordance) | La ligne d'arrêt corrigée (CLO-08) et le filtre du § 4.2 ne regardent que les étiquettes `t06…` et `t07…` : une instance d'une autre tâche du programme **étiquetée** `t06…` ou `t07…` bloquerait la création (P10), à tort selon les écrits (b) 1 et 2. | aux rédacteurs des ordres de P3-bis, de T0.8 et du texte de validité : étiquettes hors de ces deux préfixes | P10 ; point ouvert pour la mère |
| S-6 | mineur | La borne de taille (étape 7) se calcule après les paquets et les essais ; un dépassement arrête après ≈ 0,3 à 1,2 h payées. La part des sondes neuves (matrices `d × d`) est d'environ 1,1·10⁹ octets à `d` = 4 096, `K` = 2, `p6` = 1 (§ 5 bis) : la marge sous 2·10⁹ dépend de `n`, inconnu avant 7b. | estimer avant l'étape 5 (un `pip install numpy==2.4.6` suffit à la lecture des deux en-têtes) ; ou relever la borne après un calcul de la mère sur les nombres de 7b | § 5 bis ; § 7 (code 2 avant le modèle) |
| S-7 | cosmétique | `essais-sauts.txt` porte deux fois certaines lignes `XFAIL` (résumé court de `-rsxX` et lignes de résultat). | sans effet sur la comparaison | rien |
| S-8 | réserve v3 (R-2258) | Les trois « T07 REFUS » (l. 27, 34, 42) sortent par `exit 2`, avant la minuterie, sans demander l'état « stopped », sans date : invisibles au filtre du § 4.5 d'origine. | dater, journaliser et demander « stopped » | § 4.5 (couples 6 et 7) |
| S-9 | réserve v3 (R-2258) | Après cinq `DELETE` en échec, la minuterie ne demande pas l'état « stopped » ; la carte continue. | demander « stopped » (voie que l'amorce de T0.6 emploie en fin de run) | § 6 (couple 4), § 4.7 |
| S-10 | réserve v3 (R-2258) | Sur un écart de la ligne d'essais, `essais.txt` n'est ni poussé ni journalisé : la fille ne voit que la ligne. | écrire au journal les lignes `SKIPPED`, `XFAIL`, `FAILED`, `ERROR` | remesure (§ 11 bis) |
| S-11 | réserve v3 (R-2258) | La garde du repli écrit `OUVERTURE-T07` au début de `repli-seul` ; la poussée ne vient qu'après le recalcul (l. 357-365) : une instance perdue dans l'intervalle emporte la ligne. | pousser le journal des ouvertures dès la garde | § 7 (couple 5) |
| **S-12** | **bloquant au brouillon 6** | Le v2 appelle `lecture_v2` aux lignes 302 (`empreinte-config`), 357 (`repli-seul`), 367 (`passe-blanc`) et 372 (`etape-a-apres-repli`) : avec la configuration v7, l'étape 8 s'arrête (« n_plancher 800 ≠ 200 », code 2, rien d'ouvert) ; aucune commande de la v4 n'est jouée. | **script v3** (`scripts/etape_a_t07_variante_b_v3.sh`, nom neuf, R12) : (1) les quatre appels → `controle_ia.t07.lecture_v4` ; (2) l'étape A lancée avec `CUBLAS_WORKSPACE_CONFIG=:4096:8` dans son environnement ; (3) le modèle et le nom du processeur (`/proc/cpuinfo`) écrits au journal ; hors EPYC, l'étape A lancée en plus avec `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` (non éprouvé) ; (4) étape 8 : si la révision de 7b n'est pas celle de P3 (`runs/20261019-230011-p3-reel/manifeste.json`, `config.agent`), préchargement de celle de P3 (échec → code 2) ; (5) `planchers-figees-t07.npz` et `reextraction-p3-t07.json` poussés avec les sorties (déjà sous `donnees/<run-t07>/` et `diag/<run-t07>/`) ; (6) S-1, S-3, S-4, S-8 à S-11 au choix de la mère ; répétition jouet (comme le v2, § 11) et contre-lecture courte avant que la mère remplisse `SHA_SCRIPT_V3_T07` | P9 et P13 : sans le v3, aucune création |
| **S-13** | mineur (brouillon 6) | La borne de taille (§ 5 bis) lit `P` = `n_plancher` de la v7 (800) mais ne compte ni `planchers-figees-t07.npz` (2 × 800 directions de largeur 4 096 en double précision ≈ 5,2·10⁷ octets, au-delà des 5·10⁷ « autres sorties ») ni les 2 × 200 directions de P3 notées en descriptif (≈ 400 nombres par action) ; à `d` = 4 096, `K` = 2, `p6` = 1, `C` = 2 et ≈ 5 760 actions notées : sondes neuves ≈ 1,29·10⁹, scores ≈ 0,45·10⁹, total ≈ 1,85·10⁹ octets, sous la borne de 2·10⁹ (marge ≈ 0,15·10⁹, au lieu d'environ 0,8·10⁹ à `P` = 200) | au v3 : ajouter `2·n_p3` à `F` et la taille de `planchers-figees-t07.npz` aux « autres sorties » | rien ; la borne reste de 2·10⁹ octets |
| **S-14** | réserve (brouillon 8, R-2313) | **bash antérieur à 4.4 non éprouvé** : la construction de bash 4.3 a été refusée par un classifieur de permissions (rapporté, non contourné, R-2313) ; les formes `${t[@]+"${t[@]}"}` du v4 (CLC-P3-05) reposent sur leur définition documentée ; le mutant s5 (forme du v3) survit sous bash 5.2, équivalent | aucune (réserve écrite, R-2313) | l'image de l'instance a un bash 5 : sans effet attendu |
| **S-15** | réserve (R-2313) | branche « autre révision » de l'étape 8 (préchargement de la révision de P3 quand elle n'est pas celle de 7b) non éprouvable hors ligne | — | P13 (i) la rend inattendue |
| **S-16** | réserve (R-2313) | un morceau de poids **tronqué non vide** passe le contrôle du cache (l'index ne porte pas de tailles) ; le chargement échouerait après l'ouverture : les deux bras arrêtés, motif écrit, aucune bascule | lire les en-têtes des fichiers de poids (non fait) | § 5, étape 13 (arrêt technique : nœud) |
| **S-17** | réserve (R-2313) | la suite `tests/test_t07_*` entière n'a pas été rejouée au commit final (arrêtée à 29 % faute de disque, sans échec ; `tests/test_t07_plancher_v3_*` : 92 passés) | la mère la rejoue entière à C7 (§ 11 bis) ; sa dernière ligne est `ATT` | P12 |

S-8 à S-11 viennent de la contre-lecture R2 (`88ea9f06…`, § 5). Aucun des onze ne bloque l'étape A ; tous restent en réserve pour
une v3 éventuelle (décision de la mère) ; **le script v2 (`e68d3306…`) reste celui de cet ordre** (R-2255, R-2258). **Brouillon 6** :
il ne l'est plus : **S-12 exige un v3** (configuration v7, commandes `lecture_v4`) ; S-1 à S-11 y restent proposés (décision
de la mère) ; S-13 est un constat du rédacteur du brouillon 6. **Brouillon 7** : **S-12 et S-13 sont réglés par le script v3**
(`a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560`, commit `7e23a554` ; rapport v2, § 5) ; S-1, S-3, S-4, S-8 à S-11 n'y sont pas appliqués (au
choix de la mère) ; S-2, S-5, S-6, S-7 inchangés. **Brouillon 8** : le script de cet ordre est le **v4** (`4b17d1f0…`, commit `a621dcd3`) :
S-12 et S-13 y restent réglés ; CLC-P3-02 (contrôle entier à l'étape 8) et CLC-P3-05 (formes sûres sous `set -u`) y sont réglés ;
S-14 à S-17 sont des réserves.

Sources : `scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`, lu en entier) ; ordre brouillon 3 (`b053a220…`) ; contre-lecture
courte v3 (`d0fe9053…`) ; rapport complémentaire 5 (`e58be6c9…`) ; contre-lecture courte de l'option (c) (`7a327462…`) ;
contre-lecture orchestrée du brouillon 22 (`47537dfa…`) ; brouillon 22 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`,
lu pour la liste d'arrêt l. 1897-1900 et le module l. 2427-2438 ; brouillon, non opposable : le texte qui fait foi est celui de la
ligne `SCELLEMENT-T07`) ; `registres/go.md` de `main` (GO-2026-11-10-04, GO-2026-11-10-06) ; `registres/decisions.md` de `main`
(R-2112, R-2115, R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249, R-2255, R-2258) ; contre-lecture R2 du brouillon 4
(`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`, `88ea9f06…`) et ses couples (`cf2e4c98…`) ; `registres/scellements-v1.md` au commit `2c8ab779`
(trois lignes : `SCELLEMENT-JEUX-T07-JD`, `SCELLEMENT-JEUX-T07-JA`, `SCELLEMENT-T08-BASE-A` ; une quatrième, `GEL-T08`, à `709d16fc` : son fichier est recopié sans effet, rejoué par la contre-lecture R2).
