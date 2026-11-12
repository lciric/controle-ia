# LISEZMOI — commandes externes v5 de Kimi et d'Argon pour le tour fermé, étage 1 (code 4 réservé au plafond de session)

Rédigé le 3 novembre 2026, de 06:17 à 07:34 UTC (heures de `date -u`), par un sous-agent développeur de session-depot.
**Rien n'est scellé, rien n'est commis, rien n'a été lancé de payant ; aucun réseau hors de la boucle locale, aucun modèle,
aucune clé ni variable de clé, aucun fichier `.sha256` créé, aucun fichier existant modifié, rien sous `donnees/`, aucun
`git fetch` ; ports 8802 à 8807 jamais utilisés (ports éphémères seulement).** Arbre `wt-commandes-tf` (branche
`outils/commandes-tour-ferme-v1`, tête `9538620b`), dossier `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`.
Fichiers neufs seulement (R12) : les v4 et les v3, leurs essais, leurs bancs, leurs diffs, les LISEZMOI v1 et v2, les
empreintes v1 et v2 et `registre_depense_cumulee_v1.py` sont inchangés (`sha256sum -c EMPREINTES-commandes-tour-ferme-v2.txt`
et `…-v1.txt` : 7 et 8 OK après le travail).

## But

Demande du directeur (conv-audit, n° 393, § 4), appliquée telle quelle, après la contre-lecture courte du préenregistrement du
tour fermé, brouillon 6 (dépôt public `ideation-organism`, commit `d54b85c`,
`orchestrator/prereg/contre-lecture-courte-preenregistrement-tour-ferme-v6.md`, section 1) :

- **B11** : le code 4 « rien envoyé », que l'adaptateur v64 lit « budget_depasse » (fin des tours de la carte), est **réservé
  au refus que la session porte en elle-même** — `cause_refus = plafond_session`. **Tout autre refus** (`garde_etape`,
  `garde_cumulee`, `registre_illisible`, `relais_plafond`, `relais_max_appels`, et les 402 et 429 du relais ou du fournisseur
  transmis par le relais) **sort en code 3 au plancher, rien parti** (`envoye: false`, coût 1e-6), que la v64 lit « erreur » :
  arrêt de la course. Sans cette règle, une limite du relais ou de la commande viderait chaque carte suivante (« non
  concluant ») au lieu d'arrêter, et la lecture gelée rendrait une issue fausse (course à blanc L2b-cl6 de la contre-lecture).
- **I33** : la dernière ligne d'un code 4 ne porte ni `modele_servi` (sauf exactement le modèle demandé), ni `refus`, ni
  `stop_reason`. Vérifié dans `pole/adaptateurs.py` (gelé, `a1a8ede8…`, l. 680-700 et 750-760) : sur un code non nul, la classe
  gelée `AdaptateurCommandeExterne.lancer` appelle `controle_modele(objet, modele, seulement_si_dit=True)` dès que la ligne est
  conforme (texte, coût fini > 0 : le plancher l'est) ; un `refus` vrai, un `stop_reason` « refusal », ou une clé `modele_servi`
  nulle, vide ou différente du modèle demandé y donnent un refus R-764, **statut « refus »**, avant que la v64 ne voie le code ;
  or `AdaptateurCommandeExterneV64.lancer` (`pole/adaptateur_commande_v64.py` l. 119-129) ne change en « budget_depasse » que
  le statut « erreur » (l. 123) : la session serait lue « refus » → arrêt. Rejoué (essai `test_v64_lecture_d_une_ligne_sain_et_artefacts`).
- `cause_refus` reste sur la ligne, code 4 comme code 3, pour le registre et l'audit.

## Fichiers neufs du dossier

| fichier | sha256 | rôle |
|---|---|---|
| `commande_kimi_v5.py` | `5d9d662000e7b577…` | commande externe de Kimi (relais local 8804) : v4 + trois changements |
| `commande_argon_v56_nuit_v5.py` | `0b52aba8c4cfff95…` | commande externe d'Argon, sous-commande `appeler` (relais local 8805) : v4 + trois changements ; `servir` identique |
| `test_commandes_tour_ferme_v5.py` | `511852568754c113…` | 136 essais `pytest` (47 fonctions ; la suite v4 aux codes de la v5, plus la règle, I33, la signature, la lecture par la v64) |
| `mutations_commandes_tour_ferme_v5.py` | `ed0eb278a79884c3…` | banc de 91 mutations (64 du banc v4 et 6 de la contre-lecture v4, transposées ; X6b et 20 neuves sur la règle) |
| `diff-kimi-v4-v5.patch` | `047080d9404d799f…` | `diff -u` v4 → v5 de Kimi (111 lignes, 63 lignes `+`/`−`) |
| `diff-argon-v4-v5.patch` | `baea1e1a9820daae…` | `diff -u` v4 → v5 d'Argon (116 lignes, 66 lignes `+`/`−`) |
| `LISEZMOI-commandes-tour-ferme-v3.md` | (voir les empreintes) | ce fichier |
| `EMPREINTES-commandes-tour-ferme-v3.txt` | — | `sha256sum` de chacun des fichiers neufs ci-dessus (elle-même exclue) |

Empreintes entières : `EMPREINTES-commandes-tour-ferme-v3.txt` (`sha256sum -c` dans le dossier). Le registre partagé reste
`registre_depense_cumulee_v1.py`, sha256 `8ba92066b358ffb8…` (identique, contrôlé par un essai).

**v4 + diff = v5, vérifié** : copies des v4 (`10afdab5…`, `5c6d5149…`) dans un dossier vide, `patch -p0 < diff-…-v4-v5.patch`,
puis `cmp` avec les v5 : **égal** pour Kimi et pour Argon ; de même avec `patch -o SORTIE FICHIER_V4 diff` (cible explicite).
Les deux v5 ont été fabriquées depuis les v4 par **remplacements exacts** (chaque motif présent une fois exactement, sinon
arrêt ; script de travail hors du dépôt :
`/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/scripts/fabriquer_v5_v1.py`) :
9 remplacements chez Kimi, 8 chez Argon.

## Différences v4 → v5

Le détail, numéroté, est en tête de chaque fichier (historiques v4, v3, v2 gardés en dessous).

**Kimi (`commande_kimi_v5.py`, `VERSION = "commande-kimi-v5"`)**

1. **Code 4 réservé à `plafond_session` (B11)** : les refus du registre (`garde_etape`, `garde_cumulee`, `registre_illisible`)
   passent de `rendre(4, …)` à `rendre(3, …)`, même ligne sinon (`envoye: false`, plancher, `cause_refus`, diagnostic) ; un 402
   ou un 429 **signé par le relais Kimi** (`relais` = `relais-kimi-…`, corps lu en entier) n'est plus rendu en code 4 : il garde
   le code 3 du bloc des erreurs HTTP, au plancher, `envoye: false`, et reçoit `cause_refus` (`relais_plafond`,
   `relais_max_appels`) ; un 402 ou un 429 **de Moonshot transmis** par le relais (sans la signature) sort, comme en v4, en code 3
   au plancher, `envoye: false`, sans cause (une cause du relais y serait fausse). La signature ne décide donc plus que la cause.
   Les deux contrôles du plafond de session, seules sorties en code 4, sont inchangés.
2. **I33** : rien à retirer (les deux lignes de code 4 ne portaient déjà que `texte`, `cout_usd`, `version`, `erreur`, `envoye`,
   `role`, `cause_refus`) ; la règle est écrite en tête et contrôlée par les essais sur toute ligne de code 4, et par une lecture
   statique du source.
3. **Version, en-tête, ligne d'usage.** Rien d'autre ne change : clé d'étape propre au fournisseur, bornes de sortie par rôle,
   signature des refus propres du relais, gardes, pire cas, registre, protocole.

**Argon (`commande_argon_v56_nuit_v5.py`, `VERSION = "commande-argon-v56-nuit-v5"`, sous-commande `appeler`)**

1. **Code 4 réservé à `plafond_session` (B11)** : refus du registre en code 3 (comme chez Kimi) ; tout 402 ou 429 de son relais
   (le relais Argon ne transmet jamais un statut de l'interface : une erreur de Gemini lui revient en réponse 200 portant
   `echec`, code 3 de la commande, inchangé) passe de `fin(4 if e.code in (402, 429) else 3, …)` à `fin(3, …)`, au plancher,
   `envoye: false`, `cause_refus` gardée.
2. **I33** : comme chez Kimi (rien à retirer ; écrit et contrôlé).
3. **Version, en-tête, lignes d'usage.** Rien d'autre ne change (dont la ligne JSON sur un refus d'argparse).

**Sous-commande `servir` d'Argon : identique à la v4 octet pour octet hors la constante `VERSION`** (vérifié par programme et
par l'essai `test_bloc_servir_identique_a_la_v4`) : le bloc compris entre la ligne-marqueur du relais (comprise) et celle de la
commande (exclue) fait 8 573 octets, identique en v3, v4 et v5 (donc en v2) ; entre les imports et ce bloc, la seule ligne qui
change est `VERSION` ; la fonction `principal` et la fin du fichier sont identiques à la v4 octet pour octet ; les fonctions et
constantes que lit `servir` ont le même source ou la même valeur ; un refus d'argparse pour `servir` donne en v3, v4 et v5 le
même code (2), la même sortie standard (vide) et la même sortie d'erreur. Seuls changent, par `VERSION`, le champ `version` de
`GET /relais/etat` et l'en-tête `Server` (et la première ligne de l'en-tête, description d'argparse jamais affichée). Le relais
8805 est un instrument gelé d'A1-v3, servi depuis `commande_argon_v56_nuit_v2.py` : la v5 ne sert qu'en `appeler`.

**Fenêtre d'entrée du modèle : aucune des deux commandes ne la contrôle** (ni en v4 ni en v5 : seul le pire cas en dollars est
jugé avant envoi ; les relais bornent seulement la taille du corps, 413, code 3) ; conformément à la demande, ce contrôle n'est
pas ajouté. Une consigne au-delà de la fenêtre partirait, et l'erreur de l'interface reviendrait en code 3 ou 5 : « erreur »,
arrêt (réserve 2).

## Cause → code → lecture par la v64

Lecture par `AdaptateurCommandeExterneV64` (copie de `ideation-organism` à `eaa74ca` ; `adaptateur_commande_v64.py`
`adb73287…`, `adaptateurs.py` `a1a8ede8…`, `adaptateurs_v56.py` `d36c79b2…`, identiques à `63ed933`), **rejouée** sur la dernière
ligne réelle de chaque commande v5 lancée avec la commande de la configuration ci-dessous (faux relais local, porte
« environnement » réelle, `ETAPE_POLE=tour_ferme_v64`, part 44.00 ou 6.00, modèle servi exigé) : essai
`test_lecture_v64_des_six_causes` (12 cas). Effet dans l'étage : selon la demande (n° 393) et la table de la contre-lecture v4
(section 5), non rejoué ici.

| `cause_refus` | quand | code v5 (v4) | dernière ligne | lecture par la v64 | effet dans l'étage |
|---|---|---|---|---|---|
| `plafond_session` | le pire cas de l'appel, à la sortie minimale du rôle, passe `PLAFOND_SESSION_USD` (deux contrôles) | **4** (4) | `envoye: false`, 1e-6, `cause_refus` ; ni `modele_servi`, ni `refus`, ni `stop_reason` | « budget_depasse », coût compté 0, `rien_envoye` | fin des tours de la carte (expérimentateur) ; témoin « non concluant » (vérificateur) ; arrêt pour un proposeur (A.5) |
| `garde_etape` | réglé + engagé du fournisseur sous `ETAPE_POLE/<fournisseur>` + pire cas > `PLAFOND_ETAPE_USD` | **3** (4) | `envoye: false`, 1e-6, `cause_refus`, diagnostic | « erreur », coût 1e-6 compté | arrêt de la course |
| `garde_cumulee` | réglé + engagé des deux fournisseurs + pire cas > `--plafond-cumule-usd` ; ou ses deux contrôles d'entrée | **3** (4) | idem | « erreur » | arrêt |
| `registre_illisible` | ligne illisible, dossier absent, fichier ou verrou illisible | **3** (4) | idem | « erreur » | arrêt |
| `relais_plafond` | 402 du relais lui-même (Kimi : signé `relais-kimi-…` ; Argon : tout 402) | **3** (4) | `envoye: false`, 1e-6, `cout_origine: plancher`, `cause_refus` ; registre : `debut` puis `fin` code 3 à 1e-6 | « erreur » | arrêt |
| `relais_max_appels` | 429 du relais lui-même (idem) | **3** (4) | idem | « erreur » | arrêt |
| (aucune) | Kimi : 402 ou 429 de Moonshot transmis par le relais (sans signature) | 3 (3) | `envoye: false`, 1e-6, sans cause | « erreur » | arrêt |

`cause_refus` est présente sur les six causes et sur elles seules (absente des codes 0, 2, 5, 6 et des autres codes 3 : relais
absent, 400, 403, 411, 413, échec de l'interface). Codes inchangés hors de cette table : 0 conforme ; 2 réglage, entrée ou option
refusés ; 5 réponse non conforme (dont modèle servi différent, `modele_servi` rendu, lu « refus » R-764) ; 6 délai dépassé ou
interruption (coût = pire cas réservé).

## Commandes exactes pour la configuration du tour fermé

Chemins absolus **chez la fille** ; interpréteur **`/usr/bin/python3`** (`-I -B`, comme en production) ; mêmes options que la v4
(LISEZMOI v2), toutes écrites même à leur défaut pour que l'empreinte de la configuration les gèle. `{REGISTRE}` et l'argument
qui suit `--plafond-cumule-usd` sont substitués par le lanceur (`<SORTIE absolue>/registre-depense-cumulee-v1.jsonl` et `50`).
`--modele` doit être égal à `proposeurs[fournisseur].modele` (sinon `MODELE_DEMANDE_POLE` ≠ `--modele` → code 2 avant tout envoi).
Ces deux listes sont celles que la suite joue (constante `CONFIGURATION` de `test_commandes_tour_ferme_v5.py`, avec l'adresse
du faux relais et le registre de l'essai substitués) ; égalité vérifiée par programme à la livraison.

`fournisseurs.kimi.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v5.py",
 "--url-relais", "http://127.0.0.1:8804", "--modele", "kimi-k3.1-pro",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "65536", "--max-sortie-court", "16000", "--sortie-min-jetons", "4096",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

`fournisseurs.argon.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v5.py",
 "appeler", "--url-relais", "http://127.0.0.1:8805", "--modele", "gemini-4-argon",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000", "--sortie-min-jetons", "1000",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

Avec, pour chacun, comme en v4 : `"type": "commande_externe"` et `"porte_plafond": {"type": "environnement"}` (la porte passe
`ETAPE_POLE=tour_ferme_v64` et `PLAFOND_ETAPE_USD` = la part, `44.00` ou `6.00` ; la commande juge la part sous
`tour_ferme_v64/kimi` ou `tour_ferme_v64/argon`). Clé exigée par la v64 (`bareme_depuis_configuration`, aucun défaut ; mineur 2
de la contre-lecture v4) : `fournisseurs.kimi.prix_entree_usd_par_million_jetons = 2` (`--prix-entree` de Kimi) et
`fournisseurs.argon.prix_entree_usd_par_million_jetons = 10` (`PRIX[0]` d'Argon). Le manifeste porte l'empreinte de chaque
argument qui est un fichier (`description()` de l'adaptateur) : `/usr/bin/python3` (lien vers `/usr/bin/python3.13`, sha256
`dc9c6efba6e3583b…` ici, 3.13.18) et la commande (`EMPREINTES-commandes-tour-ferme-v3.txt`) ; le registre, importé depuis le
dossier des commandes, n'est pas un argument (empreinte `8ba92066…`, `EMPREINTES-commandes-tour-ferme-v1.txt`).

## Essais (commandes et comptes exacts)

La lecture par la v64 exige une copie du dépôt public au commit lu, sur `PYTHONPATH` (dossier `orchestrator`) ; sans elle, ou
avec un module d'empreinte différente, les 25 essais qui la lisent **échouent** (vérifié : 25 erreurs, aucun saut).

```
mkdir COPIE && git -C /home/user/ideation-organism archive eaa74ca orchestrator/pole | tar -x -C COPIE
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v5.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator PY_COMMANDES=/usr/bin/python3 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v5.py
```

(`COPIE` en chemin absolu. Ici : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/ideation-eaa74ca`,
123 fichiers de `orchestrator/pole`.)

Résultats du 3 novembre 2026 dans l'arbre de session-depot (Python 3.13.18, pytest 9.1.1) : **commandes sous l'interpréteur du
dépôt : 136 passés, 0 échoué, 77,8 s** (06:38:02 à 06:39:23 UTC) ; **commandes sous `/usr/bin/python3 -I -B` : 136 passés,
0 échoué, 94,8 s** (06:39:55 à 06:41:30) ; **v4 sur les v4, inchangée : 87 passés, 0 échoué, 52,6 s** (07:33:06 à
07:33:59). Faux relais : `ThreadingHTTPServer(("127.0.0.1", 0))`, une requête par connexion, connexion fermée après la
réponse, lecture bornée à 30 s, relais lent toujours libéré en fin d'essai ; aucune connexion sortante ; processus lancés par
les essais arrêtés par leur PID.

Ce que la suite v5 couvre, pour chacune des deux commandes sauf mention :

- **tout ce que couvrait la v4, aux codes de la v5** : rôles permis et inconnus, `MODELE_DEMANDE_POLE`, `PLAFOND_SESSION_USD`
  invalides, porte « environnement » incomplète, consigne vide, options obligatoires absentes et refus d'argparse (ligne JSON),
  `servir` refusé par argparse à l'identique (v3, v4, v5), adresse hors boucle locale, sorties maximale et minimale par rôle et
  leurs défauts, vérificateur à 0,10 USD, second contrôle du plafond de session, reste de la borne de l'expérimentateur
  (`plafond_session` : **code 4**) ; registre plein, plafond cumulé invalide, registre illisible, dossier absent, dossier à la
  place du fichier, garde d'étape (**code 3**) ; chaque message du registre gelé et sa cause ; B1 (deux fournisseurs, même
  registre, même `ETAPE_POLE`, parts différentes ; idempotence ; garde cumulée commune, refus en **code 3**) ; 402 et 429 du
  relais (**code 3**, cause, `fin` au registre en code 3) ; 502 « modèle servi différent » de Kimi (code 5) ; modèle servi
  différent (code 5) ; coût d'un échec d'Argon au pire cas réservé ; délai dépassé et signaux (code 6) ; `/usr/bin/python3` ;
  aucune clé lue ni transmise ; vrai gestionnaire de `servir` (402 et 429 lus en **code 3** par `appeler`, 411, 413,
  `/relais/etat` à la `VERSION` v5, journal sans texte, refus sans clé et sans collisionneur conforme) ;
- **la règle de la v5 sur toute sortie** (`invariants_v5`, appelée à chaque lancement d'une commande v5) : code 4 ⇒ `envoye` le
  booléen faux, cause `plafond_session`, ni `refus`, ni `stop_reason`, ni `modele_servi` sauf exactement le modèle demandé ;
  toute `cause_refus` ⇒ son code (4 ou 3), `envoye: false`, plancher, texte vide ;
- **les six causes** dans la configuration du tour (rôle joué : Kimi expérimentateur à 0,80, Argon vérificateur à 0,10 ; part
  sous `ETAPE_POLE`) : code attendu, `envoye: false`, coût 1e-6, cause juste, sortie d'erreur vide, rien reçu ni réservé pour les
  quatre refus d'avant l'envoi, `debut` puis `fin` en code 3 pour les deux refus du relais (`test_six_causes_code_ligne_et_registre`) ;
- **Kimi, signature** (mineur 4 de la contre-lecture v4, X1 à X3) : forme réelle du refus du relais (`{"erreur", "relais",
  **compteur.etat()}`, 492 et 552 octets), signature exacte d'une autre version (`relais-kimi-v4`), signature après le 300e
  octet → code 3 **avec** la cause ; 429 et 402 de Moonshot (forme `exceeded_current_quota_error`), corps illisible, marque
  relâchée (`relais-argon-v2`, `moonshot`, vide, casse différente, non textuelle, dans une liste), corps qui n'est pas un objet →
  code 3 **sans** cause ;
- **chaque rôle sous `ETAPE_POLE`**, proposeur compris (X6) : clé `tour_ferme_v64/<fournisseur>` à la dernière ligne et à la
  ligne `debut` ;
- **la lecture par la v64** : les six causes (ci-dessus) ; **témoin v4** (R5) : la même préparation avec les commandes v4 →
  code 4 lu « budget_depasse » pour `garde_etape` et `relais_max_appels` (B11 reproduit) ; **contrat de I33** sur une ligne
  rejouée : ligne de code 4 de la v5 → « budget_depasse » ; avec `modele_servi` égal au modèle demandé → « budget_depasse » ; avec
  `modele_servi` nul, vide ou autre, `refus` vrai, `stop_reason` « refusal » → « refus » ; `envoye` en texte, ou code 3 →
  « erreur » ;
- **lecture statique** (module `ast`) : la constante 4 n'est un code de sortie qu'aux deux `rendre(4, …)` des contrôles du
  plafond de session (`cause_refus="plafond_session"`, sans `**`, sans `modele_servi`, `refus` ni `stop_reason`), et aucune valeur
  affectée à `code` ne vaut 4 ;
- l'identité du bloc `servir` et de `principal` avec la v4, l'empreinte du registre partagé.

Non couvert (comme en v4) : le dépassement de réserve (code 5, `depassement_reserve`), code inchangé depuis la v2 ; un relais
réel (8804, 8805) ; un modèle ; le lanceur v64 de bout en bout (seul l'adaptateur v64 et sa porte sont joués).

## Banc de mutations

```
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PYTHONPATH=COPIE/orchestrator nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v5.py
```

Le banc exige `PYTHONPATH` (sinon il s'arrête), vérifie d'abord que chaque motif est présent une fois exactement et que chaque
fichier muté se lit encore comme du Python (sinon il s'arrête : une faute de syntaxe n'est jamais comptée « tuée »), joue le
cas sain (dossier non muté) qui doit passer (R5), puis, pour chaque mutation, copie le dossier (les deux v5, les deux v4 pour le
témoin et l'identité, la v3 d'Argon, le registre, la suite), applique la mutation et joue la suite avec `-x` ; il relève le
premier essai qui échoue.

Résultat du 3 novembre 2026 (06:44:47 à 07:32:27 UTC, `date -u`) : **motifs vérifiés ; cas sain (dossier non muté) :
passe — 136 passed in 76.70s (77.0 s) ; 91 mutations tuées sur 91 jouées ; code 0** — banc lancé une seule fois, en
arrière-plan, 47 min 40 s en tout, aucune autre suite d'essais lancée pendant ce temps, aucun processus restant ensuite
(vérifié par `ps`). Les 27 mutations propres à la v5 et à la contre-lecture v4 (X1 à X6, X6b, R1 à R20) sont toutes tuées par
des essais de comportement (la lecture statique, placée plus loin dans la suite, n'a eu à en tuer aucune). Sortie brute du banc
(hors du dépôt) : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v5/sorties/banc-v5.txt`.

| id | fichier | mutation | sort | suite | premier essai qui échoue | durée |
|---|---|---|---|---|---|---|
| K1 | `commande_kimi_v5.py` | rôle lecteur_test retiré de ROLES | tuée | 1 failed, 3 passed in 2.47s | `test_chaque_role_permis_accepte[kimi-lecteur_test]` | 2.8 s |
| K2 | `commande_kimi_v5.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 3 passed in 2.49s | `test_chaque_role_permis_accepte[kimi-lecteur_test]` | 2.8 s |
| K3 | `commande_kimi_v5.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 33 passed in 19.63s | `test_sortie_maximale_choisie_selon_le_role[kimi-lecteur_test-500]` | 20.0 s |
| K4 | `commande_kimi_v5.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 40 passed in 24.53s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.8 s |
| K5 | `commande_kimi_v5.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 40 passed in 24.07s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.4 s |
| K6 | `commande_kimi_v5.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 12 passed in 8.51s | `test_plafond_session_absent_ou_invalide_code_2[kimi]` | 8.8 s |
| K7 | `commande_kimi_v5.py` | version v4 rendue | tuée | 1 failed in 0.84s | `test_chaque_role_permis_accepte[kimi-proposeur_ideation]` | 1.2 s |
| K8 | `commande_kimi_v5.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 10 passed in 7.18s | `test_modele_demande_different_code_2[kimi]` | 7.5 s |
| K9 | `commande_kimi_v5.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 8 passed in 5.49s | `test_role_inconnu_refuse_code_2[kimi]` | 5.9 s |
| K10 | `commande_kimi_v5.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 14 passed in 10.45s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 10.7 s |
| K11 | `commande_kimi_v5.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 50 passed in 30.85s | `test_registre_cumule_plein_code_3[kimi]` | 31.2 s |
| A1 | `commande_argon_v56_nuit_v5.py` | rôle experimentateur_test retiré de ROLES | tuée | 1 failed, 6 passed in 4.32s | `test_chaque_role_permis_accepte[argon-experimentateur_test]` | 4.6 s |
| A2 | `commande_argon_v56_nuit_v5.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 37 passed in 22.67s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 23.0 s |
| A3 | `commande_argon_v56_nuit_v5.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 37 passed in 23.43s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 23.7 s |
| A4 | `commande_argon_v56_nuit_v5.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 41 passed in 26.77s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 27.1 s |
| A5 | `commande_argon_v56_nuit_v5.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 41 passed in 25.78s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.1 s |
| A6 | `commande_argon_v56_nuit_v5.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 13 passed in 9.49s | `test_plafond_session_absent_ou_invalide_code_2[argon]` | 9.8 s |
| A7 | `commande_argon_v56_nuit_v5.py` | version v4 rendue | tuée | 1 failed, 4 passed in 3.23s | `test_chaque_role_permis_accepte[argon-proposeur_ideation]` | 3.5 s |
| A8 | `commande_argon_v56_nuit_v5.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 11 passed in 7.74s | `test_modele_demande_different_code_2[argon]` | 8.0 s |
| A9 | `commande_argon_v56_nuit_v5.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 9 passed in 5.97s | `test_role_inconnu_refuse_code_2[argon]` | 6.2 s |
| A10 | `commande_argon_v56_nuit_v5.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 15 passed in 11.35s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.6 s |
| A11 | `commande_argon_v56_nuit_v5.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 51 passed in 32.11s | `test_registre_cumule_plein_code_3[argon]` | 32.5 s |
| A12 | `commande_argon_v56_nuit_v5.py` | le relais (servir) tolère un corps sans Content-Length (411 perdu) | tuée | 1 failed, 133 passed in 76.55s (0:01:16) | `test_bloc_servir_identique_a_la_v4` | 76.9 s |
| C1 | `commande_kimi_v5.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 33 passed in 20.82s | `test_sortie_maximale_choisie_selon_le_role[kimi-lecteur_test-500]` | 21.1 s |
| C2 | `commande_argon_v56_nuit_v5.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 37 passed in 23.92s | `test_sortie_maximale_choisie_selon_le_role[argon-lecteur_test-500]` | 24.3 s |
| C3 | `commande_kimi_v5.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 40 passed in 24.64s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 25.0 s |
| C4 | `commande_argon_v56_nuit_v5.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 41 passed in 25.89s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 26.2 s |
| C5 | `commande_argon_v56_nuit_v5.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 81 passed in 49.00s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 49.3 s |
| C6 | `commande_kimi_v5.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 75 passed in 45.72s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 46.0 s |
| C7 | `commande_kimi_v5.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 95 passed in 60.83s (0:01:00) | `test_delai_depasse_code_6_au_pire_cas[kimi]` | 61.1 s |
| C8 | `commande_kimi_v5.py` | gestionnaires de signaux retirés | tuée | 1 failed, 97 passed in 63.33s (0:01:03) | `test_signal_code_6_au_pire_cas[kimi-SIGTERM]` | 63.7 s |
| C9 | `commande_kimi_v5.py` | contrôle du modèle servi retiré | tuée | 1 failed, 92 passed in 58.61s | `test_modele_servi_different_code_5[kimi]` | 58.9 s |
| C10 | `commande_argon_v56_nuit_v5.py` | contrôle du modèle servi retiré | tuée | 1 failed, 93 passed in 60.27s (0:01:00) | `test_modele_servi_different_code_5[argon]` | 60.6 s |
| C11 | `commande_argon_v56_nuit_v5.py` | coût d'un échec pris au chiffre du relais, pas au pire cas réservé | tuée | 1 failed, 94 passed in 62.25s (0:01:02) | `test_argon_cout_d_un_echec_au_pire_cas_reserve` | 62.6 s |
| C12 | `commande_kimi_v5.py` | garde d'étape du registre débranchée (plafond_etape_usd=None) | tuée | 1 failed, 14 passed in 11.29s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 11.7 s |
| N1 | `commande_kimi_v5.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 14 passed in 12.48s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 12.8 s |
| N2 | `commande_argon_v56_nuit_v5.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 15 passed in 11.92s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 12.2 s |
| N3 | `commande_kimi_v5.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 14 passed in 11.53s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 11.8 s |
| N4 | `commande_argon_v56_nuit_v5.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 15 passed in 11.61s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.9 s |
| N5 | `commande_kimi_v5.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 60 passed in 36.70s | `test_b1_suffixe_idempotent[kimi]` | 37.1 s |
| N6 | `commande_argon_v56_nuit_v5.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 61 passed in 37.35s | `test_b1_suffixe_idempotent[argon]` | 37.7 s |
| N7 | `commande_kimi_v5.py` | champ etape de la dernière ligne = clé du registre (valeur reçue perdue) | tuée | 1 failed, 14 passed in 9.94s | `test_etape_sans_plafond_d_etape_code_2[kimi]` | 10.3 s |
| N8 | `commande_argon_v56_nuit_v5.py` | champ etape_registre absent de la dernière ligne | tuée | 1 failed, 4 passed in 3.15s | `test_chaque_role_permis_accepte[argon-proposeur_ideation]` | 3.5 s |
| N9 | `commande_kimi_v5.py` | cause : préfixe de la garde d'étape faux (garde d'étape lue garde cumulée) | tuée | 1 failed, 54 passed in 33.53s | `test_garde_d_etape_code_3[kimi]` | 33.8 s |
| N10 | `commande_argon_v56_nuit_v5.py` | cause : garde d'étape et garde cumulée permutées | tuée | 1 failed, 51 passed in 31.92s | `test_registre_cumule_plein_code_3[argon]` | 32.2 s |
| N11 | `commande_kimi_v5.py` | cause absente sur le premier contrôle du plafond de session | tuée | 1 failed, 40 passed in 24.47s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.8 s |
| N12 | `commande_argon_v56_nuit_v5.py` | cause absente sur le second contrôle du plafond de session | tuée | 1 failed, 47 passed in 29.48s | `test_plafond_session_second_controle_code_4[argon]` | 29.8 s |
| N13 | `commande_kimi_v5.py` | cause absente sur un refus du registre | tuée | 1 failed, 50 passed in 31.64s | `test_registre_cumule_plein_code_3[kimi]` | 32.0 s |
| N14 | `commande_argon_v56_nuit_v5.py` | cause : registre illisible lu garde cumulée | tuée | 1 failed, 53 passed in 32.79s | `test_registre_illisible_code_3[argon]` | 33.1 s |
| N15 | `commande_kimi_v5.py` | cause du refus signé du relais perdue (signature jamais lue ; code 3 sans cause, comme en v3) | tuée | 1 failed, 75 passed in 45.52s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 45.9 s |
| N16 | `commande_kimi_v5.py` | signature du relais ignorée (erreur de l'amont 402/429 avec la cause du relais) | tuée | 1 failed, 85 passed in 51.29s | `test_refus_du_relais_402_429_code_3[kimi-402-relais_plafond]` | 51.6 s |
| N17 | `commande_argon_v56_nuit_v5.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed in 34.85s | `test_cause_du_registre_sur_chaque_refus_du_registre_gele` | 35.2 s |
| N18 | `commande_kimi_v5.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed in 34.04s | `test_cause_du_registre_sur_chaque_refus_du_registre_gele` | 34.4 s |
| N19 | `commande_argon_v56_nuit_v5.py` | cause_refus sur tout refus HTTP du relais (403 compris) | tuée | 1 failed, 84 passed in 52.14s | `test_cause_refus_absente_hors_des_six_refus[argon]` | 52.5 s |
| N20 | `commande_argon_v56_nuit_v5.py` | dernière ligne JSON d'argparse retirée (comportement v3) | tuée | 1 failed, 19 passed in 14.20s | `test_arguments_obligatoires_absents_code_2[argon]` | 14.5 s |
| N21 | `commande_argon_v56_nuit_v5.py` | dernière ligne JSON d'argparse aussi pour servir (servir changé) | tuée | 1 failed, 27 passed in 18.95s | `test_servir_refus_d_argparse_inchange_depuis_la_v3` | 19.3 s |
| N22 | `commande_argon_v56_nuit_v5.py` | champ role absent de la ligne d'argparse | tuée | 1 failed, 19 passed in 13.59s | `test_arguments_obligatoires_absents_code_2[argon]` | 13.9 s |
| N23 | `commande_argon_v56_nuit_v5.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 96 passed in 64.92s (0:01:04) | `test_delai_depasse_code_6_au_pire_cas[argon]` | 65.3 s |
| N24 | `commande_argon_v56_nuit_v5.py` | gestionnaires de signaux retirés | tuée | 1 failed, 99 passed in 66.89s (0:01:06) | `test_signal_code_6_au_pire_cas[argon-SIGTERM]` | 67.3 s |
| N25 | `commande_kimi_v5.py` | cause fausse sur le second contrôle du plafond de session | tuée | 1 failed, 46 passed in 29.16s | `test_plafond_session_second_controle_code_4[kimi]` | 29.5 s |
| N26 | `commande_argon_v56_nuit_v5.py` | clé d'étape au nom de l'autre fournisseur | tuée | 1 failed, 15 passed in 11.10s | `test_etape_sans_plafond_d_etape_code_2[argon]` | 11.4 s |
| N27 | `commande_kimi_v5.py` | cause : refus du registre toujours garde d'étape | tuée | 1 failed, 50 passed in 31.33s | `test_registre_cumule_plein_code_3[kimi]` | 31.6 s |
| N28 | `commande_kimi_v5.py` | écart de modèle signalé par le relais (502) perdu : modele_servi non rendu | tuée | 1 failed, 91 passed in 57.92s | `test_kimi_ecart_de_modele_signale_par_le_relais_code_5` | 58.3 s |
| N29 | `commande_kimi_v5.py` | 502 du relais rendu en code 3 au lieu de 5 | tuée | 1 failed, 91 passed in 58.96s | `test_kimi_ecart_de_modele_signale_par_le_relais_code_5` | 59.3 s |
| X1 | `commande_kimi_v5.py` | signature du relais relâchée : toute chaîne `relais` vaut refus du relais | tuée | 1 failed, 89 passed in 56.27s | `test_kimi_signature_du_relais[402-relais_plafond]` | 56.6 s |
| X2 | `commande_kimi_v5.py` | signature du relais exacte « relais-kimi-v3 » (un relais v4 signé serait lu amont) | tuée | 1 failed, 89 passed in 55.77s | `test_kimi_signature_du_relais[402-relais_plafond]` | 56.1 s |
| X3 | `commande_kimi_v5.py` | corps d'erreur tronqué à 300 octets avant la lecture de la signature | tuée | 1 failed, 75 passed in 47.84s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 48.3 s |
| X4 | `commande_argon_v56_nuit_v5.py` | OSError du registre lue garde_cumulee (RegistreIllisible inchangé) | tuée | 1 failed, 53 passed in 35.15s | `test_registre_illisible_code_3[argon]` | 35.5 s |
| X5 | `commande_argon_v56_nuit_v5.py` | refus d'argparse rendu en code 4 (que la v64 lirait « budget_depasse ») | tuée | 1 failed, 19 passed in 14.02s | `test_arguments_obligatoires_absents_code_2[argon]` | 14.3 s |
| X6 | `commande_kimi_v5.py` | clé d'étape non suffixée pour le seul proposeur | tuée | 1 failed, 63 passed in 38.35s | `test_cle_d_etape_suffixee_pour_chaque_role[kimi-proposeur_ideation]` | 38.7 s |
| X6b | `commande_argon_v56_nuit_v5.py` | clé d'étape non suffixée pour le seul proposeur | tuée | 1 failed, 67 passed in 41.34s | `test_cle_d_etape_suffixee_pour_chaque_role[argon-proposeur_ideation]` | 41.6 s |
| R1 | `commande_kimi_v5.py` | refus du registre rendu en code 4 (comportement v4) | tuée | 1 failed, 50 passed in 31.21s | `test_registre_cumule_plein_code_3[kimi]` | 31.5 s |
| R2 | `commande_argon_v56_nuit_v5.py` | refus du registre rendu en code 4 (comportement v4) | tuée | 1 failed, 51 passed in 31.38s | `test_registre_cumule_plein_code_3[argon]` | 31.7 s |
| R3 | `commande_kimi_v5.py` | refus 402/429 signé du relais rendu en code 4 (comportement v4) | tuée | 1 failed, 75 passed in 45.05s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 45.3 s |
| R4 | `commande_argon_v56_nuit_v5.py` | refus 402/429 du relais rendu en code 4 (comportement v2 à v4) | tuée | 1 failed, 81 passed in 49.96s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 50.2 s |
| R5 | `commande_kimi_v5.py` | 402/429 de l'amont transmis par le relais rendu en code 4 (lecture littérale écartée en v4) | tuée | 1 failed, 75 passed in 46.75s | `test_six_causes_code_ligne_et_registre[kimi-relais_plafond]` | 47.0 s |
| R6 | `commande_kimi_v5.py` | modele_servi nul remis sur la ligne de code 4 (premier contrôle du plafond de session) | tuée | 1 failed, 40 passed in 24.62s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.9 s |
| R7 | `commande_argon_v56_nuit_v5.py` | modele_servi vide remis sur la ligne de code 4 (second contrôle du plafond de session) | tuée | 1 failed, 47 passed in 28.17s | `test_plafond_session_second_controle_code_4[argon]` | 28.5 s |
| R8 | `commande_kimi_v5.py` | refus remis sur la ligne de code 4 (second contrôle du plafond de session) | tuée | 1 failed, 46 passed in 27.45s | `test_plafond_session_second_controle_code_4[kimi]` | 27.7 s |
| R9 | `commande_argon_v56_nuit_v5.py` | stop_reason « refusal » remis sur la ligne de code 4 (premier contrôle du plafond de session) | tuée | 1 failed, 41 passed in 24.43s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 24.7 s |
| R10 | `commande_kimi_v5.py` | plafond_session rendu en code 3 (premier contrôle) | tuée | 1 failed, 40 passed in 23.80s | `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]` | 24.1 s |
| R11 | `commande_argon_v56_nuit_v5.py` | plafond_session rendu en code 3 (second contrôle) | tuée | 1 failed, 47 passed in 28.33s | `test_plafond_session_second_controle_code_4[argon]` | 28.7 s |
| R12 | `commande_kimi_v5.py` | refus du registre compté au pire cas, pas au plancher | tuée | 1 failed, 50 passed in 30.32s | `test_registre_cumule_plein_code_3[kimi]` | 30.6 s |
| R13 | `commande_argon_v56_nuit_v5.py` | envoye vrai sur un refus du registre (code 3) | tuée | 1 failed, 51 passed in 30.37s | `test_registre_cumule_plein_code_3[argon]` | 30.7 s |
| R14 | `commande_argon_v56_nuit_v5.py` | garde d'étape seule rendue en code 4 | tuée | 1 failed, 55 passed in 32.90s | `test_garde_d_etape_code_3[argon]` | 33.2 s |
| R15 | `commande_kimi_v5.py` | registre illisible seul rendu en code 4 | tuée | 1 failed, 52 passed in 31.93s | `test_registre_illisible_code_3[kimi]` | 32.2 s |
| R16 | `commande_argon_v56_nuit_v5.py` | 429 du relais seul rendu en code 4 | tuée | 1 failed, 82 passed in 49.18s | `test_six_causes_code_ligne_et_registre[argon-relais_max_appels]` | 49.5 s |
| R17 | `commande_argon_v56_nuit_v5.py` | cause absente sur un refus 402/429 du relais (code 3 sans cause) | tuée | 1 failed, 81 passed in 48.48s | `test_six_causes_code_ligne_et_registre[argon-relais_plafond]` | 48.8 s |
| R18 | `commande_kimi_v5.py` | garde cumulée seule rendue en code 4 | tuée | 1 failed, 50 passed in 30.31s | `test_registre_cumule_plein_code_3[kimi]` | 30.6 s |
| R19 | `commande_argon_v56_nuit_v5.py` | plafond_session rendu en code 3 (premier contrôle) | tuée | 1 failed, 41 passed in 25.26s | `test_sortie_minimale_du_lecteur_est_la_sienne[argon]` | 25.5 s |
| R20 | `commande_kimi_v5.py` | plafond_session rendu en code 3 (second contrôle) | tuée | 1 failed, 46 passed in 28.31s | `test_plafond_session_second_controle_code_4[kimi]` | 28.6 s |

## Réserves

1. **I34 n'est pas traité** (hors de la demande : « avec seulement » la règle) : une réponse coupée par sa borne de sortie sort
   toujours en code 5 (Kimi : `finish_reason` « length » ; Argon : statut `TRONQUE`), lu « erreur » : arrêt de la course, même
   pour l'expérimentateur et le vérificateur ; T128 de la contre-lecture courte v6 demande pour ces deux rôles un code 0 avec le
   texte, le coût et `modele_servi`. Le constat A.6 bis le trouvera non conforme : décision à prendre (version suivante, ou
   arrêt accepté par écrit).
2. **Fenêtre d'entrée du modèle non contrôlée** (dit plus haut, non ajoutée) : une consigne au-delà sortirait en code 3 ou 5,
   arrêt ; T128 demande que la plus longue consigne d'expérimentateur (≈ 393 000 caractères, mesure du rapport v6) tienne dans
   la fenêtre du modèle servi, ou que la commande la refuse en code 4 ; à la borne de 0,80 USD, Kimi refuse déjà en
   `plafond_session` toute consigne de plus de 378 402 caractères ASCII (limite du LISEZMOI v2 : un jeton compté par octet du
   corps), ce qui ne dit rien de la fenêtre.
3. **`cause_refus` n'est écrite qu'à la dernière ligne.** Le registre gelé n'a pas de champ de cause : un refus du relais y laisse
   `debut` puis `fin` (code 3, 1e-6, statut « echec », `cout_origine` « plancher »), les quatre autres causes n'y écrivent rien
   (comme en v4) ; T128 souhaite la cause « écrite aussi à son registre » : il faudrait un registre v2, hors de la demande. La v64
   ne garde pas la cause : le motif d'un « erreur » est fait de la sortie d'erreur de la commande (`adaptateurs.py` l. 753), que
   les commandes laissent vide ; la cause d'un arrêt n'est donc lisible qu'à la dernière ligne de la commande, que l'étage ne
   garde pas (mineur 3 de la contre-lecture v4, mineur 53 de la contre-lecture courte v6) : à porter à conv-audit si le relevé
   partiel scellé doit dire la cause d'un arrêt.
4. **Prix de la règle** (B11 ; à accepter par écrit par le directeur selon la contre-lecture courte v6) : toute limite propre d'un
   relais ou de la commande arrête désormais la course (code 3, relevé partiel, aucune issue). A.6 bis reste la condition pour
   que cela n'arrive pas (I1 de la contre-lecture v4) : instances neuves des relais pour la course, sans autre usage ; relais Kimi
   `--max-appels` ≥ 1 731, `--plafond-usd` ≥ 44 + `--reserve-par-appel` (≥ 44,40 au défaut, ≈ 1 USD de marge conseillée), barème
   2 / 10 ; relais Argon `--plafond-usd` ≥ 6, `--max-appels` ≥ 147 ; `GET /relais/etat` relevé avant le premier appel. L'exemple
   d'usage de `servir` dans l'en-tête d'Argon (`--plafond-usd 10 --max-appels 50`, historique de la v2) n'est pas le réglage de la
   course.
5. **Kimi, 402 et 429 de Moonshot transmis** : code 3 au plancher, `envoye: false`, comme la v4 et comme le veut la demande,
   alors que l'appel est parti vers l'amont (le relais, lui, le compte au pire cas) ; sans effet sur la lecture v64 (arrêt).
6. Les effets dans l'étage (fin des tours, témoin « non concluant », arrêt) viennent de la demande et de la contre-lecture v4 ;
   seuls l'adaptateur v64 et sa porte « environnement » sont rejoués ici, pas `jouer_etage_1` ni le lanceur.
7. La suite dépend d'une copie du dépôt public au commit `eaa74ca` (empreintes contrôlées) : à refaire chez qui la rejoue.
8. **Contre-lecture neuve (R2) de la v5 à faire** avant d'écrire la configuration (A.2 gèle les chemins des commandes) ; ce
   LISEZMOI n'en tient pas lieu. Chemins chez la fille à vérifier, empreintes v3 comprises (mineur 7 de la contre-lecture v4).
9. Rien n'est commis ni scellé ; aucun `.sha256` créé ; le scellement du dossier revient à session-depot.
