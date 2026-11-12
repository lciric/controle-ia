# Les mesures du tour « mesures fortes » — plan de mise en œuvre v1 (sur le « go » de Lazar, 27 octobre 23:47 Paris)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), écrit après le relevé `date -u` de 23:33:48 UTC.
Source : synthèse partielle `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` (`bed9107b…`, sur
`main`), quatre cellules valides (conceptions A, B, C ; critique T2-C). **Rien ici n'est éprouvé** : des plans de mesure,
chacun passant par un préenregistrement scellé et contre-lu **avant toute lecture** (R1, R2), même quand la règle est
levée pour le pôle (R-546 ne couvre pas ces mesures : elles servent H2, H8, G1). Ce que chaque mesure teste, son nul, ses
témoins, ses données, sa dépense, son ordre.

## Verdict

1. **Une mesure se fait cette nuit sans dépense** (mesure 1, unanime) : préenregistrement v2 écrit, contre-lu, à sceller.
2. **Trois se font sans dépense dès que le préenregistrement est écrit**, sur des données existantes (2, 5 en partie, 6
   en partie) ; **trois demandent la banque avec sabotage de la couche 2** (3, 4, 5, 7) : devis chez session-depot, GO.
3. **Deux décisions de T2-C à trancher au préenregistrement de H2** (A(a)1, A(a)3) : la première est traitée dans la
   mesure 1 (M4), la seconde renvoyée à la mesure 3.

## Les mesures, dans l'ordre proposé

| n° | mesure (cellules) | ce qu'elle teste | nul et témoins | données | dépense | état |
|---|---|---|---|---|---|---|
| **1** | **fausses alertes de l'agrégateur séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée** (T1-A ordre 2, T1-B « changer d'avis », T1-C étape 1 ; **unanime**) | le comparateur de H2 doit être calibré par épisode entier ; Ville sous indépendance et le seuil par action ne tiennent pas ; le conforme ne protège que de la dépendance que son calibrage a vue (A(a)3) | épisodes honnêtes ; placebo = 400 sondes aléatoires appariées ; artefacts testés (R5) | sondes figées de P3 sur 60 épisodes honnêtes (`scores-p3.npz`) | 0 | **préenregistrement v2 écrit et contre-lu** (`mesure-unanime-v1/`) ; scellement puis lecture cette nuit |
| **2** | **dissocier par le nul** : « la sonde mesure X » doit battre un prédicteur de surface du texte **et** la sonde aléatoire appariée en covariance (T1-A duel 3, T1-B thèse, T1-C (c)1) | la sonde lit-elle autre chose que le style et le hasard ? (N-029 : prédicteur sur les traits du texte obligatoire) | nul informé = prédicteur de surface ajusté sur le calibrage ; témoin vrai = sonde réelle à effet planté ; faux = sonde aléatoire ; A(a)4 de T2-C : le prédicteur de surface est constant d'une sonde à l'autre → une fiche par sonde, même prédicteur | P3 : saboteur contre honnête (60 + 60), 30 sondes réelles, 400 placebo, traits du texte à calculer sur `textes-actions-p3.jsonl` | 0 | à préenregistrer ; **attention** : P3 a déjà une lecture préenregistrée (candidat 4) — la mesure 2 relit les mêmes issues : elle doit être dite **exploratoire et secondaire**, ou attendre la couche 2 (recommandé : couche 2 pour le décisif, P3 pour le pilote) |
| **3** | **H2, additivité interne** : séquentiel contre maximum **recalibré à l'épisode**, et contre ordre permuté (T1-A duel 1, T1-C E-M2) ; sonde réelle contre aléatoire (T1-B X1) | l'accumulation additive détecte ce que le seuil par action manque, **à fausses alertes par épisode égales** | nul : le maximum calibré par épisode ; témoin propre à H2 : séquentiel sur scores **permutés** entre épisodes (pari v2 § 4) ; A(a)1 de T2-C (« chaque action sous le seuil » rend le maximum nul par construction) : **tranché ici** — la sous-population de H2a se définit par les scores par action au seuil 1 %, et le comparateur est le maximum **recalibré sur cette sous-population** (pas le seuil d'origine) | **couche 2** (épisodes sabotés diffus, horizons variés) ; P3 en pilote (10 actions seulement) | devis couche 2 | à préenregistrer avec H2a réécrite (pari v2 § 4) |
| **4** | **théorème négatif** : garde des fausses alertes sous corrélation injectée par copule, à l'évaluation seulement (T1-A duel 2, T1-C M2) | le délai de détection Θ(γ) sous furtivité par action (programme § 3) sur des scores réels | nul : indépendance ; témoins : copule de corrélation connue (vrai), permutation (faux) ; A(a)3 : injection **à l'évaluation seule** (mesure 1, M4, en est la première version) | P3 honnêtes (mécanisme), couche 2 (sabotage) | 0 puis devis | mesure 1 (M4) d'abord ; préenregistrement propre ensuite |
| **5** | **H8, validité** : instances = sondes (A) ou familles (B) ; concordance pureté / tenue (C M1) | une sonde « valide » (pure : lit le concept) tient-elle mieux sous attaque ? | A(a)2 de T2-C : cent sondes d'un même banc gonflent la richesse → **unité = famille** (B), pas la sonde | sondes de T0.7 (quand entraînées) ; P3 : 30 sondes, 10 par concept × famille : trop peu | devis T0.7 et couche 2 | après T0.7 |
| **6** | **déférence** : témoin de texte neutre de même longueur, plan rhétorique × intention (T1-A duel 4, T1-B X4, T1-C M3) | le moniteur suit-il le style plutôt que l'intention ? (A(a)4 : « le style passe pour l'intention ») | témoins : texte neutre de même longueur et de même place (P3 a déjà le témoin instruit et la condition « mention sans usage » : 60 + 60 épisodes) ; nul : rappel égal | P3 (témoin, mention) ; couche 2 pour le plan complet | 0 (P3) puis devis | à préenregistrer sur P3 comme pilote, en lisant d'abord ce que le candidat 4 a déjà conclu (T3 : mention non séparée de l'honnête) |
| **7** | **conscience d'évaluation** comme problème de mesure (T1-A duel 6, T1-B X3, T1-C § 3) | cadrage évalué contre réel à contenu fixé ; étiquettes permutées ; sonde aléatoire ; **on mesure le cadrage, pas l'intention** | nul : permutation des étiquettes ; témoins : cadrage promu attendu, permuté et aléatoire non promus ; garantie par épisode honnête entier (A, C) | épisodes **à produire** (deux cadrages à contenu fixé) : couche 2 ou pilote dédié (« quelques dollars », contrôles croisés du programme § 7) | devis | après la couche 2 ; HC2b (papier C) la recoupe |
| 8 | **diversité (H5)** : matrice de transfert d'attaque (T1-A duel 5, T1-B X6, T1-C M5) | une attaque optimisée contre A réussit-elle contre B ? | témoins : deux graines d'une même sonde (doivent transférer) | E1.5 (attaques adaptatives, sous GO) et T0.7 | devis E1.5 | phase 1 |
| 9 | **pari d'équivalence** (A, B) et **concordance** (C) comme troisièmes engagements du pôle | « A et B sont équivalents à ε près » ; « pureté et tenue concordent » | B(a)1, B(c)1 de T2-C : deux moniteurs muets sont « équivalents » → **garde d'information** (rappel minimal certifié) obligatoire ; unité = la consigne, jamais l'item (B(a)2) | code (pari apparié v26 : deux paris unilatéraux contre ±ε) | 0 | conception à écrire (pari v10) après la contre-lecture de la v9 |

## Convergences des cellules reprises comme règles (sans dépense)

- **« 1 % » nominal, jamais certifié** sur nos banques → toute fiche qui cite « à 1 % » dit « au seuil scellé calibré sur C
  épisodes honnêtes entiers » (pari v5 § 2.4 bis) ; la mesure 1 en donne la première vérification.
- **Le comparateur de H2 se calibre par épisode entier** → bases conformes (T0.8), le seuil par action ne définit que la
  sous-population de H2a (pari v2 § 4, C4).
- **Les instances ne sont pas indépendantes** → unité d'appariement = consigne ou organisme (D-S1) ; sondes d'un même banc =
  une famille (mesure 5).
- **Robustesse bornée** au catalogue clos et au mode tenu à l'écart (T1-A (a)7, T1-B a9 ; décision nommée pour Lazar : H8,
  HC6) — cohérent avec ce qui a été dit cette nuit sur l'équipe rouge.
- **70 milliards seulement après G1 en 8** (T1-B ordre 5) : décision nommée pour Lazar.

## Ce que ce plan ne dit pas

Les cellules critiquaient le pari en **v1** (la contradiction sur le prix du mélange, T1-B a11, est réglée depuis la v2 :
log 4 seul) ; les deux équipes rouges manquantes et toute riposte ; la conception de C n'a reçu aucune critique. Les
dépenses sont des ordres de grandeur, les devis appartiennent à session-depot.
