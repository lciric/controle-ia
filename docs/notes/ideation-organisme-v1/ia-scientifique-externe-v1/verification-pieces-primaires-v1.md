# Vérification sur pièces primaires des notes A et B (cadres « IA scientifique ») — v1

29 octobre 2026, rédigée à 22:37 UTC (`date -u`) ; sources consultées de 22:31 à 22:36 UTC. **Sous-agent neuf, qui n'a écrit aucune des deux notes.**
Note A : `docs/notes/ideation-organisme-v1/ia-scientifique-externe-v1/choix-ia-scientifique-v1.md`. Note B : `origin/canal/conv-audit-n04:…/ideation-organisme-approches-v1/note-organisme-hybride-ai-scientist-v1.md`.
Méthode : fichiers bruts (`raw.githubusercontent.com`) au commit de tête donné par `git ls-remote`, sans clonage ni exécution ; pages et PDF arXiv ; page Nature. L'interface GitHub a été refusée (403) : étoiles, nombre et dates de commits invérifiables.
Préfixes : **v2@** = `https://raw.githubusercontent.com/SakanaAI/AI-Scientist-v2/96bd51617cfdbb494a9fc283af00fe090edfae48/` ; **v3@** = `…/SakanaAI/AI-Scientist-v3/df8313889a004f8a44a472e19a833cd547bb828a/` ; **H@** = `…/RobertTLange/headless-cli/93cd9b06b85f848af1308c41e018991b33907c5e/`.
PDF lus (sha256) : `arxiv.org/pdf/2504.08066v1` `53bafd3028e3…` ; `2610.18933v1` `cb170b543574…` ; `2408.06292v3` `e911f90b0114…`. Gardés hors du dépôt ; à verser dans `docs/sources/pdf/` pour être opposables (R7).

## Verdict

1. « Agentic Scientist v3 » existe : dépôt `SakanaAI/AI-Scientist-v3`, « The Agentic Scientist », arXiv 2610.18933, Apache-2.0. Il date du 13 octobre 2026, comme le dit A ; B donne une date fausse.
2. **Les deux motifs pour lesquels B exclut v2 sont faux tels qu'ils sont écrits.** Le code se replie sur le processeur. L'idéation et la rédaction peuvent appeler Claude par l'interface directe d'Anthropic. **Mais la phase d'expériences force Bedrock**, ce qu'aucune des deux notes ne voit. Cela casse la configuration I de A tant que ce point n'est pas corrigé.
3. Sur v3, A se trompe sur le réseau par défaut (`host`, pas `bridge`) et sur Docker (défaut, pas exigence). Aucune note ne relève deux points : les agents utilisent le Web, et rédiger une tâche depuis une question est expérimental.

## Table des affirmations

V = VÉRIFIÉE, F = FAUSSE, NV = NON VÉRIFIABLE.

| n° | note | affirmation | classe | preuve |
|---|---|---|---|---|
| 1 | A, B | La licence de v2 est l'« AI Scientist Source Code License » v1.0 de décembre 2025, dérivée de la Responsible AI License, avec mention obligatoire | V | v2@LICENSE l.1-4, l.39-40 ; README l.203-207 |
| 2 | A | Clause « Surveillance » visant des personnes | V | LICENSE l.25-27 |
| 3 | B | v2 exige une carte NVIDIA et CUDA | **F** | README : « designed to run on » (l.41) ; le code se replie : v2@ai_scientist/treesearch/parallel_agent.py l.1171-1172, « falling back to CPU-only mode » |
| 4 | A | Citation du README sur les cartes NVIDIA | V | README l.41 |
| 5 | B | Dans v2, Claude ne passe que par Bedrock | **F** | v2@ai_scientist/llm.py l.481-483 : `claude-` → `anthropic.Anthropic()`. Le README ne documente que Bedrock (l.73-79). Vrai pour la phase d'expériences (ligne 7) |
| 6 | A | `llm.py` de v2 : Anthropic direct, Bedrock, Vertex, OpenAI, et Gemini par une adresse compatible OpenAI codée en dur | V | llm.py l.480-539 |
| 7 | — | **Fait nouveau, omis par A et B** : les expériences de v2 n'appellent Claude que par Bedrock | — | v2@ai_scientist/treesearch/backend/backend_anthropic.py l.17-18, `AnthropicBedrock` ; choisi pour tout `claude-` (backend/\_\_init\_\_.py l.14-15, l.69) ; modèle par défaut au format Bedrock (bfts_config.yaml l.57) |
| 8 | A | Liste blanche des modèles figée en 2024-2025 | V | llm.py l.13-73 ; imposée par `choices=` (perform_ideation_temp_free.py l.277) |
| 9 | A | Vision par OpenAI ou Ollama seulement | V | v2@ai_scientist/vlm.py l.195-213 |
| 10 | A | 4 ouvriers ; 20, 12, 12 et 18 itérations ; débogage de profondeur 3 ; code écrit par claude-3-5-sonnet, retour par gpt-4o | V | bfts_config.yaml l.38-43, l.57, l.63, l.74 |
| 11 | A | Code exécuté par `exec` dans un processus enfant, sans conteneur, limite de 3 600 s, environnement hérité | V | interpreter.py l.117-118, l.144, l.170 ; bfts_config.yaml l.19 |
| 12 | A, B | Avertissement « will execute LLM-written code », bac à sable recommandé | V | README l.25-26 |
| 13 | A, B | 15 à 20 USD par course d'expériences ; environ 5 USD de rédaction | V | README l.180 (chiffres des auteurs) |
| 14 | A, B | Semantic Scholar est facultatif | V | README l.83, l.186-188 |
| 15 | A | v2 accepte un fichier d'idées en entrée | V | README l.145 (`--load_ideas`) |
| 16 | A | Commit de tête de v2 : `96bd516` | V | `git ls-remote` |
| 17 | A | Commit du 19 décembre 2025 ; 7 422 étoiles | NV | 403. Date cohérente avec la LICENSE (l.2) |
| 18 | A, B | Article de v2 : arXiv 2504.08066, titre et auteurs | V | page abs, v1 du 10 avril 2025 |
| 19 | A, B | Un manuscrit sur trois accepté en atelier, note moyenne 6,33 (6, 6 et 7), puis retiré | V | PDF v2 p.2 et p.9 |
| 20 | A | Les auteurs disent leur système faible pour formuler des hypothèses neuves | V | PDF v2 p.13 |
| 21 | B | Article dans Nature, « Towards end-to-end automation of AI research », du 2 octobre 2026 | **F** | `nature.com/articles/s41586-026-10265-5` : en ligne le 25 mars 2026, Nature 651(8107). Titre exact |
| 22 | B | Précision équilibrée du relecteur : 69 % | V | même page Nature (« 69% versus 66% ») ; absent du PDF v2 |
| 23 | A, B | Licence de v3 : Apache-2.0 | V | v3@LICENSE ; pyproject.toml l.11 |
| 24 | A | Article de v3 : arXiv 2610.18933, cinq auteurs, 13 octobre 2026 | V | page abs, v1 du 13 octobre 2026 à 11:28 UTC |
| 25 | B | Article de v3 publié le 15 octobre 2026 | **F** | même page : 13 octobre |
| 26 | A | Commit de tête de v3 : `df83138` | V | `git ls-remote` |
| 27 | A | Commit du 18 octobre ; 8 commits ; 555 étoiles | NV | 403 |
| 28 | A, B | Six phases, chacune dans son conteneur Docker, sur un instantané local | V | v3@README.md l.29-30, l.297-306 |
| 29 | A, B | Les agents `claude`, `codex`, `cursor`, `opencode`, `gemini` et `pi` sont pilotés par Headless ; `claude` par défaut | V | README l.89-93, l.123-125 |
| 30 | A, B | Agents à permissions totales (`--allow yolo`), héritant des clés, orientables par les fichiers de tâche | V | README l.40-45 |
| 31 | A, B | Carte graphique seulement pour certains préréglages (deux pour `grpo`) ; `circpack` tourne sur processeur | V | README l.64-66, l.79-82, l.176-177 |
| 32 | A | Les candidats ne peuvent pas écrire dans les sorties de l'évaluateur | V | docs/evaluation_evidence.md l.9-10 |
| 33 | A | Contradiction entre `ANTHROPIC_API_KEY` et la voie Bedrock | V | README l.134 ; docs/agent_billing.md l.11-12 ; levée en partie (fiche) |
| 34 | A | Aucun chiffre de coût publié | V | rien dans les fichiers lus ; registre de coût par course (pipeline.md l.296-299) |
| 35 | A | v3 exige un démon Docker | **F** | Docker est le défaut (README l.29-30), mais le mode natif est documenté (README l.61-62 ; install.md l.161-168). Les six phases en mode natif n'ont pas été vérifiées |
| 36 | A | Réseau des conteneurs : `bridge` par défaut | **F** | `agsci run` : `host` (install.md l.163, l.170 ; README l.143-144) ; `bridge` seulement pour `agsci investigate` et la phase post-hoc |
| 37 | A | Headless est sous Apache-2.0 | V | H@LICENSE ; commit épinglé (Dockerfile l.63) |
| 38 | A | Headless : 52 étoiles, 362 commits | NV | 403 |
| 39 | A | Headless transmet les identifiants courants ; le reste passe par `--docker-env` | V | H@docs/usage.md l.345, l.186 |
| 40 | A | Claude Code accepte `ANTHROPIC_BASE_URL` | V | `code.claude.com/docs/en/env-vars.md` l.138 ; version 2.1.285 épinglée (Dockerfile l.58) |
| 41 | A, B | v3 peut être branché sur notre relais par `ANTHROPIC_BASE_URL` | NV | variable absente de la liste transmise (usage.md l.345) ; passage de `--docker-env` par `agsci` non lu |
| 42 | B | Évaluateur et grille scellés, évaluation finale scellée, lignes de base et ablations | V | README l.299-303 (citation littérale introuvable) |
| 43 | B | L'article v3 cite Claude Opus, GPT, DeepSeek et Kimi | V | PDF v3 p.15 |
| 44 | B | Un article accepté en présentation orale à ALIFE 2026 | V | PDF v3 p.2, « ALIFE 2026 talk » |
| 45 | B | Cet article a été lourdement retouché par des humains | **F** | PDF v3 p.2 : « after limited human edits and verification » (p.22 : corrections d'affirmations non soutenues) |
| 46 | B | 70 campagnes sur 5 tâches | V | PDF v3 p.21 |
| 47 | B | Corrélation de 0,44 entre performance et notes des relecteurs | V | PDF v3 p.12 |
| 48 | B | Un agent a pris un raccourci sur l'évaluation | V | PDF v3 p.21 : « changed the evaluation protocol on a subset of RL fine-tuning runs » |
| 49 | B | Docker peut être remplacé par `bwrap` (marqué SUPPOSÉ dans B) | NV | exige une exécution |
| 50 | A | Aucune évaluation indépendante de v3 | NV | affirmation d'absence |
| 51 | A | Licence de v1 affichée « Other » | V | même licence que v2 (AI-Scientist@1de1dbc LICENSE l.1-2), non standard |
| 52 | A | Article de v1 : arXiv 2408.06292 et ses auteurs | V | page abs |
| 53 | A | Incidents de v1 : script qui se relance lui-même ; limite de temps allongée | V | PDF v1 p.19 ; PDF v3 p.21 |
| 54 | A | Agent Laboratory : licence MIT, commit `d9017d9` | V | LICENSE ; `git ls-remote` |
| 55 | A | Agent Laboratory appelle OpenAI, `claude-3.5-sonnet` et Gemini | V | AgentLaboratory@d9017d9 inference.py l.76-82, l.97-98 |
| 56 | B | Agent Laboratory n'appelle qu'OpenAI et DeepSeek | **F** | même fichier, l.97-98 : `anthropic.Anthropic(...)` |
| 57 | A, B | AI-Researcher et MLR-Copilot n'ont aucune licence | V | aucun `LICENSE`, `.md` ou `.txt` à la racine (404) aux commits `f9a6f84` et `5f7df06` |
| 58 | A, B | CodeScientist : Apache-2.0, exécution chez Modal | V | LICENSE ; README l.261 |
| 59 | B | AIDE : licence MIT, prend Anthropic en charge | V | WecoAI/aideml@ad73d22 LICENSE ; README l.50, l.126 |

**Décompte sur 58 lignes classées (la ligne 7 est hors décompte) : 44 VÉRIFIÉES, 8 FAUSSES (n° 3, 5, 21, 25, 35, 36, 45, 56), 6 NON VÉRIFIABLES (n° 17, 27, 38, 41, 49, 50).** Fausses par note : A en a 2 (n° 35 et 36), plus l'omission de la ligne 7 ; B en a 6.

## Fiches

**AI-Scientist-v2** (`96bd516`).
- *Licence* : licence maison à restrictions d'usage ; toute diffusion doit déclarer qu'elle est générée par machine (l.39-40) ; les restrictions doivent être reprises dans les accords de distribution (l.42). Ce n'est pas une licence libre.
- *Matériel* : conçu pour une carte, mais se replie sur le processeur ; `torch` est requis (launch_scientist_bfts.py l.5).
- *Modèles* : pour l'idéation et la rédaction, Anthropic direct, Bedrock, Vertex, OpenAI, Gemini, Ollama ; **pour les expériences, Claude par Bedrock seulement**, sinon OpenAI ou Ollama ; vision par OpenAI ou Ollama.
- *Exécution* : `exec` dans un processus enfant, même utilisateur et même réseau, sans conteneur.
- *Maintenance* : date du commit non lisible.

**The Agentic Scientist** (`df83138`).
- *Licence* : Apache-2.0, comme Headless.
- *Matériel* : le processeur suffit pour `circpack` ; une carte seulement pour les préréglages qui la déclarent.
- *Modèles* : agents de code par Headless. Claude passe par Claude Code, avec un abonnement ou `ANTHROPIC_API_KEY` (README l.134). Bedrock n'est que la voie payante *de repli* : « With no detected subscription or configured backup, `auto` preserves native authentication » (H@README.md l.138-149). La relecture facultative envoie le manuscrit à OpenAI (README l.211-212). Headless n'impose pas de plafond local en dollars (H@README.md l.157-158).
- *Exécution* : Docker par défaut, réseau `host`, fichier `.env` monté (install.md l.129-131). L'article dit que les agents « leverage general web access » (PDF p.22). Dépendance `scholarly` (pyproject l.40). Rédiger une tâche depuis un brief est « experimental… not yet robust » (README l.279-293).
- *Maintenance* : stade « Alpha » (pyproject l.20) ; article du 13 octobre 2026.

## Conséquences pour le choix

Établi :
- E1. B exclut v2 sur deux prémisses fausses (lignes 3 et 5). Confiance haute.
- E2. **La configuration I de A ne tourne pas en l'état.** Ses correctifs ne touchent pas `backend_anthropic.py` : les expériences appelleraient Bedrock, que l'on ne peut pas joindre sous `bwrap` sans clé. Confiance haute.
- E3. Par défaut, v3 ouvre plus que ne le dit A : réseau `host`, Web consulté par les agents, aucun plafond local. Confiance haute.
- E4. v3 est sous licence libre ; v2 impose des restrictions et une mention de génération par machine. Confiance haute.

Inféré :
- I1. Notre entrée est une question, pas un évaluateur. Elle ferait donc passer v3 par sa voie de rédaction de tâche, qui est expérimentale. Confiance moyenne.
- I2. Une fois `backend_anthropic.py` corrigé, v2 tient dans ce conteneur : un seul processus sous `bwrap`, sans démon Docker. v3 demande un démon Docker, ou des agents natifs à pleins droits qu'il faudrait envelopper. Confiance moyenne.
- I3. La licence de v2 ne bloque pas un usage interne : elle impose surtout une mention. Confiance moyenne ; aucun juriste ne l'a lue.
- I4. Aucune des deux recommandations ne tient sur ses propres motifs. Confiance moyenne.

## Décision pour le directeur

**Décision** : quel cadre préparer pour l'hybride, au vu des pièces primaires.
**Enjeu** : un bras comparable, enfermé sans clé ni réseau, sans dépenser sur des prémisses fausses.

| option | avantage | inconvénient |
|---|---|---|
| (a) v2, configuration I de A **corrigée** (`backend_anthropic.py` passe par `anthropic.Anthropic()` et le relais) | tient dans ce conteneur ; un seul processus ; prend nos idées en fichier | modifie du code tiers ; licence restrictive ; modèles figés en 2025 ; aucun évaluateur scellé |
| (b) v3, après revue de sûreté (réseau coupé, transmission de `ANTHROPIC_BASE_URL`, Web coupé) | licence libre ; évaluateur scellé ; agents récents | démon Docker absent ; réseau `host` par défaut ; rédaction de tâche expérimentale ; stade Alpha |
| (c) aucun cadre externe pour l'instant (option (b) de B) | aucune dépendance tierce | aucune comparaison externe |

**Recommandation : (a) pour le pilote ; (b) en préparation sur papier seulement.** Confiance 0,55. Aucune installation et aucune dépense sans GO. La revue de code du § 4.3 de A doit couvrir `treesearch/backend/*`.

Version 1 ; jamais réécrite (R12).
