# Lecture du code aux commits épinglés et devis — The Agentic Scientist v3 — v1

**Date** : 30 octobre 2026, rédigée de 07:43 à 07:58 UTC (`date -u`). **Sous-agent neuf** : n'a écrit ni la revue de sûreté ni la vérification sur pièces primaires.
**Mandat** : lecture du code sur pièces primaires et devis ; rien installé, rien cloné, rien exécuté de tiers, rien loué, aucun compte créé, aucune clé.
**Pièces lues** :
- Revue de sûreté v1 : `origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/ia-scientifique-externe-v3/revue-surete-v3-v1.md`, sha256 `b12fc9cb1c391988d6d17267e7ef47c406b7c2beab9b4e4706a71e71abfc3ff0`, égale à son fichier compagnon (abrégée **RS**).
- `docs/notes/ideation-organisme-v1/ia-scientifique-externe-v1/verification-pieces-primaires-v1.md` (abrégée **VPP**).
- Article, PDF `docs/sources/pdf/2610.18933v1.pdf`, sha256 `cb170b5435743032755f89b97136464a024df2c0fb4f46286a69945208585fd5`, égal à son compagnon.
- Code tiers, fichiers bruts lus par `curl` au travers du mandataire de la session (l'outil de lecture Web et le serveur GitHub de la session refusent ces dépôts), le 30 octobre 2026 de 07:44 à 07:48 UTC. Préfixes :
  - **v3@** = `https://raw.githubusercontent.com/SakanaAI/AI-Scientist-v3/df8313889a004f8a44a472e19a833cd547bb828a/`
  - **H@** = `https://raw.githubusercontent.com/RobertTLange/headless-cli/93cd9b06b85f848af1308c41e018991b33907c5e/` (dépôt et commit confirmés par v3@`src/docker/agent-cli/Dockerfile` l.63-65 et v3@`src/scripts/lib/container_agent.sh` l.6).
- Pages de prix, consultées le 30 octobre 2026 de 07:49 à 07:51 UTC (adresses au § 3).

Limites : l'arborescence des dépôts n'a pas pu être listée (interface GitHub refusée, 403) ; les fichiers ont été trouvés par les chemins cités dans la documentation et dans les `source`/`import`. Fichiers lus en entier ou par passages ciblés : README, `docs/install.md`, `docs/pipeline.md`, `docs/agent_billing.md`, `configs/config.yaml`, `configs/pipeline_config.yaml`, `configs/preset/paper.yaml`, `configs/posthoc_config.yaml`, `configs/variants_config.yaml`, Dockerfile, `pyproject.toml`, `src/pipeline/config.py`, `src/investigation/config.py`, `src/investigation/constants.py`, `src/investigation/task_runtime.py`, `src/orchestrator/paper_step.py`, `src/aireview.py`, `src/scripts/run.sh`, `src/scripts/idea.sh`, `src/scripts/lib/container_agent.sh`, `src/scripts/lib/concept_figure.sh` ; H@`README.md`, `docs/usage.md`, `src/cli.ts`, `src/billing.ts`, `src/agents.ts`, `src/models-dev.ts`. **Non lus** : variantes (`src/variants_pipeline/`), phase post-hoc en Python, courtier de l'évaluateur, `src/scripts/task.sh` et `paper.sh` hors recherche ciblée.

## Verdict

1. **Aucune adresse Anthropic codée en dur** ni dans v3 ni dans Headless : le relais est joignable par `ANTHROPIC_BASE_URL`. **Mais la variable posée dans le `.env` ne suffit pas** : pour toute tâche à contrat (toutes celles livrées), le `.env` est filtré par une liste de clés qui ne la contient pas, et les passe-variables sont vidés. Il faut l'**image dérivée** (réglages gérés de Claude Code), sans toucher au code Python.
2. Le réseau se règle **sans retouche** (`container.network` et `posthoc.container.network` sont passés tels quels à `docker run`), mais plusieurs conteneurs **effacent l'environnement** : un mandataire désigné par `HTTPS_PROXY` casse l'installation des dépendances de la tâche. Il faut un mandataire **transparent** (interception au niveau du réseau), pas seulement par variables.
3. Trois réglages par défaut fuient et se corrigent par configuration : copie des identifiants de `~` dans les conteneurs (`container.auth_root`), préréglage `paper` qui **active la relecture par OpenAI**, et Headless qui **retire `ANTHROPIC_API_KEY`** dès qu'un `~/.claude.json` existe (utiliser `ANTHROPIC_AUTH_TOKEN`). Devis : environ 14 à 18 USD par cycle tout compris (dont moins de 1 USD de machine), environ 835 à 1 100 USD pour trois courses de 20 cycles, essai compris (estimation, non opposable).

**Corrections à la revue de sûreté (RS)** : (a) RS § 2 suppose que Headless lance les conteneurs et qu'il faut `--docker-env` : **faux à ce commit** ; v3 lance lui-même `docker run`, puis exécute Headless *dans* le conteneur (container_agent.sh l.982-989, l.1169-1237) ; `--docker-env` n'est jamais utilisé. (b) RS § 3 prévoit un réseau interne avec `HTTPS_PROXY` : insuffisant (point 2). (c) RS ne voit ni le filtre du `.env`, ni `auth_root`, ni le préréglage `paper` qui contient `review`, ni le retrait de la clé par Headless, ni le modèle figé `claude-opus-5-5` des figures de concept.

## 1. Table des six points

Toutes les lignes ci-dessous ont été lues le **30 octobre 2026 entre 07:44 et 07:48 UTC** ; URL = préfixe + chemin.

| n° | Question | Fichier et lignes (URL) | Citation courte | Lecture | Verdict |
|---|---|---|---|---|---|
| 1a | Adresse codée en dur ? | v3@`src/investigation/constants.py` l.39 ; H@`src/models-dev.ts` l.6 ; recherche d'adresses sur tous les fichiers lus | `CODEX_STREAM_URL = "https://chatgpt.com/backend-api/codex/responses"` ; `"https://models.dev/api.json"` | Seules adresses en dur : point d'accès de Codex (agent non utilisé) et tarifs de models.dev. Aucune pour Anthropic. | **sûr** |
| 1b | La variable atteint-elle les conteneurs ? | v3@`src/scripts/run.sh` l.1272-1280 et `src/scripts/idea.sh` l.930-938 ; v3@`src/scripts/lib/container_agent.sh` l.176-177, l.766-771 | `sanitize_env_file_for_docker … "$(agent_provider_allowed_env_keys …)"` ; liste pour `claude` : `HEADLESS_BILLING ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN AWS_… CLAUDE_CODE_OAUTH_TOKEN CLAUDE_CODE_USE_BEDROCK` | Tâche à contrat (fichier `task_contract.json`, run.sh l.344-351) + conteneur : le `.env` est réduit à cette liste ; **`ANTHROPIC_BASE_URL` est retirée**. | **à configurer** (image dérivée) |
| 1c | Autres voies d'entrée | v3@`run.sh` l.359-360 ; `idea.sh` l.377-378 ; `container_agent.sh` l.344-377 | `export AGENT_CONTAINER_PASSTHROUGH_KEYS=""` | Les passe-variables de l'hôte sont vidés par chaque phase. Restent : `ENV` de l'image, ou réglages gérés de Claude Code dans l'image. | **à configurer** |
| 1d | Effacements d'environnement | v3@`src/scripts/lib/concept_figure.sh` l.660-664 ; v3@`src/orchestrator/paper_step.py` l.168-174 | `for concept_env_key in $(compgen -e); do … unset …` ; `exec env -i PATH=…` | Le conteneur des figures de concept efface toute variable hors liste, **y compris un `ENV ANTHROPIC_BASE_URL` de l'image** ; un fichier de réglages gérés survit (fichier, pas variable — **SUPPOSÉ** pour Claude Code 2.1.285, à éprouver). | **à configurer** ; échec fermé si le mandataire refuse `api.anthropic.com` |
| 1e | Headless garde-t-il l'adresse ? | H@`src/billing.ts` l.20-26, l.65-77, l.91-107, l.131-136 ; H@`src/cli.ts` l.1136-1147 | `claudePaidVariables = ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL", …]` ; `return "native"` | Voie « native » (aucun abonnement, aucun Bedrock) : environnement transmis intact. Voies abonnement et Bedrock : **retirent `ANTHROPIC_BASE_URL`**. Donc aucun jeton d'abonnement, aucun fichier `.credentials.json`, aucune variable `AWS_*`. | **à configurer** |
| 1f | Clé retirée par Headless | H@`src/agents.ts` l.258-274 | `env.ANTHROPIC_API_KEY !== undefined && claudeOauthExists(env) ? { ANTHROPIC_API_KEY: undefined }` ; `claudeOauthExists` teste `$HOME/.claude.json` | Claude Code écrit `~/.claude.json` ; le foyer du conteneur persiste (`.agent_home`, container_agent.sh l.862-866, l.1206). Après le premier appel, `ANTHROPIC_API_KEY` serait retirée (**lu dans le code, effet à éprouver**). `ANTHROPIC_AUTH_TOKEN` n'est pas retiré et figure dans la liste (l.177). | **à configurer** : jeton de course dans `ANTHROPIC_AUTH_TOKEN` (en-tête `Authorization: Bearer`, le relais doit l'accepter) |
| 2a | Mode réseau par défaut | v3@`src/pipeline/config.py` l.132-135 ; `configs/pipeline_config.yaml` l.50-52 ; `configs/config.yaml` l.84 | `default="host"` ; `posthoc: container: network: bridge` | `agsci run` : `host` ; post-hoc : `bridge` ; `agsci investigate` seul : `bridge`. Confirme VPP n°36. | **à configurer** |
| 2b | Un réseau nommé est-il accepté ? | v3@`src/investigation/config.py` l.277-280, l.581-582 ; `container_agent.sh` l.1176, l.1552 ; `task_runtime.py` l.607-608 ; `paper_step.py` l.4345-4346 | `container.network must be non-empty` ; `--network "$container_network"` | Aucune liste fermée ; la valeur passe telle quelle à `docker run`. `container.network=<réseau>` et `posthoc.container.network=<réseau>` suffisent, sans retouche. | **à configurer** |
| 2c | Réseaux créés, passerelle | `container_agent.sh` l.1223-1226 ; `task_runtime.py` l.2397-2400 | `--add-host=host.docker.internal:host-gateway` ; `network="none"` | v3 ne crée aucun réseau. Hors `host`, il ajoute un nom vers l'hôte, sauf `AGENT_CONTAINER_DISABLE_HOST_GATEWAY=1`. L'évaluation de référence tourne **sans réseau** (bon). | **à configurer** (poser la variable) |
| 2d | Mandataire par variables ? | `task_runtime.py` l.592-621, l.2209-2215 | `--env HOME=/tmp --env PYTHONNOUSERSITE=1 …` | La création de l'environnement de la tâche (installation des paquets) se fait sur `container.network` avec **seulement** ces variables : un `HTTPS_PROXY` n'y entre pas. Idem figures (1d). Node (Headless, `fetch`) ignore `HTTPS_PROXY` par défaut (SUPPOSÉ pour Node 22). | **à corriger dans l'architecture** : mandataire transparent (§ 2) |
| 3a | `.env` lu et monté | v3@`src/pipeline/config.py` l.136-139 ; `run.sh` l.266-273 ; `docs/install.md` l.129-131 | `default=".env"` ; `if [ -z "$CONTAINER_ENV_FILE" ] && [ -f "$REPO_ROOT/.env" ]; then CONTAINER_ENV_FILE="$REPO_ROOT/.env"` | Le `.env` de la racine est repris **même si `container.env_file` est vide**, dès qu'il existe. | **à configurer** : aucun `.env` à la racine ; un fichier d'environnement de course hors du dépôt, ne contenant que `ANTHROPIC_AUTH_TOKEN` |
| 3b | Fichiers d'identifiants copiés | `container_agent.sh` l.824-828, l.869-901 ; `src/investigation/config.py` l.281-283 ; `src/pipeline/config.py` l.949-960 | `.claude/.credentials.json` / `.claude/auth.json` ; `auth_root: … default="~"` | Copie, depuis `~` de l'hôte, des identifiants de l'agent dans le foyer du conteneur. Doit être un vrai dossier (l.959-960). | **à configurer** : `container.auth_root=<dossier vide dédié>` |
| 3c | Clés lues par Headless | H@`src/billing.ts` l.142-170 | `if (nonempty(env.CLAUDE_CODE_OAUTH_TOKEN)) return "subscription"` ; lit `.credentials.json`, `auth.json`, `.claude.json` | Détecte un abonnement par fichiers : s'il en trouve, voie abonnement → adresse du relais retirée (1e). | **à configurer** (foyer vierge) |
| 3d | Relecture et figures | v3@`src/aireview.py` l.39, l.506-513 ; `docs/pipeline.md` l.57-61 ; `concept_figure.sh` l.590-616 | `MODEL = "o4-mini-2025-04-16"` ; `OPENAI_API_KEY is not configured` ; `no concept-figure VLM key available; using deterministic export` | Lisent `OPENAI_API_KEY` ou `GEMINI_API_KEY` dans l'environnement ou le `.env` ; absents → relecture en échec non bloquant, figures en export simple. | **sûr** si aucune de ces clés |
| 4a | Cycles et tentatives | `configs/config.yaml` l.28-44 ; `configs/pipeline_config.yaml` l.37-45 ; `configs/preset/paper.yaml` l.14-21 | `max_idea_cycles: 20` (étage) ; `max_idea_cycles: 3 # investigation default: 20` (orchestrateur) ; préréglage : 20 | Défaut d'`agsci run` : 3 cycles, 1 évaluation par tentative ; ablations : 5 réplications × 5 évaluations ; préréglage de campagne : 20 cycles. | **à configurer** |
| 4b | Durées | `configs/config.yaml` l.37-41, l.50-64, l.66-77 ; `configs/variants_config.yaml` l.25-34 ; `configs/posthoc_config.yaml` l.17-24 | `run_timeout_seconds: 21600` ; `idea_timeout_seconds: 3600` ; `harness_evaluation_timeout_seconds: 7200` ; `timeout_seconds: 7200` (article) | Bornes de durée par tentative, idée, évaluation, variante (7 200 s), analyse (3 600 s), article ; réparations bornées (`max_repair_rounds: 10`, `design_max_repairs: 8`…). **Aucune borne de durée globale de course.** | **à configurer** + `timeout` du processus sur l'hôte |
| 4c | Dépense | H@`README.md` l.157 ; v3@`docs/agent_billing.md` l.38-39 ; `docs/pipeline.md` l.296-301 | `Headless does not impose a local dollar cap` ; `operational telemetry, not an authenticated billing or spending-limit system` | Aucun plafond en dollars, aucun nombre maximal de tours passé à `claude` (recherche négative). Registre de coût = télémétrie. Headless : au plus 5 exécutions par appel (H@README l.198-199). | **à corriger hors de v3** : plafond 402 du relais par course, plus plafond de l'espace de travail chez Anthropic |
| 5a | OpenAI (relecture) activée par le préréglage | `configs/preset/paper.yaml` l.12 | `phases: task_drafting,investigation,ablations,final_evaluation,posthoc,paper,review,revision` | **`preset=paper` active `review`**, qui envoie le manuscrit à OpenAI ; RS § 2 l'ignore. | **à configurer** : ne pas utiliser `preset=paper`, ou poser `execution.phases=` explicitement sans `review` |
| 5b | Figures de concept | `concept_figure.sh` l.603-616, l.618-626, l.672-675 ; Dockerfile l.116-118 | `--enhance-model gpt-image-2 --audit-vlm gpt-5.5` ; repli Gemini ; `claude) printf 'claude-opus-5-5'` | Sans clé OpenAI ni Gemini : export simple. L'agent de figures appelle Claude avec un **modèle figé `claude-opus-5-5`** : à mettre dans la liste du relais, sinon figures en échec non bloquant. | **à configurer** |
| 5c | Bedrock | `container_agent.sh` l.1212-1221 ; H@`src/billing.ts` l.65-77, l.120-136 | `-e CLAUDE_CODE_USE_BEDROCK=1` si `AWS_ACCESS_KEY_ID` et `AWS_SECRET_ACCESS_KEY` dans le fichier | Activé seulement par des clés AWS présentes. | **sûr** si aucune variable `AWS_*` |
| 5d | Autres appels | H@`src/models-dev.ts` l.131-133, l.183-204 ; `container_agent.sh` l.976 ; `pyproject.toml` l.40 ; Dockerfile l.79, l.138 | `HEADLESS_MODELS_DEV_CACHE=` (vide) ; `scholarly==1.7.11` ; `curl -fsSL https://cursor.com/install \| bash` | Headless lit les tarifs sur models.dev à chaque appel (cache désactivé par v3) : coût estimé absent si refusé, sans gravité. Google Scholar par `scholarly` : Web ouvert, journalisé. Cursor, npm, miroirs Debian, GitHub : **à la construction de l'image seulement**. | **sûr** (journalisé) |
| 6a | Image | Dockerfile l.1-3, l.56-61, l.63-77, l.128-141 | `FROM node:22-bookworm-slim` ; `FROM python:3.12-slim` ; `@google/gemini-cli` sans version ; `USER agent` | Une seule image `agentic-scientist/agent-cli:latest`. Images de base et Gemini non épinglées par empreinte ; installateur Cursor par `curl \| bash`. Aucun `ENV` d'adresse. | **à configurer** : construire une fois, consigner l'empreinte de l'image (R9) |
| 6b | Privilèges | `container_agent.sh` l.1169-1177, l.1547-1552 | `docker run -d --rm --init --name … --user "$(id -u):$(id -g)" --network …` | Ni `--privileged`, ni `--cap-add`, ni périphérique (recherche négative) ; utilisateur de l'hôte. Mais ni `--cap-drop`, ni `no-new-privileges`, ni limite de processus pour les **agents** ; l'évaluateur, lui, les a (`task_runtime.py` l.592-606 : `--read-only --cap-drop ALL --security-opt no-new-privileges --pids-limit 4096`). | **à configurer** : démon en `userns-remap` ou sans racine, `"no-new-privileges": true` dans `daemon.json` |
| 6c | Socket Docker | `container_agent.sh` l.268-277, l.1178-1185 ; `run.sh` l.352 ; `idea.sh` l.370 | `case "${AGENT_CONTAINER_MOUNT_DOCKER_SOCK:-0}"` ; `export AGENT_CONTAINER_MOUNT_DOCKER_SOCK=0` | Monté seulement si la variable vaut 1 ; forcé à 0 par les phases lues. | **sûr** (à vérifier à l'essai : `ls /var/run/docker.sock` dans chaque conteneur) |
| 6d | Montages | `container_agent.sh` l.415-432, l.473-497, l.1203-1208, l.1227-1232 | `-v "$container_mount_root:/workspace"` ; `-v "$container_home_dir:/home/agent-home"` ; `/dev/null:…:ro` | Espace de travail en écriture, foyer sous le dossier de course, dossier temporaire, montages supplémentaires choisis par la phase ; fichiers scellés masqués par `/dev/null`. Aucun montage de `~` de l'hôte (copie seulement, 3b). | **sûr** si `auth_root` vide et `AGENTIC_TEMP_ROOT` sous un disque dédié |

## 2. Architecture réseau retenue pour le devis (correction de RS § 3)

- **Réseau interne sans route** (`internal: true`, nouveau nom, par exemple `agsci-interne-v1`) pour tous les conteneurs de phase (`container.network` et `posthoc.container.network`), plus `AGENT_CONTAINER_DISABLE_HOST_GATEWAY=1`.
- **Mandataire de sortie transparent et journalisé** (par exemple mitmproxy en mode inverse ou transparent selon le nom annoncé, sous TLS — sécurité de la couche de transport), seul membre à deux pattes. Pour que les outils qui ignorent `HTTPS_PROXY` (2d, 1d) passent quand même : la **résolution de noms** du réseau interne renvoie l'adresse du mandataire pour tout nom (serveur de noms dédié sur le réseau interne, ou résolveur du démon pointé dessus), le mandataire relit le nom demandé et sort. `HTTPS_PROXY` reste posé dans les réglages gérés pour Claude Code. Autorité du mandataire dans l'image dérivée : `NODE_EXTRA_CA_CERTS` (gardée même par l'effacement des figures, concept_figure.sh l.660), magasin du système, `pip.conf`.
- **Règle unique de blocage** : préfixe `github.com/lciric/controle-ia` (et ses formes `raw.githubusercontent.com/lciric/controle-ia…`, `api.github.com/repos/lciric/controle-ia…`, `codeload.github.com/lciric/controle-ia…`), en préfixe de chemin, insensible à la casse ; refus journalisé. Refus aussi de `api.anthropic.com`, `api.openai.com`, `*.amazonaws.com` (bedrock) : ce ne sont pas le Web des agents mais des contournements du relais.
- **Passe-relais** : sur le réseau interne, nom unique `relais`, qui ne transmet qu'à **une adresse** (le relais réel, § 4) ; c'est la valeur de `ANTHROPIC_BASE_URL` dans les réglages gérés.
- **Pare-feu de l'hôte** (chaînes `DOCKER-USER` et `INPUT`, IPv4 et IPv6) : refuser 169.254.0.0/16, 10/8, 172.16/12, 192.168/16, 100.64/10, l'adresse et la passerelle de l'hôte ; IPv6 coupé dans Docker ; seule sortie permise : le mandataire et le tunnel du relais.
- **Image dérivée** (nouveau nom, R12) : fichier de réglages gérés de Claude Code (chemin système Linux SUPPOSÉ `/etc/claude-code/managed-settings.json`, à vérifier sur 2.1.285) avec `ANTHROPIC_BASE_URL=http://relais:…`, modèles par défaut (dont le modèle de fond) dans la liste du relais, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, `HTTPS_PROXY` ; autorité du mandataire. Aucune ligne du code Python de v3 ne change.
- **Lancement** : `agsci run <tâche> container.network=agsci-interne-v1 posthoc.container.network=agsci-interne-v1 container.auth_root=<vide> container.env_file=<fichier de course> container.image=<image dérivée> execution.phases=task_drafting,investigation,ablations,final_evaluation,posthoc,paper investigation.execution.workers=2 investigation.execution.max_idea_cycles=<N>` ; `timeout` de l'hôte autour.

## 3. Devis

### 3.1 Dimensionnement (tiré du code et de l'article)

- **Processeurs** : 16 virtuels. Pièces : l'article donne « 8 CPU cores, 30 min » par itération de recherche pour sa tâche sur processeur (PDF p.11, tableau 3) ; 2 ouvriers (p.18 ; `investigation.execution.workers`) → 16. Variante économique : 8 avec 1 ouvrier.
- **Mémoire** : 32 à 64 Go (SUPPOSÉ ; aucune pièce ; les gabarits à 16 processeurs en ont 64).
- **Disque** : 200 Go au moins. Pièces : plafond de l'historique de course 16 Gio (`configs/config.yaml` l.100, `max_total_bytes: 17179869184`) ; environnement de tâche jusqu'à 16 Gio (`max_runtime_bytes: 17179869184`, l.62) ; image avec Chromium, TeX Live, Draw.io et deux environnements Python (Dockerfile l.41-53, l.85-124) ; journaux du mandataire avec corps.
- **Durée** : article p.11 : 20 itérations par course, 30 min par itération sur processeur ; plus idées (≤ 3 000 s chacune au préréglage, `paper.yaml` l.19), ablations (variantes ≤ 7 200 s), post-hoc, article (≤ 7 200 s). Estimation (inférence) : **course de 20 cycles ≈ 30 h** marge comprise ; course courte de 5 cycles ≈ 10 h ; **essai à blanc et construction de l'image ≈ 6 h** (une fois).

### 3.2 Machines louées (prix publics, hors taxes, consultés le 30 octobre 2026 entre 07:49 et 07:51 UTC ; aucun compte créé)

| Fournisseur | Machine de travail | Prix horaire | Machine relais (option B, § 4) | Page |
|---|---|---|---|---|
| **Hetzner Cloud** | CCX43 : 16 processeurs AMD dédiés, 64 Go, 360 Go NVMe | 0,4431 EUR/h (plafond 276,49 EUR/mois) ; CCX33 (8, 32 Go, 240 Go) : 0,2227 EUR/h | CPX22 : 2 processeurs, 4 Go, 80 Go : 0,0320 EUR/h | `https://www.hetzner.com/cloud/general-purpose/`, `…/regular-performance/` (page : « Price incl. IPv4 » ; certains produits marqués « currently unavailable » : disponibilité à confirmer) |
| **DigitalOcean** | General Purpose : 16 processeurs, 64 Gio, 200 Gio | 0,75 USD/h ; 8 processeurs, 32 Gio, 100 Gio : 0,375 USD/h (+ volume 100 Gio : 10 USD/mois) | Basic 1 processeur, 2 Gio : 0,01786 USD/h | `https://www.digitalocean.com/pricing/droplets`, `…/pricing/volumes` |
| **Scaleway** | POP2-16C-64G : 16 processeurs, 64 Go | 0,59 EUR/h + bloc 200 Go × 0,000130 EUR/Go/h = 0,026 → **0,616 EUR/h** ; POP2-8C-32G : 0,29 EUR/h | non relevé (relais possible chez Hetzner) | `https://www.scaleway.com/en/pricing/virtual-instances/`, `…/pricing/storage/` (adresse IPv4 publique exclue du prix, non relevée) |

Les trois offrent des machines virtuelles complètes (démon Docker, `iptables`), facturées à l'heure, détruisables par interface de programmation. Aucune carte graphique.

| Coût machine (travail + relais B) | Hetzner (EUR) | DigitalOcean (USD) | Scaleway + relais Hetzner (EUR) |
|---|---|---|---|
| par heure | 0,4751 | 0,7679 | 0,648 |
| essai à blanc (6 h) | 2,85 | 4,61 | 3,89 |
| course de 20 cycles (30 h) | 14,25 | 23,04 | 19,44 |
| **par cycle** (1,5 h) | **0,71** | **1,15** | **0,97** |
| **trois courses + essai** | **45,60** | **73,72** | **62,21** |

### 3.3 Appels au modèle (non opposable)

- **Pièce vérifiée** : PDF p.19, figure 16, panneau « Cost evolution » (lu sur rendu de la page) : courbe Opus-4.7 + Claude Code ≈ **430 USD cumulés à environ 50 cycles** ; Codex ≈ 180 ; Pi ≈ 90 ; légende : « cumulative API cost per evolution cycle », « three seeds per agent » ; bande ombrée = dispersion entre graines, ce qui suggère une courbe **par course** (moyenne), pas un cumul des trois graines (inférence). Tâche GRPO sur cartes graphiques, **phase d'investigation seule**. → **≈ 8,6 USD par cycle**, lecture de figure, **non opposable** (R7 : pas de chiffre au texte).
- Hypothèse pour les autres phases (rédaction de tâche, ablations, post-hoc, article, figures) : **+50 % à +100 %** du coût d'investigation (SUPPOSÉ, aucune pièce).
- Notre tâche est sur processeur ; le modèle choisi peut différer d'Opus 4.7 ; le barème du modèle retenu est à relever sur la page de prix d'Anthropic avant le GO.

| Scénario | Investigation | Course entière (×1,5 à ×2) |
|---|---|---|
| Essai à blanc (amont factice, puis 1 cycle réel) | ≈ 9 | 9 à 17 |
| Course courte, 5 cycles | ≈ 43 | 65 à 86 |
| **Course de 20 cycles** | ≈ 172 | **258 à 344** |
| **Trois courses de 20 cycles** | ≈ 516 | **774 à 1 032** |

### 3.4 Total

- **Par cycle, tout compris** : 12,9 à 17,2 USD de modèle + 0,7 à 1,2 de machine ≈ **14 à 18 USD**. La machine pèse moins de 8 %.
- **Trois courses de 20 cycles + essai** : 774 à 1 032 + 9 à 17 USD de modèle, + machine 45,60 EUR (Hetzner ; taux de change non consulté, hypothèse 1 EUR ≈ 1,15 USD → ≈ 52 USD) ≈ **835 à 1 100 USD**. Avec DigitalOcean : ≈ 855 à 1 125 USD.
- **Trois courses courtes (5 cycles, 10 h) + essai** : modèle 204 à 275 USD + machine 17,10 EUR (≈ 20 USD) ≈ **225 à 295 USD**.
- Plafond du relais par course : à fixer **après** la mesure d'un cycle à l'essai à blanc (RS § 9 point 8) ; proposition : 2 × (coût mesuré d'un cycle × N cycles × 2). Second plafond indépendant : limite de dépense de l'espace de travail de la clé chez Anthropic.

## 4. Point à trancher : comment la machine louée joint le relais sans que la clé soit lisible

Contraintes lues : la clé n'est jamais sur la machine de travail ; les agents sont en `--allow yolo` (README l.40-45) et voient tout ce qui est sur le réseau interne ; ils ne voient que `relais` (passe-relais) et le mandataire ; le jeton de course (`ANTHROPIC_AUTH_TOKEN`) est lisible par eux par construction — il ne doit ouvrir que le relais, plafonné et révocable.

| Option | Principe | Avantage | Inconvénient |
|---|---|---|---|
| **A. Tunnel vers le relais de la session** | La session (qui tient la clé) ouvre un tunnel **sortant** vers la machine louée (shell sécurisé avec renvoi inverse, ou tunnel chiffré sur 443) ; sur la machine, le bout du tunnel n'écoute que pour le passe-relais | aucune machine ni compte de plus ; clé jamais hors de la session | la session est **éphémère** (une course dure ~30 h) : coupure = course perdue ; la session ne peut recevoir aucune connexion entrante, donc dépend d'une sortie autorisée vers une adresse de machine louée (non vérifiée ; l'outil de lecture Web de cette session refuse déjà des domaines) ; la session doit détenir une clé d'accès à la machine |
| **B. Relais sur une seconde machine louée** (recommandée) | Petite machine (CPX22, 0,032 EUR/h) qui porte la clé **dédiée** (espace de travail Anthropic à plafond de dépense, révocable) et le relais (liste des modèles, plafond 402 par jeton, trace) ; la machine de travail la joint par tunnel chiffré (WireGuard) **d'une seule adresse source** ; aucun accès de la machine de travail à la machine relais autre que le port du relais | indépendante de la vie de la session ; trace et plafond hors de portée des agents ; un seul point d'entrée ; même fournisseur, même réseau privé possible | une machine et une clé de plus à garder (surface chez le fournisseur) ; la clé vit sur une machine louée, d'où clé dédiée et plafonnée ; un compte chez le fournisseur (nœud) |
| C. Passerelle gérée d'un tiers | Relais hébergé par un service tiers (fonction de périphérie) qui garde la clé dans son coffre | aucune machine relais à tenir | compte et tiers de plus ; trace chez un tiers ; contrat et données hors du programme |
| (exclue) Relais sur la machine de travail | — | — | clé sur la machine : contraire au mandat |

**Recommandation : B**, confiance **0,65**. Raisons : la durée d'une course dépasse la vie sûre d'une session ; la session ne reçoit rien en entrée ; B garde la clé hors de la machine de travail et hors de portée des agents tout en survivant à la session. Garde-fous : clé dédiée dans un espace de travail plafonné ; jeton de course plafonné et révoqué en fin de course ; pare-feu de la machine relais n'acceptant que l'adresse du tunnel ; trace du relais rapatriée et scellée avec le journal du mandataire (R6). **A reste utile pour l'essai à blanc court** (amont factice, 1 cycle), si la sortie de la session vers la machine est permise.

## 5. Décision pour Lazar

**Décision** : où tourne le relais qui tient la clé pendant les courses de v3.
**Enjeu** : faire tourner v3 intacte, Web ouvert, plusieurs heures, sans que la clé soit jamais lisible par les agents ni par la machine de travail, avec un plafond de dépense hors de leur portée.

| Option | Avantage | Inconvénient |
|---|---|---|
| (A) Tunnel vers le relais de la session | rien à louer de plus ; clé reste dans la session | course perdue si la session tombe ; sortie de la session vers la machine non vérifiée |
| (B) Relais sur une seconde petite machine louée, clé dédiée plafonnée | robuste sur 30 h ; plafond et trace hors de portée ; ≈ 1 EUR par course | un compte, une clé dédiée et une machine de plus à garder |
| (C) Passerelle gérée d'un tiers | aucune machine relais | tiers, compte, trace hors du programme |

**Recommandation : (B)**, (A) seulement pour l'essai à blanc. Confiance 0,65.
**Pas de défaut à 48 heures** : compte chez un fournisseur, clé et dépense sont des nœuds ; attendre le GO sur devis (≈ 225 à 295 USD pour trois courses courtes, ≈ 835 à 1 100 USD pour trois courses de 20 cycles, essai à blanc compris ; non opposable avant mesure).

## 6. Réserves

- Estimations de durée, de mémoire, de part des autres phases et de taux de change : SUPPOSÉES ; coût par cycle lu sur une figure (tâche à cartes graphiques, Opus 4.7, investigation seule).
- Comportements de Claude Code 2.1.285 (réglages gérés comme fichier qui survit à l'effacement d'environnement, en-tête du jeton `ANTHROPIC_AUTH_TOKEN`) et de Node 22 (mandataire ignoré par `fetch`) : SUPPOSÉS, à éprouver à l'essai à blanc (RS § 9).
- Effet du retrait de `ANTHROPIC_API_KEY` par Headless (1f) : lu dans le code, non observé.
- Variantes, post-hoc en Python et courtier de l'évaluateur non lus : d'autres `docker run` peuvent exister ; l'essai à blanc doit lister tous les conteneurs créés (`docker events`) et vérifier réseau, montages et environnement de chacun.
- Prix publics du jour, hors taxes, susceptibles de changer ; disponibilité des gabarits Hetzner non confirmée.

Version 1 ; jamais réécrite (R12).
