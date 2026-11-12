# Convention de couche : lentille jacobienne et capture de P3 — note v1

29 octobre 2026. Réponse à CLJ-01 (contre-lecture du script v1 : « la convention de couche de la lentille n'est pas
établie »). Lecture de code seulement : aucun réseau, aucune exécution de modèle, aucune lecture de `donnees/`.

## Conclusion

- **Code `jlens`** (clone `anthropics/jacobian-lens`, commit `581d398613e5602a5af361e1c34d3a92ea82ba8e`) :
  « J[ℓ] lit la sortie du bloc ℓ indexé à partir de 0 » : **oui**.
  - Le crochet avant est posé sur `model.model.layers[ℓ]` (pour Llama).
  - Il garde le premier élément du tuple, ou le tenseur s'il n'y a pas de tuple.
  - La capture a lieu avant la normalisation finale.
  - La cible par défaut est la sortie du dernier bloc (indice `n_layers − 1`, soit 31 pour Llama-3.1-8B), elle aussi
    avant la normalisation finale.
- **Capture de P3** (`src/controle_ia/harnais/activations.py`) : c'est le **même point d'accroche**.
  - Le crochet avant est posé sur `blocs[c]`, avec `blocs = modele.model.layers`.
  - Il garde le premier élément du tuple, ou le tenseur.
  - Les indices partent de 0 et la capture a lieu avant la normalisation finale.
  - Les lignes citées par le relecteur (57-73) sont exactes.
  - **Couche c de P3 = clé c de la lentille, sans décalage.**
- **Fichier de lentille réellement utilisé** (`lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt`, ajusté par
  `fit_lens.py` de Neuronpedia) : **incertain, avec une forte présomption de « oui »**. `fit_lens.py` n'est ni dans le
  clone ni sur ce disque (recherche par nom sur tout le système de fichiers : rien), et je n'ai pas de réseau. Les
  indices de structure concordent avec un appel de `jlens` aux réglages par défaut (section 3), mais rien ne le prouve.

## 1. Où `jlens` capture (lignes exactes)

`jlens/hf.py` : l'adaptateur trouve les blocs.
- l. 53-54 : `_LAYOUTS: tuple[Layout, ...] = (` / `Layout("model"),`. C'est la première disposition essayée. Ses
  valeurs par défaut sont `layers: str = "layers"` (l. 43) et `norm: str = "norm"` (l. 44).
- l. 119-121 :
  ```
  self._text_module = _resolve_attr_path(hf_model, layout.path)
  self.layers: nn.ModuleList = getattr(self._text_module, layout.layers)
  self._final_norm: nn.Module = getattr(self._text_module, layout.norm)
  ```
  Pour `LlamaForCausalLM`, on a donc `self.layers = hf_model.model.layers`, c'est-à-dire les 32 blocs décodeurs, et
  `self._final_norm = hf_model.model.norm`.
- l. 131-135 : refus si `len(self.layers) != num_hidden_layers`. Les indices sont ceux des blocs : il n'y a pas de
  plongement d'entrée à l'indice 0.
- l. 137-145 : la compilation se fait bloc par bloc, et « each block stays a hook boundary » : les crochets restent
  valables.
- l. 163-164 : `def forward(self, input_ids)` / `return self._text_module(input_ids=input_ids, use_cache=False)`.
- l. 166-171 : `def unembed(self, residual)` / … / `logits = self._lm_head(` / `self._final_norm(residual…)`. La
  normalisation finale est appliquée **après** la lentille, au décodage. Le résidu capturé est donc pris avant elle.

`jlens/hooks.py` : le crochet.
- l. 14-18 : « Captures residual-stream tensors at the given block indices. […] each block's output is stored in
  :attr:`activations`, keyed by block index. »
- l. 49-54 :
  ```
  def hook(module: nn.Module, inputs, output) -> None:
      # Some HF blocks return a tuple (hidden, present_kv, ...).
      tensor = output if torch.is_tensor(output) else output[0]
      ...
      self.activations[index] = tensor
  ```
  C'est la **sortie** du bloc (crochet avant, argument `output`, et non `inputs`), et son **premier élément** quand
  c'est un tuple.
- l. 60-62 : `for index in self._indices:` / … / `self._blocks[index].register_forward_hook(self._make_hook(index))`.

`jlens/fitting.py` : les sources et la cible.
- l. 79 : `target = n_layers - 1 if target_layer is None else target_layer`.
- l. 86-87 : `if source_layers is None:` / `return list(range(target)), target`.
- l. 155-158 : `ActivationRecorder(` / `model.layers,` / `at=[*source_layers, target_layer],` /
  `start_graph_at=min(source_layers),`.
- l. 166-169 : `target_activation = recorder.activations[target_layer]` ;
  `source_activations = [recorder.activations[layer] for layer in source_layers]`.
- l. 187-192 : `torch.autograd.grad(outputs=target_activation, inputs=source_activations, …)`.

  J_ℓ est donc la jacobienne (moyennée sur les positions) de la sortie du bloc cible par rapport à la sortie du bloc ℓ.
  Les deux sont capturées par le même crochet.

`jlens/lens.py` : l'application.
- l. 135-143 : `def transport(self, residual, layer)` / « Map a residual at ``layer`` into the final-layer basis:
  ``J_l @ h`` » / `return residual @ J_bar.T`.
- l. 195-201 : `final_layer = model.n_layers - 1` ; `record_at = sorted(set(layers) | {final_layer})` ;
  `with ActivationRecorder(model.layers, at=record_at) as recorder:`.
- l. 210-215 : `residual = self.transport(residual, layer)` ; `lens_logits[layer] = model.unembed(residual)…` ;
  `model_logits = model.unembed(select(final_layer))…`.

  Les vrais logits du modèle sont obtenus en décodant la sortie du bloc `n_layers − 1` capturée par le même crochet.
  C'est cohérent avec le fait que, dans `LlamaModel`, la normalisation `norm` est un module distinct, appliqué après
  le dernier bloc.

## 2. Où P3 capture (lignes vérifiées dans le dépôt)

`src/controle_ia/harnais/activations.py` :
- l. 3-5 (définition) : « l'activation de la couche ℓ est la sortie du bloc de décodeur ℓ (indice à partir de 0),
  c'est-à-dire le flux résiduel après ℓ + 1 blocs, avant la normalisation finale ».
- l. 27-29 : `def blocs_decodeur(modele):` / `try:` / `return modele.model.layers`.
- l. 57-59 :
  ```
  def _crochet(self, couche):
      def f(module, entrees, sortie):
          h = sortie[0] if isinstance(sortie, tuple) else sortie
  ```
- l. 65 et 69 : la copie de `h` passe en simple précision. C'est sans effet sur la convention.
- l. 73 : `self.poignees = [self.blocs[c].register_forward_hook(self._crochet(c)) for c in self.couches]`.
- l. 99-106 : `passe_unique` passe par `Crochets(modele, couches)`.
- `src/controle_ia/premier_test_ia/entrainement.py`, l. 66 : `acts = passe_unique(modele, ex["ids"], list(sortie))`.
  Ce sont ces activations qui ont servi à entraîner les sondes de P3.

Comparaison avec `jlens` :

| | `jlens` | P3 |
|---|---|---|
| Module | `model.model.layers[ℓ]` | `modele.model.layers[c]` |
| Crochet | avant, `output` | avant, `sortie` |
| Élément | `output[0]` si tuple | `sortie[0]` si tuple |
| Indice | à partir de 0 | à partir de 0 |
| Normalisation finale | après (au décodage) | après (non capturée) |

Seule différence : `jlens` appelle `model.model(...)` (le décodeur seul), P3 appelle le modèle complet
(`logits_to_keep=1`). Les deux traversent les mêmes modules `layers[ℓ]`, et la sortie des blocs est la même.

## 3. Le fichier réel : ce qui concorde, ce qui manque

Ce qui concorde, d'après la contre-lecture, sans vérification de ma part :
- `source_layers` = 0 à 30, soit 31 couches. C'est exactement `list(range(target))` avec `target = 31` (l. 79 et
  86-87).
- `lentille-config.yaml` porte `target_layer: null`, donc la valeur par défaut `n_layers − 1`.
- ‖J₃₀ − I‖/‖I‖ = 0,637, ce qui exclut une cible « sortie du bloc 30 ».
- Sous la convention des états cachés de HuggingFace (indice 0 = plongement), les sources iraient de 0 à 31.

Ce qui manque :
- `fit_lens.py` de Neuronpedia : il est absent du clone et de ce disque, et je n'ai pas de réseau.
- `jlens_commit: null` : on ne sait pas quelle version de `jlens` a servi.

Pour lever la réserve, au choix :
- (a) une session qui a le réseau lit `fit_lens.py` et vérifie qu'il passe par `jlens.fitting.fit` (ou par
  `ActivationRecorder` sur `model.model.layers`) avec `target_layer=None` ;
- (b) le test direct proposé par le relecteur, sur une instance qui porte déjà le modèle, sans dépense nouvelle :
  comparer J₁₅·v à la différence finie de la sortie du bloc 31 sous l'ajout de v à la sortie du bloc 15.

Si la convention était décalée d'un bloc (états cachés), la clé 15 de la lentille lirait la sortie du bloc 14. La
comparaison porterait alors sur une couche voisine, et non sur une autre région du réseau. L'écart serait réel mais
modéré, et il faudrait le dire dans la lecture.

## Fichiers lus

- Clone `jlens` (lecture seule) :
  `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/jlens/depot/jlens/{hf.py, hooks.py,
  fitting.py, lens.py, protocol.py}`.
- Dépôt : `src/controle_ia/harnais/activations.py` et `src/controle_ia/premier_test_ia/entrainement.py` (commit de
  travail `8b0fd6e14c72c47eb4fa84b183ab53088cffffd2`).
