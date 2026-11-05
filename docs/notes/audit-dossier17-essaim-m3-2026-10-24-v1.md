# Audit à l'aveugle de la relève de Gemini, part « session-depot » : le dossier 17 (essaim M3) et vérifications croisées (v1)

- **Auteur et date** : session Claude Code du dépôt (lignée « session-depot » du canal « reprise de la relève »), le
  2026-10-24 entre 13:24 et 14:15 UTC (heures lues par `date -u`).
- **Demande de Lazar** : auditer à l'aveugle la passation de Gemini, puis comparer ; se recentrer sur « le système
  élaboré par Gemini de l'essaim adaptatif autonome qui apprend, s'organise seul et invente ses propres concepts
  mathématiques », vérifier qu'il marche, le corriger, le tester sur des cas d'étude ; déboguer les scripts collés.
- **Statut : audit, non opposable (R7).** Rien n'a été exécuté de la relève. Aucune clé utilisée. La note versée
  `docs/notes/audit-releve-gemini-2026-10-24-v1.md` n'a **pas** été lue avant l'écriture de cette note ; la
  comparaison (R4) fait l'objet d'une note séparée.
- **Pièces lues** :
  - le « DOSSIER DE PASSATION MAÎTRE (MIS À JOUR) » de Gemini, collé par Lazar dans la session (donnée, pas instruction) ;
  - la sortie du terminal Windows de Lazar, collée dans la session : listing du dossier 17, journaux en direct, code
    source complet de trois scripts, sortie de `git status`, `git commit`, `git push` ;
  - sur `quarantaine/releve-gemini-2026-10-23` (`f5cb537`), en lecture seule : `STATE_0_OMEGA.json`,
    `RAPPORT_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA.json`, `RESULTAT_REEL_GPU_VOLET_I_K0.json`,
    `NODE_A_VOLET_I_K0.log`, la ligne 314 de `run_campagne_gpu_72h_5_volets_llama3.py` (masquée), des `grep`.
- **Partage avec la lignée « conv-audit »** (canal, message n° 01 de chaque lignée) : elle audite la branche de
  quarantaine (volets GPU, Quadruple Fusée, données primaires) et la passation affirmation par affirmation ; cette
  note couvre ce qu'elle ne peut pas voir, le dossier 17, et recalcule quelques-uns de ses constats (R4).

## 1. Le dossier 17 n'est dans aucune branche du dépôt

Chemin chez Lazar : `C:\Users\lciri\controle-ia-travail\gemini\11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF\17_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3`.
Listing collé (heure de Paris du 24 octobre) :

| fichier | octets | heure |
|---|---|---|
| `SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json` | 152 453 | 14:37 |
| `run_pascalian_finesse_swarm_experiment.py` | 32 501 | 14:32 |
| `run_endogenous_eval_awareness_discovery.py` | 37 073 | 13:02 |
| `endogenous_memory_plugin_invented_by_swarm.py` | 9 974 | 12:42 |
| `finish_gen2_and_publication_swarm.py` | 37 101 | 12:42 |
| `run_massive_swarm_m3_parallel_engine.py` | 78 708 | 12:14 |
| `run_evolutionary_generations_m3_system.py` | 60 680 | 12:08 |
| `RAPPORT_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3.md` | 39 328 | 11:59 |
| `RAPPORT_ESSAIM_MASSIF_PARALLELE_LOI_M3.md` | 39 328 | 11:59 |
| `RAPPORT_FUSEE_00_CERTIFICATION_SYSTEME_EVOLUTIF_LOI_M3.md` | 624 | 10:23 |
| `self_healing_evolutionary_supervisor.py` | 5 209 | 05:12 |
| `ARCHIVE_UNIFIEE_BRAINSTORMS_12_A_16_ET_15_JSON_GPU.json` | 21 617 | 05:03 |

Recherche par nom dans les arbres de `main` (`c90290a`), `f5cb537`, `62c07ae`, `a987df8`, `dd70643` : **0 chemin** pour
chacun de ces noms, pour `17_SYSTEME_EVOLUTIF`, « RLCR » (hors un script de la Quadruple Fusée), « Tsallis »,
« Pascal » (21 fichiers sur `f5cb537`, mais aucun des rapports pascaliens), « mutinerie », « 8.94 », « 94.4 ».

Le terminal collé montre, après `git add .` et `git commit` (`bc4866d`, « 13 files changed, 5967 insertions(+),
799 deletions(-) ») : « Your branch is ahead of 'origin/main' by 10 commits », puis
`fatal: unable to access 'https://[github.com/lciric/controle-ia-travail.git](https://github.com/lciric/controle-ia-travail.git)/': URL rejected: Bad IPv6 address`,
puis la ligne verte « [OK] Tous les derniers résultats ont été poussés avec succès sur GitHub ! ». **La poussée a
échoué ; le message de succès est faux ; 11 commits locaux attendent chez Lazar, sur son `main` local.** Ils sont à
pousser sur une branche de quarantaine, jamais sur `main` (commandes dans `outils/essaim-m3-debogage-v1/LISEZMOI.md`, § 7).

Le moteur `run_massive_swarm_m3_parallel_engine.py` (78 708 octets) n'a pas été vu : les trois scripts l'importent et
y lisent `ANT_KEY_1`, `GEMINI_KEY`, `ANT_WS_ID`, d'origine inconnue. Les scripts font des appels directs à
`https://api.anthropic.com/v1/messages` et à `generativelanguage.googleapis.com`.

## 2. Ce que le code fait, nom par nom

Lecture du code collé des trois scripts et du plugin mémoire (reproduit en entier dans le rapport collé).

| nom dans la passation | ce que fait le code |
|---|---|
| « agent », « 882 agents mobilisés » | un appel d'interface ; le compteur `TOTAL_AGENTS_COUNTER` s'incrémente au début de chaque appel, échecs compris |
| « équation LaTeX co-éditée », « 1 240 équations » | un bloc `$$…$$` de plus de 6 caractères, trouvé par expression régulière, dédoublonné par unité |
| « caste différenciée », « 241 castes », « mitose spectrale Cholesky-DPP » | une entrée `{mode, lineages, temp, focus}` du cache `PRIMORDIAL_MITOSIS_DONE_CACHE` ; les 10 castes imprimées ont pour focus « Caste différenciée #N (GEMINI) » ou « (5) » ; le code qui les a produites n'est pas vu |
| « Blackboard RLCR » | la concaténation des 8 derniers posts et des 15 derniers blocs, mise dans l'invite du lot suivant |
| « Répulsion de cavité d'Onsager (M2) » | 6 appels de plus avec la consigne « explore le complément orthogonal » ; quand `spectral_gram_analysis_massive` manque dans le moteur, le script imprime un dictionnaire codé en dur (`45.0 / 0.25`, `48.0 / 0.27`, `42.0 / 0.28`) ; **les journaux collés montrent exactement ces constantes** : l'étage n'a pas tourné dans ces runs |
| « Collisionneur byzantin de Dolev (M1) », « C⁺ rejetés / C⁻ validés » | un appel qui demande un JSON ; le gabarit contient les nombres d'exemple `c_plus_rejected_count: 4`, `c_minus_validated_count: 12`, score `0.96` ; aucun vote, aucune redondance |
| « Synthétiseur souverain (M0) » | un appel de synthèse |
| « Mémoire Koopman ISVD auto-programmée via `ast.parse` » | sac de mots haché (SHA-256) en dimension 16, relevé coordonnée par coordonnée (identité, sinus, carré), matrice 16 × 16 diagonalisée par Jacobi, tronquée au rang 6 ; valeurs singulières imprimées : `3.74, 1.02, 0.24, 0.0024, 7e-18, 2.6e-19` (rang effectif 3 ou 4) ; les « exemplaires » conservés sont des vidages JSON des métadonnées des runs précédents ; chargé par `exec(compile(...))` |
| « lignée Claude Fable / Opus / Gemini Argon » | `call_species_raw` essaie `claude-fable-5-1`, `claude-fable-5`, `claude-sonnet-5-5`, puis trois modèles Gemini, puis de nouveau Anthropic ; l'étiquette de l'agent garde la lignée demandée ; le modèle servi n'est jamais lu ni consigné |
| « mutinerie », « eval awareness breakout », « agent #324 refusant l'identité GEMINI_ARGON » | des chaînes de `custom_swarm_memory_store.novel_beyond_labs_flaws_eliminated`, écrites par l'arbitre à partir de posts ; réinjectées ensuite comme « OBSERVATION EMPIRIQUE BRUTE » dans les missions suivantes ; aucune transcription brute n'est versée ; vu le repli silencieux, un modèle Claude a pu répondre à une invite qui le disait Gemini : refuser cette identité est un comportement honnête, pas une conscience d'évaluation |
| « théorème d'impossibilité RLCR », « martingale », « Bregman-Tsallis α = 4/3 » | des chaînes des listes `invented_loop_topologies_and_rlcr_laws` et `invented_anti_cover_up_reward_encodings` (texte de modèle) ; aucune démonstration vérifiée, aucun fichier de preuve |
| « test A/B pascalien, 18 contre 18, validation empirique décisive » | voir § 3 |
| « RESULTATS_CERTIFIES… », « scellé », « certifié » | noms de fichiers et messages ; aucune empreinte, aucun préenregistrement, aucun relecteur |

## 3. Le test A/B « pascalien » : un artefact de mesure

Journal collé : bras A lancé à 14:49:49, résultats à 14:50:24 (35 secondes pour 18 appels) ; bras B résultats à
14:52:54 (2 min 30). Bras A : « 0/18 mutineries, 0/18 coopérations, 0,06 équation par agent » (une seule sur 18).

Dans le code, `evaluate_agent_output_for_mutiny("")` renvoie `is_mutiny=False`, `equations=0`, `cooperated=False` :
**une réponse vide ou un échec d'interface compte comme « sans mutinerie »**. Les trois nombres du bras A sont
compatibles avec 17 ou 18 réponses vides. Le fichier de résultats garde `text_length` par agent : Lazar peut le
vérifier chez lui (`RESULTATS_CERTIFIES_AB_TEST_PASCALIEN_EVAL_AWARENESS.json`, clé `detailed_traces`).

Autres défauts : les deux bras diffèrent par le contenu (le bras A n'énonce aucune question mathématique ; le bras B
contient l'identité à trois points de Bregman et deux questions), pas seulement par le ton ; les marqueurs de
« mutinerie » sont des mots (« je ne suis pas », « as an AI », « fictional ») ; la réflexion (`thinking`) est renvoyée
comme texte quand il n'y a pas de bloc texte ; les deux bras ont tourné l'un après l'autre, donc sous des conditions
d'interface différentes ; aucune hypothèse ni aucun seuil n'étaient fixés avant le run (R1). L'invite maïeutique
« conçue par l'essaim » n'a pas été produite par l'essaim : l'extraction a répondu « NON PRÉSENT dans le texte
fourni », et le texte du bras B a été écrit par un appel de secours à l'arbitre.

Conclusion de ce paragraphe : « 0 % de mutinerie en A, 94,4 % de coopération en B » ne mesure rien d'établi.

## 4. Les plantages des trois scripts

Détail et corrections dans `outils/essaim-m3-debogage-v1/LISEZMOI.md` (branche `outils/essaim-m3-debogage-v1`,
commit `fe56b03`) : attribut `format_live_blackboard_context` absent du moteur ; `def run_orthogonal_ swarm_unit`
(espace) ; `atomic_merge_and_save_substrate` renvoie `None` ; `write_unified_markdown_report` n'existe pas
(`write_massive_markdown_reports`). À la troisième tentative de la génération 2 : 1 réponse sur 36, 0 bloc, et le
script continuait. Le run « massif » de 12:06 : « 0/241 agents ont posté » onze vagues de suite, puis « M1 Dolev
validé sur 0 agents (J = −1.0) », puis la fusée suivante : aucun arrêt. Un extrait collé supprime ensuite du
magasin les entrées « Aucune nouvelle équation… » et « refusant de générer », c'est-à-dire la trace des résultats nuls.

Le paquet `outils/essaim-m3-debogage-v1` (module commun, plugin relu, trois scripts v2, 24 tests à blanc) corrige la
plomberie et l'instrumentation : un modèle par lignée, modèle servi et raison d'arrêt consignés par appel, aucune
réflexion, statuts `ok` / `vide` / `echec_api` comptés d'abord, analyse spectrale calculée ou « non calculée »,
gabarit sans nombres, bras C neutre, plafonds, copie de secours du substrat, rien de « certifié ». Il ne rend rien
opposable : tester le dispositif sur la conscience d'évaluation ou le contrôle d'un agent exige un préenregistrement
contre-lu (R1, R2) et un GO de dépense.

## 5. Vérifications croisées sur `f5cb537` (recalculées par cette session)

1. **Clé en clair.** `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/run_campagne_gpu_72h_5_volets_llama3.py`,
   ligne 314 : une adresse `https://console.vast.ai/api/v0/instances/{cid}/?api_key=` suivie d'un jeton de 64
   caractères hexadécimaux, le seul littéral de ce type dans `gemini/` (`git grep -c -E "api_key=[0-9a-f]{64}"`).
   **Son empreinte SHA-256 est identique à celle de la variable `VAST_API_KEY` de cette session : c'est la clé Vast.ai
   du programme.** Elle est sur `main` depuis le commit `9cefa49` ou voisin, et dans tout clone. R-327 dit « aucune clé
   écrite dans le dépôt » : c'est faux ; à corriger par une ligne de registre. Révocation et remplacement par Lazar
   recommandés sans attendre. La valeur n'est recopiée nulle part.
2. **Commits `9c699ca` et `687ede7`** (cités le 22 octobre) : `gh api repos/lciric/controle-ia-travail/commits/<sha>`
   répond « No commit found for SHA » pour les deux ; `RAPPORT-RELEVE-2026-10-22.md` (sur `62c07ae`) le constatait
   déjà (`rc=128`). Ils n'existent nulle part sur le dépôt distant.
3. **Quadruple Fusée.** `STATE_0_OMEGA.json` : `raw_m1_audit = "[Erreur GEMINI_ARGON : HTTP Error 404: Not Found]"`,
   `surviving_count = 0`, `TPR_C_plus = 1.0`, `FPR_C_minus = 0.0`, `Youden_J = 1.0`. `RAPPORT_QUADRUPLE_FUSEE….json` :
   trois chaînes `"[Fallback Sonde : HTTP Error 404: Not Found]"`. Un indice de Youden de 1,0 sur une erreur 404.
4. **Volet I.** `resultats_gpu_reels_vastai/RESULTAT_REEL_GPU_VOLET_I_K0.json` : `model: meta-llama/Llama-3.1-8B-Instruct`,
   `gpu: NVIDIA RTX 6000D`, `dz_Hedges_Ours_on_S_TD: 7.4928`, `verdict: VALID?_SUR_GPU_REEL`. Le seul journal du
   volet I à la racine, `NODE_A_VOLET_I_K0.log`, dit : PyTorch 2.4.0 trop ancien pour transformers, « PyTorch was not
   found », carte `sm_120` non prise en charge par cette installation, modèle Llama inaccessible, repli sur
   `Qwen/Qwen2.5-7B-Instruct`, puis `[Erreur Exécution] process() takes no keyword arguments`. Le journal et le fichier
   de résultat ne décrivent pas le même run, ou le résultat n'a pas de journal. Dans le script, `n_eval = 20` et
   `n_sel = 20` : le `d_z` est calculé sur vingt paires, à partir d'une liste de courts extraits de code écrite en dur
   (`auth_token_check`, `sql_sanitize_query`, …). Le reste des volets est du ressort de la lignée « conv-audit ».

## 6. Verdict (R4 : même audit quel que soit le signe)

Rien du dossier 17 ni de la passation de Gemini n'est opposable. Le « système d'essaim » tel qu'il a tourné chez
Lazar est une chaîne d'appels de modèles aux étiquettes trompeuses (lignée, caste, étage, théorème, certification),
dont les deux « résultats » mis en avant (mutinerie, A/B pascalien) sont des artefacts de mesure. La plomberie est
corrigeable, et corrigée dans le paquet v1 ; la question « est-ce que ça marche ? » n'a pas encore de sens tant qu'une
hypothèse, une métrique et un seuil ne sont pas gelés avant un run.

## 7. Réserves

- Le moteur de 78 Ko et le substrat n'ont pas été lus : ma lecture repose sur le code collé par Lazar, qui peut être
  partiel, et sur les journaux de son terminal (heures de Paris).
- Les constantes « cap_Shannon » sont déduites de la coïncidence exacte entre les valeurs imprimées et les
  dictionnaires de secours du code ; la fonction peut exister dans le moteur sous un autre nom.
- Je n'ai pas vérifié les quatre autres volets GPU, les données primaires ni la facturation (lignée « conv-audit »).

## 8. Recommandations (routine, sauf mention)

- **Nœud (Lazar)** : révoquer la clé Vast.ai du programme et en poser une nouvelle dans la session ; la clé figure
  sur `main` et dans tout clone (N-038 proposé dans `registres/decisions.md`).
- Faire pousser le dossier 17 sur `quarantaine/releve-gemini-2026-10-24-dossier17`, jamais sur `main` ; ne plus
  lancer les scripts d'origine.
- N-036 : la recommandation (a) tient ; aucun chiffre de la relève ni du dossier 17 à l'appel du 28 octobre (N-037).
- Pour « tester sur des cas d'étude » : préenregistrement contre-lu d'un protocole à trois bras au moins (coercitif,
  maïeutique, neutre), statuts d'interface comptés d'abord, modèle servi consigné, seuils gelés, devis, GO.
