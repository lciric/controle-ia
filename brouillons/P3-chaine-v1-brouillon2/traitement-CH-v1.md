# Traitement des constats de la contre-lecture de la chaîne de P3 — chaîne v1, brouillon 2

- Constats traités : `prereg/contre-lectures/P3-premier-test-v1-relecture-chaine-v1.md`
  (`57060da8f239f6c894978a187668f5f75d2b214cd25e9c7e3463b32dd7461db6`), CH-01 à CH-24, sur la chaîne brouillon 1
  (`brouillons/P3-chaine-v1-brouillon1/`, gardée telle quelle, R12).
- Chaîne traitée : `brouillons/P3-chaine-v1-brouillon2/`, treize scripts (les douze du brouillon 1, corrigés, et
  `controle_cinq_minutes_p3_v1.sh`, nouveau, CH-23). Les chemins de fichier sans dossier désignent ce dossier ; les numéros
  de ligne sont ceux du brouillon 2 à la date de ce fichier.
- Textes suivis : brouillon 4 du texte (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,
  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`), configuration candidat 3
  (`brouillons/P3-premier-test-config-v1-candidat3.json`, `702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde`,
  empreinte canonique `2f343a6f…`), consignes candidat 2 (`a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c`),
  décision R-202 (`registres/decisions.md`).
- Rédaction : sous-agent neuf, rédacteur de code (routine sur processeur). Ce fichier n'est pas une contre-lecture : la
  relecture courte du traitement reste à faire par un sous-agent neuf (R2).

## Constats

| constat | gravité | sort | où | comment | raison d'un sort autre que « corrigé » |
|---|---|---|---|---|---|
| CH-01 : le banc des contrôles ne peut pas finir conforme (A19 exige un seul KO) | bloquant | corrigé | `essais_controles_p3_v1.sh` l. 137-138 (compte exigé : `jouer()`, l. 93) | A19 exige deux KO : la pièce sans sceau et `verifier-arbre` (`docs/` est scellé). Banc rejoué (section « Épreuves ») : A19 conforme à deux KO. | — |
| CH-02 : le GO cité n'est pas lié au GO de la création | majeur | corrigé | `verifications_p3_v1.py` l. 39, 63-64 ; `lancer_p3_v1.sh` l. 128-135, 291, 302 ; `controles_avant_depense_p3_v1.sh` l. 142-147 ; bancs : `essais_lanceur_p3_v1.sh` l. 346 (G05), `essais_controles_p3_v1.sh` l. 124 (A06b), `essais_scellement_p3_v1.sh` l. 248 (S24b) | Une seule constante, `GO_CALCUL = "GO-2026-10-04-08"`, dans le module commun : tout autre GO cité est refusé. Le GO validé par le module est celui que portent la garde rejouée et la création (`GO_ID="$GOP3"`). Le cas « GO de calcul d'un autre périmètre (GO-2026-10-17-01) » est refusé aux trois bancs. | — |
| CH-03 : le scellement ne relit pas les preuves des essais | majeur | corrigé | `sceller_p3_v1.sh` l. 22-24, 32, 76-82, 133-145 ; `verifications_p3_v1.py` l. 25-31, 187-235 ; `repetition_finale_p3_v1.sh` l. 9-11, 28, 45-48, 52-56 ; bancs : `essais_scellement_p3_v1.sh` l. 43-59 (journaux fabriqués), l. 338-352 (S41 à S41d), `essais_lanceur_p3_v1.sh` l. 349-380 (P30a à P30j) | Avant le commit, le scellement exige les cinq journaux suivis à HEAD avec leur sceau exact, les relit par le module commun (verdict de la dernière ligne, aucune ligne d'échec, scripts éprouvés exacts, une seule empreinte par script), puis compare chaque script éprouvé à sa copie versée : le même texte que le lanceur. Variante écrite : la copie jouée par la répétition finale n'exige que trois journaux (bancs du lanceur, de la surveillance et des contrôles), et non quatre, car son propre journal n'existe pas encore et celui du banc du scellement éprouve la copie versée que la répétition remplace ; ses quatre lignes changées sont comptées. | — |
| CH-04 : le lanceur n'exige pas de cœurs | majeur | corrigé | `lancer_p3_v1.sh` l. 18-19, 44-45, 182-188 ; `controles_avant_depense_p3_v1.sh` l. 250-251, 255-256 ; brouillon 4 l. 288-296, 371 ; bancs : `essais_lanceur_p3_v1.sh` l. 208-209, 211, 213, 443-444 | Le filtre local exige `cpu_cores_effective` ≥ 16 et `cpu_ram` ≥ 128 000 Mo ; le bloc 9 relie ces deux constantes aux valeurs du texte. Offres moins chères à 15 cœurs, 15,9 cœurs, cœurs illisibles ou 127 999 Mo écartées au banc ; 16 cœurs acceptés. Seuil de 16 et non de 32 : borne du brouillon 4, où le run prend min(32, cœurs disponibles) fils (TC-12) et où la mesure à la taille réelle donne 823 s par couche à 4 fils, soit environ 2 470 s pour trois couches, sous le budget de 3 600 s (`docs/notes/P3-mesures-v2/chrono-reel-4fils-v1.txt`, `aa04961504f409579ddba6e56bab2a0d0c72597e3171352c663b70f71b1e4ca5`). | — |
| CH-05 : « sondes figées avant le premier épisode » n'est établi qu'« avant la fin du premier lot » | mineur | corrigé | `recuperation_p3_v1.sh` l. 23, 354-363 (contrôle 6e), 419-420 (libellé de 6d) ; `repetition_jouet_p3_v1.sh` l. 42-43, 303-305, 373 (artefact q-v1) ; `verifications_p3_v1.py` l. 133 | Preuve tirée des résultats scellés : `duree_s` des sondes figées ≤ `duree_s` des épisodes − `descriptifs.duree_s`, même origine, tolérance de 0,2 s. Le contrôle du journal (6d) dit « avant la fin du premier lot ». Artefact « durée des sondes figées après le début des épisodes » : KO 6e attendu. | — |
| CH-06 : données orphelines acceptées ; sceau des scores jamais confronté au fichier | mineur | corrigé | `recuperation_p3_v1.sh` l. 135-171 (2b), 214-228 (4c) ; `repetition_jouet_p3_v1.sh` l. 34-37, 343, 352 (artefacts o-v1 et i-v1) | (a) 4c exige aussi le sens inverse : toute donnée présente a son résultat et son sceau. (b) Chaque fichier de données présent est vérifié par son sceau compagnon (`verifier`), puis rattaché à l'empreinte écrite dans son résultat et dans le résumé. Artefacts « donnée orpheline » (KO 4c) et « sceau des scores faux » (KO 2b). | — |
| CH-07 : la répétition jouet laisse des gardes de la récupération sans épreuve | mineur | corrigé | `repetition_jouet_p3_v1.sh` l. 6-7, 29-45, 60, 132-136, 145, 165, 251-257, 311-314, 327-387 ; `recuperation_p3_v1.sh` l. 38-40 ; `verifications_p3_v1.py` l. 114-138 | (a) Cas sain g-v1 joué par la copie versée, gardes 0, 3f et 6b dans leur forme réelle (carte A100 SXM4 factice), puis artefacts KO 0, KO 3f et KO 6b. (b) Jetons factices de 15 caractères, les mêmes à l'instance jouet et à la récupération ; artefact « jeton dans une trace » (KO 7). (c) Artefact « résultat rattaché au manifeste d'un autre run » (KO 2b) rétabli. Artefacts ajoutés pour 4d (sondes permutées), 5 (sonde retirée) et 6f (lot manquant) : 4 sains et 17 artefacts, chacun à un seul KO. Restent sans artefact : 1a, 1b, 1d, 1e, 2a, 2c, 3a à 3e, 4a, 4b, les motifs du journal (6) et 6c. | — |
| CH-08 : garde des modules gelés d'étapes antérieures perdue | mineur | corrigé | `controles_avant_depense_p3_v1.sh` l. 10-11, 53, 103-120 ; brouillon 4 l. 19-23 ; banc : `essais_controles_p3_v1.sh` l. 225-226 (A55, A55b) | Garde rétablie : aucune différence entre S et le commit cité par le texte du pilote (`MODULES_LECTURE`, `pilote_a.py`, `harnais/`, `sondes/familles.py`), ni entre S et le commit cité par le texte des notations (`noter_pilote_a.py`, `lire_notations_pilote.py`). Vérifié au commit `8db38d0` : aucune différence aujourd'hui. | — |
| CH-09 : aucune révocation de la décision R-192 n'est lue | mineur | corrigé en partie | `verifications_p3_v1.py` l. 8-13, 42, 71-92 ; bancs : `essais_lanceur_p3_v1.sh` l. 287-296 (G06, G06b, G07, G07b), `essais_controles_p3_v1.sh` l. 126-127 (A08, A08b), l. 301-302 (G05, G06 du module), `essais_scellement_p3_v1.sh` l. 186 (S09d) | La chaîne refuse une ligne « révocation » du registre des GO qui nomme R-192 sans nommer d'autre GO, et toute ligne R-… du registre des décisions qui révoque, retire ou annule R-192. Une mention de R-192 sans révocation, ou la révocation d'un autre GO sous R-192, passe (cas sains). | La partie « écrire au texte la forme d'une révocation » change le texte : à décider (question 1). |
| CH-10 : borne de l'étape non établie (téléchargement non borné, disque de l'instance gardée sans borne) | mineur | corrigé en partie | `lancer_p3_v1.sh` l. 13-15, 46, 59, 182-188, 299 ; `controles_avant_depense_p3_v1.sh` l. 252-259 ; brouillon 4 l. 288-291, 301-303, 419 (TC-19) ; bancs : `essais_lanceur_p3_v1.sh` l. 210, 212, 237-240, 445-446, `essais_controles_p3_v1.sh` l. 242-243 | `inet_down_cost` relu et borné par le filtre local (`TELECHARGEMENT_MAX`) ; le lanceur refuse de tourner tant que la borne vaut « A_FIXER » ; le bloc 9 exige la borne fixée et citée au texte sous la forme « téléchargement au plus <valeur> USD par Go ». « Inatteignable » n'est plus écrit. Le sort du fichier complet est écrit au brouillon 4 (instance arrêtée, gardée 72 heures au plus) et dans `lancement.txt` (puis détruite par son identifiant). | La valeur de la borne et les montants de l'étape pour le téléchargement et le disque sont des valeurs du texte et une dépense : à décider (question 2). |
| CH-11 : l'accord de Lazar dans la session n'est pas relu | mineur | corrigé | `verifications_p3_v1.py` l. 14-17, 96-111 ; `lancer_p3_v1.sh` l. 30-32, 35-36, 40, 100-110, 136 ; brouillon 4 l. 38-42 ; banc : `essais_lanceur_p3_v1.sh` l. 221-225, 307-319 | Troisième argument ACCORD : la ligne R-… du jour qui contient « accord de Lazar », « P3 » et « lancement », relue par le module commun avant les contrôles et de nouveau juste avant la création. Cas : accord absent, d'un autre jour, sans « lancement », en double, argument mal formé ou absent. | — |
| CH-12 : tolérances de 3 et 2 jetons non préenregistrées | mineur | corrigé | `controles_avant_depense_p3_v1.sh` l. 255-258 (bloc 9), 281-330 (bloc 10) ; bancs : `essais_controles_p3_v1.sh` l. 274-283 (B01, B01b, B01c, B04, B05) | Tolérances retirées : longueurs égales tâche par tâche entre les trois conditions instruites, et égales aux valeurs citées (51 et 10 jetons à l'encodage seul ; dans le gabarit, 52 sur 56 tâches et 51 sur 4 pour les consignes, 10 sur 60 pour les indications : `docs/notes/P3-mesures-v2/longueurs-gabarit-consignes-candidat2-v1.txt`, `28b87c71971cb6ba027d7ea97a28c5330fec1e9257bb1fbef8363bedc4b90e73`). Le bloc 9 exige ces valeurs au texte. | — |
| CH-13 : une instance du programme peut passer pour celle d'un autre projet | mineur | corrigé | `lancer_p3_v1.sh` l. 21-22, 47, 222-267 ; banc : `essais_lanceur_p3_v1.sh` l. 381-401 (V01 à V08) | Liste positive : une instance nommée en argument n'est tolérée que si son étiquette commence par « rr- ». Étiquettes « t05- », « p3- », « t09- » ou sans préfixe refusées (V04 à V04d). | — |
| CH-14 : gardes sans artefact ; gardes redondantes | mineur | corrigé | Module : `essais_controles_p3_v1.sh` l. 297-300 (G01 à G04), 321 (M03b), 338 (M17), 340 (M18). Contrôles : `essais_controles_p3_v1.sh` l. 133 (A13b), 150 (A26b), 173-174 (Z1c4), 187-190 (Z1h, Z1i), 212 (Z2g), 223 (A54), 275 (B01b). Lanceur : `essais_lanceur_p3_v1.sh` l. 201 (P05b), 217-218 (P08c, P08d), 259 (N09), 265-267 (N04b), 305 (G08), 450-453 (A03), 455 (réponses masquées relues). Scellement : `essais_scellement_p3_v1.sh` l. 164 (S07c), 242 (S23b), 272 (S27d), 275 (S27e). Surveillance : `essais_surveillance_p3_v1.sh` l. 117-123 (M10). Gardes redondantes : `verifications_p3_v1.py` l. 40 ; `lancer_p3_v1.sh` l. 111-113, 134, 138, 219 ; `controles_avant_depense_p3_v1.sh` l. 102, 168, 202, 283-284 ; `sceller_p3_v1.sh` l. 120, 172, 188-189 | Un artefact pour chaque garde relevée quand il ne coûte qu'une ligne de banc. Gardes redondantes retirées (sous-condition « P3 » du module, second contrôle des jetons du lanceur) ou commentées « garde redondante, sans artefact possible » (sortie du module, encodage de l'amorce, prix après le choix, deux scripts répétés, `CHEMINS_GELES`, dernière ligne de `verifier-arbre`, contenu de S et origin/main après la poussée, texte privé absent du gabarit). | — |
| CH-15 : les consignes jouées par la répétition ne sont pas consignées | mineur | corrigé | `repetition_jouet_p3_v1.sh` l. 46-47, 69, 71 ; `verifications_p3_v1.py` l. 18-24, 150-159 ; `controles_avant_depense_p3_v1.sh` l. 158-162 ; `sceller_p3_v1.sh` l. 43, 125-129 ; bancs : `essais_controles_p3_v1.sh` l. 164-165 (A30d), 336-337 (M15, M16), `essais_scellement_p3_v1.sh` l. 214 (S18b) | Ligne « consignes répétées : <nom> <sha256> » écrite par la répétition et exigée par le module commun, contre l'épingle CONSIGNES_RELUES, aux contrôles et au scellement. | — |
| CH-16 : la surveillance écrit sans masque si les jetons manquent | mineur | corrigé | `surveiller_p3_v1.sh` l. 8-9, 32-35 ; `controle_cinq_minutes_p3_v1.sh` l. 32-35 ; banc : `essais_surveillance_p3_v1.sh` l. 124-131 (M11, M11b), 185 (C14) | Les deux jetons passés à l'instance (8 caractères au moins) sont exigés au départ ; sinon code 2, rien n'est écrit. | — |
| CH-17 : liste des instances arrêtées tolérées écrite en dur, sans l'instance des notations | mineur | corrigé en partie | `lancer_p3_v1.sh` l. 20-21, 56 ; banc : `essais_lanceur_p3_v1.sh` l. 174-192 (P00 : 56438435 arrêtée, tolérée), 230 (P11e : en marche, refusée) | L'instance des notations refaites (56438435, arrêtée par son identifiant le 2026-10-18, `registres/arrets.md` l. 22) est ajoutée à la liste ; elle n'est tolérée que relue arrêtée. Faits postérieurs : 56438435 et 55538944 ont été détruites le 2026-10-19 à 09:41 UTC (R-212), et la destruction de 55292763 et 55458787 est rendue à Lazar (R-213) ; les garder dans la liste est sans effet sur la sûreté (une instance détruite ne revient pas sur le compte), mais la liste n'est plus exacte. | La règle à consigner au texte ou au plan, et la liste exacte à verser (sans les deux instances détruites), relèvent du texte et de la session : à décider (question 3). |
| CH-18 : « aucun texte d'action poussé » contrôlé sur deux fichiers seulement | mineur | corrigé en partie | `recuperation_p3_v1.sh` l. 7-8, 17-21, 42, 210, 229, 236-258, 299-335 ; `repetition_jouet_p3_v1.sh` l. 39-40, 273-283, 364 (artefact n-v1) | Chaînes bornées dans tous les résultats, le manifeste et `run.json` (200 caractères ; 1 000 pour le motif d'un arrêt) ; textes des actions de 64 caractères ou plus cherchés (48 caractères de leur milieu) dans tous les autres fichiers ajoutés ; chaque ligne des scores à sa place du plan (épisode, condition, tâche, pas) ; comptes par condition égaux et de somme n ; motif d'un arrêt affiché borné à 200 caractères. Artefact « texte recopié dans le journal » : KO 4f. | « Écrire au texte ce qui est contrôlé » change le texte : à décider (question 4). |
| CH-19 : faits exclus comptés sans `n_faits_max` | pour information | corrigé | `controles_avant_depense_p3_v1.sh` l. 225, 331-333 ; banc : `essais_controles_p3_v1.sh` l. 250 (A49b) | Le bloc 9 exige `n_faits_max` nul ; le bloc 10 applique `n_faits_max` comme le run. | — |
| CH-20 : deux commentaires inexacts | pour information | corrigé | `controles_avant_depense_p3_v1.sh` l. 25-26, 121-122, 345-370 | Libellés corrigés : le run de P3 n'a pas de garde des versions (comparaison au pilote à la récupération, 3f) ; l'environnement des contrôles est déjà installé. Ses versions sont comparées aux dépendances épinglées de S avant la suite complète (10 dépendances, aucun écart aujourd'hui). | — |
| CH-21 : marge entre la surveillance et le KILL de l'amorce non déclarée | pour information | corrigé | brouillon 4 l. 297-300 ; `surveiller_p3_v1.sh` l. 6-7 | La marge est écrite au brouillon 4 (5 minutes moins le démarrage du conteneur et le clonage, 42 s au pilote), avec les bornes de 360 minutes (amorce) et de 22 200 s (surveillance) ; la surveillance la rappelle en commentaire. | — |
| CH-22 : crédit inséré tel quel dans du code | pour information | corrigé | `lancer_p3_v1.sh` l. 23-24, 268-288 ; banc : `essais_lanceur_p3_v1.sh` l. 217-218 (P08c, P08d) | Le crédit est lu et vérifié (nombre fini, non booléen) dans le programme qui calcule le minimum ; aucune valeur relue n'entre dans du code ; une réponse non numérique (avec apostrophe) est refusée en code 2. | — |
| CH-23 : contrôle à cinq minutes prévu, jamais écrit | pour information | corrigé | `controle_cinq_minutes_p3_v1.sh` (nouveau) ; `lancer_p3_v1.sh` l. 73-78, 299-301 ; `sceller_p3_v1.sh` l. 70-72 ; `verifications_p3_v1.py` l. 191-192 ; `controles_avant_depense_p3_v1.sh` l. 242, 247 ; banc : `essais_surveillance_p3_v1.sh` l. 137-201 (C00 à C19) | Treizième script : état relu sous forme filtrée (en marche ; prix au plus 1,30 USD de l'heure et au plus celui de l'offre choisie ; machine et hôte ; carte ; étiquette) et journal masqué (une seule ligne « AMORCE … commit S », aucun échec d'amorce, ligne de début, tests attendus, carte, branche poussée). Le lanceur écrit la fenêtre (création + 180 à 300 s) et la commande ; le banc de la surveillance l'éprouve. Le nom du script reste à reporter au champ « [au candidat] » du brouillon 4 (l. 381). | — |
| CH-24 : vérifié sans constat | pour information | sans objet | — | Rien à corriger. Ses constantes « 270 et 330 minutes » sont devenues 300 et 360 minutes au brouillon 4 : la chaîne les relie (bloc 9), mais les scripts de l'instance ne sont pas encore alignés (défaut hors de la chaîne, ci-dessous). | — |

## Décompte

- 23 constats CH-01 à CH-23 : **19 corrigés** (CH-01 à CH-08, CH-11 à CH-16, CH-19 à CH-23), **4 corrigés en partie**
  (CH-09, CH-10, CH-17, CH-18 : la partie restante change le texte ou demande une décision de Lazar), **0 non corrigé**.
  CH-24 : sans objet.

## Questions à décider

1. CH-09 : le texte écrit-il la forme que prendrait une révocation de la décision R-192 pour P3 ? Si oui, laquelle :
   (a) une ligne de type « révocation » au registre des GO qui nomme R-192 sans nommer d'autre GO ; (b) une ligne R-… du
   registre des décisions qui « révoque », « retire » ou « annule » R-192 ; (c) l'une ou l'autre, ce que la chaîne lit
   aujourd'hui ?
2. CH-10 : quelle borne de téléchargement (`inet_down_cost`, USD par Go) le texte fixe-t-il pour l'offre, et quels montants
   écrit-il pour le téléchargement et pour le disque de l'instance arrêtée (72 heures au plus) dans la borne de dépense de
   l'étape ? Données relevées : 0,026 USD par Go et 0,022 USD de l'heure de stockage à l'offre du pilote
   (`traces/t05-pilote-v1-20261012-1035/offre.json`, `4f1eee6457818f4a5019aba35a9b3eb10f42e9d9173cc629623ee4b84083acc0`) ;
   0,039 USD par Go, environ 20 Go (environ 0,8 USD) et 0,027 USD de l'heure de stockage à l'offre 29019328
   (`registres/depenses.md` l. 26, `c603a97492517ff6edf977f542dffb4992378fb149fe02c2e58ff4b3b124085d`) ; environ 0,6 USD de
   téléchargement constatés (même registre, l. 38). Calcul : 72 heures de disque à 0,022 ou 0,027 USD de l'heure font 1,60
   ou 1,94 USD. Le lanceur porte « A_FIXER » et refuse de tourner tant que la valeur n'est pas reportée.
3. CH-17 : la règle des instances arrêtées tolérées au lancement (liste fermée dans le lanceur, chacune relue arrêtée)
   s'écrit-elle au texte ou au plan ? Et quelle liste verser : « 55292763 55458787 », puisque 56438435 et 55538944 ont
   été détruites le 2026-10-19 (R-212), ou une liste vide si Lazar détruit aussi 55292763 et 55458787 (R-213) ? Le
   brouillon 2 porte encore les quatre identifiants : changeraient une ligne du lanceur (l. 56) et, au banc du lanceur, la
   liste factice par défaut (l. 48) et les cas P00, P11b et P11e (l. 189, 227, 230) ; une liste vide demanderait aussi
   de changer le contrôle de forme du lanceur (l. 58), qui exige au moins un identifiant.
4. CH-18 : le texte écrit-il ce que la récupération contrôle pour « aucun texte d'action hors du fichier des textes »
   (chaînes de 200 caractères au plus dans les résultats, le manifeste et `run.json`, 1 000 pour le motif d'un arrêt ;
   textes de 64 caractères ou plus cherchés dans les autres fichiers ajoutés ; motif affiché borné à 200 caractères), ou
   garde-t-il sa seule phrase actuelle (brouillon 4 l. 149 : « Aucun autre fichier poussé ne porte de texte d'action ») ?

## Ce que le brouillon 4, la configuration candidat 3 et R-202 changent pour la chaîne

- Quatrième condition « mention sans usage » (R-202 (2)) : 4 conditions × 60 tâches = 240 épisodes, 30 lots de 8. Bloc 9 :
  plan de 240 épisodes et « = 240 épisodes » au texte (`controles_avant_depense_p3_v1.sh` l. 256, 271) ; bloc 10 :
  longueurs égales entre les trois conditions instruites (saboteur, témoin, mention ; l. 296, 311-330) ; récupération :
  comptes par condition égaux et de somme n, lots comptés sur le plan (`recuperation_p3_v1.sh` l. 246-252, 411-413) ;
  répétition jouet à quatre conditions (`repetition_jouet_p3_v1.sh` l. 113).
- Données brutes gardées (R-202 (1)) : scores par jeton des sondes principales (`jetons-principales-p3.npz`) et textes des
  actions (`textes-actions-p3.jsonl`), scellés. Récupération : chemins permis (1c), sceaux et rattachements (2b,
  l. 119-120, 144-156), pièces dans les deux sens (4c, l. 219-225), scores par jeton (4d), textes des actions (4e), textes
  hors du fichier des textes (4f).
- Bornes du brouillon 4 (Plan d'analyse, point 4, l. 288-306) reliées aux constantes par le bloc 9 et citées au texte :
  durée du run 16 200 s et budget d'entraînement 3 600 s (configuration candidat 3 ; `controles_avant_depense_p3_v1.sh`
  l. 224) ; délai externe du run 300 minutes et plafond de l'amorce 360 minutes (l. 238-239 : scripts de l'instance) ;
  surveillance à la création + 22 200 s (`lancer_p3_v1.sh` l. 43, `surveiller_p3_v1.sh` l. 28) ; crédit sur 6,5 heures
  (`lancer_p3_v1.sh` l. 42) ; dépense de l'étape 22 200 s × 1,30 USD = 8,02 USD + arrêt 0,22 USD + téléchargement + disque
  72 heures (`lancer_p3_v1.sh` l. 13-15) ; offre à 16 cœurs effectifs et 128 000 Mo (l. 44-45) ; téléchargement borné
  (l. 46, valeur à fixer : question 2). Mesures citées par le brouillon 4 : `docs/notes/P3-mesures-v2/chrono-reel-4fils-v1.txt`
  (823 s par couche à 4 fils), `docs/notes/P3-mesures-v2/longueurs-gabarit-consignes-candidat2-v1.txt` (longueurs, 7 faits
  exclus), `docs/notes/P3-mesures-calcul-v1/LISEZMOI.md` (`76c245fe…` : ordres de grandeur, budget fixé par une garde de
  durée). Aucun chiffre nouveau n'est introduit par la chaîne.
- Pièces relues épinglées par les contrôles (`controles_avant_depense_p3_v1.sh` l. 35-44) : candidat
  `brouillons/P3-premier-test-i-a-v1-candidat1.md` (à créer), configuration candidat 3, consignes candidat 2 ; épingles
  laissées à « A_EPINGLER » dans ce brouillon (elles se fixent au candidat relu).
- Ce que le candidat doit porter pour que la chaîne passe (éprouvé sur un candidat d'essai, ci-dessous) : les champs
  « [au candidat] » du commit du code (une fois), des empreintes des deux scripts de l'instance (forme
  « (`<sha256>`, sha256) »), du nombre de tests attendus (une fois), de la borne de téléchargement sous la forme exacte
  « téléchargement au plus <valeur> USD par Go » (virgule décimale) ; les valeurs citées que relit le bloc 9
  (`controles_avant_depense_p3_v1.sh` l. 255-259) ; les rapports épinglés cités par « `chemin` (`empreinte`) » ; le nom
  du contrôle à cinq minutes (l. 381 du brouillon 4) ; TC-11 : `tests/test_premier_test_ia_gardes_v1.py`, 20 tests.

## Défauts hors de la chaîne (non corrigés ici : arbre gelé, hors de ma tâche)

- `scripts/p3_instance.sh` l. 247 porte encore `270m` et `scripts/amorce_instance_p3.sh` l. 38 `330m`, quand le brouillon 4
  écrit 300 et 360 minutes : les contrôles avant dépense refuseront S tant qu'ils diffèrent (bloc 9, l. 238-239).
- `scripts/p3_instance.sh` l. 150-157 (`ajouter_donnees`) et `scripts/amorce_instance_p3.sh` l. 47-48 (chemin du plafond)
  n'ajoutent ni `jetons-principales-p3.npz`, ni `textes-actions-p3.jsonl`, ni leurs sceaux, que `run.py` écrit (l. 423-435)
  et que R-202 (1) veut gardés : sur un vrai run, ces données resteraient sur l'instance et la récupération rendrait un KO 4c.
- Les deux demandent un nouveau commit du code (chemins gelés), donc un nouveau « code relu ». Le code d'essai K des bancs
  les corrige pour l'essai seulement (déclaré ci-dessous).
- Pour information : le message de commit du scellement porte une ligne « Claude-Session » écrite en dur, héritée du
  brouillon 1 (`sceller_p3_v1.sh` l. 184) ; à mettre à la session qui scellera, avant le versement.

## Épreuves (bancs rejoués, journaux non officiels)

Rejoués le 2026-10-19 depuis une copie du brouillon 2, dans
`/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/p3-v1-brouillon2/`, journaux gardés dans ce
dossier ; rien n'est écrit dans le dépôt de travail (clones jetables, dépôts nus locaux, faux outil de location).

- Code d'essai K (`d1b6837f7707f2c05a5e5f927153db8473e8a808`, dépôt jetable) : HEAD du dépôt de travail (`8db38d0`), plus
  `tests/test_premier_test_ia_gardes_v1.py`, plus les deux scripts de l'instance alignés pour l'essai seulement (300 et 360
  minutes, données nouvelles poussées) ; 892 tests collectés.
- Commit d'essai C2 (`4380f30e00ef5dfbcfa7482adaa8332845dd63b0`, sur K, dépôt jetable sans adresse distante) : un candidat
  d'essai (le brouillon 4 dont les champs nécessaires aux gardes portent des valeurs d'essai, dont une borne de
  téléchargement de 0,05 USD par Go ; `38e542058ec92f57aee3c02bdd37287412f8b921df8df24164b1be7dd7defb56`), les treize
  copies versées du brouillon 2 (épingles d'essai et ligne H des contrôles : 7 lignes changées ; borne d'essai du lanceur :
  1 ligne) et un journal synthétique de la répétition jouet, déclaré comme tel dans le journal. Un premier commit d'essai C
  (`0bc755fe401d01c8ebf8dd629312bd8f8e341569`) a porté les passages d'avant les corrections ci-dessous.
- Dernières lignes : surveillance (36 cas) « FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : 0 » ; lanceur
  (113 cas) « FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : 0 » ; scellement sur C2 (63 cas, passage 4) « FIN DU BANC
  DU SCELLEMENT DE P3 ; cas non conformes : 0 » ; contrôles sur C2 (135 cas, vrai tokeniseur compris, passage 2) « FIN DU
  BANC DES CONTRÔLES DE P3 ; cas non conformes : 0 ». Passages antérieurs, sur C : scellement, arrêt « S22 : montage
  impossible », puis 2 cas non conformes, puis 0 ; contrôles, 2 cas non conformes. Chaque script éprouvé par ces journaux
  est égal à sa copie du brouillon 2, sauf la copie versée des contrôles (épingles d'essai, par construction).
- Répétition jouet (en plus des quatre bancs ; copie jouée dont seules les lignes H et D changent, code d'essai K) :
  « FIN DE LA RÉPÉTITION » (passage 4, 2 914 s : suite de 892 tests dans l'instance jouet, 1 676 s ; run jouet de 240
  épisodes et 480 actions, environ 6,5 minutes, mémoire résidente maximale relevée 2 483 Mo). Journal conforme au module
  commun (`verifications_p3_v1.py repetition`, code 0) : trois passages à leur code (0, 2, 1), trois récupérations
  conformes et une des traces seules (code 4), dix-sept artefacts refusés chacun par un seul KO au préfixe attendu, gardes
  0, 3f et 6b jouées dans leur forme réelle. Passages antérieurs : 1, arrêté par le rédacteur (run trop lent à un fil) ;
  2, run jouet tué (code 137) au lot 46 sous le noyau « math », puis arrêt « artefact e : préparation impossible » ; 3,
  arrêté par le rédacteur pour passer au noyau « defaut ». Limite : au cas sain, la recherche des textes d'action hors du
  fichier des textes (4f, b) n'a cherché aucun texte, les actions jouet ayant moins de 64 caractères ; seul l'artefact
  n-v1 l'éprouve. La copie de la répétition versée à C2 est antérieure au passage au noyau « defaut » : aucun des bancs
  des contrôles et du scellement ne l'exécute (le journal de la répétition y est synthétique).
- Défauts des bancs relevés au rejeu et corrigés dans ce brouillon : (1) S22 cherchait la citation d'un rapport sur une
  seule ligne, alors qu'elle passe à la ligne dans le brouillon 4 (`essais_scellement_p3_v1.sh` l. 230-235) ; (2) une
  épingle changée au banc rendait caducs les journaux de preuve fabriqués, et la garde des preuves arrêtait avant les gardes
  visées par S24b et S25 (`epingle_versee()`, l. 95-103) ; (3) le motif attendu d'un KO était lu comme une expression
  rationnelle (« ['temperature'] », A45 refusé à tort ; `essais_controles_p3_v1.sh` l. 89-92) ; (4) M11 n'altérait pas les
  noms de P3, qui portent un chiffre (l. 330-332) ; (5) configuration du run jouet de la répétition : à un fil, un lot de 8
  actions prenait environ 100 s, soit environ 6 000 s pour 60 lots, au-delà des 3 000 s de la configuration jouet ; sous
  le noyau d'attention « math », la mémoire d'une passe unique croît comme le carré du nombre de jetons (1,4 Go de plus
  pour 5 950 jetons ; 25 Mo sous « defaut »), et un passage a été tué sans trace (code 137) au lot 46, celui de la tâche
  la plus longue (2509.24912v2) : 4 fils, 9 000 s et noyau « defaut », celui de la configuration réelle
  (`repetition_jouet_p3_v1.sh` l. 9-15, 112-113).
