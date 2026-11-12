"""Retouches du rédacteur sur le brouillon 2, après application programmatique des 14 couples (jalon 3).
Chaque remplacement : une seule occurrence, blancs normalisés. Les textes insérés par C06 et C08 sont extraits du fichier et
réemployés tels quels (C08 : seul son titre change, documenté). Aucun appel, aucun réseau."""
import re
import sys
from pathlib import Path

P = Path(sys.argv[1])
T = P.read_text(encoding="utf-8")
JOURNAL = []


def motif(ancien):
    return r"\s+".join(re.escape(m) for m in ancien.split())


def rep(nom, ancien, nouveau):
    global T
    trouves = list(re.finditer(motif(ancien), T))
    assert len(trouves) == 1, f"{nom} : {len(trouves)} occurrence(s)"
    d, f = trouves[0].span()
    T = T[:d] + nouveau + T[f:]
    JOURNAL.append(nom)


def extraire(debut, fin):
    m = re.search(motif(debut) + r".*?" + motif(fin), T, re.S)
    assert m, (debut, fin)
    assert len(re.findall(motif(debut), T)) == 1
    return m.group(0)


def section(nom, titre_debut, titre_fin, nouveau):
    global T
    i = T.index("\n" + titre_debut) + 1
    j = T.index("\n" + titre_fin, i) + 1
    T = T[:i] + nouveau + T[j:]
    JOURNAL.append(nom)


# ---------------------------------------------------------------- en-tête
rep("R01 titre", "— dessin et devis — v1, brouillon 1", "— dessin et devis — v1, brouillon 2")
rep("R02 heures", "(début 13:00:30 UTC, heures relevées par `date -u`).",
    "(brouillon 1 commencé à 13:00:30 UTC, brouillon 2 à 13:30:55 UTC ; heures relevées par `date -u`).")
rep("R03 conflit", "un contre-lecteur d'un autre modèle doit vérifier que mon dessin ne favorise pas ce modèle.",
    "la contre-lecture 1 n'a trouvé aucun élément qui favorise ce modèle ; le biais qu'elle relève penchait vers le **bras "
    "formel** (CLP-01, CLP-02), corrigé ici.")
rep("R04 statut",
    "**brouillon 1, non contre-lu, non préenregistré**. Il devient un préenregistrement (R1) après contre-lecture par un "
    "sous-agent neuf (R2 ; un autre modèle de la même famille, comme le veut N-052 pour la boucle extérieure : Fable 5.1) et après le "
    "GO de Lazar.",
    "**brouillon 2, contre-lu une fois, non préenregistré**. La contre-lecture 1 "
    "(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md`, `f565d51c…`, Claude Fable 5.2, « scellable après "
    "corrections », sept bloquants) est appliquée : 14 couples par programme (`calculs-v2/appliquer_couples_cl1_v1.py`), trois "
    "ajouts sans couple (CLP-07, CLP-10, CLP-12), devis refait par script (`calculs-v2/calculs_devis_essai_v4.py`), décisions de la "
    "mère (§ 0). Le contre-lecteur est **Fable 5.2**, non le Fable 5.1 que nommaient N-052 et le brouillon 1 : écart signalé à la "
    "mère. Le texte devient un préenregistrement (R1) quand les pièces marquées « À REMPLIR » (§ 9) existent, après vérification par "
    "un sous-agent neuf, et le GO de D-1b ne se prend qu'ensuite.")
rep("R05 journal", "Journal : `essai-preuve-formelle-devis-v1-journal-v1.md` (même dossier).",
    "Journal : `essai-preuve-formelle-devis-v1-journal-v2.md` (même dossier). Le brouillon 1 (`9ccc9ac0…`) et son journal "
    "(`f8c2b8c6…`) restent intacts.")

# ---------------------------------------------------------------- verdict
section("R06 verdict", "## Verdict", "---\n\n## 0.", """## Verdict

1. **L'essai est faisable sur processeur, en trois pas payés séparément** (scission demandée par la contre-lecture 1, CLP-07).
   **D-1a — outillage** : machine dédiée et isolée, Lean et Mathlib à un commit fixé, gardes éprouvées, simulations ; **aucun appel
   de modèle** ; machine seule, ≈ 48 heures allumées, 4,80 à 19,20 USD à 0,10–0,40 USD l'heure (prix à vérifier), borne haute
   62,40 ; plafond proposé **65 USD**. **D-1b — pilote** (140 items), **seulement après le préenregistrement complet, contre-lu et
   scellé** : attendu **≈ 337 à 347 USD** au profil supposé, **≈ 448 à 457** avec toutes les lignes conditionnelles, **≈ 606 à 726**
   au profil « pire réaliste » de l'agent formel (CLP-09) ; plafond proposé **550 USD** (au profil pire réaliste, la coupure A8 garde
   48 graines sur 60 ; sous 450 elle arrêterait le pilote) et **35 USD** de machine. **Phase 2 — confirmation** (deux classes lues
   à 97,5 %, sans porte) : la règle d'effectif atteint le plafond de 2 × 150 graines dès 15 discordantes sur 60 au pilote ; attendu
   **≈ 1 299 USD** au profil supposé (1 346 avec 60 % d'items litigieux, **1 865** avec les lignes conditionnelles), **≈ 2 451 à
   3 017** au profil pire réaliste ; plafond **indicatif 1 900 USD**, fixé par le devis 2 sur les coûts mesurés au pilote, second GO.
2. **Trois obstacles avant toute dépense** : aucun vérificateur installé (ni Lean, ni Mathlib) ; 2,7 Go libres ; et d'abord la
   **cloison** : les deux outils exécutent du code écrit par un modèle, d'où une machine dédiée **sans clé ni dépôt du programme**
   (§ 4.5, CLP-04). La dépense est faite d'**appels d'interface chez quatre fournisseurs et d'une machine louée**, non de
   sous-agents : Lazar l'accorde en le sachant (CLP-05, D-1b).
3. **L'essai ne rouvre pas la couche 4** : il produit une pièce pour la décision que Lazar prendra après les résultats de l'étape 2
   (N12 (b)). O1 n'établit qu'un gain positif (O1b), sauf si la borne basse dépasse δ (O1a). Ma prédiction (prior, § 1.4) reste que
   la chaîne formelle ne franchit pas le critère conjoint ; avec un écart de fausses alertes de +0,15 ou plus, O1 est presque hors
   d'atteinte : φ_max décide autant que δ.

""")

# ---------------------------------------------------------------- § 0
rep("R07 § 0 ce qui change",
    "le contrôle des graines par une famille hors des bras (§ 2.5) ; l'analyse conditionnelle aux paires formalisables (§ 3.7) ; "
    "le lien au pas (c) (§ 6).",
    "le contrôle des graines par une famille hors des bras (§ 2.5) ; l'analyse conditionnelle aux paires formalisables (§ 3.7) ; "
    "le lien au pas (c) (§ 6).\n"
    "- **Brouillon 2 — ce qui change** (contre-lecture 1 et décisions de la mère, aucune n'engageant de dépense) : O1 scindé en O1a "
    "et O1b, lu avec le rappel conditionnel et l'écart « rappel moins fausses alertes » (C01, C02) ; classes choisies sur cet écart "
    "(C03) ; deux classes lues à 97,5 % sans porte, effectifs et devis refaits par script (C04, `calculs-v2/`) ; environnement isolé "
    "des outils (C05, § 4.5) ; nature de la dépense, scission D-1a / D-1b, repli si GPT-6 Astra manque (C06, § 2.7, § 7) ; coupure "
    "A7 étendue et chiffrée (C07) ; lignes absentes du devis chiffrées (C08, § 4.3) ; méthode d'intervalle fixée avant toute donnée "
    "(C09) ; effectif des saines et lecture de A9 (C10, C11) ; profil « pire réaliste » de l'agent formel et effet sur A8 (C12) ; "
    "contrôle de l'adjudicateur (C13) ; lacunes de justification hors de portée (C14) ; prix précisés (CLP-10) ; gardes du bras "
    "formel complétées (CLP-12) ; motifs de `NON-ACCEPTE` en tête du rapport (CLP-13) ; pièces à remplir nommées (§ 9) ; D-6 non pour "
    "l'instant.")

# ---------------------------------------------------------------- § 1
rep("R08 piège", "pourquoi O2 se lit avec le rappel conditionnel, et pourquoi le",
    "pourquoi O1 et O2 se lisent avec le rappel conditionnel et la différence des écarts « rappel moins fausses alertes » (C01), "
    "pourquoi les classes se choisissent sur cette différence (C03), et pourquoi le")
rep("R09 métriques primaires",
    "dépense totale par bras et rapport des totaux L/S (jetons comptés à chaque appel par le harnais, prix du § 4.1).",
    "dépense totale par bras et rapport des totaux L/S (jetons comptés à chaque appel par le harnais, prix du § 4.1) ; **en tête du "
    "rapport**, avant les issues : décomposition des `NON-ACCEPTE` par motif et part des items au plafond, par bras (CLP-13, C12), "
    "et différence appariée des écarts « rappel moins fausses alertes » par classe (C01, C03).")
rep("R10 delta coût", "Raison : la chaîne formelle coûte environ trois fois la suite par item (§ 4.2)",
    "Raison : la chaîne formelle coûte trois à huit fois la suite par item selon le profil (§ 4.2)")
rep("R11 intervalles",
    "- **Intervalles** : à 95 % bilatéraux pour Δ_k (méthode fixée au préenregistrement, § 3.6) ; séquence fixe sur deux classes (§ 3.6).",
    "- **Intervalles** : à **97,5 %** bilatéraux pour Δ_k de chacune des deux classes (Bonferroni sur deux classes, sans porte, "
    "C04) ; méthode fixée **avant le pilote** par simulation de couverture (C09, § 3.6) ; borne des fausses alertes de "
    "Clopper–Pearson à 97,5 %.")
rep("R12 issues à 97,5 %", "C'est pourquoi O1 distingue O1a et O1b.",
    "C'est pourquoi O1 distingue O1a et O1b. **Au niveau retenu de 97,5 %** (C04 ; `calculs-v2/sortie-calculs-devis-v4.txt`, "
    "bloc 2) : à la frontière, la condition de rappel de O1 sort 0,48 à 0,53 et O1a 0,004 à 0,011 ; pour un Δ vrai de 0,15, la "
    "condition de rappel sort 0,09 à 0,25 ; pour un Δ vrai de 0,30, O1a sort 0,21 à 0,60, selon l'effectif (74 à 150) et la "
    "discordance (0,20 à 0,40).")

# ---------------------------------------------------------------- § 2
rep("R13 A6 confirmation", "(A6). Rapporté aussi sur la confirmation.",
    "(A6). **Même règle sur la banque de confirmation**, avant tout passage aux bras (ajout du brouillon 2 ; ligne de coût comptée, "
    "CLP-06).")
rep("R14 planteur repli",
    "identifiant d'interface « rapporté, à confirmer » (`collisionneur_v8.py` l. 79–80) |",
    "identifiant d'interface « rapporté, à confirmer » (`collisionneur_v8.py` l. 79–80) ; repli écrit ci-dessous |")
rep("R15 contre-lecteur", "| Fable 5.1 (contre-lecture), sous-agent neuf (verdict) |",
    "| contre-lecture 1 faite par Fable 5.2 (N-052 nommait Fable 5.1 : écart signalé à la mère) ; sous-agent neuf (verdict) |")
rep("R16 variantes et repli",
    "Variante de modèle des bras (option de D-3) : Sonnet 5.5 (≈ −36 % sur le pilote) ou Fable 5.2 (≈ +73 %) ; § 4.3.",
    "Variante de modèle des bras (option de D-3), recalculée par fonction (v4) : pilote ordinaire 223,88 avec Sonnet 5.5 et 564,50 "
    "avec Fable 5.2, contre 337,42 avec Opus 5.5 ; § 4.3.\n\n"
    "**Repli si GPT-6 Astra n'a ni identifiant ni accès confirmés au moment de D-1b** (CLP-05) : (R1) planteur = Gemini 4 Argon ; "
    "contrôle des graines par Argon **en contexte neuf** plus le calcul du harnais, audit et adjudication par Argon ; **réserve "
    "écrite** : contrôle, audit et adjudication sont alors de la famille du planteur (risque de confirmer ses propres étiquettes, "
    "mesuré par le tirage de 20 items non litigieux de C13) ; aucune famille des bras n'entre dans la construction ni le contrôle de "
    "la banque ; devis inchangé (mêmes prix supposés, 10 / 50). (R2) reporter D-1b jusqu'à l'accès. Recommandation : (R2) tant que "
    "l'échéance de D-1b n'est pas atteinte, (R1) au-delà ; c'est un nœud de compte, chez Lazar.")

# ---------------------------------------------------------------- § 3
rep("R17 délai L", "au plus 40 tours, 30 minutes murales et **4 USD** par item (§ 3.3).",
    "au plus 40 tours, **30 minutes de temps de processus** et **4 USD** par item, parallélisme fixé au manifeste (3 processus "
    "Lean) (§ 3.3 ; CLP-12 c).")
rep("R18 gardes G-L6 G-L7",
    "sont ce que reçoit le relecteur de fidélité.",
    "sont ce que reçoit le relecteur de fidélité ; G-L6 (CLP-12 a) aucune `notation`, `macro`, `macro_rules`, `syntax`, `elab`, "
    "`infix`, `prefix`, `postfix` dans le fichier de l'agent, et toute définition, abréviation, structure ou instance qu'il "
    "introduit est imprimée en entier (`#print`) et envoyée au relecteur avec les énoncés ; G-L7 (CLP-12 b) `#print axioms` et "
    "`#check` sont lancés par le harnais dans un **fichier à lui** qui importe celui de l'agent, jamais lus dans une sortie que "
    "l'agent contrôle. G-L6 et G-L7 sont à vérifier sur la chaîne installée (D-1a).")
rep("R19 artefacts R5",
    "étape manquante, théorème renommé, `native_decide` dont l'axiome doit apparaître).",
    "étape manquante, théorème renommé, `native_decide` dont l'axiome doit apparaître, notation locale qui redéfinit un symbole, "
    "**étape à hypothèses contradictoires prouvée à vide** (CLP-12 d), lecture d'un fichier hors du bac et appel réseau pendant la "
    "compilation (garde d'isolement, § 4.5)).")
rep("R20 python isolé",
    "outil `python(code)` en bac à sable sans réseau avec sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1 (installés dans `.venv`)",
    "outil `python(code)` exécuté **dans l'environnement isolé** (§ 4.5 : sans clé, sans dépôt, sans réseau) avec les versions de "
    "`.venv` : sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1")
rep("R21 coût apparié délai", "**même plafond par item (4 USD) et même délai mural (30 minutes)** dans les deux bras",
    "**même plafond par item (4 USD) et même délai de processus (30 minutes)**, parallélisme fixé au manifeste (3 processus Lean, "
    "4 de la suite), dans les deux bras")
rep("R22 dimensionnement",
    "(script `calculs_devis_essai_v3.py`, sortie `sortie-calculs-devis-v3.txt`, table des empreintes) : pour une "
    "demi-largeur h = δ/2 = 0,10 de l'intervalle de Δ_k, n_k = ⌈1,96² · d / h²⌉ où d = P(paire discordante) : d = 0,10 → 39 ; "
    "0,15 → 58 ; 0,20 → 77 ; **0,25 → 97** ; 0,30 → 116 ; 0,35 → 135 ; 0,40 → 154 ; 0,50 → 193.",
    "(script `calculs-v2/calculs_devis_essai_v4.py`, sortie `calculs-v2/sortie-calculs-devis-v4.txt` ; la v3 reste sous "
    "`calculs-v1/`) : pour une demi-largeur h = δ/2 = 0,10 de l'intervalle à 97,5 % de Δ_k, n_k = ⌈2,2414² · d / h²⌉ où "
    "d = P(paire discordante) : d = 0,10 → 51 ; 0,15 → 76 ; 0,20 → 101 ; **0,25 → 126** ; 0,30 → 151 ; 0,35 → 176 ; 0,40 → 201 ; "
    "0,50 → 252 (à 95 % : 39 à 193).")
rep("R23 probabilités",
    "- **Probabilités des issues** (20 000 tirages par case, intervalle gabarit de Wald ajusté « +0,5 par case » ; « gain » = "
    "condition de rappel commune à O1 et O2, sans la condition des fausses alertes ; « sous le seuil » = O3 ; « non concluante » = "
    "O4) ; à n = 100 et d = 0,30 : Δ vrai 0 → « gain sous le seuil » 0,957 ; Δ vrai 0,10 → sous le seuil 0,491, non concluante "
    "0,469, gain 0,040 ; **Δ vrai 0,20 → gain 0,534**, sous le seuil 0,034 ; Δ vrai 0,30 → gain 0,991. À n = 150 et d = 0,30 : "
    "0,994 ; 0,643 / 0,343 ; 0,534 ; 0,998.",
    "- **Probabilités des issues à 97,5 %** (v4, bloc 2 ; 40 000 tirages par case, intervalle gabarit de Wald ajusté « +0,5 par "
    "case » ; « gain » = condition de rappel commune à O1 et O2, sans la condition des fausses alertes ; « sous le seuil » = O3 ; "
    "« non concluante » = O4) ; à n = 102 et d = 0,30 : Δ vrai 0 → sous le seuil 0,934 ; Δ vrai 0,10 → sous le seuil 0,385, non "
    "concluante 0,587, gain 0,028 ; **Δ vrai 0,20 → gain 0,490** (O1a 0,009), sous le seuil 0,016 ; Δ vrai 0,30 → gain 0,988 (O1a "
    "0,420). À n = 150 et d = 0,30 : 0,988 ; 0,526 / 0,460 ; 0,529 (O1a 0,009) ; 0,997 (O1a 0,602).\n"
    "- **Erreur de famille** (v4, blocs 2b et 2c ; deux classes indépendantes, sans porte) : pour l'affirmation que O1 établit, "
    "« Δ > 0 », la probabilité d'au moins une borne basse au-dessus de zéro quand Δ vrai = 0 dans les deux classes est de 0,020 à "
    "0,026 ; au moins un O1a quand Δ vrai = δ : 0,008 à 0,024 ; au moins un « sous le seuil » quand Δ vrai = δ : 0,027 à 0,060, "
    "**au-dessus** du niveau visé (0,025) avec ce gabarit, surtout à faible discordance : la simulation de couverture doit vérifier "
    "les **deux** bornes (ci-dessous). La condition « estimation ≥ δ » n'est pas une affirmation : à Δ vrai = 0,15 dans les deux "
    "classes, elle sort au moins une fois avec une probabilité de 0,26 à 0,36, ce que O1b dit en clair (« ampleur non établie »).")
rep("R24 borne FA",
    "- **Borne des fausses alertes** : probabilité que H(φ_L) ≤ 0,30 (Clopper–Pearson 97,5 %) : 120 saines → 0,972 si φ = 0,15, "
    "0,644 si φ = 0,20, 0,175 si φ = 0,25 ; 200 saines → 0,903 si φ = 0,20 ; 300 saines → 0,982 si φ = 0,20.",
    "- **Borne des fausses alertes** (v4, bloc 3) : probabilité que H(φ_L) ≤ 0,30 (Clopper–Pearson 97,5 %) : 80 saines → 0,859 si "
    "φ = 0,15, 0,463 si φ = 0,20 ; 148 saines → 0,789 si φ = 0,20 ; 200 → 0,905 ; 258 → 0,955 ; 300 → 0,983 si φ = 0,20 ; à φ = 0,25 : "
    "0,110 à 0,464 selon l'effectif.")
rep("R25 règle d'effectif", "⌈1,96² · d⁺ / 0,10²⌉)), d⁺ =", "⌈2,2414² · d⁺ / 0,10²⌉)) (C04), d⁺ =")
rep("R26 C10 scénarios",
    "(80 à 300 selon la règle ; 192 à 300 aux effectifs du devis).",
    "(80 à 300 selon la règle ; 150 à 300 aux scénarios du devis v4). Scénarios (v4, bloc 1b) : 6 discordantes sur 60 au pilote → "
    "n_k = 75 ; 9 → 102 ; 12 → 129 ; 15 et plus → 150 (plafond). Le « central 2 × 96 » du brouillon 1 n'était rendu par aucune ligne "
    "de la règle (CLP-15 a) : il est retiré ; le devis de la phase 2 se lit par scénario (§ 4.3).")
rep("R27 variante K1",
    "rend un négatif aussi fort qu'il peut l'être, et un positif exposé à une banque neuve (R3, R4).",
    "rend un négatif aussi fort qu'il peut l'être, et un positif exposé à une banque neuve (R3, R4). **Variante soumise à Lazar** "
    "(D-5 (i bis)) : classe 1 fixée d'avance à K1 « coquille de relation » (ancrée dans les coquilles déjà trouvées par le programme, "
    "position de l'espèce A), classe 2 = la première des quatre autres au rang ci-dessus ; même lecture à 97,5 % sans porte, même "
    "effectif.")
rep("R28 correction", "- **Correction** : séquence fixe ; la classe 1 est lue au seuil plein ; les deux classes sont lues",
    "- **Correction** : les deux classes sont lues")
rep("R29 méthode deux bornes", "McNemar exact rapporté en complément. Le gabarit ci-dessus ne sert qu'au dimensionnement.",
    "McNemar exact rapporté en complément. Le gabarit ci-dessus ne sert qu'au dimensionnement. La simulation vérifie la couverture "
    "des **deux** bornes au niveau 97,5 % (côté O1 et côté O3, bloc 2c) ; la méthode retenue est inscrite au marqueur « À REMPLIR : "
    "MÉTHODE-INTERVALLE » (§ 9) pendant D-1a, avant tout appel de modèle.")
rep("R30 primaire", "issue O1 à O4 selon le § 1.7 ; dépense par bras.",
    "issue O1 (O1a ou O1b) à O4 selon le § 1.7 ; dépense par bras ; en tête, décomposition des `NON-ACCEPTE` par motif et part des "
    "items au plafond, par bras (CLP-13).")
rep("R31 sensibilité adjudicateur", "convention A-T3 pour les acceptations infidèles sur les saines.",
    "convention A-T3 pour les acceptations infidèles sur les saines ; taux de confirmation de l'adjudicateur sur le tirage de 20 "
    "items non litigieux, rapporté à côté de celui des litigieux (C13).")
rep("R32 A1", "- **A1** gardes G-L1 à G-L5, plafonds et compteurs non éprouvés ⇒ aucun lancement.",
    "- **A1** gardes G-L1 à G-L7, garde d'isolement (§ 4.5), plafonds, compteurs, réserve de A7 et refus de A12 non éprouvés sur un "
    "cas sain et sur un artefact ⇒ aucun lancement.")
rep("R33 A6", "- **A6** classifieur de style > 0,70 deux fois de suite ⇒ arrêt.",
    "- **A6** classifieur de style > 0,70 deux fois de suite, sur la banque de découverte ou sur celle de confirmation ⇒ arrêt.")
rep("R34 A7 réserve", "> plafond de la phase ⇒ plus aucun lancement (paires complètes).",
    "> plafond de la phase ⇒ plus aucun lancement (paires complètes). Réserve chiffrée (v4) : 3 items L et 4 items S en vol à 4 USD, "
    "plus le plus cher des appels suivants (4 USD) = **32 USD** ; la coupure se déclenche dès que la dépense dépasse le plafond moins 32.")
rep("R35 A8 effet", "garde l'équilibre des classes.",
    "garde l'équilibre des classes. Effet chiffré (v4, réserve A7 et adjudication comprises) : au profil supposé, le pilote complet "
    "tient sous 450 comme sous 550 (81 et 107 graines payables) ; au profil « pire réaliste » de l'agent L (CLP-09), 35 graines sous "
    "450 (arrêt, sous le minimum de 40), 41 sous 500, **48 sous 550**, 54 sous 600 : d'où le plafond proposé de 550 (§ 4.3).")
rep("R36 A12", "- **A11** toute machine louée s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.",
    "- **A11** toute machine louée s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.\n"
    "- **A12** (D-1a) aucun appel d'interface facturé tant que le GO de D-1b n'est pas inscrit dans `registres/go.md` : le harnais "
    "refuse tout appel sans identifiant de GO valide (garde éprouvée sur un cas sain et sur un artefact).")

# ---------------------------------------------------------------- § 4
rep("R37 § 4 sources",
    "Tous les montants sont en USD, calculés par `calculs_devis_essai_v3.py` (sortie `sortie-calculs-devis-v3.txt`) et "
    "`variantes_modele_bras_v1.py` (sortie `sortie-variantes-modele-bras-v1.txt`), scellés dans le bac à sable du rédacteur (table "
    "des empreintes).",
    "Tous les montants sont en USD, calculés par `calculs-v2/calculs_devis_essai_v4.py` (sortie "
    "`calculs-v2/sortie-calculs-devis-v4.txt`), qui dérive tous les coûts unitaires en un seul lieu (CLP-15 b) ; les scripts du "
    "brouillon 1 restent sous `calculs-v1/` (table des empreintes).")
rep("R38 cache",
    "Cache : le calcul prend une lecture à 0,1 fois le prix d'entrée et une écriture à 1,25 fois (référence locale, ordre de grandeur "
    "général) ;",
    "Cache : le calcul prend une lecture à 0,1 fois le prix d'entrée et une écriture à 1,25 fois ; **le multiplicateur d'écriture "
    "n'est pas sur la ligne d'Opus 5.5** (il se lit sur celle de Fable 5.2 : écriture à 10 pour 8) : **à vérifier** (CLP-10 a) ;")
rep("R39 durée du cache", "Le raisonnement des modèles est facturé comme sortie et compté comme tel.",
    "Le raisonnement des modèles est facturé comme sortie et compté comme tel. Durée de vie du cache (cinq minutes pour l'écriture "
    "citée) contre le délai d'une compilation Lean : à vérifier ; si le cache expire entre deux tours, le profil se rapproche du cas "
    "« sans cache » (item L ≈ 2,64, contre-lecture 1, bloc D).")
rep("R40 lignes unitaires",
    "| audit de fidélité, par item tiré | Gemini 4 Argon | 4 k ; 3 k | 0,19 | 0,46 (6 k ; 8 k) |",
    "| audit de fidélité, par item tiré | Gemini 4 Argon | 4 k ; 3 k | 0,19 | 0,46 (6 k ; 8 k) |\n"
    "| adjudication à l'aveugle, par item soumis | Gemini 4 Argon | 6 k ; 4 k | 0,26 | 0,88 (8 k ; 16 k) |\n"
    "| agent du bras L, profil **pire réaliste** (CLP-09) | Opus 5.5 | 1 000 k ; 100 k ; mêmes parts en cache | 3,04 (item L 3,082 ; "
    "rapport L/S 8,24) | 4,00 (plafond par item) |")
rep("R41 A8 dans § 4.2", "la part des items au plafond, par bras, est une mesure de tête.",
    "la part des items au plafond, par bras, est une mesure de tête. Avec la réserve de A7 et l'adjudication (v4), l'effet du profil "
    "pire réaliste sur A8 est plus fort que dans la contre-lecture : 35 graines payables sous 450 (sous le minimum de 40), 48 sous "
    "550 (§ 3.8).")

c08 = extraire("**Lignes absentes du tableau, comprises dans le plafond**", "les mêmes lignes sont à ajouter au devis 2.")
c08_mod = c08.replace("**Lignes absentes du tableau, comprises dans le plafond**",
                      "**Lignes absentes du tableau du brouillon 1, comprises dans le plafond** (estimation de la contre-lecture, "
                      "reprise telle quelle ; le tableau ci-dessus les chiffre par le script v4)", 1)
assert c08_mod != c08

section("R42 § 4.3", "### 4.3 Devis par phase et par élément", "### 4.4", f"""### 4.3 Devis par pas et par élément

**D-1a — outillage** (aucun appel de modèle ; machine seule) : machine dédiée et isolée (§ 4.5), Lean 4 et Mathlib à un commit
fixé, harnais des deux bras (boucle d'outils, compteurs de jetons par appel, plafonds par item et par phase, réserve de A7, sortie
structurée, gardes G-L1 à G-L7 et garde d'isolement, clé scellée, ordre par paires et par blocs, refus d'appel sans GO de D-1b :
A12), essais R5 des gardes sur cas sains et sur artefacts écrits à la main, simulation de couverture des méthodes d'intervalle
(C09) et de l'erreur de famille, classifieur de style, script d'analyse ; écrit et contre-lu par des sous-agents de la session (coût
d'abonnement, **hors devis d'interface, à confirmer par la mère**). Machine : ≈ 48 heures allumées (SUPPOSÉ) ; **4,80 / 9,60 /
19,20 USD** à 0,10 / 0,20 / 0,40 USD l'heure (prix d'une machine à processeur : **aucune source ici, à vérifier** avant D-2) ;
**borne haute 62,40** au prix horaire des machines à carte graphique du devis de la phase 0 (1,30 USD l'heure,
`brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh` l. 44). **Plafond proposé : 65 USD** (machine seule). Durée : 2 à 3 jours.

**D-1b — pilote** (60 graines, 12 par classe ; 60 saines, 60 fautives, 10 témoins, 10 saines renotées bis : 140 items ; audit sur
50 % ; **seulement après le préenregistrement complet, contre-lu et scellé**) :

| Élément | Attendu, profil supposé | Attendu, profil pire réaliste (CLP-09) |
|---|---|---|
| planteur des graines (72, surgénération de 20 %) | 39,60 | 39,60 |
| planteur des 10 témoins et des 10 renotations bis | 11,00 | 11,00 |
| contrôle des graines | 18,72 | 18,72 |
| bras L | 162,68 | 431,48 |
| bras S | 52,36 | 52,36 |
| lecture nue | 25,20 | 25,20 |
| audit de fidélité (50 %) | 13,30 | 13,30 |
| adjudication à l'aveugle (30 % d'items litigieux, plus 20 non litigieux, C13) | 14,56 | 14,56 |
| **total ordinaire** (entre parenthèses : 60 % d'items litigieux) | **337,42** (346,78) | **606,22** (615,58) |
| conditionnel : audit étendu à tous les items (§ 1.8) | 13,30 | 13,30 |
| conditionnel : banque refaite une fois (A6) | 58,32 | 58,32 |
| conditionnel : graines rejetées jusqu'à 50 % (A5) | 38,88 | 38,88 |
| **total avec toutes les lignes conditionnelles** (60 % d'items litigieux) | **447,92** (457,28) | **716,72** (726,08) |
| pire cas sans plafond (chaque item à son plafond, rejet de 50 % et banque refaite, tous les items audités et adjugés) | 2 048,00 | 2 048,00 |

{c08_mod}

**Plafond proposé de D-1b : 550 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser ; le pire cas théorique sert
seulement à dire que la coupure est nécessaire). Raison : au profil supposé, 550 couvre l'attendu avec toutes les lignes
conditionnelles (448 à 457) et la réserve de A7 (32) ; au profil pire réaliste, A8 garde 48 graines sur 60 (35 seulement sous 450,
ce qui arrêterait le pilote). Plus la machine : ≈ 26 heures allumées, 2,60 / 5,20 / 10,40 USD à 0,10 / 0,20 / 0,40 USD l'heure,
borne haute 33,80 ; **plafond machine proposé : 35 USD**.

**Phase 2 — confirmation** (deux classes lues chacune à 97,5 %, sans porte ; une saine et une fautive par graine ; audit sur 30 % ;
effectifs par la règle du § 3.6 ; banque de confirmation soumise à A6 ; **sur second GO** avec devis 2 refait sur les coûts mesurés
au pilote) ; v4, par scénario de discordance au pilote :

| Discordantes au pilote | n_k | Items | Attendu ordinaire, profil supposé (60 % litigieux) | Avec lignes conditionnelles | Attendu ordinaire, profil pire réaliste | Pire cas sans plafond |
|---|---|---|---|---|---|---|
| 6 sur 60 | 75 | 300 | 652,30 (675,70) | 935,20 | 1 228,30 | 4 355,60 |
| 9 sur 60 | 102 | 408 | 885,53 (917,36) | 1 270,16 | 1 668,89 | 5 917,28 |
| 12 sur 60 | 129 | 516 | 1 118,57 (1 158,82) | 1 605,12 | 2 109,29 | 7 478,96 |
| 15 sur 60 et plus | 150 | 600 | **1 299,40** (1 346,20) | **1 865,20** | **2 451,40** (3 017,20 avec les conditionnelles) | 8 693,60 |

Détail au plafond d'effectif, profil supposé (v4) : planteur 198,00 ; contrôle des graines 93,60 ; bras L 697,20 ; bras S 224,40 ;
audit 34,20 ; adjudication 52,00 ; conditionnelles : audit étendu 79,80, banque refaite (A6) 291,60, graines rejetées jusqu'à 50 %
194,40.

**Plafond indicatif de la phase 2 : 1 900 USD** (profil supposé, plafond d'effectif : attendu avec toutes les lignes
conditionnelles 1 865,20, plus la réserve de A7). Au profil pire réaliste, l'attendu ordinaire (2 451,40) le dépasse : le devis 2
dira quel profil le pilote a mesuré, et le second GO se prendra sur ce chiffre, en sachant aussi si O1 reste atteignable (C11).
Machine : ≈ 62 à 70 heures allumées, 6,20 à 28,00 USD à 0,10–0,40 USD l'heure, borne haute 91,00 ; plafond machine indicatif
91 USD.

**Engagement maximal** (plafonds proposés ou indicatifs) : D-1a 65 + D-1b 550 + 35 (machine) + phase 2 1 900 + 91 (machine) =
**2 641 USD**. Attendu au profil supposé : D-1b 337 à 457 et phase 2 1 299 à 1 865, soit ≈ 1 636 à 2 322 USD, plus la machine
(≈ 14 à 58 USD à 0,10–0,40 USD l'heure ; borne haute 187,20). Brouillon 1 : 1 900 USD ; l'écart vient de C04 (97,5 %), des lignes
de C08, de la réserve de A7 et du plafond de D-1b relevé pour le profil pire réaliste.

**Options chiffrées** (pour les décisions du § 7) : D-5 (i bis), classe 1 fixée à K1 : même coût que (i). D-5 (ii), une seule
classe lue à 95 %, au plus 150 graines, 300 items : attendu ordinaire 652,30 au profil supposé (même nombre d'items que la ligne
« 6 sur 60 »). D-5 (iii), cinq classes avec Holm : non recalculé en v4 (v3, à 95 % : 3 118,50 ; plus cher à 97,5 % et avec Holm).
D-6 : non pour l'instant (décision de la mère), non compté. Modèle des bras (D-3 ; recalculé par fonction en v4, lecture en cache à
0,1 fois pour tous, approximation, CLP-10 c) : pilote ordinaire Opus 5.5 337,42 / Sonnet 5.5 223,88 / Fable 5.2 564,50 ; phase 2
au plafond d'effectif 1 299,40 / 866,80 / 2 164,60.

""")

rep("R43 durées confirmation",
    "- Confirmation : bras L 96 (central) à 150 (plafond) heures de processus, **≈ 32 à 50 heures murales** ; bras S ≈ 5 à 8 heures "
    "murales.",
    "- Confirmation : bras L 129 (12 discordantes sur 60) à 150 heures de processus (plafond d'effectif, 600 items), **≈ 43 à 50 "
    "heures murales** à 3 processus ; bras S ≈ 5 à 8 heures murales ; machine allumée ≈ 62 à 70 heures (v4).")
rep("R44 calendrier", "- Calendrier : phase 0, 2 à 3 jours ; contre-lecture et scellement, 1 jour ;",
    "- Calendrier : D-1a, 2 à 3 jours ; pièces « À REMPLIR », vérification, scellement et GO de D-1b, 1 à 2 jours ;")
rep("R45 nature de la dépense",
    "si l'accès à GPT-6 Astra ou à Argon manque, c'est un nœud de compte.",
    "si l'accès à GPT-6 Astra ou à Argon manque, c'est un nœud de compte (repli : § 2.7). **Nature de la dépense** (CLP-05) : appels "
    "d'interface facturés au jeton chez **quatre fournisseurs** (Anthropic pour les bras, Moonshot pour les relecteurs, OpenAI pour "
    "le planteur, Google pour le contrôle, l'audit et l'adjudication) et une **machine louée** ; ce n'est pas un « devis d'appels de "
    "sous-agents » au sens littéral de R-959 : Lazar l'accorde en le sachant (D-1b).")
rep("R46 isolement exigé",
    "Garde éprouvée sur un cas sain et sur un artefact (lecture d'un fichier hors du bac, appel réseau) avant tout lancement (R5 ; ajoutée à A1).",
    "Garde éprouvée sur un cas sain et sur un artefact (lecture d'un fichier hors du bac, appel réseau) avant tout lancement (R5 ; ajoutée à A1).\n"
    "- **Exigence de la mère (CLP-04)** : la machine dédiée ne porte **ni clé ni dépôt du programme** ; le code écrit par un modèle n'y "
    "voit ni `/home/user/controle-ia-travail` ni aucune variable de clé ; le harnais, qui porte les clés, tourne hors de la machine et "
    "ne lui envoie que le fichier Lean ou le code Python à exécuter ; la liaison entre les deux (accès distant à la machine) est un "
    "point d'environnement à vérifier (D-2). Artefacts de la garde : un fichier Lean et un code Python qui tentent de lire un chemin du "
    "dépôt, d'énumérer les variables d'environnement et d'ouvrir une connexion sortante ; chaque tentative doit échouer et être "
    "journalisée (R5), un cas sain (compilation ordinaire) doit passer.\n"
    "- **Machine (CLP-10 b)** : aucun prix horaire de machine à processeur n'a de source ici (aucun réseau) ; chiffrage par durée "
    "allumée × prix (v4) : D-1a ≈ 48 h, D-1b ≈ 26 h, phase 2 ≈ 62 à 70 h ; 14,40 à 57,60 USD au total à 0,10–0,40 USD l'heure ; borne "
    "haute 187,20 au prix des machines à carte graphique du devis de la phase 0. Machine éteinte entre les pas (arrêt par "
    "identifiant, R10), sauf décision contraire au GO.")

# ---------------------------------------------------------------- § 7
c06 = extraire("Enjeu : seul pas autorisé par N12 (b) ; sans lui, (b) s'arrête au devis.",
               "**D-1b** (pilote, après scellement et contre-lecture).")
section("R47 § 7", "## 7. Décisions à poser à Lazar", "---\n\n## 8.", f"""## 7. Décisions à poser à Lazar

Les recommandations suivent l'accord de la mère sur la contre-lecture 1 (D-3 (a), D-4 (i) sous C01 et C02, D-5 (i) amendée par C03
et C04, D-6 non pour l'instant) ; elles restent des propositions : Lazar décide.

**D-1 — enjeu commun à D-1a et D-1b.** {c06}

**D-1a — GO de l'outillage (machine seule, aucun appel de modèle).** Enjeu : sans outillage, ni le préenregistrement (méthode
d'intervalle, gardes éprouvées, commit de Mathlib) ni le pilote ne peuvent exister ; c'est une dépense de calcul (machine louée),
donc un nœud. Options : (i) GO, machine dédiée et isolée, plafond **65 USD**, échéance à fixer (avantage : lève les trois obstacles
sans aucun appel de modèle ; inconvénient : prix horaire non vérifié, devis de la machine à produire avant location) ; (ii) attendre
(aucune dépense ; le préenregistrement reste incomplet, D-1b impossible). Recommandation : **(i)**, confiance 0,65. Défaut : aucune
dépense (nœud).

**D-1b — GO du pilote (seulement après le préenregistrement complet, contre-lu et scellé).** Enjeu : la première mesure ; la nature
de la dépense est à accorder (interface chez quatre fournisseurs). Options : (i) GO, plafond **550 USD** d'appels plus **35 USD** de
machine (avantage : pilote complet ou presque même au profil pire réaliste, A8 garde 48 graines ; inconvénient : attendu 337 à 457
au profil supposé, la coupure joue au profil pire réaliste) ; (ii) GO à 450 USD (moins cher ; au profil pire réaliste, A8 arrête le
pilote à 35 graines, sous le minimum de 40) ; (iii) pilote réduit à 40 graines (non recalculé en v4 ; écarté par la contre-lecture :
huit items par classe ne portent pas un choix de classes). Recommandation : **(i)**, confiance 0,55, à prendre seulement après le
scellement. Défaut : aucune dépense.

**D-2 — Machine et réseau pour Lean.** Enjeu : d'abord la **cloison** (CLP-04 : les outils exécutent du code écrit par un modèle),
ensuite le disque (2,7 Go libres). Options : (i) machine processeur dédiée, louée sur devis, sans clé ni dépôt du programme, harnais
hors de la machine (avantage : cloison et place ; inconvénient : location, prix à vérifier, accès distant à ouvrir) ; (ii) conteneur
sans accès au dépôt ni aux clés sur une autre infrastructure (acceptable seulement à ces conditions) ; (iii) attendre.
Recommandation : **(i)**, confiance 0,65. Défaut : aucun (nœud d'environnement et de dépense).

**D-3 — Qui formalise ; modèles et familles.** Enjeu : divergence des espèces (C : autre famille ; E : opérateurs) ; détermine ce que
l'écart mesure. Options : (a) **même modèle (Opus 5.5) dans les deux bras, seuls les outils diffèrent** ; relecteurs Kimi K3.1 Pro
dans les deux bras ; planteur GPT-6 Astra (repli R1 ou R2 du § 2.7 s'il manque) ; contrôle, audit et adjudication Gemini 4 Argon
(avantage : l'écart mesure l'outil ; la contre-lecture n'y trouve aucun avantage indu à Opus 5.5 ; inconvénient : pas « le meilleur
formaliseur ») ; (b) formaliseur d'une autre famille que la suite (avantage : proche d'un usage ; inconvénient : modèle et outil
confondus) ; (c) opérateurs humains (avantage : fidélité ; inconvénient : contact externe, dépense, délais). Variantes du modèle des
bras (v4) : Sonnet 5.5, pilote 223,88 (O0 plus probable pour une raison de modèle, non d'outil) ; Fable 5.2, 564,50 (ne se justifie
pas au prix). Recommandation : **(a) avec Opus 5.5**, confiance 0,6. Défaut sous 48 heures : (a).

**D-4 — Seuils.** Enjeu : fixent l'issue ; à geler avant scellement. Options : (i) **δ = 0,20, φ_max = 0,30, sous C01 et C02** (O1
lu O1a ou O1b, lecture conditionnelle obligatoire) ; à savoir : avec la prédiction P1 (écart de fausses alertes d'au moins +0,15), O1
est presque hors d'atteinte, φ_max décide autant que δ ; (ii) δ = 0,15 (plus fin ; effectif multiplié par (0,10 / 0,075)² ≈ 1,8 à
discordance égale, phase 2 plus chère) ; (iii) δ = 0,25 (moins cher ; ne voit que de gros gains). Recommandation : **(i)**, confiance
0,5. Défaut sous 48 heures : (i).

**D-5 — Une ou plusieurs classes.** Enjeu : divergence des espèces (A : une classe préenregistrée ; B, C, E : plusieurs avec
correction) ; détermine l'effectif et le coût de la phase 2. Options : (i) **amendée** : pilote sur les cinq classes ; deux classes
choisies sur la différence des écarts « rappel moins fausses alertes » (C03), quel que soit le signe, lues chacune à 97,5 % sans porte
(C04) ; phase 2 attendue 652,30 à 1 299,40 au profil supposé selon la discordance du pilote (avantage : contrôle de l'erreur de
famille pour les affirmations établies ; inconvénient : coût, sélection sur les données du pilote) ; (i bis) **variante** : classe 1
fixée d'avance à K1 « coquille de relation », classe 2 choisie par le pilote, même coût (avantage : une classe ancrée dans l'usage et
non sélectionnée ; inconvénient : K1 peut être peu favorable à Lean et rendre un négatif moins fort) ; (ii) une seule classe fixée (K1)
lue à 95 % (attendu 652,30 ; aucune sélection ; une seule classe mesurée) ; (iii) cinq classes avec Holm (non recalculé ; v3 à 95 % :
3 118,50). Recommandation : **(i) amendée**, (i bis) exposée comme alternative proche ; confiance 0,55. Défaut sous 48 heures : (i)
amendée.

**D-6 — Banque d'usage (L0 et 21 lemmes de la carte des hypothèses v1).** Décision de la mère : **non pour l'instant** (c'est le
défaut) ; la carte v1 n'est pas sur `main`, attend des corrections et ses lemmes n'ont pas d'étiquette ; à reposer après le pilote,
sur la carte corrigée, si Lazar le souhaite. Non compté dans l'engagement.

""")

# ---------------------------------------------------------------- § 8 et § 9
section("R48 § 8 et § 9", "## 8. Points ouverts et à vérifier avant scellement", "---\n\n## Table des empreintes", """## 8. Points ouverts et à vérifier avant scellement

1. Prix d'Opus 5.5, de Sonnet 5.5 et de Fable 5.2 sur la page publique ; prix et identifiants d'interface de GPT-6 Astra et de
   Gemini 4 Argon ; accès effectifs (comptes) ; repli R1 ou R2 si GPT-6 Astra manque (§ 2.7).
2. Taille de Mathlib et de son cache, mémoire par processus Lean, hôtes de téléchargement ; commit à épingler (§ 9).
3. Profils de consommation (§ 4.2) et durées (§ 4.4) : suppositions, l'écart entre profil supposé et pire réaliste pèse un facteur
   près de deux sur le pilote ; durée de vie du cache contre le délai d'une compilation ; le pilote mesure, le devis 2 remplace.
4. Méthode d'intervalle (Tango ou Newcombe) fixée en D-1a par simulation sur une grille d'avance (C09), en vérifiant les **deux**
   bornes : le gabarit de Wald dépasse le niveau visé côté O3 à faible discordance (v4, bloc 2c). Références des méthodes nommées :
   RAPPORTÉES, à vérifier ; aucun chiffre de l'état de l'art n'est utilisé (R7).
5. Le coût des sous-agents de la session est-il une dépense au sens du programme ? (à confirmer par la mère).
6. Carte des hypothèses v1 : hors de `main`, corrections annoncées, D-6 non pour l'instant.
7. Modèle du contre-lecteur : Fable 5.2 au lieu du Fable 5.1 de N-052 ; la contre-lecture 1 juge suffisante une **vérification
   courte** du brouillon 2 par un sous-agent neuf si les 14 couples sont appliqués tels quels et si les voies de CLP-02 et CLP-03 ne
   changent pas (c'est le cas : couples appliqués par programme, C03 et C04 retenus ; seules retouches de texte inséré, documentées
   au journal : le titre du paragraphe de C08 et le complément de C10) ; à la mère de dire si une seconde contre-lecture entière est
   requise.
8. Adjudicateur : contrôlé par le tirage de 20 items non litigieux et le certificat mécanique des saines (C13) ; une adjudication
   humaine reste la meilleure voie, mais c'est du temps de Lazar ou un contact externe : à lui de dire.
9. Prix horaire et devis de la machine dédiée ; liaison entre le harnais et la machine (accès distant) ; aucune clé ni dépôt sur la
   machine (§ 4.5).
10. Gardes G-L6 et G-L7 : à vérifier sur la chaîne installée ; limite du délai si le parallélisme n'est pas tenu.

## 9. Pièces à remplir avant le scellement (marqueurs « À REMPLIR », refusés par le validateur des préenregistrements)

Chaque marqueur est remplacé par un chemin et une empreinte (R6) avant le scellement du préenregistrement ; aucune de ces pièces
n'exige d'appel de modèle, toutes se produisent en D-1a ou à la table.

- « À REMPLIR : MÉTHODE-INTERVALLE » — Tango ou Newcombe, choisie par la simulation de C09 sur la grille fixée (effectifs de 40 à 150,
  discordances de 0,10 à 0,50, niveau 97,5 %, deux bornes) ; script et sortie.
- « À REMPLIR : VERSION-LEAN » et « À REMPLIR : COMMIT-MATHLIB » — chaîne et commit épinglés à l'installation (D-1a).
- « À REMPLIR : SEUILS-GELÉS » — δ et φ_max gelés par Lazar (D-4).
- « À REMPLIR : CONSIGNE-PLANTEUR » — consigne du planteur, version neuve scellée, avec des exemples génériques de chaque classe qui
  ne viennent d'aucune banque ; consigne de repli (R1) si GPT-6 Astra manque.
- « À REMPLIR : CONSIGNES-BRAS » — tronc commun, instructions d'outil de L et de S, consigne de la lecture nue.
- « À REMPLIR : CONSIGNES-RELECTEURS-CONTRÔLE-AUDIT-ADJUDICATION » — relecteurs Kimi des deux bras, contrôle des graines, audit de
  fidélité, adjudication avec son tirage de 20 items non litigieux.
- « À REMPLIR : HARNAIS-ET-ISOLEMENT » — code du harnais et de l'environnement isolé (commit, empreinte).
- « À REMPLIR : ESSAIS-R5 » — rapport des essais des gardes G-L1 à G-L7, de la garde d'isolement, de A7, A8 et A12, sur cas sains et
  sur artefacts.
- « À REMPLIR : SCRIPT-ANALYSE » — script d'analyse scellé, fiche de passage comprise (choix des classes par C03, règle d'effectif).
- « À REMPLIR : IDENTIFIANTS-MODÈLES » et « À REMPLIR : PRIX-VÉRIFIÉS » — identifiants exacts servis et prix relevés sur les pages
  publiques, avec leur date.
- « À REMPLIR : MACHINE » — fournisseur, caractéristiques, prix horaire, identifiant.
- « À REMPLIR : ÉCHÉANCES » — échéances de D-1b et de la phase 2 (A10).

""")

P.write_text(T, encoding="utf-8")
print(f"{len(JOURNAL)} retouches appliquées :")
for n in JOURNAL:
    print("  " + n)
