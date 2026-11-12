# Ce qui manque au script v2 pour appliquer la règle primaire v3

29 octobre 2026. Le script v2 (`comparaison_jlens_logitlens_sondes_p3_v2.py`, `c02d989f…`) n'est pas modifié.
Cette note dit ce qu'une v3 doit ajouter. Elle ne change pas le calcul des lentilles (`vers_sortie`, `rms`,
`Desembedding`, `tete`, `masque_debut_de_mot`, `jetons_du_concept`), qui reste celui de la v2.

## Bloquants : sans eux, la règle v3 ne s'applique pas

**B1. Sélection des 16 sondes, sans les principales.**
- Le mode `toutes-lineaires` prend aussi les deux principales et leur applique la règle v2. Le mode par défaut ne
  prend que les familles principales.
- Il faut un mode `non-principales-lineaires` : toutes les `SondeLineaireJetons` hors planchers et hors
  `resultat.principales`.
- Refus nommé si le compte n'est pas exactement 16, ou si une principale est dans la sélection. Les principales ne
  doivent être décodées nulle part, même en descriptif.
- `--un-seul-couple` est interdit dans ce mode (ou rend la règle « incomplète » sans verdict).

**B2. Nulle isotrope de 10 000 directions, nouvelle étiquette de graine.**
- `N_ALEATOIRES = 200` est une constante. La v3 a besoin de 10 000 par couche, étiquette `isotropes-v3/c<couche>`,
  entropie 20261029 (`numpy.random.SeedSequence`, comme `graines_aleatoires`).
- Avec 200 tirages, le plus petit p de rang (1/201) est au-dessus de 0,05/32 : la correction est inatteignable.

**B3. Fonction de verdict v3, par comptes entiers.**
- `n_iso = #{nuls isotropes ≥ S}`, `n_pl = #{planchers ≥ S}` (couche 15).
- « cohérent » ⇔ S ≥ 2 et n_iso ≤ 14 et (couche 15 ⇒ n_pl ≤ 2). Aux couches 7 et 23 : isotropes seules.
- Pas de `np.quantile` dans le verdict. Le quantile 0,99 `inverted_cdf` des planchers peut être rapporté, avec le
  libellé « troisième plus grand de 200 ».
- Refus `planchers-insuffisants` si une sonde de la couche 15 n'a pas exactement 200 planchers de son concept.
- Constantes gelées, pas d'options : K = 20, N_iso = 10 000, m = 32, α = 0,05, n_iso max = 14, n_pl max = 2, S min = 2.
- Contrôle interne : m calculé = 16 × 2 = 32, sinon refus `incoherence-interne`.

**B4. Énoncé v3 et empreintes.**
- Constante d'énoncé = le texte de `enonce-regle-primaire-v3.txt`, mot pour mot. Empreinte rendue :
  `be02039011c50c50a4eca0c38c26c7d31c38f6fc7315567659e8fd6cb7b64820`. Un test le vérifie.
- La liste de mots doit avoir l'empreinte `aac34d5c…` (contrôle en dur ou option `--sha256-concepts` exigée ;
  CLJ2-05).

**B5. Verdict d'ensemble et comparaison.**
- Bloc `verdict_ensemble` : pour chaque lentille, X, niveau (« aucune verbalisation détectée » / « minoritaire, au-delà
  du hasard » / « majoritaire »), liste des sondes cohérentes, borne 32 × 15/10 001.
- Bloc `comparaison` : grille par sonde ; b, c ; p du test du signe exact bilatéral (`math.comb`) ; booléen
  « formulation permise ».
- `complete` vrai seulement si les 32 cases existent et si l'ensemble des sondes est exactement la liste des 16.
  Sinon, aucun verdict d'ensemble.

## Utiles, non bloquants

**U1. Coût de calcul.**
- Décodage : 10 000 × 3 couches × 2 lentilles = 60 000 directions × 128 256 × 4 096 ≈ 6 × 10¹³ opérations. Plus
  200 × 2 lentilles × 2 concepts pour les planchers. Ordre de grandeur sur processeur : 10 à 30 minutes. Non mesuré.
- Mémoire : garder les isotropes par blocs de 1 000 (un bloc de 4 096 × 1 000 en double précision fait 33 Mo) et ne
  garder que les indices des 20 jetons de tête (20 × 10 000 entiers par couche et lentille).
- **Les diagnostics z** de la v2 recalculent la nulle sur toutes les isotropes pour chaque sonde, lentille et
  concept (64 fois). Avec 10 000, c'est lourd. Les calculer sur les 200 premières isotropes, ou mettre en cache par
  (couche, lentille). Ils restent descriptifs.

**U2. Descriptif utile à la lecture.**
- S en mots distincts (casse confondue) à côté de S en jetons.
- Verdict au seuil v2 (n ≤ 2 sur 200 premières isotropes), et, à la couche 15, verdict sans planchers : en strates,
  étiquetés « descriptif ».
- Médiane et quantile 0,99 de chaque nulle par concept (déclencheur d'audit de la règle, section 5).
- Strates X par couche, concept, famille.

**U3. CLJ2-01** (lecture de `results.prompts_fitted` imbriqué). Hors règle. Si on fait une v3 du script, autant le
corriger, avec un essai factice à configuration imbriquée.

**U4. CLJ2-02.** Verser le script v3 au dépôt et committer avant l'exécution ; `git status --porcelain` vide.

## Essai factice v3 (à écrire avec le script)

- Planter un signal dans quelques sondes non principales, à chaque couche, sous l'une ou l'autre lentille.
- Vérifier la borne n_iso ≤ 14 aux deux bords (14 donne « cohérent », 15 « non cohérent »), et n_pl ≤ 2.
- Vérifier que les principales n'apparaissent nulle part dans la sortie.
- Vérifier les refus : compte ≠ 16, principale sélectionnée, planchers ≠ 200, liste à empreinte fausse, énoncé
  modifié.
- Vérifier X, les niveaux, b, c et le test du signe sur un cas construit.
- Puis contre-lecture du script v3 par un sous-agent neuf (R2), avant toute exécution réelle.
