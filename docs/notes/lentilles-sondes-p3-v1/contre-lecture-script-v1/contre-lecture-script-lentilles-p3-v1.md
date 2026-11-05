# Contre-lecture du script « lentille jacobienne contre lentille des logits » sur les sondes de P3 — v1

Contre-lecteur neuf (règle R2) : je n'ai pas écrit le script. Début 08:01:40 UTC, fin 08:12 UTC, 29 octobre 2026.
Aucune dépense, aucun téléchargement, aucun épisode lu.

## Verdict

**Exécutable après corrections.**
- Le calcul est juste. Sur un couple réel (`tromperie-difference_moyennes-c15`), un recalcul indépendant (torch, safetensors, tokenizers) redonne exactement les mêmes têtes et les mêmes scores z. Le pic de mémoire est de 5,6 Go et la durée de 134 secondes.
- Le fichier de lentille ne fixe pas la convention de couche : il n'a pas de clé `provenance`. Les indices de structure vont dans le bon sens, mais rien ne le prouve.
- Le critère de « cohérence » n'a pas de règle de lecture gelée.
- À corriger avant toute lecture : CLJ-01, CLJ-02, CLJ-03 et CLJ-04. CLJ-05 à CLJ-10 sont mineurs.

## Réponses aux six questions

1. **Essai factice : 25 sur 25, reproduit.** Je l'ai relancé dans un dossier neuf (`essai-factice-relu/`). L'empreinte de la sortie (`28beaa40…`) est identique à celle livrée.
   - Les trois signaux plantés se séparent comme annoncé.
     - Tromperie, couche 15, plantée sous J : la lentille jacobienne la voit (z = 1,47, p = 0,005, neuf jetons du concept en tête). La lentille des logits ne la voit pas (p bilatéral = 0,95).
     - Enjeux, couche 15, plantée en sortie : c'est l'inverse (p = 0,005 contre p bilatéral = 0,54).
     - Tromperie, couche 23, avec J proche de l'identité : 18 jetons communs sur 20, cosinus 0,972.
     - Couche 7 : rien ne sort.
   - L'essai distingue aussi `J·w` de `Jᵀ·w`, car J₁₅ y est orthogonale à un facteur près.
   - Le fichier de `altere/` au sceau volontairement périmé échoue bien à `sha256sum -c`.
   - Pour produire les poids factices, l'essai lit deux fichiers de code du dépôt (`sondes/familles.py`, `premier_test_ia/figees.py`), via `--depot`. Moi, je ne les ai pas lus.
2. **Convention de la lentille : correcte.**
   - Le script calcule `transport @ X`, soit J·w. C'est exactement `w @ J.T`, la forme documentée par le fichier. Sur la vraie lentille, avec un vecteur témoin, l'écart relatif est de 2 à 4 × 10⁻¹⁷.
   - La forme fautive `Jᵀ·w` donnerait un tout autre résultat : cosinus 0,02 à la couche 7, 0,19 à la couche 15, 0,60 à la couche 23. J est très asymétrique (‖J − Jᵀ‖/‖J‖ ≈ 0,9 à 1,4).
   - Couches : le fichier n'a pas de clé `provenance`. Ses clés sont `J`, `n_prompts`, `source_layers` et `d_model`, donc ni `capture_point` ni `stream_reduce`. Voir CLJ-01.
3. **Normalisation finale : bonne lecture.**
   - Le script calcule `W_U · (g ⊙ u / rms(u))`, avec u = w ou J·w, et sans epsilon dans le mode « direction ».
   - Le facteur rms est un scalaire, donc il ne change pas le classement. C'est vérifié : avec w multiplié par 3,7, les logits sont identiques à 0 près. Et −w donne exactement les logits opposés.
   - Le gain g de `model.norm.weight` n'est pas uniforme : il va de 0,27 à 2,94 (moyenne 2,34, écart type 0,18). Il change donc le classement : sur trois témoins, la tête avec g et la tête sans g n'ont que 7, 16 et 15 jetons communs sur 20.
   - Appliquer g est la bonne lecture, puisque le modèle multiplie par g après la normalisation. Ce n'est pas un défaut.
   - **Signe** : « plus » vaut +w, du côté où le score de la sonde monte. Pour les deux sondes principales, l'aire de validation est de 1,0 et 0,992 (au-dessus de 0,5). Le script rapporte **les deux bouts** : têtes plus et moins, `p_haut`, `p_bas`, `p_bilateral`, `meilleur_rang_plus` et `meilleur_rang_moins`.
   - Ce que veut dire la classe 1 (« consigne malhonnête », « high-stakes ») : non vérifié, il faudrait lire le dépôt.
4. **Entrées réelles.**
   - Le script accepte par défaut le fichier léger `sondes-figees-legeres.npz` (`701f73bd…`), contrôlé contre `sondes_legeres_sha256`. Il n'accepte le fichier complet (`91b61c45…`) que si celui-ci s'appelle `sondes-figees.npz`, ou si l'on passe `--sha256-sondes-npz`.
   - Les sondes principales sont retrouvées par leur nom dans la clé `index`, aux indices 1 et 16.
   - Les 424 empreintes de sondes sont recalculées et toutes concordent : aucun refus. Elles concordent aussi avec le JSON. Les six sondes de Mahalanobis manquent au fichier léger, comme prévu.
   - Le vocabulaire est relu en entier : 128 256 jetons, aucun manquant, et le décodage est identique à celui de la bibliothèque `tokenizers`.
   - J'ai lancé le mode réel sur **un seul couple** (`tromperie-difference_moyennes-c15`) à partir d'une copie réduite et rescellée du JSON (outil `filtrer_un_couple_v1.py`) : code 0, 134 s, pic de mémoire résidente 5 647 Mo. La sortie et le manifeste sont scellés (`sha256sum -c` : OK).
   - **Je n'ai pas lu les têtes, les scores ni les p.** Cette sortie de test n'est pas le résultat et ne doit pas être lue comme tel.
5. **Refus nommés, testés sur les entrées réelles** (`refus-reels/journal-refus-v1.txt`) :
   - `sceau-faux`, `sceau-absent`, `empreinte-sondes-npz`, `torch-absent-pour-pt`, `couche-absente-lentille` (couche 31), `dimension` (désembedding de forme (4096,)) et `poids-illisibles` sortent tous avec le code 2 ;
   - aucun refus ne laisse de sortie ;
   - un `.pt` illisible, quand torch est présent, plante sans refus nommé (CLJ-05) ;
   - sortie et manifeste ont chacun leur empreinte compagnon. Le script refuse d'écraser.
6. **Liste de mots** : sceau compagnon au 29 octobre, 07:58:53 UTC. Aucune sortie réelle n'existait avant mon essai, que je n'ai pas lu. Mais la liste n'est datée que dans un brouillon, et elle contient des jetons parasites (CLJ-03). Quant au critère de « cohérence », il n'est pas défini (CLJ-02).

## Constats

**CLJ-01 — majeure, à lever avant lecture (ce n'est pas un défaut du code). La convention de couche de la lentille n'est pas établie.**
- Preuve :
  - Le fichier `.pt` n'a pas de clé `provenance`.
  - `lentille-config.yaml` indique `target_layer: null` et `jlens_commit: null`. L'ajustement est passé par `fit_lens.py` de Neuronpedia, dont l'environnement a été reconstitué après coup.
  - Indices de structure : les sources vont de 0 à 30 (31 couches), avec une cible implicite à 31. C'est cohérent avec « sortie du bloc ℓ, cible = sortie du bloc 31 avant normalisation » : sous la convention des états cachés, les sources iraient de 0 à 31.
  - ‖J₃₀ − I‖/‖I‖ = 0,637, loin de 0. Cela exclut une cible « sortie du bloc 30 ».
  - La convention de P3 (sortie du bloc ℓ) ne vient que de la note de l'auteur. Je ne l'ai pas vérifiée, car la lecture du dépôt m'est interdite.
- Correction : avant la lecture, une note scellée qui cite les lignes de capture :
  - `jlens/hf.py` (crochet sur `model.model.layers[l]`) ;
  - `fit_lens.py` de Neuronpedia ;
  - `harnais/activations.py` de P3.

  À défaut, un test direct sur une instance qui porte déjà le modèle complet, sans dépense nouvelle : comparer J₁₅·v à la différence finie de la sortie du bloc 31 sous un ajout de v à la sortie du bloc 15.

**CLJ-02 — moyenne. Le critère de « cohérence » n'a pas de règle de lecture.**
- Preuve : le script rapporte, pour chaque cas, le nombre de jetons en tête, le meilleur rang, z, et les p contre les isotropes et contre les planchers, sans aucun seuil. Le mode par défaut donne 6 sondes × 2 lentilles × 2 concepts × 2 bouts × 2 références, soit 96 valeurs de p, sans correction. La marge d'interprétation après coup est entière.
- Correction : geler avant l'exécution une règle primaire unique. Par exemple, la sonde principale est « cohérente sous la lentille X » si :
  - p_haut ≤ 0,01 contre les isotropes, et contre les planchers à la couche 15 (avec 200 nuls, le plus petit p possible est 0,005) ;
  - et le z du concept propre dépasse le z de l'autre concept.

  Tout le reste est déclaré descriptif.

**CLJ-03 — moyenne. La liste de mots ramène des jetons parasites, et elle n'est datée que dans un brouillon.**
- Preuve : la correspondance exacte, sans tenir compte de la casse ni des espaces, trouve 47 jetons pour « tromperie » et 78 pour « enjeux ». Parmi eux :
  - les booléens de code `False`, `false`, ` FALSE`, `\tfalse` ;
  - `fib`, ` fib` et ` Fib` (Fibonacci en code) ;
  - des morceaux sans espace (`lie`, `lied`, `stakes`, `risk`) ;
  - pour « enjeux », des mots génériques (`life`, `important`, `legal`).

  Le score z donne le même poids à chaque variante. Cinq mots n'ont pas de jeton : `deceiving`, `dishonesty`, `fabricate`, `liars`, `mislead`.
- Correction : décider **avant toute lecture**. Soit on garde la v1 et on le dit. Soit on fait une v2 restreinte aux jetons de début de mot (avec espace initial), sans `false` ni `fib`. Dans les deux cas, la sceller et la verser au dépôt (date de commit) avant l'exécution. Ne jamais utiliser `--correspondance prefixe`, qui attrape par exemple `lien` et `lieutenant`.

**CLJ-04 — moyenne. La lentille, le désembedding, le vocabulaire et les concepts ne sont pas contrôlés contre une empreinte attendue.**
- Preuve : seuls le JSON des sondes (par son sceau) et le fichier des poids (par `sondes_legeres_sha256`) sont contrôlés. Le reste est seulement consigné. Une lentille de même largeur mais d'un autre modèle, par exemple le modèle de base, passerait sans refus.
- Autre défaut : `empreintes-entrees-v1.txt` contient sa propre ligne, qui est fausse par construction. `sha256sum -c` sur ce fichier rend donc un échec.
- Correction : faire précéder l'exécution d'un `sha256sum -c` qui exclut cette ligne (voir la commande plus bas), et retirer la ligne du fichier.

**CLJ-05 — mineure. Un `.pt` illisible, quand torch est présent, ne donne pas de refus nommé.**
- Preuve : cas 4 du journal des refus. Le script s'arrête sur `EOFError`, avec le code 1, et sans sortie.
- Correction : entourer `torch.load` d'un `try` et lever `Refus("lentille-illisible", …)`.

**CLJ-06 — mineure. Deux messages trompeurs.**
- Preuve : la route par index exige un nom en `.safetensors.index.json`. Or l'entrée livrée s'appelle `index.json`, ce qui donne le refus `poids-illisibles`, alors que le message annonce « index.json:nom » accepté. Par ailleurs, quand on passe `--sha256-sondes-npz`, le refus `empreinte-sondes-npz` attribue toujours l'empreinte attendue à `sondes_legeres_sha256`.
- Correction : corriger les deux libellés. En attendant, passer le fragment directement (`model-00004-of-00004.safetensors:…`).

**CLJ-07 — mineure. Pas d'option pour un seul couple sonde × couche.**
- Preuve : pour mon essai, il a fallu une copie réduite et rescellée du JSON.
- Correction : facultative, l'exécution réelle n'en a pas besoin. On pourrait ajouter `--seulement NOM`.

**CLJ-08 — mineure. Un contrôle de l'essai factice est mal libellé et sans pouvoir réel.**
- Preuve : le libellé annonce « p ≤ 0,01 contre aléatoires et planchers », mais le code teste les planchers à ≤ 0,05. La valeur obtenue, 0,048, est le plus petit p possible avec 20 planchers (1/21) : ce contrôle ne peut rien distinguer de plus.
- Correction : corriger le libellé, ou passer à 200 planchers factices.

**CLJ-09 — mineure. Le manifeste est incomplet au sens de R9.**
- Preuve : il n'a ni commit, ni révision du modèle, ni empreinte de `lentille-config.yaml`. L'interpréteur n'y est nommé que par son nom court.
- Correction : consigner ces trois éléments dans une note scellée à côté de la sortie, ou ajouter une option de provenance.

**CLJ-10 — information. La lentille a été ajustée sur 461 textes, pas sur 1 000.**
- Preuve : `n_prompts = 461` et `prompts_fitted: 461`, après un arrêt anticipé à une variation de 0,002. Il s'agit bien du modèle Instruct d'après le fichier de configuration, mais la révision n'est pas consignée.
- Correction : le dire dans la lecture.

## Commande d'exécution recommandée

À lancer après CLJ-01 à CLJ-04 : convention de couche citée, règle de lecture gelée, liste de mots décidée et versée. Si l'on fait une v2 de la liste, remplacer le chemin `--concepts`. L'interpréteur doit avoir torch (celui de `.venv`).

```
L=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lentilles-p3
S=$L/script/comparaison-jlens-logitlens-sondes-p3-v1
D=/home/user/controle-ia-travail/diag/20261019-230011-p3-reel
( cd $L/entrees && grep -v ' empreintes-entrees-v1.txt$' empreintes-entrees-v1.txt | sha256sum -c - ) && \
( cd $S && sha256sum -c comparaison_jlens_logitlens_sondes_p3_v1.py.sha256 concepts-sondes-p3-v1.json.sha256 ) && \
( cd $D && sha256sum -c sondes-figees.json.sha256 ) && \
/home/user/controle-ia-travail/.venv/bin/python -I -B $S/comparaison_jlens_logitlens_sondes_p3_v1.py comparer \
  --sondes-json $D/sondes-figees.json \
  --sondes-npz $L/entrees/sondes-figees-legeres.npz \
  --lentille $L/entrees/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt \
  --desembedding $L/entrees/model-00004-of-00004.safetensors:lm_head.weight \
  --norme-finale $L/entrees/model-00004-of-00004.safetensors:model.norm.weight \
  --vocabulaire $L/entrees/tokenizer.json \
  --concepts $S/concepts-sondes-p3-v1.json \
  --sortie $L/sortie-reelle-v1/sortie-jlens-sondes-p3-v1.json
```

Six sondes et trois couches : j'estime le besoin à environ 6 Go de mémoire et quelques minutes (non mesuré ; le couple seul a pris 5,6 Go et 134 s).

## Non vérifié

- La convention de capture dans le code de `jlens` et de Neuronpedia, et celle de P3 (`harnais/activations.py`). Voir CLJ-01.
- Ce que veut dire la classe 1 de chaque sonde.
- Que le fragment `model-00004` est bien à la révision `0e9e39f…`, et l'origine de la lentille (`d5300a15…`) au-delà de son fichier de configuration.
- Les variantes `--covariances` et `--activations-moyennes` sur des données réelles : il n'y a pas d'entrées pour elles.
- Le mode par défaut complet (six sondes) en réel.
- Le papier lui-même.

## Fichiers produits (dans `…/lentilles-p3/relecture/`)

- `contre-lecture-script-lentilles-p3-v1.md` (ce rapport) et son `.sha256`.
- `outils/verifier_convention_norme_v1.py` et son journal `outils/verifier_convention_norme_v1.journal.txt` : convention, structure des couches, gain g.
- `outils/recalcul_independant_v1.py` et son journal : concordance avec le script, sans afficher de résultat.
- `outils/filtrer_un_couple_v1.py`, avec `entrees-filtrees/sondes-figees.json` et son `.sha256` (copie réduite à une sonde).
- `essai-factice-relu/` : essai factice relancé, 25 sur 25.
- `essai-reel-un-couple/` : sortie, manifeste, empreintes et journal. **Non lus, à ne pas lire comme résultat.**
- `refus-reels/` : journal des refus sur les entrées réelles.
