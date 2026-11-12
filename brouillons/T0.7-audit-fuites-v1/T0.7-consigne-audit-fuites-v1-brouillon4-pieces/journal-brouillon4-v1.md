# Journal du brouillon 4 de la consigne de l'audit des fuites de T0.7 — v1

Travail commencé le 2026-11-11 à 13:28 UTC, journal écrit à partir de 13:43 UTC (heures relevées par `date -u`), par un
**agent neuf** (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sous
la consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-audit-fuites-t07-brouillon4-v1.md`
(`df38829a025db0f341b1a919d1c2afbfbd19c4f5c7019b8926483dd0f4cf629d`, vérifiée par `sha256sum` avant lecture, égale à son
compagnon ; R-2346) et les interdits communs v2 qu'elle recopie. Je n'ai écrit ni T0.7, ni ses contre-lectures, ni son
module, ni les brouillons 1 à 3 de cette consigne, ni leur contre-lecture ; ayant lu T0.7, je suis exclu ensuite de tout
rôle de lecteur de P3-bis et de tout rôle d'auditeur ou de contre-lecteur de l'audit des fuites. Bac à sable :
`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/audit-fuites-b4/` (scripts d'exploration
et essais à blanc ; non versés). Aucun commit, aucune ligne de registre, aucun appel externe, aucune dépense.

## 1. Pièces

| pièce | chemin | sha256 |
|---|---|---|
| brouillon 4 | `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon4.md` | `f9f4bd380a3066371c88d39ede0ef60bde77070311cd2cd9ca221cf8f3f194c5` |
| couples | `…-brouillon4-pieces/couples-brouillon3-vers-brouillon4-v1.json` | `746f38793753fcf4167296c5057854fa56784fad96fb96a8ca3d1529c55e36b7` |
| script | `…-brouillon4-pieces/appliquer_couples_brouillon4_v1.py` | `7539b4779e9def222791fafa5165915e00ab85a7bca12693c85101ccd41dd037` |
| sortie brute du script (`appliquer`, 13:42 UTC) | `…-brouillon4-pieces/sortie-script-v1.txt` | `2042c9a21cf41227fb6c0a2c28806455aba74557cb3d2f1ba84b2b7a69ed04b6` |

`…` = `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1`. Le brouillon 3 est intact
(`0d51099e5ef58829ce83731592eb8573aae8ce8848344488ffc672be45ac273e`, revérifié après l'écriture).

**Procédé.** Le script (lancé depuis la racine du dépôt, `PYTHONPATH=src .venv/bin/python <script> appliquer`) : joue
d'abord 19 essais sur jouets (R5 : chaque garde passe sur un cas sain et arrête sur un artefact : découpage des cellules,
clé absente ou en double, « ancien » absent ou en double, « nouveau » ambigu au retour, passage absent, double ou partiel,
découpeur à octet changé, compagnon faux ou fichier absent, écriture sur un fichier différent) ; vérifie les empreintes
des entrées et de leurs compagnons ; calcule les comparaisons des § 2 et 3 ci-dessous ; tente la vérification du découpeur
par `git show` (§ 5) ; applique 23 couples au brouillon 3, chacun présent une fois au moment de son remplacement ; défait
les couples du dernier au premier et exige le brouillon 3 à l'octet ; exige pour marqueurs restants exactement
`<<RAPPORT_CONTRE_LECTURE_2>>` et, découpeur non vérifié, `<<CHEMIN_DECOUPEUR>>` ; n'écrase aucun fichier différent (R12).
Deux essais à blanc (`--a-blanc`, sorties dans le bac à sable) ont précédé ; la sortie réelle est égale octet pour octet au
second. **Vérification indépendante** (petit programme distinct, bac à sable) : les couples du fichier JSON, appliqués au
brouillon 3, donnent le brouillon 4 ; défaits, le brouillon 3 ; chaque « ancien » est unique dans le brouillon 3 et chaque
« nouveau » unique dans le brouillon 4 ; la cellule citée au § 2.1 et les troisième et quatrième cellules sont égales à
celles du texte scellé, découpées par une fonction écrite à part.

## 2. Lignes `AUDIT-FUITES-T07` et `CONSIGNE-AUDIT-FUITES-T07` (§ 2.1, § 2.2)

Découpage des cellules : coupure aux `|` non échappés (le `\|` de la cellule reste dans la cellule), une espace retirée de
chaque bord ; ce découpage redonne les empreintes citées par le brouillon 3 pour le brouillon 21 (`9cee4938…`,
`95c8b659…`), donc c'est le même.

| ligne | brouillon 21 | brouillon 22 | texte scellé |
|---|---|---|---|
| `CONSIGNE-AUDIT-FUITES-T07` | l. 2086 | l. 2110 | l. 2207 |
| `AUDIT-FUITES-T07` | l. 2087 | l. 2111 | l. 2208 |

- **`AUDIT-FUITES-T07`, ligne entière : texte scellé = brouillon 22, à l'octet : OUI** (sha256 de la ligne, sans fin de
  ligne, dans les deux : `53eca69ef2cd0c777d16f8ad64f380ecaa62381fa21ea05a728ba92c55ce6051`).
- Deuxième cellule au texte scellé : `381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede` (égale au
  brouillon 22) ; première, troisième et quatrième cellules égales à celles du brouillon 21.
- **Couples de la cellule, brouillon 21 → texte scellé, calculés par programme** : quatre ; dans l'ordre de la cellule, ils
  recouvrent les couples A, C, B et D du journal du brouillon 3 (§ 4) ; les quatre couples du journal, extraits du journal
  par programme et appliqués tels qu'écrits, donnent la cellule du texte scellé, dont l'empreinte est le repère que le
  journal du brouillon 3 avait calculé pour A + B + C + D (§ 3, point 5). Le couple calculé A diffère de l'écriture du
  journal par ses bords seulement (il commence à « **différence de construction** », sans « une », et finit à
  « organisme**, » avec la virgule commune) : même effet.
- **Fait utile pour la contre-lecture des écarts** (conformité à R-2203, que je ne prononce pas) : la cellule scellée est la
  cellule du brouillon 21 plus exactement le couple A (phrase de la lecture (a), membre de phrase entier) et les couples
  facultatifs B, C, D, que R-2212 dit retenus par la mère.
- **`CONSIGNE-AUDIT-FUITES-T07`, ligne entière** : brouillon 21 = brouillon 22 = texte scellé, à l'octet (sha256 de la ligne
  `33d8e306abe31e186ed17e5b794be5c0740b8936050ce23410ffe116c254cdee`) ; le § 2.2 du brouillon 3 (cellule 2, cellules 3 et 4)
  est égal au brouillon 21, donc au texte scellé : **rien n'est recopié à neuf** ; seule une phrase de constat est ajoutée
  sous le titre (couple C11).
- L'annexe B du brouillon 3 est égale à l'octet à la ligne du brouillon 21.

## 3. Passages du § 2.3 comparés au texte scellé

Chaque bloc cité (« > ») du § 2.3, préfixe retiré, cherché dans le brouillon 21 et dans le texte scellé : présent **une
fois, en lignes entières, à l'octet** dans les deux. **Aucun passage ne diffère, aucun n'est introuvable** : rien n'est
recopié à neuf ; les numéros de ligne du texte scellé sont ajoutés aux titres (couples C12 à C18).

| passage | brouillon 3 | sha256 du bloc | brouillon 21 | texte scellé |
|---|---|---|---|---|
| plan, point 4 ter | l. 83 | `72e1ceb7ae65609c439c5df92e38e5a627dcf3e8d01c4a605dc041d7339166f8` | l. 1350-1355 | l. 1492-1497 |
| grille, L1b | l. 92 | `dde0824be7e7ba1616452e6e9287293d37c5ecf22c59d3c16c9186ca6844f47b` | l. 1765 | l. 1907 |
| grille, L6 | l. 96 | `5e7118d404c938c2ae268833db47a4bfce8ebfe0fa4de1a69dd60f62ceca8dc9` | l. 1769 | l. 1911 |
| liste d'arrêt | l. 100 | `46f49843011a0d5308682e3a29986d7b54e4d2a2927745b58cbaf1c27357ae86` | l. 1864-1867 | l. 2009-2012 |
| « Non interprétable » | l. 107 | `990bbac422cb63e76662a687a7644e8553a1055b3a219d76eb7bf1333c0dbaf7` | l. 1083-1089 | l. 1226-1232 |
| « Module » (paraphrase, non citée) | l. 115 | `809306570d0c8bdc5459b78e416dca5ebf0514b844f4f45ec324ea7a8aec01f9` (l. 2442-2444 du brouillon 21) | l. 2442-2444 | l. 2574-2576 |

## 4. Couples du brouillon 3 au brouillon 4 (23 appliqués, un en attente)

Chaque couple est au fichier JSON (champ `motif`). Les couples marqués « cohérence » appliquent la règle du point 1 du
mandat (« texte scellé » au lieu de « brouillon 22 ») hors du seul § 2.1, là où le brouillon 3 parlait au futur de la ligne
du brouillon 22 ou d'un marqueur rempli depuis ; ils sont indépendants les uns des autres et des autres couples (anciens
disjoints) : la mère peut les retirer un à un (question Q-B4-3).

| couple | motif | lieu |
|---|---|---|
| C00 | point 5 | titre : « brouillon 3 » → « brouillon 4 » |
| C01 | point 5 | statut du brouillon 4 (qui, quand, d'où ; brouillon 4 = brouillon 3 + couples) ; l'ancien statut devient « Brouillon 3 (historique) » |
| C02 | cohérence | en-tête, état des marqueurs (un rempli ; deux restants, dont `CHEMIN_DECOUPEUR`, § 5) |
| C03 | cohérence | en-tête, ordre des opérations (texte scellé, puis remplissage, puis découpeur, contre-lecture, scellement) |
| C04 | cohérence | en-tête, « Ce qui gouverne » : ligne du texte scellé (chemin, empreinte, l. 2208) |
| C05 | cohérence | en-tête : ligne `CONSIGNE-AUDIT-FUITES-T07` égale au texte scellé ; vérification des cellules contre le texte scellé (« puis à celui de T0.7 » retiré : T0.7 est scellé) |
| C06 | cohérence | § 0, Q3 : ligne corrigée au brouillon 22 puis scellée ; « si la ligne du texte scellé ne dit pas (a) » |
| C07 | cohérence | § 1 : « (au brouillon 22) » → « (texte scellé de T0.7, § 2.1) » |
| C08 | point 1 | titre du § 2.1 |
| C09 | point 1 | marqueur `LIGNE_AUDIT_FUITES_T07_B22` rempli (source, égalité avec le brouillon 22, cellule 2 et son sha256, cellules 3 et 4, quatre couples) |
| C10 | point 1 | note de remplissage (texte scellé ; point (6) ajouté : égalité avec le brouillon 22 ; renvoi au § 14.2) |
| C11 | point 2 | § 2.2 : constat d'égalité au texte scellé (l. 2207), rien de recopié |
| C12 | point 2 | § 2.3 : constat d'égalité au texte scellé, rien de recopié |
| C13 à C18 | point 2 | § 2.3 : numéros de ligne du texte scellé ajoutés aux six repères |
| C19 | point 3 | **en attente, non appliqué** (§ 5) : `CHEMIN_DECOUPEUR` |
| C20 | cohérence | § 6 : « texte de la ligne au brouillon 22 » → « ligne du texte scellé de T0.7 » |
| C21 | point 4 | titre du § 14.2 : « commandée par la mère : R-2212, Q16 ; R-2346 » |
| C22 | point 4 | objet du § 14.2 : différentiel du brouillon 3 au brouillon 4, remplissages, conformité de la ligne scellée à R-2203 ; fichiers à donner ; phrase « si la mère ne la commande pas » retirée (elle la commande) ; `<<RAPPORT_CONTRE_LECTURE_2>>` laissé |
| C23 | point 4 | titre de l'annexe B : **elle reste**, pour comparaison (base des couples du § 2.1), non applicable |

**Laissés tels quels** (historique ou hors mandat) : le tableau du § 14.1 (traitement au brouillon 3, dont « phrase corrigée
au brouillon 22 ») ; « T0.7 non scellé » dans la raison de Q3 (raison au moment de la décision) ; le « Calendrier visé » du
§ 4 (Q-B4-5) ; les renvois aux lignes du brouillon 21 hors du § 2 (Q-B4-4).

## 5. Découpeur : `CHEMIN_DECOUPEUR` non rempli (commit absent du clone local)

- **Constat** (2026-11-11, entre 13:28 et 13:33 UTC ; `date -u` relevé à 13:28 et à 13:32) : `git show
  c7484c43657a2ce22d76af33efd06aaa11a6aafa:donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/<fichier>` rend « fatal: path
  … does not exist in 'c7484c43…' » pour les trois fichiers et leurs compagnons ; `git show --stat c7484c43…` rend « bad
  object » ; `git cat-file -t` du hash complet : « could not get object info » ; `git rev-parse --verify c7484c43^{commit}` :
  rien ; aucune référence locale dont le nom contient « decoupeur » (`git for-each-ref`, filtré) ; le dépôt n'est pas
  superficiel ; le seul autre arbre de travail (`scellement/p3bis-v1`, bac à sable de la mère) partage le même magasin
  d'objets ; l'ancien clone `/home/user/controle-ia` ne l'a pas non plus (`cat-file`). Vérifié sur disque avant de le
  déclarer absent (R11). **Aucun `fetch`** (interdits, règle 4) : je m'arrête sur ce point.
- **Ce qui est vérifié quand même** : les trois empreintes de R-2238 sont égales, caractère pour caractère, à celles de la
  réception R1 v4 scellée (`docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/etape-E-reception-r1-v4-v1.md`,
  `bb6652f2cdd914f2ba0b3cd70c8af37ee6dd40fb0da0db8e289133ed6f5e79e1`, égale à son compagnon, l. 70-72) ; le commit et le
  dossier figurent dans R-2238. Ce n'est **pas** la vérification demandée (recalcul par `git show` sur le commit, comparaison
  aux compagnons du commit).
- **Couple prêt, non appliqué** (fichier JSON, champ `en_attente`, `C19-en-attente`) : ancien « `<<CHEMIN_DECOUPEUR>>` »
  (accents graves compris) → le dossier, le commit, la branche (R-2238), l'extraction par
  `git archive c7484c43… donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/ | tar -x -C <bac à sable>` dans le bac à sable
  de l'auditeur, **écrite comme exception à la règle 4 des interdits** (qui ne permet que `git show <commit>:<chemin>`), et
  les trois empreintes.
- **Pour finir** (geste de la mère) : amener le commit `c7484c43…` dans le clone local (branche de données
  `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1`, poussée selon R-2238 ; `fetch` interdit aux sous-agents), puis
  relancer `PYTHONPATH=src .venv/bin/python <script> appliquer --a-blanc <dossier>` : le script recalcule alors les trois
  empreintes par `git show`, les compare à R-2238 et aux compagnons du commit (`<fichier>.sha256`, format de `sha256sum` ;
  tout écart ou fichier absent → arrêt, essais 6a à 6d), applique C19 et les variantes « rempli » de C02 et C03, et écrit un
  brouillon complet (brouillon 3 + couples) à verser sous un nom neuf (R12). Le même commit devra être présent sur la
  machine de l'auditeur.

## 6. Sources lues (empreintes recalculées par `sha256sum` ou par le script)

| source | sha256 | ce qui a été lu |
|---|---|---|
| consigne du brouillon 4 | `df38829a…` (égale au compagnon) | en entier |
| brouillon 3 | `0d51099e…` (égale au compagnon) | en entier |
| journal du brouillon 3 | `a153119f…` (égale au compagnon) | en entier |
| brouillon 2 | `ecd80ce4…` (égale au compagnon) | en-tête (l. 1-40) ; nombre de lignes du différentiel 2 → 3 |
| contre-lecture 1, `prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon2-cl1.md` | `02b9d8b5…` (égale au compagnon) | en entier |
| texte scellé de T0.7, `prereg/T0.7-sondes-v0-v1.md` | `d7d180ec…` (égale au compagnon et à R-2321) | lignes de registre `CONSIGNE-AUDIT-FUITES-T07` et `AUDIT-FUITES-T07` ; passages du § 2.3 et lignes de renvoi, par programme |
| brouillons 21 et 22 de T0.7 | `f7dcb226…`, `8b84cba5…` (égales aux compagnons) | mêmes lignes ; l. 2440-2446 du brouillon 21 |
| `registres/decisions.md` | fichier vivant, non haché | lignes R-2203, R-2212, R-2232, R-2238, R-2321, R-2346 seules |
| réception R1 v4, `etape-E-reception-r1-v4-v1.md` | `bb6652f2…` (égale au compagnon) | l. 66-73 (empreintes du découpeur) |
| `src/controle_ia/scellement.py` | — | liste des fonctions (`sceller` refuse d'écraser une empreinte différente) |
| `src/controle_ia/t07/criteres_v1.py` par `git show` à `a621dcd3` et `8ae9fc44` | `12b999fe…` aux deux commits | empreinte seule (Q-B4-6) |

Aucun fichier de `diag/`, de `runs/` ni de `donnees/` ouvert ; aucun chemin interdit ouvert ; recherches seulement par
`grep -n` sur des fichiers nommés. **Contact à déclarer** (consigne : le dire tel quel) : pour compter les objets
accessibles, j'ai lancé `git log --all --oneline | grep -c .`, qui parcourt les messages de commit de toutes les références
locales, y compris, s'il y en a dans ce clone, les branches de la règle 1 des interdits ; la sortie a été réduite à un
nombre (3292), aucun message ni nom de branche n'a été affiché, aucun fichier de ces branches n'a été lu ; je ne l'ai pas
refait. De même `git for-each-ref` (noms de références seulement, filtrés sur « decoupeur », aucune sortie) et `git worktree
list` (deux arbres : `main` et `scellement/p3bis-v1`).

## 7. Renvois du brouillon 3 aux lignes du brouillon 21, hors du § 2 (non changés ; information)

Chaque ligne citée du brouillon 21 est présente une fois, à l'octet, dans le texte scellé :

| renvoi (lieu au brouillon 4) | brouillon 21 | texte scellé |
|---|---|---|
| § 4, préalable 2 (« T0.7 l. 2078 ») | l. 2078 | l. 2199 |
| § 4, fenêtre et ouverture (« T0.7 l. 2046 », deux fois) | l. 2046 | l. 2166 |
| § 4 (« l. 2047-2050 ») | l. 2047-2050 | l. 2167-2170 |
| § 4 (« l. 1385-1390 ») | l. 1385-1390 | l. 1527-1532 |
| en-tête (« l. 2086 », « l. 2087 ») | l. 2086, 2087 | l. 2207, 2208 (dits par C04 et C05) |

## 8. Questions ouvertes pour la mère

- **Q-B4-1 (bloquant pour le scellement)** : commit du découpeur `c7484c43…` absent du clone local (§ 5) : l'amener (geste de
  la mère), puis relancer le script ; et confirmer que la consigne peut écrire l'exception à la règle 4 des interdits pour le
  seul `git archive` de ce commit et de ce dossier (R-2238 prévoit `git archive`, la règle 4 ne permet que `git show`).
  Variante sans exception : l'auditeur écrit les trois fichiers par `git show <commit>:<chemin> > <bac à sable>/<fichier>`,
  qui reste dans la lettre de la règle 4 ; je la recommande (confiance 0,7), défaut : la mère décide.
- **Q-B4-2** : l'objet du § 14.2 est, selon le mandat, le différentiel du brouillon 3 au brouillon 4 ; or le différentiel du
  brouillon 2 au brouillon 3 (corrections de la contre-lecture 1, essais 15 à 23, sous-commande `prealables`, contrôle des
  modules importés, réponse à CLAF-18) n'a jamais été contre-lu : R-2212 prévoyait une contre-lecture « des écarts » après
  le remplissage. Recommandation : donner aussi le brouillon 2 au contre-lecteur et étendre l'objet au différentiel 2 → 4
  (confiance 0,7) ; je ne l'ai pas écrit dans le § 14.2, pour suivre le mandat à la lettre.
- **Q-B4-3** : garder les couples de cohérence C02 à C07 et C20 (recommandé, confiance 0,75 : sans eux l'en-tête et les § 0,
  1 et 6 parlent d'une ligne « telle qu'elle sera au brouillon 22 » et d'un marqueur déjà rempli) ou les retirer un à un.
- **Q-B4-4** : renuméroter, au prochain brouillon, les renvois du § 4 aux lignes du texte scellé (table du § 7) ; ou laisser
  le repérage par chaîne exacte du § 5.1, point 7.
- **Q-B4-5** : le « Calendrier visé » du § 4 parle encore du brouillon 22 et du 12 novembre au soir ; inchangé.
- **Q-B4-6** (information) : la ligne `CODE-T07` existe désormais (R-2321, code `a621dcd3`) ; `criteres_v1.py` y a
  l'empreinte `12b999fe…`, égale à celle de `8ae9fc44` citée au § 5.1, point 6 : pas d'écart.
- **Q-B4-7** (rappel, hors mandat) : CLAF-18 reste « à vérifier contre P3-bis scellé » (§ 4).
