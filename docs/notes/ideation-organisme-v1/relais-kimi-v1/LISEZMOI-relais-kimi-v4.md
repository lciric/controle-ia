# Relais Kimi v4 : recherche Web officielle de Moonshot — LISEZMOI

Lignée session-depot (sous-agent), 30 octobre 2026, vers 23:50 UTC. Demande du n° 263 de conv-audit (mot de Lazar relayé,
R-629) : Kimi K3.1 Pro lit les sources primaires de l'essaim de Navier-Stokes et des 722 manuscrits, **avec la recherche
Web intégrée de l'API Moonshot si elle existe**. **Aucun appel payant, aucune clé lue, aucune instance.** Ce dossier
complète les v1 à v3, qui restent inchangées (R12).

## 1. Ce que dit la documentation publique (lue le 30 octobre 2026)

Pages téléchargées par curl en lecture seule, copiées et empreintées dans `doc-moonshot-lue-2026-10-30-v1/`
(`EMPREINTES-doc-moonshot-v1.txt`). `platform.moonshot.ai` et `platform.moonshot.cn` redirigent (301) vers
`platform.kimi.ai` et `platform.kimi.com`.

**Verdict : il n'existe pas d'outil intégré `$web_search` dans la Chat Completions API actuelle. Il existe trois
équivalents, tous payés à l'appel, hors de `usage`.**

1. **Pas de `$web_search` en Chat Completions.** Le schéma `ToolDefinition` de https://platform.kimi.ai/docs/api/chat
   n'admet que `type: enum: - function` (`api_chat.md`). L'ancienne page `https://platform.kimi.ai/docs/guide/use-web-search`
   renvoie (308) vers « Best Practices for Web Search », qui ne décrit plus `$web_search`. Aucun `builtin_function` dans
   les pages lues (recherche par `grep`). Règle R8 : « absent des pages lues », pas « supprimé » (SUPPOSÉ : retiré).
2. **Outil officiel `web-search` par l'API Formula, dans Chat Completions** — https://platform.kimi.ai/docs/guide/use-official-tools
   (`guide_use-official-tools.md`). Citations exactes :
   - « When using official tools such as web search with `kimi-k3.1-pro`, use the Formula API official tools channel
     described on this page (OpenAI protocol, standard `function` tool); the example below has been verified with
     `kimi-k3.1-pro`. »
   - Quatre étapes : « 1. `GET /v1/formulas/{uri}/tools` — fetch the tool declarations (`uri` such as
     `moonshot/web-search:latest`); 2. `POST /v1/chat/completions` — send the tool declarations; the model returns
     standard `function`-type `tool_calls`; 3. `POST /v1/formulas/{uri}/fibers` — execute exactly what `tool_calls`
     specifies (`name` + `arguments` passed through verbatim; this step produces the tool\_call billing); 4.
     `POST /v1/chat/completions` — send the assistant message (with `tool_calls`) and the `role: "tool"` results to get
     the final answer. »
   - Déclaration rendue (exemple) : `{"type": "function", "function": {"name": "web_search", "description": "Search the
     web for information", "parameters": {"type": "object", "properties": {"query": {"description": "What to search
     for", "type": "string"}}, "required": [ "query" ]}}}`.
   - Résultat chiffré : « `web-search` was set as protected when created, so its result appears in the
     `context.encrypted_output` field […]; this content can be passed directly into the tool call. »
   - « you must return results for all `tool_calls` for the model to continue, otherwise the request will be considered
     invalid and rejected ».
   - **Donc le client fait la boucle et doit renvoyer les arguments tels quels** (étape 3), puis le résultat dans un
     message `tool` au `tool_call_id` aligné.
   - Prix (https://platform.kimi.ai/docs/pricing/websearch, tableau lu dans `pricing_websearch.html`) : « Formula API
     (web-search tool) » — `moonshot/web-search:latest` — « $0.005 / call » — « Charged per execution
     (`POST /v1/formulas/{uri}/fibers`) ». Jetons du modèle en plus : « When using web search via the Responses API or the
     Formula API, model input/output Tokens are still billed at the corresponding model pricing. »
   - Écart dans la page des prix : « On `kimi-k3`, each execution of the official `web-search` tool through the Formula API
     […] incurs one call charge » (le texte nomme `kimi-k3`, la page des outils `kimi-k3.1-pro`) : supposé valoir pour les
     deux (SUPPOSÉ).
3. **Responses API, outil côté serveur** — https://platform.kimi.ai/docs/api/responses (`api_responses.md`) : « Add
   `{"type": "web_search"}` to `tools`. The server first decides from the input whether a search is needed, then runs it
   and injects the results into the model context » ; exemple avec `"model": "kimi-k3.1-pro"` ; « Each executed search is
   billed per call (\$0.005 per call, same price for image search) » ; `include: ["web_search_call.action.sources"]` rend
   les pages touchées ; « At most one `web_search` tool is allowed per request. » Pas de boucle côté client.
4. **API de recherche autonomes** (https://platform.kimi.ai/docs/guide/best-practices-for-web-search, tableau de prix) :
   `POST /v1/tools/search` « $0.002 / call », `POST /v1/tools/search_pro` « $0.003 / call », `POST /v1/tools/fetch`
   « $0.002 / call » ; résultats **en clair** (titre, lien, extraits ; `fetch` rend le corps d'une page en Markdown).

**Prix des jetons de `kimi-k3.1-pro`** (https://platform.kimi.ai/docs/pricing/chat, tableau lu dans `pricing_chat.html`) :
entrée « $2.00 / MTok », sortie « $10.00 / MTok », entrée en cache « $0.20 / MTok », écriture de cache 5 min
« $2.00 / MTok », 1 h « $4.00 / MTok ». Raisonnement toujours actif, `reasoning_effort` « `low`, `high`, and `max`
(default `max`) » ; « For multi-turn conversations and tool calls, add the complete assistant message returned by the API
to the next request. Do not keep only `content`. » (https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart).

**Voie retenue ici : l'outil officiel par l'API Formula** (n° 2), seul équivalent qui passe par `/v1/chat/completions`,
donc par le relais existant, et seul dont la documentation dit qu'il a été vérifié avec `kimi-k3.1-pro`.

## 2. Fichiers livrés

- `relais_kimi_v4.py` : la v3 plus la recherche officielle seule (sa docstring détaille). Inactive par défaut
  (`--max-recherches 0` : tout `tools` refusé). Active : `tools` = exactement la déclaration de `web_search`, à
  l'identique (celle de la documentation, ou celle que l'amont a rendue par le relais) ; tout autre outil, un second
  outil, `builtin_function`, `functions`, un `tool_choice` étranger : 400 sans envoi. Deux chemins exacts de plus : la
  déclaration (`GET …/web-search:latest/tools`, sans coût) et l'exécution (`POST …/web-search:latest/fibers`, corps
  exactement `{"name": "web_search", "arguments": "<objet JSON>"}`, recopié tel quel). Plafond : chaque recherche réserve
  `--prix-recherche` (obligatoire, aucun défaut) et le compte dès l'envoi ; `--max-recherches` ; journal et
  `/relais/etat` : `recherches`, `cout_recherches_usd`, `refus_recherche`, empreinte SHA-256 des arguments (jamais leur
  texte).
- **Correction trouvée dans la v3** (réserve) : sa docstring annonce le réassemblage de `message.tool_calls` depuis le
  flux, mais son code ne le fait pas ; un appel d'outil de l'amont aurait été relayé comme une réponse vide à
  `finish_reason: "tool_calls"`. Sans effet sur les usages passés (aucun outil envoyé), mais c'est un repli silencieux
  (R5). La v4 réassemble les `delta.tool_calls` par `index` et journalise `tool_calls_rendus`.
- `commande_kimi_recherche_v1.py` : la boucle d'outil côté client (la documentation l'exige), bornée en tours
  (`--max-tours`), en recherches (`--max-recherches`) et en coût (`PLAFOND_SESSION_USD`, pire cas avant chaque envoi,
  y compris « rechercher puis pouvoir encore conclure »). Une borne atteinte impose `tool_choice: "none"` au tour suivant ;
  le dernier tour l'impose toujours. Message assistant renvoyé entier (`reasoning_content` compris). Sortie : dernière
  ligne JSON avec `texte`, `cout_usd` (borne haute, cache non déduit), `tours`, `recherches`, `requetes_recherche`.
- `faux_amont_kimi_v3.py` : la v2 plus l'aller-retour (déclaration, `delta.tool_calls` en morceaux, fibres à sortie
  chiffrée simulée) ; il **vérifie** l'alignement des `tool_call_id`, la fidélité des résultats renvoyés et la présence du
  raisonnement renvoyé.
- `test_relais_kimi_v4.py` : 36 essais (cas sain complet, neuf formes d'outil interdit, cinq fibres mal formées, autre
  formule, boucle bornée en tours et en recherches, 429 du relais, fibre en échec, plafond du relais qui compte la
  recherche, budget de la commande, `--prix-recherche` obligatoire, clé jamais au journal ni en sortie, non-régression de
  la v3 et de `commande_kimi_v1.py`).
- `consigne-kimi-sources-essaim-722-v1.md` : la consigne pour Kimi (questions A1 à A10, B1 à B7, C1, C2 ; citations
  exactes avec lien, mode de lecture, niveau P ou S, ce qui n'a pas pu être lu ; au plus 20 recherches).
- `doc-moonshot-lue-2026-10-30-v1/` : les pages de documentation lues, avec empreintes.

## 3. Essais (aucun réseau sortant, clé factice)

```bash
cd docs/notes/ideation-organisme-v1/relais-kimi-v1
PYTHONDONTWRITEBYTECODE=1 /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider test_relais_kimi_v4.py
```
Résultat le 30 octobre 2026 : **36 réussis, 0 échec, trois passes** ; `test_relais_kimi_v3.py` rejoué : 13 réussis.

## 4. Devis de l'appel (cible ≤ 3 USD)

Réglages recommandés : `kimi-k3.1-pro`, `reasoning_effort` `high` (le défaut `max` coûte plus de raisonnement),
`--max-tours 10`, `--max-recherches 20` (commande et relais), `--max-sortie-jetons 32768`, `--sortie-min-jetons 8192`,
**plafond dur 3 USD** dans la commande et dans le relais (`--plafond-usd 3`, `--max-appels 12`).

Modèle de coût (SUPPOSÉ : taille d'un résultat de recherche inconnue, il est chiffré ; consigne ≈ 8,8 ko, ≈ 2 600
jetons) — chaque tour renvoie tout l'historique :

| Scénario | Résultat par recherche | Tours / recherches | Entrée cumulée | Sortie | Borne haute (sans cache) | Attendu (cache lu à 0,20) |
|---|---|---|---|---|---|---|
| bas | 3 000 jetons | 7 / 10 | ≈ 0,17 M | ≈ 22 000 | 0,61 USD | 0,39 USD |
| central | 5 000 jetons | 10 / 20 | ≈ 0,68 M | ≈ 43 000 | 1,89 USD | 0,91 USD |
| haut | 10 000 jetons | 10 / 20 | ≈ 1,27 M | ≈ 69 000 | 3,33 USD | 1,50 USD |

Recherches : 20 × 0,005 = 0,10 USD au plus. **Devis : ≈ 1 USD attendu, 3 USD au pire** (plafond dur : dans le scénario
haut, la commande impose la fin avant 3 USD de borne haute). Une seule exécution ; pas de nouvel essai sans nouveau devis.

Lancement (session neuve avec `KIMI_API_KEY`, **après le GO de Lazar** ; arrêt par PID, R10) :
```bash
DOS=<dossier-neuf>; cd docs/notes/ideation-organisme-v1/relais-kimi-v1
GO_ID=GO-AAAA-MM-JJ-NN env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" \
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B relais_kimi_v4.py --port 8790 --modeles-permis kimi-k3.1-pro \
    --plafond-usd 3 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 12 --max-recherches 20 \
    --prix-recherche 0.005 --delai-amont-s 1800 --delai-silence-s 600 --journal $DOS/relais-journal.jsonl \
    > $DOS/relais.log 2>&1 &
echo $! > $DOS/relais.pid
PLAFOND_SESSION_USD=3 ROLE_POLE=lecteur_sources python3 -I -B commande_kimi_recherche_v1.py --url-relais http://127.0.0.1:8790 \
    --max-tours 10 --max-recherches 20 --reasoning-effort high --max-sortie-jetons 32768 --sortie-min-jetons 8192 \
    < consigne-kimi-sources-essaim-722-v1.md > $DOS/sortie.jsonl
# comparer le pid de /relais/etat à $DOS/relais.pid, puis : kill <pid>
```
(`--prix-cache 2` : borne haute volontaire ; le prix lu du cache est 0,20.)

## 5. Réserves et SUPPOSÉ

1. **Résultats chiffrés (R7).** La recherche officielle rend `encrypted_output` : ni nous ni le relais ne voyons ce que
   Kimi a lu. Ses citations restent **non opposables** jusqu'à vérification sur la page. Voie de vérification proposée
   (sans dépense ici, sur devis) : relire chaque lien cité par `POST /v1/tools/fetch` (0,002 USD la page, texte en clair,
   empreintable), ce qui demande une v5 du relais (chemin exact de plus) ou un petit script ; ou la Responses API avec
   `include: ["web_search_call.action.sources"]`, qui rend au moins la liste des pages touchées.
2. Les pages d'OpenAI répondent par une page anti-robot de Cloudflare (`cf-mitigated: challenge`, essai `curl -I` du
   30 octobre) ; la recherche de Moonshot pourrait n'en rendre que des extraits : la consigne demande à Kimi de le dire.
   Voie gratuite à essayer d'abord pour le dépôt `openai/math` : l'outil GitHub de la session (lecture du README et du
   journal des modifications) ; `curl` vers `github.com` est refusé par le mandataire (403).
3. SUPPOSÉ : la déclaration rendue par l'amont égale celle de la documentation (sinon la commande la lit par le relais,
   qui l'admet alors) ; le format en flux des `tool_calls` de Kimi suit la page « Use Kimi API for Tool Calls » (id et nom
   au premier morceau, `index`, arguments concaténés) ; le contenu chiffré compte en jetons d'entrée à l'appel suivant et
   reste sous l'hypothèse « un jeton par octet au moins » du pire cas.
4. SUPPOSÉ : la recherche « On `kimi-k3` » de la page des prix vaut pour `kimi-k3.1-pro` (même prix, 0,005 USD).
5. Le relais compte une recherche au prix plein dès l'envoi, même en échec (la documentation dit qu'un échec n'est pas
   facturé) : borne haute volontaire.
6. Clé : même limite que la v1 (`/proc/<pid>/environ`, F-C7).
