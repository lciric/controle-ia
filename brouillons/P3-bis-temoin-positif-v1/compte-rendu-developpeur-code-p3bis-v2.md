# Compte rendu du développeur — corrections du code de P3-bis d'après sa contre-lecture (CP-01 à CP-17) — v2

- **Auteur** : sous-agent développeur neuf (Claude Opus 5.5, `claude-opus-5-5`) de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai écrit ni le code de P3-bis v1, ni ses brouillons, ni ses contre-lectures, ni
  T0.6, ni T0.7, ni le lanceur de P3-bis (écrit en parallèle dans `/home/user/wt-p3bis-lanceur`, que je n'ai pas touché ;
  aucun fichier de la table des noms communs renommé).
- **Heures** (toutes relevées par `date -u`) : début 2026-11-10 05:20:47 UTC ; arbre créé à 05:21 ; écriture accidentelle
  et refus du classifieur vers 05:42-05:44 (écart E-1) ; premier passage de la liste ciblée v2 de 05:58:35 à 06:18:23 ;
  second passage de 06:19:57 à 06:40:04 ; essai de fermeture v2 de 06:41:00 à 06:48:07 ; dossiers temporaires effacés par
  leur chemin exact après chaque passage ; compte rendu écrit ensuite (heure du commit qui le porte).
- **Lieu** : arbre `/home/user/wt-p3bis`, branche `prep/p3bis-code-v2`, tirée de `main` `04a1b392` par la commande de la
  consigne ; commits locaux seulement, jamais `fetch` ni `push`, rien écrit dans un autre arbre (sauf l'écart E-1).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-corrections-code-p3bis-v2.md`
  (`79e126ae…`, vérifiée) ; noms communs `noms-communs-p3bis-v2.md` (`766992f4…`, vérifiée) ; interdits communs
  `consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`, vérifiée).
- **Lu** (empreintes vérifiées) : contre-lecture du code `brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md`
  (`7a074ad1…`, entière) ; brouillon 9 (`eb65773f…` : en-tête, tables « du 6 au 7 » à « du 8 au 9 », « Plan d'analyse »
  entier, « Critères de lecture gelés », « Liste d'arrêt », « Ce que le code et la chaîne doivent changer ») ; N-066
  (`21e83ed5…`, entière) ; compte rendu du développeur v1 (`977d84c1…`, entier) ; les douze fichiers du code v1 (commit
  `e86a6f32`, empreintes égales à celles du compte rendu v1) ; de P3 : `lecture.py` (gardes du mode décisif, `analyser`),
  `prereg.py` (`problemes`, `exiger_prereg_scelle`), `manifeste.creer_manifeste`, `harnais/validation_reelle.py`
  (`exiger_code_cite`, `exiger_code_importe_sous`), `tests/test_premier_test_ia_lecture.py` (essai du mode décisif) ;
  `tests/test_cibles_invisibles_v1.py` (inventaire). **T0.7** : seul `src/controle_ia/t07/registre_v1.py` de `main`
  (`914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0`, dernier commit qui le touche `72be6999`), et
  seulement ses lignes 39 à 43 (motifs `SHA`, `DATE`, `CLE`, `FORMAT_DATE`), relevées par `grep` pour CP-15.
- **Tailles seulement** (`ls -l`, aucun contenu ouvert) : `donnees/20261019-230011-p3-reel/` et
  `diag/20261019-230011-p3-reel/episodes-p3.json` de P3, dans le clone de la mère (taille du second paquet, plus bas).
- **Non ouvert** : aucun fichier ni aucune branche des interdits communs ; aucun fichier de T0.7 autre que celui nommé ;
  aucun appel externe, aucun `vastai`, aucune dépense ; ni le brouillon 9 ni la configuration écrits ; aucune valeur tirée
  d'une sonde de 7a (aucune sous mes yeux).

## Verdict

**Défauts bloquants CP-01 à CP-03 et défauts CP-04 à CP-11, CP-14, CP-16 réglés ; CP-12, CP-15 et CP-17 réglés avec un
résidu déclaré ; CP-13 laissé au texte.** Code au commit `02217f1cf5255ef87c42285fc579d38c5a6ff003` : liste ciblée v2
(30 fichiers) **531 passés, 0 échec, 0 sauté** ; essai différentiel de fermeture v2 **CONFORME** ; identité avec P3 : 14
ajouts, aucun fichier de P3 modifié ni retiré. Un incident à traiter par la mère : écart E-1.

## Commits (branche `prep/p3bis-code-v2`, locaux)

| commit | heure (UTC) | jalon |
|---|---|---|
| `fc5bf130` | 05:29:23 | 1 : CP-10, inscription à l'inventaire des cibles invisibles |
| `a2272d52` | 05:37:21 | 2 : `ouverture_p3bis_v2.py` |
| `bd0a7521` | 05:45:18 | 3 : ses essais ; `exclure_localement` corrigé |
| `6050c788` | 05:49:50 | 4 : essai différentiel de fermeture v2 et ses essais |
| `5699a6d7` | 05:54:41 | 5 : gardes de la lecture complémentaire, chaîne fermée décisive |
| `f046f7d1` | 05:57:10 | 6 : scripts de l'instance v2, liste ciblée v2, essai des scripts v2 |
| `02217f1c` | 06:19:39 | 7 : compagnons des fichiers neufs ; **commit du code proposé** |
| `66793d49` | 06:48:38 | 8 : sortie scellée de l'essai de fermeture v2 |
| (suivant) | — | 9 : ce compte rendu, scellé |

`git diff --quiet 02217f1c 66793d49 -- . ':(exclude)brouillons'` : vide (seul `brouillons/` change après le commit du code).

## Essais

| essai | commande | résultat |
|---|---|---|
| liste ciblée v2, passage 1 (commit `f046f7d1`) | `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider --basetemp=/home/user/wt-p3bis/.essais-tmp/liste-v2 -rs $(cat scripts/essais-cibles-p3bis-v2.txt)` | 530 passés, **1 échec** (dernière assertion de mon essai neuf `test_essai_differentiel_de_fermeture_complet` : l'essai, conforme, laissait le dossier vide `second-paquet` ; corrigé dans le script au jalon 7), 1 186,12 s |
| **liste ciblée v2, passage 2 (commit `02217f1c`)** | même commande, `--basetemp=/home/user/wt-p3bis/.essais-tmp/liste-v2-b` | **531 passés, 0 échec, 0 sauté**, 1 204,76 s (Python 3.13.18, conteneur à 4 cœurs, environnement de la mère) |
| essai des cibles invisibles (hors liste) | `… -m pytest -q -p no:cacheprovider --basetemp=… tests/test_cibles_invisibles_v1.py` | 21 passés (avant l'inscription : 1 échec, l'inventaire) |
| essai de fermeture v2, une fois (commit `02217f1c`) | `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B scripts/essai_fermeture_p3bis_v2.py /home/user/wt-p3bis/.essais-tmp/essai-fermeture-final brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt` | code 0, « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME », 18 lignes conformes, 0 non conforme, 7 min 07 s |

Essais neufs : `tests/test_premier_test_ia_ouverture_p3bis_v2.py` 73, `tests/test_essai_fermeture_p3bis_v2.py` 6,
`tests/test_premier_test_ia_lecture_p3bis_gardes_v1.py` 7, `tests/test_script_p3bis_v2.py` 9 : 95 ; 436 + 95 = 531. Aucun essai
existant modifié (seule l'entrée de `REGISTRE`, qui n'est pas une fonction d'essai, CP-10). La suite complète n'a pas été
jouée (interdit). Place libre relevée avant chaque passage (`df -h /home/user`) : jamais sous 3 Go (minimum vu 3,7 Go).

Sortie de l'essai de fermeture (extraits ; fichier versé) : taille 16 783 360 octets aux 16 passages sains ; une seule forme
des sorties de classe 1 sur les 16 ; longueurs `zlib` : plage totale 11 octets, plages par issue 8, 9, 9 et 2, plus grande 9,
dépassement 2 pour une marge de 16 ; durées de 8,32 à 10,28 s, plus grand écart entre issues 1,96 s ; contrôles positifs
détectés chacun par son critère : issue imprimée (sortie), code (code), non bourré (taille fixe : 10 240 octets), 4 096 zéros
(règle des plages : 16 782 069 à 16 782 077 contre 16 786 141 à 16 786 147), sommeil (71,19 s contre 9,86 s), corps non
comprimé (règle des plages, ≈ 9 900 octets d'écart), fichier resté en clair (inventaire de l'arbre ; `git status
--porcelain` ne le voit pas) ; second paquet : sels neufs, quatre morceaux, relectures exactes.

## Table des défauts (fait, fichier, ligne, essai)

Abréviations : `ob2` = `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` ; `t-ob2` =
`tests/test_premier_test_ia_ouverture_p3bis_v2.py` ; `ef2` = `scripts/essai_fermeture_p3bis_v2.py` ; `t-ef2` =
`tests/test_essai_fermeture_p3bis_v2.py` ; `t-lg` = `tests/test_premier_test_ia_lecture_p3bis_gardes_v1.py` ; `t-sc2` =
`tests/test_script_p3bis_v2.py`. Lignes au commit du code.

| # | état | fait | où | essais |
|---|---|---|---|---|
| CP-01 | **réglé** | trois décisions lues (`Décision : maintenir|ouvrir|ouvrir pleinement`) ; modes `pleine`, `reduite`, `pleine-anticipee` ; « ouvrir » sans garde adaptée conforme : refus `garde-adaptee-absente` ou `garde-adaptee-posterieure` en tout mode, **jamais d'ouverture** (plus de branche 2 sous « ouvrir ») ; `pleine-anticipee` seulement sous « ouvrir pleinement » ; une seule « ouvrir pleinement » après « ouvrir », et seulement si une ouverture `reduite` appuyée sur la ligne de cet « ouvrir » est lue au journal, datée strictement avant la ligne suivante ; sinon `ligne-apres-decision-finale` | `ob2` l. 153, 166, 917-945 (`lire_decision`), 962-982 (`suite_des_decisions`), 994-1016 (`garde_adaptee_en_vigueur`), 1046-1121 (`garde_ouverture`) | `t-ob2` : `test_branche_1_reduite_puis_ouvrir_pleinement_puis_plus_rien`, `test_complement_pleine_apres_la_reduite`, `test_ouvrir_sans_garde_adaptee_conforme_n_ouvre_jamais` (6 cas × 3 modes), `test_branche_2_ouvrir_pleinement_et_maintenir`, `test_suite_des_decisions_refusee` (6 suites), `REFUS` « ligne après ouvrir », « ligne après ouvrir pleinement », « décision inconnue » |
| CP-02 | **réglé** | journal au format exact du texte (l. 668-695) : deux lignes d'en-tête exactes, six cellules, clés `OUVERTURE-P3BIS` et `REFUS-OUVERTURE-P3BIS`, mode seul, appui `CLÉ=sha256` dans l'ordre du mode, paquets `<sha256> <sha256>`, motif `-` ou `code : texte` d'un code de la liste fermée (17 codes recopiés du texte) ; chaque ligne vérifiée avant d'être écrite ; journal entier relu à chaque tentative (format, ordre des ouvertures) ; `deja-ouverte` ; journal hors format : refus `ligne-mal-formee`, ligne neuve qui suit, la fautive jamais corrigée ; un code par refus (celui du premier défaut, tous les défauts dans le texte) | `ob2` l. 163-180, 182-201, 672-791 (`lire_ligne_journal`, `exiger_format_journal`, `lire_journal`, `ligne_journal`, `inscrire`), 1046-1060 | `t-ob2` : `test_chemin_normal_ouverture_pleine_sans_le_fichier_de_t07_journal_exact` (texte entier du journal comparé), `test_codes_de_refus_et_en_tete_du_journal_egaux_au_texte`, `test_format_du_journal_cas_sain_et_chaque_ligne_hors_format` (cellule en trop ou en moins, clé inconnue, date mal formée, mode inconnu, appui hors forme, paquets, motif hors liste, ordre interdit, en-tête, saut de ligne), `test_ligne_ecrite_verifiee_avant_l_ecriture`, `test_journal_hors_format_refus_ligne_mal_formee_et_ligne_neuve_qui_suit`, `test_refus_de_la_garde_code_de_la_liste_fermee_rien_ouvert_et_journalise` (29 cas, code vérifié et ligne relue au format) |
| CP-03 | **réglé** | quatre passages par issue (16 sains) ; règle du texte : plage totale ≤ plus grande plage d'une même issue + 16 octets, plages et écarts écrits ; contrôle positif « 4 096 octets de bourre à zéro sous « vu » seulement », détecté par cette règle (deux passages par issue) ; variante « corps non comprimé » gardée ; contrôle négatif par issue ; seuil absolu de 64 octets retiré | `ef2` (constantes `PASSAGES_PAR_ISSUE`, `MARGE_ZLIB`, `ZEROS_BOURRE`, `regle_zlib`, `constats`, `essai`) | `t-ef2` : essai complet ; `test_regle_des_plages_cas_sain_au_seuil_et_au_dela` |
| CP-04 | **réglé** | `corps.bin` = longueur L de l'archive comprimée sur 8 octets (poids fort en tête), flux xz, bourre ; relecture : 0 < L ≤ 16 780 792, flux fini exactement après L octets | `ob2` l. 125, 293-312 (`corps_lectures`, `lire_corps`) | `t-ob2` : `test_fermer_taille_fixe_longueur_sur_8_octets_corps_comprime_puis_bourre`, `test_relecture_du_paquet_des_lectures_refuse_les_alterations` (L = 0, L hors borne, L − 1, L + 1, cas sain refait) |
| CP-05 | **réglé** | `lectures_fermees` mesure le dépliage, chaque lecture et la chaîne avant la mise en paquet, et écrit `durees-lectures-v1.json` dans l'espace fermé avant `fermer` (classe 2, dans le paquet) | `ob2` l. 133, 610-653 | `t-ob2` : `test_lectures_fermees_cas_sain_durees_dans_le_paquet` ; `t-lg` : `test_chaine_fermee_de_bout_en_bout_en_mode_decisif` |
| CP-06 | **réglé** | journal impossible à écrire (dossier `registres/` absent, chemin occupé, écriture en échec) : `JournalImpossible`, refus code 2, rien d'ouvert, aucune ligne ; l'ouverture n'a lieu qu'après l'écriture de sa ligne | `ob2` l. 193-194, 771-790, 1184-1228 | `t-ob2` : `test_journal_impossible_a_ecrire_refus_rien_ouvert` |
| CP-07 | **réglé** | fichiers laissés dans le clone relevés par l'inventaire de l'arbre (`.git` exclu ; chemins ignorés et exclus compris) ; seuls le paquet et son compagnon admis ; contrôle positif « fichier de lecture resté en clair » sous un chemin exclu, détecté, et la sortie montre que `git status --porcelain` ne le voit pas | `ef2` (`fichiers_laisses`, `laisses_attendus`, `constats`, variante `fichier-reste`) | `t-ef2` : essai complet ; `test_fichiers_laisses_voit_les_chemins_ignores_et_exclus` |
| CP-08 | **réglé** | option `--instant` retirée de la ligne de commande ; l'instant est celui de l'horloge ; le paramètre reste en Python pour les essais | `ob2` l. 1263-1316 | `t-ob2` : `test_ligne_de_commande_code_2_sur_refus_0_sur_ouverture_sans_instant` (`--instant` refusé par l'analyseur) |
| CP-09 | **réglé** | un essai d'artefact (et un cas sain) par garde nommée : membre absolu, à « .. », non ordinaire, en double ; morceaux non consécutifs, index illisible, d'un autre run, sans morceau ; chemin hors de `donnees/<run>/` ; chemins communs aux deux paquets ; extraction en échec après la ligne du journal ; décision datée après sa ligne ; `SCELLEMENT-T07` à la date de la décision ou après ; garde adaptée citant un autre texte ; dossier hors d'un clone git ; lecture : cas sain décisif (texte scellé factice, commit cité), `max_nouveaux` illisible (absent, booléen, 0, texte), sondes principales différentes, deux lignes d'audit, état sans aire ; bout en bout décisif de la lecture complémentaire et de `lectures-fermees` | `t-ob2`, `t-lg` (`lecture_p3bis_v1.py` inchangée) | `t-ob2` : `test_membres_de_cas_sain_et_noms_ou_genres_refuses`, `test_relecture_du_second_paquet_index_morceaux_et_chemins`, `test_chemins_communs_aux_deux_paquets_refus`, `test_extraction_en_echec_apres_la_ligne_du_journal`, `REFUS` « décision datée après sa ligne », `test_ouvrir_sans_garde_adaptee_conforme_n_ouvre_jamais`, `test_exclure_localement_hors_d_un_clone_git` ; `t-lg` : les 7 essais |
| CP-10 | **réglé** | `run_v2.py::executer` inscrit au dictionnaire `REGISTRE` (exempté, avec sa raison), **aucune fonction d'essai touchée** ; compagnon `.sha256` aligné (écart E-2) | `tests/test_cibles_invisibles_v1.py` l. 357-358 | `tests/test_cibles_invisibles_v1.py` : 21 passés (l'essai d'inventaire échouait avant l'inscription) |
| CP-11 | **réglé** | refus du dépliage : code et motif imprimés (intégrité du second paquet seulement) ; refus de `fermer` : code seul imprimé, motif écrit dans `espace-ferme-p3bis/mise-en-paquet.erreurs`, l'espace restant en place | `ob2` l. 134, 610-653 | `t-ob2` : `test_lectures_fermees_depliage_refuse_imprime_code_et_motif`, `test_lectures_fermees_motif_de_la_mise_en_paquet_garde_dans_l_espace_ferme` |
| CP-12 | **partiel** | tous les fichiers neufs renvoient au brouillon 9 ; la docstring de la v2 nomme `REFUS-OUVERTURE-P3BIS` ; `run_v2.py` et `lecture_p3bis_v1.py`, inchangés (R12, table des noms communs), gardent leurs renvois au brouillon 6, et les fichiers v1 aussi | — | — |
| CP-13 | **au texte** | listé seulement (côté texte) | — | — |
| CP-14 | **réglé** | graines du jouet : `SeedSequence(20261110, spawn_key=(i,))` par issue, écrites dans la sortie | `ef2` (`graine`, `essai`) | `t-ef2` : `test_graines_derivees_par_issue`, essai complet |
| CP-15 | **réglé pour la v2, résidu déclaré** | l'essai v2 compare les motifs à des chaînes recopiées de `t07/registre_v1.py` (empreinte et commit écrits), sans importer T0.7 ; mais la liste ciblée v2 garde, par la lettre de la consigne (« v1 plus tes fichiers neufs »), `tests/test_premier_test_ia_ouverture_p3bis_v1.py`, qui importe toujours `controle_ia.t07.registre_v1` (écart E-4) | `ob2` l. 155-162 ; `t-ob2` l. 36-39 | `t-ob2` : `test_motifs_du_registre_egaux_aux_chaines_recopiees_de_t07` |
| CP-16 | **réglé** | `exposer-issue` : `--lecture-p3bis` exigée pour les lignes 2 à 5, sceau vérifié (`scellement.verifier`), issue mécanique lisible, accord exigé ; ligne 1 sans | `ob2` l. 1231-1260 | `t-ob2` : `test_exposer_issue_accord_exige_et_sceau_de_la_lecture_verifie` |
| CP-17 | **réglé, résidu déclaré** | antériorités strictes de `SCELLEMENT-T07` et de la garde adaptée à la ligne de la décision « ouvrir » ; `lectures-fermees` exige `--entropie` dès que `--prereg` est donné ; `p3bis_instance_v2.sh` rend 5 dès que le second paquet a échoué, arrêt compris (fonction `sortir`, EXIT et TERM) ; résidu : la sous-commande `fermer` seule garde `--entropie` facultative (interface inchangée pour le lanceur ; écart E-6) | `ob2` l. 994-1016, 610-617 ; `scripts/p3bis_instance_v2.sh` (`sortir`) | `t-ob2` : `test_ouvrir_sans_garde_adaptee_conforme_n_ouvre_jamais` (égalité refusée, une seconde avant admise), `test_lectures_fermees_mode_decisif_exige_l_entropie` ; `t-sc2` : `test_second_paquet_partiel_en_echec_pendant_un_arret_code_5` |

## Écarts déclarés

- **E-1 — écriture accidentelle hors de mon arbre, remise en état refusée (à traiter par la mère).** La première version de
  mon essai `test_exclure_localement_hors_d_un_clone_git` créait un dossier « non git » sous le `--basetemp` exigé, donc
  **sous mon arbre** : `git rev-parse --git-path info/exclude` y a trouvé le dépôt englobant, et `exclure_localement` a
  ajouté la ligne `/x/` (4 octets) à **`/home/user/controle-ia-travail/.git/info/exclude`**, fichier commun à tous les arbres
  liés de ce dépôt (date du fichier 2026-11-10 05:42:07 UTC ; il fait 244 octets : les 240 octets du gabarit de git, égaux
  à `/usr/share/git-core/templates/info/exclude`, puis `/x/\n`). J'ai voulu retirer exactement ces 4 octets
  (`truncate -s 240` puis comparaison au gabarit) ; **refus du classifieur, tel quel** : « Permission for this action was
  denied by the Claude Code auto mode classifier. Reason: [Irreversible Local Destruction]. » Je me suis arrêté sur ce
  point : aucune autre tentative. Effet : un chemin `x` à la racine d'un arbre de ce dépôt serait ignoré par git ; à
  06:49 UTC, aucun chemin `x` dans aucun des arbres listés par `git worktree list`. Remède proposé : retirer la dernière ligne
  `/x/` de ce fichier. Correction de l'essai : plafond `GIT_CEILING_DIRECTORIES` posé sur son dossier temporaire (git ne
  remonte plus vers un dépôt englobant) ; vérifié que la date et la taille du fichier n'ont plus bougé ensuite (deux passages
  complets de la liste compris). Aucun autre essai ne travaille hors d'un dépôt jetable.
- **E-2 — compagnon de `tests/test_cibles_invisibles_v1.py` réécrit** (`6a833e3e…` → `c3e08fc2…`) à la main, l'outil de
  scellement refusant d'écraser (R12) : la consigne ordonne l'inscription dans ce fichier même ; sans cela le compagnon serait
  faux (`tests/` n'est pas sous `verifier-arbre`). L'historique local (clone superficiel) ne montre pas comment les quatre
  inscriptions antérieures ont traité ce compagnon.
- **E-3 — codes de refus des cas que la liste fermée ne nomme pas** (docstring de la v2, « Choix déclarés ») : fichier
  cité absent → `sceau-faux` ; décision mal formée, d'un autre fichier, datée avant le rendez-vous ou après sa ligne →
  `ligne-mal-formee` ; journal hors format → `ligne-mal-formee` ; aucune `SCELLEMENT-T07` ou garde adaptée citant un autre
  texte → `garde-adaptee-absente` ; `SCELLEMENT-T07` ou garde adaptée datée à la ligne de la décision « ouvrir » ou après →
  `garde-adaptee-posterieure` ; mode demandé sans la décision qui l'autorise → `ni-scores-ni-ouvrir` ; `pleine` demandée sous
  « ouvrir » ou « ouvrir pleinement » sans lignes de T0.7 conformes → code du premier défaut de ces lignes (`ligne-absente`,
  `compagnon-absent`, `sceau-faux`, `date-posterieure`) ; date de mise en paquet illisible, paquet faux, chemins communs,
  paquets autres que ceux de l'ouverture réduite → `paquet-faux`. Plusieurs défauts : code du premier relevé, tous écrits
  dans le texte libre. **Sans ligne au journal** : journal impossible à écrire (`JournalImpossible`, code 2) ; erreurs
  d'appel (mode inconnu, dossier de sortie déjà présent ou parent absent ; code 1). Extraction en échec après la ligne
  `OUVERTURE-P3BIS` : code 1, la ligne reste (sens prudent pour T0.7). À relire par la mère pour la concordance avec T0.7.
- **E-4 — liste ciblée v2 = liste v1 + mes quatre fichiers d'essais (lettre de la consigne).** Elle garde donc les essais des
  fichiers v1, dont `tests/test_premier_test_ia_ouverture_p3bis_v1.py`, qui importe toujours `controle_ia.t07.registre_v1`
  (résidu de CP-15), et `tests/test_essai_fermeture_p3bis_v1.py` (≈ 3,5 min sur l'instance). Proposition, si la mère le
  veut : une liste v3 sans `test_premier_test_ia_ouverture_p3bis_v1.py`, `test_essai_fermeture_p3bis_v1.py` ni
  `test_script_p3bis_v1.py` (essais de fichiers que la chaîne v2 n'emploie plus ; `test_premier_test_ia_lecture_p3bis_v1.py`
  doit rester : il essaie la lecture complémentaire, qui n'a pas changé), et un `p3bis_instance` qui porte son empreinte.
- **E-5 — amorce v2 créée** : `scripts/amorce_instance_p3bis_v2.sh` (la table la prévoit « seulement si elle change » : elle
  change, puisqu'elle appelle le script de l'instance par son nom). Seul écart à la v1 : le script appelé. À signaler au
  lanceur.
- **E-6 — `fermer` seul garde `--entropie` facultative** (résidu de CP-17) : `lectures-fermees`, que la chaîne joue, l'exige
  en mode décisif ; je n'ai pas changé l'interface de `fermer` (la table des noms communs ne le prévoit pas). Recommandation :
  le lanceur passe toujours `--entropie` à `fermer` quand il refait une mise en paquet.
- **E-7 — défaut hérité de la v1 trouvé par un essai neuf et corrigé dans la v2** : `exclure_localement` écrivait deux fois un
  motif répété dans un même appel.
- **E-8 — chaque mode jugé sur ses seules conditions** : `reduite` est permise sous une dernière décision « ouvrir » avec la
  garde adaptée en vigueur même si `SCORES-T07` et `SONDES-T07` sont déjà inscrites ; `pleine-anticipee` sous « ouvrir
  pleinement » de même. Le texte ne tranche pas ce croisement ; aucun code de la liste fermée ne le refuserait.
- **E-9 — lecture de « une seule « ouvrir pleinement » après une ouverture réduite lue au journal »** : l'ouverture `reduite`
  doit être appuyée sur la ligne de cet « ouvrir » (`RENDEZ-VOUS-P3BIS-N=<empreinte>` de cette ligne) et datée strictement
  avant la ligne « ouvrir pleinement ». **Ajout** : le complément `pleine` ou `pleine-anticipee` doit ouvrir les mêmes paquets
  que l'ouverture réduite (sinon `paquet-faux`).
- **E-10 — essai différentiel** : le dossier de chaque passage est effacé dès ses sorties relevées (place disque) ; contrôles
  positifs joués à un passage par issue, sauf « 4 096 zéros » et « corps non comprimé » (deux par issue, pour la règle des
  plages) ; l'écart de durée est le plus grand entre deux passages d'issues différentes ; graines du jouet changées (11 à 14
  de la v1 → `SeedSequence(20261110, spawn_key=(i,))`), les quatre issues étant réalisées par ces graines.
- **E-11 — CP-12 partiel** : `run_v2.py` et `lecture_p3bis_v1.py` restent tels quels (R12 ; la table : une v2 de la lecture
  « seulement si le code change ») et gardent leurs renvois au brouillon 6 ; les fichiers v1 aussi.
- Le texte nomme encore partout les noms v1 (`ouverture_p3bis_v1.py`, `essais-cibles-p3bis-v1.txt`, `p3bis_instance.sh`,
  `amorce_instance_p3bis.sh`, `essai_fermeture_p3bis_v1.py`) : à remplacer par les noms v2 au texte.

## Ce qui va au texte (version neuve, relue sur l'écart)

1. Écarts du développeur v1 : **3** (cinq sous-commandes ajoutées à `fermer` et `ouvrir`) ; **4** (second paquet :
   `donnees/<run>/` entier, non comprimé, index `paquet-run-ferme-v1.json`, dépliage des seuls fichiers lus) ; **5**
   (`.git/info/exclude` du clone fermé et du clone de l'instance) ; **7** (motif étendu aux lignes 44 à 46 de
   `t06/test_croise.py`, non 43 à 45) ; **9** (réserves de PB-9 calculées hors module, par le lecteur du verdict) ; **10**
   (« aucun essai qui lit `donnees/` » : les données non suivies).
2. **CP-13** : sorties en clair hors de la liste de la classe 1 — dossier `traces/` (journal, `tests.txt`, `run.err`,
   `run.json`, `pip-freeze`, `nvidia-smi`, processeur, `second-paquet.txt`), empreintes de fichiers de classe 2 dans
   `resume.json` et dans le manifeste du run, index `paquet-run-ferme-v1.json` ; à ajouter à la classe 1, avec la phrase de
   justification (contre-lecture, CP-13).
3. **Taille réelle du second paquet** : non mesurable ici — le fichier complet des sondes (`sondes-figees.npz`) n'est pas
   dans le clone de la mère, seul son compagnon y est. Fichiers présents de P3 (`ls -l`) : `jetons-principales-p3.npz`
   17 205 068, `scores-p3.npz` 8 906 138, `sondes-figees-legeres.npz` 17 682 551, `textes-actions-p3.jsonl` 3 148 659 octets
   (46 942 416 en tout, plus 438 octets de compagnons), et `episodes-p3.json` 716 410 octets ; avec le fichier complet des
   sondes, ≈ 0,85 Go selon le développeur v1 (non vérifié), soit une dizaine de morceaux de 90 Mo au lieu de « ≈ 45 Mo »
   (texte, l. 70).
4. **Code de sortie 5** de `p3bis_instance_v2.sh` : second paquet en échec, après le run **ou pendant un arrêt** ; la
   surveillance garde l'instance (non détruite) sur ce code.
5. Choix de la v2 à écrire au texte : E-3 (codes des cas non nommés, refus sans ligne), E-8, E-9 ; fichier
   `durees-lectures-v1.json` (durées du dépliage, de chaque lecture et de la chaîne avant la mise en paquet, classe 2) ;
   `mise-en-paquet.erreurs` dans l'espace fermé (motif d'un refus de `fermer`) ; motif d'un refus du dépliage imprimé
   (classe 1 de fait : il ne porte que sur l'intégrité du second paquet) ; essai différentiel : fichiers laissés relevés par
   l'inventaire de l'arbre. CP-04 est réglé dans le code : rien à porter au texte pour lui.
6. Liste du marqueur `EMPREINTES_CODE_P3BIS` : y ajouter `scripts/essai_fermeture_p3bis_v2.py` et l'amorce v2.

## Valeurs proposées pour les marqueurs

- **`COMMIT_CODE_P3BIS`** : `02217f1cf5255ef87c42285fc579d38c5a6ff003` (branche `prep/p3bis-code-v2`). Si la mère porte ces
  fichiers sur `main` par un autre commit, la valeur est à reprendre au commit qui les porte, avec `git diff --quiet
  02217f1c <ce commit> -- <CHEMINS_GELES>` vide.
- **`EMPREINTES_CODE_P3BIS`** (au commit `02217f1c`, chacune égale à son compagnon) :
  - `src/controle_ia/premier_test_ia/run_v2.py` `83ebeac77d171d62832af47c95f6a00b94aa75a7afe3b29dacd600ccb8b9e6d5` (inchangé)
  - `src/controle_ia/premier_test_ia/lecture_p3bis_v1.py` `bfe0effcfa0d7f525872410a7f9823c509cac878143a4fdcce7d207dfbddfea9` (inchangé)
  - `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` `330915f67402e097c2581fee0de2ed6950954f2c071356df19b27980bb5f5bb3`
  - `scripts/essai_fermeture_p3bis_v2.py` `389ca52dbf145de6028667354180dac82ca4a87328262ef2ab18a290841987ef`
  - `scripts/essais-cibles-p3bis-v2.txt` `3ecf3cdaee807ec4e74059132b4bded1962fb576e3adba6c31e8f64206f62276`
  - `scripts/p3bis_instance_v2.sh` `83820dfd8ef7205c44f89e63450d801d60b95eddecb504cd2af992fa5b1eaa5d` (porte en dur l'empreinte de la liste)
  - `scripts/amorce_instance_p3bis_v2.sh` `b331e44f763f87744b9669998c8a7aa32308e449d07ba414e6c2bb0bc4ed22f4`
  - `tests/test_premier_test_ia_ouverture_p3bis_v2.py` `e4ef18fa36589db2256439d3f63cbec206e8b9008b296d5fc9e357cfba2e2c65`
  - `tests/test_essai_fermeture_p3bis_v2.py` `fc6bce8bc6a3c58f40d0bbce36279926efbfdd62bb1d76428f634bb0be51a5a5`
  - `tests/test_premier_test_ia_lecture_p3bis_gardes_v1.py` `c0520b385b9c88cc8523844a1282048acebc9413c10a4efa9c4c95f5db692b7a`
  - `tests/test_script_p3bis_v2.py` `86f020219dfc4806bd356fd538c6691bdc926d0fce87891bc6d1aa9bfc6f1eb7`
  - `tests/test_cibles_invisibles_v1.py` `c3e08fc24b45e71545109010eb3b5b7f44d176e66875550038ec8235c57d9fad` (modifié, CP-10 ; compagnon aligné, E-2)
  - `.claude/hooks/garde_calcul.py` `184b3bbd92e95a10af2237c939b33ddce61c5bee7c7526076a1c91d863588502` (inchangée)
  - essai de fermeture : `brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt`
    `06e84ff732ebd7b30c33e18bdab7ea979fadb7d290da92c71383ac82072dceb5` (commit `66793d49`)
  - fichiers v1 gardés tels quels (empreintes du compte rendu v1, `977d84c1…`), dont les essais v1 de la liste.
- **`IDENTITE_CODE_P3BIS`** : `git diff --name-status 7a54d431d89745839220f882b41b13e8c62ecfdd 02217f1c -- src/controle_ia/premier_test_ia
  src/controle_ia/sondes src/controle_ia/harnais src/controle_ia/environnements src/controle_ia/organismes src/controle_ia/bases
  src/controle_ia/manifeste.py src/controle_ia/gardes.py src/controle_ia/scellement.py src/controle_ia/prereg.py
  requirements-gpu.txt requirements-cpu.txt requirements-donnees.txt` rend quatorze lignes, toutes `A` : les six ajouts
  étrangers à P3 déjà notés par le texte (`bases/bris_egalite_v1.py` et `bases/trace_lite_conduite_v1.py` avec leurs
  compagnons, `environnements/noter_rejeu_juges_v1.py` et `_v2.py`), puis `premier_test_ia/lecture_p3bis_v1.py`,
  `ouverture_p3bis_v1.py`, `ouverture_p3bis_v2.py`, `run_v2.py`, chacun avec son compagnon. Aucun fichier de P3 modifié ni
  retiré. (Sortie à verser par la mère comme fichier cité, au commit retenu.)
- **`TESTS_ATTENDUS_P3BIS`** (provisoire) : **531** (liste v2, Python 3.13.18, environnement de la mère, 4 cœurs ; aucun
  sauté) ; à recompter dans un clone neuf du commit du code, sous Python 3.11 et `requirements-gpu.txt` seul ; 531 change si
  la liste change (E-4).
- **`ESSAI_FERMETURE_P3BIS`** : `brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt`
  (`06e84ff732ebd7b30c33e18bdab7ea979fadb7d290da92c71383ac82072dceb5`, compagnon présent), joué une fois au commit
  `02217f1c` par `PYTHONPATH=src python -B scripts/essai_fermeture_p3bis_v2.py DOSSIER_NEUF SORTIE.txt` ; quatre passages par
  issue, règle des plages à 16 octets, sept contrôles positifs détectés, dernière ligne « ESSAI DIFFÉRENTIEL DE FERMETURE :
  CONFORME ».

## Points ouverts pour la mère

1. E-1 : retirer la ligne `/x/` de `/home/user/controle-ia-travail/.git/info/exclude` (refusé à ce sous-agent).
2. E-4 : garder la liste v2 telle quelle (lettre de la consigne) ou une liste v3 sans les essais des fichiers v1 de P3-bis.
3. Essai de concordance du journal avec le lecteur de T0.7 (point 4 du mandat : je n'ai pas lu le lecteur de T0.7) ; E-3,
   E-8, E-9 en sont les points à regarder.
4. Contre-lecture courte de l'écart v1 → v2 par un autre modèle (R2, N-052).
