# Collisionneur v8 : cinq espèces, espèce E = GPT-6 Astra (OpenAI)

Écrit le 1er novembre 2026 par un sous-agent développeur neuf, sur le mot direct de Lazar (R-962 : « go devis et go depenses
5 especes avec gpt-6-astra »). Règle R12 : fichier neuf, le v7 (`donnees/collisionneur-noeuds-v1/collisionneur_v7.py`,
sha256 `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc`) reste intact ; l'essai `test_v7_intact` le vérifie.
Rien ici n'est scellé ni commis par le sous-agent ; aucun appel payant ni réseau n'a été fait.

## Ce qui change depuis le v7 (et rien d'autre)

1. **Espèce E** dans `MODELES` : `{"id": "gpt-6-astra", "fournisseur": "openai", "prix": (10.0, 50.0), "max": 32000, "max_relance": 65536}`.
   L'identifiant est RAPPORTÉ (conv-audit), les prix (10 / 50 USD par million de jetons d'entrée / sortie) et les plafonds de
   sortie sont SUPPOSÉS : barème volontairement haut, commenté dans le script. `LETTRES = ("A", "B", "C", "D", "E")`.
2. **`appeler_openai(modele_id, prompt, max_tokens, attentes=(0, 10, 30, 90))`** : `POST {OPENAI_BASE_URL}/chat/completions`
   (défaut `https://api.openai.com/v1`), en-tête `Authorization: Bearer` lu dans `OPENAI_API_KEY`, corps
   `{"model", "messages": [{"role": "user", "content": prompt}], "max_completion_tokens": max_tokens}` ; `urllib` comme
   Gemini (contexte TLS depuis `SSL_CERT_FILE`, mandataire de l'environnement) ; reprises sur 429, 500, 502, 503, 504 avec les
   mêmes attentes que Gemini ; délai 1 800 s ; la clé est masquée (`[clé]`) dans tout message d'erreur, comme pour Gemini.
   `OPENAI_BASE_URL` n'est acceptée que vers la boucle locale (`http://127.0.0.1:PORT`, `http://localhost:PORT`, sans
   mandataire ; sert aux essais hors réseau) ou égale à l'adresse d'OpenAI ; toute autre adresse est refusée sans appel, pour
   que la clé ne parte jamais vers un tiers.
3. **`lire_reponse_openai`** : texte `choices[0].message.content`, `finish_reason`, `usage.prompt_tokens` /
   `completion_tokens`, modèle servi `model`, `id`. Les jetons de raisonnement (`completion_tokens_details.reasoning_tokens`)
   sont AJOUTÉS à la sortie s'ils existent (SUPPOSÉ, voir « à vérifier en ligne ») ; l'usage garde les deux nombres bruts
   (`sortie_visible`, `raisonnement`) pour recalculer si l'API les incluait déjà. Un champ `message.refusal` servi est lu comme
   un refus (catégorie = début du texte du refus).
4. **`statut_reponse("openai", rep)`** : `stop` → OK si plein, sinon VIDE ; `length` → TRONQUE si plein, sinon VIDE ;
   `content_filter` (ou champ `refusal`) → REFUS ; aucun choix → VIDE ; autre fin → ANOMALIE. Un REFUS n'est jamais relancé
   et ferme la porte du tour, comme pour A et B ; la règle **R-831** s'applique alors à E comme à Fable ou Opus 4.6 : l'arbitre
   relance le **même run** avec `--accepter-absence` sur les trois cellules d'E de l'étage, les quatre autres espèces continuent
   et reçoivent un bloc « PIÈCE ABSENTE » à la place de ses cellules (essai `test_refus_d_astra_regle_R831`). Le code du v7
   n'est pas modifié sur ce point : il traitait déjà les refus ainsi, R-831 est une règle d'exploitation.
5. **Nombres d'espèces dérivés de `LETTRES`** partout où le v7 les écrivait en dur :
   - préambule servi aux modèles : « Collisionneur épistémique 4×3 … entre quatre modèles » → gabarit formaté une fois au
     chargement (« 5×3 … entre cinq modèles ») ; `construire_prompt` reste identique au v7 (essai de non-régression) ;
   - docstring (« 3×3 », « aux trois modèles »), description de la ligne de commande (« 3×3 »), notes de Jev (« des trois
     modèles »), commentaire « Jev, quatrième pôle » ;
   - `devis` : le pire cas de Jev comptait **3 cellules par tour** depuis la v2 (faux depuis la v4 à quatre espèces) → `len(LETTRES)` ;
     `devis` imprime aussi le nombre de cellules par étage (10, 15, 15 ; 40 au total) ;
   - tout le reste (`autres`, `entrees`, `lire_arbitrage`, `lancer_etage`, `ecrire_etat`, `verifier` via `MODELES[cid[-1]]`)
     suivait déjà `LETTRES` : chaque espèce critique les quatre autres et répond à quatre critiques, sans changement de code.
   Aucun « 4 » ni « 12 » codé en dur n'a été trouvé dans le v7 (le « 4 » de `max_retries=4` et les codes de sortie n'ont rien à
   voir avec les espèces ; « quatre protocoles expérimentaux » en E2-T1 est le nombre de protocoles demandés, inchangé).
6. `VERSION = "collisionneur-v2.11-cinq-especes-gpt6-astra"` ; `APPELANTS["openai"]`.

Fonctions dont la source est identique au v7, vérifiée par `inspect.getsource` dans l'essai
`test_fonctions_inchangees_identiques_au_v7` : tout sauf `statut_reponse`, `devis`, `ecrire_notes_jev` (une chaîne), `principal`
(une chaîne) ; `TOURS`, `CONSIGNES`, `QUESTIONS_JEV`, `JEV`, `EFFORT`, `MARQUEUR`, `REFUS_GEMINI` et les espèces A à D sont égaux.

## Fichiers de ce dossier

| Fichier | sha256 |
|---|---|
| `collisionneur_v8.py` | `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` |
| `test_collisionneur_v8.py` | `2f5efa14b459e64f798a79d3696e8a211a936ccb5ae7cbe46ab4a6b97d37f0a6` |
| `appel_controle_v9.py` | `ecca2070a653f29ca55ce9678302cb4106cd4c1d11d403770ad6aec91f57c571` |

Empreintes recalculées à l'écriture de ce fichier (`sha256sum`) ; celle de ce LISEZMOI est donnée dans le rapport du sous-agent.
Rien n'a de compagnon `.sha256` : le scellement (R6) revient à la session qui versera ces fichiers.

## Essais (hors réseau) : 27 passés

```
cd docs/notes/ideation-organisme-v1/course-2/collisionneur-v8
../../../../../.venv/bin/python -m pytest -q -p no:cacheprovider test_collisionneur_v8.py
```
Un faux serveur HTTP local (ThreadingHTTPServer dans un fil, port libre) imite l'API d'OpenAI ; `appeler_openai` le joint par
`OPENAI_BASE_URL`. Scénarios : réponse normale (corps de requête et en-tête `Bearer` vérifiés), `length`, `content_filter`,
champ `refusal`, sortie vide, aucun choix, `tool_calls` (ANOMALIE), 429 puis 429 puis succès, 503 puis succès, 429 sans
relance permise (ECHEC), erreur 400 qui renvoie l'en-tête (clé masquée), corps non JSON, port fermé, adresse tierce refusée,
clé absente, clé fausse (401) ; usage avec `reasoning_tokens` ; `cout`, `cout_pire_cas` ; `devis` sur un faits factice (40 lignes,
15 à l'étage III, 8 pour E) ; étage III de bout en bout à cinq espèces (A à D par des appelants factices injectés, E par le faux
serveur) : 15 cellules, `verifier` sans problème, pièces croisées dans l'ordre attendu, journal sans la clé ; refus d'E puis
R-831 par `--accepter-absence` (12 cellules, blocs absents, état) ; modèle servi différent → code 3 ; plafond trop bas → code 4 ;
non-régression sur le v7 (sources identiques, `statut_reponse` pour anthropic / gemini / kimi sur une grille, `cout`,
préambule identique au nombre près) ; v7 intact par empreinte. Le paquet `anthropic` n'est pas nécessaire aux essais.
La suite du dépôt (`python -m pytest -q` à la racine, `testpaths = tests`) ne ramasse pas ce dossier.

## Comment lancer (gabarit)

Variables lues : `ANTHROPIC_API_KEY` (plus `ANTHROPIC_WORKSPACE_ID` si la clé l'exige), `GEMINI_API_KEY`, `KIMI_RELAIS_URL`
(relais Kimi local lancé à part, boucle locale seulement), **`OPENAI_API_KEY`** ; facultatives : `SSL_CERT_FILE`,
`TYPESAFE_API_KEY` (option `--jev`). Jamais d'export de clé dans un fichier journalisé ; `python -I -B`.

```bash
# 0. Appel de contrôle des cinq espèces (un appel payant par espèce, 1 024 jetons de sortie au plus) : GO sur devis d'abord.
python -I -B appel_controle_v9.py collisionneur_v8.py controle-cinq-especes-v1.json GO-AAAA-MM-JJ-NN
# 1. Devis (aucun appel).
python -I collisionneur_v8.py devis --faits FAITS.md --question QUESTION.md
# 2. Étage III ciblé (le cas des nœuds) ; plafond de run ≥ 1,5 × estimation, ≤ reste du poste.
python -I -B collisionneur_v8.py etage3 --sortie run-…-e3-v1 --faits FAITS.md --question QUESTION.md --plafond-usd 30
# 3. Refus d'E (porte fermée, code 2) : R-831, même run, absence acceptée pour ses trois cellules.
python -I -B collisionneur_v8.py etage3 --sortie run-…-e3-v1 --faits FAITS.md --question QUESTION.md --plafond-usd 30 \
  --accepter-absence E3-T1-conception-E --accepter-absence E3-T2-critique-croisee-E --accepter-absence E3-T3-reponse-E
# 4. Vérification indépendante, sans réseau.
python -I collisionneur_v8.py verifier run-…-e3-v1
```
Devis sur un faits d'une ligne, pour l'ordre de grandeur de l'espèce E seule : 1,62 à 2,09 USD au pire cas par cellule
(32 000 jetons de sortie à 50 USD le million) ; `  étage 3 : 15 cellules, 38.08 USD au pire cas, sans relance`. Avec un faits réel de 45 000 mots,
l'entrée pèse davantage : refaire le devis sur le vrai fichier avant le GO.

## À vérifier en ligne avant tout lancement (aucune session ici n'avait de clé OpenAI)

1. **Identifiant exact du modèle** : `GET https://api.openai.com/v1/models` (en-tête `Authorization: Bearer`) ; chercher
   `gpt-6-astra` et ses variantes. Attention : `modele_conforme` (v7, inchangée) accepte tout suffixe après un tiret, donc un
   modèle servi `gpt-6-astra-mini` ou daté passerait ; si une variante « mini » existe, demander l'identifiant daté complet.
2. **Prix réels** (page des tarifs d'OpenAI) : 10 / 50 sont rapportés, pris comme hauts ; corriger `MODELES["E"]["prix"]`
   (nouvelle version du script, R12) si le réel est plus haut ; s'il est plus bas, garder le barème haut est acceptable.
3. **Plafond de sortie** : `max_completion_tokens` 32 000 puis 65 536 en relance sont supposés ; vérifier la limite du modèle
   (erreur 400 sinon) et si l'API exige un paramètre d'effort de raisonnement pour une sortie longue.
4. **Jetons de raisonnement** : vérifier si `usage.completion_tokens` inclut déjà `completion_tokens_details.reasoning_tokens`
   (documentation d'OpenAI : oui pour les modèles de raisonnement). Si oui, le v8 compte double la sortie (sur-estimation du coût
   et du journal, jamais sous-estimation) : corriger en v9 (`sortie = completion_tokens`) ; les champs bruts du journal
   permettent de recalculer les dépenses déjà consignées.
5. **Politique de refus d'Astra** : le directeur rapporte qu'il « refuse les tâches de cybersécurité offensive » ; la question
   des nœuds touche à la sécurité. Tester par l'appel de contrôle puis par la première cellule ; un refus se traite par R-831
   (ci-dessus) : pas d'arrêt du poste, pas de reformulation de la question pour contourner le refus (refus enregistré tel quel).
   Vérifier aussi la forme du refus servie (`finish_reason: content_filter`, champ `refusal`, ou texte poli avec `stop` : ce
   dernier cas serait lu OK par le script, comme pour Kimi ; l'arbitre le verra à la lecture).
6. **Mandataire et TLS** depuis la machine de lancement : `api.openai.com` doit être joignable à travers le mandataire de
   l'environnement (`HTTPS_PROXY`, `SSL_CERT_FILE`), comme Gemini.

## Ce que le sous-agent n'a pas fait

Aucun appel réel, aucun scellement, aucun commit, aucune lecture d'autres fichiers de `donnees/` que le v7 et
`appel_controle_v8.py` ; pas de script de lancement (`lancer-tour-…sh`) : les lanceurs existants sont sous `donnees/`, hors
périmètre de lecture, à adapter par la session principale (ajout de `OPENAI_API_KEY` et du v8).
