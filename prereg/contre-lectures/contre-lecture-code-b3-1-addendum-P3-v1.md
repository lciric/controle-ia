# Contre-lecture R2 du module final de l'addendum de P3, face au brouillon 3 (revue CB1)

**Verdict : scellable après corrections.** Deux constats majeurs (CB1-01, CB1-02), quatre mineurs (CB1-03 à CB1-06),
deux pour information (CB1-07, CB1-08). Les deux majeurs se corrigent en quelques lignes ; ils doivent l'être avant le
scellement, car après la lecture décisive le module ne peut plus changer.
Le calcul statistique est juste : A1, A2 (b), A3 et A4 (b), refaits à la main, égalent le module à 1e-12 près. Aucune
règle du brouillon 3 n'est absente du code. Les défauts sont ailleurs : un lecteur de fichier qui peut tuer l'addendum
entier, et une phrase de synthèse contraire aux critères gelés.

- Relecteur : sous-agent neuf (R2), qui n'a écrit ni le brouillon ni le module. Date : 2026-10-20 (UTC).
- Texte qui fait foi : `addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon3.md` (sha256
  `30a99398313dc3752d4b0eca0c75335103b58b81b23d48cee07e854ff66b130b`).
- Module relu : `addendum-p3/final/complements_p3_v1.py` (sha256
  `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa`, 2 083 lignes). Tests :
  `addendum-p3/final/test_complements_p3_v1.py` (sha256
  `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc`). Notes : `addendum-p3/final/NOTES-SYNTHESE.md`.
  Les deux empreintes sont celles des notes ; elles n'ont pas changé pendant la revue.
- Code gelé lu (dépôt de travail, lecture seule) : `premier_test_ia/lecture.py`, `statistiques.py`, `conditions.py`,
  `notation.py`, `run.py` ; `sondes/evaluation.py`, `sondes/temoins.py` ; `manifeste.py` ; `environnements/propositions.py` ;
  `harnais/validation_reelle.py` ; `scellement.py` ; `prereg.py`.
- Essais : `addendum-p3/rapports/revue-b3-1/` (scripts, journaux). Rien n'a été écrit ailleurs. Aucun fichier du dépôt de
  travail n'a été modifié. Tous mes lancements portent `-B` et `PYTHONDONTWRITEBYTECODE=1`.

## Ce qui a été fait

1. Lecture ligne à ligne du brouillon 3 et du module ; pour chaque phrase normative, la ligne qui l'applique (table en
   fin de rapport).
2. Suite de tests complète, depuis le dossier de revue : **117 passed in 589.47 s** (`revue-b3-1/pytest-complet.log`) ;
   de nouveau 117 passed sous relevé des lignes (`pytest-trace.log`, `pytest-trace2.log`).
3. Calcul à la main, par boucles explicites et `aire_sous_courbe` du code gelé, même flux de tirages que le module
   (`essai_main_A1_A2b_A3_A4b.py`, `essai_main_A1_T4_A2b_attention.py`, journaux `essai_main.log`,
   `essai_main_complement.log`) :
   - A1, cinq jeux (97,5 % sur saboteur contre honnête, 95 % ailleurs) : bornes de Δ et Δ observé égaux à 1e-12 ;
   - A1 sur T4 (tranches figées de la lecture) et A4 (a) (tranches recalculées dans chaque tirage) : égaux ; nombre de
     tranches par tirage égal ;
   - A2 (b), sonde au maximum et sonde à attention (softmax des logits restreints à la fenêtre) : les 2 × 50 fenêtres de
     chaque action, tirées dans l'ordre de `rang`, sont égales ; δ̄ observé et bornes de δ̄(b) égaux ;
   - A3 : bornes de Δ_ST et Δ_SM égales ;
   - A4 (b), tranche (tâche, rang de la copie) calculée explicitement : borne basse de Δ_intra et Δ observé égaux.
4. Essais pour casser : aire vectorisée contre le code gelé (2 947 cas aléatoires, ex aequo massifs, tranches à une
   classe : plus grand écart 2,2e-16) ; règles (1) et (2) de A5 et lecteur étendu de A6 sur 30 000 textes fabriqués (aucun
   `DefautDuModule`, aucune exception autre qu'une garde, position de la règle (2) toujours sur une clé du coût) ;
   lecture des textes avec des séparateurs Unicode (CB1-01) ; synthèse sur des entrées fabriquées (CB1-02, CB1-03) ;
   effectif de A4 (b) (CB1-05) ; relevé des gardes jamais exécutées par les tests (CB1-06 ; un premier relevé,
   `lignes-executees-contaminees-par-le-fichier-de-tests.json`, mêlait les lignes du fichier de tests, dont le nom finit
   de même : écarté, refait avec un filtre exact).

## Constats (le plus grave d'abord)

### CB1-01 — majeur — un texte d'action avec U+2028, U+2029 ou U+0085 rend l'addendum impossible

- **Où** : `charger_textes`, l. 2001-2007 (`donnees.decode("utf-8").splitlines()`), appelée par `executer`, l. 2034
  (garde 4, avant le manifeste).
- **Problème** : le run écrit les textes par `json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n"` (`run.py`,
  `_ecrire_textes`, l. 384-390). Ce codage laisse tels quels, dans les chaînes, U+2028, U+2029 et U+0085.
  `str.splitlines()` coupe la ligne à ces caractères ; `json.loads` lève alors `JSONDecodeError`. Ce n'est pas une
  `GardeArret` : l'addendum s'arrête avant le manifeste, sur une trace Python, pour un run source valide. Reproduit
  (`essai_textes_separateurs.py`, journal `essai_textes_separateurs.log`) : U+2028, U+2029, U+0085 →
  `json.decoder.JSONDecodeError : Unterminated string` ; texte normal et U+000B (que `json.dumps` échappe) → relus
  égaux. Un modèle de langue peut produire ces caractères (rare, mais 2 400 actions d'environ 300 jetons). Le module est
  scellé avant la lecture décisive : après elle, aucune correction n'est possible sans nœud de Lazar. Tout l'addendum
  serait perdu.
- **Correction** : découper sur `"\n"` seulement (`json.dumps` n'écrit jamais de saut de ligne brut) :
  `[json.loads(x) for x in donnees.decode("utf-8").split("\n") if x]` ; transformer une ligne illisible en `GardeArret`
  avec son numéro (aucun texte dans le motif). Tests : cas sain (textes avec U+2028, U+2029, U+0085, relus égaux à
  l'écrit, garde 5 passée) ; artefact (ligne tronquée : arrêt écrit, rien d'écrit sous `runs/`).

### CB1-02 — majeur — la recommandation au verdict qualifie « non robuste » une conclusion seulement non contrôlée

- **Où** : `synthese`, l. 1750-1757 (`recommandation_au_verdict_R13`).
- **Problème** : toute réserve, y compris `reserve_<analyse>_non_lue` et `reserve_addendum_largement_non_lu`, produit
  « établie au sens de la lecture décisive, non robuste aux contrôles de l'addendum (réserves : …) ». Les critères gelés
  (brouillon 3, l. 277) disent pour `reserve_<analyse>_non_lue` : « la conclusion reste établie ; le verdict cite qu'elle
  n'a pas été contrôlée ». Une conclusion non contrôlée n'est pas « non robuste ». Les lignes A7 des critères (l. 275-276 :
  « séparation non établie hors de cette forme du coût » ; « séparation confondue avec cette forme du coût, non séparable
  par restriction ») ne sont pas reprises non plus. Reproduit (`essai_synthese.py`, journal `essai_synthese.log`) :
  P3-P3 visée par la seule `reserve_A8_non_lue` → « P3-P3/sonde-a : établie au sens de la lecture décisive, non robuste
  aux contrôles de l'addendum (réserves : reserve_A8_non_lue) ». Le sous-agent du verdict R13 lit cette phrase. Le texte
  du brouillon est lui-même en tension : le plan, point 6 (l. 257-259), dit « pour chaque conclusion visée par au moins une
  réserve ».
- **Correction** : deux listes par conclusion. Réserves de contrôle contraire → « non robuste aux contrôles de l'addendum
  (réserves : …) » ; réserves « non lue » et réserve générale → « non contrôlée par l'addendum (réserves : …) ». Pour
  `reserve_A7_forme_du_cout` et `reserve_A7_forme_quasi_totale`, ajouter la lecture gelée des critères. Écrire la même
  règle au plan, point 6, du brouillon suivant. Test : une conclusion à réserve « non lue » seule ne reçoit jamais
  « non robuste ».

### CB1-03 — mineur — l'audit de symétrie lit « toutes non lues » comme « suspect de propreté »

- **Où** : `synthese`, l. 1735-1738.
- **Problème** : `declenchees` compte les contrôles « non lu » comme déclenchés. Si chaque contrôle d'une cible établie
  est « non lu » (analyses en échec), le déclencheur vaut vrai, motif « toutes les réserves possibles sont déclenchées »,
  lecture « addendum suspect de propreté ». Reproduit (`essai_synthese.py`, cas 2 : 2 réserves possibles, 2 « non lues »,
  déclencheur vrai). Le cas « tout a échoué » est celui de la garde 11, pas un résultat trop propre (R4). Le brouillon
  (l. 285-288) ne tranche pas.
- **Correction** : compter, pour « toutes », les seuls contrôles contraires (`controle_contraire is True`) ; rapporter à
  côté le nombre de « non lu ». Ou écrire le choix dans le brouillon.

### CB1-04 — mineur — arrêts ajoutés à la liste fermée

- **Où** : (a) cohérence lecture contre run source, `exiger_coherence`, l. 582-606, appelée l. 1833 et l. 2038 ;
  (b) égalité avec `lecture._localisation`, l. 642-646 ; (c) garde 5 renforcée (mesures relues), l. 413-419 ; (d) garde 9
  élargie à la commande du module, l. 2017 ; (e) un manifeste illisible sous `runs/` arrête les gardes 2 et 9,
  l. 1917-1928 ; (f) module exécuté hors de son chemin, l. 1892-1894 ; (g) graines de l'entropie de P3, l. 1799-1806 ;
  (h) forme du nom du run, l. 1873-1878 ; (i) paramètres de tirage, l. 225-236.
- **Problème** : la liste d'arrêt (l. 292-321) et la liste fermée des tests (l. 325-335) ne les nomment pas. Par lecture
  du code, aucune ne peut se déclencher sur un run réel cohérent, sauf (e) si un manifeste d'un autre run était abîmé :
  les 39 manifestes de `runs/` du dépôt de travail se lisent aujourd'hui (vérifié en lecture seule). Les notes (§ 4, § 7.2)
  le signalent déjà.
- **Correction** : les écrire dans le brouillon (liste d'arrêt et liste fermée des tests), ou les retirer. Pour (e),
  préférer : manifeste illisible = arrêt seulement s'il pourrait être une lecture décisive ou un passage de l'addendum
  (même motif écrit).

### CB1-05 — mineur — silences du texte comblés par le code, à écrire

- **Où et quoi** :
  - (a) A4 (b), l. 301 (via `ecart_conjoint`) : l'effectif minimal général (10 de chaque côté, « Seuil », l. 202)
    s'ajoute à « deux tâches mixtes et dix paires ». Reproduit (`essai_A4b_effectif.py`) : 4 tâches mixtes, 24 paires,
    11 positifs et 9 négatifs → « non calculable », alors que la règle propre de A4 (b) est remplie. Si T1 est établi,
    cela donne `reserve_A4_non_lue`.
  - (b) A8, l. 1548 : une action de trois jetons au plus compte « dans les trois premiers jetons ».
  - (c) Garde 11 : une entrée est « en échec » dès qu'un de ses calculs l'est (l. 924) ; une réserve générale par cible
    établie (l. 1726-1729).
  - (d) A2 (c), l. 1069 : le champ du coût entier est comparé à la fenêtre de longueur L qui le précède.
  - (e) A7 (iii), l. 1508-1510 : une corrélation non définie rend « non lu » (donc `reserve_A7_non_lue`).
  - (f) Garde 2, l. 1947 : l'empreinte du préenregistrement de P3 est comparée au fichier scellé, pas à celle que cite
    l'en-tête du brouillon (l. 15-16).
  - (g) A6, l. 1412-1413 : une entrée P3-P2 ou mention « non calculable » dans la lecture décisive rend le contrôle
    « non lu » ; la condition de réserve (« ne l'était pas dans la lecture décisive ») pourrait aussi se lire remplie.
- **Correction** : une ligne par point dans le brouillon suivant. Aucun changement de code demandé.

### CB1-06 — mineur — gardes jamais éprouvées par les tests (R5)

- **Où** : relevé des lignes exécutées par la suite de tests (greffon `revue-b3-1/trace_lignes.py`, journal
  `pytest-trace2.log` : 117 passed ; relevé `lignes-executees-module.json` ; liste `gardes_non_eprouvees.log`). Le module
  compte 101 instructions `raise` de garde ; **33 ne sont jamais exécutées** par les tests. Limite : la ligne de commande
  lancée dans un processus séparé n'est pas tracée (elle ne couvre que l'entropie, le passage réussi et le second
  passage).
- **Problème** : R5 (« toute garde d'arrêt testée sur un cas sain et sur un artefact ») et la liste fermée des tests du
  brouillon (l. 325-335) ne sont tenues qu'en partie. Branches de gardes nommées par le brouillon et jamais éprouvées :
  - garde 1 : préenregistrement sans l'entropie de P3 (l. 1891), sans les empreintes citées (l. 1898), tests absents
    (l. 1903) ;
  - garde 2 : manifeste de lecture présent mais `lecture-p3.json` absent (l. 1954 ; le test « absente » s'arrête avant,
    sur le manifeste manquant) ; `run_source` de la sortie autre que `--run-source` (l. 1961) ;
  - garde 3 : code de retour non nul de `git log` ou `git show` (l. 1971 ; seul `merge-base` est éprouvé) ;
  - garde 4 : empreinte des textes (l. 2006) ; branche morte en pratique, car `lecture.charger_source` vérifie déjà
    l'empreinte des textes et s'arrête avant ;
  - garde 5 : texte absent ou hors de forme (l. 407) ;
  - garde 7 : sept branches de typage (l. 446, 449, 456, 461, 473, 476, 480) ;
  - verrou : contrôle lu sur une cible non établie (l. 1780) ;
  - forme du run source : l. 522, 529, 531, 539, 541 ; plancher conjoint : l. 246, 305, 308, 317 ; autres : l. 361,
    598, 699, 711, 916, 1195, 1547, 1926.
  Branches mortes par construction : l. 699 et l. 711 (le tokeniseur par caractères décode toujours le texte ; la clé
  rendue par `bornes_champs` est toujours une clé de `_CLE_BRUTE`), l. 2006 (voir plus haut).
- **Correction** : un artefact par branche de garde nommée par le brouillon (gardes 1, 2, 3, 5, 7, verrou) ; pour les
  branches mortes, les retirer ou écrire qu'elles sont des défenses en profondeur, sans test possible.

### CB1-07 — information — fichier de cache dans le dossier final

- **Où** : `addendum-p3/final/__pycache__/complements_p3_v1.cpython-311.pyc`, créé le 2026-10-20 à 01:50:47 UTC.
- **Problème** : absent au début de la revue ; pas créé par elle (tous mes lancements portent `-B` et
  `PYTHONDONTWRITEBYTECODE=1`). Une autre revue lancée en parallèle (`rapports/revue-b3-2/`, créé à 01:51:12) l'a
  probablement écrit. Copié sous `docs/procedures/P3-addendum-v1/`, il ferait échouer `verifier-arbre` (notes, § 7.3).
- **Correction** : ne verser que les deux fichiers `.py` ; supprimer ce cache avant le versement (je ne l'ai pas touché).

### CB1-08 — information — ce qui tient

- 117 tests passent ; empreintes inchangées.
- A1, A2 (b), A3, A4 (a), A4 (b) refaits à la main : égaux à 1e-12 (voir « Ce qui a été fait »).
- Verrou : table fermée des conclusions (l. 502-512) conforme ligne à ligne au plan, point 5 ; « sans objet » sans rien
  hors du descriptif (l. 908-910, vérifié sur la sortie l. 1775-1780) ; clés interdites retirées des sorties gelées
  (l. 827-834) et cherchées dans toute la sortie (l. 1781-1783) ; issue recopiée et lecture inchangée (l. 1824-1826,
  l. 1865-1867).
- Règle des jetons : chaque score d'empan passe par `agreger_par_jeton` (l. 630-631, 994, 998, 1001, 1004) ; les seules
  moyennes portent sur des aires de jeu (δ̄, l. 1030), sur des poids (A8) ou sur des tâches (A9).
- Règles (1) et (2) de A5 : les quatre cas du brouillon donnent les valeurs du test ; aucune divergence inventée sur
  30 000 textes fabriqués.

## Texte face au code (chaque phrase normative et la ligne qui l'applique)

| brouillon 3 | module | état |
|---|---|---|
| En-tête : empreintes du module et des tests lues par expression régulière | l. 75-76, 1896-1906 | conforme |
| Statut non décisif | l. 77, 2042 (`decisif=False`) | conforme |
| Entrées : run source, textes lus sur place, lecture vérifiée | l. 2033-2036, 440-485 | conforme ; lecture des textes : CB1-01 |
| Actions notées (scores tous finis) | l. 550 | conforme |
| Aire vectorisée égale à 1e-12 | l. 164-220 | conforme (essai : 2,2e-16) |
| Score d'empan par `agreger_par_jeton`, jamais de moyenne de jetons | l. 630-631, 994-1004, 1528-1551 | conforme |
| Famille « attention » contre `agregation` (arrêt) | l. 563-579 | conforme |
| Rééchantillonnage par blocs, dégénérescence, 1 % | l. 251-270, 299-336 | conforme |
| Graines `addendum/<analyse>/<sonde>/<objet>` | l. 239-240, 1786-1806, 2041-2044 | conforme |
| Niveaux (table fermée) | l. 84, 947-951, 1065, 1156, 1253-1257, 1292, 1482 | conforme |
| Forme de la sortie (`descriptif`, `controles`, `cible`, `controle_contraire`) | l. 869-925 | conforme |
| A1 : Δ = A − Q0,95 par tirage, cinq jeux, T1, T4, cibles, placebo descriptif | l. 113-115, 938-970 | conforme (calcul à la main) |
| A2 (a) à (d) | l. 975-1092 | conforme ; (c) : CB1-05 (d) |
| A3 : Δ_ST, Δ_SM, bornes hautes descriptives | l. 1097-1171 | conforme (calcul à la main) |
| A4 (a), (b), (c) | l. 1176-1283 | conforme ; (b) : CB1-05 (a) |
| A5 : règles (1) et (2), divergences, invalides, `T2_propre`, sensibilité descriptive | l. 692-803, 1288-1346 | conforme |
| A6 : lecteur étendu, population de `cout`, comptes, effets refaits | l. 806-816, 1351-1419 | conforme ; CB1-05 (g) |
| A7 (i), (ii), (iii) | l. 660-673, 1424-1514 | conforme ; (iii) : CB1-05 (e) |
| A8 : jeton dominant, règle stricte, segments, poids | l. 1519-1628 | conforme ; CB1-05 (b) |
| A9 descriptif | l. 1633-1666 | conforme |
| Seuil : effectif minimal, table des réserves, cible établie sinon « sans objet » | l. 273-278, 904-921 | conforme |
| Plan 1 à 4 : ordre, commande, gardes avant le manifeste, sortie unique | l. 2022-2075 | conforme |
| Plan 5 : verrou mécanique | l. 497-512, 1763-1783 | conforme |
| Plan 6 : synthèse | l. 1713-1760 | recommandation : CB1-02 |
| Plan 7 : recalcul de l'issue et des états | l. 422-437 | conforme |
| Plan 8 : nombre de contrôles à côté des réserves | l. 1732-1734, 1758-1759 | conforme |
| Critères : verrou unidirectionnel | l. 1824-1826, 1865-1867 | conforme |
| Critères : audit de symétrie | l. 1734-1749 | CB1-03 |
| Critères : lecture des réserves au verdict | l. 1750-1757 | CB1-02 |
| Gardes 1 à 11 | l. 1881-1908, 1938-1965, 1975-1998, 2033-2036, 395-419, 422-437, 440-485, 488-494, 2010-2019, 563-579, 1723-1729 | conformes ; ajouts : CB1-04 |
| Seule `GardeArret` donne « échec » ; toute autre exception arrête ; arrêt écrit après le manifeste | l. 880-894, 1672-1690, 2049-2056 | conforme |

**Règles absentes** : aucune. **Règles ajoutées** : CB1-04 (arrêts) et CB1-05 (silences comblés).
