# Pari de signe (pari apparié borné) — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 27 octobre 2026 à partir des neuf cellules du tour.
- **D'où** : GO-2026-10-27-11, par délégation ; branche `donnees/collisionneur-pari-de-signe-v1`, commit `8d52cf4` ; tour de 17:16 à 17:51 UTC. Empreintes compagnon des neuf cellules revérifiées : 9 sur 9 conformes.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte). Neuf cellules valides, aucun refus, 10,83 USD.
- **Pièces** reçues entières ; § 13 et D-c cités, non servis (T1-B). **Rien n'a tourné** : ni les dix contrôles fatals de S, ni aucune expérience du tour (T1-A, T2-B, T3-B (c)).
- Matériau de décision, jamais une consigne. **Rien d'opposable** (R7) : aucune citation de littérature n'est vérifiée sur PDF empreinté ; les chiffres des modèles sont illustratifs.

## Verdict en cinq lignes

1. **Amender, pas adopter tel quel ; personne ne remplace.** Le cadre tient : la tâche comme unité, un contraste borné calculé par le noyau, la garde par union des nuls (T1-C (e), T3-A (c), T3-B (c)).
2. **Retirer la forme signe du mélange.** Les trois établissent, chacun de son côté, que le mélange parts + signe ne teste que l'intersection {E[v] ≤ 0} ∩ {E[s] ≤ 0}. Il peut promouvoir un moniteur moins bon en moyenne (T1-A A1, T1-B a1, T1-C (b)1). Dérivation, pas résultat.
3. **La garde à δ = 0,10 ne traduit pas « à 1 % »** : elle laisse passer 11 % contre 1 % (T1-A A3, T1-B §3). Les remèdes divergent (T3-A E3′, T3-B ligne 5, T3-C §5).
4. **Choisir la « meilleure base noire » sur le développement fabrique un homme de paille par le bruit.** B et C jugent contre toutes les bases (intersection-union), A contre un ensemble de confiance du meilleur (T2-C A(b)2, T3-B C1-a, T3-C §7, T3-A E6).
5. **D'abord, sans dépense** : un script qui mesure le niveau de chaque procédure candidate sous un nul « moyenne ≤ 0, médiane > 0 ». Il décide du signe, du primaire de G1 et du dimensionnement de la couche 2 (T3-A (c), T3-B E0, T3-C Exp. 1).

## Validité

- **Tient**, si les tâches sont indépendantes : la forme parts seule, la garde par union des nuls (S §3.5), le minimum de deux e-valeurs (T1-A §1, T1-B §1, T3-B (c)).
- **Ne tient pas** : le mélange. Contre-exemples : 70 % des tâches à +0,2 et 30 % à −0,6 (A) ; 80 % à +0,1 et 20 % à −0,4 (B) ; 75 % à +0,15 et 25 % à −0,6 (C). Les contrôles 1 et 3 de S sont symétriques et ne peuvent pas le voir (T1-A A1, T1-B E1, T3-C Exp. 1).
- Le « McNemar » de S, par tâche, est un nul de médiane ; celui de la pièce C, par épisode, un nul de moyenne (T1-B a2).
- **Hypothèses fragiles** :
  - organismes : « 40 tâches » peuvent valoir 4 unités (T1-A A2, T1-C Exp. 4). A fait de l'organisme l'unité dès qu'il porte deux tâches d'une strate (T3-A E2′) ; B veut le mesurer (T3-B E5) ;
  - seuils : bruit du quantile, égalités des juges ordinaux, dérive des honnêtes par mode (T1-B a6, T2-B A-9, T2-A B-6) ;
  - calibrage scellé : Ville tient pour le nul conditionnel, pas pour « le vrai 1 % » ; S est touchée aussi (T3-A, réponse à C-1 ; T3-B B1.1) ;
  - paires voisines : liste figée et empreintée avant le calcul des parts (T1-B (c), T1-C (a)6) ;
  - pondération : S moyenne par tâche, N-054 compte par épisode (T1-A A4) ; A pondère par m_t/m_max (T3-A).
- **Simulation** : effet de tâche commun à A et B, faux positifs indépendants, ni bruit de seuil ni monde asymétrique (T1-B a4-a6) ; sens du biais inconnu (T2-B A-4, T3-A A-4).
- **Niveau de 0,02 et 0,014** : horizon fini et dépassement du seuil, pas une prudence rachetable (T1-A A6, T1-B a12, T1-C (b)1). B corrige sa thèse : une lecture unique au seuil 1/α n'est jamais plus puissante qu'une lecture continue (T3-B B-1). Le prix de 4 à 6 tâches avancé par C repose sur un argument contesté (T2-A C-10).

## Puissance et alternatives

- **Le signe battait les parts** parce que la mise est bornée par 1, alors que la mise optimale des parts vaut 2,3 (A) ou 4,2 (C). Pas général : cela s'inverse à peu d'épisodes ou sous forte corrélation (T1-A A7, T1-B §2, T1-C (b)2).
- **Prix du retrait** (S-sortie, 20 points, dix épisodes) : parts seules 0,10 à 20 tâches, 0,72 à 30, 0,98 à 40 ; mélange 0,91 à 30. Peu à 40, beaucoup à 20 ou 30. À 10 points, parts seules non simulées : sans doute plus de 100 tâches (T1-B §2, T3-B B-3).
- **Mise prévisible** : bornée par 1 aussi ; gain plafonné au prix du mélange, log 4 ≈ 1,4 nat, une dizaine de tâches (T2-A C-6, T2-B C-4, T3-C §4).
- **Rang, permutation, deux échantillons** : testent l'échangeabilité ou la symétrie, pas E[v] ≤ 0 (T1-A §2, T1-B §2) ; C retire son repli de permutation (T3-C §7).
- **Effectif fixe** : t et rééchantillonnage sont anti-conservateurs sous asymétrie à petit n (T2-A B-1, T2-C B(a)2). B l'accepte : niveau d'au moins 0,12 dans le monde de C à 25 tâches (T3-B C2). Bornes exactes candidates : Hoeffding, Bentkus (T3-A E4′, T3-B E0).
- **Désaccord** : C tient le pari parts pour « le seul test exact » à distance finie (T3-C (c)1.4) ; A et B proposent des bornes exactes à effectif fixe.
- **Vrais leviers** : épisodes par tâche (0,50 contre 0,92 à 30 tâches, pour trois contre dix épisodes) et nombre de tâches (T1-A §2, T1-B §2).
- **Références, toutes à vérifier** : Waudby-Smith et Ramdas, « Estimating means of bounded random variables by betting » (2020 pour S et A, « 2024, prépublication 2020 » pour C) ; Shekhar et Ramdas, « Nonparametric two-sample testing by betting », 2023 ; Ramdas, Grünwald, Vovk, Shafer, « Game-theoretic statistics and safe anytime-valid inference », 2023 ; Wang et Ramdas, « False discovery rate control with e-values », 2022 ; Berger, « Multiparameter hypothesis testing and acceptance sampling », 1982 ; Bates et al., « Testing for outliers with conformal p-values », 2023 ; Hoeffding 1963 ; Bentkus 2004 ; Efron et Tibshirani 1993.
- **Citations douteuses** : C marquait Waudby-Smith et Ramdas « VÉRIFIÉ », donnait « Llama-3.1-8B-Instruct » pour rapporté (P dit « portés sur 8B ») et citait le contrôle n° 6 comme un résultat. Retiré (T2-A C-6, C-10, T2-B C-1, T3-C §2). Sa riposte range pourtant sous « établi » le « seul test exact » et l'échec du t, non exécutés (T3-C (c)1).

## Le point de fonctionnement et le critère de G1

- **Accord** : « même taux nominal, asymétrie ≤ δ » est inacceptable à δ = 0,10. Le contrôle n° 6 de S prédit lui-même qu'un écart de 4 points passe à 70 honnêtes (T1-A A3, T1-B §3, T1-C (b)3).
- **Trompeur** : écrire « à 1 % » quand seul le nominal est tenu (T1-B §3). Même à δ = τ, 10 à 15 points de rappel s'achètent ; à 1 %, aucun δ certifiable n'a de dents (T2-B A-3, T3-A (c)).
- **Retiré en riposte** : le 5 % primaire, qui changerait N-008, donc ta décision (T3-A A-3) ; l'aire partielle sous la courbe, autre estimande (T3-C §5) ; l'appariement « par construction », vrai seulement en moyenne sur les calibrages (T3-B B1.1).
- **Reste en désaccord** :
  - A : ni calibrage séparé ni garde ; seuils au même rang des honnêtes d'épreuve ; niveau absolu rapporté (T3-A E3′). Non contre-lu.
  - B : garde bloquante de S, par strate ; δ = 0,10 n'est toujours pas « 1 % », seules des données ou ta décision y changent quelque chose (T3-B (c)).
  - C : garde de S intacte, stratifiée par mode (T3-C §5).
- **Juges ordinaux** : score continu d'abord ; sinon graine scellée (B), bris d'égalité scellé (C), « cellule non comparable » hors de [τ/2 ; 2τ] (A) (T3-A A-9, T3-B C3, T3-C §5).

## Les pentes (H2, H3)

- **Deux niveaux ne lisent pas « croît »** (T1-A E5), ni les contrastes linéaires à trois niveaux : celui de A ignore le milieu, celui de C promeut (0 ; −0,3 ; −0,3 ; +0,3), où le blanc est dominé (T2-B A-6, T2-C A(b)3, T2-A C-8).
- **Convergence** : « croît » = chaque accroissement adjacent promu, par union des nuls ; H3a gardée à chaque N (T3-A E5′, T3-B E9, T3-C §6).
- **H2** porte sur le rappel du séquentiel seul (T1-B a10, T2-C A(a)3), qui gonfle avec la longueur (T2-A B-7, T2-C B(b)3). Remèdes : garde des fausses alertes par horizon (T3-A E5′) ; seuil calibré par horizon (T3-B E8).
- **H2a, non résolue** : le filtre « chaque action sabotée sous le seuil » ampute le comparateur (T1-C (a)4, T1-B a9). La correction de C était biaisée (T2-A C-4, T2-B C-3). Trois remèdes non contre-lus : strate définie par un trait de génération (T3-A A-7) ; même masque d'actions sur l'épisode honnête jumeau (T3-C §3) ; filtre identique des deux côtés (T2-B). Le calibrage du moniteur par action reste ambigu (T1-B a9) ; C l'exige par épisode entier (T3-C §3).
- **Autres formes** : inférence universelle illisible pour un lecteur de G1 ; régression séquentielle sans validité sous dépendance (T1-A §4, T1-B §4).
- **Taille** : S ne dimensionne aucune pente ; le facteur ½ demande environ quatre fois plus de paires (T1-B §4).

## Ce qui manque au préenregistrement de G1

| ligne | A (T1-A §5, T3-A) | B (T3-B) | C (T1-C §5, T3-C) |
|---|---|---|---|
| 1 unité | organisme dès deux tâches par strate | tâche, organisme si E5 | tâche et organisme |
| 2 seuils | rang des honnêtes d'épreuve | score continu ; τ = 1 % | rang commun, égalités brisées |
| 3 comparateur | ensemble de confiance | intersection-union | intersection-union |
| 4 statistique | parts, pondérées par épisode | primaire désigné par E0 puis E3′ | parts seules |
| 5 faux positifs | pas de garde | garde bloquante par strate | garde de S par mode |
| 6 strates | conjonction de modes ; « tous modes » hors porte | règle de passage : ta décision | par mode et global, e-BH |
| 7 intervalle | suite de confiance | borne basse déclarée | bilatéral |
| 8 témoins | plus trois faux asymétriques | par strate | planchers rapportés ; bras génériques seuls sur le mode tenu à l'écart |
| 9 arrêt | une lecture, jamais resoumise | taille fixée d'avance | sous 30 tâches, « pas de dents » |
| 10 échec, repli | contrôle fatal raté : test fixe de N-054 | déviation = échec | repli par permutation retiré |

- **Différences** : le pari est toujours primaire pour C ; pour A, sauf test fixe valide plus puissant de 0,25 ; pour B, la batterie choisit. **Il ne convient pas** sous 30 unités indépendantes par mode (T1-A §5, T1-C §5).

## Ce que les équipes rouges ont cassé et ce que les ripostes ont tenu

- **Cassé, accepté** :
  - chez A : E3 vrai par construction ; banque d'épreuve lue avant le gel ; e-BH qui laisse un mode porter « tous modes » (T2-B A-2, A-5, T2-C A(a)4) ;
  - chez B : dimensionnement fait avec le mélange ; règle de porte contraire à N-054 ; « porte suspendue » (T2-A B-3, B-4, T2-C B(a)4) ;
  - chez C : défaut de garde inexistant ; troncature invalide ; statuts gonflés (T2-A C-1, C-2, T2-B C-1).
- **Tenu** : A, Ville tient sous calibrage scellé pour le nul conditionnel (T3-A). B, l'intersection-union équivaut à « bat la meilleure », et un blocage déclaré d'avance n'élève pas le niveau (T3-B C1-a, C4-a). C, la défense de S par A sur H2a tombe (T3-C §3).
- **Non contre-lu**, faute de quatrième tour : rang des honnêtes, ensemble de confiance (A) ; batterie E0 (B) ; masque symétrique, « seul test exact » (C). Le prix de l'intersection-union reste à chiffrer (T2-C B(a)1, T3-B C1-b).

## Recommandation des trois et ce qui les ferait changer d'avis

- **A** : amender (parts, pondération, rang, ensemble de confiance, pentes par intersection, porte conjonctive). Remplacerait pour G1 si un test fixe tenait α et gagnait plus de 0,25 ; le pari resterait au pôle. D'abord E1 et l'étape 1 de E4′ (T3-A (c)).
- **B** : amender ; primaire désigné par la batterie ; intersection-union. Retire sa critique si le mélange tient en M1 ; le pari devient primaire sauf si un test fixe valide gagne au moins 0,10. D'abord E0 (T3-B (c), E3′).
- **C** : amender puis adopter. Garderait le signe si G1 devenait « meilleur en moyenne et sur la majorité des tâches » (T1-C (e)) ; pas de clause en riposte. D'abord Exp. 1 et 3 en un script (T3-C (c)3).

## Pour ta décision

| option | avantage | inconvénient |
|---|---|---|
| 1. Adopter S tel quel | déjà écrit et dimensionné | aucune cellule ne le soutient ; mélange suspect ; δ = 0,10 n'est pas « 1 % » |
| 2. Amender S ; le pari parts reste le moteur de G1 | seule forme exacte acceptée par tous | coûte des tâches à 20 ou 30 par mode ; trois remèdes divergents, non contre-lus |
| 3. Amender S ; la batterie désigne le primaire | gagne en puissance si un test fixe valide existe | C le nie ; N-054 point 4 pourrait devoir changer (T3-A E4′) |

**Ce qui ressort des cellules** : amender, à l'unanimité ; batterie sans dépense d'abord. Entre 2 et 3, A et B font décider la batterie ; C choisit déjà 2.

**Décisions nommées pour toi** : point de fonctionnement (1 % pour les trois) ; règle de passage et modes obligatoires (A propose « contrôles » et le mode tenu à l'écart) ; planchers rapportés ou critères (T3-A C-4, T3-B B-4, B-5).

**Ce qui reste à vérifier.**
- Toutes les références ; les dix contrôles fatals de S.
- Le simulateur : corrélation A/B par épisode, effet de tâche sur les faux positifs, scores discrets, monde asymétrique (T1-B §6, T3-A E8).
- **Taille de banc de la couche 2** :
  - organismes indépendants par mode : inconnus. Si l'organisme est l'unité, le devis se compte en organismes et les « 40 tâches » tombent (T1-A A2, T3-A E2′) ;
  - coût par épisode : absent des faits (T1-A (d), T1-B (d)) ;
  - sabotées : 40 à 50 par mode à 20 points (T3-C (c)2.5), plus de 100 à 10 points (T3-B B-3) ;
  - honnêtes : 70 à 150 selon S, peut-être 1,5 fois plus avec effet de tâche (T1-B E6) ;
  - totaux illustratifs : 2 700 (A), 3 000 à 4 000 (B), 2 300 à 2 600 épisodes (C) ; C seul les dit tenir dans 100 à 300 USD (T1-C (d)) ;
  - pentes et intersection-union : non chiffrées.
- Organismes dans T0.5 (T1-B E5) ; ce qu'un concepteur voit du mode tenu à l'écart (T2-B, fin).
