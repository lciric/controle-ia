# Devis — course A1-v4 (attaque de Goodhart contre le nul v9, mondes W2 et W2 gradué, hôte durable) — v1

Écrit le 8 novembre 2026 (16:39 UTC, calcul ; adapté à 16:48 UTC sur R-1890 ; heures `date -u`) par le rédacteur neuf du brouillon 3 (`preenregistrement-attaque-goodhart-v4-brouillon3.md`, ce dossier). **Aucune dépense engagée par ce fichier.** Tout chiffre renvoie à un chemin et une ligne ; le calcul est `devis-a1-v4-reprise-v9-v1.py` (arithmétique seule, `timeout 600 nice -n 10 python3 -I -B`), sortie `devis-a1-v4-reprise-v9-v1-sortie.txt` (ce dossier ; empreintes à relever par la mère au versement). Aucune donnée de course lue : les taux sont ceux que la note W2 a mesurés sur la sortie scellée de la troisième course d'A1-v3.

## 1. Deux lignes de GO, deux enveloppes

| objet | GO | montant | échéance | source |
|---|---|---|---|---|
| appels de modèle (Argon seul, `gemini-4-argon`) | **GO-2026-11-02-22** | **200 USD** (plafond du texte scellé, égalité exacte exigée par le lanceur) | 2026-11-16 | `registres/go.md` l. 210 |
| machine (hôte durable Vast : location, stockage, téléchargement) | **GO-2026-11-08-12** | **35 USD** | 2026-11-16 | `registres/go.md` l. 283 ; R-1890 (`registres/decisions.md` l. 1848) |

Les deux enveloppes ne se cumulent avec aucune autre : GO-2026-11-05-03 (35 USD, l. 251) est écrit pour l'hôte durable d'A1-v3 et ne couvre pas cette course ; les dépenses d'A1 (39,45 USD) et des trois courses d'A1-v3 (4,245753 ; 48,49583 ; 58,44887 USD ; `registres/depenses.md` l. 320, 328, 353, 376) ne s'imputent pas ici.

## 2. Taux mesurés (troisième course d'A1-v3, 5 novembre 2026)

Source : note W2, `docs/notes/ideation-organisme-v1/breche-w2-v1/couts-suite-w2-v1.txt` (compagnon dans le dossier), lignes 1 à 3, calculées sur la sortie scellée `e0b3145b…` et le journal du relais `494c70fb…` (960 appels, 58,44887 USD ; verdict `7dade9ef…` l. 70) :
- coût moyen par appel : **W1 0,0632 USD, W2 0,0413 USD** (l. 1) ; durée moyenne : **W1 9,4 s, W2 8,5 s** (l. 1) ;
- appels joués : W1 859 ; W2 **34,21 par unité**, 821 appels (l. 2–3) ;
- rejeu sous v8 mesuré : 0,0535 s par évaluation (l. 11) ; sous v9, mesuré à blanc le 2 novembre : 0,19 à 0,22 s sans appariement, 0,25 à 0,29 s avec (brouillon 2 public `7be8589e…`, § 9, L2, l. 376) ; le code v4 retient **0,5 s** (arrondi haut, `pole/attaque_goodhart_v4.py` l. 76) ;
- machine : **0,0617 USD/h** (GTX 1080, `registres/depenses.md` l. 371) ; relevé final Vast de la troisième course **0,284 USD** pour 4,417 h de carte, disque et téléchargement compris (l. 375) ; prix horaire maximal admis par le lanceur durable : **0,40 USD/h** ; vie maximale de la machine : **80 h** (texte V4-3 `0b35494b…`, § 8 l. 1654).

Hypothèses d'appels par unité du code v4 (`pole/attaque_goodhart_v4.py` l. 73) : W1 (36, 48) ; W2 (34, 40) ; maximum 64 par unité (4 suites × 16). **W2 gradué (W2g)** pris comme W2 : deux suites sous v9 sans promotion = 32 appels, plus 2 à 8 sous v8 ; une promotion sous v9 **raccourcit** la suite (arrêt à la première promotion), donc (34, 40) est une borne haute pour W2g ; le pire cas (64 par unité) est commun.

## 3. Périmètre retenu : W2 + W2 gradué (R-1890)

### 3.1 Appels (sous GO-2026-11-02-22, 200 USD)

| grandeur | attendu | pire cas | source |
|---|---|---|---|
| appels | **1 632 à 1 920** (24 × (34 à 40) × 2 mondes) | **3 072** (48 unités × 64) | sortie, ligne « variante W2+W2g » |
| USD aux taux mesurés (0,0413 bas, 0,0632 haut) | **67,40 à 121,34** | **194,15** (3 072 × 0,0632) | même ligne |
| USD aux appels mesurés de la troisième course (2 × 821 = 1 642) | **67,8 à 103,8** | — | sortie, ligne « variante (ii) aux appels mesurés » ; égal à la note W2 l. 47 et `couts-suite-w2-v1.txt` l. 5 |
| USD au taux du bloc `plan-gele` (0,062, ce que le lanceur recalcule) | 101,18 à 119,04 | **190,46** | B2v4 § 12 l. 423 (même forme ; le brouillon 2 comptait W1 : 104,16 à 130,94) |
| durée des appels, un fil (8,5 s bas, 9,4 s haut) | **3,85 à 5,01 h** | **8,02 h** à 9,4 s ; **34,13 h** à 40 s (hypothèse haute gardée du bloc) | sortie |

**Plafond 200 USD ≥ 194,15 ≥ 190,46** : le pire cas aux taux mesurés tient sous le GO ; un taux par appel 1,03 fois plus haut que le mesuré haut arrêterait la course au plafond au pire cas seulement (code 3, trace partielle, aucun taux lu) ; dans la bande attendue, le plafond est atteint à partir d'un taux de **0,104 USD par appel** (200 / 1 920), 1,65 fois le mesuré haut.

### 3.2 Rejeux et évaluations (processeur de la machine, 0 USD d'appels)

- en course : évaluations sous v9 appariées au v8 (0,56 s) et sous v8 : ≈ 0,24 h (B2v4 § 12 l. 424) ;
- rejeux : **307 200 évaluations sous v9** (24 unités × 2 mondes × 32 lois × 200 ; B2v4 l. 424–425) : **21,33 h** sur deux cœurs à 0,5 s ; **8,1 à 9,4 h** aux durées mesurées à blanc (0,19 à 0,22 s) (sortie, ligne « rejeux sous v9 ») ; 19 200 sous v8 (≈ 0,15 h) ; audit A2 : 200 rejeux par loi promue sous v9 (sur W2, attendu 0 ; sur W2g, jusqu'à 48 lois × 200 = 9 600, ≈ 0,3 à 0,7 h) ;
- **durée totale attendue ≈ 12 à 27 h** (appels 3,85 à 5,01 h, rejeux 8 à 21 h, marges) ; **pire cas 55,76 h** (B2v4 § 12 l. 426 : 34,13 h d'appels à 40 s + 21,39 h de rejeux + course) **< `duree_max_h: 72`** ; sur un relais mort non relancé, chaque tentative attend au plus 30 min avant d'être « échouée (relais) » ; une panne plus longue que la marge (≈ 16 h au pire cas) fait tomber la garde de 72 h (arrêt d'infrastructure, aucun taux lu).

### 3.3 Machine (sous GO-2026-11-08-12, 35 USD)

| durée de vie de la machine | à 0,0617 USD/h (mesuré) | à 0,40 USD/h (maximum admis) |
|---|---|---|
| 4,7 h (durée de la troisième course) | **0,29 USD** | 1,88 |
| 12 h (attendu bas : appels + rejeux mesurés) | 0,74 | 4,80 |
| 24 h (attendu haut) | **1,48** | 9,60 |
| 48 h | **2,96** | 19,20 |
| 80 h (vie maximale, minuterie) | 4,94 | **32,00** |

Source : sortie, lignes « machine ». **Attendu ≈ 0,3 à 3 USD** (la ligne GO-2026-11-08-12 dit de même) ; **au plus 32,00 USD** au prix maximal sur la vie maximale, plus ≈ 0,05 USD de disque et de téléchargement par la mesure de la troisième course (0,048 USD sur 0,284, l. 375) : **≤ 32,57 USD** comme V4-3 (§ 12 l. 1904) ; **plafond 35 USD**. Le lanceur durable refuse toute offre au-dessus de 0,40 USD/h et vérifie 35 USD exactement sur la ligne du GO.

### 3.4 Avant la course, à 0 USD

- épreuve hors ligne « W2 gradué » (note W2 § 2, étape 4) : ≈ 7 lignes × 1 000 répétitions, **29 à 58 min sur un cœur** (`couts-suite-w2-v1.txt` l. 8) ; fixe λ\* ;
- essais et mutations du code v5 et du lanceur durable v5 : processeur, quelques minutes à quelques dizaines de minutes ;
- contre-lecture, scellement : travail d'agents, aucun appel de modèle payant hors des sessions elles-mêmes.

### 3.5 Total attendu et pire cas du périmètre retenu

| | appels (GO-2026-11-02-22) | machine (GO-2026-11-08-12) | total |
|---|---|---|---|
| attendu bas (appels mesurés, taux bas, 12 h de machine) | 67,8 | 0,74 | **≈ 68,5 USD** |
| attendu haut (code, taux haut, 24 h de machine) | 121,34 | 1,48 | **≈ 122,8 USD** |
| pire cas (3 072 appels à 0,0632 ; 80 h à 0,40) | 194,15 | 32,57 | **≈ 226,7 USD**, sous les deux plafonds (200 + 35 = 235) |

## 4. Annexe — variante non retenue : W1 + W2 (brouillon 2 tel que rédigé), pour comparaison

| grandeur | attendu | pire cas |
|---|---|---|
| appels | 1 680 à 2 112 | 3 072 |
| USD aux taux mesurés | 69,38 à 133,48 | 194,15 |
| USD aux appels mesurés (859 + 821 = 1 680) | 88,2 à 106,2 (W1 au taux de W1, W2 au taux de W2 ; `couts-suite-w2-v1.txt` l. 4) | — |
| USD au taux du bloc (0,062) | 104,16 à 130,94 (B2v4 § 12 l. 423) | 190,46 |
| durée des appels | 3,97 à 5,51 h | 8,02 h (34,13 h à 40 s) |

Source : sortie, lignes « variante W1+W2 » et « variante (i) aux appels mesurés ». Même machine, mêmes rejeux. Écart avec le périmètre retenu : ≈ 2 à 12 USD d'appels en plus (W1 coûte plus cher par appel et par unité que W2 à la troisième course), pour une information que la note W2 juge faible (W1 sous v9 borné par monotonie ; `note-breche-w2-v1.md` l. 51). Non retenue par Lazar (R-1890).

## 5. Ce que ce devis ne couvre pas

- Une seconde course d'A1-v4 après un arrêt d'infrastructure : texte neuf et GO neuf (brouillon 3, § 0.5 bis).
- La réplication par Kimi (GO-2026-11-02-25, 150 USD, écrite pour A1-v3, l. 215) : hors de ce devis.
- Le travail d'agents (rédaction, contre-lecture, développement v5, verdict) : non chiffré en dollars ici.
- La rotation de la clé d'Argon (close sans rotation, R-1723).
