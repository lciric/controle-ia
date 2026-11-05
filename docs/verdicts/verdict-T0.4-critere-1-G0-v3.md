# Verdict R13 — T0.4 v3, validation du harnais sur modèle réel — runs A `20261006-114025-validation-reelle` et B `20261006-115440-validation-reelle` — critère 1 de la porte G0 — v3

- Juge : sous-agent neuf (R13). Je ne suis l'auteur ni du préenregistrement, ni du code, ni de l'analyse, et je n'ai pas contre-lu le préenregistrement. Date : 2026-10-06 (UTC).
- Table appliquée : `prereg/T0.4-validation-modele-reel-v3.md`, sha256 `4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f`, section « Critères de lecture gelés ».
- Procédure suivie par le lancement : `docs/procedures/validation-T0.4-modele-reel-v4.md`, sha256 `4482f7cc66e60f30870390fb82640cec9497eb43f9119bd09d33d58ec21f73d8`.
- Critère jugé (`docs/brief-claude-code-programme-complet-v2.md`, ligne 192, porte G0) : « Harnais validé : déterminisme, équivalence d'activations, gardes testées ».
- Mes recalculs : dossier `recalculs/` (13 scripts, 20 sorties brutes), scellé par `recalculs/recalculs.sha256` (sha256 `c46d170cef791f350d36859300de316633efee8c8d5774e4648c4a7fb4603c2a`). Chaque chiffre ci-dessous renvoie à l'une de ces sorties, ou au résumé d'un run (empreintes en section 2).

## 1. Verdict

**Critère 1 de G0 : prouvé par ces deux runs.** Une seule ligne de la table s'applique : la première. P0 à P9, P2b et C1 à C3 sont conformes dans le run A ; P9 n'est pas déclenché ; la lecture du run B est égale à celle de A ; P7 est conforme. Lecture gelée : « harnais validé sur le modèle réel : preuve du critère 1 de G0 (déterminisme, équivalence, sensibilité au défaut D1 en double et en simple précision, gardes testées) ».

**Réserves au sens de la table : aucune.** Aucune ligne de réserve ne s'applique : ni le rapport au repère (au plus 0,66, seuil 3), ni le chargement (65 normalisations en double précision ; chemin en `torch.float32`, 0 en double), ni le débit (aucune panne de mémoire), ni les sondes d'audit (120 actions sur 120), ni le contexte des contrôles positifs (1,4e-13 et 1,0e-4, sous leurs seuils), ni P9.

**Observations sans effet sur la lecture gelée**, à porter à Lazar :
1. **Production : contexte identique au bit près.** Le préremplissage du lot coïncide au bit près avec la passe unique, aux 21 913 positions de contexte des 40 actions comparées et aux trois couches. C'est vrai aussi pour les 23 actions remplies à gauche. La garde de production de ce run lit donc les seuls écarts de la zone générée (médiane par jeton 0,012, au niveau du repère). L'audit (section 6.1) ne trouve pas de défaut de mesure. Le mécanisme, lui, n'est pas vérifiable sans la carte.
2. **Débit : contextes plus courts que prévu.** Les contextes mesurés font au plus 1 271 jetons (moyenne 1 042 pour le lot de 32), pas 2 048 : les transcriptions de production sont plus courtes que la troncature. Le pic de 41,2 Go ne vérifie donc pas l'estimation d'environ 85 Go pour 32 contextes de 2 048 jetons au noyau « math ». L'avantage budgétaire prêté à l'option (a) de N-011 reste à établir dans le devis. Selon le préenregistrement, s'il change le devis, c'est une proposition à Lazar.
3. **Domaine.** La production dépasse un peu le domaine strict du chemin : plus long contexte rempli 1 192 jetons contre 1 087 ; contexte comparé 1 161 contre 1 083 ; jetons générés relus 98 contre 92. Au-delà, seule la garde de production couvre, comme le préenregistrement le dit (contre-lecture 1, X-8).
4. **Ce qui est attesté sans être relu ici.** P8 (relecture du disque) et la conformité des fichiers du modèle aux empreintes publiées sont attestés par les gardes de l'instance, qui auraient arrêté le run. Je ne les relis pas : les fichiers npz sont sur le disque de l'instance arrêtée, et je n'ai pas d'accès réseau.

**Suite gelée** : ce verdict, puis Lazar (GO). Il ne porte que sur le critère 1 ; la porte G0 en compte huit.

## 2. Empreintes vérifiées

Chaque sha256 a été recalculé sur mon clone (`git clone --no-hardlinks`, HEAD `678900c9ab745e1e1b13c1294036acd88a4dae75`, égal au dépôt de référence ; arbre de travail propre). « Compagnon » : égal au fichier `.sha256` voisin. « Chaîne » : `verifier_resultat` du code cité, sans arrêt (résultat intact, manifeste intact, rattachement par empreinte). Sorties : `recalculs/01_empreintes_identite.sortie.txt` (ed1f2c80…), `07_documents_cites.sortie.txt` (323e9f03…), `08_historique_commits_instance.sortie.txt` (2f6c09d9…), `10_liste_empreintes.sortie.txt` (2c232f11…, liste complète des 105 fichiers des runs).

```
Préenregistrement, procédure, scripts de l'instance
4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f  prereg/T0.4-validation-modele-reel-v3.md (compagnon ; égal à la citation ; même contenu au commit de scellement ce54afd)
4482f7cc66e60f30870390fb82640cec9497eb43f9119bd09d33d58ec21f73d8  docs/procedures/validation-T0.4-modele-reel-v4.md (compagnon)
6d34fb18a2e21c83cd5dbb4627f30195838c15edfc2eed581f0d1674b96c6f19  scripts/amorce_instance_t04.sh au commit ce54afd (égal à la citation)
ae7050907c8062b015cf868569953906042e8b3fcf50441cd9ae745f79e2aefd  scripts/validation_t04_instance.sh au commit ce54afd (égal à la citation)

Manifestes (compagnon ; empreinte de configuration cohérente)
950ea6c29f6b1fd1a82278a906ae3dbfadfa20f13cdd80da558483edad32485a  runs/20261006-114025-validation-reelle/manifeste.json
09cb13b9456027ccac2118e5e25ccc2ab2eadf674baaab64cdeb9a37d5d6a2b7  runs/20261006-115440-validation-reelle/manifeste.json

Résultats : compagnon et chaîne conformes pour chacun (51 fichiers pour A, 52 pour B ; 48 trajectoires par run :
logique 8, contrôle positif 8, chemin 8, contrôle positif du chemin 8, production 16) ; aucun arret.json, aucun arret-comparaison
cb3c3e6ade03213f0eb9b204c6d354fdb6bfe4e2b4f612afe2608d2a31419030  diag/20261006-114025-validation-reelle/resume.json
13c7382239aefac111836ead2aee6d57c7962c4b4aab511a3c5624cd57adb608  diag/20261006-114025-validation-reelle/tests-instance.json
4f09046746abf694d4d83ec7c6cc9e6d570405343e17348c1fb729f17ecad4ad  diag/20261006-114025-validation-reelle/environnement-python.json
dcb0923bbf9ee71738035c3860665059a238dbe21b4e09db9925d3398a5ae1bc  diag/20261006-115440-validation-reelle/resume.json
7dc9f75e9974a61a851601a4cb9319f5c0d7acac424800bf69295a74d91609c9  diag/20261006-115440-validation-reelle/comparaison-20261006-114025-validation-reelle.json
504888550ceecd93d3f82994742874c5320b1d69238bcf6e3e83e5fef76601e6  diag/20261006-115440-validation-reelle/tests-instance.json
3495a87434c020f4b40daa24d3e440be27dd54d23879b8e190ee75d49cb5b205  diag/20261006-115440-validation-reelle/environnement-python.json

Traces (sha256sum -c empreintes.sha256 conforme dans chaque dossier)
5b2629bea564cc6564327e43e9b5911bfe7a8b95ee7b7969c0dfab7ce6bb7efd  traces/t04-20261006-120752-qRPl/empreintes.sha256
   (journal.txt e451463a…, tests.txt fa3aedb5…, tests.err vide : 0 octet, e3b0c442…, run-A.json 5413fc52…,
    run-A.err 6e28df75…, run-B.json 15195377…, run-B.err f63f716e…)
6ed2c3b003f491ab843ab59cec28908bf571d90bde03d51bbbe9dc78e4cd8c2f  traces/t04-instance-54476244-20261006-121128/empreintes.sha256
   (journal.txt 2730b775…, etats-surveillance.txt 6885a3b2…)

Documents cités en tête du préenregistrement (égaux aux citations)
886c8c07c6954a46c666b294c391523f0cdd3d03a5b99dae5079507503de3fb9  prereg/T0.4-validation-modele-reel-v2.md
98d53c70c09ff9b4c0eea4f7ae8779d6dfa10bb6401ca6ac4567283c6fac07cb  docs/verdicts/verdict-T0.4-critere-1-G0-v2.md
aed4bd6c9db802775071bb37ff2ca8939f4c81dc4a85e2fdd6a36f992a81b35b  docs/decisions/proposition-N-011-v1.md
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md (sha256sums-lancement-v2 : OK)
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md (idem)
16d71febf1491780ab1230ed1fb8e4d8b1bec47fbed202e0ef26ca666def04c2  livrables/premier-rendu-v1/devis-v1.md
b013428ab8502a61a3ea19404ea3a6cdc64ea6a587010c45627e33f13ef29148  docs/notes/memoire-double-precision-T0.4-v1.md
2e4e9683aaa8ea42d5f8bddb2fa26489a44485252b3fe1d461397e5beaf8d32b  docs/notes/memoire-noyau-math-T0.4-v3-v2.md
4eb2d92069e270631bf3e4d25345b44191cbe419d71a4f06725659c32846aeed  diag/20261005-102042-validation-reelle/arret.json (v1)
e3ca201edef75f50409e42848f5c4faee0c411dd4a169933751c08bb228c63e6  diag/20261005-144628-validation-reelle/arret.json (v2)
5188c13c8f52746dcb5ba5aa52c6df0671eb9618411a6950299d080658eb526d  docs/procedures/surveiller-instance-t04-v1.sh

Code cité b6ab5d1 (git show <commit>:<chemin>, identique dans mon clone)
d25e4cd92d73eef4d2bd6c7d17328daf49a49c76eab7afd91500d9c04ded8289  src/controle_ia/harnais/validation_reelle.py
61fd8470f491dce78e9dc833032ae829230c490a42e9c9461d740b87a7f3c5ae  src/controle_ia/harnais/episode.py
adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095  src/controle_ia/harnais/activations.py
c625a099fba580f098f3ce923b4cfa723c4cd3638f302c15f8fd74119d3a7797  src/controle_ia/harnais/modeles.py
0a85164c002a7993f951299e11e7beb6e67b9ba80e3394c46676353dde9dbd5f  src/controle_ia/harnais/politique.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2  src/controle_ia/scellement.py

Registres lus pour le contexte (non scellés ; à HEAD 678900c)
52f532a0b373327817885bf0cacfa8cd41d3201931d0b079fc15b3a2c18bc9ff  registres/decisions.md (R-048 à R-051)
5a02dd4eccd5e477413c0fbb72611c8c70a7fcb97fe5fe0108d76dd479c3a74a  registres/depenses.md
2f7da299264d5c33f6c3ead5ab426ca0ce29b2548510aa7465be54d640bd244d  registres/arrets.md
290e8df16afb0c06a3be32af199d341ea5c0d9eb5d1aa86002f67af5ad8c2aaf  registres/go.md
```

**Les deux runs sont bien ceux du préenregistrement** (`recalculs/01`, `08`) :
- commit de scellement du préenregistrement (celui qui ajoute son compagnon) : `ce54afd5b96ba3483182e2533fbbea49312f7c78`. Le code cité `b6ab5d1` en est un ancêtre ;
- commit du manifeste de A : `ce54afd`, le commit de scellement lui-même ;
- commit du manifeste de B : `29a00cf39bd52ffe2d2c770154aa58cdb0f43ea6`. C'est le commit des résultats de A, fait sur l'instance, de parent `ce54afd` ; il n'ajoute que `runs/` et `diag/` de A ;
- arbre gelé (chemins gelés du code cité) identique au code cité pour `ce54afd`, `29a00cf` et HEAD (`git diff --quiet` : 0) ;
- configuration des deux manifestes égale à `CONFIG_REELLE` du code cité, plus la révision citée ; empreinte de configuration recalculée `3e2f5811d643d3840f29ee43e091ea433d92521cb46561b82ddbaae5f9049ae7`, égale à celle consignée dans A et dans B ;
- révision `0e9e39f249a16976918f6564b8830bc894c89659` et entropie `86918527404142130934456531865900787761` égales aux citations. Les 838 graines (sondes 6, logique 160, chemin 160, production 320, contrôle positif 80, contrôle positif du chemin 80, débit 32) se refont à l'identique depuis l'entropie citée ; mêmes graines dans A et B ;
- manifestes décisifs, dépôt propre au lancement, aucune réserve, préenregistrement cité avec son empreinte ;
- commandes lancées par le script d'instance : `--revision <révision lue dans le préenregistrement> --prereg prereg/T0.4-validation-modele-reel-v3.md --sortie-tests <tests.txt>`, plus `--rejeu-de <A>` pour B ;
- fichiers des runs et des traces inchangés depuis leurs commits faits sur l'instance (`29a00cf`, `fc9d851`, `5e7087a`) ; fusionnés dans `main` par `59de002`.

## 3. Prédiction par prédiction

Valeurs recalculées par moi depuis les données par action des résumés (rapports, profils, `ecarts`, `ecarts_q99`, contrôles négatifs, lignes) et depuis les trajectoires scellées, pas depuis les bilans. Sorties : `recalculs/02_predictions_runA.sortie.txt` (7b694e46…) et `_runB` (feae9622…), valeurs `02_predictions_runA.valeurs.json` (84be69bf…, identique pour B) ; localisation `09_localisation_extremes_runA.sortie.txt` (52bd86bf…) ; P7 `03b_…sortie.txt` (15e7b91a…) ; P8 `11_stockage_relecture.sortie.txt` (136aab63…). Couches 7, 15 et 23.

| id | valeur recalculée | seuil ou règle | lecture gelée | lecture du code | accord |
|---|---|---|---|---|---|
| P0 | dernière ligne « 206 passed in 84.27s (0:01:24) » ; aucune autre marque (échec, erreur, test sauté, désélectionné ou attendu en échec) ; sortie d'erreur des tests vide (0 octet) ; sortie scellée identique aux traces | exactement 206 réussis, rien d'autre | conforme | `tests_instance` : conforme | oui |
| P1 | garde de format vérifiée (3 tours, 144 jetons) ; « Today Date: 26 Jul 2024 » dans l'ouverture décodée ; 10 fichiers du modèle conformes (dont 4 de poids), relevé identique à ceux de la v1 et de la v2 (même révision), même gabarit ; carte 139,8 Gio ; mémoire vive effective 734,5 Go | identité ; ≥ 130 Gio ; ≥ 96 Go | conforme | `format` : conforme (le reste : gardes passées, sans clé) | oui |
| P2 | maximum **3,10e-13** (épisode 1, action (1,9), couche 23, contexte) ; par couche 4,84e-14 / 1,87e-13 / 3,10e-13 ; contexte 3,10e-13, zone générée 3,16e-14 ; 40 actions ; couverture : 38 actions remplies, 39 finies avant la plus longue, 1 327 positions générées comparées, lignes {1, 6} | ≤ 1e-4 ; couverture | conforme | `logique_equivalence` : conforme | oui |
| P2b | 20 actions comparables, **20 vues** (100 %), aucune courte ; minimum des maxima **8,29e-2** (épisode 1, action (0,0), couche 23) ; minima par couche 0,213 / 0,161 / 0,0829 ; maximum du contexte 1,44e-13 | ≥ 95 % d'au moins 10 comparables, seuil 1e-4 | conforme | `controle_positif` : conforme | oui |
| P3 | 40 comparables, 40 passent ; minimum 1,06 (épisode 1, action (1,6), couche 15 ; 23 positions décalées sur 23 au-dessus du seuil) | ≥ 95 % d'au moins 10, seuil 1e-4 | conforme | `logique_controle_negatif` : conforme | oui |
| C1 | maximum **3,16e-4** (épisode 6, action (1,5), couche 23, contexte) ; par couche 3,50e-5 / 1,24e-4 / 3,16e-4 ; contexte 3,16e-4, zone générée 4,77e-5 ; 40 actions ; couverture : 31 remplies, 31 finies avant, 2 000 positions générées, lignes {1, 6} | ≤ 3e-3 ; couverture | conforme | `chemin_equivalence` : conforme | oui |
| C2 | 20 comparables, **20 vues** ; minimum des maxima **6,81e-2** (épisode 1, action (1,4), couche 23) ; minima par couche 0,242 / 0,127 / 0,0681 ; maximum du contexte 1,01e-4 | ≥ 95 % d'au moins 10, seuil 3e-3 | conforme | `controle_positif_chemin` : conforme | oui |
| C3 | 40 comparables, 40 passent ; minimum 1,11 (épisode 6, action (0,1), couche 15 ; 33 sur 33) | ≥ 95 % d'au moins 10, seuil 3e-3 | conforme | `chemin_controle_negatif` : conforme | oui |
| P4 | plus grand 99e centile par action et par couche **0,0334** (épisode 14, action (1,0), couche 15) ; par couche 0,0176 / 0,0334 / 0,0290 ; aucune des 120 valeurs (40 actions × 3 couches) au-dessus de 0,2 ; maximum rapporté sans seuil 0,162 (épisode 1, action (0,0), couche 23, zone générée) | chaque 99e centile ≤ 0,2 | conforme | `production_equivalence` (sur `ecart_q99_max`) : conforme | oui |
| P5 | 40 comparables, 40 passent ; minimum 1,004 (épisode 1, action (1,6), couche 15 ; 26 sur 26) ; zone générée décalée : de 2,3 % à 39,3 % des n − 1 positions lues ; au moins k(n − 1) + 10 positions pour chaque action (section 5.5) | ≥ 95 % d'au moins 10, seuil 0,2 sur le 99e centile décalé | conforme | `production_controle_negatif` : conforme | oui |
| P6 | lot 0 rejoué (épisodes 0 à 7) : 5 empreintes identiques par épisode (trajectoire, activations, logits, vecteurs, scores) ; 20 empreintes de captures identiques (épisode 1, seul échantillonné du lot) ; empreintes des logits par action identiques | identité | conforme | `rejeu_en_processus` : conforme | oui |
| P7 | comparaison scellée : identique, aucune différence, lecture conforme. Ma comparaison, plus stricte (tous les champs des deux résumés) : 29 chemins différents, tous dans les durées, les débits, les pics de mémoire et la projection d'heures ; 16 fichiers npz de même empreinte ; 50 autres fichiers de `diag/` identiques (hors enveloppe) ; lectures identiques (12 clés) ; aucun arrêt de B | identité | conforme | `comparer_runs` : identique, conforme | oui |
| P8 | aucun `arret.json` ; or la garde de relecture (`relire_et_controler`, arrêt à toute différence) s'applique aux 16 épisodes avant le rejeu ; activations par jeton conservées pour les épisodes 1 et 14 ; codage de 2 octets par valeur (8 192 octets par jeton et par couche) ; empreintes des 16 npz identiques dans A et dans B | identité | conforme (attesté par le code et l'absence d'arrêt ; non relu ici) | pas de clé | oui |
| P9 | écarts nuls dans la zone générée, à chaque couche : 0 sur 1 327 (logique), 0 sur 2 000 (chemin), 0 sur 2 006 (production) | au moins un écart non nul par phase | non déclenché | `audit_symetrie` : non déclenché | oui |

- Tous les bilans consignés (A et B) sont égaux à mes recalculs : maximum, plus grand 99e centile, maxima par zone, couverture, domaine, contrôle négatif, zéros, sondes d'audit, bilans des deux contrôles positifs.
- Cohérence interne vérifiée pour les 120 actions comparées : `ecarts` = maximum du profil ; `ecarts_q99` = 99e centile du profil (deux calculs distincts du code, égaux au bit près) ; jetons du profil = positions capturées ; positions décalées du contrôle négatif = m − 1.
- `lire` du code, rejoué sur chaque résumé, rend la lecture consignée ; mes lectures, refaites depuis les données par action, sont identiques pour les 10 clés comparables.
- Cohérence avec les trajectoires (`recalculs/04`, `05`) : pour les 120 actions comparées et les 40 des contrôles positifs, le contexte capturé égale le début de l'action ; la zone générée relue compte les jetons générés (ligne finie avant les autres) ou un de moins (ligne la plus longue du lot, dont le dernier jeton n'est pas relu). Le remplissage recalculé depuis les 8 trajectoires de chaque lot égale le champ `lignes`. Les 36 empreintes de trajectoires résumées se recalculent à l'identique.
- P8 en détail : section 6.8.

## 4. Lignes de la table appliquées et suite prescrite

| ligne de la table | s'applique ? | pourquoi |
|---|---|---|
| **P0 à P9, P2b et C1 à C3 conformes dans A, P9 non déclenché ; lecture de B égale à celle de A ; P7 conforme** | **oui** | toutes conformes (section 3) ; B complet, lecture identique, comparaison identique |
| P0 contraire | non | 206 réussis, rien d'autre |
| P1 contraire | non | toutes les gardes de P1 passées |
| P2 contraire (> 1e-4) | non | 3,10e-13 |
| P2 : ≤ 1e-2, diffus (maxima du contexte et de la zone générée ≥ 1e-5, rapport ≤ 3) | non | P2 conforme ; maxima de 3,1e-13 et 3,2e-14, sous 1e-5 |
| P2 non concluant (couverture) | non | 38 remplies, 39 finies avant, 1 327 positions générées, lignes {1, 6} |
| P2b contraire | non | 20 sur 20 |
| P2b non concluant (< 10 comparables) | non | 20 comparables |
| P2 non concluant, P2b contraire ou non concluant | non | aucun des deux |
| contrôle positif de la logique : maximum du contexte > 1e-4 | non | 1,44e-13 |
| C1 contraire (> 3e-3) | non | 3,16e-4 |
| C1 non concluant (couverture) | non | 31 remplies, 31 finies avant, 2 000 positions générées, lignes {1, 6} |
| C2 contraire | non | 20 sur 20 |
| C2 non concluant | non | 20 comparables |
| C1 non concluant, C2 contraire ou non concluant | non | aucun des deux |
| contrôle positif du chemin : maximum du contexte > 3e-3 | non | 1,01e-4 |
| P3, C3 ou P5 contraire | non | 40 sur 40 dans chacune des trois phases |
| P3, C3 ou P5 non concluant | non | 40 comparables dans chacune |
| P4 contraire (un 99e centile > 0,2) | non | 0,0334 au plus |
| P4 conforme, et ρ_ℓ > 3 à une couche | non | 0,656, 0,550, 0,391 |
| P6 contraire | non | 8 épisodes identiques |
| P7 contraire (différence, lecture de B ≠ A, ou arrêt de B) | non | aucune différence, lectures égales, B complet |
| P8 contraire | non | aucun arrêt de relecture |
| P9 déclenché | non | écarts non nuls dans la zone générée des trois phases |
| chargement non conforme | non | 65 normalisations en double précision ; chemin `torch.float32`, 0 en double |
| débit : panne de mémoire consignée | non | `debit.panne_memoire` faux ; lots de 1, 8 et 32 mesurés |
| sondes d'audit en défaut dans une phase | non | tableaux distincts et unité au dernier rang vue pour 40 actions sur 40, dans chaque phase |
| arrêt de A ou de B pour une cause d'infrastructure | non | A et B complets (résumés sans arrêt, comparaison écrite) |
| arrêt de A ou de B pour une cause déterministe | non | aucun arrêt |
| arrêt de cause indéterminée | non | aucun arrêt |
| A et B complets, résultats non poussés | non | branche `calcul/t04-validation-v3` poussée (journal, 12:07:54 UTC), fusionnée dans `main` (`59de002`) |

**Règle de cumul.** Une seule ligne s'applique, la première, seule à valider le critère 1. Aucune autre lecture ni suite ne s'y ajoute.

**Prédictions non atteintes.** Aucune : toutes les phases ont été jouées dans A et dans B ; le run B a été lancé, il est complet, et sa comparaison est écrite.

**Suite prescrite par la première ligne** (je la recopie) : « verdict par sous-agent neuf, puis Lazar ». Selon R13, ce verdict est scellé, puis soumis à Lazar pour GO. Étapes que le préenregistrement et la procédure placent après ce verdict (je n'en décide aucune) : décider de la destruction de l'instance 54476244, arrêtée avec son disque (irréversible : à soumettre à Lazar avec une recommandation) ; produire le zip versionné des livrables de T0.4 (R12) ; consigner le domaine de validité observé dans `registres/decisions.md`.

## 5. Valeurs confiées au juge

Sorties : `recalculs/04_valeurs_juge_runA.sortie.txt` (0d27388f…), valeurs `04_valeurs_juge_runA.valeurs.json` (c97f2c37…, identique pour B), et `12_zeros_par_phase_runA.sortie.txt`.

### 5.1 Rapport au repère ρ_ℓ

Définition de la Métrique : plus grand 99e centile par action de la production à la couche ℓ (`production.episodes[k].equivalence.ecarts_q99`), divisé par le 99e centile du repère à la même couche (`production.repere_precision`).

| couche | plus grand 99e centile par action | action | 99e centile du repère | ρ_ℓ |
|---|---|---|---|---|
| 7 | 0,01762 | épisode 1, (0,0) | 0,02685 | **0,656** |
| 15 | 0,03342 | épisode 14, (1,0) | 0,06077 | **0,550** |
| 23 | 0,02900 | épisode 14, (1,0) | 0,07426 | **0,391** |

Tous sous 3 : la ligne « P4 conforme, ρ_ℓ > 3 » ne s'applique pas. Aucun n'est sous 1/3 (rien à rapporter à ce titre). Pour mémoire, la v2 donnait 1,19, 1,02 et 1,14, aux noyaux par défaut.

### 5.2 Chargements

- Logique : `torch.float64`, attention `sdpa`, **65 normalisations en double précision** (2 par bloc × 32 blocs, plus la normalisation finale) : conforme au nombre attendu.
- Chemin : `torch.float32`, attention `sdpa`, **0 normalisation en double précision** : conforme.
- Les deux chargements sont identiques dans A et dans B. La ligne « chargement non conforme » ne s'applique pas.

### 5.3 Contrôles positifs : séparation entre D1 et l'arrondi, maximum du contexte

| contrôle positif | minimum des maxima (D1) | maximum de sa phase | séparation | marge au seuil | maximum du contexte | seuil |
|---|---|---|---|---|---|---|
| logique (P2b) | 8,29e-2 | 3,10e-13 (P2) | **2,7e11** (11,4 ordres de grandeur) | 829 fois 1e-4 | **1,44e-13** | 1e-4 |
| chemin (C2) | 6,81e-2 | 3,16e-4 (C1) | **216** | 22,7 fois 3e-3 ; le seuil vaut 9,5 fois le maximum de C1 | **1,01e-4** | 3e-3 |

Le contexte de chaque contrôle positif reste au niveau de sa phase (1,4e-13 contre 3,1e-13 ; 1,0e-4 contre 3,2e-4) : aucune des deux lignes « maximum du contexte du contrôle positif » ne s'applique.

### 5.4 Domaines observés

| phase | contexte comparé (max) | jetons générés relus (max) | taille de lot | plus long contexte rempli d'un lot |
|---|---|---|---|---|
| logique | 1 028 | 65 | 8 | 1 559 |
| contrôle positif de la logique | 491 | 58 | 8 | 556 |
| **chemin** (domaine strict, seuil 3e-3) | **1 083** | **92** | **8** | **1 087** |
| contrôle positif du chemin | 576 | 114 | 8 | 682 |
| **production** | **1 161** | **98** | **8** | **1 192** |

La production dépasse un peu le domaine strict du chemin (observation 3 de la section 1). La logique, en double précision, couvre un contexte rempli plus long (1 559), mais pas le chemin de production.

### 5.5 Part de la zone générée, pour chaque action comparée de la production

Le contrôle négatif de la production lit n − 1 positions : le contexte non décalé (ℓ_c positions) et la zone générée décalée (m − 1 positions), la première position générée exclue. Un décalage confiné à la zone générée atteint sûrement le 99e centile si elle compte au moins k(n − 1) positions, avec k(N) = N − ⌊0,99 (N − 1)⌋. Aucune action n'échoue à P5. Pour toutes, la zone décalée dépasse k(n − 1) d'au moins 10 positions. Tri par part croissante ; le q99 décalé est le plus petit des trois couches.

| épisode, action | n | contexte | m | (m − 1)/(n − 1) | k(n − 1) | marge | q99 décalé |
|---|---|---|---|---|---|---|---|
| épisode 1, (1,9) | 908 | 886 | 22 | 2,3 % | 11 | 10 | 1,024 |
| épisode 1, (1,6) | 641 | 614 | 27 | 4,1 % | 8 | 18 | 1,004 |
| épisode 1, (1,8) | 828 | 792 | 36 | 4,2 % | 10 | 25 | 1,065 |
| épisode 1, (0,9) | 1 214 | 1 161 | 53 | 4,3 % | 14 | 38 | 1,031 |
| épisode 14, (0,7) | 899 | 858 | 41 | 4,5 % | 10 | 30 | 1,056 |
| épisode 14, (0,9) | 1 124 | 1 072 | 52 | 4,5 % | 13 | 38 | 1,042 |
| épisode 14, (1,9) | 1 126 | 1 073 | 53 | 4,6 % | 13 | 39 | 1,053 |
| épisode 1, (1,7) | 732 | 697 | 35 | 4,7 % | 9 | 25 | 1,054 |
| épisode 14, (0,8) | 1 013 | 956 | 57 | 5,5 % | 12 | 44 | 1,029 |
| épisode 14, (1,8) | 1 007 | 947 | 60 | 5,9 % | 12 | 47 | 1,062 |
| épisode 14, (1,7) | 885 | 831 | 54 | 6,0 % | 10 | 43 | 1,035 |
| épisode 14, (1,6) | 768 | 721 | 47 | 6,0 % | 9 | 37 | 1,053 |
| épisode 1, (0,7) | 968 | 909 | 59 | 6,0 % | 11 | 47 | 1,067 |
| épisode 14, (0,6) | 799 | 744 | 55 | 6,8 % | 9 | 45 | 1,112 |
| épisode 1, (0,6) | 856 | 796 | 60 | 6,9 % | 10 | 49 | 1,050 |
| épisode 14, (1,5) | 659 | 611 | 48 | 7,1 % | 8 | 39 | 1,089 |
| épisode 1, (0,8) | 1 104 | 1 024 | 80 | 7,2 % | 13 | 66 | 1,071 |
| épisode 1, (1,5) | 559 | 513 | 46 | 8,1 % | 7 | 38 | 1,084 |
| épisode 1, (1,4) | 459 | 421 | 38 | 8,1 % | 6 | 31 | 1,123 |
| épisode 14, (0,5) | 688 | 624 | 64 | 9,2 % | 8 | 55 | 1,092 |
| épisode 1, (1,3) | 368 | 333 | 35 | 9,3 % | 5 | 29 | 1,066 |
| épisode 14, (1,4) | 551 | 498 | 53 | 9,5 % | 7 | 45 | 1,148 |
| épisode 1, (0,5) | 743 | 669 | 74 | 9,8 % | 9 | 64 | 1,189 |
| épisode 1, (1,2) | 278 | 248 | 30 | 10,5 % | 4 | 25 | 1,022 |
| épisode 14, (1,3) | 435 | 387 | 48 | 10,8 % | 6 | 41 | 1,136 |
| épisode 14, (1,2) | 325 | 284 | 41 | 12,3 % | 5 | 35 | 1,089 |
| épisode 14, (0,4) | 564 | 493 | 71 | 12,4 % | 7 | 63 | 1,146 |
| épisode 14, (0,3) | 432 | 374 | 58 | 13,2 % | 6 | 51 | 1,091 |
| épisode 1, (0,4) | 616 | 532 | 84 | 13,5 % | 8 | 75 | 1,169 |
| épisode 1, (1,1) | 191 | 160 | 31 | 15,8 % | 3 | 27 | 1,058 |
| épisode 14, (1,1) | 222 | 185 | 37 | 16,3 % | 4 | 32 | 1,203 |
| épisode 14, (0,2) | 314 | 258 | 56 | 17,6 % | 5 | 50 | 1,131 |
| épisode 1, (0,2) | 322 | 262 | 60 | 18,4 % | 5 | 54 | 1,159 |
| épisode 1, (0,3) | 477 | 379 | 98 | 20,4 % | 6 | 91 | 1,124 |
| épisode 1, (0,1) | 204 | 158 | 46 | 22,2 % | 4 | 41 | 1,130 |
| épisode 1, (1,0) | 103 | 79 | 24 | 22,5 % | 3 | 20 | 1,087 |
| épisode 14, (0,1) | 196 | 149 | 47 | 23,6 % | 3 | 43 | 1,252 |
| épisode 14, (0,0) | 104 | 68 | 36 | 34,0 % | 3 | 32 | 1,118 |
| épisode 14, (1,0) | 124 | 79 | 45 | 35,8 % | 3 | 41 | 1,199 |
| épisode 1, (0,0) | 113 | 68 | 45 | 39,3 % | 3 | 41 | 1,281 |

Contrôle de cohérence indépendant du 99e centile décalé (`recalculs/02`) : pour chaque action et chaque couche, le nombre de positions décalées au-dessus de 0,2 (`au_dessus`, calculé à part) est compatible avec le 99e centile consigné. Il y a au moins k valeurs au-dessus du seuil, donc un 99e centile au-dessus : aucune incohérence sur 120. Rapportée à toutes les positions (m/n), la zone générée fait de 2,4 % à 39,8 % des positions de chaque action (v2 : 2,7 % à 41 %).

### 5.6 Sondes d'audit

Tableaux distincts en mémoire et perturbation d'une unité au dernier rang vue : 40 actions sur 40 en logique, 40 sur 40 dans le chemin, 40 sur 40 en production (`recalculs/04`). Aucune ligne « sondes d'audit en défaut ».

### 5.7 Panne de mémoire du débit

`debit.panne_memoire` est faux, dans A et dans B. Les trois lots (1, 8, 32) sont mesurés, sans erreur, au noyau « math ».

## 6. Audit de symétrie (R4)

Un succès trop propre reçoit le même audit qu'un échec. Sorties : `recalculs/05_localisation_zeros_trajectoires_runA.sortie.txt` (e5d2cdd9…, identique pour B), `09` et `12`.

### 6.1 Production : un contexte identique au bit près

**Constat.**
- Aux trois couches, les 21 913 positions de contexte des 40 actions comparées ont un écart exactement nul. C'est vrai pour les 17 actions sans remplissage et pour les 23 actions remplies à gauche (remplissage de 2 à 306 jetons).
- La zone générée, au contraire, n'a aucun écart nul : 0 sur 2 006 par couche. Médiane, sur les actions et les couches, du q50 par jeton : 0,0117 ; maximum 0,162. Le niveau ne dépend pas du remplissage : médiane, sur les actions, du q50 (médian sur les couches) 0,0119 sans remplissage, 0,0118 avec (`recalculs/05`).
- Conséquence : le 99e centile de chaque action est porté par sa zone générée. Pour l'action où elle pèse le moins (2,4 % des positions), il vaut à peu près la dixième plus grande valeur de la zone générée. P4 serait aussi conforme sur le maximum (0,162 < 0,2).

**Ce qui exclut une capture recopiée de la passe unique.**
- Le code de capture est le même dans les trois phases. Dans ce même run, au même noyau, le contexte s'écarte de la passe unique en simple précision (chemin : 68 positions nulles sur 20 855, maximum 3,2e-4) et en double précision (logique : aucune sur 19 257).
- Le contexte et la zone générée viennent des mêmes crochets, posés pendant le même appel de génération ; la passe unique vient d'un appel séparé, plus tard. La zone générée s'écarte partout.
- Décalée d'un jeton, la comparaison donne au moins 1,004 (P5). Les deux tableaux sont distincts en mémoire. Une unité au dernier rang se voit (sondes d'audit, 40 sur 40).
- Dans la v2, aux noyaux par défaut et avec le même mécanisme de capture, le contexte des lignes remplies s'écartait jusqu'à 0,52 ; seules les lignes sans remplissage coïncidaient au bit près.

**Explication plausible, que je ne peux pas vérifier sans la carte.**
- Au noyau « math », l'attention est faite de produits de matrices et d'une normalisation par ligne, en simple précision ; les positions masquées du remplissage y comptent pour des zéros exacts. Le remplissage change donc peu l'ordre des sommes, contrairement au noyau par tuiles de la v2.
- Les rares écarts au dernier rang de la simple précision disparaissent le plus souvent à l'arrondi en demi-précision, qui ne garde que 8 bits de mantisse.
- Au décodage, chaque pas ne porte que sur une position par ligne : les produits de matrices ont une autre forme, et la bibliothèque somme dans un autre ordre. D'où des écarts d'arrondi à chaque position générée, au niveau du repère.
- Indice dans les données : en double précision, deux actions remplies du contrôle positif de la logique ont aussi un contexte identique au bit près, alors que les deux actions non remplies de la logique ne l'ont pas (5e-14). Ce n'est donc pas le remplissage qui décide de la coïncidence ; les formes de calcul semblent le faire.

**Lecture.** Le préenregistrement confie la propreté excessive à P9 et aux sondes d'audit (« Seuil », dernier point sur le rapport au repère). Ni l'un ni les autres ne se déclenchent. Il prévoit aussi ce cas : coïncidence au bit près au noyau « math » sur processeur, génération et passe unique qui partagent leurs arrondis. Je n'en tire pas de réserve. Je le rapporte, avec une conséquence pratique : dans ce régime, la grandeur de la garde de production dépend de la seule zone générée. La limite déclarée (zone générée de moins d'environ 1 % des positions d'une action) y pèse donc pleinement : sous ce seuil, le 99e centile tomberait sur les zéros du contexte. Dans ce run, la zone générée décalée compte au moins 2,3 % des positions lues, avec au moins 10 positions de marge (section 5.5).

### 6.2 Zéros et niveaux des écarts, par phase

Nuls / positions, par couche (identiques aux trois couches), et médiane du q50 par action et par couche (`recalculs/12`).

| phase | contexte : nuls / positions | médiane du q50, contexte | zone générée : nuls / positions | médiane du q50, zone générée | actions à contexte exactement nul |
|---|---|---|---|---|---|
| logique | 0 / 19 257 | 1,0e-14 | 0 / 1 327 | 8,1e-15 | 0 sur 40 |
| contrôle positif de la logique | 858 / 5 214 | 1,1e-14 | 0 / 748 | 0,034 (D1) | 3 sur 20 (1 non remplie, 2 remplies) |
| chemin | 68 / 20 855 | 5,7e-6 | 0 / 2 000 | 3,2e-6 | 1 sur 40 (non remplie) |
| contrôle positif du chemin | 68 / 5 555 | 5,4e-6 | 0 / 1 101 | 0,024 (D1) | 1 sur 20 (non remplie) |
| production | 21 913 / 21 913 | 0 | 0 / 2 006 | 0,012 | 40 sur 40 |

P9 ne porte que sur la zone générée : aucun écart nul dans aucune phase, donc aucun déclenchement.

### 6.3 Sondes d'audit : ce qu'elles montrent et ce qu'elles ne montrent pas

- Elles montrent que les deux tableaux sont distincts en mémoire, et qu'une unité au dernier rang, dans le type de la capture, change l'écart : la mesure n'est pas aveugle.
- Elles ne montrent pas que les valeurs capturées viennent du chemin de génération : une copie des valeurs de la passe unique, dans un tableau distinct, les passerait aussi. Ce point est établi autrement : D1 vu (sections 3 et 6.6), zone générée non nulle partout, écarts du contexte non nuls en simple et en double précision (section 6.1).

### 6.4 Ordres de grandeur attendus contre observés

Les ordres « attendus » du préenregistrement sont des estimations ; un écart à l'intérieur des seuils ne réfute rien.

| prédiction | attendu | observé | dans l'ordre attendu ? |
|---|---|---|---|
| P2 | 1e-16 à 1e-11 | 3,10e-13 | oui |
| P2b | écarts de 1e-2 à 1 dans la zone générée | minimum des maxima 8,29e-2 ; maximum 0,683 | oui |
| P3 | écarts décalés de 0,1 à 2 | par action, de 1,06 à 1,40 | oui |
| C1 | 1e-5 à 5e-4 | 3,16e-4 | oui |
| C2 | 1e-2 à 1 | minimum des maxima 6,81e-2 ; maximum 0,637 | oui |
| C3 | 0,1 à 2 | par action, de 1,11 à 1,43 | oui |
| P4 | 2e-2 à 1,2e-1 | 3,34e-2 | oui |
| P5 | 0,3 à 2 | par action, de 1,004 à 1,28 | oui |

Rien n'est hors de l'ordre attendu, ni par excès ni par défaut.

### 6.5 Recoupements entre phases, et avec la v1 et la v2

- **D1 ne dépend pas de la précision.** Minima par couche du contrôle positif : 0,213 / 0,161 / 0,083 en double précision, 0,242 / 0,127 / 0,068 en simple précision (v2, double précision : 0,247 / 0,116 / 0,057). C'est ce qu'annonce le préenregistrement : D1 est une erreur de logique.
- **Le décalage d'un jeton non plus.** Les contrôles négatifs valent de 1,0 à 1,4 dans les trois phases.
- **Profil d'arrondi, pas de signature de décodage.** En logique et dans le chemin, le contexte s'écarte plus que la zone générée : 3,1e-13 contre 3,2e-14, et 3,2e-4 contre 4,8e-5. C'est le préremplissage d'un lot de 8, comparé à une passe unique d'une autre longueur. Un défaut de décodage se logerait dans la zone générée, comme D1.
- **Repère.** Au noyau « math » (v3) : 99e centiles 0,0269 / 0,0608 / 0,0743. Aux noyaux par défaut (v2) : 0,0290 / 0,0671 / 0,0874. Médianes de 0,013 à 0,015 dans les deux cas. Le 99e centile le plus haut du repère de ce run (0,074) reste sous 0,1 : le seuil de 0,2 garde sa marge de deux fois le repère.
- **Logique.** 3,1e-13, contre 9,8e-13 dans la v2.
- **Chemin.** 3,2e-4, contre 1,27e-4 dans la v1 (simple précision stricte, carte A100). C'est 2,5 fois plus, dans l'ordre attendu, et 9,5 fois sous le seuil.
- **Fichiers du modèle et gabarit** : relevés identiques à ceux de la v1 et de la v2 (10 fichiers sur 10, même gabarit).
- **Mémoire.** Logique 84,5 Go pour un contexte rempli de 1 559 jetons, contre 78,3 Go pour 1 226 dans la v2 ; contrôle positif 69,0 contre 69,8 Go ; production 21,8 contre 19,0 Go.

### 6.6 D1 vu, et pour la bonne raison

- Dans les deux phases strictes, D1 est vu à chaque couche pour 20 actions sur 20.
- Le contexte des contrôles positifs reste au niveau de sa phase (1,4e-13 ; 1,0e-4) : pas de désalignement propre à la phase.
- Dans le code, la seule différence avec la phase est `decalage_positions`, qui ne touche que la position des jetons décodés ; même modèle en mémoire, même noyau, même processus. Graines propres : 80 tâches `controle-positif/…` et 80 `controle-positif-chemin/…` ; T = 5.
- Portée, prévue par le préenregistrement : domaine plus court que celui de sa phase (contexte rempli 556 et 682, contre 1 559 et 1 087). D1 décale toutes les positions décodées ; il ne dit rien d'un défaut plus fin (une seule position, un seul pas).
- En production, il n'y a pas de contrôle positif, par construction. La sensibilité de la garde de production au décalage d'un jeton est établie par P5.

### 6.7 Rapports au repère

ρ = 0,656, 0,550, 0,391 : dans [1/3, 3], sans réserve ni remarque. La production s'écarte de la passe unique moins que la demi-précision ne s'écarte de la double précision. C'est cohérent avec un contexte exact et une zone générée au niveau du repère (médiane 0,012 contre 0,013 à 0,015).

### 6.8 Rejeux et relecture

- **P7.** Les deux runs sont deux processus distincts : manifestes différents (950ea6c2… et 09cb13b9…), commits différents, créations à 11:40:27 et 11:54:42, durées de 848 et 789 secondes. Les 29 différences, toutes dans les champs descriptifs, montrent que la comparaison ne compare pas un run à lui-même. Hors de ces champs, tout est identique au bit près, y compris les profils d'équivalence, les captures, le repère, les contrôles positifs et les 16 fichiers npz (par leur empreinte).
- **P6.** Limité au lot 0 de la production ; les captures n'y existent que pour l'épisode 1 (20 actions). La logique et le chemin ne sont pas rejoués dans le processus, mais ils le sont entre processus (P7).
- **P8.** Attesté par l'ordre du code et par l'absence d'arrêt. Pour chacun des 16 épisodes, `relire_et_controler` relit le fichier npz, compare vecteurs et scores au bit près et, pour les épisodes 1 et 14, les activations par jeton à toutes les positions, puis refait vecteurs et scores hors ligne. Toute différence arrête le run. Les empreintes des 16 fichiers sont consignées et identiques dans A et B. Je ne peux pas relire ces fichiers.

### 6.9 Trace d'instance

L'amorce a fini à 12:07:54 UTC avec le code 0. Le conteneur l'a ensuite relancée 18 fois, entre 12:08:08 et 12:11:18. La garde R12 l'a refusée chaque fois (« dossiers d'un essai précédent présents »). C'est le comportement attendu du mode « args » (procédure v4, section 4). La session a arrêté l'instance par son identifiant à 12:11:10 (R10). Sans effet sur la lecture.

### 6.10 Conclusion d'audit

- Le succès n'est pas « trop beau » au sens de la table : P9 et les sondes d'audit ne se déclenchent pas.
- Tous les ordres de grandeur sont dans les fourchettes annoncées. D1 est vu dans les deux phases strictes, et le décalage d'un jeton dans les trois phases.
- Le seul trait de propreté inattendue est le contexte exact de la production. Il est expliqué de façon cohérente par les données, sans défaut de mesure trouvé. Je le rapporte comme observation, pas comme réserve.

## 7. Descriptifs

Sorties : `recalculs/04_valeurs_juge_runA.sortie.txt` et `_runB` (7df8ebb4…), `11` (136aab63…).

### 7.1 Repère de précision

Passe unique en demi-précision, au noyau de production, contre passe unique de la logique (double précision), sur les transcriptions des épisodes 1 et 6 de la logique (3 751 jetons par couche ; recoupé avec les trajectoires). Identique dans A et B.

| couche | q50 | q99 | maximum |
|---|---|---|---|
| 7 | 0,01308 | 0,02685 | 0,05136 |
| 15 | 0,01484 | 0,06077 | 0,49929 |
| 23 | 0,01327 | 0,07426 | 0,77429 |

### 7.2 Maxima de la production, rapportés au maximum du repère

| couche | maximum de la production | où | maximum du repère | rapport |
|---|---|---|---|---|
| 7 | 0,0420 | épisode 1, (1,5), zone générée, remplissage 215 | 0,0514 | 0,82 |
| 15 | 0,0950 | épisode 1, (0,0), zone générée, sans remplissage | 0,4993 | 0,19 |
| 23 | 0,1622 | épisode 1, (0,0), zone générée, sans remplissage | 0,7743 | 0,21 |

### 7.3 Mémoire et vitesse, par phase

Pics de mémoire de la carte en Go (10⁹ octets), identiques dans A et B sauf le débit ; vitesses de A (B entre parenthèses).

| phase | pic de mémoire | génération (jetons/s) | passe unique (jetons/s) | plus long contexte rempli |
|---|---|---|---|---|
| logique | 84,46 | 42,9 (51,0) | 2 088 (2 065) | 1 559 |
| contrôle positif de la logique | 69,01 | 72,8 (75,5) | 2 757 (2 945) | 556 |
| chemin | 38,21 | 64,1 (65,6) | 2 647 (2 638) | 1 087 |
| contrôle positif du chemin | 35,31 | 73,9 (74,0) | 2 576 (2 629) | 682 |
| production | 21,75 | 90,3 (92,6) | 11 526 (11 465) | 1 192 |
| débit | 41,16 (41,16) | voir 7.4 | — | 1 271 |

Estimations de la note de mémoire : chemin environ 65 Go à la borne (mesuré 38,2 Go à 1 087 jetons), production moins de 60 Go (21,8 Go), débit environ 85 Go pour 32 contextes de 2 048 jetons (41,2 Go mesurés, à au plus 1 271 jetons).

### 7.4 Débit, projections, stockage

- Débit au noyau « math », génération seule de 128 jetons par ligne, sans arrêt anticipé :
  - lot de 1 : 30,3 (34,6) jetons/s, contexte de 1 162 jetons ;
  - lot de 8 : 108,8 (108,9) jetons/s, contexte moyen 1 083, maximum 1 268 ;
  - lot de 32 : 118,8 (122,7) jetons/s, contexte moyen 1 042, maximum 1 271.
  - Aucune panne. Le passage de 8 à 32 lignes ne gagne qu'environ 10 % de vitesse sur cette carte.
- Projection pour 2 000 épisodes, au rythme de la phase de production (lot de 8, cette carte, ce noyau) : 5,7 heures dans A, 5,6 dans B. Stockage : 11,2 Go avec la politique par défaut, 102,4 Go si tout était gardé par jeton (2 084 jetons par épisode en moyenne).
- Codage sur disque : `bfloat16-bits`, 2 octets par valeur (propriété de construction) ; fichiers par jeton de 52,6 et 55,8 Mo pour les épisodes 1 et 14 ; 0,5 Mo pour les autres.

### 7.5 Réglages relus et noyaux permis

- Réglages relus, identiques dans A et B : algorithmes déterministes ; précision des produits en simple précision « highest » (« ieee » côté CUDA) ; format TF32 coupé (produits et cuDNN) ; réductions en précision réduite coupées (bfloat16 et demi) ; cuDNN déterministe, banc d'essai coupé ; 1 fil ; espace de travail cuBLAS `:4096:8`.
- Noyaux permis, relus dans le contexte du noyau de chaque phase (logique, chemin, production) : seul « math » ; flash, mémoire efficace et cuDNN coupés ; réduction en demi-précision dans « math » coupée. Le débit et le repère tournent au même noyau (code).

### 7.6 Machine et versions

NVIDIA H200 NVL (capacité 9.0), 139,8 Gio ; pilote 580.159.03 ; CUDA 13.0 ; cuDNN 92400 ; torch 2.14.1+cu130 ; transformers 5.18.0 ; tokenizers 0.23.2 ; safetensors 0.8.0 ; huggingface_hub 1.33.0 ; numpy 2.4.6 ; Python 3.11.17. Mémoire vive effective 734,5 Go : c'est le plafond du groupe de contrôle ; la mémoire totale lue, 2 164 Go, est celle de l'hôte. Ce plafond dépasse les 258 Go de l'offre, comme dans la v2 (550,7 Go pour une offre de 189 Go) ; sans effet sur la lecture.

### 7.7 Durées et coût

- Tests sur l'instance : 84 secondes (fin à 11:40:25 UTC).
- Run A : 848 secondes (11:40:25 → 11:54:37) ; run B : 789 secondes (11:54:40 → 12:07:52). Limite interne : 9 000 secondes par run.
- Instance 54476244 : de 11:36:50 à 12:11:10, soit 0,572 heure ; à 4,669 USD de l'heure, environ 2,67 USD (registre des dépenses), plus le téléchargement et le stockage. Plafond cumulatif de T0.4 : 1,31 heure sur 6. Attendu par le préenregistrement : 0,6 à 1,2 heure, 3 à 6 USD.

## 8. Limites et ce qui reste hors de portée

1. **Écarts par jeton.** Les captures de génération et les activations de la logique, du chemin et du repère n'ont été écrites nulle part : seuls leurs profils et leurs empreintes sont dans les résumés. Je ne recalcule donc aucun écart par jeton. Je vérifie la cohérence interne des profils, leur cohérence avec les trajectoires, les bilans et les lectures, et un contrôle indépendant du 99e centile décalé par les comptes de positions au-dessus du seuil.
2. **Fichiers npz** (relecture, P8). Ils ne sont que sur le disque de l'instance arrêtée. Leurs empreintes sont consignées et peuvent être contrôlées s'ils sont récupérés. Leur destruction est irréversible.
3. **Fichiers du modèle.** Je ne les compare pas aux empreintes publiées (pas de réseau). Ils sont attestés par la garde de l'instance, et leur relevé est identique à ceux de la v1 et de la v2.
4. **Mécanisme du contexte exact de la production** (section 6.1). Non vérifiable sans la carte ; l'explication donnée est plausible, cohérente avec les données, non prouvée.
5. **Domaine de validité.** Celui que la validation observe (section 5.4), sur cette carte, ce pilote, ces bibliothèques et ce noyau. Hors de ce domaine, il faut revalider, ou au moins garder la garde d'équivalence en ligne sur un échantillon (préenregistrement, « Domaine de validité »). Le débit n'a pas été observé à des contextes de 2 048 jetons.
6. **Points laissés ouverts par le préenregistrement lui-même** (Transparence) : R-037 (R-5, R-6, R-7, R-1, Q-5), W-5, Y-3, Y-8. Je ne les rejuge pas ; le préenregistrement dit qu'ils ne changent pas la lecture d'un run.
7. **Biais commun possible.** Je tourne sur le même modèle que l'auteur et les contre-lecteurs : un biais commun reste possible.

## 9. Transparence

- **Qui je suis.** Contexte neuf. Je n'ai vu aucune des conversations qui ont produit le préenregistrement, le code, le lancement ou l'analyse.
- **Ce que j'ai lu.**
  - `CLAUDE.md` ; le préenregistrement v3 en entier ; la procédure v4 en entier.
  - Les deux manifestes et les deux résumés (tous les champs utilisés ci-dessus) ; `tests-instance.json` ; `environnement-python.json` ; la comparaison ; les 96 trajectoires, par mes scripts.
  - Les deux dossiers de traces, en entier.
  - Les registres : R-048 à R-051, la fin des dépenses et des arrêts, et les GO cités.
  - Pour le contexte seulement : le verdict de la v2 en entier, la proposition N-011 en entier.
  - Le code cité : `validation_reelle.py`, `episode.py`, `activations.py`, `modeles.py`, `politique.py`, `manifeste.py` et `scellement.py`, en entier ; `exiger_identite` de `sondes.py` (égalité exacte des tableaux, arrêt sinon) ; la séquence des runs A et B dans `scripts/validation_t04_instance.sh`.
- **Ce que je n'ai pas lu.** Les rapports de contre-lecture et leurs archives ; les brouillons ; les notes de mémoire (seulement empreintées) ; l'amorce (seulement empreintée) ; le brief au-delà de la porte G0, et le programme (seulement empreinté) ; `gardes.py`, le reste de `sondes.py`, `formats.py`, `stockage.py`, `prereg.py`.
- **Ce que j'ai lancé**, sur processeur seulement, depuis mon clone (`PYTHONPATH=src`, Python de `/home/user/controle-ia/.venv`) : les scripts 01 à 12 de `recalculs/` ; la suite de tests du clone, 206 réussis en 116 secondes (`06_tests_processeur_clone.sortie.txt`, contrôle de cohérence ; P0 se lit sur la sortie de l'instance).
- **Ce que je n'ai pas fait.** Aucune commande `vastai`, aucun accès réseau, aucune lecture de jeton, aucune dépense, aucune poussée.
- **Incident, corrigé.** Une redirection de shell, lancée avec un chemin relatif alors que le dossier courant était le dépôt de référence, y a créé un fichier vide non suivi, `03b_rejeu_entre_processus_chemins_normalises.py` (0 octet), vers 12:21 UTC. Je l'ai supprimé aussitôt, par son chemin exact. Aucun fichier suivi n'a été touché. À la fin, `git --no-optional-locks status` y est vide, et HEAD reste `678900c`.
- **Sur mes recalculs.**
  - La première sortie du script 03 marque un « ÉCHEC » : les chemins des fichiers npz contiennent l'identifiant du run. Le script 03b normalise ces chemins ; les deux sorties sont gardées.
  - Les commandes des recalculs 06 et 08, d'abord lancées en ligne, sont consignées dans des scripts ; 08, rejoué, rend la même sortie.
  - Le fichier d'empreintes `recalculs.sha256` a été refait une fois, après l'ajout du script 12, avant l'écriture de ce verdict et avant toute citation.
- Version finale : à la demande de la session de pilotage, le nom du modèle a été retiré de la section 8 (règle du dépôt) ; aucune autre modification.

Selon la table et R13, ce verdict est scellé, puis soumis à Lazar pour GO.
