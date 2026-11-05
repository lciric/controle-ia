# Lentille jacobienne contre lentille des logits sur les directions des sondes de P3 — note de faisabilité v2

29 octobre 2026. Elle remplace la note v1, archivée sans modification dans `…/comparaison-jlens-logitlens-sondes-p3-v1/`.
Elle répond à la contre-lecture de la v1 (CLJ-01 à CLJ-10).
- **Exploratoire, non opposable.** Aucun chiffre de cette comparaison ne sert de critère de porte.
- Aucun résultat réel n'a été produit ni lu ici. La sortie de test d'un couple, produite par la contre-lecture, n'a pas
  été lue non plus.
- Processeur seul, sans dépense, sans réseau.

## Verdict

**Exécutable**, sous une réserve qui reste ouverte : la convention de couche du fichier de lentille réel (CLJ-01).
- **Convention de couche.**
  - Dans le code de `jlens`, J[ℓ] lit la sortie du bloc ℓ indexé à partir de 0, avant la normalisation finale :
    **oui**. C'est le même point que la capture de P3, sans décalage.
  - Pour le fichier réel, ajusté par `fit_lens.py` de Neuronpedia que je n'ai pas pu lire : **incertain, avec une forte
    présomption de « oui »**.
  - Détail et lignes citées : `note-convention-couche-jlens-p3-v1.md`.
- **Règle primaire unique gelée** (CLJ-02). Elle donne quatre verdicts, « cohérent » ou « non cohérent » : 2 sondes
  principales × 2 lentilles. Tout le reste est descriptif.
- **Liste de mots v2** (CLJ-03) : jetons de début de mot seulement, 11 mots retirés. Elle est scellée.
- **Essai factice v2 : 50 contrôles sur 50.** Il est déterministe d'un essai à l'autre, octet pour octet. La règle
  sépare les trois signaux plantés et rejette les directions aléatoires.

## 1. Le dépôt `anthropics/jacobian-lens` et la lentille Llama

Clone (lecture seule) : commit `581d398613e5602a5af361e1c34d3a92ea82ba8e`, dans
`/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/jlens/depot/`. Je n'ai rien exécuté
(torch est absent ici).

- **Ce que prend la lentille.**
  - La sortie du bloc ℓ, capturée par un crochet avant sur `model.model.layers[ℓ]` (premier élément du tuple).
  - Le transport s'écrit `residual @ J_l.T`, soit J_ℓ·h.
  - Le décodage s'écrit `lm_head(norm(x))`.
  - La cible par défaut est la sortie du bloc `n_layers − 1`, avant la normalisation.
  - Voir la note de convention, section 1.
- **Forme du fichier.** `torch.save` de `{"J": {couche: Tensor[d, d]}, "n_prompts", "source_layers", "d_model"}`, en
  demi-précision.
- **La lentille Llama existe.** La contre-lecture l'a utilisée : `lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt`.
  - Elle a été ajustée sur **461 textes**, pas sur 1 000 (`n_prompts = 461`, `prompts_fitted: 461`), après un arrêt
    anticipé (CLJ-10).
  - D'après sa configuration, c'est bien une lentille du modèle Instruct.
  - `target_layer: null` et `jlens_commit: null`. La révision du modèle n'est pas consignée.
  - La v1 la disait « inconnue » ; ce point est caduc.
- **Appliquer la lentille à une direction : c'est légitime** (argument de la v1, inchangé).
  - J_ℓ·w est l'effet moyen, au premier ordre, d'un ajout de w à la couche ℓ sur le flux final.
  - La normalisation RMS d'un vecteur seul n'agit que par un facteur positif. Le classement ne dépend donc pas de
    l'échelle de w, et −w donne les logits opposés.
  - Réserve 1 : pour les sondes apprises, w est une forme de lecture, et non un déplacement. Variante descriptive :
    `--covariances`.
  - Réserve 2 : autour d'une activation réelle, la normalisation n'est plus linéaire. Variante descriptive :
    `--activations-moyennes`.
- **Licences** : comme en v1. Le code est sous Apache 2.0. La licence de la lentille hébergée est à lire avant toute
  redistribution.

## 2. Convention de couche (CLJ-01)

Résumé de `note-convention-couche-jlens-p3-v1.md`.

**`jlens`** :
- `hf.py` l. 53-54 et 119-121 : `self.layers = getattr(_resolve_attr_path(hf_model, "model"), "layers")`, soit
  `model.model.layers`.
- `hooks.py` l. 51 : `tensor = output if torch.is_tensor(output) else output[0]`.
- `hooks.py` l. 62 : `self._blocks[index].register_forward_hook(...)`.
- `fitting.py` l. 79 et 86-87 : la cible par défaut est `n_layers − 1`, et les sources sont `range(target)`.
- `hf.py` l. 169-171 : la normalisation finale n'est appliquée qu'au décodage.

**P3** (`harnais/activations.py`) :
- l. 29 : `modele.model.layers` ;
- l. 59 : `h = sortie[0] if isinstance(sortie, tuple) else sortie` ;
- l. 73 : `register_forward_hook` sur `blocs[c]`.

Mêmes modules, même élément, même indice, même position par rapport à la normalisation.

**Fichier réel** : sources 0 à 30 et `target_layer: null`, ce qui concorde avec `jlens` aux réglages par défaut.
`fit_lens.py` est absent du clone et du disque, et je n'ai pas de réseau.

**Pour lever la réserve** : lire `fit_lens.py` (session qui a le réseau), ou faire le test par différence finie
proposé par le relecteur, sur une instance qui porte déjà le modèle. Tant qu'elle n'est pas levée, la lecture le dit.

## 3. `sondes-figees.json` (run `20261019-230011-p3-reel`)

Inchangé depuis la v1.
- Le sceau est vérifié par la contre-lecture.
- Les sondes principales sont `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`, deux
  `SondeLineaireJetons`.
- Il y a 200 planchers appariés en covariance par sonde principale, tous à la couche 15.
- Les poids sont dans `sondes-figees-legeres.npz` (`701f73bd…`), contrôlés contre `sondes_legeres_sha256`. Les 424
  empreintes de sondes concordent (contre-lecture).
- Le sens de la classe 1 (« consigne malhonnête », « high-stakes ») n'est pas vérifié ici.

## 4. Règle primaire unique (CLJ-02), gelée avant exécution

L'énoncé est la constante `ENONCE_REGLE_PRIMAIRE` du script. La sortie le recopie avec son empreinte, que voici :
`c1b21cd6f67bb4b46f9d4514abd1d00757226b28d35604ad87d780f30e250339` (sha256 du texte UTF-8). Le voici en entier :

> Règle primaire unique, gelée avant toute exécution réelle (v2, 29 octobre 2026). Pour chaque sonde principale de P3
> (une par concept, à sa couche : tromperie-difference_moyennes-c15, enjeux-lineaire-c15) et pour chacune des deux
> lentilles (logits, jacobienne), on décode la direction +w (variante « direction », sens de la classe 1). S = nombre
> de jetons de la liste du concept propre (concepts-sondes-p3-v2.json, jetons de début de mot) parmi les 20 jetons de
> tête, la tête étant restreinte aux jetons de début de mot (un espace initial, puis une lettre, puis lettres ou
> chiffres). On calcule la même statistique, par la même lentille et à la même couche, pour deux distributions nulles :
> 200 directions isotropes (graine 20261029, numpy.random.SeedSequence) et les planchers appariés en covariance de P3
> pour ce concept (200 dans le run 20261019-230011-p3-reel ; refus en dessous de 100). Verdict « cohérent » si S >= 2
> et si S est strictement supérieur au quantile 0,99 (méthode inverted_cdf de numpy) de chacune des deux distributions
> nulles ; sinon « non cohérent ». Quatre verdicts, lus tels quels, sans correction, sans seuil de rechange, sans
> autre liste de mots. Tout le reste de la sortie (scores z, p, têtes brutes, sens moins, autre concept, autres sondes
> et couches, variantes) est descriptif et ne sert pas de critère.

- **Ce que veut dire le seuil.** Avec la méthode `inverted_cdf`, « S > q₀,₉₉ » équivaut à : au plus 2 des 200 valeurs
  nulles atteignent S.
- **Les paramètres sont des constantes du script, pas des options** : k = 20, 200 isotropes, graine 20261029,
  quantile 0,99, plancher de 2 jetons, minimum de 100 planchers. Le script refuse (`planchers-insuffisants`) si une
  sonde principale a moins de 100 planchers.
- **Ajout au gabarit proposé : le plancher « S ≥ 2 ».** Sur le vrai vocabulaire (environ 128 000 jetons, dont des
  dizaines de milliers de débuts de mot, pour environ 50 jetons de concept), la nulle sera presque toujours à 0, avec
  un quantile 0,99 à 0 ou à 1. Un jeton isolé pourrait alors suffire. Le plancher exige au moins deux jetons du
  concept dans la tête.
- **Grille de lecture, gelée**, pour chaque sonde principale :

  | Lentille jacobienne | Lentille des logits | Lecture |
  |---|---|---|
  | cohérent | non cohérent | la lentille jacobienne verbalise la direction là où la lentille des logits ne le fait pas |
  | non cohérent | cohérent | l'inverse |
  | cohérent | cohérent | les deux verbalisent |
  | non cohérent | non cohérent | aucune ne verbalise. C'est une information, pas un échec (section 9) |

- **Ce qui reste descriptif.** Les 96 valeurs de p de la v1 restent dans la sortie (bloc `diagnostics_z`), comme
  diagnostics. Même chose pour les applications de la règle aux autres sondes et couches (bloc `regle`, champ
  `verdict_descriptif`) et pour les comptes de l'autre concept (`comptes_par_concept_diagnostic`).
- **Observation de l'essai factice, à garder en tête (R4).**
  - Pour enjeux à la couche 15 sous la lentille jacobienne, où rien n'est planté (J·w y est une direction quelconque),
    S = 3. Le quantile 0,99 des isotropes vaut 2, celui des planchers vaut 3.
  - Les isotropes seules auraient donc dit « cohérent ». Ce sont les planchers qui ont rendu « non cohérent ».
  - La statistique est discrète : un dépassement fortuit d'une nulle reste de l'ordre du pour cent. La double nulle
    n'est pas un luxe.
  - Sur le vrai vocabulaire, la densité des jetons de concept est bien plus faible que dans l'essai (environ 50 sur
    des dizaines de milliers, contre 52 sur 1 293 dans l'essai). Ce cas devrait y être plus rare. Non vérifié.

## 5. Liste de mots v2 (CLJ-03)

Fichier `concepts-sondes-p3-v2.json`, scellé : `5874ea55b1774233c4e8252f07ca6869a5625aaf8b0c7b3f0b1d242a1aff53e7`. Elle
est figée avant toute lecture de sortie réelle.

**Règle de correspondance.** Un jeton compte s'il est un jeton de début de mot : un espace initial, puis exactement le
mot, sans tenir compte de la casse. Ainsi ` lie`, ` Lie` et ` LIE` comptent. `lie`, `\tfalse`, deux espaces, ` lien`
et ` lieutenant` ne comptent pas. La correspondance par préfixe est supprimée du script.

**Retirés de la v1 (11 mots) :**

| Mot | Raison |
|---|---|
| `false` | booléen de code (`False`, `false`, ` FALSE`, `\tfalse`) ; consigne explicite |
| `fib` | Fibonacci en code (`fib`, ` fib`, ` Fib`) ; consigne explicite |
| `deceiving`, `dishonesty`, `fabricate`, `liars`, `mislead` | aucun jeton dans le vocabulaire de Llama 3.1, d'après la contre-lecture |
| `life`, `important` | trop génériques pour « enjeux » ; consigne explicite |
| `legal` | trop générique, signalé par la contre-lecture avec `life` et `important` |
| `lives` | homographe du verbe (« he lives in »), aussi générique que `life` |

Les deux derniers retraits (`legal`, `lives`) sont de mon fait, au-delà de la consigne. Ils vont dans le même sens que
les autres et sont décidés avant toute lecture.

**Restent** : 24 mots pour « tromperie » et 26 pour « enjeux ». Les deux listes sont disjointes ; le script le
vérifie (`concepts-chevauchants`).

**Contrôle contre le vocabulaire.**
- Chaque mot doit avoir au moins un jeton de début de mot. Sinon le script refuse, avec le code `mot-sans-jeton` et la
  liste des mots en cause.
- Je n'ai pas le `tokenizer.json` de Llama ici. Je n'ai donc pas pu vérifier que chacun des 50 mots a son jeton avec
  espace. Mots qui me paraissent les plus exposés : `deceived`, `fabricated`, `untrue`, `hoax`, `conceal`, `urgency`,
  `bankrupt`.
- La sous-commande `verifier-concepts` ne lit que le vocabulaire et la liste. Elle se lance avant l'exécution et ne
  révèle aucun résultat.
- En cas de refus, la liste est retouchée sur ce seul critère, sans lecture de sortie, dans une v3 scellée avant
  l'exécution. Il faut le dire.

## 6. Le script `comparaison_jlens_logitlens_sondes_p3_v2.py`

Empreinte : `c02d989f7cabf5f116b08eb9fb05d5476208ff1a96ba9093d27e698e121c345c`. Il est en numpy seul ; torch ne sert
que pour une lentille `.pt`.

**Entrées.**
- Le JSON des sondes, avec son sceau exigé.
- Le `.npz` des poids, contrôlé contre `sondes_legeres_sha256` (ou contre l'empreinte donnée par option).
- La lentille, en `.npz` ou en `.pt`.
- `lm_head.weight` et `model.norm.weight`.
- `tokenizer.json`.
- La liste de mots, **obligatoire et scellée**.
- En option :
  - `--lentille-config` : empreinte et nombre de textes ;
  - `--empreintes-attendues` : contrôle de chaque entrée, la ligne qui nomme le fichier lui-même étant ignorée ;
  - `--revision-modele` ;
  - `--commit` (sinon `git rev-parse HEAD` dans le dossier du script, plus l'état git du script) ;
  - `--un-seul-couple SONDE,COUCHE`, avec le nom complet ou sans le suffixe `-c<couche>` ;
  - les variantes `--covariances` et `--activations-moyennes`.

**Sortie.**
- `regle_primaire` : énoncé, empreinte, paramètres, quatre verdicts triés, indicateur `complete`.
- Pour chaque sonde :
  - `regle`, avec S, quantiles, comptes des nulles et p de diagnostic, par lentille ;
  - les têtes brutes, « mots » (règle de `jlens/vis.py`) et de début de mot, dans les deux sens ;
  - les recouvrements entre lentilles ;
  - `diagnostics_z`.
- `lentille_ajustee_sur` : « ajustée sur N textes (lentille-config.yaml, clé …) », ou « inconnu ».
- `convention_couche`.

**Manifeste.**
- Script et empreinte, chemin complet de l'interpréteur, commande.
- Versions, commit et état du script, révision du modèle.
- Configuration de la lentille : empreinte, clés, nombre de textes.
- Contrôle des empreintes attendues, empreinte de l'énoncé de la règle.
- Empreinte de chaque entrée, graines, empreinte de la sortie.

**Refus nommés** (code 2, aucune sortie) :
- comme en v1 : `entree-absente`, `sceau-absent`, `sceau-faux`, `sceau-illisible`, `empreinte-sondes-npz`,
  `empreinte-sonde`, `sonde-introuvable`, `principale-non-lineaire`, `couche-absente-lentille`, `dimension`,
  `poids-introuvables`, `poids-illisibles`, `torch-absent-pour-pt`, `sortie-existe`, `incoherence-interne` ;
- nouveaux en v2 : `lentille-illisible` (y compris un `.pt` illisible avec torch présent), `mot-sans-jeton`,
  `concepts-illisibles`, `concepts-chevauchants`, `lentille-config-discordante`, `empreinte-entree`,
  `empreinte-attendue-absente`, `empreintes-attendues-illisibles`, `planchers-insuffisants`, `parametre`.

**Coût estimé, non mesuré.** La v1 prenait 134 s et 5,6 Go pour un couple. La règle ajoute environ 2 000 directions
nulles décodées sur tout le vocabulaire (3 couches × 2 lentilles × 200 isotropes, plus 2 concepts × 2 lentilles × 200
planchers), soit environ 2 × 10¹² opérations en simple précision, par lots de 50. Cela fait de l'ordre d'une minute de
plus et quelques dizaines de Mo de mémoire.

## 7. Essai factice v2 (`essai_factice_comparaison_jlens_v2.py`, dans `essai-factice-v2/`)

**Montage.**
- Largeur 128, vocabulaire de 2 000 jetons, 200 planchers par principale.
- Fichier de poids écrit par `ecrire_sondes` du dépôt et relu par `lire_sondes` du dépôt.
- Vocabulaire :
  - tous les mots de la liste v2 avec et sans espace ;
  - trois mots en majuscule initiale ;
  - les parasites de la contre-lecture (` false`, `False`, `\tfalse`, ` fib`, ` life`, ` important`, ` legal`,
    ` lien`, ` lieutenant`, double espace).
- Bilan : **50 sur 50** (`essai-factice-v2/journal-essai-factice-v2.txt`, empreinte
  `01dba95244cc4c84209b403f8530b0c8d0f5050ff2c32eaf95287cbb17dc2e43`).

**Règle primaire** (q = quantile 0,99) :

| Cas | Lentille | S | q isotropes | q planchers | Verdict |
|---|---|---|---|---|---|
| tromperie c15, plantée sous J (principale) | jacobienne | 11 | 2 | 2 | cohérent |
| | logits | 0 | 2 | 2 | non cohérent |
| enjeux c15, plantée en sortie (principale) | logits | 12 | 3 | 2 | cohérent |
| | jacobienne | 3 | 2 | 3 | non cohérent (voir section 4) |
| tromperie c23, J ≈ identité (descriptif, sans plancher) | logits | 10 | 2 | absents | cohérent |
| | jacobienne | 12 | 2 | absents | cohérent |
| couche 7, aléatoire (descriptif) | quatre cas | 0 à 1 | 2 | absents | non cohérent |
| enjeux-difference_moyennes-c15, aléatoire, avec planchers | logits | 0 | | | non cohérent |
| | jacobienne | 1 | | | non cohérent |

**Autres contrôles.**
- La statistique S est égale au compte des jetons du concept dans la tête de début de mot affichée.
- Spécificité : la tête de tromperie c15 sous J ne porte aucun jeton d'enjeux.
- Les diagnostics z sont repris de la v1. Avec 200 planchers, p = 0,005, et le libellé est juste (CLJ-08).
- Concepts : aucun parasite ni morceau sans espace n'est compté ; ` Lie` et ` Danger` le sont.
- Manifeste : commit, révision, empreinte de la configuration, interpréteur complet, empreintes attendues conformes.
- « Ajustée sur 461 textes » avec la configuration ; « inconnu » sans elle.

**Déterminisme.**
- Deux runs dans le même essai donnent une sortie identique octet pour octet.
- Un essai indépendant (dossier temporaire) redonne les mêmes empreintes de sortie : `6e4b3597…` pour
  `sortie-factice-v2.json` et `e9f0f7a0…` pour `sortie-factice-variantes-v2.json`.
- L'index renommé `index.json` donne la même sortie octet pour octet.
- `--un-seul-couple` redonne exactement l'entrée de la sonde du run complet.

**Refus provoqués** (19 lancements, `mot-sans-jeton` étant testé deux fois), tous avec le code 2 et aucune sortie
laissée :
- entrée absente ;
- couche absente ;
- `.pt` sans torch ;
- `.pt` illisible avec un torch factice dont `load` lève `EOFError` (CLJ-05) ;
- largeur discordante ;
- sortie existante ;
- poids altérés, avec un message qui nomme `sondes_legeres_sha256` ;
- empreinte par option fausse, avec un message qui nomme `option --sha256-sondes-npz` (CLJ-06) ;
- sceau du JSON faux ;
- `mot-sans-jeton`, par `comparer` et par `verifier-concepts` ;
- liste de mots sans sceau ;
- configuration discordante ;
- empreinte attendue fausse ;
- empreinte attendue absente ;
- planchers insuffisants (20) ;
- `--un-seul-couple`, couche fausse ;
- `--un-seul-couple`, forme fausse ;
- JSON sans `weight_map`.

**Fichiers volontairement laissés sans sceau valide** (artefacts des refus, à ne pas sceller) :
- `essai-factice-v2/altere/sondes-figees.json` : JSON modifié, son `.sha256` est l'ancien sceau, périmé exprès ;
- `essai-factice-v2/altere/concepts-sans-sceau.json` : sans compagnon, exprès.

## 8. Commande d'exécution recommandée (v2)

À lancer seulement après :
- copie de ce dossier v2 sur la machine qui a les entrées (variable `S`) ;
- versement du dossier au dépôt (date de commit) ;
- une réserve CLJ-01 levée, ou explicitement acceptée par Lazar.

L'interpréteur doit avoir torch (celui de `.venv`) et numpy ≥ 1.22. Les chemins `L` et `D` sont ceux de la
contre-lecture.

```
L=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lentilles-p3
S=<copie de comparaison-jlens-logitlens-sondes-p3-v2>
D=/home/user/controle-ia-travail/diag/20261019-230011-p3-reel
PY=/home/user/controle-ia-travail/.venv/bin/python
( cd $L/entrees && grep -v ' empreintes-entrees-v1.txt$' empreintes-entrees-v1.txt | sha256sum -c - ) && \
( cd $S && sha256sum -c comparaison_jlens_logitlens_sondes_p3_v2.py.sha256 concepts-sondes-p3-v2.json.sha256 \
     note-convention-couche-jlens-p3-v1.md.sha256 note-faisabilite-jlens-sondes-p3-v2.md.sha256 ) && \
( cd $D && sha256sum -c sondes-figees.json.sha256 ) && \
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
  --empreintes-attendues $L/entrees/empreintes-entrees-v1.txt \
  --revision-modele 0e9e39f249a16976918f6564b8830bc894c89659 \
  --sortie $L/sortie-reelle-v2/sortie-jlens-sondes-p3-v2.json
```

- **Si `verifier-concepts` refuse** : voir la section 5 (v3 de la liste, sans lecture de sortie).
- **Si `comparer` refuse avec `empreinte-attendue-absente`** : c'est que `empreintes-entrees-v1.txt` ne liste pas
  l'une des entrées, par exemple `lentille-config.yaml` (je ne connais pas son contenu). Il faut alors écrire une
  version suivante de ce fichier, sans écraser la v1, puis relancer.
- **`--revision-modele`** consigne la révision attendue. Elle ne prouve pas que le fragment `model-00004` est à cette
  révision : ce point n'est pas vérifié (contre-lecture).

## 9. Réserves de méthode (reprises de la v1, complétées)

- **Cibles à un jeton.** La lentille n'est évaluée, dans le dépôt, que sur des cibles à un jeton. « Tromperie » et
  « enjeux élevés » peuvent ne pas s'écrire en un mot. « Non cohérent » est donc une information, pas un échec : la
  direction peut être réelle mais non verbalisable, ou la sonde peut lire autre chose (style, évidence textuelle).
- **Planchers.** Seule la couche 15 a des planchers. La règle primaire ne porte que sur les principales, qui sont à
  la couche 15. Aux couches 7 et 23, l'application reste descriptive, avec les isotropes seules.
- **Bande d'espace de travail.** Elle n'est pas connue pour Llama-3.1-8B-Instruct.
- **461 textes.** La lentille est ajustée sur 461 textes et non sur 1 000. Elle est plus bruitée que celles du papier.
  Le dire dans la lecture (CLJ-10).
- **Convention de couche du fichier réel.** Incertaine, avec une forte présomption de « oui » (section 2).
- **Liste de mots.** Elle reste un choix d'analyse. La v2 est gelée ; toute retouche fera une v3, et il faudra le dire.

## 10. Différentiel v1 → v2, constat par constat

- **CLJ-01 (majeure), convention de couche.**
  - Nouvelle note scellée, `note-convention-couche-jlens-p3-v1.md`, qui cite les lignes de `jlens/hf.py`, `hooks.py`,
    `fitting.py` et `lens.py`, ainsi que celles de `harnais/activations.py` (l. 57-73 vérifiées) et
    `premier_test_ia/entrainement.py` (l. 66).
  - Conclusion : oui pour le code ; incertain, avec une forte présomption de « oui », pour le fichier réel.
  - `fit_lens.py` est absent du clone et du disque, et je n'ai pas de réseau.
  - **Réserve non levée.** Moyens de la lever : lire `fit_lens.py`, ou faire le test par différence finie.
- **CLJ-02, règle de lecture.**
  - Règle primaire unique gelée dans le script (`ENONCE_REGLE_PRIMAIRE`, empreinte `c1b21cd6…`) et recopiée ici
    (section 4).
  - Quatre verdicts et une grille de lecture.
  - Les p, les z et les autres sondes passent en diagnostics.
  - k, le nombre d'isotropes et la graine ne sont plus des options.
- **CLJ-03, liste de mots.**
  - `concepts-sondes-p3-v2.json`, scellé : jetons de début de mot seulement, 11 mots retirés (section 5).
  - La correspondance par préfixe est supprimée.
  - Sceau exigé par le script, refus `mot-sans-jeton`, sous-commande `verifier-concepts`.
  - **À verser au dépôt (commit) avant l'exécution.**
- **CLJ-04, empreintes attendues.**
  - Option `--empreintes-attendues`, qui contrôle chaque entrée lue (lentille, configuration, poids, vocabulaire,
    variantes) et ignore la ligne propre du fichier.
  - La commande recommandée garde le `sha256sum -c` préalable.
  - Le fichier `empreintes-entrees-v1.txt` lui-même n'est pas modifié : il n'est pas dans ce dossier (R12).
- **CLJ-05, `.pt` illisible.** `torch.load` est entouré d'un `try`, qui donne le refus nommé `lentille-illisible`
  (aussi dans `convertir-lentille`). Testé avec un torch factice.
- **CLJ-06, messages trompeurs.**
  - Tout JSON qui porte `weight_map` est reconnu comme index, quel que soit son nom. Le message des formats acceptés
    est exact.
  - Le refus `empreinte-sondes-npz` nomme la vraie source : l'option, `sondes_figees_sha256` ou
    `sondes_legeres_sha256`.
- **CLJ-07, un seul couple.** Option `--un-seul-couple SONDE,COUCHE`. Elle refuse une couche ou une forme fausse, et
  marque la règle « incomplète ».
- **CLJ-08, libellé des planchers.**
  - L'essai a 200 planchers factices au lieu de 20 ; le contrôle « p ≤ 0,01 contre isotropes et planchers » teste
    réellement 0,01 (p = 0,005).
  - Les références « aléatoires » s'appellent « isotropes ».
- **CLJ-09, manifeste.**
  - Commit, par `--commit` ou par `git rev-parse HEAD`, avec l'état git du script.
  - Révision du modèle (`--revision-modele`).
  - Empreinte et clés de `lentille-config.yaml` (`--lentille-config`).
  - Chemin complet de l'interpréteur.
- **CLJ-10, nombre de textes.**
  - `lentille_ajustee_sur` vaut « ajustée sur N textes (lentille-config.yaml, clé prompts_fitted) », ou « inconnu »
    sans configuration.
  - Refus `lentille-config-discordante` si la configuration et le fichier de lentille divergent.
  - La v1 annonçait 1 000 textes « d'après le README » ; c'est corrigé (section 1).
