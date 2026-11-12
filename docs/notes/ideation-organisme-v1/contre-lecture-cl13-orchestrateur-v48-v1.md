# Contre-lecture CL13 — orchestrateur du pôle, versions 47 et 48 (depuis la v46)

- Date : 2026-10-29, 23:30 UTC.
- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent **neuf** (règle R2) : n'a écrit aucune version de l'orchestrateur.
- Objet : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/orchestrateur-pole-v7/` de la branche
  `origin/canal/conv-audit-n04` (tête `c3fce25d`, arbre de la v48 au commit `19cadf8c`), extrait par `git archive` hors du dépôt.
  Rien d'autre n'a été lu sur la branche ; aucune branche `donnees/*` ni `quarantaine/*`. Arbre de la v47 pour comparaison :
  même dossier au commit `15ab6ea4` (« Orchestrateur v47 »).
- Aucun appel payant, aucune clé : chaque essai a tourné avec un environnement vidé (`env -i`, clé factice seulement) ; la
  suite complète a tourné en plus dans un espace réseau isolé (`bwrap --unshare-net`, boucle locale seule).

## Empreintes vérifiées

| fichier | empreinte SHA-256 | vérification |
|---|---|---|
| `EMPREINTES-orchestrateur-pole-v7-v48.txt` | `7ce592d103ac4f5193d3281a5886cfda5f33c47736f4b34572f282914a637a37` | égale à l'attendue (`7ce592d1…`) et à son `.sha256` |
| fichiers listés par la v48 | — | `sha256sum -c` : **172 OK, 0 échec** |
| `LISEZMOI-orchestrateur-pole-v7-v48.md` | `d948b0c8a897bcfa9d909dc67809df23412b4a1ad2e3769a2587e5418d022183` | égale à l'attendue (`d948b0c8…`) |
| `LISEZMOI-orchestrateur-pole-v7-v47.md` | `672b41c1ff8eb4c01c208dbb2386a97753eae8d8bab653095e089da0a95908ae` | égale à la ligne de la liste v48 |
| `EMPREINTES-orchestrateur-pole-v7-v47.txt` | `f232c2e285749862cb16d55405b3a71a7da49166e280b954d02fd7dd9e890949` | sur l'arbre du commit `15ab6ea4` : **169 OK** |

Fichiers changés depuis la v46 (comparaison des listes v46 et v48) : nouveaux `pole/protocole_outils.py`, `pole/moisson.py`,
`pole/relais_moisson.py`, `pole/tests_de_mort.py`, `essais/test_v47_relais_moisson.py` ; modifiés `pole/adaptateurs.py`,
`pole/ideation.py`, `pole/dossier_ferme.py`, `pole/relais_reel.py`, `demonstrations/ideation_v1.py`,
`demonstrations/repetition_generale_v6.py`, `essais/test_v7_ideation.py`, `essais/test_adaptateurs.py`,
`essais/test_v6_relais_reel.py`, `essais/faux_sdk/claude_agent_sdk.py`. Entre v47 et v48 : `tests_de_mort.py` nouveau,
`adaptateurs.py`, `protocole_outils.py`, `ideation.py`, `ideation_v1.py`, `test_v7_ideation.py` modifiés.

## Verdict

**Lançable après corrections** — sans l'option (`--tests-de-mort 0`), la v48 est la v47 (prouvé ici) et le moissonneur comme
le correctif R-764 tiennent ; mais **l'étage de tests de mort (`--tests-de-mort ≥ 1`) ne doit pas être lancé** avant
CL13-01 à CL13-04 : le script de l'expérimentateur sort du bac à sable `bwrap` (écriture dans `/usr` de l'hôte quand le noyau
tourne en superutilisateur, et écrasement d'un fichier quelconque de l'hôte par le noyau lui-même, quel que soit l'utilisateur).

## Comptes d'essais

- Suite complète de la v48 (`python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, environnement vidé, réseau isolé) :
  **466 essais, 466 OK, 0 échec, 0 ignoré** (`Ran 466 tests in 263.723s — OK`). Journal :
  `essais48.log`, SHA-256 `f3f42e81ad1487b45a765be909ecab31eb4b6cfd305e63b779c61ddbe9d7c931`.
- Suite de la v47 (même commande, arbre `15ab6ea4`) : **444 essais, 444 OK** (`essais47.log`, SHA-256
  `24e1b65a8ca5129a559c10550f25f61fb68be7561e7516e9342af961a5d5d64f`).
- Annoncé par l'auteur : 466 OK dont 1 ignoré. Ici `bwrap` 0.9.0 est installé : **`test_v48_22` est joué et passe**, seul ou dans
  la suite, dans l'espace réseau isolé comme directement (`Ran 1 test in 0.282s — OK`). Mais il ne prouve que la sonde
  `disponible()` et le refus d'un exécuteur non isolé (voir CL13-08) : il passe alors que CL13-01 existe.
- Le code des essais a été lu avant : faux kit (`essais/faux_sdk`), faux exécuteurs, garde-fou d'essai sur `socket.connect`,
  aucun adaptateur réel armé avec le vrai kit (le kit réel `claude_agent_sdk` 0.2.172 et l'outil `claude` 2.1.312 sont
  installés ici : d'où l'environnement vidé et le réseau isolé par précaution).

Sondes écrites pour cette contre-lecture (bloc-notes de la session, hors dépôt, non versées ; empreintes pour R6) :

| sonde | SHA-256 |
|---|---|
| `sonde_bac.py` | `5d947b19a79d260824734e52bc11e39dea9ebed5dcef4497e16c7e8486e14cbf` |
| `sonde_privileges.py` | `fa283d90042650889ad9f2521f72cee8c737c17f817514b8232894aedc8da3f3` |
| `sonde_usr.py` | `c8c9571dae76ba068b385d757f174bb572fb334e00432b1cf4d79d2baf167a6b` |
| `sonde_etage.py` | `332a70251b7fddbb22e81a5fa1ebaee15aa861114603f2d2f9c8bc6df056c1e9` |
| `sonde_delai.py` | `aab6ee69a5b1bff5caaa0d3e282768ac95ac87289eac1bbcd9197cb7d189ffa1` |
| `course_reference.py` | `39fdf7d3a86c99a005050dbc94c37671e89f5b7b0917adf9b5dcd519eaedfe01` |

## Ce qui tient (vérifié par essai, pas seulement lu)

- **Réseau du bac à sable** (`sonde_bac.py`) : une seule interface (`lo`), connexion vers un écouteur du noyau sur la boucle
  locale refusée (`ConnectionRefusedError`), adresse externe injoignable (`OSError`), résolution de noms impossible (`gaierror`).
- **Environnement du bac à sable** : clé factice posée chez le noyau (`CLE_FACTICE_DU_NOYAU=sk-ant-api03-FACTICE…`), le script
  ne voit que `HOME, LANG, PATH, PWD, PYTHONDONTWRITEBYTECODE, PYTHONHASHSEED, PYTHONIOENCODING`.
- **Fichiers de l'hôte invisibles** : racine du bac à sable = `bin dev etc lib lib64 proc sbin travail usr` ; `/etc/passwd`,
  `/home`, `/root/…`, `/tmp`, un fichier secret de l'hôte : tous `FileNotFoundError` ; deux processus visibles seulement.
- **Délai** (`sonde_delai.py`) : boucle infinie tuée à 3,0 s, sa ligne `RESULTAT:` imprimée avant la mort est gardée mais
  l'exécution est « tuée » (jamais comptée) ; un processus détaché par `setsid` meurt aussi ; aucun processus survivant.
- **Refus de l'étage sans repli** : `test_v48_12` (bac à sable absent → course interrompue, aucun appel, aucun dossier) ; le code
  (`pole/ideation.py` l. 1590-1601, `pole/tests_de_mort.py` l. 782-787) n'a aucune branche vers un autre exécuteur ;
  l'exécuteur factice est refusé avec le moteur réel (l. 783-784 ; lanceur l. 911-912).
- **Préenregistrement court scellé avant la session** : `pole/tests_de_mort.py` l. 945 (sceau) avant l. 974 (première session) ;
  empreinte dans la consigne ; journal numéroté (`test_v48_01`).
- **Classement figé par empreinte** : `classement-fige.json` scellé avant toute session (l. 835-837), empreinte et sceau revérifiés
  après (l. 1121-1127) ; arrêt sinon (`test_v48_09`, OK). Une fiche dont l'empreinte diffère de celle du classement est refusée.
- **Rétrocompatibilité** (`course_reference.py`) : la même course de référence (faux adaptateur, deux proposeurs, deux juges,
  seconde passe) jouée par l'arbre de la v47 et par celui de la v48 : 50 fichiers chacun, mêmes chemins, **46 identiques octet
  pour octet** ; seuls `manifeste-depart.json` et `manifeste-fin.json` (et leurs `.sha256`) diffèrent, sur `code_sha256` (trois
  modules changés, `tests_de_mort.py` ajouté) et l'empreinte de la liste blanche (chemin du dossier provisoire). C'est exactement
  ce que dit le LISEZMOI. Au niveau du lanceur simulé, la comparaison n'a pas de sens : deux courses de la **même** version
  diffèrent déjà sur 36 fichiers (clés d'anonymisation tirées au hasard), en v47 comme en v48.
- **R-764, trois barrières présentes** : (1) kit — `CLAUDE_CODE_NO_MODEL_FALLBACK=true` et
  `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1` dans `env`, `fallback_model=None` (`pole/adaptateurs.py` l. 36, 344-346, 389) ; lu
  dans le binaire de l'outil 2.1.312 installé ici : `function vz(){return!i.CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK&&!h2()}`, ce qui
  confirme la lecture de l'auteur ; (2) noyau — modèle servi et `stop_reason` de chaque message, événements système
  `model_refusal_fallback`, `model_fallback`, `model_refusal_no_fallback` → statut « refus », arrêt, jamais « budget dépassé »
  (l. 441-506) ; le kit installé range bien un sous-type inconnu en `SystemMessage` générique ; (3) relais — `--modeles-permis`,
  403 avant tout envoi à l'amont (`pole/relais_reel.py` l. 257-270), liste vide = tout refusé ; le lanceur exige la liste égale aux
  modèles de la course. Essais cas sain et artefacts : `test_v47_r764_refus_de_modele_trois_barrieres`, `test_v48_10`, essais du
  relais : OK. Pour Claude, je n'ai trouvé aucun chemin où un refus ou une bascule passe sans arrêt ; pour Argon, voir CL13-05.
- **Moissonneur** : relais à part sur la boucle locale, deux routes seulement, paramètres `q` et `n` seuls, jeton propre, gardes 1
  à 3 refaites au relais et 1 à 6 au noyau, plafond par source, aucun en-tête d'identité par défaut, amonts codés en dur sans
  suivi de redirection, réponses scellées avec empreinte des octets bruts et du JSON canonique, cache scellé et rejeu sans
  réseau, tours de moisson comptés dans les sommes de plafonds et la moisson servie dans les gardes de taille. Restes : CL13-09.

## Constats

### CL13-01 — Le script de l'expérimentateur garde les capacités du superutilisateur et défait la lecture seule : écriture dans `/usr` de l'hôte

- **Gravité : critique** (sortie du bac à sable ; exécution de code hors du bac à sable au lancement suivant).
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 434-453 (`ExecuteurBacASable.commande`) ; sonde l. 504-541.
- **Défaut** : quand le noyau tourne en superutilisateur (le cas ici, et probablement chez session-depot, conteneur en
  superutilisateur), `bwrap` garde par défaut toutes les capacités du processus enfermé (identifiant 0 dans un espace
  d'utilisateurs `0 0 1`). Le script peut alors remonter en écriture les montages que `bwrap` a posés en lecture seule — `/`,
  `/travail/tranche`, et surtout **`/usr` et `/etc/alternatives` de l'hôte**, montés par liaison — puis y écrire. Un module
  planté dans `/usr/lib/python3.13/` s'exécuterait au prochain lancement du noyau, avec son réseau (relais), ses fichiers et son
  environnement. La sonde `disponible()` ne teste que le réseau et `open('../hors-travail.txt')` : elle passe, `test_v48_22` aussi.
- **Essai exécuté** : `env -i PATH=/usr/bin:/bin HOME=… python3 -B sonde_usr.py <arbre v48> <dossier>` (fichier témoin neuf
  `/usr/lib/cl13-sonde-<hasard>.txt`, retiré aussitôt par l'hôte) ; et `sonde_privileges.py`. Sorties :

  ```
  v48 telle quelle : code 0 {"cap_eff": "000001fffeffffff", "uid": 0, "écrire /usr avant remontage": "OSError",
    "remonter /usr en écriture": "OK", "écrire /usr après remontage": "ÉCRIT", "remonter /travail/tranche en écriture": "OK"}
  v48 telle quelle : témoin présent sur l'hôte : True
  v48 telle quelle : témoin retiré par l'hôte : True
  (sonde_privileges) "uid_map": ["0","0","1"], "remonter / en écriture": "OK", "écrire / après remontage": "ÉCRIT",
    "écrire tranche après remontage": "ÉCRIT" ; tranche côté hôte après exécution : ['altere.txt', 'serie.csv']
    "mknod/lecture disque": "PermissionError [Errno 1] Operation not permitted"
  ```
  (la création d'un nœud de périphérique est refusée : pas de lecture brute du disque ; l'altération de la tranche est rattrapée
  par la vérification d'empreintes du noyau, l. 1056-1066, qui rend « non concluant »).
- **Correction** : dans `commande`, ajouter `--unshare-user --uid 65534 --gid 65534 --cap-drop ALL` (et, si possible,
  `--disable-userns` et un filtre d'appels système) ; dans la sonde, ajouter deux artefacts : `CapEff` doit valoir 0, et une
  tentative de remonter `/usr` en écriture doit échouer ; en faire l'objet de `test_v48_22`. Essai de la correction (même sonde,
  commande complétée par ces quatre drapeaux) :

  ```
  corrigée : code 0 {"cap_eff": "0000000000000000", "uid": 65534, "écrire /usr avant remontage": "OSError",
    "remonter /usr en écriture": "Operation not permitted", "écrire /usr après remontage": "OSError",
    "remonter /travail/tranche en écriture": "Operation not permitted"}
  corrigée : témoin présent sur l'hôte : False
  corrigée : sonde disponible() : (True, 'bwrap présent ; sonde OK ; connexion réseau refusée (réseau isolé) ; …')
  ```

### CL13-02 — Le noyau suit un lien symbolique posé par le script et écrase un fichier quelconque de l'hôte

- **Gravité : critique** (indépendant de CL13-01 : marche aussi avec un utilisateur sans privilège dans le bac à sable).
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 1029-1031 (`open(chemin_script, "w")` dans le dossier de travail inscriptible
  par le script) ; même défaut l. 1064-1066 (copie de la tranche « remise à l'identique » par `open(…, "w")`).
- **Défaut** : le dossier de travail est inscriptible par le script ; à l'exécution n, le script remplace `script.py` par un lien
  vers un chemin de l'hôte ; à l'exécution n+1, le noyau (hors bac à sable, avec ses droits) écrit le nouveau script **à travers
  le lien** : contenu choisi par l'expérimentateur, cible choisie par lui (code du pôle, `classement.json`, fichier de démarrage
  de l'interpréteur, etc.).
- **Essai exécuté** : `sonde_etage.py`, classe `SondesCL13Ecrasement` (étage complet, faux kit, **vrai** `bwrap`, quota de 3
  exécutions) : exécution 1 `os.remove('script.py'); os.symlink(<fichier de l'hôte>, 'script.py')`, exécution 2 un script
  marqué. Sortie : `FICHIER DE L'HÔTE APRÈS L'ÉTAGE : "# ÉCRIT PAR L'EXPÉRIMENTATEUR\nprint('RESULTAT: 0.4')\n"` (contenu
  d'origine : `CONTENU ORIGINAL DE L'HÔTE`).
- **Correction** : ne jamais écrire, lire ni hacher côté hôte un chemin du dossier inscriptible sans `O_NOFOLLOW` et vérification
  `lstat` (fichier régulier seulement) ; mieux : écrire le script dans un dossier du noyau **non monté en écriture** et le lier en
  lecture seule (`--ro-bind <script> /script.py`), vider ou recréer le dossier de travail par `unlink` avant chaque écriture ;
  ajouter l'artefact « lien posé sur `script.py` » aux essais R5.

### CL13-03 — Fichiers produits : le noyau suit les liens et copie dans la sortie scellée son propre environnement et des fichiers de l'hôte

- **Gravité : haute** (fuite de secrets de l'hôte vers `SORTIE`, qui est scellée puis versée au dépôt).
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 1042-1046 (`os.path.getsize` et `open(…, "rb")` suivent les liens) ;
  l. 374-386 (`_empreintes_de` consigne bien `lien:<cible>`, mais la copie ne regarde pas ce marqueur).
- **Défaut** : un script qui crée `environ.txt → /proc/self/environ` et `secret.txt → <fichier de l'hôte>` obtient du noyau la
  copie scellée de l'environnement **du noyau** et du fichier de l'hôte dans `execution-NN/produits/`. Les contenus ne sont pas
  servis aux agents (noms seulement), mais ils sont écrits, scellés et poussés. La garde de l'adaptateur réel ne refuse que onze
  noms de variables (`pole/relais.py` l. 15-18) : `GEMINI_API_KEY_2`, des clés de relais ou de sources ouvertes, ou un fichier
  de clé du relais resteraient copiables.
- **Essai exécuté** : `env -i … CLE_FACTICE_DU_NOYAU=sk-ant-api03-FACTICE… python3 -B sonde_etage.py <arbre v48>
  SondesCL13.test_cl13_liens_symboliques_suivis_par_le_noyau`. Sortie (chemin, octets, clé factice présente, secret présent) :
  `('noyau/tests-de-mort/fable-p1-02/execution-01/produits/environ.txt', 158, True, False)`,
  `('…/execution-01/produits/secret.txt', 19, False, True)`.
- **Correction** : `os.lstat` et `stat.S_ISREG` avant toute copie ou empreinte ; liens, tubes, périphériques et prises consignés
  comme tels (« non copié : lien vers … »), jamais suivis ; artefact R5 correspondant.

### CL13-04 — Un tube nommé dans le dossier de travail bloque le noyau sans fin, sans manifeste

- **Gravité : moyenne** (aucune dépense, mais arrêt silencieux : ni verdict, ni manifeste de l'étage ni de fin ; R5).
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 374-386 (`_empreintes_de` → `sha256_fichier`, `pole/outils.py` l. 33-38,
  `open(chemin, "rb")` sur un tube sans écrivain).
- **Essai exécuté** : `timeout -s KILL 60 python3 -B sonde_etage.py <arbre v48> SondesCL13.test_cl13_tube_nomme` (script
  `os.mkfifo('tuyau'); print('RESULTAT: 0.4')`, délai d'exécution 20 s) : `code de sortie 137 (tué par timeout après 60 s)` ;
  le script avait fini, le noyau restait bloqué dans le calcul d'empreinte.
- **Correction** : même garde que CL13-03 (`lstat`, fichiers réguliers seulement) ; borne aussi sur le nombre de fichiers parcourus.

### CL13-05 — R-764 : aucun contrôle du modèle servi pour Argon (commande externe), proposeur, juge ou expérimentateur de l'étage

- **Gravité : moyenne**.
- **Fichier et lignes** : `pole/adaptateurs.py` l. 601-662 (`AdaptateurCommandeExterne` : la commande rend `{texte, cout_usd}`,
  rien sur le modèle) ; l. 560 (la v48 ouvre aux rôles de l'étage).
- **Défaut** : les trois barrières ne couvrent que Claude. Si la commande d'Argon bascule d'elle-même vers un autre modèle, ou rend
  un refus en texte, le noyau ne le voit pas : pour l'expérimentateur, un refus en texte devient « réponse sans demande (vaut
  fin) » puis « non concluant », sans arrêt ; pour un proposeur ou un juge, au mieux une fiche ou une note invalide.
- **Essai exécuté** : lecture du code et de `test_v48_18` / `test_v48_19` (Argon expérimentateur : aucune assertion sur un modèle
  servi) ; aucune voie de lecture du modèle n'existe à éprouver.
- **Correction** : exiger dans la ligne JSON de la commande un champ `modele_servi` (et `refus` facultatif), le comparer au modèle
  demandé comme `modele_conforme`, statut « refus » sinon ; à défaut, le dire au manifeste comme barrière absente pour Argon.

### CL13-06 — R-764, Claude : défense en profondeur incomplète sur le message de résultat

- **Gravité : mineure**.
- **Fichier et lignes** : `pole/adaptateurs.py` l. 488-494 (branche `ResultMessage`).
- **Défaut** : `ResultMessage.stop_reason` et `ResultMessage.model_usage` (modèles réellement facturés, champ présent dans le kit
  0.2.172 installé) ne sont pas lus. D'après le binaire 2.1.312, un refus sans repli arrive comme `system/model_refusal_no_fallback`
  ou comme message de l'assistant à `stop_reason === "refusal"` : les deux sont couverts ; le contrôle supplémentaire fermerait le
  cas d'une forme de flux non prévue. Par ailleurs le binaire porte un crochet `PreModelSwitch` (38 occurrences ; refus de
  changement de modèle par l'hôte du kit) : quatrième barrière possible côté kit, **à vérifier** (absent du type `HookEvent` du kit
  Python).
- **Essai exécuté** : `grep -a` sur `/opt/claude-code/bin/claude` (chaînes citées ci-dessus) ; lecture de
  `claude_agent_sdk/types.py` (l. 1378-1390 et 1695-1712).
- **Correction** : au `ResultMessage`, refus si `stop_reason == "refusal"` ou si une clé de `model_usage` n'est pas conforme au
  modèle demandé.

### CL13-07 — Barrière 3 : les modèles de l'étage ne sont pas dans la liste exigée du relais (contraire au LISEZMOI)

- **Gravité : mineure** (le défaut ferme : il bloque, il ne laisse rien passer).
- **Fichier et lignes** : `demonstrations/ideation_v1.py` l. 1131 et 1220 : `modeles_attendus=[m for _, m in proposeurs + juges]`.
- **Défaut** : le LISEZMOI v48 dit « modèles de l'étage inclus dans les modèles permis au relais » ; le code inclut seulement
  proposeurs et juges (les modèles de l'étage sont vérifiés contre Opus et Fable par `verifier_modele_reel`, pas contre le relais).
  Une course à modèle unique (Opus) avec un lecteur Fable : relais exigé = {Opus}, la session du lecteur prend un 403, l'étage
  s'arrête ; lancer le relais avec {Opus, Fable} fait refuser la course. Et quand les deux modèles sont permis, une bascule Opus →
  Fable passe la barrière 3 (la barrière 2 la rattrape).
- **Essai exécuté** : lecture ; `test_v48_10` n'éprouve que `ModeleNonPermis` (modèle hors Opus et Fable).
- **Correction** : `modeles_attendus` = proposeurs + juges + expérimentateur + lecteur quand l'étage est demandé ; essai du lanceur.

### CL13-08 — `test_v48_22` et la sonde ne prouvent pas ce que leur texte annonce

- **Gravité : mineure** (mais c'est ce qui a laissé passer CL13-01 à CL13-04 ; R5).
- **Fichier et lignes** : `essais/test_v7_ideation.py` l. 6712-6721.
- **Défaut** : la docstring annonce « un script qui lit la tranche … réussit, une écriture hors du dossier de travail échoue, un
  script trop long est tué » ; le corps ne joue que `disponible()` et le refus d'`ExecuteurNonIsole`. Aucun essai ne joue l'étage
  avec le vrai `bwrap`, ni les artefacts capacité, remontage, lien et tube.
- **Essai exécuté** : `python3 -B -m unittest -v essais.test_v7_ideation.TestV48.test_v48_22_bac_a_sable_reel_si_bwrap_present`
  → `OK` (0,28 s), alors que `sonde_usr.py` montre l'évasion.
- **Correction** : faire de `test_v48_22` l'essai réel annoncé, plus les artefacts de CL13-01 à CL13-04 (les sondes de cette
  contre-lecture peuvent servir de base).

### CL13-09 — Moissonneur : plafond « journalier » remis à zéro au redémarrage, amont arXiv en clair

- **Gravité : mineure**.
- **Fichier et lignes** : `pole/relais_moisson.py` l. 132-164 (`CompteurJournalier` en mémoire seulement), l. 47
  (`"arxiv": "http://export.arxiv.org/api/query"`).
- **Défaut** : relancer le relais remet le compteur à zéro le même jour ; les requêtes vers arXiv partent en clair (le texte est
  lisible et modifiable en route ; les réponses sont « non opposables », mais le contenu des requêtes est dérivé des fiches). Rappel
  déclaré par l'auteur, à garder en réserve : la garde de fuite est lexicale (identifiants, bardeaux, extraits > 60 caractères) ;
  une **paraphrase** d'une hypothèse du programme quitte la machine (≤ 4 × 200 caractères par proposeur et par tour).
- **Essai exécuté** : lecture ; `essais/test_v47_relais_moisson.py` (9 essais, OK dans la suite).
- **Correction** : compteur persistant (fichier scellé par jour) ; `https://export.arxiv.org/api/query` ; le reste à faire valider
  par Lazar au GO de la première moisson réelle.

### CL13-10 — R12 : modules de code écrasés en place

- **Gravité : mineure** (pratique ancienne de cette lignée ; la v47 reste récupérable).
- **Fichier** : `pole/ideation.py`, `pole/adaptateurs.py`, `pole/protocole_outils.py`, `demonstrations/ideation_v1.py`,
  `essais/test_v7_ideation.py`.
- **Défaut** : « v1 à v47 gardées (R12) » vaut pour les LISEZMOI et EMPREINTES, pas pour le code : sur l'arbre de la v48,
  `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v47.txt` donne **5 FAILED** (ces cinq fichiers). La v47 n'existe plus que dans
  l'historique Git (commit `15ab6ea4`, 169/169 OK) et dans son lot zippé.
- **Essai exécuté** : commande ci-dessus.
- **Correction** : le dire tel quel dans le LISEZMOI (« code de la v47 : commit `15ab6ea4` et lot v47 ») ; ou versionner les
  modules.

### CL13-11 — « Survit » n'est pas vérifiable : le chiffre lu est celui que le script imprime

- **Gravité : mineure** (limite déclarée par l'auteur ; résultat exploratoire).
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 44-45, 637-651 (le lecteur ne voit pas le script).
- **Défaut** : l'expérimentateur peut imprimer `RESULTAT: <n'importe quoi>` sans calculer le test gelé ; le lecteur et la lecture
  mécanique concordent alors, et l'étiquette « survit » part en matériau vers la génération suivante (R4 : trop beau = réserve).
- **Correction** : étiqueter le matériau « survit (chiffre imprimé par le script, non recalculé) » ; ou servir le script scellé au
  lecteur avec la question « le script calcule-t-il le test gelé sur les données nommées ? », un « non » valant « non concluant ».

### CL13-12 — Ressources de l'hôte non bornées

- **Gravité : mineure**.
- **Fichier et lignes** : `pole/tests_de_mort.py` l. 455-459 (`RLIMIT_FSIZE` par fichier seulement).
- **Défaut** : nombre de fichiers et place totale du dossier de travail non bornés (un script peut écrire des milliers de fichiers
  de 50 Mo en 120 s, puis le noyau les hache tous) ; `/dev` et `/dev/shm` sont inscriptibles dans le bac à sable (sans effet sur
  l'hôte, éphémères).
- **Essai exécuté** : `sonde_bac.py` (`"ecrire /dev/shm/x.txt": "ÉCRIT"`) ; la saturation du disque n'a pas été jouée.
- **Correction** : dossier de travail sur un système de fichiers en mémoire borné (`--size` puis `--tmpfs`, `bwrap` ≥ 0.9) ou quota
  de place vérifié après chaque exécution ; borne du nombre de fichiers parcourus.

## Récapitulatif par gravité

| gravité | constats |
|---|---|
| critique | CL13-01 (capacités : `/usr` de l'hôte inscriptible), CL13-02 (écrasement d'un fichier de l'hôte par lien sur `script.py`) |
| haute | CL13-03 (copie de l'environnement du noyau et de fichiers de l'hôte dans la sortie scellée) |
| moyenne | CL13-04 (tube nommé : noyau bloqué sans manifeste), CL13-05 (Argon : modèle servi non lu) |
| mineure | CL13-06, CL13-07, CL13-08, CL13-09, CL13-10, CL13-11, CL13-12 |

Critère par critère : (1) R-764 — trois barrières présentes et éprouvées (cas sain et artefacts) pour Claude ; reste Argon
(CL13-05) et deux renforts (CL13-06, CL13-07). (2) Moissonneur — conforme, restes mineurs (CL13-09). (3) Étage — réseau, clés
d'environnement, refus sans repli, préenregistrement scellé avant session, classement figé : tenus ; **lecture seule et
confinement du système de fichiers : non tenus** (CL13-01 à CL13-04) ; `test_v48_22` passe ici. (4) Rétrocompatibilité —
prouvée sur la course de référence. (5) 466/466 OK. (6) Aucune garde de dépense contournée trouvée ; aucun lancement réel fait.
