# Rapport complémentaire du développeur du lanceur de P3-bis : fusion du code corrigé, bancs sans bouchon — v1

- **Auteur** : le développeur du lanceur (Claude Opus 5.5, `claude-opus-5-5`), même fil que le rapport v1
  (`rapport-developpeur-lanceur-p3bis-v1.md`, `748568cbd7a72a2fe02eb7cedeb9981f9f6fb76bff230f20526dbfefa8799e34`).
- **Consigne** : message de la mère reçu vers 06:52 UTC : fusionner `prep/p3bis-code-v2` (tête `5238b2b0`, commit du code
  proposé `02217f1c`, R-2085), retirer le bouchon d'`ouverture_p3bis_v2`, rejouer les cinq bancs et la répétition jouet
  contre le vrai code, vérifier les six points de dépendance, garder la liste ciblée v2 (531 essais), ne pas remplir les
  épingles. Compte rendu du développeur du code lu : `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v2.md`
  (`f6c93bc51111ed10b93602bb6d7a85bab8b855bc548564fe13957793c6b75e33`, vérifiée).
- **Heures** (`date -u`) : reprise à 06:53:33 UTC ; fusion à 06:54 ; bancs finaux de 07:05:36 à 07:09:14 ; répétition jouet
  de 07:05:18 à 07:14:51 (573 s) ; ce rapport ensuite.
- **Interdits tenus** : aucun fichier du code corrigé modifié (la fusion est sans conflit ; aucun chemin hors de
  `docs/procedures/P3-bis-temoin-positif-v1/` n'est changé par mes commits suivants) ; ni fetch ni push ; aucun `vastai`
  réel ; épingles `A_EPINGLER` non remplies ; garde des secrets à 0 avant chaque commit (y compris sur le diff de la
  fusion) ; aucun refus de classifieur pendant cette reprise. **Rappel du refus de la passe précédente** (rapporté tel
  quel) : l'effacement de mes dossiers temporaires du bloc-notes a été refusé par une vérification de sécurité ; je n'ai
  rien effacé depuis et mes scripts d'essai neufs n'effacent plus rien (dossiers listés plus bas, laissés à une personne).

## Verdict

Fusion faite (commit `d9501dfe`, sans conflit) ; bouchon retiré ; **379 cas de bancs, 0 non conforme**, joués contre le vrai
`ouverture_p3bis_v2.py`, la vraie `amorce_instance_p3bis_v2.sh`, le vrai `p3bis_instance_v2.sh`, la vraie liste v2 et la
vraie sortie de l'essai de fermeture v2 ; les lectures de P3 et complémentaire **réelles, en mode décisif** sous un texte
factice scellé (banc de la récupération et répétition jouet) ; répétition jouet conforme (21 étapes et vérifications ; la récupération de la fin normale joue les vraies lectures décisives et pousse un paquet de 16 783 360 octets). Six points de
dépendance vérifiés : **un seul écart**, corrigé de mon côté (ligne « motif du dépliage »).

## Commits (branche `prep/p3bis-lanceur-v1`, locaux, après `d7b1ca0f`)

| commit | jalon |
|---|---|
| `d9501dfe` | fusion de `prep/p3bis-code-v2` (tête `5238b2b0`) |
| `e45c2599` | 9 : récupération (ligne « motif du dépliage » admise) ; son banc contre le vrai module v2 et les vraies lectures décisives |
| `7c45b9b1` | 10 : bancs du lanceur, des contrôles et de la surveillance contre les vrais scripts v2 ; répétition jouet sans bouchon |
| (suivant) | 11 : journaux du développeur v2, ce rapport, scellés |

## Les six points de dépendance, contre le code réel

| # | dépendance (rapport v1) | constat sur le code corrigé | écart | correction (de mon côté seulement) | essai |
|---|---|---|---|---|---|
| 1 | sorties de `lectures-fermees --prereg --entropie` | `ouverture_p3bis_v2.lectures_fermees` (l. 610-653) : quatre lignes « code … : N » et « paquet des lectures : <sha256> » ; **en plus**, sur un refus du dépliage, une ligne « motif du dépliage : … » (CP-11 : elle ne porte que sur l'intégrité du second paquet) ; `--prereg` sans `--entropie` : `ARRÊT`, code 1 (la chaîne passe toujours les deux) ; paquet `diag/p3bis-ferme-<run>/paquet-ferme-v1.tar`, 16 783 360 octets, compagnon ; aucun reste en clair | **oui** : la récupération v1 aurait compté cette ligne « hors de la classe 1 » | `recuperation_p3bis_v1.sh` (brouillon 2, même nom) : motif `motif du dépliage : .*` admis parmi les lignes attendues, et affiché | banc de la récupération : R00 (sortie exacte, cinq lignes ; paquet relu par le banc : deux manifestes décisifs, issue « vu », ligne 4, durées écrites) ; R12 (second paquet altéré : la ligne du motif est admise et affichée, KO « lectures fermées ») ; R14 (lecture refusée par sa propre garde, configuration citée autre : KO, aucun commit) |
| 2 | constantes du script de l'instance | `p3bis_instance_v2.sh` l. 48 `DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"`, l. 53 `LISTE_TESTS="scripts/essais-cibles-p3bis-v2.txt"`, l. 54 `LISTE_SHA256="3ecf3cda…"` (= empreinte de la liste v2), l. 321 lanceur `run_v2` ; aucune commande `timeout` (seulement en commentaire) ; amorce v2 l. 42 `bash amorce-depot/scripts/p3bis_instance_v2.sh` ; empreintes `83820dfd…` et `b331e44f…`, égales au compte rendu du code | non | — (la constante `A` du lanceur et `AMORCE` des contrôles portaient déjà le nom v2) | banc des contrôles, bloc 8 et bloc 11 sur les vrais scripts : K00 conforme ; K22, K27, K28 |
| 3 | lignes du journal lues par la surveillance et le contrôle à cinq minutes | toutes écrites sous la forme attendue (fragments littéraux relevés dans le source) : `journal()` horodaté, « début : ETUDE=p3bis … », « préenregistrement lu : $ATTENDUS tests attendus ; … », « branche $BRANCHE poussée avant l'installation … », ligne de `nvidia-smi` (`memory.total`), « run : processus $PID_RUN lancé / fini, code $code », « … run complet », « SECOND PAQUET EN ÉCHEC (… », relais `PROGRES` au motif de P3 ; amorce : « AMORCE <date> : commit », « AMORCE : … », « AMORCE <date> : fin, code $code » | non | — | banc de la surveillance : seize cas X (fragments présents dans les vrais scripts) et un artefact (copie altérée vue) |
| 4 | code 5 | `sortir` (l. 206-208) et l. 246, 356 : `exit 5` dès que le second paquet a échoué, arrêt compris ; l'amorce rend ce code dans « AMORCE … fin, code 5 » | non | — | banc de la surveillance : X (fragment `exit 5`), M01 à M03 ; répétition, tentative 2 |
| 5 | chemins permis sur la branche de calcul | l'instance commite `runs/<run>` et `diag/<run>` (épisodes exclus de git), le second paquet, `traces/p3bis-<date>-XXXX/` (neuf fichiers et `empreintes.sha256`, l. 185-191) ; auteur « instance de calcul (P3-bis) » ; un run fabriqué par le code corrigé (`fabriquer_run`, même jeu de fichiers que le run de P3) passe le filtre `PERMIS` | non | — | banc de la récupération R00 ; répétition, tentative 1 |
| 6 | dernière ligne de l'essai de fermeture | sortie versée `essai-fermeture-p3bis-v2-sortie-v1.txt` (`06e84ff7…`) : dernière ligne « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME », aucune ligne commençant par « NON CONFORME » ; interface `essai_fermeture_p3bis_v2.py DOSSIER_NEUF SORTIE.txt` | non | — | banc des contrôles, bloc 6 sur la vraie sortie versée : K00, K14, K15 |

Autres points du compte rendu du code qui touchent la chaîne : **E-5** (amorce v2 créée) : déjà le nom de la chaîne ;
**E-6** (`fermer` seul garde `--entropie` facultative) : la chaîne n'appelle jamais `fermer` seul ; si la session refait
une mise en paquet à la main (liste d'arrêt : « la mise en paquet est refaite sur les mêmes fichiers »), elle passe
`--entropie` ; **E-4** et décision de la mère : liste v2 gardée (531 essais) ; les contrôles lisent N dans le texte et
exigent l'empreinte de la liste égale à `LISTE_SHA256` du script de l'instance : rien à changer.

## Bancs et répétition

| passage | heures (UTC, `date -u`) | durée | cas | non conformes | contre quoi | journal (`journaux-developpeur-v2/`) |
|---|---|---|---|---|---|---|
| module commun (pytest) | 07:05:36 – 07:05:43 | 7 s | 140 | 0 | inchangé | `banc-verifications-p3bis-v1-dev.log` |
| lanceur | 07:05:43 – 07:06:09 | 26 s | 56 | 0 | vraie amorce v2 versée, encodée, passée à la création | `banc-lanceur-p3bis-v1-dev.log` |
| surveillance et contrôle à cinq minutes | 07:06:09 – 07:06:23 | 14 s | 99 | 0 | + 17 cas X de concordance avec les vrais scripts v2 | `banc-surveillance-p3bis-v1-dev.log` |
| récupération et destruction | 07:06:23 – 07:07:34 | 71 s | 44 | 0 | vrai `ouverture_p3bis_v2`, vraies lectures décisives, run source décisif de `fabriquer_run` | `banc-recuperation-p3bis-v1-dev.log` |
| contrôles avant dépense | 07:07:34 – 07:09:14 | 100 s | 40 | 0 | vrais scripts de l'instance v2, vraie liste v2 (30 fichiers copiés), vraie sortie versée de l'essai v2 | `banc-controles-p3bis-v1-dev.log` |
| répétition jouet | 07:05:18 – 07:14:51 | 573 s (dont trois attentes de 181 s) | 21 étapes et vérifications | 0 | vrai module v2, vraie amorce v2, run source décisif, vraies lectures décisives | `repetition-jouet-p3bis-v1-dev.log` |

**Bouchons qui restent** (lignes changées comptées dans chaque journal) : faux outil de location ; contrôles avant dépense
dans les bancs du lanceur et la répétition ; dans le banc des contrôles, trois blocs : vrai tokeniseur (Hugging Face),
gardes du lanceur run_v2 (texte, configuration et données génériques réels exigés) et **la suite de la liste ciblée**
(531 essais, ≈ 20 minutes par passage : remplacée par « 531 passed », ou `FAUX_SUITE` ; la vraie liste a été jouée par le
développeur du code, 531 passés, et l'est par la répétition finale) ; l'essai de fermeture rejoué au commit S reste factice
dans ce banc (sept minutes par passage ; la sortie versée lue est la vraie ; joué en vrai par la répétition finale) ; le
script de l'instance n'est pas exécuté (la répétition simule l'instance par le faux outil ; ses lignes de journal sont
celles du vrai script, cas X) ; journaux de preuve factices à S dans le banc du lanceur et la répétition.

## Écarts, déclarés

1. **Ligne « motif du dépliage »** (point 1) : admise par la récupération, brouillon 2 ; à porter au texte avec l'écart 5 du
   compte rendu du code (« motif d'un refus du dépliage imprimé, classe 1 de fait »).
2. **Fichiers de la chaîne changés en place** (brouillon 2 dans leur en-tête : `recuperation_p3bis_v1.sh`,
   `repetition_jouet_p3bis_v1.sh`, `essais_lanceur_p3bis_v1.sh`, `essais_controles_p3bis_v1.sh`,
   `essais_surveillance_p3bis_v1.sh`, `essais_recuperation_p3bis_v1.sh`) : la table des noms communs fixe ces noms ; les
   versions du rapport v1 restent au commit `d7b1ca0f` avec leurs empreintes (rapport v1). Si la mère veut un nom neuf par
   version (R12), je propose `…_v2` pour ces six fichiers au candidat.
3. **Textes factices des bancs** : le banc de la récupération et la répétition citent maintenant le commit du code,
   l'empreinte canonique de la configuration du run et l'entropie de P3, avec les sections de R1 et R2 : forme exigée par
   les lectures décisives réelles.
4. **Nouveaux journaux sous un nom de dossier neuf** (`journaux-developpeur-v2/`) ; ceux de `journaux-developpeur-v1/`
   restent (versions du rapport v1). Les journaux canoniques restent à produire au candidat.

## Fichiers et empreintes (au commit de ce rapport)

| fichier (sous `docs/procedures/P3-bis-temoin-positif-v1/`) | changé depuis le rapport v1 | sha256 |
|---|---|---|
| `recuperation_p3bis_v1.sh` | oui (brouillon 2) | `5b957353dee9e8a3dfc010396e9a8ba83dc6674cbfc7b2282dba54582934dcbe` |
| `repetition_jouet_p3bis_v1.sh` | oui (brouillon 2) | `85096b6877e5560ee01e240aa9c0946010888aaefaf3cad0adc62ce720b792a7` |
| `essais_lanceur_p3bis_v1.sh` | oui (brouillon 2) | `5d14473df92df01f7a33eb2ca5d5e586b8833e1c3b9d2bb902454c17ce2f5545` |
| `essais_controles_p3bis_v1.sh` | oui (brouillon 2) | `f83e537c105015980bb48d04e82d604fa5e991920ea6417c7b4f6590ebc86799` |
| `essais_surveillance_p3bis_v1.sh` | oui (brouillon 2) | `ed6474302300e66ec90755542aee08e2f2addcf221325fed48cfb74be1083636` |
| `essais_recuperation_p3bis_v1.sh` | oui (brouillon 2) | `e95e8875500f9792aea197193ebf6429a1a8e053db9755531f0a3a54f05f316b` |
| `lancer_p3bis_v1.sh` | non | `0ca137b54b1de06fba5b34830ed6872d42b8776bdf8b136c755d246efbd8eec8` |
| `verifications_p3bis_v1.py` | non | `71153720bce0d2792747a4480c3ffb7da7c71c3389bf06b369cd062d5cef58fb` |
| `controles_avant_depense_p3bis_v1.sh` | non | `8571d2f33a075aaaef6da8780c77075947d7c66b9636774989eb5fccd392c601` |
| `surveiller_p3bis_v1.sh` | non | `dbaa6a62986f149741fce12e7165e0de6df5ca456e6d07badf78b91ddf2a122e` |
| `controle_cinq_minutes_p3bis_v1.sh` | non | `51411159616708fa45056cf95c536ab602496fe726706442ad1016a88a08153d` |
| `detruire_p3bis_v1.sh` | non | `d44c97ea480127088a5976d62db4fa18fd3ffd978c86fe16f2ea6c60d11fc4d0` |
| `sceller_p3bis_v1.sh` | non | `82ebd30e36e81a54e1449dc08609229a0b972bf2156b6a9ec9d1c6bf5f9f0cdf` |
| `repetition_finale_p3bis_v1.sh` | non | `354dc699ec34cfdae95a2296ede8476d5e2a0b890c878a37857888ab8f46f9dd` |
| `essais_verifications_p3bis_v1.py` | non | `8130b8231ee7cbd2ddc610d4cf2f7ffba5f04eb8b1919dc0b72f93ab6c17ffa5` |
| `journaux-developpeur-v2/banc-controles-p3bis-v1-dev.log` | neuf | `0bc6cfb4cc631e0cb57277c78900f15dfca18e849a5590e7cfb6df37d4eff842` |
| `journaux-developpeur-v2/banc-lanceur-p3bis-v1-dev.log` | neuf | `3b4e0e9cd28686b26a82b6220cdef4e68c6e8e3f4d1507fb130915c6778bb4ca` |
| `journaux-developpeur-v2/banc-recuperation-p3bis-v1-dev.log` | neuf | `dfb6c5cb464a2dcc98104570c216faa1d04342b02ffb99f8a9739b912aa07063` |
| `journaux-developpeur-v2/banc-surveillance-p3bis-v1-dev.log` | neuf | `2e059acf5692f60bf254222d402526bd5bffc58811de1b0177a4a310af01d88d` |
| `journaux-developpeur-v2/banc-verifications-p3bis-v1-dev.log` | neuf | `9307edad91b779fed7ef6d3ddde04f8291cbf93f9ace4de385ce55fa8b4516a0` |
| `journaux-developpeur-v2/repetition-jouet-p3bis-v1-dev.log` | neuf | `94334f7c3f59dc71429abd16fc23f215b234c0c692e0c426f87ffb71c54bf628` |

Chaque fichier a son compagnon `.sha256` (R6) ; ce rapport est scellé à part.

## Ce qui reste

1. Au candidat : épingles `A_EPINGLER`, journaux canoniques des bancs et des deux répétitions, répétition finale en mode
   décisif (elle jouera la vraie liste v2, le vrai essai de fermeture, le vrai tokeniseur et les gardes run_v2).
2. Contre-lecture R2 de la chaîne ; brouillon 10 (écarts du rapport v1 et l'écart 1 ci-dessus).
3. Dossiers temporaires laissés dans mon bloc-notes (refus de la passe précédente ; aucune tentative depuis), sous
   `/tmp/claude-0/-home-user-controle-ia-travail/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/` : `rep-jouet-2`,
   `journaux-finaux`, `b2-surveillance`, `b2-recuperation`, `b2-controles`, `b3-lanceur`, `pt-verif3`, `v2-recup-1`,
   `v2-ctl-1`, `v2-surveillance-1`, `v2-lanceur-1`, `v2-rep-jouet`, `journaux-finaux-v2`, `final2-lanceur`,
   `final2-surveillance`, `final2-recuperation`, `final2-controles`, `pt-final2` et leurs journaux : copies d'essai, sans
   secret, à effacer par une personne.
