# Essai Lean, outillage D-1a — rapport du développeur-opérateur — v1

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. **Écrit par** : sous-agent neuf, développeur-opérateur, modèle
  Opus 5.5 (`claude-opus-5-5`) ; je n'ai écrit ni le dessin de l'essai, ni ses contre-lectures.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-outillage-lean-d1a-v1.md`
  (`9712756a9fca2ca38717cd56d8cfaab6314004c3cf1b484e21d8ea2c6591c40b`, vérifiée avant lecture). Lus et vérifiés : brouillon 3
  (`717259ed…`), journal v3 (`0bc956d6…`), vérification courte (`38e40d21…`), contre-lecture 1 (`f565d51c…`).
- **Dépense** : GO-2026-11-10-13. **Dépensé : 0 USD.** Aucun serveur, aucune clé SSH, aucun pare-feu créé chez Hetzner ;
  aucun appel de modèle. Heures relevées par `date -u` : début 2026-11-11 00:02:39 UTC ; rapport écrit vers 00:30 UTC.

## Verdict

1. **Mandat 1 (sans dépense) fait** : harnais et environnement isolé écrits en code neuf, **68 essais R5 locaux passent** (cas
   sains et artefacts de chaque garde, dans la mesure où elle s'éprouve sans Lean), commit `558bcf974c62b1531d66370f896ddb718541398d`
   sur `prep/lean-outillage-d1a-v1`, poussé, **sans fusion** dans `main`.
2. **Mandats 2 et 3 non faits, sur consigne de la mère** : l'opérateur de la course a établi que cette session ne joint aucune
   machine par SSH (sortie vers le port 22 refusée localement, comme en R-821) ; la mère m'a ordonné de ne créer aucun serveur
   et de n'essayer aucun autre port (règle 6). Les pièces VERSION-LEAN, COMMIT-MATHLIB et MACHINE restent donc **à remplir** ;
   HARNAIS-ET-ISOLEMENT est rempli ; ESSAIS-R5 l'est pour la partie hors machine seulement.
3. La voie vers une machine joignable (poste de Lazar ou autre) est à décider par Lazar ; le pilotage depuis un poste est écrit
   (`piloter_poste_v1.sh`), non éprouvé.

## Pièces du § 9 du brouillon 3

| Pièce | Valeur |
|---|---|
| **HARNAIS-ET-ISOLEMENT** | commit `558bcf974c62b1531d66370f896ddb718541398d` (arbre `3363132ecfbb4f45e81f8bced1c751872064539a`), branche `prep/lean-outillage-d1a-v1` de `lciric/controle-ia-travail` ; 48 fichiers neufs ; empreintes de chaque fichier : `empreintes-harnais-v1.txt` (ce dossier). Modules : `gardes_lean_v1.py` `e99d60e7f9ddbc9b2480d6257d42e7503b3ad3699cbe8984751b92680d4740d9`, `executeur_bac_v1.py` `5810179be7701c4cb6b0218e51170b94670e891f25853b0635a0faded0d9be51`, `epreuve_isolement_v1.py` `5fc457bf9b16a69a320e3d844cbb77ed548cb4879380168c93dfaf6b258c2334`, `sonde_reseau_v1.py` `6f9a666b276c72d6bce93690fb8b23173d090945acf7d912e88075596323bcdd`, `budget_v1.py` `b9793c00dfba409478adc4edc104d01626d6f90d0ebb42189eb2d9e6a62934a5`, `garde_go_v1.py` `6e41dc8d48597eab5b59f828a6b59e17b3912d9873c01a56d1ec53330fb262a3`, `hetzner_v1.py` `1145272c80862a2482f4a45600df208dae902d1aecb8659cad5aa5535912eb40`, `minuterie_v1.py` `aa91b47225b4f6f39a94a2cfba13f370b01facc3de5167a9c927dbf9a3e0e309`, `sortie_v1.py` `dc14622d79411bd74f0f22dc82d4a40b41cfd4a4caabc5d3d3b4fda0d3e80b70` |
| **ESSAIS-R5** | **partiel** : hors machine, 68 essais passent (`journal-essais-r5-locaux-v1.txt`) ; sur la chaîne installée, **non fait** (aucune machine joignable) : `epreuve_isolement_v1.py epreuve` et `artefacts_r5_v1/attendus-v1.json` sont prêts |
| **VERSION-LEAN** | **à remplir** à l'installation (`lean-toolchain` du commit de Mathlib épinglé, `lean --version`, consignés par `installer_chaine_v1.sh` dans `/opt/harnais/chaine-v1.json` et le journal d'installation) |
| **COMMIT-MATHLIB** | **à remplir** : choisi par `choisir_commit_mathlib_v1.sh` (dernière étiquette stable `v4.X.Y`), passé tel quel à `installer_chaine_v1.sh`, qui s'arrête si `HEAD` diffère ; je n'ai lu aucun dépôt public pour le choisir d'avance |
| **MACHINE** | **aucune créée**. Proposition seulement, sur relevé en lecture seule de l'API (`GET /v1/server_types`, 2026-11-11 00:28:19 UTC, `types-serveurs-hetzner-releve-v1.txt`) : **Hetzner `ccx33`** (8 cœurs dédiés x86, 32 Go, 240 Go de disque), 0,2260 EUR/h TTC à `hel1`, au plus 0,3355 EUR/h selon le lieu, soit 16,10 EUR pour 48 heures (≈ 20,1 USD à 1,25 USD l'euro, taux non vérifié, choisi haut) ≤ 65 USD ; cœurs dédiés pour un temps de processus reproductible, 32 Go pour trois processus Lean en parallèle avec Mathlib (mémoire par processus à mesurer). Moins cher : `cx53` (16 cœurs partagés, 32 Go) 0,0568 EUR/h ; `ccx23` (4 cœurs dédiés, 16 Go) 0,1404 à 0,2087 EUR/h. Identifiant : aucun |

## Ce qui est écrit (code neuf, branche seulement)

- **Gardes G-L1 à G-L7** (`gardes_lean_v1.py`, autonome, copié tel quel sur la machine) : lexique Lean masqué (commentaires
  imbriqués, chaînes, chaînes brutes, caractères ; élément non fermé ⇒ échec de chaque garde textuelle) ; G-L2 par le texte,
  l'avertissement « declaration uses 'sorry' » et `#print axioms` du **fichier de contrôle du harnais** ; G-L3 par le texte et
  par l'énumération des constantes du module de l'agent (une constante de genre axiome échoue même sans le mot) ; G-L4 par le
  texte et par `#check @etape_i` du contrôle ; G-L5 énoncés imprimés par Lean, transmis au relecteur (`pour_relecteur`) ; G-L6
  mots interdits, définitions imprimées en entier, et **toute constante non théorème du module ni imprimée ni descendante d'un nom
  imprimé ou attendu** (instance anonyme comprise) ; G-L7 contrôle écrit **après** la compilation de l'agent, hors de son
  dossier, exécuté dans un second bac où item et contrôle sont en lecture seule, empreinte avant et après, marqueur de fin.
- **Bac** (`executeur_bac_v1.py`) : utilisateur `bac` sans privilège ; `systemd-run` (MemoryMax 6G, MemorySwapMax 0, TasksMax
  256, LimitCPU 1800 s, RuntimeMaxSec 2100 s, LimitFSIZE 1G, `IPAddressDeny=any`) ; `bwrap --unshare-all` (aucun réseau),
  racine vide remontée en lecture seule, `/usr`, `/opt/elan`, `/opt/mathlib`, `/opt/pybac` en lecture seule, `/tmp` neuf ;
  dossier neuf par item (refus s'il existe), détruit après ; sorties écrites par systemd hors de la vue du bac ; processus
  résiduels arrêtés par PID (R10).
- **Machine** (`scripts/lean_essai_d1a_v1/`) : installation réseau ouvert (chaîne et Mathlib au commit épinglé, propriétaire
  `chaine`, montages liés en lecture seule dans `/etc/fstab`, Python du bras S aux versions de `.venv`) ; coupure à deux étages
  (pare-feu du nuage : une seule règle sortante ICMP vers 192.0.2.1/32 ; `nftables` au démarrage : DNS refusé, DHCP et
  métadonnées seuls permis) ; sonde classée par la cause (« ouverte », « fermée », « indéterminée », boucle locale en cas sain) ;
  épreuve d'isolement (leurre à jeton aléatoire, manifeste de la chaîne avant et après, fichiers pièges absents de l'hôte,
  dossiers vides, aucun processus résiduel) ; mesures (item sain trois fois, puis trois en parallèle).
- **Harnais hors machine** : A7 (`CompteurPhase`, réserve 32, coût réel au-dessus du pire cas ⇒ arrêt), plafond par item, A8
  (`decision_a8`, retrouve 60 / 50 / 40 graines à 578 USD et l'arrêt à 550 du devis v5), A12 (`AppelsModeleGardes` : registre
  relu à chaque appel ; aucun transport en D-1a), garde du GO cité à la création, A13 (`minuterie_v1` : heures entamées ×
  prix, échéance 48 h, plafond moins une heure, destruction par identifiant après lecture du nom), sortie structurée et verdicts
  des chaînes L et S.

## Essais R5 hors machine (68 passent ; `journal-essais-r5-locaux-v1.txt`)

| Garde | Cas sain | Artefacts |
|---|---|---|
| lexique | `sain_v1.lean` (« sorry », « axiom » en commentaire : aucun motif) | commentaire, chaîne, chaîne brute non fermés |
| G-L1 | compilation sans erreur | code non nul ; message d'erreur ; `.olean` absent ; bac local : erreur de compilation |
| G-L2 | axiomes permis | `sorry` (texte), `stop` sans le mot (vu par `sorryAx`), `Lean.ofReduceBool`, avertissement, sortie illisible |
| G-L3, G-L3+ | aucun mot | `axiom`, `unsafe`, `implemented_by`, `extern` ; axiome vu par l'énumération seule ; `initialize`, `#eval`, `import Lean.Elab`, `set_option debug.…` ; G-L3+ désactivable |
| G-L4 | les trois noms | étape manquante, énoncé renommé, noms dans un espace de noms (vu par le contrôle seul, aussi dans le bac local) |
| G-L5 | énoncés imprimés transmis | étape prouvée à vide : les gardes passent, l'énoncé imprimé porte les hypothèses (sur la machine seulement) |
| G-L6 | définition imprimée en entier | notation locale, instance anonyme (texte et énumération), constante non imprimée |
| G-L7 | contrôle intact et complet | empreinte changée (bac local : contrôle altéré pendant son exécution), texte changé, marqueur de fin absent, contrôle non exécuté, fausse sortie `#print axioms` de l'agent ignorée |
| bac | item sain, dossiers vides après | dossier d'item déjà présent, identifiant `../evasion`, lanceur sans isolement refusé hors essai ; commande du bac contrôlée (aucune liaison de `/srv/leurre`, `/srv/controle`, `/root`, `/opt/harnais`) |
| A7 | lancements sous le plafond | dépassement, coût réel au-dessus du pire cas, appel soldé sans lancement, double lancement |
| A8 | 60, 50, 40 graines à 578 | 35 à 550 ⇒ arrêt ; coût de graine nul, montant négatif |
| A12 | GO fictif de D-1b | GO-2026-11-10-13 (exclut les appels), GO d'une autre course, absent, mal formé, hors période, non accordé par Lazar, révoqué, registre mal formé ou absent, doublon ; la porte ne touche pas le compteur |
| A13 | rien avant l'échéance | échéance, cumul ; serveur d'un autre nom jamais touché ; serveur qui ne disparaît pas ; erreur d'API qui remonte ; devis 1,40 USD/h refusé ; heure sans fuseau |
| sonde | boucle locale « ouverte » | relevé « indéterminé », boucle locale non vue |

Contrôles en lecture du vrai registre `registres/go.md` (aucune écriture) : A12 refuse GO-2026-11-10-13 (« exclut tout appel de
modèle ») et GO-2026-11-10-11 (« pas un GO du pilote D-1b ») ; la garde de création accepte GO-2026-11-10-13 (calcul, Lazar,
échéance 2026-11-30, 65 USD).

## Ce qui ne peut se faire qu'avec une machine joignable (reste du mandat)

1. Créer le serveur (commande citant `GO_ID=GO-2026-11-10-13`, `hetzner_v1.creer_serveur`), lancer la minuterie A13, consigner
   identifiant, heure et prix horaire.
2. `choisir_commit_mathlib_v1.sh`, puis `installer_chaine_v1.sh COMMIT` réseau ouvert : **VERSION-LEAN, COMMIT-MATHLIB**, taille
   de Mathlib, temps du cache et de `lake build`, mode lecture seule vérifié.
3. Sonde « ouverte » avant coupure (cas sain), pare-feu du nuage en coupure (session), `couper_reseau_v1.sh`, sonde « fermée ».
4. Dépôt du harnais **après** la coupure ; `choisir-variante` (A ou B de l'énumération des constantes : interface de Lean à
   éprouver) ; `epreuve` (G-L1 à G-L7 sur la chaîne installée, G-L6 et G-L7 compris, isolement Lean et Python, limites) ;
   `mesurer` (temps et mémoire d'un item jouet, seul et à trois en parallèle).
5. Destruction par identifiant, vérification de l'absence, durée et coût ; lignes de `registres/depenses.md` et `arrets.md`.

## Propositions de lignes de registre (la mère les inscrit)

- `registres/depenses.md` : « 2026-11-11 — GO-2026-11-10-13 (essai Lean, D-1a) — **0,00 USD** — aucune machine créée (SSH
  injoignable depuis la session, consigne de la mère) ; un relevé gratuit de l'API (`GET /v1/server_types`) ; reste du plafond :
  65 USD. »
- `registres/arrets.md` : **aucune ligne** (aucune instance créée, rien à arrêter).

## Incidents

1. 00:02 UTC environ : consigne de la mère « ne crée aucun serveur » (mot « aucune dépense » rapporté, R-2291) ; puis levée
   (R-2292) ; puis consigne « ne crée aucun serveur » (SSH injoignable, établi par l'opérateur de la course) : **aucun serveur
   n'avait été créé**, aucune connexion SSH ni sonde réseau n'a été tentée par moi.
2. Deux défauts trouvés et corrigés **avant** le commit par les essais : substitution des chemins du lanceur local (relisait le
   texte déjà substitué) ; un essai de la minuterie mal écrit (le code était juste).
3. Aucun refus d'un contrôle ou d'un classifieur.

## Réserves

1. **Artefacts Lean jamais compilés** : écrits à la main sans Lean ni Mathlib (aucun ne tourne ici) ; une erreur de syntaxe ou un
   nom de Mathlib changé se verra au premier passage sur la machine (`attendus-v1.json` le dira par cas) et se corrigera en
   version neuve.
2. **G-L3+ est un ajout du développeur, non dans le devis** (commandes qui exécutent du code à l'élaboration ou touchent au noyau,
   `private`, imports hors de Mathlib et de ses dépendances) : à accepter ou retirer au préenregistrement (désactivable).
   Raison : un métaprogramme à l'élaboration peut ajouter une déclaration sans contrôle du noyau, ce que `#print axioms` ne voit
   pas ; une relecture du module par le noyau (`lean4checker` ou équivalent de la chaîne installée) serait la garde de fond,
   proposée, non écrite.
3. **G-L6 plus strict que le texte du devis** : une instance anonyme ou dérivée (`deriving`) fait échouer la garde, faute de nom à
   imprimer ; les consignes des bras devront le dire.
4. **CLP-12 d (étape prouvée à vide)** : aucune garde mécanique ne la détecte ; G-L5 la transmet au relecteur. Une sonde
   mécanique (tenter `False` depuis les hypothèses de chaque étape avec une tactique fixée) est possible, proposée, non écrite.
5. Énumération des constantes (variantes A et B) écrite contre l'interface de Lean de mémoire ; choisie une fois sur la chaîne
   installée ; si aucune ne passe, arrêt (G-L7 ne tient pas).
6. « Aucun code écrit par un modèle » : le harnais et les artefacts sont de moi (sous-agent, Opus 5.5), comme le prévoit le devis
   (« écrit et contre-lu par des sous-agents de la session ») ; le plan ne les exécute sur la machine qu'**après** la coupure du
   réseau. Le harnais n'est pas encore contre-lu.
7. Prix en EUR TTC lus sur l'API ; le taux USD/EUR n'est pas vérifié (1,25 pris haut).

## Fichiers de ce dossier (scellés, compagnons `.sha256`)

`rapport-outillage-d1a-v1.md` (ce fichier), `journal-essais-r5-locaux-v1.txt`, `empreintes-harnais-v1.txt`,
`types-serveurs-hetzner-releve-v1.txt`.
