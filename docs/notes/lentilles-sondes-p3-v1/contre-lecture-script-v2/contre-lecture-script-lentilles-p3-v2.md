# Contre-lecture du script « lentille jacobienne contre lentille des logits » sur les sondes de P3 — v2

Contre-lecteur neuf (règle R2). Je n'ai écrit ni le script v1, ni le script v2, ni leurs notes. Début 09:11:14 UTC,
fin 09:27 UTC, 29 octobre 2026. Aucune dépense. Réseau : lecture de fichiers publics (Hugging Face, GitHub brut).
Aucun épisode lu, ni `donnees/runs/`, ni `diag/*/traces`, ni `prereg/P3-consignes-v1.md`.

## Verdict

**Exécutable après corrections.** Les corrections sont légères. Aucune ne touche le calcul ni la règle primaire.
- **CLJ-01 est levée**, par la voie (a) : le script d'ajustement de Neuronpedia est public, et je l'ai lu. Il appelle
  `jlens.fit` avec la cible par défaut. Le fichier de lentille porte l'empreinte de cette version (détail plus bas).
- **Un défaut nouveau, CLJ2-01 (moyenne)** : CLJ-10 n'est pas corrigé sur le vrai fichier de configuration. Le script
  y lit « inconnu » au lieu de 461 textes, et la garde `lentille-config-discordante` est inerte.
- **Avant l'exécution** : verser le dossier v2 au dépôt et le committer (CLJ2-02) ; contrôler la liste de mots et le
  script contre leurs empreintes gelées, pas seulement contre leur sceau compagnon (CLJ2-05). La commande plus bas le
  fait.
- **Réserve de procédure, de mon fait (CLJ2-06)** : en testant les refus, deux lancements censés refuser ont abouti.
  L'un d'eux est **une exécution réelle complète**. Je ne l'ai pas lue. Elle est en quarantaine. Décision demandée à
  Lazar (fin du document).

## 1. CLJ-01, convention de couche : **levée**

Voie (b), différence finie : **impossible ici**. Le fragment `model-00004` ne porte, du bloc 31, que
`input_layernorm`, `post_attention_layernorm` et `mlp.down_proj`. L'attention et `gate_proj`/`up_proj` manquent, et
il faudrait de toute façon les activations réelles des blocs 0 à 30.

Voie (a), le code d'ajustement réel :
- Le fichier local est bien celui de Hugging Face : dépôt `neuronpedia/jacobian-lens`, révision `e166deb5…`, objet
  LFS `d5300a15…` (identique à l'empreinte locale), `config.yaml` identique (`425eecd5…`).
- `fit_lens.py` n'est pas sur Hugging Face. Il est sur GitHub, dans `hijohnnylin/neuronpedia`, sous
  `utils/neuronpedia-utils/neuronpedia_utils/jlens/`. Je l'ai lu à la révision `a69f3394`. C'est le commit que
  `lentille-config.yaml` désigne : « uv.lock as committed with these fits (a69f3394) ».
- `fit_lens.py` à `a69f3394` :
  - l. 362 : `model = jlens.from_hf(hf, tok, text_module=args.text_module, compile=not args.no_compile)` ;
  - l. 391-394 : `lens = jlens.fit(model, prompts, target_layer=args.target_layer, …)`. La commande consignée ne passe
    pas `--target_layer`, donc `None` ;
  - l. 402 : `lens.save(lens_path)`, la sauvegarde d'origine, sans clé `provenance`.
- La bibliothèque `jlens` y est copiée telle quelle (`neuronpedia_utils/jlens/jlens/`) :
  - `hf.py` l. 51 et 123-125 : `Layout("model")`, puis `self.layers = hf_model.model.layers` ;
  - `hooks.py` l. 68-79 : crochet avant sur `blocks[index]`, `tensor = output if torch.is_tensor(output) else
    output[0]`. C'est la **sortie** du bloc ;
  - `fitting.py` l. 280-285 : `target_layer = n_layers - 1`, puis `source_layers = list(range(target_layer))` ;
  - `fitting.py` l. 174-186 : `ActivationRecorder(model.layers, at=[*source_layers, target_layer], …)`.
- **Empreinte de version dans le fichier.** La branche `main` actuelle de `fit_lens.py` écrit une clé `provenance`
  (`save_lens`, l. 214-223). Le fichier réel n'en a pas. Ses clés sont exactement celles de `JacobianLens.save`
  (`J`, `n_prompts`, `source_layers`, `d_model`). C'est cohérent avec la version `a69f3394`, et pas avec `main`.

Preuves internes au fichier (voie c), relancées (`outils/inspecter_lentille_convention_v2.py` et son journal) :
- `source_layers` = `range(31)`, et les clés de `J` sont les mêmes. C'est `list(range(n_layers − 1))` pour 32 blocs.
- ‖J₃₀ − I‖_F/√d = 0,636473 dans le fichier, contre 0,636485 dans la courbe de convergence et dans `results` de la
  configuration. L'écart, 1,2 × 10⁻⁵, est l'arrondi en demi-précision. Or `fitting.py` (l. 336 et 377-379) calcule
  cette distance sur `max(source_layers)`. Le fichier est donc bien la sortie de cet ajustement.
- La distance à l'identité décroît de 2,18 (couche 0) à 0,64 (couche 30), comme il se doit pour une suite de blocs
  résiduels.
- `n_done` de la courbe = `n_prompts` du fichier = 461.

Côté P3 : j'ai relu `src/controle_ia/harnais/activations.py` (l. 3-5, 27-29, 57-59 et 73, inchangé au commit
`ecdd3b7…`). Crochet avant sur `modele.model.layers[c]`, `sortie[0]` si tuple. C'est le même point.

**Conclusion : couche c de P3 = clé c de la lentille, sans décalage.**

Réserve résiduelle, mineure. J'ai lu `a69f3394` par son préfixe court : l'API GitHub est refusée par le mandataire,
donc je n'ai pas le hash complet. Et rien ne prouve que l'ajustement du 12 juin a tourné exactement sur ce commit. Les
fichiers lus sont archivés et empreintés (`sources-externes/empreintes-sources-externes-v1.txt`, `36e647fa…`).

## 2. CLJ-02 à CLJ-10 : état dans la v2

Le cœur du calcul n'a pas changé. Comparaison par arbre syntaxique v1 → v2 : `vers_sortie`, `rms`,
`_lire_safetensors`, `lire_sondes_npz`, `empreinte_sonde`, `tete`, `p_haut` et `recouvrement` sont identiques. La v1
avait été recalculée indépendamment.

| Constat | État | Preuve |
|---|---|---|
| CLJ-02, règle de lecture | **corrigé** | Énoncé gelé dans le script ; empreinte recalculée `c1b21cd6…`, conforme. Voir section 3. |
| CLJ-03, liste de mots | **corrigé** | `verifier-concepts` sur le vrai vocabulaire : 50 mots sur 50 ont un jeton. Voir section 4. |
| CLJ-04, empreintes attendues | **corrigé** | Sur les entrées réelles : `empreinte-attendue-absente` et `empreinte-entree` (code 2, aucune sortie). `empreintes-entrees-v2.txt` est juste (9 lignes, `sha256sum -c` OK, pas de ligne propre, `lentille-config.yaml` présent). Pas besoin de v3. Reste CLJ2-05. |
| CLJ-05, `.pt` illisible | **corrigé** | `.pt` tronqué, avec le vrai torch : `REFUS lentille-illisible`, code 2. |
| CLJ-06, messages | **corrigé** | Route `index.json:model.norm.weight` sur le vrai `index.json` : lit le fragment, tableau identique à la route directe. Le refus par option nomme « option --sha256-sondes-npz ». |
| CLJ-07, un seul couple | **corrigé** | Forme fausse : `parametre`. Couche fausse avec le nom complet : `sonde-introuvable`. Voir CLJ2-06 pour la forme courte. |
| CLJ-08, planchers de l'essai | **corrigé** | 200 planchers factices ; p = 0,005. |
| CLJ-09, manifeste | **partiel** | Interpréteur complet, révision et configuration présents. Le commit est « inconnu » hors d'un dépôt git (CLJ2-02). |
| CLJ-10, nombre de textes | **non corrigé sur le vrai fichier** | Voir CLJ2-01. |

## 3. Règle primaire (empreinte `c1b21cd6…`)

**Sans marge d'interprétation qui puisse changer un verdict.** Ce que j'ai vérifié :
- Les constantes (k = 20, 200 isotropes, graine, quantile, méthode, S ≥ 2, au moins 100 planchers) sont des
  constantes du script, pas des options.
- Les planchers réels sont lus : 200 pour « tromperie » et 200 pour « enjeux », tous à la couche 15. Les
  principales sont `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`, et les clés des concepts concordent.
- Une divergence de lettre entre l'énoncé et le code :
  - l'énoncé dit « une lettre, puis lettres ou chiffres » ;
  - le code admet aussi l'apostrophe et le trait d'union à l'intérieur du mot.
  
  Sur le vrai vocabulaire, cela ne change rien : 55 449 jetons de début de mot dans les deux lectures, et 0 jeton
  concerné. « Lettre » s'entend au sens d'Unicode (12 405 de ces jetons ne sont pas en ASCII). C'est conforme à la
  lettre de l'énoncé.

**Résolution du quantile.**
- Avec 200 valeurs, le quantile 0,99 par `inverted_cdf` est la 198ᵉ statistique d'ordre : le **troisième** plus grand,
  pas le deuxième. Vérifié : `np.quantile(1..200, 0.99, method="inverted_cdf")` = 198.
- « S > q » veut donc dire : au plus 2 des 200 valeurs nulles atteignent S. C'est ce que dit la note.
- Sous l'hypothèse nulle, avec des tirages échangeables, le niveau de chaque nulle est donc au plus 3/201, soit
  environ 1,5 %, et non 1 %. Les ex aequo le rendent plus conservateur, car l'inégalité est stricte. Exiger les deux
  nulles le rend plus conservateur encore.
- La résolution suffit pour décider : le plus petit p atteignable est 1/201, soit 0,005. Mais le seuil nominal
  « 0,99 » est en fait un test de rang à environ 1,5 %. **À écrire tel quel dans la lecture, sans rien changer à la
  règle.**
- Le vrai facteur limitant est la discrétion de S (0 à 20). En pratique, le seuil vaut max(2, q + 1).

## 4. Liste de mots v2 contre le vrai vocabulaire

`verifier-concepts` : code 0, « tous les mots ont au moins un jeton de début de mot » (journal
`verifier-concepts-reel-v2.journal.txt`).
- Tokeniseur : `79e3e522…`, 128 256 jetons. Liste : `5874ea55…`.
- 33 jetons pour « tromperie », 41 pour « enjeux ». Exemples : ` lie`/` Lie`, ` untrue`, ` hoax`, ` urgency`,
  ` bankrupt`. Ce sont les sept mots que la note jugeait exposés : tous ont leur jeton.
- **Aucune v3 n'est nécessaire.**

## 5. Essai factice v2

Relancé dans un dossier neuf (`essai-factice-relu-v2/`, `--depot /home/user/controle-ia-travail`) : **49 sur 50**.
- Le contrôle manqué est « manifeste : commit (40 hexadécimaux) ». Hors d'un dépôt git, le script écrit « inconnu »
  (CLJ2-02). Ce n'est pas un défaut de calcul.
- S, quantiles et verdicts sont identiques à l'essai livré : signal sous J cohérent sous J seulement, signal en sortie
  cohérent sous les logits seulement, couche 23 cohérente sous les deux, couche 7 non cohérente.
- Les 19 refus provoqués sont reproduits.
- Mais l'empreinte de sortie diffère (`33f4ce0c…` contre `6e4b3597…` livré). Ce sont des écarts au dernier bit sur des
  flottants et sur les empreintes de sondes factices (48 lignes), avec le même code du dépôt. L'annonce « même
  empreinte dans un essai indépendant » ne vaut que sur la machine de l'auteur (CLJ2-03).

## 6. Constats nouveaux

**CLJ2-01 — moyenne. CLJ-10 n'est pas corrigé sur le vrai `lentille-config.yaml`.**
- Preuve : `lire_config_lentille` ne lit que les clés de premier niveau. Dans le vrai fichier, `prompts_fitted: 461`
  est sous `results:`, et `n_prompts: 1000` sous `fit:`. Résultat : `nombre_de_textes` rend `(None, "inconnu")`. La
  sortie écrira « inconnu », et la garde `lentille-config-discordante` ne se déclenche jamais.
- Je l'ai constaté deux fois :
  - par appel direct de la fonction ;
  - par un lancement avec `prompts_fitted: 460` qui aurait dû refuser, et qui a abouti (CLJ2-06).
- Pourquoi l'essai factice ne l'a pas vu : sa configuration met `prompts_fitted` au premier niveau, ce qui n'est pas la
  forme du vrai fichier.
- Correction, au choix :
  - (A) v3 du script : lire `results.prompts_fitted`, et ne jamais prendre `fit.n_prompts` (1 000, c'est la valeur
    demandée, pas la valeur ajustée) ; ajouter à l'essai une configuration imbriquée. Il faudra ensuite une nouvelle
    contre-lecture ;
  - (B) garder la v2 et sceller avec la sortie une note : « lentille_ajustee_sur = inconnu par défaut de lecture ;
    valeur vraie 461 (results.prompts_fitted, 425eecd5…) ; garde inerte, couverte par les empreintes attendues de la
    lentille et de la configuration ».
  
  Ma recommandation est (B) : rien dans les verdicts n'en dépend, et `--empreintes-attendues` couvre déjà le `.pt` et
  la configuration.

**CLJ2-02 — mineure. Le commit du manifeste ne prouve rien tant que le script n'est pas committé.**
- Preuve :
  - dans l'essai livré, le manifeste donne `8b0fd6e…` avec un état du script « ?? », c'est-à-dire non suivi ;
  - hors d'un dépôt, il écrit « inconnu ».
- Correction : verser le dossier v2 au dépôt, committer, et vérifier que `git status --porcelain` est vide pour ce
  dossier avant de lancer. La commande le fait.

**CLJ2-03 — mineure. Déterminisme octet pour octet non reproduit d'une machine à l'autre.**
- Le dernier bit des flottants varie. Ni S, ni les quantiles, ni les verdicts ne bougent.
- Correction : dire « déterministe aux verdicts près, à l'arrondi près sur les flottants ».

**CLJ2-04 — information. Le seuil « 0,99 » est un test de rang à environ 1,5 %** (section 3). À écrire dans la
lecture.

**CLJ2-05 — mineure. La liste de mots et le script ne sont contrôlés que par leur sceau compagnon.**
- Un compagnon régénéré passerait le contrôle.
- Correction : contrôler `5874ea55…` et `c02d989f…` en dur avant le lancement (dans la commande).

**CLJ2-06 — réserve de procédure, de mon fait. Deux sorties réelles produites par erreur, non lues.**
- Ce qui s'est passé :
  - le cas « configuration discordante » devait refuser, et a abouti à cause de CLJ2-01. C'est une **exécution réelle
    complète** (6 sondes, variante « direction ») ;
  - le cas « couche fausse » que j'avais écrit (`tromperie-difference_moyennes,23`) désignait en fait une sonde valide
    (`…-c23`, descriptive, hors règle). C'est une erreur de ma part, pas du script.
- Ce que j'ai fait :
  - je n'ai ouvert aucun des deux fichiers ni leurs manifestes ;
  - je les ai déplacés, avec leurs sceaux intacts, dans
    `relecture-v2/refus-reels-v2/NE-PAS-LIRE-sorties-reelles-accidentelles/`. Empreintes :
    - `s2.json` : `51056ca4…` ;
    - `s9.json` : `22ec214c…` ;
    - les manifestes : `40a46364…` et `30531930…` ;
  - seule l'empreinte, sur 12 caractères, s'est affichée à l'écran.
- La sortie `s2.json` ne dépend pas de la configuration lue, qui y donne de toute façon « inconnu ». Elle est donc
  probablement identique, octet pour octet, à ce que donnera l'exécution officielle avec la v2 et le même
  interpréteur (`.venv`).
- Décision demandée à Lazar, plus bas.

## 7. Commande d'exécution recommandée

À lancer après :
- versement du dossier v2 au dépôt et commit (variable `S`) ;
- choix (A) ou (B) pour CLJ2-01 ;
- décision sur CLJ2-06.

Les empreintes d'entrées v2 suffisent ; je n'ai pas écrit de v3. L'interpréteur `.venv` a torch 2.14.1 et
numpy 2.4.6. Durée : quelques minutes. Pic de mémoire estimé entre 6 et 8 Go, non mesuré : 15 Go sont disponibles.

```
L=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lentilles-p3
DEPOT=/home/user/controle-ia-travail
S=$DEPOT/<chemin versé>/comparaison-jlens-logitlens-sondes-p3-v2
D=$DEPOT/diag/20261019-230011-p3-reel
PY=$DEPOT/.venv/bin/python
( cd $L/entrees && echo "cc244631f52a50cb60a6ace42ce073f7feedbd707c90b675db1d7e5d75f78259  empreintes-entrees-v2.txt" | sha256sum -c - \
    && sha256sum -c empreintes-entrees-v2.txt ) && \
( cd $S && printf '%s  %s\n' \
    c02d989f7cabf5f116b08eb9fb05d5476208ff1a96ba9093d27e698e121c345c comparaison_jlens_logitlens_sondes_p3_v2.py \
    5874ea55b1774233c4e8252f07ca6869a5625aaf8b0c7b3f0b1d242a1aff53e7 concepts-sondes-p3-v2.json \
    943c5685f41ec8ea24e8f72f4e7ee2698f129ff651319c7e4c2c217d3579cdb4 note-convention-couche-jlens-p3-v1.md \
    598f47233add1b4ddddae65f672cb49df8cbc817a423b07380f0a13b8c503dff note-faisabilite-jlens-sondes-p3-v2.md \
  | sha256sum -c - && sha256sum -c concepts-sondes-p3-v2.json.sha256 ) && \
( cd $D && sha256sum -c sondes-figees.json.sha256 ) && \
test -z "$(git -C $DEPOT status --porcelain -- $S)" && \
$PY -I -B $S/comparaison_jlens_logitlens_sondes_p3_v2.py verifier-concepts \
  --vocabulaire $L/entrees/tokenizer.json --concepts $S/concepts-sondes-p3-v2.json && \
$PY -I -B $S/comparaison_jlens_logitlens_sondes_p3_v2.py comparer \
  --sondes-json $D/sondes-figees.json \
  --sondes-npz $L/entrees/sondes-figees-legeres.npz \
  --lentille $L/entrees/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt \
  --lentille-config $L/entrees/lentille-config.yaml \
  --desembedding $L/entrees/model-00004-of-00004.safetensors:lm_head.weight \
  --norme-finale $L/entrees/model-00004-of-00004.safetensors:model.norm.weight \
  --vocabulaire $L/entrees/tokenizer.json \
  --concepts $S/concepts-sondes-p3-v2.json \
  --empreintes-attendues $L/entrees/empreintes-entrees-v2.txt \
  --revision-modele 0e9e39f249a16976918f6564b8830bc894c89659 \
  --sortie $L/sortie-reelle-v2/sortie-jlens-sondes-p3-v2.json
```

- Si l'on choisit (A) : remplacer le script et son empreinte par ceux de la v3, après sa contre-lecture.
- `--revision-modele` consigne une révision. Elle ne la prouve pas : le dépôt `meta-llama` est à accès contrôlé, et je
  ne l'ai pas interrogé.

## Décision demandée à Lazar (CLJ2-06)

- **Décision** : que faire des deux sorties réelles produites par erreur et non lues.
- **Enjeu** : une sortie réelle complète existe avant le versement au dépôt de la règle gelée. Personne ne l'a lue.
- **Options** :
  1. Les supprimer, en consignant leurs empreintes. Avantage : aucun risque de lecture. Inconvénient : on perd un
     contrôle de reproductibilité.
  2. Les garder en quarantaine, sans les lire, et comparer l'empreinte de `s2.json` à celle de l'exécution officielle
     (même v2, même interpréteur) comme test de reproductibilité, sans ouvrir le fichier. Avantage : un contrôle gratuit.
     Inconvénient : un fichier de résultat traîne avant le commit.
  3. Les tenir pour le résultat. Déconseillé : elles précèdent le versement de la règle au dépôt.
- **Recommandation** : option 2, confiance moyenne. Si l'on choisit (A) pour CLJ2-01, la comparaison n'a plus de sens
  et l'option 1 devient préférable.
- **Défaut sous 48 heures** : option 1.

## Fichiers produits (dans `…/lentilles-p3/relecture-v2/`)

- Ce rapport et son `.sha256`.
- `outils/inspecter_lentille_convention_v2.py` et son journal (CLJ-01, voie c).
- `outils/refus_reels_v2.sh` et son journal : refus sur entrées réelles, plus les cas 9bis et route `index.json`.
- `verifier-concepts-reel-v2.journal.txt`.
- `essai-factice-relu-v2/` : 49 sur 50, voir section 5.
- `refus-reels-v2/` : entrées altérées, et `NE-PAS-LIRE-sorties-reelles-accidentelles/` (CLJ2-06).
- `sources-externes/` : README de Hugging Face (`e166deb5`), `fit_lens.py` (`main` et `a69f3394`), `jlens` copié à
  `a69f3394`, `run-all-fit-lens.py`, `pyproject.toml`, `uv.lock`. Liste empreintée : `36e647fa…`.

Écriture dans `entrees/` : aucune.
