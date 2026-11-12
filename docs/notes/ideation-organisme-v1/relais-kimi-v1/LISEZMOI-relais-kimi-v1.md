# Relais Kimi local, version 1

Lignée session-depot, 30 octobre 2026. Sous-agent ingénieur. **Aucun appel réel, aucune clé lue** : les essais tournent contre un faux amont local.

## Ce que c'est

`relais_kimi_v1.py` est un petit serveur HTTP qui tourne dans son propre processus, sur `127.0.0.1` seulement. Il relaie `POST /v1/chat/completions` vers l'API Moonshot (Kimi, compatible OpenAI). Il tient la clé et la liste des modèles permis (barrière R-764), avec un plafond en dollars. Bibliothèque standard seulement. Il suit le modèle de `lancement-v2/relais_gemini_v1.py` (bornes, journal, mandataire) et du relais Claude `orchestrateur-v50/arbre/pole/relais_reel.py` (plafond, réserve par appel, modèles permis).

## Lancement (arrêt par PID, R10)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$CLE" HTTPS_PROXY="$HTTPS_PROXY" \
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B relais_kimi_v1.py --port 8789 \
    --modeles-permis <identifiant-exact> --plafond-usd <plafond> \
    --prix-entree <p> --prix-sortie <p> --prix-cache <p> --max-appels 64 \
    --journal $DOS/relais-kimi-journal-v1.jsonl > $DOS/relais-kimi-v1.log 2>&1 &
echo $! > $DOS/relais-kimi.pid
```

- Le lancement n'utilise **ni `setsid` ni `nohup`** (incident du 30 octobre). `env -i` remplace son processus par Python sans changer de PID, donc `$!` est le PID du relais. `GET /relais/etat` rend ce `pid` : il faut le comparer au fichier `.pid` avant `kill <pid>`. Un essai le vérifie.
- Le client n'a besoin d'aucune clé. Si son outil en exige une, il lui donne une valeur factice : le relais retire `Authorization` et `x-api-key` et pose `Authorization: Bearer <clé>`.

## Variables et options

| Variable ou option | Rôle |
|---|---|
| `KIMI_API_KEY` (ou celle que nomme `--variable-cle`) | Clé, lue une fois au démarrage puis effacée de `os.environ`. Jamais passée en argument ni écrite dans un fichier ou le journal. |
| `HTTPS_PROXY` / `https_proxy`, `SSL_CERT_FILE` | Mandataire et certificats de l'environnement du relais. |
| `--amont` | Par défaut `https://api.moonshot.ai`. N'accepte que `https`, ou `http` vers la boucle locale pour les essais, sans chemin. |
| `--modeles-permis` (obligatoire) | Noms exacts séparés par des virgules. Tout autre modèle reçoit 403, et le refus est compté en `refus_modele`. |
| `--plafond-usd` (obligatoire), `--reserve-par-appel` (0,40) | Plafond tenu par le relais. Chaque appel réserve `max(réserve, pire cas de la requête)`. Au-delà du plafond : 402. |
| `--prix-entree`, `--prix-sortie`, `--prix-cache` (obligatoires) | Prix en USD par million de jetons. Aucun défaut. |
| `--max-jetons-sortie-pire-cas` (262 144) | Jetons de sortie supposés quand la requête ne porte pas `max_tokens`. |
| `--max-appels` (64), `--max-octets-corps` (4 000 000) | Au-delà : 429 et 413, sans rien envoyer à l'amont. |
| `--journal` | Une ligne JSON par appel, sans texte ni clé. |

## Barrières

- **Chemins** : seuls `POST /v1/chat/completions` et `GET /relais/etat` sont servis, comparés à la cible brute de la ligne de requête. Tout autre chemin, méthode ou chaîne de requête reçoit 403.
- **Modèle servi** : le relais compare le champ `model` d'une réponse 200 au modèle demandé, par égalité exacte. En cas d'écart, de champ absent ou de réponse illisible, il compte un refus de modèle : la réponse n'est **pas relayée** (502), mais sa dépense est portée au compteur.
- **Flux refusé** (`stream` vrai : 400). Trois raisons :
  1. la barrière du modèle servi doit lire `model` avant de rendre quoi que ce soit ;
  2. en flux, `usage` n'arrive qu'à la fin, et seulement avec `stream_options.include_usage` ;
  3. la réponse entière doit pouvoir être bornée.
- **Outils** : seul le type `function` est admis. Les fonctions intégrées (par exemple la recherche web) sont facturées hors de `usage`, donc le plafond ne les verrait pas.
- **Coût** :
  - formule : `(prompt − cache) × entrée + cache × prix_cache + completion × sortie` ;
  - les jetons sans case (cache au-delà de `prompt_tokens`, ou `total_tokens` au-delà de la somme) sont comptés au prix le plus fort ;
  - si `usage` est absent ou illisible, ou si la connexion est coupée après l'envoi, l'appel compte au pire cas : `(octets du corps + 1024) × entrée + max_tokens × n × sortie`.

## À vérifier avant tout GO (réserves)

1. **Adresse de l'amont.** `https://api.moonshot.ai/v1` (mondiale ; `api.moonshot.cn` pour la Chine, avec des clés propres à chaque plateforme) vient de la page officielle « Service Address », https://platform.kimi.ai/docs/api/overview. Je l'ai vue le 30 octobre 2026 **par extrait de moteur de recherche seulement**. `platform.kimi.ai` et `platform.moonshot.ai` sont hors des domaines permis de la session, donc WebFetch a échoué. Pour lire la page elle-même, il faut ajouter ces domaines dans les réglages réseau.
2. **Identifiant exact de « Kimi K3.1 Pro ».** Non vérifié. Les essais utilisent `kimi-k3.1-pro`, un nom **factice**. Il faut lire l'identifiant dans la liste officielle (`GET /v1/models`, une route que ce relais ne sert pas) et vérifier que la réponse rend le même nom dans `model`. Sinon, la barrière refusera tout.
3. **Prix.** Aucun n'est inscrit : entrée, sortie et lecture de cache sont à lire sur la page officielle des prix, à dater et à empreinter.
4. **Forme de `usage`.** Le cache est lu dans `usage.cached_tokens` ou dans `usage.prompt_tokens_details.cached_tokens`, et supposé compris dans `prompt_tokens` (convention OpenAI). C'est à confirmer. Les jetons de raisonnement sont supposés compris dans `completion_tokens`.
5. **Pire cas.** Il suppose qu'un jeton d'entrée fait au moins un octet du corps. Les images peuvent enfreindre cette hypothèse.
6. **Clé.** Effacer la variable de `os.environ` ne vide pas `/proc/<pid>/environ` : le même utilisateur peut encore y lire la clé tant que le relais vit (limite F-C7, reprise du relais Claude).

## Essais

Depuis la racine du dépôt :

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider docs/notes/ideation-organisme-v1/relais-kimi-v1/test_relais_kimi_v1.py
```

Résultat le 30 octobre 2026 : **72 réussis, 0 échec**, sur trois passes.
