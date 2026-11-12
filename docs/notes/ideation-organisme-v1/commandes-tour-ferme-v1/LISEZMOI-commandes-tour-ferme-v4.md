# LISEZMOI — commandes externes v6 de Kimi et d'Argon pour le tour fermé, étage 1 (réponse coupée de l'étage en code 0)

Rédigé le 3 novembre 2026, de 09:09 à 10:39 UTC (heures de `date -u`), par un sous-agent développeur de session-depot. Aucun
appel payant, aucun modèle, aucune clé ni variable de clé, aucun réseau hors de la boucle locale (ports éphémères ; 8802 à 8807
jamais touchés), rien sous `donnees/`. Arbre `wt-commandes-tf`, branche `outils/commandes-tour-ferme-v1`, partie de `7c223e6a`.
**État** : les v5 sont scellées et commises (`f9da51b9`, compagnons `.sha256` compris) et contre-lues
(`contre-lecture-commandes-tour-ferme-v5-v1.md`, sha256 `28caa87ce60feb2c…`, commit `7c223e6a`) ; ce LISEZMOI accompagne les
**v6**, fichiers neufs (R12), scellés et commis avec lui (commit dans le message de passation, pas ici : un fichier ne peut pas
porter l'empreinte du commit qui le contient). Les fichiers v3, v4, v5, leurs essais, bancs, diffs, LISEZMOI v1 à v3, empreintes
v1 à v3 et `registre_depense_cumulee_v1.py` sont inchangés.

## But et sources exactes

- **n° 300** de session-depot, § 3 : proposition d'une v5 (refus 402 et 429 des relais en code 3).
- **n° 393** de conv-audit, § 4 (`conv-audit_2026-11-03_n393.md`, sha256 `49f5a8d1…`) : « oui à ta v5 », règle B11 (code 4
  réservé à `plafond_session`), I33, à lire avec I34 et T128 ; prix de B11 accepté par écrit. (Le LISEZMOI v3 lui attribuait à
  tort les mots « avec seulement » : ils venaient de la consigne de développement, pas du n° 393 — CL5-01, CL5-08.)
- **Contre-lecture neuve de la v5** (`28caa87c…`) : 0 bloquant, CL5-01 et CL5-02 majeurs, CL5-03 à CL5-08 mineurs.
- **n° 406** de conv-audit, § 2 (`conv-audit_2026-11-03_n406.md`, sha256 `01a116ed770ea850…`) : « v6, réponses coupées de
  l'expérimentateur et du vérificateur rendues en code 0 (T128, I34), cause au registre ; CL5-02 : les trois essais neufs ;
  CL5-05 : `--prix-cache` ; mineurs CL5-03, 04, 06, 07, 08 à ton choix ».
- T128 et I34 : contre-lecture courte du préenregistrement du tour fermé, brouillon 6 (dépôt public `ideation-organism`,
  `d54b85c`). Lecture par la v64 : copie de `ideation-organism` à `eaa74ca` (`adaptateur_commande_v64.py` `adb73287…`,
  `adaptateurs.py` `a1a8ede8…`, `adaptateurs_v56.py` `d36c79b2…`).

## Fichiers neufs

| fichier | sha256 | rôle |
|---|---|---|
| `commande_kimi_v6.py` | `889309305aeb37de9801c2f40c31769fd268abded1ac61ea94196fd0d51195ae` | commande externe de Kimi (relais local 8804) : v5 + cinq changements |
| `commande_argon_v56_nuit_v6.py` | `5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55` | commande externe d'Argon, `appeler` (relais local 8805) : v5 + quatre changements ; `servir` identique |
| `test_commandes_tour_ferme_v6.py` | `1cbae8135be149b566860bacf0fc84c963807840c1adb8041de4fc0308fd1bf2` | 162 essais `pytest` (la suite v5, plus CL5-01 à CL5-04 et CL5-07) |
| `mutations_commandes_tour_ferme_v6.py` | `84947810a04985240c5db9ac6a136bd90c23768856964251e50b7611f71e5fc4` | banc de 111 mutations, « tuée » jamais par l'identité de `servir` |
| `diff-kimi-v5-v6.patch` | `03832df3e4851b5cd620ea6deefc5ca1cd6a5ee5bcd355a0310c0d641705ae11` | `diff -u` v5 → v6 de Kimi (113 lignes) |
| `diff-argon-v5-v6.patch` | `9ca25d8c0ad80a2f907f8d314dd44c13461b24297f7d95ca865bb0e76bc72139` | `diff -u` v5 → v6 d'Argon (104 lignes) |
| `LISEZMOI-commandes-tour-ferme-v4.md` | (voir les empreintes) | ce fichier |
| `EMPREINTES-commandes-tour-ferme-v4.txt` | — | `sha256sum` des fichiers neufs ci-dessus (elle-même exclue) |

**v5 + diff = v6, vérifié** : copies des v5 scellées dans un dossier vide, `patch -p0`, puis `cmp` : égal pour Kimi et Argon ; de
même avec `patch -o`. Les v6 sont fabriquées depuis les v5 par remplacements exacts (10 chez Kimi, 8 chez Argon ; script hors du
dépôt : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/scripts/fabriquer_v6_v1.py`) ;
la suite et le banc v6 depuis ceux de la v5 de même (`fabriquer_suite_v6_v1.py`, `essais_neufs_v6.py`, `fabriquer_banc_v6_v1.py`).

## Différences v5 → v6 (détail numéroté en tête de chaque commande)

1. **CL5-01 — réponse coupée de l'étage de tests en code 0** (Kimi : `finish_reason` « length » ; Argon : statut `TRONQUE` à
   l'usage lu) pour `experimentateur_test` et `lecteur_test` (`ROLES_COUPEE_ADMISE`) : code 0, texte (vide compris), coût lu,
   `modele_servi`, champ neuf `coupee: true` ; **statut `coupee` à la ligne `fin` du registre** (le registre gelé l'accepte sans
   changement). Proposeur et juge : code 5 comme avant (A.5). Coupée à l'usage absent : code 5 (coût au pire cas).
2. **CL5-07 — cause sur la sortie d'erreur** : toute sortie portant `cause_refus` écrit d'abord sur la sortie d'erreur
   `<VERSION> : cause_refus=<cause> : <erreur, 200 caractères au plus>` ; sur un code 3, la classe gelée la met au motif
   (`adaptateurs.py` l. 752-753), que l'étage v5 porte à `journal["arret"]` (`tests_de_mort_v5.py` l. 411-412) — rejoué : motif
   « commande externe : code 3 : commande-…-v6 : cause_refus=garde_etape : … ». Un refus du relais (402, 429), qui a réservé, écrit
   aussi sa cause comme **statut** de sa ligne `fin` au registre ; les quatre refus d'avant le registre n'y écrivent rien.
3. **CL5-03 — registre corrompu** : toute exception de `reg.reserver` (dont `UnicodeDecodeError`, octets non UTF-8) →
   `registre_illisible`, code 3 au plancher, dernière ligne (code 1 sans ligne en v5).
4. **CL5-04 — `envoye` exact (Kimi seulement)** : un 400, 402, 403, 411, 413 ou 429 **non signé** par le relais est une erreur
   de Moonshot transmise : la consigne est partie ; il sort en code 3, `envoye: true`, au **pire cas réservé** (comme le relais
   le compte et comme Argon compte un échec de l'interface). Seul un refus **signé** du relais reste `envoye: false` au plancher.
   Chez Argon rien ne change : son relais ne transmet jamais un statut de l'interface ; un échec de Gemini (429 compris) sort déjà
   en code 3, `envoye: true`, au pire cas. **Sens commun** : sur un code 3, `envoye: false` veut dire « refusé par le relais avant
   tout envoi, compté au plancher » ; `envoye: true`, « parti vers l'amont, compté au pire cas réservé ».
5. Version, en-têtes, lignes d'usage. `servir` : bloc identique à l'octet en v2, v3, v4, v5, v6 (8 573 octets) ; au-dessus, seule
   `VERSION` change ; `principal` identique à la v5 ; constantes neuves dans la partie `appeler`.

Inchangé : code 4 réservé à `plafond_session` ; ligne de code 4 sans `modele_servi`, `refus` ni `stop_reason` (I33) ; clés
d'étape, bornes, gardes, pire cas, registre, protocole. **Fenêtre d'entrée non contrôlée** (CL5-06, ci-dessous).

## Sortie → code → lecture par la v64 (rejouée sur les dernières lignes réelles des v6)

| cas | code | dernière ligne | sortie d'erreur | registre | lecture v64 | effet dans l'étage |
|---|---|---|---|---|---|---|
| `plafond_session` | **4** | `envoye: false`, 1e-6, `cause_refus` | ligne de cause | rien | « budget_depasse », 0 compté | fin des tours ; témoin « non concluant » ; arrêt pour un proposeur |
| `garde_etape`, `garde_cumulee`, `registre_illisible` (octets non UTF-8 compris) | 3 | `envoye: false`, 1e-6, `cause_refus` | ligne de cause | rien | « erreur », 1e-6, cause au motif | arrêt |
| `relais_plafond`, `relais_max_appels` (402, 429 du relais ; Kimi : signés) | 3 | idem | ligne de cause | `debut`, `fin` code 3, statut = la cause | « erreur », cause au motif | arrêt |
| 400, 403, 411, 413 du relais (Kimi : signés) | 3 | `envoye: false`, 1e-6, sans cause | vide | `fin` code 3, `echec` | « erreur » | arrêt |
| Kimi : 4xx non signé (Moonshot transmis : quota, fenêtre…) ; tout autre statut ; Argon : échec de l'interface (429 de Gemini compris) | 3 (Kimi 502 : 5) | `envoye: true`, pire cas, sans cause | vide | `fin` au pire cas | « erreur » (502 « modèle servi » : « refus ») | arrêt |
| réponse coupée, `experimentateur_test` ou `lecteur_test` | **0** | texte, coût, `modele_servi`, `coupee: true` | vide | `fin` code 0, statut `coupee` | « ok » | réponse sans demande (fin des tours) ou témoin « non concluant » |
| réponse coupée, proposeur ou juge ; ou coupée sans usage | 5 | sans texte | vide | `fin` code 5, `tronque` | « erreur » | arrêt (A.5) |

Effets dans l'étage : selon T128, la demande et la contre-lecture v4 ; seuls l'adaptateur v64 et sa porte sont rejoués ici.

## Commandes exactes pour la configuration (mêmes options que la v4 et la v5)

`fournisseurs.kimi.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v6.py",
 "--url-relais", "http://127.0.0.1:8804", "--modele", "kimi-k3.1-pro",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "65536", "--max-sortie-court", "16000", "--sortie-min-jetons", "4096",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

`fournisseurs.argon.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v6.py",
 "appeler", "--url-relais", "http://127.0.0.1:8805", "--modele", "gemini-4-argon",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000", "--sortie-min-jetons", "1000",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

Pour chacun : `"type": "commande_externe"`, `"porte_plafond": {"type": "environnement"}` (`ETAPE_POLE=tour_ferme_v64`, part
`44.00` ou `6.00`, jugée sous `tour_ferme_v64/kimi` ou `tour_ferme_v64/argon`) et `prix_entree_usd_par_million_jetons` = `2`
(Kimi) et `10` (Argon). Ces deux listes sont celles que la suite joue (`CONFIGURATION`), égalité vérifiée par programme.
Interpréteur au manifeste : `/usr/bin/python3` → `/usr/bin/python3.13`, sha256 `dc9c6efba6e3583b…`, 3.13.18 ; commandes :
`EMPREINTES-commandes-tour-ferme-v4.txt`.

**Réglages exigés des relais** (CL5-05 ; I1 de la contre-lecture v4 ; A.6 bis ; avec la v6 une limite propre d'un relais
**arrête** la course) : instances neuves pour la course, sans autre usage, `GET /relais/etat` relevé avant le premier appel et
après le dernier.
- relais Kimi 8804 (`relais_kimi_v3.py`) : `--modeles-permis kimi-k3.1-pro --prix-entree 2 --prix-sortie 10 --prix-cache 2`
  (**`--prix-cache` est obligatoire**, sans défaut : refus de démarrer sinon ; ≤ 2, le barème de la commande),
  `--plafond-usd` ≥ 44,40 (44 + `--reserve-par-appel` 0,40 ; ≈ 1 USD de marge conseillée pour les jetons hors compte),
  `--max-appels` ≥ 1 731 (3 propositions + 12 sessions × 144 cartes et témoins) ;
- relais Argon 8805 (servi depuis `commande_argon_v56_nuit_v2.py`, `servir`) : `--modeles-permis gemini-4-argon`,
  `--plafond-usd` ≥ 6, `--max-appels` ≥ 147 (3 + 144). L'exemple d'usage de l'en-tête (`--plafond-usd 10 --max-appels 50`) n'est
  pas le réglage de la course.

## Fenêtre d'entrée (CL5-06)

Aucune commande ne contrôle la fenêtre du modèle ; rien n'est ajouté. Kimi expérimentateur à 0,80 USD : `plafond_session`
refuse (code 4) toute consigne au-delà de **378 402** caractères ASCII, **344 002** avec un caractère accentué sur dix, **369 173**
avec une fin de ligne sur quarante (recalculé le 3 novembre avec les fonctions de la v6, comme la contre-lecture) ; une consigne de
393 000 caractères est refusée en code 4. Le relais Kimi porte, comme borne haute « à revoir », une fenêtre de 262 144 jetons
(`relais_kimi_v3.py` l. 142) : une consigne acceptée ne la dépasse que sous ≈ 1,45 caractère par jeton ; au-delà, l'erreur de
Moonshot reviendrait en 400 transmis → code 3, `envoye: true` → arrêt. Argon : la borne de session (≈ 27 000 caractères au
vérificateur) rend la question sans objet.

## Essais

```
mkdir COPIE && git -C /home/user/ideation-organism archive eaa74ca orchestrator/pole | tar -x -C COPIE
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v6.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator PY_COMMANDES=/usr/bin/python3 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v6.py
```

Résultats (Python 3.13.18, pytest 9.1.1, copie `eaa74ca` ; `TMPDIR` dans le dossier de travail) : **162 passés, 0 échoué**
(96,3 s, 09:16:10 à 09:17:51 UTC) ; **commandes sous `/usr/bin/python3 -I -B` : 162 passés, 0 échoué** (101,6 s, 09:18:09 à
09:19:51). Sans la copie du dépôt public, les 33 essais qui lisent la v64 échouent (33 erreurs, aucun saut ; vérifié).

Ajouté à la suite v5 : `invariants_v6` sur toute sortie (règle de la v5, plus la ligne de cause sur la sortie d'erreur, sans texte
de consigne, et `coupee` réservé au code 0 de l'étage) ; réponse coupée pour les quatre rôles (code 0 ou 5, statut au registre),
vide, sans usage, et lue par la v64 (« ok » pour l'étage, « erreur » pour le proposeur) ; registre aux octets non UTF-8 (code 3,
et « erreur » au plancher par la v64) ; **CL5-02** : 21 statuts de 400 à 599 hors 402 et 429 par chaque commande (signés et non
signés chez Kimi : 63 sorties), jamais code 4, sans cause, `envoye` et coût exacts ; 403 du vrai gestionnaire de `servir` lu par
`appeler` ; trois échecs de quota de Gemini (429, `RESOURCE_EXHAUSTED`) → code 3 ; lecture statique qui résout les constantes
nommées ; six causes : ligne de cause exacte et statut du registre ; lecture v64 : cause au motif d'un code 3.

## Banc de mutations

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v6.py
```

**Une mutation n'est jamais « tuée » par l'identité de `servir`** (CL5-02) : l'essai d'identité de `servir` est désélectionné
pour chaque mutation, seul le code 1 de pytest compte, tout autre code arrête le banc. Mutations : les 91 du banc v5 transposées,
les cinq de la contre-lecture v5 (CL5-M1, M2, M2b, M3, M3b), 15 propres à la v6 (S1 à S15).

Résultat du 3 novembre 2026 (09:20:00 à 10:30:31 UTC) : **cas sain (dossier non muté) : passe — 162 passed in 96.44s (0:01:36) (96.7 s) ; 111 mutations tuées sur 111 jouées ; code 0**. Sortie brute (hors du dépôt) : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/sorties/banc-v6.txt`.

| id | fichier | mutation | sort | suite | premier essai qui échoue | durée |
|---|---|---|---|---|---|---|
| K1 | `commande_kimi_v6.py` | rôle lecteur_test retiré de ROLES | tuée | 1 failed, 3 passed, 1 deselected in 2.62s | `test_chaque_role_permis_accepte[kimi-lecteur_test]` | 2.9 s |
| K2 | `commande_kimi_v6.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 3 passed, 1 deselected in 2.61s | `test_chaque_role_permis_accepte[kimi-lecteur_test]` | 2.9 s |
| K3 | `commande_kimi_v6.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 33 passed, 1 deselected in 20.41s | `test_sortie_maximale_choisie_selon_le_role[kimi-lecteur_test-500]` | 20.7 s |
| K4 | `commande_kimi_v6.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 40 passed, 1 deselected in 24.16s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.5 s |
| K5 | `commande_kimi_v6.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 40 passed, 1 deselected in 24.46s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.8 s |
| K6 | `commande_kimi_v6.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 12 passed, 1 deselected in 8.01s | `test_plafond_session_absent_ou_invalide_code_2[kimi]` | 8.3 s |
| K7 | `commande_kimi_v6.py` | version v5 rendue | tuée | 1 failed, 1 deselected in 0.88s | `test_chaque_role_permis_accepte[kimi-proposeur_ideation]` | 1.2 s |
| K8 | `commande_kimi_v6.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 10 passed, 1 deselected in 6.58s | `test_modele_demande_different_code_2[kimi]` | 6.9 s |
| K9 | `commande_kimi_v6.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 8 passed, 1 deselected in 5.46s | `test_role_inconnu_refuse_code_2[kimi]` | 5.8 s |
| K10 | `commande_kimi_v6.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 14 passed, 1 deselected in 10.40s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 10.7 s |
| K11 | `commande_kimi_v6.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 50 passed, 1 deselected in 30.29s | `test_registre_cumule_plein_code_3[kimi]` | 30.6 s |
| A1 | `commande_argon_v56_nuit_v6.py` | rôle experimentateur_test retiré de ROLES | tuée | 1 failed, 6 passed, 1 deselected in 4.37s | `test_chaque_role_permis_accepte[argon-experimentateur_test]` | 4.6 s |
| A2 | `commande_argon_v56_nuit_v6.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 37 passed, 1 deselected in 22.14s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 22.4 s |
| A3 | `commande_argon_v56_nuit_v6.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 37 passed, 1 deselected in 22.81s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 23.2 s |
| A4 | `commande_argon_v56_nuit_v6.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 41 passed, 1 deselected in 26.04s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.3 s |
| A5 | `commande_argon_v56_nuit_v6.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 41 passed, 1 deselected in 26.24s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.5 s |
| A6 | `commande_argon_v56_nuit_v6.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 13 passed, 1 deselected in 9.51s | `test_plafond_session_absent_ou_invalide_code_2[argon]` | 9.8 s |
| A7 | `commande_argon_v56_nuit_v6.py` | version v5 rendue | tuée | 1 failed, 4 passed, 1 deselected in 3.19s | `test_chaque_role_permis_accepte[argon-proposeur_ideation]` | 3.5 s |
| A8 | `commande_argon_v56_nuit_v6.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 11 passed, 1 deselected in 7.15s | `test_modele_demande_different_code_2[argon]` | 7.4 s |
| A9 | `commande_argon_v56_nuit_v6.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 9 passed, 1 deselected in 6.12s | `test_role_inconnu_refuse_code_2[argon]` | 6.4 s |
| A10 | `commande_argon_v56_nuit_v6.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 15 passed, 1 deselected in 11.24s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.5 s |
| A11 | `commande_argon_v56_nuit_v6.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 51 passed, 1 deselected in 31.07s | `test_registre_cumule_plein_code_3[argon]` | 31.3 s |
| A12 | `commande_argon_v56_nuit_v6.py` | le relais (servir) tolère un corps sans Content-Length (411 perdu) | tuée | 1 failed, 133 passed, 1 deselected in 82.52s (0:01:22) | `test_servir_codes_402_429_411_413_inchanges` | 82.8 s |
| C1 | `commande_kimi_v6.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 33 passed, 1 deselected in 20.62s | `test_sortie_maximale_choisie_selon_le_role[kimi-lecteur_test-500]` | 20.9 s |
| C2 | `commande_argon_v56_nuit_v6.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 37 passed, 1 deselected in 23.13s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 23.5 s |
| C3 | `commande_kimi_v6.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 40 passed, 1 deselected in 25.41s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.7 s |
| C4 | `commande_argon_v56_nuit_v6.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 41 passed, 1 deselected in 26.03s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.3 s |
| C5 | `commande_argon_v56_nuit_v6.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 81 passed, 1 deselected in 49.11s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 49.4 s |
| C6 | `commande_kimi_v6.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 75 passed, 1 deselected in 45.61s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 45.9 s |
| C7 | `commande_kimi_v6.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 95 passed, 1 deselected in 60.43s (0:01:00) | `test_delai_depasse_code_6_au_pire_cas[kimi]` | 60.7 s |
| C8 | `commande_kimi_v6.py` | gestionnaires de signaux retirés | tuée | 1 failed, 97 passed, 1 deselected in 63.63s (0:01:03) | `test_signal_code_6_au_pire_cas[kimi-SIGTERM]` | 64.0 s |
| C9 | `commande_kimi_v6.py` | contrôle du modèle servi retiré | tuée | 1 failed, 92 passed, 1 deselected in 57.30s | `test_modele_servi_different_code_5[kimi]` | 57.6 s |
| C10 | `commande_argon_v56_nuit_v6.py` | contrôle du modèle servi retiré | tuée | 1 failed, 93 passed, 1 deselected in 57.57s | `test_modele_servi_different_code_5[argon]` | 57.9 s |
| C11 | `commande_argon_v56_nuit_v6.py` | coût d'un échec pris au chiffre du relais, pas au pire cas réservé | tuée | 1 failed, 94 passed, 1 deselected in 58.55s | `test_argon_cout_d_un_echec_au_pire_cas_reserve` | 58.8 s |
| C12 | `commande_kimi_v6.py` | garde d'étape du registre débranchée (plafond_etape_usd=None) | tuée | 1 failed, 14 passed, 1 deselected in 9.68s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 10.0 s |
| N1 | `commande_kimi_v6.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 14 passed, 1 deselected in 11.05s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 11.4 s |
| N2 | `commande_argon_v56_nuit_v6.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 15 passed, 1 deselected in 10.97s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.5 s |
| N3 | `commande_kimi_v6.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 14 passed, 1 deselected in 10.62s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 10.9 s |
| N4 | `commande_argon_v56_nuit_v6.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 15 passed, 1 deselected in 11.06s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.4 s |
| N5 | `commande_kimi_v6.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 60 passed, 1 deselected in 37.10s | `test_b1_suffixe_idempotent[kimi]` | 37.4 s |
| N6 | `commande_argon_v56_nuit_v6.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 61 passed, 1 deselected in 36.77s | `test_b1_suffixe_idempotent[argon]` | 37.1 s |
| N7 | `commande_kimi_v6.py` | champ etape de la dernière ligne = clé du registre (valeur reçue perdue) | tuée | 1 failed, 14 passed, 1 deselected in 9.59s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 9.9 s |
| N8 | `commande_argon_v56_nuit_v6.py` | champ etape_registre absent de la dernière ligne | tuée | 1 failed, 4 passed, 1 deselected in 3.21s | `test_chaque_role_permis_accepte[argon-proposeur_ideation]` | 3.5 s |
| N9 | `commande_kimi_v6.py` | cause : préfixe de la garde d'étape faux (garde d'étape lue garde cumulée) | tuée | 1 failed, 54 passed, 1 deselected in 32.71s | `test_garde_d_etape_code_3[kimi]` | 33.0 s |
| N10 | `commande_argon_v56_nuit_v6.py` | cause : garde d'étape et garde cumulée permutées | tuée | 1 failed, 51 passed, 1 deselected in 30.77s | `test_registre_cumule_plein_code_3[argon]` | 31.1 s |
| N11 | `commande_kimi_v6.py` | cause absente sur le premier contrôle du plafond de session | tuée | 1 failed, 40 passed, 1 deselected in 24.70s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.0 s |
| N12 | `commande_argon_v56_nuit_v6.py` | cause absente sur le second contrôle du plafond de session | tuée | 1 failed, 47 passed, 1 deselected in 28.32s | `test_plafond_session_second_controle_code_4[argon]` | 28.6 s |
| N13 | `commande_kimi_v6.py` | cause absente sur un refus du registre | tuée | 1 failed, 50 passed, 1 deselected in 30.07s | `test_registre_cumule_plein_code_3[kimi]` | 30.4 s |
| N14 | `commande_argon_v56_nuit_v6.py` | cause : registre illisible lu garde cumulée | tuée | 1 failed, 53 passed, 1 deselected in 32.23s | `test_registre_illisible_code_3[argon]` | 32.5 s |
| N15 | `commande_kimi_v6.py` | cause du refus signé du relais perdue (signature jamais lue ; code 3 sans cause, comme en v3) | tuée | 1 failed, 75 passed, 1 deselected in 45.84s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.2 s |
| N16 | `commande_kimi_v6.py` | signature du relais ignorée (toute erreur lue refus du relais : cause et rien parti) | tuée | 1 failed, 85 passed, 1 deselected in 51.79s | `test_refus_du_relais_402_429_code_3[kimi-402-relais_plafond]` | 52.1 s |
| N17 | `commande_argon_v56_nuit_v6.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed, 1 deselected in 34.37s | `test_cause_du_registre_sur_chaque_refus_du_registre_gele` | 34.7 s |
| N18 | `commande_kimi_v6.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed, 1 deselected in 34.25s | `test_cause_du_registre_sur_chaque_refus_du_registre_gele` | 34.6 s |
| N19 | `commande_argon_v56_nuit_v6.py` | cause_refus sur tout refus HTTP du relais (403 compris) | tuée | 1 failed, 84 passed, 1 deselected in 51.09s | `test_cause_refus_absente_hors_des_six_refus[argon]` | 51.5 s |
| N20 | `commande_argon_v56_nuit_v6.py` | dernière ligne JSON d'argparse retirée (comportement v3) | tuée | 1 failed, 19 passed, 1 deselected in 13.04s | `test_arguments_obligatoires_absents_code_2[argon]` | 13.3 s |
| N21 | `commande_argon_v56_nuit_v6.py` | dernière ligne JSON d'argparse aussi pour servir (servir changé) | tuée | 1 failed, 27 passed, 1 deselected in 16.29s | `test_servir_refus_d_argparse_inchange_depuis_la_v3` | 16.6 s |
| N22 | `commande_argon_v56_nuit_v6.py` | champ role absent de la ligne d'argparse | tuée | 1 failed, 19 passed, 1 deselected in 13.65s | `test_arguments_obligatoires_absents_code_2[argon]` | 14.0 s |
| N23 | `commande_argon_v56_nuit_v6.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 96 passed, 1 deselected in 63.45s (0:01:03) | `test_delai_depasse_code_6_au_pire_cas[argon]` | 63.8 s |
| N24 | `commande_argon_v56_nuit_v6.py` | gestionnaires de signaux retirés | tuée | 1 failed, 99 passed, 1 deselected in 66.03s (0:01:06) | `test_signal_code_6_au_pire_cas[argon-SIGTERM]` | 66.4 s |
| N25 | `commande_kimi_v6.py` | cause fausse sur le second contrôle du plafond de session | tuée | 1 failed, 46 passed, 1 deselected in 28.88s | `test_plafond_session_second_controle_code_4[kimi]` | 29.2 s |
| N26 | `commande_argon_v56_nuit_v6.py` | clé d'étape au nom de l'autre fournisseur | tuée | 1 failed, 15 passed, 1 deselected in 12.10s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 12.4 s |
| N27 | `commande_kimi_v6.py` | cause : refus du registre toujours garde d'étape | tuée | 1 failed, 50 passed, 1 deselected in 31.78s | `test_registre_cumule_plein_code_3[kimi]` | 32.1 s |
| N28 | `commande_kimi_v6.py` | écart de modèle signalé par le relais (502) perdu : modele_servi non rendu | tuée | 1 failed, 91 passed, 1 deselected in 58.02s | `test_kimi_ecart_de_modele_signale_par_le_relais_code_5` | 58.3 s |
| N29 | `commande_kimi_v6.py` | 502 du relais rendu en code 3 au lieu de 5 | tuée | 1 failed, 91 passed, 1 deselected in 57.14s | `test_kimi_ecart_de_modele_signale_par_le_relais_code_5` | 57.5 s |
| X1 | `commande_kimi_v6.py` | signature du relais relâchée : toute chaîne `relais` vaut refus du relais | tuée | 1 failed, 89 passed, 1 deselected in 54.42s | `test_kimi_signature_du_relais[402-relais_plafond]` | 54.7 s |
| X2 | `commande_kimi_v6.py` | signature du relais exacte « relais-kimi-v3 » (un relais v4 signé serait lu amont) | tuée | 1 failed, 89 passed, 1 deselected in 54.43s | `test_kimi_signature_du_relais[402-relais_plafond]` | 54.8 s |
| X3 | `commande_kimi_v6.py` | corps d'erreur tronqué à 300 octets avant la lecture de la signature | tuée | 1 failed, 75 passed, 1 deselected in 46.07s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.4 s |
| X4 | `commande_argon_v56_nuit_v6.py` | OSError du registre lue garde_cumulee (RegistreIllisible inchangé) | tuée | 1 failed, 53 passed, 1 deselected in 33.25s | `test_registre_illisible_code_3[argon]` | 33.6 s |
| X5 | `commande_argon_v56_nuit_v6.py` | refus d'argparse rendu en code 4 (que la v64 lirait « budget_depasse ») | tuée | 1 failed, 19 passed, 1 deselected in 12.97s | `test_arguments_obligatoires_absents_code_2[argon]` | 13.3 s |
| X6 | `commande_kimi_v6.py` | clé d'étape non suffixée pour le seul proposeur | tuée | 1 failed, 63 passed, 1 deselected in 39.94s | `test_cle_d_etape_suffixee_pour_chaque_role[kimi-proposeur_ideation]` | 40.3 s |
| X6b | `commande_argon_v56_nuit_v6.py` | clé d'étape non suffixée pour le seul proposeur | tuée | 1 failed, 67 passed, 1 deselected in 41.77s | `test_cle_d_etape_suffixee_pour_chaque_role[argon-proposeur_ideation]` | 42.1 s |
| R1 | `commande_kimi_v6.py` | refus du registre rendu en code 4 (comportement v4) | tuée | 1 failed, 50 passed, 1 deselected in 31.04s | `test_registre_cumule_plein_code_3[kimi]` | 31.4 s |
| R2 | `commande_argon_v56_nuit_v6.py` | refus du registre rendu en code 4 (comportement v4) | tuée | 1 failed, 51 passed, 1 deselected in 32.11s | `test_registre_cumule_plein_code_3[argon]` | 32.4 s |
| R3 | `commande_kimi_v6.py` | refus 402/429 signé du relais rendu en code 4 (comportement v4) | tuée | 1 failed, 75 passed, 1 deselected in 46.41s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.7 s |
| R4 | `commande_argon_v56_nuit_v6.py` | refus 402/429 du relais rendu en code 4 (comportement v2 à v4) | tuée | 1 failed, 81 passed, 1 deselected in 49.58s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 49.9 s |
| R5 | `commande_kimi_v6.py` | 402/429 de l'amont transmis par le relais rendu en code 4 (lecture littérale écartée en v4) | tuée | 1 failed, 75 passed, 1 deselected in 45.87s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.2 s |
| R6 | `commande_kimi_v6.py` | modele_servi nul remis sur la ligne de code 4 (premier contrôle du plafond de session) | tuée | 1 failed, 40 passed, 1 deselected in 25.46s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.8 s |
| R7 | `commande_argon_v56_nuit_v6.py` | modele_servi vide remis sur la ligne de code 4 (second contrôle du plafond de session) | tuée | 1 failed, 47 passed, 1 deselected in 29.96s | `test_plafond_session_second_controle_code_4[argon]` | 30.3 s |
| R8 | `commande_kimi_v6.py` | refus remis sur la ligne de code 4 (second contrôle du plafond de session) | tuée | 1 failed, 46 passed, 1 deselected in 29.52s | `test_plafond_session_second_controle_code_4[kimi]` | 29.9 s |
| R9 | `commande_argon_v56_nuit_v6.py` | stop_reason « refusal » remis sur la ligne de code 4 (premier contrôle du plafond de session) | tuée | 1 failed, 41 passed, 1 deselected in 26.03s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.3 s |
| R10 | `commande_kimi_v6.py` | plafond_session rendu en code 3 (premier contrôle) | tuée | 1 failed, 40 passed, 1 deselected in 24.74s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.0 s |
| R11 | `commande_argon_v56_nuit_v6.py` | plafond_session rendu en code 3 (second contrôle) | tuée | 1 failed, 47 passed, 1 deselected in 29.39s | `test_plafond_session_second_controle_code_4[argon]` | 29.7 s |
| R12 | `commande_kimi_v6.py` | refus du registre compté au pire cas, pas au plancher | tuée | 1 failed, 50 passed, 1 deselected in 31.37s | `test_registre_cumule_plein_code_3[kimi]` | 31.7 s |
| R13 | `commande_argon_v56_nuit_v6.py` | envoye vrai sur un refus du registre (code 3) | tuée | 1 failed, 51 passed, 1 deselected in 31.69s | `test_registre_cumule_plein_code_3[argon]` | 32.0 s |
| R14 | `commande_argon_v56_nuit_v6.py` | garde d'étape seule rendue en code 4 | tuée | 1 failed, 55 passed, 1 deselected in 33.36s | `test_garde_d_etape_code_3[argon]` | 33.7 s |
| R15 | `commande_kimi_v6.py` | registre illisible seul rendu en code 4 | tuée | 1 failed, 52 passed, 1 deselected in 31.86s | `test_registre_illisible_code_3[kimi]` | 32.1 s |
| R16 | `commande_argon_v56_nuit_v6.py` | 429 du relais seul rendu en code 4 | tuée | 1 failed, 82 passed, 1 deselected in 50.03s | `test_six_causes_code_ligne_et_registre[argon-relais_max_appels]` | 50.4 s |
| R17 | `commande_argon_v56_nuit_v6.py` | cause absente sur un refus 402/429 du relais (code 3 sans cause) | tuée | 1 failed, 81 passed, 1 deselected in 48.92s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 49.2 s |
| R18 | `commande_kimi_v6.py` | garde cumulée seule rendue en code 4 | tuée | 1 failed, 50 passed, 1 deselected in 30.33s | `test_registre_cumule_plein_code_3[kimi]` | 30.6 s |
| R19 | `commande_argon_v56_nuit_v6.py` | plafond_session rendu en code 3 (premier contrôle) | tuée | 1 failed, 41 passed, 1 deselected in 26.05s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.4 s |
| R20 | `commande_kimi_v6.py` | plafond_session rendu en code 3 (second contrôle) | tuée | 1 failed, 46 passed, 1 deselected in 28.62s | `test_plafond_session_second_controle_code_4[kimi]` | 28.9 s |
| CL5-M1 | `commande_kimi_v6.py` | 400, 411 et 413 du relais rendus en code 4 par une constante nommée | tuée | 1 failed, 106 passed, 1 deselected in 67.30s (0:01:07) | `test_code_4_seulement_aux_deux_controles_du_plafond_de_session[kimi]` | 67.6 s |
| CL5-M2 | `commande_argon_v56_nuit_v6.py` | 400, 411 et 413 du relais rendus en code 4 (constante dans le prologue, au-dessus de servir) | tuée | 1 failed, 107 passed, 1 deselected in 91.38s (0:01:31) | `test_code_4_seulement_aux_deux_controles_du_plafond_de_session[argon]` | 91.7 s |
| CL5-M2b | `commande_argon_v56_nuit_v6.py` | 400, 411 et 413 du relais rendus en code 4 (constante dans la partie appeler) | tuée | 1 failed, 107 passed, 1 deselected in 77.34s (0:01:17) | `test_code_4_seulement_aux_deux_controles_du_plafond_de_session[argon]` | 77.7 s |
| CL5-M3 | `commande_argon_v56_nuit_v6.py` | échec de l'interface portant « 429 » rendu en code 4, envoye faux (constante dans le prologue) | tuée | 1 failed, 107 passed, 1 deselected in 69.04s (0:01:09) | `test_code_4_seulement_aux_deux_controles_du_plafond_de_session[argon]` | 69.4 s |
| CL5-M3b | `commande_argon_v56_nuit_v6.py` | échec de l'interface portant « 429 » rendu en code 4, envoye faux (constante dans appeler) | tuée | 1 failed, 107 passed, 1 deselected in 67.52s (0:01:07) | `test_code_4_seulement_aux_deux_controles_du_plafond_de_session[argon]` | 67.9 s |
| S1 | `commande_kimi_v6.py` | réponse coupée en code 0 pour tous les rôles (proposeur compris) | tuée | 1 failed, 135 passed, 1 deselected in 77.59s (0:01:17) | `test_reponse_coupee_code_0_pour_l_etage_de_tests_seulement[kimi-proposeur_ideation]` | 77.9 s |
| S2 | `commande_argon_v56_nuit_v6.py` | réponse coupée en code 0 pour tous les rôles (proposeur compris) | tuée | 1 failed, 139 passed, 1 deselected in 78.75s (0:01:18) | `test_reponse_coupee_code_0_pour_l_etage_de_tests_seulement[argon-proposeur_ideation]` | 79.1 s |
| S3 | `commande_kimi_v6.py` | réponse coupée de l'étage en code 5 (comportement v5) | tuée | 1 failed, 105 passed, 1 deselected in 66.92s (0:01:06) | `test_source_sans_lecture_de_cle` | 67.2 s |
| S4 | `commande_argon_v56_nuit_v6.py` | vérificateur retiré des rôles à réponse coupée admise | tuée | 1 failed, 105 passed, 1 deselected in 67.41s (0:01:07) | `test_source_sans_lecture_de_cle` | 67.7 s |
| S5 | `commande_kimi_v6.py` | statut coupee non écrit au registre (tronque) | tuée | 1 failed, 137 passed, 1 deselected in 78.11s (0:01:18) | `test_reponse_coupee_code_0_pour_l_etage_de_tests_seulement[kimi-experimentateur_test]` | 78.4 s |
| S6 | `commande_argon_v56_nuit_v6.py` | champ coupee absent de la ligne | tuée | 1 failed, 141 passed, 1 deselected in 81.24s (0:01:21) | `test_reponse_coupee_code_0_pour_l_etage_de_tests_seulement[argon-experimentateur_test]` | 81.6 s |
| S7 | `commande_argon_v56_nuit_v6.py` | réponse coupée sans usage acceptée en code 0 | tuée | 1 failed, 144 passed, 1 deselected in 84.56s (0:01:24) | `test_reponse_coupee_vide_ou_sans_usage[argon]` | 84.9 s |
| S8 | `commande_kimi_v6.py` | texte d'une réponse coupée non rendu | tuée | 1 failed, 137 passed, 1 deselected in 78.93s (0:01:18) | `test_reponse_coupee_code_0_pour_l_etage_de_tests_seulement[kimi-experimentateur_test]` | 79.3 s |
| S9 | `commande_kimi_v6.py` | ligne de cause retirée de la sortie d'erreur | tuée | 1 failed, 40 passed, 1 deselected in 24.83s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.1 s |
| S10 | `commande_argon_v56_nuit_v6.py` | ligne de cause retirée de la sortie d'erreur | tuée | 1 failed, 41 passed, 1 deselected in 26.23s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.6 s |
| S11 | `commande_kimi_v6.py` | registre corrompu hors des exceptions prises (code 1 sans ligne, v5) | tuée | 1 failed, 151 passed, 1 deselected in 88.14s (0:01:28) | `test_registre_non_utf8_code_3[kimi]` | 88.4 s |
| S12 | `commande_argon_v56_nuit_v6.py` | registre corrompu hors des exceptions prises (code 1 sans ligne, v5) | tuée | 1 failed, 152 passed, 1 deselected in 87.07s (0:01:27) | `test_registre_non_utf8_code_3[argon]` | 87.4 s |
| S13 | `commande_kimi_v6.py` | erreur de l'amont transmise comptée rien parti, au plancher (v5) | tuée | 1 failed, 85 passed, 1 deselected in 51.70s | `test_refus_du_relais_402_429_code_3[kimi-402-relais_plafond]` | 52.0 s |
| S14 | `commande_kimi_v6.py` | cause d'un refus du relais non écrite au registre (statut echec) | tuée | 1 failed, 75 passed, 1 deselected in 45.91s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.2 s |
| S15 | `commande_argon_v56_nuit_v6.py` | cause d'un refus du relais non écrite au registre (statut echec) | tuée | 1 failed, 81 passed, 1 deselected in 50.24s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 50.6 s |

Les cinq mutations de la contre-lecture v5 sont tuées d'abord par la lecture statique (qui résout désormais les constantes
nommées) ; **rejouées sans elle ni l'essai d'identité** (`-k "not code_4_seulement"`, fin à 10:38:56 UTC ; script hors du dépôt
`/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/scripts/cl5_sans_statique_v1.py`),
elles sont toutes tuées par les essais de comportement neufs : CL5-M1, M2, M2b par `test_autres_statuts_http_code_3_jamais_4`,
CL5-M3, M3b par `test_argon_echec_de_quota_de_l_interface_code_3`. S3 et S4 (constante `ROLES_COUPEE_ADMISE` changée) sont
tuées d'abord par le contrôle de cette constante (`test_source_sans_lecture_de_cle`), puis par les essais de la réponse coupée.

## Réserves

1. **Coupée vide** : une réponse coupée sans texte sort en code 0, texte vide (lecture voulue : réponse sans demande, fin des
   tours ; témoin « non concluant ») ; si le vérificateur raisonne au-delà de ses 1 000 jetons de sortie, il rendra souvent
   « non concluant » sans arrêt : c'est le prix de T128.
2. **`cause_refus` au registre** : seulement pour les deux refus du relais (statut de la ligne `fin`) ; les quatre refus d'avant
   le registre n'y laissent rien (registre gelé, aucune réservation) — leur cause est à la dernière ligne et, nouveau, au motif de
   l'étage (`journal["arret"]`). T128 nomme la clé `cause`, les commandes `cause_refus`.
3. **CL5-04 change le compte d'une erreur de Moonshot transmise** : pire cas (au lieu du plancher) au registre de la commande et
   au noyau ; c'est le côté prudent, aligné sur le relais et sur Argon ; la lettre du n° 393 (« au plancher, rien parti ») est
   ainsi remplacée pour les erreurs de l'amont, sur la latitude laissée par le n° 406 (mineurs « à ton choix »). À confirmer par
   conv-audit au brouillon 7.
4. Fenêtre non contrôlée (ci-dessus) ; dépassement de réserve (code 5) non rejoué ; relais réels et lanceur v64 non joués.
5. La suite dépend d'une copie du dépôt public à `eaa74ca` (empreintes contrôlées).
6. Contre-lecture neuve (R2) de la v6 à faire avant la configuration v4.
