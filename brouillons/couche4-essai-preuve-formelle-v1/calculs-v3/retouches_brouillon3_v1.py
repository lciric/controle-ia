"""retouches_brouillon3_v1.py — du brouillon 2 (`05bcf094…`) au corps du brouillon 3 : vérification courte du brouillon 2
(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md`, `38e40d21…`, VL-01 à VL-08) et
décisions de la mère. Chaque remplacement : une seule occurrence, blancs normalisés ; les chiffres viennent de
`calculs-v3/sortie-calibrage-score-apparie-v1.txt` et `calculs-v3/sortie-calculs-devis-v5.txt`. Aucun appel, aucun réseau.
Usage : python retouches_brouillon3_v1.py BROUILLON2 SORTIE (la table des empreintes est refaite à part)."""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
T = Path(sys.argv[1]).read_text(encoding="utf-8")
FAIT = []


def motif(a):
    return r"\s+".join(re.escape(m) for m in a.split())


def rep(nom, ancien, nouveau):
    global T
    t = list(re.finditer(motif(ancien), T))
    assert len(t) == 1, f"{nom} : {len(t)} occurrence(s)"
    d, f = t[0].span()
    T = T[:d] + nouveau + T[f:]
    FAIT.append(nom)


def rep_bloc(nom, debut, fin, nouveau):
    global T
    t = list(re.finditer(motif(debut) + r".*?" + motif(fin), T, re.S))
    assert len(t) == 1 and len(re.findall(motif(debut), T)) == 1, f"{nom} : bloc introuvable ou ambigu"
    d, f = t[0].span()
    T = T[:d] + nouveau + T[f:]
    FAIT.append(nom)


def section(nom, titre_debut, titre_fin, nouveau):
    global T
    i = T.index("\n" + titre_debut) + 1
    j = T.index("\n" + titre_fin, i) + 1
    T = T[:i] + nouveau + T[j:]
    FAIT.append(nom)


# ------------------------------------------------------------------ en-tête
rep("S01 titre", "— dessin et devis — v1, brouillon 2", "— dessin et devis — v1, brouillon 3")
rep("S02 heures", "brouillon 2 à 13:30:55 UTC ;", "brouillon 2 à 13:30:55 UTC, brouillon 3 à 13:58:22 UTC ;")
rep("S03 statut", "**brouillon 2, contre-lu une fois, non préenregistré**. La contre-lecture 1",
    "**brouillon 3, contre-lu une fois et vérifié une fois, non préenregistré**. La vérification courte du brouillon 2 "
    "(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md`, `38e40d21…`, Claude Fable 5.2, "
    "même modèle que le contre-lecteur 1 ; « présentable à Lazar pour D-1a » ; VL-01, VL-04 et VL-05 bloquaient le scellement) est "
    "appliquée avec les décisions de la mère (§ 0) ; calculs neufs sous `calculs-v3/`. La contre-lecture 1")
rep("S04 journal",
    "Journal : `essai-preuve-formelle-devis-v1-journal-v2.md` (même dossier). Le brouillon 1 (`9ccc9ac0…`) et son journal "
    "(`f8c2b8c6…`) restent intacts.",
    "Journal : `essai-preuve-formelle-devis-v1-journal-v3.md` (même dossier). Les brouillons 1 (`9ccc9ac0…`) et 2 (`05bcf094…`), "
    "leurs journaux et `calculs-v1/`, `calculs-v2/` restent intacts.")

# ------------------------------------------------------------------ verdict
section("S05 verdict", "## Verdict", "---\n\n## 0.", """## Verdict

1. **L'essai est faisable sur processeur, en trois pas payés séparément.** **D-1a — outillage** : machine dédiée et isolée, Lean et
   Mathlib à un commit fixé, gardes éprouvées ; **aucun appel de modèle** ; plafond **65 USD**, tenu par une **minuterie de
   destruction de la machine à 48 heures** (A13) même au prix horaire de borne haute (48 × 1,30 = 62,40) : **le premier GO n'engage
   que 65 USD**. **D-1b — pilote** (140 items), **seulement après le préenregistrement complet, contre-lu et scellé** : attendu
   **≈ 337 à 457 USD** au profil supposé, **≈ 606 à 726** au profil « pire réaliste » de l'agent formel ; plafond proposé **578 USD**,
   le plus petit qui garde **40 graines même si chaque item formel coûte 4 USD** (52 au profil pire réaliste, les 60 au profil
   supposé), plus **35 USD** de machine (minuterie à 26 heures). Ces 40 graines sont l'effectif du pilote réduit qu'écarte
   D-1b (iii) : le dire à Lazar (§ 4.3). **Phase 2 — confirmation** (deux classes) : attendu **≈ 1 299 USD** au plafond d'effectif
   (1 346 avec 60 % d'items litigieux ; 1 865 à 1 912 avec les lignes conditionnelles), **≈ 2 451 à 3 064** au profil pire
   réaliste ; plafond **indicatif 1 950 USD**, fixé par le devis 2, second GO.
2. **Somme des plafonds : 2 719 USD ; ce n'est pas un maximum.** Si le pilote mesure le profil pire réaliste, l'enveloppe complète
   est d'**environ 3 252 à 3 865 USD** (la vérification courte, au plafond de D-1b de 550, trouvait ≈ 3 224 à 3 790) (VL-03).
3. **Méthode des intervalles fixée avant toute donnée** (VL-01) : score apparié (dit de Tango) avec des **valeurs critiques
   calibrées par affirmation et par effectif, par énumération exacte** ; au z nominal, aucune méthode ne tenait sa cible (le
   gabarit de Wald du brouillon 2 laissait « sous le seuil » à 0,051 par classe pour une cible de 0,0125). La formule est contrôlée
   par dérivation mais **sa source reste à lire** (`<<SOURCE_TANGO>>`), avec un repli écrit.
4. **Obstacles avant toute dépense** : aucun vérificateur installé ; 2,7 Go libres ; la **cloison** : machine sans clé ni dépôt
   du programme, **intégrité de la machine** elle-même (lecture seule, dossier neuf par item, aucune persistance, clé de la banque
   jamais sur la machine) et réseau coupé avant tout code écrit par un modèle (VL-05). Dépense : **appels d'interface chez quatre
   fournisseurs et machine louée** (CLP-05). Repli du planteur : **R2 (reporter) par défaut**, R1 seulement sur mot de Lazar.
5. **L'essai ne rouvre pas la couche 4** : il produit une pièce pour la décision que Lazar prendra après l'étape 2 (N12 (b)). Ma
   prédiction (§ 1.4) reste que la chaîne formelle ne franchit pas le critère conjoint.

""")

# ------------------------------------------------------------------ § 0
rep("S06 § 0 brouillon 3", "pièces à remplir nommées (§ 9) ; D-6 non pour l'instant.",
    "pièces à remplir nommées (§ 9) ; D-6 non pour l'instant.\n"
    "- **Brouillon 3 — ce qui change** (vérification courte et décisions de la mère, aucune n'engageant de dépense) : méthode "
    "d'intervalle fixée par énumération exacte, critère par queue et par affirmation, valeurs critiques calibrées, formule contrôlée et "
    "source marquée `<<SOURCE_TANGO>>` (VL-01, § 3.6) ; deux phrases fausses corrigées (§ 1.7, D-5) ; minuterie de destruction des "
    "machines (VL-02, A13) ; « somme des plafonds » et enveloppe au profil pire réaliste (VL-03) ; A8 réécrit comme le script le "
    "calcule, coupure sous 40 graines écrite, plafond de D-1b à 578, aveu sur les 40 graines (VL-04) ; intégrité intérieure de la "
    "machine, épreuve d'isolement qui a un sens, ordre d'installation, repli R2 par défaut (VL-05) ; niveaux des bornes des fausses "
    "alertes et périmètre de la famille (VL-06) ; résidus des couples (VL-07) ; traçabilité (VL-08) ; prix d'Argon lu sur une page "
    "archivée (§ 4.1).")

# ------------------------------------------------------------------ § 1
rep("S07 tests et bornes",
    "- **Intervalles** : à **97,5 %** bilatéraux pour Δ_k de chacune des deux classes (Bonferroni sur deux classes, sans porte, "
    "C04) ; méthode fixée **avant le pilote** par simulation de couverture (C09, § 3.6) ; borne des fausses alertes de "
    "Clopper–Pearson à 97,5 %.",
    "- **Tests et bornes** (VL-01, VL-06) : chaque affirmation sur Δ_k (« B > 0 », « B ≥ δ », « H < δ ») est un test unilatéral au "
    "niveau **0,0125 par classe** (deux classes, Bonferroni, sans porte, C04), par le **score apparié à valeurs critiques calibrées "
    "par affirmation et par effectif** (§ 3.6) ; la famille des deux classes est ainsi tenue à 0,025 **par affirmation** sur la "
    "grille de la nuisance. Fausses alertes : **borne haute unilatérale** de Clopper–Pearson à 97,5 % (queue 0,025) ; l'affirmation "
    "« fausses alertes bornées » est une affirmation de plus, à 0,025, **hors** de la famille des affirmations sur Δ.")
rep("S08 O2 lecture",
    "l'écart vient des échecs de formalisation, non d'une détection, et le rapport le dit en tête. |",
    "l'écart vient des échecs de formalisation, non d'une détection, et le rapport le dit en tête. La condition H(φ_L) > φ_max "
    "n'établit pas φ_L > φ_max : O2 se lit « fausses alertes non bornées sous φ_max », non « fausses alertes établies au-dessus » "
    "(VL-06). |")
rep("S09 trois fois sur cent",
    "alors que « sous le seuil » n'y sort qu'environ trois fois sur cent :",
    "alors que « sous le seuil » n'y sort qu'environ trois fois sur cent **à 95 %, au gabarit du brouillon 1** (au niveau 97,5 % "
    "retenu, le même gabarit le laisse sortir jusqu'à 0,051 par classe pour une cible de 0,0125 : calcul exact, `calculs-v3/`, VL-01) :")
rep_bloc("S10 issues à 97,5 %", "**Au niveau retenu de 97,5 %** (C04 ;", "la discordance (0,20 à 0,40).",
         "**Avec le score calibré** (`calculs-v3/sortie-calibrage-score-apparie-v1.txt`, bloc 3 ; calcul exact ; n = 102 et 150, "
         "discordance 0,30 et 0,40) : à la frontière, la condition de rappel de O1 sort 0,49 à 0,53 et O1a 0,008 à 0,011 ; pour un Δ "
         "vrai de 0,15, la condition de rappel sort 0,14 à 0,20 ; pour un Δ vrai de 0,30, O1a sort 0,28 à 0,73 ; « sous le seuil » à "
         "la frontière, 0,010 à 0,012 (cible 0,0125).")

# ------------------------------------------------------------------ § 2.7
rep("S11 repli R2",
    "Recommandation : (R2) tant que l'échéance de D-1b n'est pas atteinte, (R1) au-delà ; c'est un nœud de compte, chez Lazar.",
    "**Retenu par défaut et fixé dans le texte scellé : (R2)** ; (R1) seulement sur mot de Lazar **avant** le scellement : passer à R1 "
    "après le scellement serait un écart à un préenregistrement (nœud) ; c'est aussi un nœud de compte (VL-05).")

# ------------------------------------------------------------------ § 3.6
rep("S12 borne FA niveau", "probabilité que H(φ_L) ≤ 0,30 (Clopper–Pearson 97,5 %) :",
    "probabilité que H(φ_L) ≤ 0,30 (borne haute **unilatérale** de Clopper–Pearson à 97,5 %, queue 0,025) :")
rep("S13 devis central", "plafond de 150 inchangé ; devis central à refaire)",
    "plafond de 150 inchangé ; devis refait en v4, « central » retiré)")
rep_bloc("S14 issues et famille", "- **Probabilités des issues à 97,5 %**", "(« ampleur non établie »).",
         "- **Probabilités des issues** (score apparié à valeurs critiques calibrées, calcul exact, "
         "`calculs-v3/sortie-calibrage-score-apparie-v1.txt`, bloc 3 ; « gain » = condition de rappel commune à O1 et O2, sans la "
         "condition des fausses alertes ; « sous le seuil » = O3 ; « non concluante » = O4) : à n = 102 et d = 0,30 : Δ vrai 0 → sous "
         "le seuil 0,913 ; Δ vrai 0,10 → sous le seuil 0,331, non concluante 0,639, gain 0,029 ; **Δ vrai 0,20 → gain 0,490** (O1a "
         "0,009), sous le seuil 0,010 ; Δ vrai 0,30 → gain 0,988 (O1a 0,503). À n = 150 et d = 0,30 : 0,984 ; 0,481 / 0,505 ; 0,530 "
         "(O1a 0,011) ; 0,998 (O1a 0,731). Le brouillon 2 les donnait au gabarit de Wald, par tirages (v4, bloc 2).\n"
         "- **Erreur de famille** (calcul exact, blocs 1 et 2) : avec les valeurs critiques calibrées, chaque affirmation (« B > 0 » "
         "sous Δ = 0 ; « H < δ » et « B ≥ δ » sous Δ = δ, bord p₀₁ = 0 compris) tient 0,0125 par classe sur toute la grille de la "
         "nuisance, donc au plus 0,025 pour deux classes, affirmation par affirmation ; la famille ne contient que les affirmations sur "
         "Δ (les fausses alertes sont à part, § 1.6). Au z nominal, les erreurs exactes maximales par classe étaient : gabarit de Wald "
         "0,0151 (« B > 0 », n = 40, discordance 0,75), **0,0506** (« H < δ », n = 43, au bord p₀₁ = 0) et 0,0172 (« B ≥ δ ») ; "
         "score de Tango non calibré 0,0126, 0,0142 et **0,0224** (« B ≥ δ », n = 56, discordance 0,22) ; Newcombe dépasse aussi "
         "(vérification courte, bloc B). Les fourchettes « 0,020 à 0,026 » et « 0,027 à 0,060 » du brouillon 2 venaient de tirages sur "
         "une grille plus étroite (VL-07 d). La condition « estimation ≥ δ » n'est pas une affirmation : à Δ vrai = 0,15, elle sort "
         "encore 0,14 à 0,20 par classe (bloc 3), ce que O1b dit en clair (« ampleur non établie »).")
rep_bloc("S15 méthode", "- **Méthode d'intervalle du préenregistrement** :", "pendant D-1a, avant tout appel de modèle.",
         "- **Méthode du préenregistrement** (VL-01 ; **remplace la règle de C09**, qui désignait un ensemble vide : aucune méthode "
         "n'a une couverture minimale au-dessus du nominal, et la couverture bilatérale cachait des queues à 0,02) : **score apparié** "
         "(dit de Tango) ; **valeurs critiques calibrées par affirmation et par effectif** par **énumération exacte** de la loi "
         "trinomiale, sans tirage, sur une grille écrite d'avance : n de 40 à 150 (tous les entiers) ; Δ = 0 avec une discordance de "
         "0,01 à 0,80 ; Δ = δ avec une discordance de δ (bord p₀₁ = 0) à 0,80 ; pas de 0,01. **Critère, par queue et par "
         "affirmation** : z*(n) est le plus petit z ≥ 2,2414 (pas 0,0005) dont l'erreur exacte maximale sur la grille est ≤ 0,0125 ; "
         "rejet inclusif. **Résultat** (`calculs-v3/calibrage_score_apparie_v1.py`) : z* maximal 2,2634 pour « B > 0 », 2,2939 pour "
         "« H < δ », 2,5169 pour « B ≥ δ » (O1a, n = 57) ; la table par effectif est scellée (`calculs-v3/valeurs-critiques-calibrees-v1.json`) "
         "et le script d'analyse l'applique à l'effectif réalisé sans regarder les verdicts. O1a est lu à sa valeur plus sévère sans "
         "redimensionner ; la règle d'effectif garde 2,2414 (« B > 0 » et « H < δ » demanderaient au plus 2 % et 5 % d'effectif en plus à "
         "largeur égale, et la règle est au plafond de 150 dès 15 discordantes sur 60). Discordance au-delà de 0,80 (hors grille) : "
         "lecture confirmatoire suspendue, cas rapporté ; effectif réalisé sous 40 : aucune lecture confirmatoire. **Formule** : "
         "q = [√(B² − 4AC) − B] / (2A), avec A = 2n, B = −n₁₀ − n₀₁ + (2n − n₁₀ + n₀₁)Δ₀, C = −n₀₁Δ₀(1 − Δ₀) ; "
         "S(Δ₀) = (n₁₀ − n₀₁ − nΔ₀) / √(n(2q + Δ₀(1 − Δ₀))) ; « B > 0 » ⇔ S(0) ≥ z* ; « B ≥ δ » ⇔ S(δ) ≥ z* ; « H < δ » ⇔ "
         "S(δ) ≤ −z*. **Source : `<<SOURCE_TANGO>>`** (forme donnée de mémoire par la vérification courte et par le rédacteur ; aucune "
         "source lisible sans réseau ni dans le dépôt). **Contrôle fait** : q coïncide avec le maximum de vraisemblance sous la contrainte "
         "p₁₀ − p₀₁ = Δ₀ calculé numériquement (écart maximal 6·10⁻⁹ sur 3 000 cas) et S se réduit à McNemar pour Δ₀ = 0 (bloc 0). "
         "**Repli écrit** si la source dément la forme close : la statistique est **définie par ces principes** (score sous contrainte, "
         "maximum calculé numériquement), sans attribution, et les valeurs critiques se recalibrent par le même script. McNemar exact "
         "rapporté en complément. Le marqueur « À REMPLIR : SOURCE-TANGO » (§ 9) bloque le scellement tant que la source n'est pas lue "
         "ou le repli adopté.")

# ------------------------------------------------------------------ § 3.8
rep("S16 A1", "- **A1** gardes G-L1 à G-L7, garde d'isolement (§ 4.5), plafonds, compteurs, réserve de A7 et refus de A12",
    "- **A1** gardes G-L1 à G-L7, garde d'isolement et garde d'intégrité de la machine (§ 4.5, VL-05), minuterie de A13, plafonds, "
    "compteurs, réserve de A7 et refus de A12")
rep_bloc("S17 A8", "- **A8** étalonnage :", "d'où le plafond proposé de 550 (§ 4.3).",
         "- **A8** étalonnage (VL-04) : la banque du pilote est construite d'abord (72 graines plantées et contrôlées) ; viennent "
         "ensuite les **20 items de contrôle** (10 témoins, 10 saines renotées bis), puis les graines par **blocs équilibrés** de 5 "
         "(une par classe). Après les 20 items de contrôle et les deux premiers blocs (10 graines, soit 20 items analysables ; 40 items "
         "en tout, chacun vu par les deux bras et la lecture nue), le harnais calcule **G = 10 + ⌊(P − D − R − H) / c⌋**, où P est le "
         "plafond, D la dépense faite, R la réserve de A7 (32 USD), H les charges hors graines restant à payer (adjudication du tirage "
         "de 20 items non litigieux, audit restant, lignes conditionnelles déjà déclenchées) et c le coût **mesuré** d'une graine (deux "
         "items vus par les deux bras et la lecture nue, leur audit, leur adjudication à la part litigieuse mesurée) ; le pilote est "
         "ramené à G graines, arrondi au bloc inférieur. **G < 40 ⇒ arrêt** avant toute autre graine : issue « pilote non payable au "
         "plafond », aucune fiche de passage, devis refait, nouveau GO. **Si A7 coupe en cours de route sous 40 graines** : pilote "
         "tronqué, lu en description seulement (aucun choix de classes, aucune fiche de passage, aucune phase 2 sans nouveau GO). "
         "Chiffres (`calculs-v3/sortie-calculs-devis-v5.txt`, bloc 1, même formule) : à 578 USD, 115 graines payables au profil "
         "supposé (le pilote complet de 60), 52 au profil pire réaliste (10 blocs, 50 graines équilibrées), **40 si chaque item formel "
         "coûte 4 USD** (8 blocs) ; à 550, 107, 48 et 37 (arrêt). Pistes chiffrées si A8 menace : fin sans parallélisme (réserve 12 au "
         "lieu de 32) et abandon de la lecture nue (diagnostic) : 44 graines au lieu de 40 au cas « tout à 4 USD », 57 au lieu de 52 au "
         "profil pire réaliste ; elles s'écrivent au préenregistrement ou ne s'appliquent pas.")
rep("S18 A9 niveau", "si la borne basse à 95 % (Clopper–Pearson) de φ_L au pilote dépasse φ_max",
    "si la borne basse **unilatérale à 97,5 %** (Clopper–Pearson, queue 0,025 : borne basse de l'intervalle bilatéral à 95 %, "
    "VL-06) de φ_L au pilote dépasse φ_max")
rep("S19 A13",
    "refuse tout appel sans identifiant de GO valide (garde éprouvée sur un cas sain et sur un artefact).",
    "refuse tout appel sans identifiant de GO valide (garde éprouvée sur un cas sain et sur un artefact).\n"
    "- **A13** (VL-02) machine : fournisseur et prix horaire consignés avant la location ; cumul « heures allumées × prix » relevé à "
    "chaque heure ; **minuterie de destruction par identifiant (R10)** au plus tard à **48 heures** pour D-1a, **26** pour D-1b, "
    "**70** pour la phase 2, et destruction plus tôt dès que le cumul atteint le plafond moins une heure ; aucune machine allumée sans "
    "tâche en cours ; garde éprouvée sur un cas sain et sur un artefact (R5). Les plafonds tiennent même à 1,30 USD l'heure (62,40 ≤ "
    "65 ; 33,80 ≤ 35 ; 91,00 ≤ 91 ; v5, bloc 4). Une machine détruite emporte son installation : la chaîne et Mathlib, épinglées, se "
    "réinstallent à l'identique au pas suivant, dans la minuterie de ce pas.")

# ------------------------------------------------------------------ § 4
rep("S20 prix Argon",
    "| Gemini 4 Argon (contrôle, audit, adjudication) | 10 | 50 | `collisionneur_v8.py` l. 73–74 : « valeur volontairement haute » | **à vérifier** |",
    "| Gemini 4 Argon (contrôle, audit, adjudication) | 10 | 50 | `collisionneur_v8.py` l. 73–74 : « valeur volontairement haute » ; "
    "page archivée `docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html` (`ad2140dd…`) : 2 / 10 jusqu'au 30 novembre 2026, "
    "4 / 20 à partir du 1er décembre | **lu sur page archivée** ; le devis garde 10 / 50 (prudent ; sensibilité au § 4.3) |")
rep("S21 D-1a minuterie", "**Plafond proposé : 65 USD** (machine seule). Durée : 2 à 3 jours.",
    "**Plafond proposé : 65 USD** (machine seule), tenu par la **minuterie de destruction à 48 heures** (A13 ; 48 × 1,30 = 62,40). "
    "Si l'outillage n'est pas fini à l'échéance, la machine est détruite quand même et un nouveau GO est demandé. Durée : 2 à 3 jours "
    "de travail, dont au plus 48 heures de machine.")
rep_bloc("S22 C08 daté", "**Lignes absentes du tableau du brouillon 1, comprises dans le plafond**",
         "les mêmes lignes sont à ajouter au devis 2.",
         "Les lignes conditionnelles et l'adjudication, absentes du brouillon 1, avaient été estimées par la contre-lecture 1 (annexe, "
         "bloc E) contre l'ancien plafond de 450 ; elles sont chiffrées ci-dessus par script (v4, repris en v5) et figurent au devis 2 "
         "(VL-07 a).")
rep_bloc("S23 plafond D-1b", "**Plafond proposé de D-1b : 550 USD**", "**plafond machine proposé : 35 USD**.",
         "**Plafond proposé de D-1b : 578 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser). Raison (VL-04, "
         "`calculs-v3/sortie-calculs-devis-v5.txt`, bloc 1) : c'est le plus petit plafond qui garde **40 graines même si chaque item "
         "formel coûte 4 USD** (577,66) ; il couvre au profil supposé l'attendu avec toutes les lignes conditionnelles (448 à 457) "
         "plus la réserve de A7, et garde 52 graines au profil pire réaliste (550 en gardait 48 ; 450, 35). **Ce qu'il faut dire "
         "franchement** : 40 graines (8 par classe) est **exactement l'effectif du pilote réduit que D-1b (iii) écarte** parce que huit "
         "items par classe ne portent pas un choix de classes ; au profil pire réaliste (50 graines équilibrées, 10 par classe), le "
         "pilote payé n'en est guère au-dessus. Conséquences : si A8 ramène le pilote sous 60 graines, la fiche de passage marque le "
         "choix des classes « fragile » et le dit au second GO ; la variante (i bis) de D-5 (K1 fixée d'avance) en dépend moins, une "
         "seule classe y étant choisie sur le pilote ; garder 60 graines demanderait 639 USD au profil pire réaliste et 767 au cas « tout "
         "à 4 USD ». Machine : ≈ 26 heures allumées, minuterie de destruction à 26 heures (A13), 33,80 à 1,30 USD l'heure ; **plafond "
         "machine proposé : 35 USD**.")
rep("S24 plafond phase 2",
    "**Plafond indicatif de la phase 2 : 1 900 USD** (profil supposé, plafond d'effectif : attendu avec toutes les lignes "
    "conditionnelles 1 865,20, plus la réserve de A7).",
    "**Plafond indicatif de la phase 2 : 1 950 USD** (profil supposé, plafond d'effectif, **60 %** d'items litigieux : attendu avec "
    "toutes les lignes conditionnelles 1 912,00, plus la réserve de A7, soit 1 944, arrondi ; 1 900 ne couvrait pas ce cas, VL-07 c ; "
    "v5, bloc 3).")
rep("S25 machine phase 2", "plafond machine indicatif 91 USD.",
    "plafond machine indicatif 91 USD, minuterie de destruction à 70 heures (A13).")
rep_bloc("S26 somme des plafonds", "**Engagement maximal** (plafonds proposés ou indicatifs)",
         "du plafond de D-1b relevé pour le profil pire réaliste.",
         "**Somme des plafonds** (proposés ou indicatifs ; VL-03 ; v5, bloc 5) : D-1a 65 + D-1b 578 + 35 (machine) + phase 2 1 950 + 91 "
         "(machine) = **2 719 USD**. **Ce n'est pas un maximum** : si le pilote mesure le profil pire réaliste, la phase 2 complète "
         "demanderait 2 483,40 à 3 096,00 USD (attendu plus réserve de A7, de 30 % d'items litigieux sans lignes conditionnelles à 60 % "
         "avec elles), soit une **enveloppe d'environ 3 252 à 3 865 USD** (au plafond de D-1b de 550 et à 30 % d'items litigieux, la "
         "vérification courte trouvait ≈ 3 224 à 3 790 ; même calcul, bloc 5) ; ou une phase 2 réduite sous son plafond. **Le premier "
         "GO (D-1a) n'engage que 65 USD.** Attendu au profil supposé : D-1b et phase 2, ≈ 1 637 à 2 369 USD, plus la machine (≈ 14 à 58 "
         "USD à 0,10–0,40 USD l'heure ; borne haute 187,20). Brouillon 2 : somme de 2 641 ; l'écart vient du plafond de D-1b porté à 578 "
         "et de celui de la phase 2 à 1 950.\n\n"
         "**Prix d'Argon lu sur page archivée** (v5, bloc 6) : 2 / 10 USD par million jusqu'au 30 novembre 2026, 4 / 20 à partir du "
         "1er décembre, au lieu des 10 / 50 supposés : le devis est prudent sur les lignes d'Argon (pilote ordinaire, profil supposé, "
         "309,47 à 4 / 20 au lieu de 337,42 ; plafond minimal pour 40 graines au cas « tout à 4 USD » 553,86 au lieu de 577,66) ; les "
         "chiffres du devis gardent 10 / 50.")
rep("S27 artefacts sans objet",
    "Artefacts de la garde : un fichier Lean et un code Python qui tentent de lire un chemin du dépôt, d'énumérer les variables "
    "d'environnement et d'ouvrir une connexion sortante ; chaque tentative doit échouer et être journalisée (R5), un cas sain "
    "(compilation ordinaire) doit passer.",
    "Artefacts de la garde : voir l'épreuve d'isolement de la puce suivante ; tenter de lire un chemin du dépôt ne prouve rien sur "
    "une machine qui ne le porte pas (VL-05).")
rep("S28 intégrité machine", "Machine éteinte entre les pas (arrêt par identifiant, R10), sauf décision contraire au GO.",
    "Machine détruite à l'échéance de chaque pas par minuterie (A13, R10).\n"
    "- **Intégrité à l'intérieur de la machine (VL-05)** : un utilisateur sans privilège ; **un dossier neuf par item**, détruit "
    "après l'item ; **chaîne Lean et Mathlib en lecture seule** (propriétaire distinct, montage en lecture seule) ; le fichier de "
    "contrôle du harnais (G-L7) est écrit après le code de l'agent, hors de son dossier ; **aucune persistance** d'un item à l'autre "
    "ni d'un bras à l'autre ; limites de processus, de mémoire et de temps par item ; **la clé de la banque et les sorties de l'autre "
    "bras ne sont jamais sur la machine**. **Ordre** : réseau ouvert pour installer la chaîne et Mathlib (D-1a), puis **réseau "
    "sortant coupé et éprouvé avant toute exécution de code écrit par un modèle** ; aucune réouverture ensuite sans nouveau GO. "
    "**Épreuve d'isolement** (qui a un sens sur une machine sans dépôt) : un fichier Lean et un code Python tentent de lire un "
    "fichier leurre posé hors du dossier de l'item, d'écrire dans le fichier de contrôle du harnais, d'écrire dans la chaîne ou "
    "dans Mathlib, de laisser un fichier lu par l'item suivant, d'ouvrir une connexion sortante ; chaque tentative échoue et se "
    "journalise, un cas sain (compilation ordinaire) passe (R5). Ces exigences font partie du périmètre de D-1a.")

# ------------------------------------------------------------------ § 7
rep("S29 D-1a décision", "Recommandation : **(i)**, confiance 0,65. Défaut : aucune\ndépense (nœud).",
    "Règle d'arrêt : minuterie de destruction à 48 heures (A13), plafond tenu même à 1,30 USD l'heure ; **ce premier GO n'engage "
    "que 65 USD**. Recommandation : **(i)**, confiance 0,65. Défaut : aucune dépense (nœud).")
rep_bloc("S30 D-1b décision", "**D-1b — GO du pilote", "scellement. Défaut : aucune dépense.",
         "**D-1b — GO du pilote (seulement après le préenregistrement complet, contre-lu et scellé).** Enjeu : la première mesure ; la "
         "nature de la dépense est à accorder (interface chez quatre fournisseurs). Options : (i) GO, plafond **578 USD** d'appels plus "
         "**35 USD** de machine (avantage : 40 graines garanties même si chaque item formel coûte 4 USD, 52 au profil pire réaliste, les "
         "60 au profil supposé ; inconvénient : 40 graines est l'effectif du pilote réduit écarté en (iii), le choix des classes devient "
         "fragile si A8 joue) ; (ii) GO à **639 USD** plus 35 (avantage : 60 graines au profil pire réaliste ; inconvénient : plus cher, "
         "46 graines seulement au cas « tout à 4 USD ») ; (iii) pilote réduit à 40 graines par construction (écarté : huit items par "
         "classe ne portent pas un choix de classes). Le plafond de 550 du brouillon 2 ne tient pas le cas « tout à 4 USD » (37 "
         "graines : arrêt). Recommandation : **(i)**, confiance 0,5 ; (ii) si Lazar veut un choix de classes robuste même au profil "
         "pire réaliste. À prendre seulement après le scellement. Défaut : aucune dépense.")
rep("S31 D-5 famille",
    "(avantage : contrôle de l'erreur de famille pour les affirmations établies ; inconvénient : coût, sélection sur les données du "
    "pilote)",
    "(avantage : erreur de famille **visée** à 0,025 par affirmation, **établie sur la grille de la nuisance** par les valeurs "
    "critiques calibrées (calcul exact, `calculs-v3/`), sous réserve de la source de la formule (`<<SOURCE_TANGO>>`) ; au gabarit de "
    "Wald du brouillon 2, O3 dépassait, jusqu'à 0,051 par classe ; inconvénient : coût, sélection sur les données du pilote)")

# ------------------------------------------------------------------ § 8 et § 9
section("S32 § 8", "## 8. Points ouverts et à vérifier avant scellement", "## 9.", """## 8. Points ouverts et à vérifier avant scellement

1. **Source de la formule du score apparié** (`<<SOURCE_TANGO>>`) : à lire (Tango, 1998, ou une implantation de référence) ; si
   elle dément la forme close, adopter le repli écrit (§ 3.6) et relancer le calibrage.
2. Prix d'Opus 5.5, de Sonnet 5.5 et de Fable 5.2 sur la page publique ; prix et identifiants de GPT-6 Astra (repli R2 par défaut) ;
   prix d'Argon lu sur une page archivée du 8 novembre (le devis garde 10 / 50, prudent) ; accès effectifs (comptes).
3. Taille de Mathlib, mémoire par processus Lean, hôtes de téléchargement ; commit à épingler (§ 9).
4. Profils de consommation et durées : suppositions ; le profil formel décide de la taille du pilote (A8) ; durée de vie du cache
   contre le délai d'une compilation ; le pilote mesure, le devis 2 remplace.
5. Grille de la nuisance bornée à une discordance de 0,80 et à n de 40 à 150 (§ 3.6) : hors grille, aucune lecture confirmatoire.
6. Le coût des sous-agents de la session est-il une dépense au sens du programme ? (à confirmer par la mère).
7. Carte des hypothèses v1 : hors de `main`, corrections annoncées, D-6 non pour l'instant.
8. Contre-lecteur et vérificateur : tous deux Fable 5.2 (N-052 nomme Fable 5.1) ; la contre-lecture du préenregistrement devra
   relire en entier le § 3.6 (méthode neuve), A8 et le § 4.5 (intégrité), écrits après la contre-lecture 1.
9. Adjudicateur : contrôlé par le tirage de 20 items non litigieux et le certificat mécanique des saines (C13) ; adjudication
   humaine = temps de Lazar ou contact externe.
10. Machine : devis du fournisseur, prix horaire, liaison entre le harnais et la machine ; gardes G-L6 et G-L7, garde d'intégrité
    et épreuve d'isolement à éprouver sur la chaîne installée (D-1a).
11. Pilote à 40–52 graines si le profil formel est cher : le choix des classes est alors fragile (§ 4.3, D-1b).

""")
rep("S33 § 9 méthode",
    "- « À REMPLIR : MÉTHODE-INTERVALLE » — Tango ou Newcombe, choisie par la simulation de C09 sur la grille fixée (effectifs de 40 à 150, "
    "discordances de 0,10 à 0,50, niveau 97,5 %, deux bornes) ; script et sortie.",
    "- « À REMPLIR : SOURCE-TANGO » — lecture de la source de la formule du score apparié (`<<SOURCE_TANGO>>`), ou adoption du repli "
    "écrit au § 3.6 et recalibrage.\n"
    "- « À REMPLIR : MÉTHODE-INTERVALLE » — méthode fixée par la vérification courte et la mère (score apparié à valeurs critiques "
    "calibrées, `calculs-v3/`) ; à remplir : le script d'analyse qui lit `valeurs-critiques-calibrees-v1.json` (ou sa version "
    "recalibrée), avec son empreinte.")

# ------------------------------------------------------------------ restes relevés à la relecture
rep("S34 D-1a calibrage", "simulation de couverture des méthodes d'intervalle (C09) et de l'erreur de famille",
    "calibrage exact des valeurs critiques (§ 3.6 ; fait sur processeur sous `calculs-v3/`, à refaire si la source de la formule "
    "l'exige)")
rep("S35 D-6 somme", "Non compté dans l'engagement.", "Non compté dans la somme des plafonds.")
rep("S36 § 9 repli", "consigne de repli (R1) si GPT-6 Astra manque.",
    "consigne de repli (R1), seulement si Lazar retient R1 avant le scellement (R2 par défaut).")
rep("S37 § 4.2 A8", "35 graines payables sous 450 (sous le minimum de 40), 48 sous 550 (§ 3.8).",
    "35 graines payables sous 450 (sous le minimum de 40), 48 sous 550, 52 sous 578, plafond proposé au brouillon 3 (v5 ; § 3.8).")
rep("S38 § 1.7 sens des bornes", "Par classe k confirmée (B(·) borne basse, H(·) borne haute des intervalles) :",
    "Par classe k confirmée (B(·) borne basse, H(·) borne haute ; pour Δ_k, au sens des tests calibrés du § 3.6 : « B(Δ_k) > 0 » ⇔ "
    "S(0) ≥ z*, « B(Δ_k) ≥ δ » ⇔ S(δ) ≥ z*, « H(Δ_k) < δ » ⇔ S(δ) ≤ −z*, chaque z* à sa valeur calibrée) :")

Path(sys.argv[2]).write_text(T, encoding="utf-8")
print(f"{len(FAIT)} retouches appliquées : " + ", ".join(FAIT))
