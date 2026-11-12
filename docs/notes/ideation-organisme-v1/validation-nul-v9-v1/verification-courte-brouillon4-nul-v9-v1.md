# Vérification courte du brouillon 4 du nul v9 — changement de description seulement ; B1, I5 et I6 levés

**Conclusion : changement de `pole/nul_v9.py` de description seulement (aucun calcul touché), B1, I5 et I6 levés ; 14 empreintes égales ; aucun constat bloquant.**

Lecteur : sous-agent neuf de la session mère.
Début : 2026-11-08 10:05:34 UTC (`date -u`). Fin : 2026-11-08 10:09 UTC environ (`date -u`).
Copie lue : `/home/user/wt-organisme-66dbcf1-v` (arbre détaché à `66dbcf1`), interprète `/home/user/controle-ia-travail/.venv/bin/python`. Aucune sortie de la course lue (ni branche `donnees/validation-nul-v9-v1`, ni `resultats/banc-tricheurs-v9-validation-v1/`, ni `registres/`).

## 1. Le changement de `pole/nul_v9.py` (`9e6ca23` → `516feca`)

Lu : `git -C /home/user/wt-organisme-66dbcf1-v diff 9e6ca23 516feca -- orchestrator/pole/nul_v9.py` (69 lignes touchées). Lecture à l'œil : docstring du module (la liste « non couverte » devient trois sortes), `PHRASES_MEMBRES_V9` (ajout « même loi aveugle, même poids »), `NON_COUVERT_V9` (4 entrées au lieu de 5), trois constantes neuves (`HORS_DU_NUL_PAR_CHOIX_V9`, `HORS_DU_NUL_PAR_NATURE_V9`, `RESERVES_V9`), fonction neuve `description_publique()`, `description()` rend trois clés de plus et une description de plus.

Preuve par programme (script en entier plus bas) :
- arbres complets, docstrings retirées (module, classes, fonctions) : **différents** (attendu : des constantes et deux fonctions changent) ;
- différences par nœud de tête, exactement 7 : AJOUT `HORS_DU_NUL_PAR_CHOIX_V9`, AJOUT `HORS_DU_NUL_PAR_NATURE_V9`, CHANGE `NON_COUVERT_V9`, CHANGE `PHRASES_MEMBRES_V9`, AJOUT `RESERVES_V9`, CHANGE `description`, AJOUT `description_publique` ;
- les 39 autres nœuds de tête (tout le reste du module : constantes de calcul, classes, fonctions d'évaluation) : **arbres égaux** (`reste egal apres retrait des noeuds differents: True`) ; l'ordre des nœuds communs est inchangé ;
- aucun des 39 nœuds communs ne cite l'un des 7 noms changés ou ajoutés (`noeuds communs qui citent un nom change: []`) : aucune fonction de calcul du module ne lit ces constantes ni `description` ni `description_publique`.

Hors du module : `grep` dans `orchestrator/` des usages (hors essais) : `demonstrations/banc_tricheurs_v9.py:541` met `nul_v9.description()` dans le manifeste (champ `nul`, écrit seulement, jamais relu comme entrée d'un calcul) ; `pole/attaque_goodhart_v4.py` lit `PHRASES_MEMBRES_V9`, `NON_COUVERT_V9`, `HORS_DU_NUL_PAR_CHOIX_V9`, `HORS_DU_NUL_PAR_NATURE_V9` pour composer un texte de description destiné à un juge (autre fichier, non gelé ici, hors validation du nul ; c'est le seul « message lu par un autre module »). Valeurs rendues changées : seulement le contenu de `description()` (texte et trois clés neuves), `NON_COUVERT_V9` et `PHRASES_MEMBRES_V9` ; aucune valeur numérique, aucune richesse, aucune promotion.

Version au commit `66dbcf1` : `git diff --quiet 516feca 66dbcf1 -- orchestrator/pole/nul_v9.py` → identique (le commit de scellement ne touche que 6 fichiers de `prereg/`). Comparaison d'arbres `9e6ca23` contre `66dbcf1` : même résultat. Empreinte au commit `66dbcf1` : `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` = valeur de la section 12.

## 2. Essais ajoutés pour B1, I5, I6 (et I2)

Diffs lus : `essais/test_nul_v9.py` et `essais/mutations_nul_v9.py`, `9e6ca23..516feca`.

- **B1, cas sain** (`GrainesEtPreenregistrement.test_mode_decisif_cas_sain_et_refus`) : texte d'essai scellé au nom décisif gelant les 14 empreintes réelles, sans option de plan ; `jouer_tout` bouché ; vérifie code 3, une seule course, 31 lignes égales à `banc.LIGNES`, 1 000 répétitions, durée transmise 48 h × 3 600 s à chaque tâche, entropie = empreinte du texte, manifeste « decisif ». Artefacts : `--lignes M01` et `--repetitions 999` → code 2, `lire_preenregistrement` jamais appelé, rien écrit, toujours une seule course. Fait bien ce que B1 demandait.
- **B1, monotonie par la richesse seule** : sous-essai « monotonie-richesse » (log W v9 2,0 contre v8 1,0, aucune promotion) → arrêt `MonotonieViolee`, code 3. Conforme.
- **I5** (`LectureGelee.test_ordre_des_issues`) : M03 à 90/1 000 et perte de I02 à 120/1 000 → « trou » ; perte de I02 et M02 apparié à 20/1 000 → « puissance perdue » ; les valeurs intermédiaires (`fatales`, `perte_de_puissance`, `artefact`) sont aussi vérifiées. Conforme.
- **I6** (`CertificatMorceaux.test_valeur_certifiee_sous_optimisation_tronquee`) : 30 mondes de l'essai de domination (mêmes graines), `PALIERS_MU=(1e-2,)`, `PAS_MAX_PAR_PALIER=1`, valeur ≥ vraisemblance du monde − 1e-9 à 5 instants ; dents : au moins un instant où la meilleure valeur atteinte + 1e-3 est sous la vraisemblance. Conforme.
- **Mutations** G1 à G5, L1, L2, C5 et « description publique : choix rangés parmi les trous » : toutes « tuées pour la raison attendue » au rejeu (voir ci-dessous), chacune avec un essai et une expression de raison propres (par exemple G3 `2 != 3`, G4 `28800`, L1/L2 les deux issues inversées, C5 « optimisation tronquée… sous la vraisemblance du monde »).

Rejeu :
- `nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider essais/test_nul_v9.py` (depuis `orchestrator/`, 10:06:04 → 10:06:40) — dernière ligne : `37 passed, 35 subtests passed in 36.36s`. Égal à l'attendu.
- `nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B essais/mutations_nul_v9.py` (10:06:46 → 10:08:08, code de sortie 0) — dernières lignes : `mutations : 43 ; tuées pour la raison attendue : 43 ; tuées pour une autre raison : 0 ; défaut du banc : 0 ; survivantes : 0 ; non appliquées : 0` puis `témoin après restauration : 26 essais, 0 en échec`. Égal à l'attendu.
- `git -C /home/user/wt-organisme-66dbcf1-v status --porcelain` après le banc de mutations : sortie vide, la copie est revenue intacte.

## 3. Les 14 empreintes (section 12), recalculées au commit `66dbcf1`

Commande de la section 12 depuis `orchestrator/`, comparée au bloc délimité par `empreintes-du-code : début/fin` du texte scellé (`diff` des deux listes de 14 lignes : aucune différence). Ligne par ligne, toutes **égales** :

```
ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12  demonstrations/banc_tricheurs_v7.py   égale
0be47e4b5916a98499faf9c40d65369b41e3a5463d7ab444ed18ba18bba08c03  demonstrations/banc_tricheurs_v8.py   égale
7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44  demonstrations/banc_tricheurs_v9.py   égale
f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b  pole/__init__.py                      égale
78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85  pole/caviardage.py                    égale
fabc3d0873e6db639f2578eb00ef0035d7831a3b2a1457ffce1d91aa7a364e1c  pole/controles_pari.py                égale
798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18  pole/cycle.py                         égale
ec018f147196222268d91358ce2038bb35bf76069e6bf8928dea9e3db59d1074  pole/fiche.py                         égale
71f1d08613bf335aa9ef7aa1397f20aa24553fea2f1b858c10b265d62f8ab79e  pole/memoire.py                       égale
0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910  pole/nul_filles_v2.py                 égale
cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888  pole/nul_v8.py                        égale
7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95  pole/nul_v9.py                        égale
966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444  pole/outils.py                        égale
359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc  pole/selection_pari.py                égale
```

## 4. Constats

Bloquant : aucun.

Important : aucun.

Mineur :
1. `orchestrator/pole/nul_v9.py` ligne 6 : la docstring cite toujours le brouillon 1 (déclaré en 0 ter point 7, M7) ; sans effet.
2. `essais/test_nul_v9.py`, `DescriptionPublique.test_description_dit_la_classe_et_le_non_couvert` : la fonction `choix_parmi_les_trous` détecte un choix rangé parmi les trous par la sous-chaîne « aveugle » ; heuristique étroite (elle ne détecterait pas un choix reformulé sans ce mot). Les dents réelles viennent de `test_description_publique_separe_trous_choix_et_nature` (mutation tuée) ; sans conséquence sur B1, I5, I6.
3. Le champ `nul` du manifeste de la course (`demonstrations/banc_tricheurs_v9.py:541`) changera de contenu par rapport à tout manifeste écrit sous `9e6ca23` (trois clés de plus, `non_couvert` à 4 entrées) : à savoir pour un lecteur de la sortie qui comparerait avec un essai ancien ; aucun calcul concerné.
4. Horloge : la consigne est datée « vers 10:10 UTC » ; `date -u` de ma session donnait 10:05:34 au début. Les heures ci-dessus sont celles de `date -u`.

## Script de comparaison des arbres syntaxiques (`cmp_ast.py`, entier)

Exécuté : `/home/user/controle-ia-travail/.venv/bin/python -I -B cmp_ast.py 516feca` (et avec `66dbcf1`). Fichier : `/tmp/claude-0/-home-user-ideation-organism/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/cmp_ast.py`.

```python
import ast, subprocess, sys
D = "/home/user/wt-organisme-66dbcf1-v"
def src(rev):
    return subprocess.run(["git", "-C", D, "show", rev + ":orchestrator/pole/nul_v9.py"], check=True, capture_output=True, text=True).stdout
def strip(tree):
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            b = n.body
            if b and isinstance(b[0], ast.Expr) and isinstance(b[0].value, ast.Constant) and isinstance(b[0].value.value, str):
                n.body = b[1:] or [ast.Pass()]
    return tree
def top(tree):
    out = {}
    for i, n in enumerate(tree.body):
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)): k = type(n).__name__ + " " + n.name
        elif isinstance(n, ast.Assign): k = "Assign " + ",".join(ast.unparse(t) for t in n.targets)
        else: k = "Autre %d %s" % (i, type(n).__name__)
        out[k] = ast.dump(n)
    return out
a = strip(ast.parse(src("9e6ca23"))); b = strip(ast.parse(src(sys.argv[1] if len(sys.argv) > 1 else "516feca")))
print("arbres egaux (docstrings retirees):", ast.dump(a) == ast.dump(b))
ta, tb = top(a), top(b)
for k in sorted(set(ta) | set(tb)):
    if k not in ta: print("AJOUT  ", k)
    elif k not in tb: print("RETRAIT", k)
    elif ta[k] != tb[k]: print("CHANGE ", k)
print("ordre des noeuds de tete identique (hors ajouts):", [k for k in ta if k in tb] == [k for k in tb if k in ta])
# Preuve complementaire : retirer des deux arbres les noeuds de tete qui different (ou sont ajoutes) ; le reste doit etre egal.
diff_keys = {k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k)}
ra = {k: v for k, v in ta.items() if k not in diff_keys}; rb = {k: v for k, v in tb.items() if k not in diff_keys}
print("reste egal apres retrait des noeuds differents:", ra == rb, "(", len(ra), "noeuds de tete communs )")
# Les noms nouveaux ou modifies sont-ils references par un noeud commun (donc par un calcul) ?
noms = {"NON_COUVERT_V9", "PHRASES_MEMBRES_V9", "HORS_DU_NUL_PAR_CHOIX_V9", "HORS_DU_NUL_PAR_NATURE_V9", "RESERVES_V9", "description", "description_publique"}
for k in ra:
    n = ast.parse(ast.unparse(ast.parse(src("516feca")).body[0])) if False else None
refs = []
for n in b.body:
    key = (type(n).__name__ + " " + n.name) if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else ("Assign " + ",".join(ast.unparse(t) for t in n.targets)) if isinstance(n, ast.Assign) else None
    if key in ra:
        used = {x.id for x in ast.walk(n) if isinstance(x, ast.Name)} | {x.attr for x in ast.walk(n) if isinstance(x, ast.Attribute)}
        if used & noms: refs.append((key, sorted(used & noms)))
print("noeuds communs qui citent un nom change:", refs)
```

Sortie (`516feca`) :

```
arbres egaux (docstrings retirees): False
AJOUT   Assign HORS_DU_NUL_PAR_CHOIX_V9
AJOUT   Assign HORS_DU_NUL_PAR_NATURE_V9
CHANGE  Assign NON_COUVERT_V9
CHANGE  Assign PHRASES_MEMBRES_V9
AJOUT   Assign RESERVES_V9
CHANGE  FunctionDef description
AJOUT   FunctionDef description_publique
ordre des noeuds de tete identique (hors ajouts): True
reste egal apres retrait des noeuds differents: True ( 39 noeuds de tete communs )
noeuds communs qui citent un nom change: []
```
