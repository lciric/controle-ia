# Procédure — création de la session fille (porteuse des clés) sur le nouveau compte, v2

Écrite le 2 novembre 2026 à 23:46 UTC (heure relevée par `date -u`) par session-depot, instance 5, sur la décision de Lazar relayée
par conv-audit (n° 390, 23:34 à 23:36 UTC) : « fille neuve sur le nouveau compte ; Lazar y met lui-même les clés Kimi et Astra ;
Moonshot rechargé ». Remplace, pour la fille, le § 0.3 de la passation `registres/passations/2026-11-02-2006.md`. Aucune clé n'est
jamais écrite dans la conversation, dans un fichier ni dans un argument de ligne de commande : les clés vivent dans les réglages de
l'environnement et sont lues par leur nom.

## 1. Ce que fait Lazar (une fois, avant la création)
1. Ouvrir les réglages de l'environnement de la session (menu de l'environnement dans la barre de titre, puis « Modifier »),
   section des secrets réseau (ou variables d'environnement si cette section n'est pas offerte), et y poser les clés manquantes,
   **par leur nom exact** :
   - `KIMI_API_KEY` — Moonshot, modèle `kimi-k3.1-pro` (après la recharge du compte Moonshot ; sans crédit, le relais Kimi rend 429) ;
   - `OPENAI_API_KEY` — Astra, modèle `gpt-6-astra` (commande 8807 ; vérifier que le compte a du crédit) ;
   - `RR_ANTHROPIC_API_KEY_LUC_2` et `RR_ANTHROPIC_API_KEY_LUC_3` — collisionneur et commande Claude (8806), si les trois clés
     sont voulues ; `RR_ANTHROPIC_API_KEY_LUC` est déjà présente.
   Déjà présentes sur ce compte (vues par leur nom seulement) : `VAST_API_KEY`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN`, `GH_TOKEN`,
   `GEMINI_API_KEY_2` (Argon, `gemini-4-argon`), `RR_ANTHROPIC_API_KEY_LUC`.
2. Vérifier le réseau de l'environnement : `api.moonshot.ai`, `api.openai.com`, `api.anthropic.com`,
   `generativelanguage.googleapis.com`, `github.com`, PyPI (déjà : `api.vast.ai`, `console.vast.ai`, `huggingface.co`).
3. Dire à session-depot « clés posées » (sans les nommer autrement que par leur nom). Une session neuve les voit ; la session de
   session-depot en cours ne relit pas son environnement.

## 2. Ce que fait session-depot (après le mot de Lazar)
1. Créer la fille comme session neuve du même environnement (outil de création de session, environnement hérité), avec pour consigne
   le brief de la fille (§ 4), sans aucune clé dans le texte ; relever son identifiant de session et le consigner (`registres/decisions.md`).
2. La fille vérifie la **présence** de chaque clé par son nom (`env | grep -o '^NOM='`), jamais la valeur, et le rapporte.
3. La fille clone `lciric/controle-ia-travail` (`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`), installe
   `requirements-cpu.txt`, `bwrap` 0.9.0 (tour fermé) et récupère par refspec explicite les branches d'outils :
   `outils/commandes-a1-bis-v1` (commandes Claude 8806 et Astra 8807), `outils/commandes-tour-ferme-v1` (commandes v3 de Kimi et d'Argon),
   `donnees/recuperation-collisionneur-v8-v1` (relais Kimi v3, commande Argon v2 dont la sous-commande `servir` est le relais 8805,
   `collisionneur_v7.py`, pièces de la mini-course), `outils/collisionneur-v9-v1` et `donnees/collisionneur-v9-brainstorm-v1`.
4. Relais et commandes, tous sous `env -i` avec la seule clé qu'ils tiennent, PID consignés (R10), ports : 8802 collisionneur v9,
   8804 relais Kimi (`relais_kimi_v3.py`), 8805 relais Argon (`commande_argon_v56_nuit_v2.py servir`, **monofil**, instrument gelé
   d'A1-v3 : inchangé), 8806 commande Claude, 8807 commande Astra. Chaque relais est éprouvé par un appel de contrôle (« Réponds
   seulement par le mot OK », plafond de session 0,05 USD) avant toute course, modèle servi = modèle demandé.
5. La fille n'agit que sur les ordres écrits de session-depot (ou collés par Lazar), sous le go permanent R-1059 et ses cinq
   conditions ; elle scelle toute sortie avant lecture, la verse sur une branche de données, donne commit, empreintes et dépense.

## 3. Courses qui dépendent de la fille, dans l'ordre proposé
1. **Collisionneur v9 (GO-31, reste ≈ 19 USD sur 40)** : le dossier du tour arrêté (13 cellules) est dans le conteneur de l'ancienne
   fille (ancien compte), non poussé. Si l'ancienne fille peut encore exécuter un ordre, Lazar lui colle : « pousse le dossier du
   tour v9 scellé tel quel sur `donnees/collisionneur-v9-brainstorm-v1` » ; sinon, tour neuf déclaré tel quel chez la fille neuve,
   même prompt et mêmes faits (≈ 17 à 20 USD attendus ; extension de GO-31 si le reste ne couvre pas le pire cas).
2. **A1-v3 (GO-21, 400 USD, Argon seul)** : dès le texte scellé de conv-audit (code v3.1) et la commande exacte ; relais 8805 ;
   chemin hors clone `/home/user/hors-clone-a1-v3/`. Rien d'autre sur Argon pendant la course (relais monofil).
3. **Tour fermé, étage 1 (GO-23, 50 USD : Kimi 44, Argon 6)** : après A1-v3 (Argon partagé) ; v64 et brouillon 6 de conv-audit,
   configuration v3 scellée, `bwrap`, identité dédiée, `TMPDIR=/tmp`.
4. **Juges v2 (GO-32, 60 USD : Argon 24, Astra 36)** : commande Astra 8807 à éprouver chez la fille neuve ; après A1-v3.
5. **Attaque v4 (GO-22, 200 USD)** et **réplication Kimi d'A1-v3 (GO-25, 150 USD)** : après A1-v3, jamais en même temps.
Les courses sur carte (relance de R1 GO-27, complément GO-30, P3-bis GO-29, T0.6 GO-28) ne dépendent pas de la fille (Vast).

## 4. Brief de la fille (à coller tel quel par session-depot à la création)
> Tu es la session fille de session-depot dans le programme de contrôle de l'IA de Lazar (directeur). Tu portes les clés des
> fournisseurs par leur nom dans ton environnement : tu ne les affiches, ne les écris et ne les transmets jamais ; tu vérifies leur
> présence par `env | grep -o '^NOM='`. Tu n'agis que sur les ordres écrits de session-depot ou de Lazar. Tu clones
> `https://github.com/lciric/controle-ia-travail.git` (jamais `lciric/controle-ia`), tu installes `requirements-cpu.txt`, tu récupères
> les branches par refspec explicite seulement. Tu lances les relais et commandes sous `env -i` avec la seule clé qu'ils tiennent, tu
> consignes leurs PID, tu les arrêtes par PID (R10). Toute course exige un texte scellé, une ligne de GO valide, la commande exacte de
> conv-audit, un passage de vérification en code 0 et le scellement de la sortie avant toute lecture. Tu verses chaque sortie scellée
> sur une branche de données, tu donnes commit, empreintes et dépense par espèce dans un rapport scellé. Français, tutoiement, presque
> aucun sigle ; aucune heure écrite sans `date -u`.
