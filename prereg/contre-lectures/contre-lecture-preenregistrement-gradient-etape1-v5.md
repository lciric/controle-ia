# Contre-lecture n° 5 (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v5 « économe »

- **Relecteur neuf** : sous-agent de contre-lecture R2 n° 5. Il n'a écrit ni le préenregistrement (v1 à v5), ni le code,
  ni les lanceurs, ni aucune contre-lecture ou revérification précédente. Contre-lecture **limitée** aux corrections
  annoncées pour CE4-01 à CE4-13 et RV-01 à RV-16, et à ce qu'elles touchent.
- **Heure** (UTC, `date -u`) : début 01:27 ; le conteneur a redémarré vers 01:29 (message du coordinateur : processus
  disparus, dossier de travail vide) ; reprise à 01:30, tout refait depuis le début ; fin 02:14.
- **Texte relu : `gradient-etape1-sondes-v5.md`, SHA-256 `d7cf7746bd85c5eb63f13495116ccb2b069363a7a8b3bc304a1e10613c57839d`**
  (compagnon : OK ; marqueurs de scellement non remplis).
- **Pièces** : `EMPREINTES-pieces.txt` vérifié deux fois (avant et après le redémarrage) : **172 sur 172 OK** ; les 63
  fichiers non listés sont tous des compagnons `.sha256`. Relues : la v5, la v4 (`54b70722…`), le rapport n° 4
  (`ab77c09b…`), la revérification du code (`79bc4d13…`), le diff `ed3ce0e..44cd936`, l'arbre du code, le collisionneur,
  le lanceur v3, ses essais et leurs trois sorties, le lanceur v2, le banc de mutations et ses deux sorties, les pièces des
  pannes et de la puissance, le validateur, le gabarit, `CLAUDE.md`, le message n° 30 de « conv-audit », le script de
  scellement.
- **Code des pièces = commit cité.** Clone partagé du dépôt dans mon dossier de travail, arbre détaché à
  `44cd936fb8e1512bfedaab0924ca182a87a3f3be` (sur `origin/outils/essaim-m3-gradient-v2-travail`) : identique aux pièces,
  hors fichiers de données retirés ; diff `ed3ce0e..44cd936` recalculé = pièce (lignes `index` mises à part). Les 28
  empreintes citées par la v5 que j'ai pu recalculer concordent (`sortie-empreintes-citees-v5.txt`), et aussi l'arbre du
  noyau `888fd6d6…`.

## VERDICT : **non scellable** — 1 bloquante, 2 majeures, 7 mineures, 2 de forme

Les corrections sont réelles pour l'essentiel : 12 remarques sur 13 de la contre-lecture n° 4 et 11 sur 16 de la
revérification sont traitées (tableau plus bas). Les 126 essais passent (rejoué), les 53 essais du lanceur v3 aussi, la
puissance et les taux de coupure se refont octet pour octet, le test de Fisher est exact, l'environnement du noyau ne met
aucune clé dans une ligne de commande, le validateur ne relève que les marqueurs et l'entrée 5.

Mais trois défauts empêchent le scellement en l'état :

1. **CL5-01 (bloquante)** — Sur l'hôte recommandé, un organisme isolé lit la banque scellée, **vérités du test final
   comprises** : le dépôt git est lisible par tous, et l'arbre du code au commit cité contient la banque. Démontré depuis
   le bac à sable (taille de l'objet seulement, contenu non lu). Le texte et le contrat disent le contraire.
2. **CL5-02 (majeure)** — Les dossiers en mémoire privés (RV-04) ne couvrent que quatre dossiers ; l'hôte en a un
   cinquième inscriptible par tous (`/var/lib/php/sessions`, 1733) : une exécution de A_1 y écrit, une exécution de B_1 le
   relit. Démontré. « Aucune voie commune hors des vues » est faux.
3. **CL5-03 (majeure)** — Régression de CE4-04 (3) : à la répétition, l'amorçage de Fable est refusé par le plafond d'une
   génération (3 USD) car son pire cas est de 3,26 à 3,4 USD. La porte de la répétition ne peut donc jamais passer, et
   aucune course décisive ne partira. Démontré en simulation avec les options exactes du lanceur.

**Condition du scellement.** CL5-01, CL5-02 et CL5-03 changent le lanceur ou le code (et le texte) : nouveau commit et
nouvelle empreinte du lanceur cités, puis une revérification limitée à ces points par un sous-agent neuf. Les mineures et
la forme peuvent être corrigées dans le même passage.

---

## Tableau de suivi

### Contre-lecture n° 4

| remarque | état | preuve |
|---|---|---|
| CE4-01 pannes : bruit des petits comptes | **traitée** | `regle_pannes` : effectif ≥ 10, écart > 10 points, ≥ 3 échecs d'écart, Fisher bilatéral p < 0,01, échecs extérieurs seuls, cumulés sur les générations communes. Fisher du code = calcul exact indépendant (écart ≤ 4·10⁻¹³ sur 3 000 tableaux) ; `coupure_sous_taux_identiques` = simulation de la règle (200 000 tirages par cas) ; JSON des coupures rejoué identique (`7028c3f4…`) ; exemples du texte justes (8/10 et 10/30 coupés, p = 0,0007 et 0,0008 ; 5/10 non, p = 0,033). Mutations m7, c07, c08 : l'essai échoue. Réserves CL5-07, CL5-11. |
| CE4-02 bras B sans réponse ; contrat | **traitée** | Texte (7), (8), (9) ; rapport descriptif gelé (couverture, causes, Δ secondaire, deux familles) ; demandes `INDISPONIBLE` comptées par le serveur. Rejoué (S2) : B sans aucune réponse → six paires coupées « couverture », lecture « non concluant », sans erreur. Le comptage `INDISPONIBLE` n'a pas d'essai (c11, CL5-05). Le « dire au contrat » est consigné comme décision de Lazar. |
| CE4-03 garde du vivier | **traitée** | Deux sens (m8), écritures non latines (m10), clé de doublon complète, identifiants tirés (c13 : l'essai échoue si on garde l'ordre du fichier). Texte, points 10 et 11. Comptes du vrai fichier : promis avec `<<VIVIER_MESSAGE>>`, non vérifiables (fichier absent ; voir CL5-12). |
| CE4-04 répétition aveugle ; Fable et B | **en partie** | Extrait v2 (essai, m12) ; porte calculée par le lanceur : juste sur simulations (sain, B, cinq artefacts : `sortie-cl5-porte.txt`) mais sans essai (CL5-06) ; Fable ajoutée, mais **son amorçage ne peut pas passer le plafond** (CL5-03) ; répétition B : options justes (essai `sain-repetition-B`). |
| CE4-05 « identiques » ; autres différences | **traitée** | Historique servi sans `importee`, borne de conception 4 dans les deux bras, marque « imposée » de l'origine, indice des graines sur les lignées d'origine. Mutations c01, c03, c04 : l'essai échoue. Texte, Métrique. |
| CE4-06 rondes importées ; dépense double | **traitée** | `importee` d'après l'index, `totaux_hors_importees` (essai, m12) ; point 12 : `depense_totale_usd`. Parenthèse inexacte pour A (CL5-11). |
| CE4-07 gardes du lanceur | **traitée** | (a) `unshare -n`, `protected_hardlinks`, non-root : essais ; l. 73 et 74 (espaces de noms, dossier en mémoire) justes, rejouées par moi avec un faux `unshare`, sans essai (CL5-06) ; (b) fichier non suivi ; (c) vivier absent du commit, code 2 ; (d) Brave par le fichier et le manifeste de A ; (e) parité Gemini ; (f) verrou d'extraction (trois lancements doubles) ; (g) `fin.json` et `erreurs.txt` scellés. 53 sur 53 rejoués. |
| CE4-08 même hôte ; durée | **traitée** | Empreinte de l'hôte exigée (essai `autre-hote`) ; épreuve de durée : format rejoué sur une copie raccourcie du lanceur (JSON, compagnon vérifiable depuis le dossier, porte juste ; trou de 200 s refusé). Limites : CL5-09. |
| CE4-09 clé Gemini, GO | **traitée** | R-370 cité ; l'appel de contrôle est fait avec `go_id = GO-2026-10-24-07` (lanceur l. 266) ; état dit. Mais l'état observé ici diffère (CL5-08). |
| CE4-10 procédures, réserve, mesures | **traitée** | (a) `exclues` codé ; (b) réserve propre ; (c) rondes de conception comptées ; (d) vérification `find` par empreintes : texte ; (e) rapport des deux familles. Rejoué (S3) : refus de fuite en conception → audit ; `defaut_paires` sans `exclues` → refus ; avec → réserve qui nomme la paire. Aucun essai du dépôt (CL5-04). |
| CE4-11 réfutation à tort | **traitée** | Seuil : 0,5 %, 4,5 %, 9,2 % = `puissance-v2.json` (rejoué identique, `50a1c248…`). |
| CE4-12 première occurrence | **traitée** | Refus à plus d'une occurrence (essai `graine-en-double`) ; v5 : 0 occurrence avant remplissage, 1 après (essai de scellement sur une copie). |
| CE4-13 menues inexactitudes | **traitée** | `recherche` retiré du manifeste (essai) ; `5f2e6e51…` et GO-07 cités ; clés hors de toute ligne de commande (rejoué : 86 lignes de commande examinées, aucune clé ; voir plus bas). |

Bilan : 12 traitées, 1 en partie.

### Revérification du code sur `5e6876d`

| remarque | état | preuve |
|---|---|---|
| RV-01 (bloquante) lecture arrêtée sans réponse | **traitée** | Le noyau écrit et scelle `juge/reponses-lues.json` pour chaque génération notée (`{}` sans réponse) ; `reponses_finales` ne lit que lui ; marque d'ordre d'octets lue comme par le juge (essai, m5) ; S2 : paires coupées, pas d'erreur. |
| RV-02 dossiers vivants ; même décalage | **traitée** | Dossiers vivants à root en 0700 après chaque dépôt (essai rejoué avec les données, m3) ; `--depuis` au décalage de l'origine refusé (c12). La mémoire passe pourtant aussi par un dossier commun de l'hôte (CL5-02). |
| RV-03 vue importée lisible | **traitée** | Groupe de la lignée dès l'import (essai, lecture réelle sous un autre utilisateur ; m4). |
| RV-04 /tmp communs | **en partie** | Quatre dossiers en mémoire privés (essai ; m6 ; c09, plus forte : montage sauté, liste gardée → l'essai échoue à la lecture). Mais un autre dossier inscriptible par tous reste commun (CL5-02) et l'hôte est lisible (CL5-01). |
| RV-05 liens et tubes | **traitée** | Statut par `lire_fichier_organisme`, erreurs par le descripteur du noyau (essai, m9). |
| RV-06 espaces de noms en réel | **traitée** | Refus en réel (essai ; c02). |
| RV-07 notices, courts, oracle | **traitée** | Notices retirées et comptées (m11) ; recoupements courts au journal du noyau ; empreintes hors de l'index lisible (essai de quarantaine). |
| RV-08 appels en vol | **traitée** | Attente bornée à 900 s, reste compté (essai, m2). Durées au pire non mises à jour (CL5-11). |
| RV-09 contexte de B | **traitée** | Borne de conception et historique égaux (c03), marque d'origine (c04). |
| RV-10 sortie d'audit ; fonction unique | **en partie** | `lire_h_g1` existe et marche (rejoué S1 à S5) ; **aucun essai ne l'appelle** ; le refus de `defaut_paires` sans `exclues` n'est protégé par aucun essai (c05 : essai aveugle) ; `exclues` est accepté sans audit (S4) (CL5-04). |
| RV-11 erreurs de l'organisme comptées | **traitée** | `echec_exterieur` (c08). Réserve CL5-07 (crédit épuisé chez Anthropic, clé invalide chez Gemini, certificat). |
| RV-12 câblage ; gabarits | **traitée** | Essai de bout en bout (m1) ; fenêtres de l'entraînement écartées. |
| RV-13 traits non protégés | **en partie** | Code présent (`cli.lancer`) ; **aucun essai** (c06 : essai aveugle) (CL5-05). |
| RV-14 CE3-17 | **traitée** | Déjà dans `b7374a9` (vérifié par la contre-lecture n° 4). |
| RV-15 manifeste et temps | **en partie** | `coeurs` (essai), `recherche` retiré ; « délais réseau par opération : dit (Plan, point 4) » : **absent** du point 4 (CL5-05). |
| RV-16 essais et empreintes | **en partie** | Artefacts nouveaux : même décalage que l'origine, liens sur statut et erreurs : faits. « Tirage » : aucun essai nouveau ne discrimine le tirage à trois niveaux ; aucun artefact de décalage invalide (CL5-05). Empreintes : celles du texte, concordantes. |

Bilan : 11 traitées, 5 en partie.

---

## Remarques nouvelles

### CL5-01 — bloquante — Le test final est lisible par les organismes sur l'hôte recommandé

- Fichiers : `bac_a_sable.py` l. 249-270, 330-340 (l'espace de montage de l'organisme est celui de l'hôte, seuls /tmp,
  /var/tmp, /dev/shm, /run/lock sont recouverts) ; lanceur v3 l. 48-49, 103, 290 (`DEPOT` et `CODE` sans contrôle de
  droits) ; texte l. 210-211, 442-451 (« isolation tenue par le noyau »), l. 506 ; contrat § 2 (« sans accès hors de son
  dossier de travail »).
- Défaut : `/home`, `/home/user`, `/home/user/controle-ia-travail`, son `.git` et ses paquets sont lisibles par tous
  (755, 444). Le commit `bffe03c` y contient `banque-confrontation-v1.json` (la banque que le noyau note, vérités du test
  final comprises) et le fichier secret ; le commit du code `44cd936` les contient aussi (même objet `a6f6994c…`), donc
  l'arbre `CODE` extrait pour les courses les porte en clair. Un organisme qui parcourt le système de fichiers peut lire
  toutes les vérités, dans les deux bras. Il n'y a pas de biais de Δ par construction, mais : un score saturé fait
  « défaut du noyau » (non concluant après la dépense) ; une exploitation partielle sous 0,95 ne déclenche pas l'audit et
  rapproche les bras (« réfuté » à tort possible).
- Preuve rejouée (`sortie-cl5-lecture-hote.txt`, `28d5c545…` ; script `cl5_lecture_hote.py`) : un organisme exécuté par
  `bac_a_sable.executer` (utilisateur 60700, espaces de noms, réseau coupé, /tmp privés) liste le dépôt (34 entrées), lit
  l'en-tête `PACK` d'un paquet git, et `git cat-file -s` rend la taille de la banque (1 207 135 octets) et du fichier
  secret (55 918). **Aucun contenu lu ni affiché.** Droits : `sortie-cl5-hote-droits.txt`.
- Correction proposée : (1) lanceur : refuser si `DEPOT`, `DEPOT_GIT`, `CODE` ou l'un de leurs parents est traversable
  par les autres (même règle que le dossier des courses), et faire passer l'hôte (par exemple `chmod 0700` sur le dépôt et
  sur le dossier de `CODE`) ; (2) mieux, noyau : dans l'espace de montage de l'exécution, recouvrir d'un dossier vide en
  lecture seule `/home`, `/root`, `/srv`, `/mnt`, `/media` et tout chemin du code ou des données ; (3) essai sain et
  artefact (un fichier témoin lisible par tous, hors du dossier de travail, doit être invisible) ; (4) texte : dire ce qui
  est tenu.

### CL5-02 — majeure — Une voie commune entre bras reste ouverte hors des quatre dossiers privés

- Fichiers : `bac_a_sable.py` l. 57 (`DOSSIERS_TMP_PARTAGES` : quatre noms fixes), l. 145-161 ; lanceur v3 l. 72-75
  (aucun contrôle des autres dossiers inscriptibles) ; texte l. 210-211 (« aucune voie commune entre bras, répliques ou
  lignées hors des vues »), l. 442-446, l. 506 (« impossible »).
- Défaut : sur l'hôte, `find / -xdev -type d -perm -0002` trouve aussi `/var/lib/php/sessions` (1733). Un organisme peut
  y créer un fichier lisible par tous ; un autre utilisateur qui en connaît le nom le lit. A_r et B_r relancent le même
  code g000 : un nom fixe dans ce code suffit pour que A (avec gradient) laisse à B ce qu'il a appris, ou pour lier A_1 et
  A_2 qui tournent ensemble. Le sens va contre la prédiction (Δ tiré vers 0) ; l'indépendance des répliques n'est plus sûre.
- Preuve rejouée (`sortie-cl5-voie-commune.txt`, `61f38877…` ; `cl5_voie_commune.py`, avec un dossier 1733 de mon dossier
  de travail lié sur `/var/lib/php/sessions` dans un espace de montage privé, rien d'écrit sur l'hôte) : l'utilisateur
  60100 (décalage de A_1) écrit, l'utilisateur 60300 (décalage de B_1) lit « sonde de A : 0.93 » ; le même essai par /tmp
  rend `FileNotFoundError` (la correction RV-04 marche pour /tmp).
- Correction proposée : dans l'espace de montage de l'exécution, remonter `/` en lecture seule après avoir lié le dossier
  de travail et le dossier des sockets en écriture (seuls lieux inscriptibles : eux et les dossiers en mémoire) ; à défaut,
  recouvrir tout dossier inscriptible par tous trouvé au départ ; et refus du lanceur sur un hôte qui en garde un ;
  essai sain et artefact (le scénario ci-dessus).

### CL5-03 — majeure — La répétition refuse l'amorçage de Fable : la porte ne peut jamais passer

- Fichiers : lanceur v3 l. 225-228 (`--usd-par-generation 3`) ; `boucle.py` l. 499-502 et 505-520 (l'amorçage prend le
  plafond d'une génération, `min(usd_max, restant)`) ; `appels.py` l. 137-143 (réservation au pire cas, `max_tokens` du
  modèle à l'amorçage) ; texte l. 324-325, 361-367 ; porte l. 320-327.
- Défaut : le pire cas d'un appel d'amorçage de Fable au maximum du modèle (64 000 jetons) vaut 3,27 USD avec un prompt de
  20 000 caractères, 3,40 USD à 60 000 ; le plafond de la répétition est 3 USD par génération. L'appel est refusé avant
  d'être envoyé (`AMORCAGE_PLAFOND`) ; la porte écrit « claude-fable-5-1 : amorçage AMORCAGE_PLAFOND (attendu
  ORGANISME_VALIDE) » ; le lanceur refuse alors toute course décisive. C'est l'ajout de Fable demandé par CE4-04 (3) sans
  relever ce plafond. Sûr (rien ne part à tort), mais l'expérience ne peut pas commencer sans addendum.
- Preuve rejouée (`sortie-cl5-amorcage-repetition.txt`, `a45baeb9…`) : course simulée aux options exactes de la
  répétition (hors mode réel et entrées réelles) : Fable `AMORCAGE_PLAFOND` (« plafond 3.00 USD … pire cas 3.26 »), Opus
  et Argon `ORGANISME_VALIDE` ; témoin à 4 USD : Fable `ORGANISME_VALIDE`. Pires cas recalculés par
  `cout_pire_cas` du collisionneur cité.
- Correction proposée : `--usd-par-generation 4` (ou plus) pour la répétition, avec le plafond total et l'annexe
  recalculés ; ou un plafond d'amorçage propre. Corriger aussi la phrase « amorçage compté 3 × 12 » (l'amorçage prend le
  plafond d'une génération, 20 USD en A_r). Ajouter un essai qui fait tourner la répétition simulée aux options du
  lanceur et calcule sa porte.

### CL5-04 — mineure — La lecture gelée n'a pas d'essai ; `exclues` passe sans audit

- Fichiers : `analyse_gradient.py` l. 441-442, 464-489 ; `tests/test_noyau.py` (aucun appel de `lire_h_g1`, aucun
  `defaut_paires`, aucun `exclues`).
- Défaut : R5 — la fonction gelée qui compose toute la lecture (RV-10) et le refus de `defaut_paires` sans `exclues`
  (CE4-10 a, b) ne sont protégés par aucun essai (mutation c05 : la suite reste verte). Par ailleurs `exclues` est accepté
  avec `apres_audit=None` : une paire est coupée « trouvé[e] par l'audit de symétrie scellé » alors qu'il n'y a pas eu
  d'audit, et le verdict ne porte aucune réserve.
- Preuve rejouée (`sortie-cl5-lire-h-g1.txt`, `6ab2023d…`) : S1 sain « confirmé » ; S2 « non concluant » (six coupées) ;
  S3 audit, refus sans `exclues`, réserve juste avec ; S4 : `exclues=["claude-opus-5-5@r1"]`, `apres_audit=None` →
  « confirmé », sans réserve.
- Correction : refuser `exclues` hors de `defaut_paires` ; verser un essai de `lire_h_g1` (sain et artefacts, sur le
  modèle de S1 à S5).

### CL5-05 — mineure — Traitements annoncés, sans essai ou non faits

- RV-13 : protection des traits sans essai (c06 aveugle). CE4-02 : comptage `INDISPONIBLE` sans essai (c11 aveugle).
  CE4-10 (c) : comptage des rondes de conception sans essai du dépôt (c10 aveugle ; le comportement est juste, S3).
- RV-16 : « tirage » annoncé, aucun essai ne discrimine le tirage à trois niveaux ; aucun artefact de décalage invalide.
- RV-15 : « délais réseau par opération : dit (Plan, point 4) » — le point 4 ne le dit pas.
- Correction : verser ces essais (sain et artefact) ou corriger la table de traitement ; écrire la phrase du point 4.

### CL5-06 — mineure — Gardes du lanceur justes mais sans essai dans sa suite

- Calcul de la porte de la répétition et de la répétition B (l. 310-343) ; refus des espaces de noms (l. 73) et du
  dossier en mémoire (l. 74), que masque le faux `unshare` qui échoue toujours ; trou de plus de 180 s dans l'épreuve.
- Rejoué par moi, tous justes : `sortie-cl5-porte.txt` (sain A et B ; artefacts code 1, espèce absente, entraînements
  refusés, extrait absent, B lu comme A), `sortie-cl5-gardes-hote.txt`. Correction : les verser à la suite (R5).

### CL5-07 — mineure — Classement des échecs : crédit épuisé, clé invalide, certificat

- Fichiers : `analyse_gradient.py` l. 148-165 ; `appels.py` l. 170 (crédit épuisé = « HTTP 402 » seulement) ; texte
  l. 183-191.
- Défaut : un HTTP 400 est toujours « requête de l'organisme ». Or, à ma connaissance (non vérifiable ici, aucun appel),
  l'interface d'Anthropic a rendu un crédit épuisé en HTTP 400 (« credit balance is too low ») ; la clé invalide de Gemini
  est aussi un 400 ; une erreur de certificat levée sans `URLError` n'est pas reconnue, alors que le texte compte
  « certificat, clé » comme extérieurs. Un tel échec dans B seul (qui tourne des heures après A) ne coupe pas la paire et
  n'arrête pas la course ; entre 80 et 100 % de couverture, il compte dans le sens prédit. Preuve :
  `sortie-cl5-echec-exterieur.txt`.
- Correction : reconnaître ces messages (crédit, clé invalide, `CERTIFICATE_VERIFY_FAILED`) comme extérieurs, et le crédit
  épuisé comme `CREDIT_EPUISE` quel que soit le code ; ou le dire comme limite.

### CL5-08 — mineure — « État au scellement » contredit par l'environnement observé

- Texte l. 289-291 (Brave absente de la session) et l. 294-297 (clé Gemini n° 2 non visible).
- Constat (noms seulement, aucune valeur lue) : dans ma session, même conteneur, à 01:5x UTC après le redémarrage,
  `BRAVE_API_KEY`, `GEMINI_API_KEY_2` et `ANTHROPIC_BASE_URL` sont définies. `noyau_env` retire bien `ANTHROPIC_BASE_URL`
  (vérifié). Si Brave est présente au lancement, la source `web` est servie aux deux bras (parité tenue par le lanceur) et
  la règle des pannes a cinq comparaisons par paire, pas quatre (le « 1,1 % » le suppose).
- Correction : relire l'état au scellement et l'écrire ; dire le cas « Brave présente ».

### CL5-09 — mineure — L'épreuve de durée ne couvre ni la durée des courses ni un redémarrage

- Texte l. 310-314, 328-329 ; lanceur l. 84-102.
- Défaut : l'épreuve dure 2 h 15 ; A_r dure jusqu'à 10,5 h (jusqu'à environ 15,75 h avec l'attente de 900 s des appels en
  vol). Le conteneur a redémarré aujourd'hui vers 01:29 UTC et tous les processus ont disparu (message du coordinateur) ;
  l'empreinte de l'hôte est la même avant et après (`eafadea7…` à 01:22 et 01:51), donc « même hôte » ne voit pas un
  redémarrage. Le texte ne dit pas non plus que les courses décisives sont lancées détachées comme l'épreuve. La règle
  d'arrêt de l'hôte reste juste et ne favorise aucun signe ; c'est la dépense et l'information qui sont en jeu.
- Correction : écrire le mode de lancement des courses (détaché, PID consigné) ; dire la limite ; envisager une épreuve
  plus longue que la conception de A_r.

### CL5-10 — mineure — Une porte non passée peut venir de l'organisme, et n'a pas de suite écrite

- Lanceur l. 333-341 ; texte l. 371-381.
- Défaut : les statuts comptés « demandés » comprennent des refus causés par l'organisme (`REFUSE` d'une spécification
  d'entraînement, téléchargement hors provenance) : deux entraînements mal écrits suffisent à faire échouer la porte. Le
  texte ne dit pas ce qui suit une porte non passée sans défaut de code (nouvelle répétition dans un nouveau dossier ?
  addendum ?).
- Correction : ne compter que les échecs du noyau ou du fournisseur, ou écrire la suite.

### CL5-11 — forme — Chiffres et renvois

- « pièce `mutations-rv-v2.txt` » : la pièce s'appelle `sortie-mutations-v2.txt` ; « 53 sur 53 », « 126 essais », « douze
  corrections » et les options de l'analyseur sont cités sans empreinte (R6).
- « au plus 0,71 % » vaut à effectifs égaux ; à effectifs inégaux (A répond par ses sondes, B par des appels) j'obtiens
  0,76 % (60 contre 480 tentatives, p = 0,3 ; `sortie-cl5-pannes.txt`) ; le critère « ≥ 3 échecs d'écart » compare des
  comptes bruts d'effectifs inégaux.
- Durées « au pire » (l. 328-329) sans l'attente de 900 s ; point 12 : « égale aux totaux hors rondes importées de
  l'extrait » est faux pour A (l'amorçage n'est pas dans l'extrait : 0,039 contre 0,314 USD en simulation,
  `sortie-cl5-depense-extrait.txt`) ; « même ordre des lignées » seulement quand les mêmes lignées sont actives ; en tête,
  « sans changer … table de lecture », alors qu'une ligne procédurale est ajoutée (sans effet sur les verdicts).

### CL5-12 — forme — Script de scellement

- `sceller_etape1_v5.py` : la docstring parle encore de « la contre-lecture n° 4 » ; rien n'exige que `vivier_message`
  porte les comptes de `charger_vivier` sur le vrai fichier et l'empreinte du message (CE4-03, R6). Essai à blanc sur une
  copie (valeurs factices) : remplissage, entropie et graines justes, validateur sans plainte, une occurrence de chaque
  nom lu par le lanceur.

---

## Points demandés

**Règle des pannes.** Juste et vérifiée (CE4-01) ; limites CL5-07, CL5-08, CL5-11. **`lire_h_g1` et sortie gelée** :
justes (S1 à S5), sans essai (CL5-04). **`juge/reponses-lues.json`** : écrit pour toute génération notée, `{}` sans
réponse, lu seul ; absence = erreur. **Dossiers en mémoire et appels en vol** : justes pour leurs quatre dossiers et pour
l'attente ; CL5-02. **Garde Unicode et deux sens** : justes (m8, m10, c13). **Indice de lignée des graines** : juste (c01) ;
la base vient de l'index et du dernier rapport de A, qui ne contiennent que les lignées amorcées : même ensemble que dans A.
**Extrait v2** : juste (essai, m12). **Portes du lanceur** : lecture juste (essais), calcul juste (rejoué), mais la porte
de la répétition ne peut pas passer (CL5-03). **Environnement du noyau** : treize variables, valeurs justes, aucune clé
dans les 86 lignes de commande lues pendant l'exécution (`sortie-cl5-noyau-env.txt`, clés factices).

**Asymétrie nouvelle entre A et B** introduite par les corrections : aucune trouvée dans le code corrigé ; les
voies hors des vues (CL5-01, CL5-02) et le classement des échecs (CL5-07) sont antérieurs.

**Texte (R1).** Complet. Prédiction : identique à la v4. Hypothèse : seule la liste descriptive de H-C change (« refus et
retraits »). Table de lecture : une ligne procédurale ajoutée (`defaut_paires` sans `exclues`), sans effet sur les
verdicts. Seuil : limites ajoutées. Métrique : la règle des pannes change (la v4 n'était pas scellée ; c'est la
correction demandée). Validateur (`prereg.py` des pièces = celui du dépôt, `3b2e3ee5…`) : deux plaintes exactement,
« contre-lecture 5 sans ses deux empreintes » et les cinq marqueurs ; après remplissage factice : aucune.

---

## Ce que j'ai rejoué

Tout dans `…/r2-etape1-v5/travail/`, en root, sous `env -i PATH=/usr/bin:/bin HOME=<travail>/home LANG=C.UTF-8`,
`python -B`, `/opt/essaim-m3-venv-v1` (Python 3.13.17, numpy 2.4.6, anthropic 2.3.0, lus). Les essais et scénarios qui
lancent des organismes ont tourné dans un espace de montage privé où `/var/lib/essaim-m3` et `/var/tmp` (et, pour CL5-02,
`/var/lib/php/sessions`) sont liés à des dossiers de mon dossier de travail (`scripts/dans_ns.sh`, `dans_ns_php.sh`). Copie
du code dans `travail/code` ; pour les cinq essais qui lisent les données retirées des pièces, copie de l'arbre au commit
(`travail/code-donnees`, tirée du clone partagé `travail/git`). Aucun appel à une interface de modèle ni à une source de
moisson ; aucune clé lue, affichée ou écrite (clés factices ; noms seulement pour CL5-08) ; aucune écriture git hors de mon
clone ; aucun script de la relève de Gemini ; aucun sous-agent. Processus : épreuve raccourcie (PID 12954) finie d'elle-même,
vérifiée ; aucun processus d'organisme restant. Incident : la mutation c09 (montage sauté) a écrit deux fichiers témoins
sur l'hôte (`/tmp/rv04-c55ace00fe40`, `/dev/shm/rv04-c55ace00fe40`) ; je les ai retirés par leur nom. Un
`/tmp/rv04-73f8b7fb4cdf` daté de 00:58, antérieur à ma session, est resté en place (pas de moi).

| quoi | résultat | sortie (`travail/`) | empreinte |
|---|---|---|---|
| suite du noyau, pièces | 120 réussis, 6 échecs : 4 + 1 par données absentes, 1 par mon lien de `/var/tmp` en 0755 | `sorties/sortie-pytest-44cd936-pieces.txt` | `41c856ee…` |
| RV-04 et métrique, `/var/tmp` en 1777 | 2 réussis | `sorties/sortie-pytest-rv04-vartmp-1777.txt` | `b88588a5…` |
| 5 essais avec données | 5 réussis (126 au total) | `sorties/sortie-pytest-5-essais-avec-donnees.txt` | `43d5685d…` |
| diff `ed3ce0e..44cd936` | = pièce | `diff-rejoue-ed3ce0e-44cd936.patch` | `a9d39e8d…` |
| empreintes citées | 28 concordent | `sorties/sortie-empreintes-citees-v5.txt` | `d5a13ca4…` |
| essais du lanceur v3 | 53 sur 53, mêmes états | `sorties/sortie-essais-lanceur-v3-rejoues.txt` | `130819df…` |
| validateur, v4 → v5 | marqueurs et entrée 5 ; sections | `sorties/sortie-validateur-v5.txt`, `sorties/sortie-diff-v4-v5-sections.txt` | `a40efe22…`, `cc1b48c0…` |
| scellement à blanc | sans plainte, une occurrence par nom | `sorties/sortie-scellement-essai.txt` | `603344f4…` |
| puissance rejouée | identique (`50a1c248…`) | `puissance/puissance-v2-rejouee-cl5.json` | `50a1c248…` |
| coupures rejouées | identique (`7028c3f4…`) | `pannes/coupures-rejouees-cl5.json` | `7028c3f4…` |
| Fisher, formule, effectifs inégaux | exact ; = simulation ; 0,76 % | `sorties/sortie-cl5-pannes.txt` | `3ca449ed…` |
| classement des échecs | CL5-07 | `sorties/sortie-cl5-echec-exterieur.txt` | `4026f278…` |
| CL5-01 lecture de l'hôte | banque atteinte | `sorties/sortie-cl5-lecture-hote.txt`, `sorties/sortie-cl5-hote-droits.txt` | `28d5c545…`, `cbbf7194…` |
| CL5-02 voie commune | A → B par `/var/lib/php/sessions` | `sorties/sortie-cl5-voie-commune.txt` | `61f38877…` |
| CL5-03 amorçage de Fable | `AMORCAGE_PLAFOND` à 3 USD | `sorties/sortie-cl5-amorcage-repetition.txt` | `a45baeb9…` |
| `lire_h_g1` S1 à S5 | CL5-04 | `sorties/sortie-cl5-lire-h-g1.txt` | `6ab2023d…` |
| 13 mutations complémentaires | 9 échouent, 4 aveugles (c05, c06, c10, c11) | `sorties/sortie-cl5-mutations.txt` | `3c1d624c…` |
| porte calculée | juste | `sorties/sortie-cl5-porte.txt` | `843f008e…` |
| gardes d'hôte l. 73-74, trou d'épreuve | justes | `sorties/sortie-cl5-gardes-hote.txt` | `99ea333e…` |
| épreuve raccourcie (copie, 4 s) | format et compagnon justes | `exp-cl5-epreuve/epreuve-duree.json` | `740b66a2…` |
| environnement du noyau | aucune clé en ligne de commande | `sorties/sortie-cl5-noyau-env.txt` | `8bcb0d4f…` |
| dépense de l'extrait | CL5-11 | `sorties/sortie-cl5-depense-extrait.txt` | `eac2d631…` |

Empreintes complètes de mes sorties et scripts : `travail/EMPREINTES-travail-cl5-v1.txt` (`38041ffa…`, compagnon).

## Ce que je n'ai pas pu vérifier

- Le fichier du vivier (il n'existe pas) et ses comptes ; la banque réelle hors des cinq essais qui la lisent.
- Le code que rend l'interface d'Anthropic pour un crédit épuisé (CL5-07 : de mémoire, à confirmer).
- Les courses, la moisson et les espèces réelles ; l'en-tête d'espace de travail accepté par le serveur (l'interface
  Python lit bien `ANTHROPIC_CUSTOM_HEADERS`, vérifié dans le paquet).
- Si l'hôte retenu sera ce conteneur ; s'il redémarre souvent ; si ses variables d'environnement au lancement seront
  celles que j'ai vues.
- Les décisions et registres cités (R-xxx, GO) : hors des pièces.
