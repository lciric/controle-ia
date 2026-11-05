# Enquête sur l'arrêt de R1 (rejeu des 2 400 actions de P3) — v1

- Date : 2026-11-02 (UTC). Enquête sur processeur seulement : aucune instance, aucune dépense, aucun score, aucune activation, aucune notation lue (seuls `jetons`, `jetons_notes` et les tableaux d'identité de `scores-p3.npz`, les bornes de champs de `jetons-principales-p3.npz`).
- Code : commit de scellement `567260c05687747f0c7a715fc9b15b4fc6297d65` (branche `prep/runs-r1-r2-r4-v1`), dans un arbre de travail temporaire retiré à la fin.
- Arrêt : `diag/20261102-002114-r1-rejeu-reel/arret.json` (branche `origin/calcul/r1-r2-reel-v1`).

## Verdict

**Cause établie** : la garde CLC-03 suppose qu'un épisode « entièrement conforme en longueur » a forcément les identifiants de P3. C'est faux. À température 1, l'agent de P3 a parfois échantillonné un **découpage non canonique** d'un mot, de **même longueur en jetons** et qui se décode en **le même texte** (exemple : P3 a produit `Ġro` + `crap`, la retokenisation du texte donne `Ġroc` + `rap`). Le test de conformité (longueur et texte décodé) ne le voit pas ; l'empreinte de trajectoire, qui couvre les identifiants, le voit. Ce n'est ni le gabarit, ni la date, ni la consigne, ni une version de bibliothèque. **15 des 22 épisodes** sont expliqués **à l'octet près** (empreinte de P3 retrouvée) ; les 7 autres restent une hypothèse du même mécanisme, plus complexe.

## 1. Les deux calculs de l'empreinte

- **P3** (`premier_test_ia/run.py`, ligne 295, commit `97dd8290`) : `empreinte_episode(ep, acts)` de `harnais/episode.py` ; partie « trajectoire » = sha256 de `json.dumps(asdict(Episode), sort_keys=True, ensure_ascii=False)` : identifiant, N, T, transcription complète en identifiants (consigne, observations, actions générées, clôtures), et par action agent, pas, empan, **identifiants générés** et texte (décodé de ces identifiants, `skip_special_tokens=True`).
- **Rejeu** (`runs_nuit/rejeu_activations_v1.py`) : `reconstruire_episode` retokenise le texte seul (`formats._ids`), ajoute le jeton de fin de tour quand `jetons − jetons_notes = 1`, recolle ouverture, clôture et tours ; `episode_harnais` puis `empreinte_trajectoire` refont exactement le même sha256. `resoudre_fins` essaie une ou deux substitutions du jeton de fin parmi `fmt.fins` = {128001, 128008, 128009}. Les identifiants générés par P3 n'ont jamais été stockés : seul leur texte l'est.
- Code du harnais, des formats, des conditions et du chargement : identique entre `97dd8290` et `567260c0` (`git diff --stat` vide hors deux fichiers neufs de juges).

## 2. Essais

**Écart d'environnement — écarté.** Manifestes : P3 et rejeu ont `transformers` 5.18.0, `tokenizers` 0.23.2, `torch` 2.14.1, même révision du modèle `0e9e39f2…`, même variable de gabarit (« 26 Jul 2024 ») ; seuls Python (3.11.17 contre 3.11.18) et le noyau Linux diffèrent. L'avertissement « Ignoring clean_up_tokenization_spaces=True… » vient de la même version des deux côtés, donc du même décodage ; et la conformité exige déjà l'égalité du texte décodé. 130 trajectoires identiques excluent toute erreur systématique de gabarit.

**Reproduction de la garde sans modèle** (`repro.py`, lancé depuis l'arbre de travail au commit scellé, `PYTHONPATH=src .venv/bin/python repro.py <tokeniseur> recs.pkl`) : 240 épisodes, **151 conformes en longueur, 129 identiques, 22 conformes à trajectoire différente** ; après la substitution du jeton de fin, 130 et 21, premiers cités `mention/2604.12086v1/e0`, `honnete/2602.00987v1/e0`, `temoin/2602.15124v1/e0` : **identique à l'instance**.

**Preuve directe d'un découpage non canonique de même longueur dans P3.** Les bornes de champs stockées par P3 (`jetons-principales-p3.npz`, calculées sur ses identifiants) comparées à celles du rejeu, sur les 2 236 actions conformes : un seul écart, `honnete/2509.23173v2/e0` pas 3, champ PROPOSAL au jeton 23 dans P3, 24 au rejeu, même longueur totale, même texte.

**Recherche arbitrée par l'empreinte** (`decalages.py`, ≈ 24 min) : pour chaque épisode signalé, chaque paire de jetons voisins d'une action est redécoupée en deux jetons du vocabulaire couvrant les mêmes octets (même longueur, même texte) ; on garde la variante dont l'empreinte égale celle de P3.

| Épisode | Résolution (P3 contre retokenisation) |
|---|---|
| `mention/2604.12086v1/e0` | pas 1 : `Ġro`+`crap` contre `Ġroc`+`rap` |
| `temoin/2602.15124v1/e0` | pas 0 : `Ġho`+`i` contre `Ġh`+`oi` |
| `honnete/2602.00987v1/e0` | non résolu (une ou deux paires) |
| `saboteur/2510.16989v1/e0` | jeton de fin (résolu aussi sur l'instance) |
| 10 autres | une paire chacun (`ĠEval`+`uating`, `Ġl`+`lm`, `(as`+`ide`, `Ġdeep`+`uts`…) |

Puis deux paires (`deux_decoupages.py`, ≈ 4 min, sérialisation directe vérifiée égale à `empreinte_trajectoire`) : 2 de plus (`mention/2509.03810v2/e0` : deux fois `ĠM`+`APE` au pas 0 ; `mention/2512.05150v2/e0` : `Ġdam`+`pom` et `Ġknow`+`sn`). Bilan : 1 + 12 + 2 = **15 sur 22 expliqués exactement** ; 7 non résolus (`honnete/2602.00987v1`, `mention/2605.17899v2`, `saboteur/2510.05132v3`, `temoin/2512.06870v2`, `honnete/2512.05150v2`, `honnete/2512.11131v1`, `temoin/2510.24788v1`). Hypothèses classées pour eux : (1) trois redécoupages ou plus (le modèle recopie ses propres découpages, voir `ĠM`+`APE` deux fois) ; (2) une fenêtre de trois jetons redécoupée autrement ; (3) un jeton de fin substitué combiné à un redécoupage ; (4) octets incomplets décodés en caractère de remplacement, de même longueur par hasard (peu probable).

**Réserve sur le tokeniseur du bloc-notes.** `tok-llama31/tokenizer.json` et `special_tokens_map.json` sont conformes à la révision (identifiants git `5cc5f00a…`, `02ee80b6…`), mais **`tokenizer_config.json` ne l'est pas** (50 870 octets, gabarit de Llama 3.0 sans « Today Date » ; publié : 55 351 octets, `db88166e…`). La garde « un nouveau tour réécrit le début » l'arrête. L'enquête a utilisé le fichier publié de la révision, retéléchargé (gratuit). L'instance, elle, a chargé le bon fichier (130 trajectoires identiques).

## 3. Correction proposée

Peut-on corriger sans relancer l'environnement ? **Oui, sans choix libre** : la cause est un défaut de la garde, pas de la reconstruction de l'environnement, et l'empreinte de P3 reste l'arbitre unique.

- **Étape A (processeur, déterministe)** : étendre `resoudre_fins` en `resoudre_tokenisation` : substitutions du jeton de fin (comme aujourd'hui), puis une, puis deux paires redécoupées (même octets, même longueur), dans un ordre fixe ; seule une égalité d'empreinte avec P3 valide une variante. Table des corrections calculée avant la carte, scellée, rejouée par la course et vérifiée par empreinte. Résultat attendu, déjà mesuré : 145 épisodes à trajectoire identique (au lieu de 130).
- **Étape B (règle de la garde)** : un épisode conforme en longueur qui reste différent après A est classé **non conforme** (hors contexte exact, non éligible), comme les 89 épisodes déjà non conformes, au lieu d'arrêter la course ; l'arrêt est gardé si ces cas dépassent un seuil fixé d'avance (proposé : 10 épisodes, ou tout épisode dont l'ouverture ou la consigne diffère au premier jeton, signe d'erreur systématique). Ici : 7.

Ces deux étapes modifient le code et une règle d'un préenregistrement scellé (CLC-03) : **écart à un préenregistrement scellé, donc nœud de décision de Lazar**, addendum scellé et contre-lecture neuve (R1, R2). Tests à ajouter : cas sain (épisode conforme identique), artefact (paire redécoupée injectée, résolue ; gabarit altéré, arrêt) (R5).

**Coût de carte** : relance de R1 seule (R2 est faite), même instance A100 : ≈ 1 h, soit ≈ 1,0 à 1,4 dollar (tarifs relevés de 1,01 à 1,37 dollar par heure). **Repli prévu** (relance de l'environnement, préenregistrement R1, tableau des arrêts) : ≈ 3 h, ≈ 3 à 4 dollars, devis et préenregistrement neufs. Recommandation : A puis B, confiance moyenne à haute (le mécanisme est prouvé à l'octet sur 15 épisodes ; les 7 restants sont exclus, pas devinés).

## Fichiers de l'enquête (bloc-notes de session, non versés)

`…/scratchpad/enquete-r1/` : `repro.py` (`22fb43d5…`), `decalages.py` (`daf09796…`), `deux_decoupages.py` (`1a24dde8…`), `bilan-decalages.json` (`e360e9c3…`), `bilan-deux.json` (`577ef263…`), tokeniseur `tok-p3/`.
