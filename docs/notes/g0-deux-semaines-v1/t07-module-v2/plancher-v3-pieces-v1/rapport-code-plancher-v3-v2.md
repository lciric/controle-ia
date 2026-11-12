# Rapport du développeur : code du plancher v3 de T0.7 — v2 (corrections de la contre-lecture, configuration v8, script v3)

Écrit le 2026-11-11, de 03:21 à 04:03 UTC (heures relevées par `date -u`), par le développeur du plancher v3 (Claude Opus 5.5,
`claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur le message de la mère qui suit la
contre-lecture du code (`docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/contre-lecture-code-plancher-v3-v1.md`,
`32cbc637…`, compagnon vérifié par `sha256sum -c`) et les décisions **R-2305** et **R-2306** (`registres/decisions.md`, lues).
**Le rapport v1 (`rapport-code-plancher-v3-v1.md`, `cb31edc8…`) reste intact** ; cette v2 le remplace pour tout ce qu'elle
nomme ; le reste (§ 2 du code, § 4 de la notation, § 8 du devis) vaut tel que la v1 l'écrit, sauf mention. Mêmes interdits ;
aucune donnée de 7a, 7b, P3-bis ; aucun appel de modèle, aucune instance, aucune dépense. **Je reste exclu de tout rôle de lecteur
de P3-bis.** Fichiers non fusionnés ni scellés corrigés en place sur ma branche (écart à la lettre de R12, déclaré par R-2305).

## Verdict

**Corrections faites, éprouvées et poussées** sur `prep/t07-plancher-v3-v1`, **commit final `7e23a554aca040016a08fe510504adec172c6998`** (au-dessus de
`0d0c5da4` : `84da23aa` corrections, `68882c2d` script v3 et répétition v3, `7e23a554` essais).

- **CLP3-01** : palier « carte » resserré à **10⁻³ (témoin) et 10⁻² (directions)** ; **configuration v8**, empreinte canonique
  **`0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12`** (fichier `e31c7a79…`) ; `lecture_v4` admet la v8 et
  refuse la v7 (seuils) et la v6 (clé absente) ; réserve réécrite « écart au palier « carte », cause non établie » ; **calibrage
  rejoué (v3)** : **toutes les fautes calibrées sont arrêtées par le témoin**, **un bruit de 10⁻³ par jeton passe**.
- **Correction de la phrase du rapport v1** (§ 5) : la v1 écrivait que, « pour une faute de données, d'empan, de découpage ou de
  couche, la garde arrête » : **faux sous la v7** (« un exemple retiré » restait au palier « carte ») ; sous la v8, les fautes
  **calibrées** sont arrêtées ; **une faute d'étendue plus petite que le plafond peut encore passer, au palier « carte », avec sa
  réserve** : la garde n'arrête pas toute faute (§ 3).
- **CLP3-02** : essais qui tuent n34, n25c, n28 (banc v4 : tuées). **CLP3-03** : contrôle avant l'ouverture, à la passe à blanc
  (`controler_avant_ouverture` : quatre sceaux de P3, principales, témoin, directions de P3, **révision du modèle de P3 au cache
  local, hors ligne**), cas sain et artefacts. Notes **05** (n_plancher directions par plancher décisif, exigé à l'étape B),
  **07** (`MemoryError`, `TypeError`, `AttributeError`, `IndexError` : arrêt du seul bras), **10** (état des figées affiché par
  `etape-a-apres-repli`) faites ; **06** déclarée (§ 6).
- **Script de l'instance v3** `scripts/etape_a_t07_variante_b_v3.sh` (`a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560`) : S-12 (1) à (5) et S-13 ;
  **répétition jouet v3 de bout en bout : conforme, 17 verdicts sur 17 (un bras établi et un bras arrêté compris)**.
- **Essais** : 73 essais neufs, 72 passés, 1 sauté ; **suite `tests/test_t07_*` de l'arbre** : 530 passés, 23 sautés, 3 `xfail`, aucun échec ; **mutations** (banc v4, corrections) :
  17 mutations, 17 tuées, import tracé de la copie.

## 1. Lu (empreintes vérifiées)

- Contre-lecture du code du plancher v3 (`contre-lecture-code-plancher-v3-v1.md`, `32cbc637…`, conforme) : verdict, défauts
  CLP3-01 à 03, notes CLP3-04 à 10, table des mutations ; pièces nommées seulement.
- `registres/decisions.md`, lignes **R-2305** (corrections décidées : v8, essais, contrôle avant l'ouverture, notes) et **R-2306**
  (candidat 2 et ordre brouillon 6 ; question (1) : script v3 écrit par moi, répété en jouet).
- Ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md` (`92d9aebe…`) : § 0 ter, P13, § 5, § 5 bis, § 11, § 13
  (S-1 à S-13, dont **S-12** et **S-13**). Script v2 `scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`) et sa répétition
  `scripts/repetition_jouet_variante_b_t07_v2.py` (commit `04bc14a2`).

## 2. Corrections (fichiers corrigés en place ; essais qui les tiennent)

| constat | fichier | ce qui change | essai (et mutation tuée, banc v4) |
|---|---|---|---|
| **CLP3-01** seuils | `reextraction_p3_v1.py` | `TOLERANCES` = processeur 10⁻⁶, carte 10⁻³ (témoin), 10⁻² (directions) ; configuration v8 | `test_bruit_de_carte…` (bruit 10⁻⁴ sur le jouet : « carte »), `test_bruit_de_1e3_arrete…` (10⁻³ sur le jouet, 16 exemples : arrêt) ; config v8 / v7 / v6 (c1, c2) |
| **CLP3-01** réserve | `reextraction_p3_v1.py` | `RESERVE_CARTE` : « écart au palier « carte », cause non établie : … carte … ou faute d'étendue partielle des jetons réextraits » | assertion du texte (c3) |
| **CLP3-01** phrase | rapport | corrigée ici (§ 3) | — |
| **CLP3-02** n34 | `lecture_v4.py` | inchangé (copie `dict(t)`) ; désormais tenu | `test_lecture_descriptive_de_p3_ne_touche_pas_aux_scores_decisifs` (c15) |
| **CLP3-02** n25c | `reextraction_p3_v1.py` | inchangé (`max` des paliers) ; désormais tenu | `test_palier_global_le_pire_des_gardes` (c11) |
| **CLP3-02** n28 | `lecture_v4.py` | inchangé ; désormais tenu | bout en bout, bras établi : la réserve de la principale rapportée arrive dans `resultat.reserves` (c16) |
| **CLP3-03** | `reextraction_p3_v1.py`, `passe_blanc_v2.py` | `controler_avant_ouverture` (clé, quatre sceaux de P3, principales de P3 = configuration, témoin, directions de P3, révision du modèle de P3 au cache en réel) et `revision_au_cache` (lecture hors ligne : dossier de la révision, `config.json`, `tokenizer.json`, `tokenizer_config.json`, poids, morceaux de l'index) ; la passe à blanc v2 les joue après la configuration (refus, code 2) et écrit le résultat dans sa sortie | `test_controle_avant_ouverture_cas_sain_et_artefacts` (six artefacts), `test_revision_au_cache_cas_sain_et_artefacts` (cache factice : sain ; révision ou modèle absents ; morceau, tokeniseur, poids manquants), `test_controle_avant_ouverture_en_mode_reel_lit_le_cache`, `test_passe_blanc_v2_refusee…` (c6 à c10, c12) |
| note **05** | `lecture_v4.py` | `exiger_nombre_de_directions` à l'ouverture des scores (étape B) : chaque sonde notée a un plancher décisif de `n_plancher` directions (tableau et nombre écrit), sinon arrêt | `test_nombre_de_directions_exige_a_l_etape_b` (c13, c14) |
| note **07** | `reextraction_p3_v1.py` | `FAUTES_DU_BRAS` + `MemoryError`, `TypeError`, `AttributeError`, `IndexError` | `test_fautes_hors_garde_arretent_le_seul_bras` × 4 (c4, c5) |
| note **10** | `repli_etapes_v2.py` | `etape-a-apres-repli` affiche l'état du plancher des figées (remplacement déclaré au miroir) | miroir (c17) |
| note **06** | — | déclarée (§ 6) | — |
| notes 04, 08, 09 | — | déclarées par R-2305 ; non traitées ici (§ 9) | — |

`lecture_v4.py`, `passe_blanc_v2.py` et `repli_etapes_v2.py` sont régénérés par le générateur v2 (`generer_lecture_v4_v2.py`,
`f53f9a0162b0d9d61f02bd92b62a0a6190ca51d03c584d55308cbf98d7c7141a` : la v1 plus `exiger_nombre_de_directions` et la notice) à partir des remplacements déclarés de
`tests/miroir_plancher_v3_v1.py` (trois remplacements neufs : étape B, passe à blanc, repli) ; l'essai de miroir passe.

## 3. CLP3-01 : seuils, configuration v8, calibrage rejoué, phrase corrigée

**Configuration v8** : `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json`, sha256 du
fichier **`e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328`**, **empreinte canonique
`0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12`** (`lecture_v4 empreinte-config`, code 0). Seul changement
depuis la v7 (`diff`) : `plancher_figees.tolerances.carte_sonde` 0,01 → **0,001**, `carte_directions` 0,1 → **0,01**.
`lecture_v4` refuse la v7 (« tolérances … fixées d'avance attendues », code 2) et la v6 (« clé plancher_figees absente »).
`garde_principale` reste « rapportee » (R-2304).

**Calibrage rejoué** (`calibrage_gardes_v3.py`, `3cc30b5ff6d9274c247fd163592fd0be4e446c9169b62eff45aac5b3ec3f731a` : le v1 importé tel quel, mêmes données, recettes, mesures ;
sortie `calibrage-gardes-v3.json` `b0b1ff695265d2934ca132b8a78cae2479a8d1f58962685fbbea960a827fd703`, 03:24 à 03:29 UTC ; écarts égaux à ceux des v1 et v2) ; palier sous la v8 :

| perturbation | témoin, tromperie | témoin, enjeux | directions, tromperie | directions, enjeux |
|---|---|---|---|---|
| fils 1 contre 4 | 0 : identique | 0 : identique | 6,1 × 10⁻¹¹ : processeur | 4,7 × 10⁻¹⁴ : processeur |
| bruit 10⁻⁴ par jeton | 4,4 × 10⁻⁵ : carte | 2,2 × 10⁻⁵ : carte | 8,5 × 10⁻⁴ : carte | 2,3 × 10⁻⁴ : carte |
| **bruit 10⁻³** | **4,4 × 10⁻⁴ : carte** | **2,2 × 10⁻⁴ : carte** | **8,3 × 10⁻³ : carte** | **2,2 × 10⁻³ : carte** |
| bruit 10⁻² | 4,4 × 10⁻³ : échec | 2,2 × 10⁻³ : échec | 7,0 × 10⁻² : échec | 2,3 × 10⁻² : échec |
| **un exemple retiré** | **6,7 × 10⁻³ : échec** | **4,3 × 10⁻³ : échec** | 1,6 × 10⁻² : échec | 7,2 × 10⁻³ : carte |
| empan décalé d'un jeton | 0,12 : échec | 2,4 × 10⁻² : échec | 0,18 : échec | 3,7 × 10⁻² : échec |
| autre découpage (20 %) | 0,11 : échec | 6,0 × 10⁻² : échec | 0,18 : échec | 9,0 × 10⁻² : échec |
| autre couche | 1,5 : échec | 1,4 : échec | 1,7 : échec | 1,6 : échec |

Exigences de la mère, vérifiées par le script : **toutes les fautes calibrées arrêtées par le témoin : oui** (la plus petite,
« un exemple retiré » des enjeux, à 4,3 fois le plafond) ; **un bruit de 10⁻³ par jeton passe : oui** (palier « carte » pour
le témoin et les directions, réserve écrite). Le palier « carte » admet désormais un bruit d'environ 10⁻³ par jeton (témoin
jusqu'à ≈ 2 × 10⁻³, directions ≈ 1,2 × 10⁻³) ; sous les réglages de P3 et sur sa carte, R-679 n'en montre aucun.

**Phrase du rapport v1 corrigée** (§ 5, « Non-déterminisme de la carte ») : au lieu de « au-delà, ou pour une faute de données,
d'empan, de découpage ou de couche, la garde arrête », lire : « sous la configuration v8, toute faute **calibrée** (un exemple
retiré, empan décalé d'un jeton, autre découpage, autre couche) est arrêtée par le témoin ; une faute qui ne touche qu'une part
assez faible des jetons (écart du témoin sous 10⁻³) peut passer au palier « carte » : le bras est établi, **avec la réserve
« cause non établie »**, recopiée à l'étape B ; la garde n'arrête donc pas **toute** faute ». Sous la v7, « un exemple retiré »
(6,7 × 10⁻³ et 4,3 × 10⁻³) passait au palier « carte » : la phrase de la v1 était fausse.

## 4. CLP3-03 : contrôle avant l'ouverture (à la passe à blanc)

La passe à blanc v2 joue `reextraction_p3_v1.controler_avant_ouverture(racine, config)` juste après le contrôle de configuration,
avant tout calcul et avant l'étape A : une faute refuse la passe (`RefusPasse`, code 2, rien d'écrit) et le script de l'instance
s'arrête (« l'étape A ne part pas »). Le résultat (fichiers de P3 et leurs sceaux, fichier léger, figées : témoin, nombre de
directions de P3, graine de la seconde garde ; modèle de P3 au cache) est écrit dans la sortie de la passe à blanc. En mode
réel, `revision_au_cache` lit le cache **hors ligne** (`snapshot_download(local_files_only=True)`) ; en jouet : « sans objet ». Le
script v3 contrôle aussi la révision au cache à l'étape 8 (§ 5).

## 5. Script de l'instance v3 et répétition jouet v3

**`scripts/etape_a_t07_variante_b_v3.sh`** (fichier neuf, `a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560`, 433 lignes) = le v2 (`e68d3306…`) plus :
1. S-12 (1) : `controle_ia.t07.lecture_v4` pour `empreinte-config`, `repli-seul`, `passe-blanc`, `etape-a-apres-repli` ;
   `repli-recalcul` jamais appelé (la v4 le refuse) ;
2. S-12 (2) : étape A lancée sous `env CUBLAS_WORKSPACE_CONFIG=:4096:8` (écrit au journal) ;
3. S-12 (3) : nom du processeur (`/proc/cpuinfo`) au journal dès l'étape 1 ; hors EPYC, l'étape A reçoit en plus
   `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` (**non éprouvé sur carte, déclaré** ; joué en jouet sur ce processeur Intel) ;
4. S-12 (4) : à l'étape 8, révision du modèle de P3 lue dans le manifeste de P3 cité par la configuration
   (`donnees_p3.manifeste_p3`), comparée à celle de 7b (journal) ; autre révision → préchargée (`precharger_modele`, échec →
   code 2) ; puis **contrôlée au cache hors ligne** (`revision_au_cache`, `HF_HUB_OFFLINE=1` ; absente ou incomplète → code 2,
   rien d'ouvert) ; en essai : « sans objet (modèle jouet) » ;
5. S-12 (5) : `planchers-figees-t07.npz` et `reextraction-p3-t07.json` poussés avec les sorties de l'étape A (ils sont sous
   `donnees/<run-t07>/` et `diag/<run-t07>/`) ; leur présence est écrite au journal ;
6. **S-13** : la borne de taille compte `nf × n_p3` nombres de plus par action (directions de P3 notées en descriptif ; `nf` :
   sondes figées nommées, `n_p3` de `plancher_figees`) et `planchers-figees-t07.npz` (`nf × P × 8 × (d + 1) + 2·10⁶` octets)
   dans les sorties (et dans les morceaux prévus) ; écrits dans `taille-estimee.json` (`planchers_figees_t07`).
   **Ordre de grandeur réel** (non mesuré ; `d` = 4 096, `couches` = 3, `P` = 800, `K` = 2, `p6` = 1, `C` = 2, `L` = 4, `nf` = 2,
   `n_p3` = 200, ≈ 5 760 actions, clés ≈ 400 octets) : F ≈ 10 069 nombres par action ; scores ≈ 0,47·10⁹ ; sondes neuves ≈
   1,29·10⁹ ; planchers des figées ≈ 0,054·10⁹ ; autres 0,05·10⁹ ; **total ≈ 1,87·10⁹ octets, sous la borne de 2·10⁹** (marge ≈
   0,13·10⁹ ; à `n` plus grand que 5 760 d'environ 30 %, la borne arrête avant toute ouverture, code 2).
7. S-1, S-3, S-4, S-8 à S-11 : **non appliqués** (au choix de la mère, non demandés) ; le v3 garde ces constats tels quels.

**Répétition jouet v3** (`scripts/repetition_jouet_variante_b_t07_v3.py`, `d8dde1fb104ee2e61083f13dde226ef05341b33b6518f8aebe0bb93f20c34ce9` ; la v2 plus un run jouet de P3 versé à
`main`, configuration **v8 jouet** — seuils de la v8, `n_plancher` 12, `n_p3` 4, `garde_principale` « rapportee », `donnees_p3` =
ce run —, et un troisième dépôt au témoin de la tromperie faussé de 10⁻²) : passage du 2026-11-11 de 03:34:57 à 03:53:24 UTC (dossier neuf,
  `repetition-v3-a`, commit de la répétition `68882c2d`, script `a19c594d…`), sortie `repetition-jouet-v3-resume.json` et journal
  `repetition-jouet-v3-journal.txt` (scellés). **Conforme : 17 verdicts sur 17** — les douze de la v2 (normal code 0, phrases lues ;
  sans concepts code 0, phrases non lues ; sorties poussées, `src` et `tests` inchangés ; embargo tenu ; branche déjà poussée et
  périmètre faux : code 2 sans repli ; mesure égale à la ligne attendue ; découpage en morceaux scellés, recomposition égale ;
  minuterie saine et en échec) et cinq neufs :
  - `normal_deux_bras_etablis` : `reextraction-p3-t07.json` et `planchers-figees-t07.npz` poussés, les deux bras « établi »,
    graines `plancher/<figée>` au manifeste, `n_plancher` 12 ;
  - `bras_arrete_un_seul` (dépôt au témoin faussé) : code 0, étape A au bout ; bras de la tromperie **arrêté** par la garde
    d'identité (témoin à 9,9 × 10⁻³, « échec » ; directions de P3 à 3,0 × 10⁻⁸, « processeur ») ; bras des enjeux établi ;
    `etape-a-apres-repli` affiche `{'tromperie-lineaire-c2': 'échec', 'enjeux-difference_moyennes-c2': 'établi'}` (note 10) ;
  - `script_v3_journal` : `CUBLAS_WORKSPACE_CONFIG=:4096:8`, processeur, révision de P3 « sans objet » au journal ;
  - `taille_compte_les_planchers_des_figees` : `planchers_figees_t07` = 2 006 336 octets à la taille jouet, `sondes_figees` = 2 ;
  - `passe_blanc_controle_la_reextraction` : la sortie de la passe à blanc porte le contrôle CLP3-03 des deux figées.
  **Constat** : sur ce processeur Intel (non EPYC), le v3 lance l'étape A avec `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` ;
  en jouet, le modèle tourne sur le processeur : les activations réextraites diffèrent alors des derniers bits de celles du run de
  P3 (fait sans ces variables) et les gardes passent au palier **« processeur »** (témoin 5,0 × 10⁻⁷ et 1,2 × 10⁻⁷, directions
  ≤ 5,6 × 10⁻⁸), la principale linéaire refaite s'écarte de 5,6 × 10⁻⁶ (« rapportee » : réserve écrite). En réel, la passe avant
  tourne sur la carte, que ces variables ne touchent pas ; le témoin et les directions (numpy) n'en dépendent pas.

## 6. Note 06 déclarée : tolérance réelle du contrôle en ligne

Le contrôle en ligne de la notation par lots compare 2 directions sur une action sur 8, à 10⁻¹² de l'**échelle** de l'action.
Pour le maximum, l'échelle est max (|a|·|w| + |b|), de l'ordre du score. Pour l'attention, elle ajoute 2 · max |a|·|q| · max |a·w + b| :
à la taille de production, la contre-lecture mesure une échelle médiane d'environ 3,6 × 10⁴ fois le score ; **la tolérance
réelle vaut alors environ 4 × 10⁻⁸ du score**, sans effet sur un rang (les aires ne lisent que les rangs). Déclaré ; la
proposition de la contre-lecture (contrôler la première, celle du milieu et la dernière direction) n'est pas appliquée.

## 7. Essais, suite, mutations

- **Fichiers neufs** (`notation` 20, `reextraction` 32, `lecture` 21) : 73 essais, **72 passés, 1 sauté** (fichier v8 hors de l'extraction de l'arbre ; son contenu est écrit dans l'essai et vérifié par l'empreinte canonique).
- **Suite `tests/test_t07_*.py` de l'arbre au commit final** (un processus, un fil) : **530 passés, 23 sautés (extraction réduite, motifs écrits), 3 `xfail` du dépôt, aucun échec**, code 0 (03:39 à 04:02 UTC, 1 421,7 s, machine partagée avec la répétition et le banc ; `suite-t07-v5.txt`) ; extraction élargie aux pièces du brouillon 19 (lues par la répétition), d'où 4 sauts de moins qu'au rapport v1
- **Banc v4** (`banc_mutations_plancher_v3_v4.py` `29cd7d5e67bc38eda7f46aad14ff82a073f205015b4e1073b95e70a42dfb5a7f`, méthode de R-2246 : copies de `src/` et des invites,
  `-o pythonpath=`, import tracé des cinq modules neufs ; copie saine d'abord) : au commit `7e23a554`, 03:37 à 03:48 UTC (`banc-mutations-plancher-v3-v4.json`) : copie saine
  72 passés, 1 sauté, import de la copie ; **17 mutations, 17 tuées**, aucun import hors de la copie : c1 et c2 (seuils de la v7),
  c3 (réserve d'avant), c4 et c5 (`MemoryError`, `TypeError` hors des fautes du bras), c6 à c10 (contrôle avant l'ouverture :
  témoin, directions de P3, morceaux de l'index, fichiers essentiels, cache jamais lu en réel), c11 (palier global « le
  meilleur », n25c), c12 (passe à blanc sans le contrôle), c13 et c14 (nombre de directions non exigé : fonction, appel), c15
  (n34), c16 (n28), c17 (état des figées non affiché). Premier essai en échec : c12, c14 et c17 par le miroir, les autres par un
  essai de comportement. Les bancs v1 à v3 (code d'avant les corrections, rapport v1, § 7) ne sont pas rejoués.

## 8. Fichiers et empreintes (commit final `7e23a554aca040016a08fe510504adec172c6998`)

| fichier | sha256 | lignes |
|---|---|---|
| `src/controle_ia/t07/plancher_v3.py` | `c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8` | 211 |
| `src/controle_ia/t07/reextraction_p3_v1.py` | `66b6684cbd816d88968ac7faf9d7df98642bdfee04bddf82507352fdf408b76e` | 550 |
| `src/controle_ia/t07/lecture_v4.py` | `f193f1b12b6fd3e1194e83e11f299d8da384e5e2975adf03235acb34bb789078` | 759 |
| `src/controle_ia/t07/passe_blanc_v2.py` | `8e24642fd49c2d57d7f3093f4989a06a5d9110145f7d5574e5b000e48f82dba5` | 511 |
| `src/controle_ia/t07/repli_etapes_v2.py` | `fe08aaa14de1ca0ac88292f2c7a10ec8d591fee1e83f90c9ae38b32d0c6a2f50` | 172 |
| `tests/miroir_plancher_v3_v1.py` | `286bb3a02ae8ccf8809c4b3f51db8775c33f8ff157450dfc386dea4eb347958c` | 176 |
| `tests/test_t07_plancher_v3_notation_v1.py` | `aabda246d2169add12ebeb6cdd79e00c0668c45951521aae5c037dbb0238d63b` | 185 |
| `tests/test_t07_plancher_v3_reextraction_v1.py` | `97f80b8a2b518112e0b05a31f72471c8488df387662bb7722ad1ca36d1cb2616` | 490 |
| `tests/test_t07_plancher_v3_lecture_v1.py` | `6d722899b7f17cbc07108af85565ada223d90cf33aa6cf39d91e60d728c8b4b2` | 387 |
| `scripts/etape_a_t07_variante_b_v3.sh` | `a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560` | 433 |
| `scripts/repetition_jouet_variante_b_t07_v3.py` | `d8dde1fb104ee2e61083f13dde226ef05341b33b6518f8aebe0bb93f20c34ce9` | 499 |

## 9. Réserves

- Calibrage synthétique (comme en v1) ; aux effectifs réels (1 591 exemples des enjeux), « un exemple retiré » pèse environ quatre
  fois moins qu'au calibrage (400) : il peut passer au palier « carte », avec sa réserve ; les gardes d'effectifs le voient.
- Notes **04** (carte déjà servie, espace de cuBLAS : rapportés, non gardés), **08** (biais `b`, requête `q`, palier « carte » de la
  principale, graines de la lecture descriptive, fils de la principale : sans essai dédié) et **09** (palier « processeur » à 10⁻⁶
  admet un bruit de carte d'environ 10⁻⁷ sous ce nom ; seconde garde « sans objet » sans réserve, inatteignable en réel) :
  déclarées par R-2305, non traitées.
- `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` : joués en jouet sur un processeur Intel, jamais sur l'instance.
- La passe à blanc a désormais besoin des entrées de P3 (fichiers cités par la configuration, déjà recopiés par le script) et, en
  réel, du modèle de P3 au cache : préchargé à l'étape 8 du v3.
- Le mode réel n'est toujours pas joué (aucune carte).

## 10. Pièces (scellées, non committées, dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/`)

| pièce | sha256 |
|---|---|
| `configuration-t07-v8.json` | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` |
| `calibrage_gardes_v3.py` | `3cc30b5ff6d9274c247fd163592fd0be4e446c9169b62eff45aac5b3ec3f731a` |
| `calibrage-gardes-v3.json` | `b0b1ff695265d2934ca132b8a78cae2479a8d1f58962685fbbea960a827fd703` |
| `journal-calibrage-v3.txt` | `508abcfce92d9b4359576e6fc888a167d7ed97354ac7b12fc9dd87eea7ad5f94` |
| `generer_lecture_v4_v2.py` | `f53f9a0162b0d9d61f02bd92b62a0a6190ca51d03c584d55308cbf98d7c7141a` |
| `banc_mutations_plancher_v3_v4.py` | `29cd7d5e67bc38eda7f46aad14ff82a073f205015b4e1073b95e70a42dfb5a7f` |
| `banc-mutations-plancher-v3-v4.json` | `3c5ba14aaf9d49dad6912115046d7619f1a3c364d5b54c8111c3de5b5b514a9b` |
| `journal-banc-v4.txt` | `8d52dcd38285fc9c5d488cbf8c55dc0b0f6450f5f01870148031f7d9132235e5` |
| `repetition-jouet-v3-resume.json` | `691b98cfb3eb474b947376de69ece37dc0a178596b8aed14ffbe7b8d99e69529` |
| `repetition-jouet-v3-journal.txt` | `3d1421e72a7484566866e3a2169a7f00c5849f6a78ee936586e19a3e6d108b72` |
| `suite-t07-v5.txt` | `f012078117fc2c21382c6d03661e462f47e8de992145d8db92590be069c815b2` |
| `journal-essais-plancher-v3-v2.txt` | `05763fbb0c492e51a5e69bf3a88bff285405f248dfbff2aa9c7291137628754c` |

Pièces de la v1 inchangées dans le même dossier (rapport v1, configuration v7, calibrage v1 et v2, bancs v1 à v3, générateur v1, mesures du coût, suite v4). Le dossier de la répétition (`…/scratchpad/plancher-v3/bac/repetition-v3-a/`, 413 Mo, dépôts jouets) reste dans le bac à sable, non versé.


