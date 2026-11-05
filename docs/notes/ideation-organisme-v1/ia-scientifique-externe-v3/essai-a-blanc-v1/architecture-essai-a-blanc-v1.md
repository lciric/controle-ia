# Essai à blanc de l'Agentic Scientist v3 — architecture, scripts, épreuves, devis — v1

Lignée session-depot (instance 2), 30 octobre 2026, à partir de 08:06 UTC (`date -u`). Mandat : R-808 (mot de Lazar « 1 puis 3 » :
essai à blanc, puis une course de 5 cycles), R-806 (option (a) : relais sur une seconde machine), R-561 (blocage de
`lciric/controle-ia`). **Rien n'a été loué, aucun compte créé, aucune API appelée, aucune clé lue ni écrite.**
Base : `../lecture-code-et-devis-v3-v1.md` (`1ce823a7…`, abrégée **LC**) et la revue d'architecture de conv-audit qu'elle cite
(`revue-surete-v3-v1.md`, `b12fc9cb…`, abrégée **RS**).

## 1. Architecture (option (a))

```
            Internet (Web des agents, ouvert sauf deux refus)
                 ▲ 80/443 seulement
   ┌─────────────┼──────────────────────── machine A (agents) ────────────────────────────┐
   │   agsci-sortie-v1 172.31.0.0/24 (avec route)                                         │
   │     mandataire-v1 172.31.0.2 ────┐            passe-relais-v1 172.31.0.3 ──► wg0 ──┼──► B 10.77.0.1:8790
   │                                  │                       │                          │
   │   agsci-interne-v1 172.30.0.0/24 (internal : aucune route)                           │
   │     mandataire 172.30.0.2   relais 172.30.0.3   dns 172.30.0.4                       │
   │     conteneurs de la v3 (agents, tâche, évaluateur, figures, article)               │
   └───────────────────────────────────────────────────────────────────────────────────────┘
   ┌──────────────── machine B (relais) ────────────────┐
   │ wg0 10.77.0.1 ; relais_factice_v1.py :8790          │  essai à blanc : réponses factices, aucun appel amont
   │ entrée : WireGuard depuis A, SSH depuis Lazar       │  course réelle : relais réel, clé dédiée plafonnée
   └─────────────────────────────────────────────────────┘
```

- **Machine A** (`machine-a/mise-en-place-machine-a-v1.sh`) : Docker en espace d'utilisateurs remappé, `no-new-privileges`,
  IPv6 coupé. Deux réseaux :
  - `agsci-interne-v1`, `internal`, sans aucune route, où tournent tous les conteneurs de la v3 ;
  - `agsci-sortie-v1`, sur lequel seuls le mandataire et le passe-relais ont une patte.
- **Serveur de noms** (`machine-a/dnsmasq-interne-v1.conf`) : tout nom renvoie l'adresse du mandataire, sauf `relais` et
  `mandataire`. Ainsi les outils qui ignorent `HTTPS_PROXY` passent quand même par le mandataire (LC, points 1d et 2d) :
  l'installation des dépendances de la tâche, le `fetch` de Node, les figures après effacement d'environnement.
- **Mandataire transparent journalisé** (mitmproxy, greffon `machine-a/mandataire_addon_v1.py`, règles
  `machine-a/mandataire_regles_v1.py`).
  - Il reprend la vraie destination dans le nom TLS annoncé ou dans l'en-tête `Host`.
  - Il refuse la future copie publique : préfixe `/lciric/controle-ia` sur les hôtes de GitHub, sans égard à la casse, aux
    barres doublées ni à l'encodage ; `/repos/lciric/controle-ia…` et les recherches sur l'interface de GitHub.
  - Il refuse aussi les appels directs aux fournisseurs de modèles (Anthropic, OpenAI, Codex, Bedrock, Gemini), qui
    contourneraient le relais.
  - Il journalise chaque requête (hôte, chemin, méthode, statut, motif), sans les corps.
- **Passe-relais** : il ne transmet qu'à une seule adresse, B:8790, par le tunnel WireGuard.
- **Pare-feu** (`machine-a/pare-feu-machine-a-v1.rules`, syntaxe validée ici par `iptables-restore --test`) :
  - seuls le mandataire (80 et 443) et le passe-relais (B:8790 par `wg0`) sortent ;
  - les adresses de métadonnées et les réseaux privés sont refusés ;
  - en entrée : SSH depuis Lazar, WireGuard depuis B ; IPv6 refusé.
- **Image dérivée** (`machine-a/image-derivee/Dockerfile`, `managed-settings.json`) :
  - le code de la v3 est intact ; l'image part de celle construite aux commits épinglés, dont l'empreinte est consignée (R9) ;
  - elle ajoute les réglages gérés de Claude Code : adresse du relais, mandataire, trafic non essentiel coupé, mise à jour
    automatique coupée ;
  - elle ajoute l'autorité du mandataire (système, Node, pip).
  - Chemin des réglages gérés : SUPPOSÉ `/etc/claude-code/managed-settings.json` (LC § 2) ; à éprouver (E5).
- **Configuration de la v3** (`machine-a/lancer-essai-a-blanc-v1.sh`) :
  - `container.network` et `posthoc.container.network` sur le réseau interne ;
  - `container.auth_root` vers un dossier vide dédié (LC 3b) ;
  - aucun `.env` à la racine (LC 3a) ;
  - jeton de course seulement, par `ANTHROPIC_AUTH_TOKEN` (LC 1f), dans un fichier en mémoire vive effacé à la fin ;
  - **phases explicites, sans `review`** : pas d'OpenAI, pas de préréglage `paper` (LC 5a) ;
  - `AGENT_CONTAINER_DISABLE_HOST_GATEWAY=1`, `AGENT_CONTAINER_MOUNT_DOCKER_SOCK=0` ;
  - 1 cycle, 1 ouvrier, `timeout` de 2 h sur l'hôte.
- **Machine B** (`machine-b/mise-en-place-machine-b-v1.sh`) :
  - WireGuard, et un pare-feu qui n'accepte le relais que depuis A, par le tunnel ;
  - **relais factice** `machine-b/relais_factice_v1.py`, qui n'appelle jamais Anthropic et ne porte aucune clé. Il vérifie :
    - le jeton de course, par empreinte et à temps constant ;
    - la liste des modèles, et un plafond fictif (402 au-delà) ;
    - il tient un journal sans jeton ni corps.
- **Destruction** (`detruire-machines-v1.sh`) : par identifiant seulement (R10), à consigner dans `registres/arrets.md`.

Le jeton de course **n'est pas une clé**. Il n'ouvre que le relais : factice ici, plafonné et révocable pour la course réelle.
Les agents peuvent le lire par construction (LC § 4), c'est pourquoi le plafond est sur B, hors de leur portée.

## 2. Ce qui a été éprouvé ici (sans aucun appel externe)

| Pièce | Essai | Résultat |
|---|---|---|
| Règles du mandataire | `essais/test_essai_a_blanc_v1.py`, classe `Regles` : 12 formes de la copie publique refusées (casse, `//`, `%2F`, `%252F`, `controle-ia-travail`, `.git`, recherche par l'interface) ; 6 fournisseurs refusés ; 7 cas sains permis | **OK** (1 défaut trouvé et corrigé : la recherche `/search/code?q=user:lciric` passait, car la requête était retirée avant le test) |
| Relais factice | même fichier, classe `RelaisFactice`, serveur sur 127.0.0.1 : jeton absent ou faux → 401 ; modèle non permis → 403 ; chemin inconnu → 404 ; réponse entière et flux d'événements au format attendu ; plafond fictif atteint → 402 ; journal sans jeton ni texte ; refus d'écouter sur toutes les adresses ; refus d'un jeton trop court | **OK**, 7 essais sur 7 (`python3 -I -B essais/test_essai_a_blanc_v1.py`) |
| Greffon mitmproxy | importable sans mitmproxy (la logique est dans les règles, essayées à part) | **OK** ; son comportement réel sous mitmproxy n'est **pas** éprouvé ici (mitmproxy absent) |
| Pare-feu | `iptables-restore --test pare-feu-machine-a-v1.rules` | **OK** (syntaxe) |
| Scripts | `bash -n` sur les cinq scripts ; `managed-settings.json` lu comme JSON | **OK** (syntaxe) |
| Image dérivée, mandataire en conteneur | — | **non éprouvés** : le démon Docker n'existe pas dans ce conteneur (aucune socket), et la construction de l'image de la v3 tirerait des paquets du Web. Ce sont les épreuves E1, E5 et E8, sur A. |

## 3. Épreuves de l'essai à blanc (`machine-a/verifier-epreuves-v1.sh`)

Une seule épreuve échouée interdit la course réelle (étape 3).

| n° | Épreuve | Réussite | Échec |
|---|---|---|---|
| E1a | Aucun accès direct au Web hors du mandataire | depuis un conteneur du réseau interne, une connexion directe à une adresse IP échoue (aucune route) | la connexion aboutit |
| E1b | Le Web passe par le mandataire | une requête à `example.com` aboutit **et** apparaît dans le journal du mandataire | elle échoue (le schéma par résolution de noms ne marche pas : voir réserve 1), ou elle aboutit sans ligne au journal |
| E2 | `lciric/controle-ia` bloqué | quatre formes (GitHub, casse, `raw`, interface) rendent 403 ; `SakanaAI/AI-Scientist-v3` passe | une forme passe, ou le cas sain est refusé |
| E3 | Aucun identifiant de l'hôte dans les conteneurs | ni `~/.claude`, ni `~/.codex`, ni variable `AWS_*`, `OPENAI*`, `GEMINI*`, `CLAUDE_CODE_OAUTH*`, `ANTHROPIC_API_KEY`, ni socket Docker | un seul présent |
| E4 | Aucun appel à OpenAI | aucune ligne permise vers OpenAI, Codex, Anthropic, Bedrock ou Gemini au journal du mandataire ; pas de phase `review` au journal de la v3 | une ligne permise, ou la phase lancée |
| E5 | Tous les appels de modèle passent par B | le journal du relais factice (rapatrié de B) contient les appels de la v3 ; aucun appel direct vu par le mandataire (E4) | aucun appel vu par B : les réglages gérés ne sont pas lus (chemin SUPPOSÉ), ou Headless a pris une autre voie (LC 1e) |
| E6 | Le plafond de B tient | au-delà du plafond fictif (2 USD fictifs à 0,05 par appel, donc 40 appels), B rend 402 | aucun 402 |
| E7 | Destruction | `detruire-machines-v1.sh` par identifiant ; `hcloud server list` vide ; identifiants dans `registres/arrets.md` | une machine reste |
| E8 | Chaque conteneur créé est confiné | tout conteneur vu par `docker events` est sur `agsci-interne-v1`, sans `--privileged`, sans socket Docker | un seul hors de ces règles (LC § 6 : des `docker run` non lus peuvent exister) |

## 4. Devis (prix relevés par LC § 3.2, Hetzner, hors taxes, le 30 octobre 2026 ; 1 EUR ≈ 1,15 USD SUPPOSÉ)

| Étape | Machines | Modèle | Total |
|---|---|---|---|
| **(1) Essai à blanc** : A en CCX43 (0,4431 EUR/h) et B en CPX22 (0,0320 EUR/h) ; 6 h, construction de l'image comprise | 6 × 0,4751 = **2,85 EUR ≈ 3,3 USD** | **0** (relais factice) | **≈ 3,3 USD**, avec une marge à 5 USD si l'essai dure 10 h |
| **(3) Course de 5 cycles**, même montage, relais réel | 10 h × 0,4751 = 4,75 EUR ≈ 5,5 USD | 65 à 86 USD (LC § 3.3, lecture d'une figure, **non opposable**) | **≈ 70 à 92 USD** |

- Plafonds proposés pour l'étape 3 : relais réel à 90 USD ; limite de dépense de l'espace de travail de la clé dédiée,
  chez Anthropic, à 100 USD (second plafond, indépendant).
- L'essai à blanc mesure la durée réelle de construction et de mise en place, pas le coût par cycle : celui-ci ne sera
  mesuré qu'au premier cycle réel de l'étape 3, avec les plafonds ci-dessus.

## 5. Ce qui revient à Lazar avant tout

1. **Compte chez le loueur** (Hetzner proposé : le moins cher relevé ; disponibilité des gabarits à confirmer). C'est un
   nœud de compte : la session n'en crée aucun.
2. **Création des deux machines** et du jeton d'accès du loueur (`HCLOUD_TOKEN`), qu'il garde. Les identifiants des machines
   sont consignés par la session.
3. **Pour l'étape 3 seulement : la clé Anthropic dédiée**, dans un espace de travail plafonné (100 USD proposés), posée par
   lui à la main sur B, par variable. Elle n'est jamais dans un fichier, ni sur A, ni dans le dépôt.
4. **Un GO par étape**, sur devis : (1) environ 5 USD ; (3) environ 92 USD. L'étape 3 ne part que si les épreuves E1 à E8
   sont toutes réussies.
5. **Relecture des scripts** de ce dossier avant exécution ; leur exécution sur A et B est faite par Lazar, ou par la
   session sur son mot.

## 6. Réserves

1. **Mandataire transparent par résolution de noms** : la reprise de destination par le nom TLS est SUPPOSÉE pour la version
   de mitmproxy retenue (11.0.2, non épinglée par empreinte). Sur un réseau `internal`, Docker peut aussi ne pas transmettre
   les requêtes de noms au serveur `dns` du démon. Ce sont les épreuves E1b et E8. Si E1b échoue, repli : serveur de noms
   déclaré par conteneur, ou passage du mandataire en mode WireGuard sur A.
2. Les images d'appoint (dnsmasq, mitmproxy, socat) sont citées par étiquette : à épingler par empreinte avant usage (R9).
3. Chemin des réglages gérés de Claude Code et effet du retrait de `ANTHROPIC_API_KEY` par Headless : SUPPOSÉS (LC § 6),
   éprouvés par E5.
4. Avec un relais factice, les phases de la v3 échoueront faute de vrai contenu. L'essai éprouve la plomberie, pas la
   science : c'est voulu.
5. Durée de 6 h et taux de change : SUPPOSÉS.

Version 1 ; jamais réécrite (R12).
