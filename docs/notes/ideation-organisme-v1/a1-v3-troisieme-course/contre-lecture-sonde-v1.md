# Contre-lecture du mode sonde de l'hôte durable d'A1-v3, v1

Je suis un contre-lecteur neuf et je n'ai écrit aucune des pièces. J'ai travaillé le 4 novembre 2026, de 10:25 à 10:36 UTC
(`date -u`), en lecture seule, sans réseau, sans location ni clé.

**Verdict : lançable après corrections.** Trois corrections sont majeures (M1 à M3) : une minuterie sur la machine, `-y` au geste de
repli et la clé de Vast dans `env -i`. Sur le chemin normal, la machine se détruit seule, même si le pilote meurt. En revanche,
plusieurs pannes laissent l'instance listée sans aucun geste. Le plafond de 0,50 USD n'est pas mécanique. La commande de l'additif,
écrite telle quelle, ne crée rien.

## Empreintes vérifiées (depuis le dossier de chaque fichier ; versions égales sur `HEAD` = `origin/main` = `dd309139…`)

| pièce | sha256 |
|---|---|
| `consigne-contre-lecture-sonde-v1.md` | OK (compagnon) |
| `src/controle_ia/sonde_hote_durable_a1_v3.py` | `f7c7f79b…` OK |
| `scripts/amorce_sonde_hote_durable_a1_v3_v1.sh` | `3fb62bd1…` OK |
| `tests/test_sonde_hote_durable_a1_v3.py` | `a5d41158…` OK |
| `rapport-redaction-v3-v1-additif-1.md` | `8fde85cf…` OK |
| `src/controle_ia/hote_durable_a1_v3.py` | `5b853fde…` OK |

**Essais rejoués** avec la commande de la consigne (j'ai ajouté `-p no:cacheprovider`) : **68 passés** en 42,5 s, soit 19 essais
de la sonde et 49 du lanceur. Deux essais jouets de démonstration, écrits à part dans
`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde/test_demo_expiration.py`, passent aussi : ils
établissent le point M1(b).

## Réponses aux questions

1. **Dépense sans session vivante.**
   - Chemin normal : oui. L'hôte Python arrête la course factice au plafond, verse, puis se détruit par `CONTAINER_ID`, sans
     dépendre du pilote.
   - Minuterie indépendante sur la machine : **non**. La destruction n'a lieu qu'en fin de séquence Python (M1).
   - Les 20 min sont mécaniques pour la course factice seulement. Ils sont comptés depuis le démarrage de Python, donc sans le
     démarrage, le clonage et les installations.
   - Les 0,50 USD ne sont qu'un calcul fait d'avance (prix × 35 min, au plus 0,23 USD). Ils ne bornent pas la durée de vie de
     l'instance (m1).
   - Pire cas où la machine ne lance jamais l'amorce : rien ne tourne sur la machine, donc aucune borne mécanique n'est possible
     de ce côté. La borne repose sur un contrôle par session. Au plus prudent, c'est 0,40 USD/h, soit environ 9,6 USD par jour ;
     au plus probable, quelques centimes par jour de stockage pour une instance « exited » (m2).
2. **Clés.**
   - Aucune clé de modèle ne part : le corps est un dictionnaire littéral de six variables, et `env -i` est appliqué au pilote.
   - Deux clés atteignent la machine. `GH_TOKEN` passe par `--env` : il est gardé par Vast, se lit dans `show instances --raw` et
     reste visible de l'exploitant de l'hôte. `CONTAINER_API_KEY` est posée par Vast.
   - C'est le minimum en nombre, pas en portée (m6).
   - La sortie brute de `vastai` n'est jamais affichée quand tout réussit. En cas d'échec, ses 300 derniers caractères sont
     affichés et journalisés, avec le seul jeton GitHub masqué (f1).
3. **Destruction par identifiant.** Oui.
   - La machine ne vise que `CONTAINER_ID`, posé par Vast et contrôlé en chiffres. Aucune valeur d'environnement ne peut injecter
     un `-e`, car les espaces et les guillemets sont refusés.
   - Le pilote ne détruit jamais rien.
   - Aucun chemin du code ne peut viser 58936096, 58936099 ou 58936100. Le repli manuel de l'additif ne fait toutefois rien sans
     `-y` (M2), et la machine ne contrôle pas l'étiquette avant de se détruire (f8).
4. **GO.**
   - GO-2026-11-04-09 est exigé à trois endroits : dans la session, sur la machine (registre et garde de `main` relus au moment du
     départ) et dans l'amorce. GO-2026-11-04-06 est refusé aux trois endroits, et un essai le montre pour chacun.
   - La garde de `main` est appelée telle quelle (`decider`) et le montant de 35 USD est vérifié exactement.
   - R5 est tenu pour la plupart des gardes, avec des trous (m7).
5. **Commande de l'additif.** Elle n'est ni juste ni complète : M2, M3, m4, f6 et f7.

## Points (une ligne chacun)

- **M1 (majeure) — aucune minuterie sur la machine, indépendante de Python ; la leçon de R-1481 n'est pas appliquée.**
  - (a) Échec avant `exec … hote` : clonage refusé, disque plein, `numpy==2.5.3` introuvable (dont la sonde n'a même pas besoin),
    variable absente. L'amorce sort en code 2, le conteneur sort, et il n'y a ni destruction ni arrêt.
  - (b) Exception hors `Refus` dans `fin` ou `se_detruire` : `subprocess.TimeoutExpired` de `git` (délai de 900 s),
    `urllib.error.URLError`, ou `ClientVast("")` qui lève `Refus` hors de tout `try`. L'hôte sort sans aucun geste ; les deux
    essais de démonstration le montrent (`gestes == []`).
- **M2 (majeure) — repli de l'additif `vastai destroy instance <ID>` sans `-y`.** Selon R-1482, `vastai` 1.8.3 demande une
  confirmation et ne fait rien : la fille croirait avoir détruit la machine.
- **M3 (majeure) — `env -i` retire `VAST_API_KEY`.** Selon R-032, `vastai` 1.8.3 lit sa clé dans `VAST_API_KEY`. L'additif dit
  que la clé est dans `HOME`, sans preuve, et R-1480 rapporte que `set api-key` a été refusé. Si c'est le cas, la création échoue
  sans danger : la commande ne lance rien.
- **m1 (moyenne) — 0,50 USD non mécanique.**
  - `cout_machine` compte depuis `Machine.__init__` : le démarrage, le clonage et les installations n'y sont pas.
  - Dans `fin`, rien ne borne la durée : six poussées avec 21 min d'attente au total, plus des délais `git` de 900 s chacun.
    Cela fait jusqu'à environ 4 h, soit environ 1,6 USD à 0,40 USD/h, avant l'arrêt ou la sortie.
  - Le seuil de 0,50 USD dans `garder_sonde` ne peut pas être atteint avant 20 min, à 0,40 USD/h.
- **m2 (moyenne) — pire cas « jamais démarrée » sans borne mécanique.** La borne dépend de la fille, qui peut elle-même être coupée
  par la limite d'usage (R-1481). Rien n'oblige à écrire l'identifiant dans `registres/etat.md` pour que la routine de reprise
  (étape 4) le trouve.
- **m3 (moyenne) — la réponse de création est lue ligne par ligne.** Si `vastai --raw` rend un JSON indenté sur plusieurs lignes
  (non vérifiable hors réseau), une création réussie est lue comme « illisible ». La sonde rend alors le code 2, sans
  `.identifiant`, alors que la machine existe : risque d'une seconde création. Le lanceur T0.5 lisait le texte entier.
- **m4 (moyenne) — commande incomplète.**
  - `COMMIT_PRIVE` et `OFFRE` ne sont pas posés, et aucune ligne ne tire l'offre de `offres.json`.
  - `mkdir "$D"` n'est pas gardé, et les étapes ne sont pas enchaînées.
  - Le contrôle à « environ 35 min » peut venir avant la fin, puisque la durée comprend le démarrage et les installations.
- **m5 (moyenne) — clonage complet de l'historique du dépôt privé au démarrage.**
  - Il est fait sur 30 Go de disque, sans mesure de temps et hors des plafonds.
  - Ordres de grandeur locaux : paquet de 3,45 Gio pour un clone superficiel de 106 commits ; arbre de 2,4 Go, sans `.git` ni
    `.venv`. Il faut y ajouter le clone de versement.
  - Un disque plein mène au point M1(a).
- **m6 (moyenne, nœud de compte) — portée de `GH_TOKEN`.** Le jeton peut écrire dans tout le dépôt privé et il est exposé à un
  hôte tiers (`docker inspect`) ainsi qu'à l'enregistrement de l'instance chez Vast. La rotation de R-1480 est en attente. La portée
  de `CONTAINER_API_KEY` (instance ou compte) est inconnue.
- **m7 (moyenne) — trous de R5.**
  - L'amorce n'a aucun cas sain : aucun essai ne la mène jusqu'à `exec … hote`.
  - Le chemin « destruction refusée → arrêt » n'est jamais éprouvé, car le Vast jouet ne refuse jamais.
  - Aucun essai pour les exceptions de M1(b).
  - Aucun artefact pour la garde « espace ou guillemet » de `ClientSondeCli`, ni pour une réponse de création refusée, illisible
    ou sur plusieurs lignes.
  - `DUREE_MAX_S` absente ou mal formée fait planter `reglages_sonde` avant la classe `Machine`, sans essai.
- **f1 (faible) — fin de sortie de `vastai` montrée en cas d'échec.** `_lancer` ne masque que `GH_TOKEN`, et `inventaire` ne
  masque rien. Or l'interface de Vast accepte `?api_key=` dans l'adresse (R-333), si bien que la clé de Vast pourrait passer par
  un message d'erreur.
- **f2 (faible) — listes de clés interdites différentes.** L'amorce n'a pas `RR_*API_KEY*` ; Python l'a. La vraie garantie reste
  la liste littérale du corps.
- **f3 (faible) — message du commit versé.** Il dit « troisième course » pour la branche de la sonde ; l'étiquette est trompeuse.
- **f4 (faible) — branche unique.** Un refus sur la machine verse sur la même branche `donnees/sonde-hote-durable-a1-v3-v1`. Une
  seconde sonde trouverait cette branche (R12), ne verserait rien et la machine serait seulement arrêtée : il faut une v2 nommée.
- **f5 (faible) — mesures non versées.** Le journal de l'amorce (`/root/amorce-sonde-a1v3.log`, durée des installations) et la
  durée du clonage restent hors du dossier versé, alors que les mesurer est l'objet de la sonde.
- **f6 (faible) — prix sous-estimé.** `search offers` calcule `dph_total` avec le stockage par défaut ; `--storage 30` le
  calculerait pour le disque de 30 Go (à vérifier sur 1.8.3).
- **f7 (faible) — pas de `GO_ID=GO-2026-11-04-09` en tête de ligne.** La garde de la session ne voit pas le `vastai create` lancé
  depuis Python. Le contrôle fait dans le processus est équivalent, mais la trace demandée par CLAUDE.md manque.
- **f8 (faible) — étiquette non contrôlée.** Ni la machine (avant `DELETE`) ni la fille (avant le repli) ne vérifient l'étiquette
  `sonde-a1-v3-v1` ni la concordance avec `.identifiant`.

## Corrections proposées

1. **M1** — Dans `script_de_demarrage_sonde`, comme premier geste, avant le clonage :
   - Lancer par `setsid` une minuterie de destruction, détachée et sans modèle. À l'échéance `DUREE_MAX_S` + 15 min (+ 10 min de
     démarrage), elle appelle `curl -sS -o /dev/null -X DELETE -H "Authorization: Bearer $CONTAINER_API_KEY"
     https://console.vast.ai/api/v0/instances/$CONTAINER_ID/`, puis l'arrêt (`PUT state=stopped`) si la destruction est refusée.
   - Garder le conteneur en vie jusqu'à son échéance : après l'amorce, quel que soit son code, `wait` sur la minuterie ou
     destruction immédiate. Pour la sonde, les données sont factices, donc détruire à l'échéance même sans versement est
     acceptable.
   - Dans `fin` et `se_detruire`, attraper `Exception` (et non seulement `Refus`) autour du versement et du geste, puis passer à
     l'arrêt de repli.
   - Ajouter les essais de M1(b), sur le modèle des démonstrations.
2. **M2** — Remplacer le repli par `vastai destroy instance <ID> -y`, puis vérifier par l'inventaire filtré. Le consigner dans
   `registres/arrets.md`.
3. **M3** — Ajouter `VAST_API_KEY="$VAST_API_KEY"` à `env -i`, sauf si l'on vérifie d'abord, sans l'afficher, qu'un fichier de clé
   existe dans `HOME`. Ajouter `VAST_API_KEY` aux valeurs masquées par `_lancer`.
4. **m1** — Dans `reglages_sonde`, fixer `essais_poussee=2` et `attente_poussee_s=30`, et un délai `git` de 120 s pour la sonde.
   Écrire comme plafond réel « minuterie de la machine », et non 0,50 USD calculé.
5. **m2** — Juste après la création, écrire l'identifiant, l'échéance et l'étiquette dans `registres/etat.md`, committer et pousser.
   La fille contrôle à T+40 et T+60 min ; toute session qui reprend détruit avec `-y` après l'échéance.
6. **m3** — Lire d'abord `json.loads(texte)` en entier, et seulement ensuite ligne par ligne. Le message de refus dit « ne rien
   relancer avant l'inventaire ». Ajouter un essai avec une réponse sur plusieurs lignes.
7. **m4** — Écrire `COMMIT_PRIVE=<hash de 40 caractères>` ; tirer `OFFRE` de `offres.json`, la moins chère des offres conformes,
   par une ligne Python qui reprend `offre_la_moins_chere` ; utiliser `mkdir "$D" || exit 2` ; enchaîner les étapes par `&&` ;
   contrôler jusqu'à T+60 min.
8. **m5** — Cloner au plus juste : `git clone --filter=blob:none --no-checkout` puis `checkout` du commit, ou bien `fetch --depth 1`
   du hash. Faire de même pour le clone de versement, avec un `sparse-checkout` réduit au dossier versé. Chronométrer le clonage.
9. **m6** — Prendre un jeton à grain fin dédié à la machine : contenu seul, sur `controle-ia-travail`, expiration d'un jour,
   révoqué après la sonde. Sinon, Lazar accepte par écrit l'exposition à un hôte tiers.
10. **m7** — Ajouter les essais manquants :
    - un cas sain de l'amorce jusqu'à `exec`, avec un module factice ;
    - un Vast jouet qui refuse la destruction ;
    - les exceptions de M1(b) ;
    - l'artefact « espace ou guillemet » ;
    - les réponses de création refusée ou illisible ;
    - `DUREE_MAX_S` mal formée.
11. **f1 à f8** —
    - Ne journaliser que le code et une ligne masquée, toutes clés comprises.
    - Harmoniser la liste de l'amorce avec celle de Python.
    - Paramétrer le message du commit.
    - Nommer une branche de refus à part.
    - Copier le journal de l'amorce dans le dossier versé avant le scellement.
    - Ajouter `--storage 30` à la recherche.
    - Mettre `GO_ID=GO-2026-11-04-09` en tête de la ligne de location.
    - Contrôler l'étiquette avant le `DELETE` et avant le repli de la fille. Ne jamais toucher 58936096, 58936099 ni 58936100.
