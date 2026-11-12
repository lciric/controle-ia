# Lanceur durable v5 pour la course A1-v4 (attaque de Goodhart contre le nul v9) — rapport v1

Écrit le 8 novembre 2026, de 16:34 à 17:05 UTC (heures relevées par `date -u`), par un développeur neuf de la session mère
`session_016QhUrrLeN21G7Z9KZobE42`. Rien n'a été lancé : aucune commande `vastai` réelle (faux outil des essais seulement), aucun
appel de modèle, aucun réseau, aucune dépense, aucun commit, aucune poussée, aucun compagnon `.sha256` écrit, aucun fichier existant
modifié (dépôt privé et dépôt public), aucune valeur de clé lue ni affichée (noms de variables seulement), rien lu sous
`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/`. Tout chiffre renvoie à un chemin et une empreinte.

## 0. Verdict (à lire d'abord)

1. **Le lanceur durable v5 existe, en fichiers neufs** (R12), sous `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/` :
   module, amorce, deux configurations de mondes (variante (i) W1 et W2 ; **variante (ii) W2 et W2g, celle que Lazar a retenue**,
   R-1890), essais, différentiel v4 → v5. **138 essais passent** (`essais-lanceur-durable-v5-v1.txt`), dont le cas sain de bout en bout
   sur machine jouet et les artefacts demandés (ligne des appels ≠ 200, ligne machine absente / de type décision / échue / au plafond
   insuffisant / **au périmètre d'une course** (GO-2026-11-08-11) ou de la machine d'A1-v3 (GO-2026-11-05-03), texte non scellé ou à
   l'empreinte fausse, fichier gelé modifié, variante de mondes inconnue, clé absente par son nom, aucune valeur de clé dans la sortie).
2. **Aucun identifiant de ligne machine en dur** : la ligne vient de `GO_ID_MACHINE` (égale à `GO_ID`, convention de la garde de calcul)
   et est vérifiée contre `registres/go.md` de `main` par la garde de `main` elle-même (type calcul, Lazar, non échue, non révoquée),
   **plafond lu sur la ligne** et **périmètre lu** (mots « machine » et « A1-v4 » exigés). Sur le registre réel : GO-2026-11-08-12
   accepté (plafond lu 35 USD, échéance 2026-11-16) ; GO-2026-11-08-11 (dose-réponse, 100 USD) et GO-2026-11-05-03 (machine d'A1-v3)
   **refusés** par le périmètre (essais `test_go_de_la_machine_registre_reel_refuse_dose_reponse_et_a1_v3`). L'ordre de course doit
   tout de même fixer l'identifiant exact : la lecture du périmètre est une seconde garde, non un choix.
3. **Ce que le lanceur attend du texte** (section 4) : la ligne `mondes:` du bloc `plan-gele` égale à `mondes_texte` de la configuration
   (**`W2 et W2g`** pour la variante (ii), comme l'écrit le brouillon 3) ; `go: GO-2026-11-02-22`, `plafond_usd: 200`, `fournisseurs: argon`,
   `mode: course` ; une ligne `go_machine:` si elle existe égale à `GO_ID_MACHINE` ; aucun marqueur `<<…>>` ; chaque fichier gelé public de la
   configuration présent dans le bloc `empreintes-du-code` à la même empreinte ; nom `orchestrator/prereg/<prefixe_texte><N>.md`
   (`preenregistrement-attaque-goodhart-v4-v` dans les configurations v1).
4. **Trois réserves** : (a) le code d'attaque v4 présent ne connaît que W1 et W2 (`MONDES` de `pole/attaque_goodhart_v2.py`) : avec la
   variante (ii), le lanceur gelé v4 refusera la ligne `mondes: W2 et W2g` à `--verifier-seulement` → **rien ne part** (arrêt propre,
   branche de refus) tant que le monde W2g n'est pas dans le code ; ce code v5 demande une **configuration (ii) v2** (section 5) ;
   (b) le brouillon 3 nomme l'étiquette `a1-v4-reprise-v9-v1` et le fichier d'essais `tests/test_hote_durable_a1_v4_v5.py` ; le brief
   de la mère fixe **`a1-v4-v9`** et `tests/test_lanceur_durable_v5_a1v4.py` : j'ai suivi le brief, un couple du texte ou un mot de la
   mère tranche ; (c) les compagnons `.sha256` des configurations et des fichiers livrés sont **à écrire par la mère** (interdit ici) :
   sans compagnon, le lanceur refuse la configuration (essai `test_configurations_livrees_lisibles_et_egales_au_depot_public`).

## 1. Fichiers livrés et empreintes (`sha256sum`, 17:01 UTC ; aucun compagnon écrit)

| fichier (dossier `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/`) | empreinte SHA-256 | destination proposée au commit |
|---|---|---|
| `hote_durable_a1_v4_v5.py` (1 082 lignes) | `352380923e612e3456f4c533d2e2e61af5e7b1a69bd2f99bc5ab39c24beebae2` | copie à `src/controle_ia/hote_durable_a1_v4_v5.py` (l'amorce l'y attend) |
| `amorce_hote_durable_a1_v4_v5.sh` (68 lignes) | `745040bf9a3a0fc5049cc41b9ad13f29e4776370819095edb021724c914b38ca` | copie à `scripts/amorce_hote_durable_a1_v4_v5.sh` (`AMORCE` du module) |
| `configuration-mondes-variante-ii-v1.json` (**livrée**, W2 et W2g) | `6ec37932cf23ec4d9c5d1d1d7ba616e329e1b11329c3df0c76ab02a430c8ff6e` | reste ici ; chemin relatif passé à la location et lu au commit privé par la machine |
| `configuration-mondes-variante-i-v1.json` (acceptée, non livrée) | `efe4f5820096efc912e6033799ff26cd070e0f0c65cde2b86c09af7102db6cad` | reste ici |
| `test_lanceur_durable_v5_a1v4.py` (883 lignes, 138 essais) | `e4f743976ea32370cf633ed37e0d5f0b08cf6b1bf217334ef9520c1c303108ad` | copie à `tests/test_lanceur_durable_v5_a1v4.py` (il charge le module par son chemin : adapter `ICI` si copié) |
| `diff-lanceur-v4-vers-v5.txt` (`diff -u` module puis amorce, 1 626 lignes) | `c387e37fc7edb9953a22d95bf055a187533201aff4a43224c6ebe53c7168ea7b` | trace |
| `essais-lanceur-durable-v5-v1.txt` (« 138 passed in 26.46s ») | `dcc436ef11fcc61c59677d1d695252aea7517123a44fe7d47e119b1814a89bac` | trace |
| `rapport-lanceur-durable-v5-v1.md` (ce fichier) | — (empreinte au commit) | — |

Pièces lues, inchangées : `src/controle_ia/hote_durable_a1_v3_v4.py` `8101d33b…` ; `scripts/amorce_hote_durable_a1_v3_v4.sh` `a2cecc7e…` ;
`src/controle_ia/hote_durable_a1_v3.py`, `sonde_hote_durable_a1_v3_v10.py` ; `tests/test_hote_durable_a1_v3.py` et `_v4.py` ;
`scripts/lancer_t06_v13.sh` (scratchpad `prep-t06-explo-v1`, règle de la ligne de GO lue) ; `registres/go.md` lignes 210, 251, 282, 283 ;
`.claude/hooks/garde_calcul.py` ; dépôt public à `8947bc80` : `demonstrations/attaque_goodhart_v4.py` `6357c0f5…`, `pole/attaque_goodhart_v4.py`
`0077a647…`, `pole/nul_v9.py` `7ae450df…`, `orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon2.md` (bloc `plan-gele`) ;
`docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v4-brouillon3.md` (état de 16:56 UTC, sections 4, 8,
annexe B) ; `docs/notes/ideation-organisme-v1/breche-w2-v1/note-breche-w2-v1.md` (lignes 46 à 53).

## 2. Ce que la v5 fait (différentiel v4 → v5, résumé ; détail dans `diff-lanceur-v4-vers-v5.txt`)

Gardé de la v4 sans changement de fond : machine « gpu » à une carte ≤ 0,40 USD/h (filtre de la sonde v10), minuterie de destruction sur
la machine sans Python, client `vastai` du pilote (délais, certificat, « no_such_ask », réponses catégorisées jamais recopiées), clone
partiel du dépôt privé, deux GO revérifiés sur la machine, registre du canal copié sans retouche et sans doublon, signe de vie exigé (C2),
interpréteur 3.13 et numpy 2.5.3 (C1, correction 7), `git status --porcelain` vide deux fois (correction 5), garde sans session, versement
« partie de main » borné, contrôle des secrets avant versement, destruction vérifiée par l'inventaire sinon arrêt (correction 2), fin qui
attrape tout (correction 3), `controler` en code 6 sur tout échec de `vastai` (correction 1), reprise du conteneur sans relance (C3).

Ce qui change :

| point | v4 | v5 |
|---|---|---|
| texte | `NOM_TEXTE` en dur (`…-v3-v4.md`) | `--texte` (chemin local du texte, N lu dans le nom), `--sha-texte` (empreinte lue au scellement) ; `verifier_texte` chez le pilote et sur la machine (section 4) ; préfixe du nom par configuration (`prefixe_texte`) |
| GO des appels | `h.GO_ATTENDU` GO-2026-11-04-06, 400 | `GO_COURSE` = **GO-2026-11-02-22**, **200 USD exact** sur la ligne et chaque extension (`verifier_go_course`) |
| GO de la machine | `GO_MACHINE` en dur (GO-2026-11-05-03, 35 exact) | **`GO_ID_MACHINE`** de l'environnement (= `GO_ID`), motif, ≠ ligne des appels, garde de `main`, **plafond lu sur la ligne** (une seule valeur sur ligne et extensions), **périmètre lu** (« machine », « A1-v4 ») (`verifier_go_machine`) |
| garde de dépense | `verifier_plafond(dph)` contre 35 en dur | `verifier_plafond(dph, plafond_lu, go)` : chez le pilote **deux fois** (vérification, puis création sur l'offre retenue), sur la machine (`PRIX_H_USD` contre le plafond relu sur `main`) |
| étiquette | `a1-v3-troisieme-v1` | **`a1-v4-v9`** (brief) ; contrôlée au contrôle du pilote, à la facturation, à la destruction, dans la minuterie |
| mondes | W1 et W2, implicites | **configuration JSON + compagnon** (variante (i) ou (ii)), lue par le pilote (`--configuration-mondes`) et par la machine (`git show COMMIT_PRIVE:<chemin>` + compagnon, empreinte = `SHA_CONFIGURATION_MONDES`) ; variante inconnue, mondes discordants, compagnon absent ou faux : arrêt |
| fichiers gelés | 4 pièces privées (`EMPREINTES_GELEES`) | les 4 pièces privées, **plus** `fichiers_geles_publics` de la configuration (11 fichiers : code d'attaque v4, nul v9, nul v8, bancs v7-v8-v9, lanceurs et cœurs v2-v3-v4), vérifiés sur le clone public (pilote et machine) **et** dans le bloc du texte ; `commit_code_gele`, `lanceur_gele`, `dossier_sortie`, `etape_depense` lus dans la configuration |
| clé d'Argon | `CLE_ARGON` déjà présente chez le pilote | lue **par son nom `GEMINI_API_KEY_2`** chez le pilote (seule variable `GEMINI*` permise là), portée sous le seul nom `CLE_ARGON` ; machine et amorce refusent toute autre variable de clé, `GEMINI_API_KEY_2` comprise ; jeton GitHub par `GH_TOKEN` ou `CONTROLE_IA_GITHUB_TOKEN_2` (nom seulement) |
| commande de la course | `demonstrations/attaque_goodhart_v3.py`, `sortie-attaque-goodhart-v3` | lanceur gelé et dossier de sortie de la configuration (`demonstrations/attaque_goodhart_v4.py`, `sortie-attaque-goodhart-v4` en v1), `--preenregistrement prereg/<prefixe><N>.md`, `--go GO-2026-11-02-22` |
| noms sur la machine | `/root/a1-v3-troisieme-v1`, `journal-hote-a1-v3-troisieme-v1.log`, branches `…-a1v3-troisieme-…` | `/root/a1-v4-reprise-v9-v1` (brouillon 3), `journal-hote-a1-v4-v1.log`, `EMPREINTES-sortie-a1-v4-v1.txt`, `garde-a1-v4.jsonl`, `relais-argon-journal-a1-v4.jsonl`, `course-stdout-a1-v4.log`, fichiers du démarrage `a1v4-*`, branches `donnees/attaque-goodhart-v4-a1v4-v1`, `…-refus-v1`, `…-interrompue-v1`, `…-signe-de-vie-v1` (brouillon 3, section 8) |
| sous-commandes | `louer`, `controler`, `facturation`, `offre`, `inventaire`, `hote` | les mêmes, plus **`verifier-texte`** (texte + configuration + fichiers gelés, sans rien créer) ; `louer --verifier-seulement` : tout vérifié, deux calculs de la garde, rien créé |
| variables du corps | 11 | 14 : `NOM_TEXTE`, `CHEMIN_CONFIGURATION_MONDES`, `SHA_CONFIGURATION_MONDES` en plus ; `GO_ID` = ligne des appels, `GO_MACHINE` = ligne vérifiée |
| import | paquet ou fichier seul | paquet, sinon `controle_ia` sur le chemin, sinon fichier seul (voisins, puis `src/controle_ia` du dépôt) : le module tourne depuis `docs/` et depuis `src/controle_ia/` |

## 3. Essais (R5 : chaque garde sur un cas sain et sur un artefact) — 138 verts

Commande : `python -m pytest -q docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/test_lanceur_durable_v5_a1v4.py`
(racine du dépôt privé, `.venv` actif ; `pythonpath = ["src", "tests"]` du `pyproject.toml` ; durée ≈ 26 s). Monde jouet : faux `vastai`
(réponses en fichiers, arguments relevés), faux registre (lignes GO-2026-11-02-22 à 200, GO-2026-11-08-12 à 35, GO-2026-11-08-11 à 100),
dépôt privé nu à quatre branches avec la configuration et son compagnon sur `main`, dépôt public jouet (lanceur gelé factice de la v1,
fichiers gelés factices, texte v4-v1 scellé avec ses deux blocs), relais factice, Vast simulé. Le registre réel de `main` sert aussi aux
cas sains et aux deux refus de périmètre.

| groupe | essais | cas sains | artefacts (→ arrêt explicite, rien créé) |
|---|---|---|---|
| constantes, nom du texte, préfixe | 2 | GO 200, étiquette, branches neuves, aucun identifiant machine en dur dans le source | v3, brouillon, autre dossier, v0, préfixe illisible |
| GO des appels | 7 | ligne factice et ligne réelle | 199, « ≈ 200 », absente, autre identifiant |
| GO de la machine | 18 | ligne factice, **ligne réelle GO-2026-11-08-12**, extension conforme | absente, **type décision**, **échue** (avant et après), pas Lazar, plafond « — » ou « ≈ », plafonds différents, révoquée, égale à la ligne des appels, vide, mal formée, **périmètre d'une course (GO-2026-11-08-11)**, **machine d'A1-v3 (GO-2026-11-05-03)** ; les deux derniers aussi sur le registre réel |
| garde de dépense | 1 | 0,40 USD/h sous 35 | 32, 1 USD, plafond illisible (0, négatif, None, booléen, texte) |
| clés et jeton | 1 | `GEMINI_API_KEY_2` seule permise chez le pilote | `GEMINI_API_KEY`, `KIMI_KEY` ; sur la machine `GEMINI_API_KEY_2` refusée |
| configuration des mondes | 20 | variantes (i) et (ii) ; les deux fichiers livrés lisibles (compagnon calculé), 11 fichiers gelés égaux au clone public local | variante inconnue, variante/mondes discordants, `mondes_texte` vide, étiquette, GO, plafond, commit, préfixe, fichiers gelés vides/illisibles/sans le lanceur, clé en trop ou manquante, compagnon absent, compagnon faux, JSON illisible, fichier absent ; **les fichiers livrés sans compagnon sont refusés** |
| texte | 18 | texte v4-v1 jouet ; ligne `go_machine` égale | v3, brouillon, empreinte attendue fausse, marqueur restant, mondes W1 et W2 sous la (ii), plafond 400 ou texte, GO v3, mode essai, deux fournisseurs, empreinte différente dans le bloc, fichier absent du bloc, `go_machine` = appels, `go_machine` ≠ ligne vérifiée, nom v5 sous préfixe v4, compagnon absent/faux, empreinte attendue mal formée |
| fichiers gelés sur le clone | 1 | 11 égaux | nul v9 modifié ; code d'attaque v4 absent |
| corps de création | 1 | 14 variables, `GO_ID` appels, `GO_MACHINE`, étiquette, aucune clé interdite | `go_machine` = appels ou mal formé, nom du texte v3, secret absent, échéance, chemin de configuration absolu |
| script de démarrage, minuterie | 1 | noms `a1v4`, amorce v5, étiquette dans la minuterie, bornes | hash court refusé |
| location (`louer`) | 32 | cas sain : 1 appel, état (`plafond_machine_usd` 35, variante ii, texte, mondes), deux calculs de garde, `CLE_ARGON=` dans les arguments de `vastai` et jamais `GEMINI_API_KEY_2`, aucun secret dans journal ni état ; « no_such_ask » puis contrat | **`GO_ID_MACHINE` absent / mal formé / ≠ `GO_ID` / = appels / périmètre d'une course / absent du registre** ; ligne machine **décision / échue / 1 USD** ; ligne des appels **199 / absente** ; **clé absente par son nom** ; autre clé `GEMINI_API_KEY` ; jeton absent ; empreinte du texte fausse ; volume ; offre pas la moins chère ; commit mal formé ; **variante inconnue** ; compagnon de configuration absent ; mondes du texte ≠ configuration ; marqueur ; nom brouillon ; `go_machine` du texte ≠ ligne ; **fichier gelé modifié** ; seconde location ; création incertaine |
| `--verifier-seulement` | 1 | 0 appel, « rien créé », deux calculs (4,4779 USD ≤ 35), aucun identifiant ni état écrits | — |
| masquage de la sortie | 1 | sortie standard + journal après un refus de Vast qui recopie les trois secrets : aucun n'y figure | — |
| contrôle et facturation par identifiant | 8 | absente → 0 ; avant borne → 5 ; vie → 5 ; sans vie à T0 + 30 → 1 et `detruire 4242` ; après échéance → 7 ; facturation filtrée | étiquette `a1-v3-troisieme-v1` → 2 sans geste ; protégée → 2 ; destruction non suivie → 3 ; étiquette autre à la facturation → 2 |
| fichier seul (`python -I -B`, import de repli) | 1 | `offre` → 21 ; `verifier-texte` → JSON, 11 égaux, rien écrit | `inventaire` sans `VAST_API_KEY` → « REFUS » sans trace ; `verifier-texte` empreinte fausse → 2 |
| amorce | 14 | jusqu'à l'`exec` du module v5, versions au journal, aucun secret | `CLE_ARGON`, `NOM_TEXTE`, `SHA_CONFIGURATION_MONDES` absentes ; GO appels v3 ; `GO_MACHINE` = appels ou « 35 » ; nom brouillon ou autre dossier ; `GEMINI_API_KEY_2`, `KIMI_API_KEY` présentes ; échéance texte ; mémoire < 2 Go ; module v5 absent |
| machine (hôte, monde jouet) | 21 | **cas sain** : deux GO acceptés (35 lu, 200 exact), garde recomputée (16,28 ≤ 35), configuration (ii) lue au commit privé, signe de vie poussé, 4 pièces privées + 11 fichiers publics égaux, texte v4-v1 = compagnon = `SHA_TEXTE`, `--verifier-seulement` 0, course lancée par le lanceur gelé v4 factice, versement « partie de main » sur `donnees/attaque-goodhart-v4-a1v4-v1`, liste d'empreintes juste, journaux `a1-v4`, aucun secret, destruction par l'identifiant 90000001 ; commande de la course vérifiée (lanceur v4, `prereg/…-v4-v1.md`, `--go GO-2026-11-02-22`, sortie sous `/…/a1-v4-reprise-v9-v1/`) ; reprise du conteneur : rien relancé, branche `…-interrompue-v1` | **nul v9 modifié après le scellement**, ligne machine décision / 1 USD, appels 199, `GO_MACHINE` = dose-réponse (périmètre) / = appels, `GO_ID` v3, empreinte de configuration ≠ pilote, `SHA_TEXTE` faux, nom v3, texte v2 introuvable, `CHEMIN_CONFIGURATION_MONDES` absente, `GEMINI_API_KEY_2` sur la machine, échéance trop proche, **variante inconnue**, mondes W1 et W2, `go_machine` du texte = GO-2026-11-05-03 → chacun : « REFUS … », aucune course lancée, branche de refus versée sans secret, machine détruite ; étiquette `a1-v3-troisieme-v1` → code 4, **aucun geste** |

Total : 138 (`essais-lanceur-durable-v5-v1.txt`). Les essais existants (`tests/test_hote_durable_a1_v3*.py`) n'ont pas été touchés ni rejoués
(aucun fichier existant modifié).

## 4. Ce que le lanceur attend du texte (brouillon 3 → texte scellé `…-v4-v<N>.md`)

Lu par `verifier_texte` chez le pilote (`louer`, `verifier-texte`) et sur la machine ; tout écart = arrêt explicite, rien ne part.

1. **Nom et place** : `orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v<N>.md` (N ≥ 1 ; préfixe `prefixe_texte` de la configuration,
   `preenregistrement-attaque-goodhart-v4-v` en v1). Si le code d'attaque v5 exige `…-v5-v<N>.md` (brouillon 3, annexe B, point 6), la
   configuration (ii) v2 portera `"prefixe_texte": "preenregistrement-attaque-goodhart-v5-v"` : rien à changer au lanceur.
2. **Compagnon** `<nom>.sha256` dont le premier mot égale l'empreinte du fichier, elle-même égale à `--sha-texte` (lue au scellement) et à
   `SHA_TEXTE` sur la machine.
3. **Aucun marqueur** au motif `<<[A-Z0-9_]+>>` : les cinq du brouillon 3 (`<<COMMIT_LANCEUR_DURABLE_V5>>`, `<<COMMIT_CODE_V5>>`,
   `<<EMPREINTES_AU_COMMIT>>`, `<<CASE_CONFIGURATION>>`, `<<DOSE_LAMBDA>>`) doivent être levés avant le scellement.
4. **Bloc `plan-gele`** entre `<!-- plan-gele : début -->` et `<!-- plan-gele : fin -->` (une fois chacun), lignes `clé: valeur` :
   - `mode: course` ; `fournisseurs: argon` ; `go: GO-2026-11-02-22` ; `plafond_usd: 200` (exactement) ;
   - **`mondes: W2 et W2g`** (variante (ii), valeur exacte de `mondes_texte` de la configuration ; `W1 et W2` pour la (i)) ; le brouillon 3
     l'écrit déjà ainsi (ligne 154) ;
   - `go_machine: GO-2026-11-08-12` (facultative ; si présente, égale à `GO_ID_MACHINE` du pilote et à `GO_MACHINE` de la machine, et
     différente de la ligne des appels) ; le brouillon 3 la porte (ligne 164) ;
   - les autres lignes (`grille`, `juge_ancien`, `dose_w2g`, `rejeux_*`, …) ne sont pas lues par le lanceur durable : le lanceur gelé les juge.
5. **Bloc `empreintes-du-code`** entre `<!-- empreintes-du-code : début -->` et `<!-- empreintes-du-code : fin -->`, lignes `<sha256>  <chemin>` :
   il doit contenir **chaque** fichier de `fichiers_geles_publics` de la configuration à la **même** empreinte (11 en v1 : `pole/attaque_goodhart_v4.py`
   `0077a647…`, `pole/nul_v9.py` `7ae450df…`, `pole/nul_v8.py` `cc452aaf…`, `demonstrations/attaque_goodhart_v4.py` `6357c0f5…`,
   `demonstrations/banc_tricheurs_v9.py` `7e4bff59…`, `…v8.py` `0be47e4b…`, `…v7.py` `ef016d25…`, `pole/attaque_goodhart_v2.py` `3c9de8b8…`,
   `pole/attaque_goodhart_v3.py` `cb9cffe7…`, `demonstrations/attaque_goodhart_v2.py` `58609e0c…`, `demonstrations/attaque_goodhart_v3.py`
   `87d52ace…`) ; le bloc peut en porter davantage (les 77 de `FICHIERS_GELES`). Ces fichiers doivent être, sur le clone public au
   `COMMIT_PUBLIC`, à ces mêmes empreintes.
6. **Hors du texte, passé au lanceur** : `COMMIT_PUBLIC` (commit du texte scellé, descendant de `commit_code_gele` de la configuration),
   `COMMIT_PRIVE` (commit de `main` qui porte le lanceur v5, l'amorce **et la configuration avec son compagnon**), `COMMIT_REGISTRE`
   (commit de `canal/conv-audit-n04` au registre sans doublon portant GO-2026-11-02-22), `--configuration-mondes` (chemin local ; relatif au
   dépôt privé pour la machine), environnement `GO_ID=GO_ID_MACHINE=GO-2026-11-08-12`, `GEMINI_API_KEY_2`, `GH_TOKEN` ou `CONTROLE_IA_GITHUB_TOKEN_2`,
   `VAST_API_KEY`.

Exemple de vérification sans création (mère, après scellement), depuis la racine du dépôt privé :
```
GO_ID=GO-2026-11-08-12 GO_ID_MACHINE=GO-2026-11-08-12 PYTHONPATH=src python -I -B src/controle_ia/hote_durable_a1_v4_v5.py verifier-texte \
  --texte /home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v1.md --sha-texte <empreinte> \
  --configuration-mondes docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v1.json
```
puis `louer … --verifier-seulement` avec les mêmes arguments plus `--registre-main registres/go.md --garde-main .claude/hooks/garde_calcul.py
--offres <réponse brute> --offre <id> --commit-prive … --commit-public … --commit-registre … --journal-local <journal neuf>` : tout vérifié,
garde de dépense calculée deux fois, rien créé.

## 5. Ce qui reste à la mère

1. **Compagnons `.sha256`** des deux configurations (le lanceur les exige), du module, de l'amorce, des essais, du différentiel, du relevé
   d'essais et de ce rapport (`python -m controle_ia.scellement sceller …`).
2. **Copies de code** : module → `src/controle_ia/hote_durable_a1_v4_v5.py`, amorce → `scripts/amorce_hote_durable_a1_v4_v5.sh`, essais →
   `tests/test_lanceur_durable_v5_a1v4.py` (adapter `ICI` au chemin du module, ou charger `controle_ia.hote_durable_a1_v4_v5`) ; rejeu
   des 138 essais ; les originaux restent ici (R12). Le script de démarrage attend l'amorce à `scripts/…v5.sh` et l'amorce attend les
   cinq modules sous `src/controle_ia/` du commit cloné.
3. **Contre-lecture** du lanceur v5 par un lecteur neuf (R2 ; le brouillon 3, section 13, point 6, la prévoit avec le code v5), puis **commit
   sur `main`** → `<<COMMIT_LANCEUR_DURABLE_V5>>`.
4. **Configuration (ii) v2** quand le code d'attaque v5 (monde W2g) est commité : `fichiers_geles_publics` recalculés (fichiers v5 ajoutés,
   `sha256sum` sur le clone), `commit_code_gele` = `<<COMMIT_CODE_V5>>`, `lanceur_gele` = `demonstrations/attaque_goodhart_v5.py`,
   `dossier_sortie` = `sortie-attaque-goodhart-v5`, `etape_depense` = `attaque_goodhart_v5/argon`, `prefixe_texte` selon le nom que le
   lanceur gelé v5 exige ; compagnon ; commit avant la location (la machine la lit à `COMMIT_PRIVE`). Jusque-là la (ii) v1 refuse de fait
   la course (le lanceur gelé v4 ne connaît pas W2g) : c'est voulu.
5. **Alignements du texte** (couples du brouillon 3) ou mot de la mère : étiquette (`a1-v4-v9` ici, `a1-v4-reprise-v9-v1` au brouillon 3,
   section 8) ; nom du fichier d'essais ; le brouillon 3 dit « `GO_MACHINE` … 35 USD (égalité exacte) » : le lanceur lit le plafond sur la
   ligne (35 sur GO-2026-11-08-12) et le périmètre ; `EMPREINTES-sortie-a1-v4-v1.txt`, branches, dossier `/root/a1-v4-reprise-v9-v1`,
   `mondes: W2 et W2g`, `go_machine:` : déjà égaux.
6. **Ordre de course v1** (dérivé de l'ordre v3) : exporter `GO_ID` et `GO_ID_MACHINE` à `GO-2026-11-08-12` (identifiant exact fixé par
   l'ordre), `GEMINI_API_KEY_2` par son nom, le jeton par son nom ; `verifier-texte` puis `louer --verifier-seulement` puis `louer` ; contrôles
   à T0 + 40 min et après l'échéance (`controler`) ; ligne pour `registres/etat.md` écrite par `louer`.
7. **Registre et empreintes au commit** : `<<EMPREINTES_AU_COMMIT>>` (77 + fichiers v5), `<<CASE_CONFIGURATION>>` (`e5306c47…` si la
   configuration d'Argon reste celle des quatre courses : les quatre pièces privées de la v4 sont reprises telles quelles par la v5, clé
   `pieces_privees` facultative pour en changer), `<<DOSE_LAMBDA>>`.

## 6. Réserves et limites déclarées

- Le périmètre est lu par deux mots (« machine », « a1-v4 », minuscules) : garde de forme contre une confusion de ligne, non une lecture du
  sens ; l'ordre fixe l'identifiant exact. Une ligne de course qui contiendrait ces deux mots passerait cette garde (aucune telle ligne au
  registre de `main` le 8 novembre à 17:00 UTC).
- Le monde jouet des essais ne joue pas le lanceur gelé v4 réel (lanceur factice de la v1) : la fermeture `--verifier-seulement` sur le vrai
  texte scellé reste l'épreuve de la mère (section 4, exemple), comme pour la v4 (épreuve texte v4 lanceur gelé).
- Les journaux du relais et de la course gardent les réglages de la v1 (`PLAFOND_RELAIS_USD` 410, 9 000 appels) ; le brouillon 3 les admet
  (« ≥ 200 USD et ≥ 8 000 appels »).
- Le lanceur ne lit pas la ligne `dose_w2g` ni `juge_ancien` : le lanceur gelé v5 en est le juge.
- Aucun `.sha256` écrit ici ; les empreintes de la section 1 sont celles de 17:01 UTC et deviennent fausses si un fichier est retouché.
