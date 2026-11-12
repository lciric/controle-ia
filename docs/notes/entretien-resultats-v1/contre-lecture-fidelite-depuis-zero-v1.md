# Contre-lecture de fidélité — « Le contrôle boîte blanche des menaces diffuses, expliqué depuis zéro », v1

- **Verdict : fidèle après corrections.** 0 erreur bloquante, 4 majeures, 11 mineures.
- Contre-lecteur : sous-agent neuf (R2), Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur (Opus 5.5). Je n'ai écrit aucune des pièces citées ni le document.
- Document lu : `docs/notes/entretien-resultats-v1/explication-programme-depuis-zero-v1.html`, sha256 recalculé `8c190a574094697c82688ee5a30adf11bf3230e47e72deee7ddcca21a9947dcf`, égal à l'empreinte attendue ; commit `5b3286c0`, branche `claude/upbeat-cray-dmauvv`. Document non modifié.
- Date : 10 novembre 2026 (UTC). Non scellé.
- Non lus, par consigne : la branche `donnees/mesure-unanime-v15-sortie-v1` et toute sortie de la mesure ; le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`) ; `diag/*/lecture-sondes-t06.json` ; les lignes R-604 et R-605 de `registres/decisions.md` ; aucune valeur de clé.

Les numéros de ligne du document sont ceux du fichier HTML. « [T] » désigne le texte envoyé, `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt`.

## 1. Résumé par point de la consigne

| Point vérifié | Constat |
|---|---|
| 1. Registre des énoncés (48 lignes) | Les 48 citations de « tel que le jury l'a lu » sont exactes, à la bonne ligne de [T]. Versions actuelles et décisions : exactes, sauf trois nuances (mineures 3, 5, 7). Réfutations : aucune inventée ; « non fixé » est écrit là où rien n'est fixé. États : exacts, sauf la mesure unanime dite « courue » (majeure 2). |
| 2. Théorie | Énoncés formels fidèles à [T] l. 54-100 et à N-003/N-004. Tous les chiffres recalculés sont justes. Illustrations marquées comme telles. « Classique » contre « neuf » suit [T] l. 84-88. Deux erreurs de fond : l'exemple 2 (majeure 3) et le résumé en mots simples du théorème (majeure 1). |
| 3. Résultats « faits » | Chacun renvoie à un verdict scellé de `docs/verdicts/`, à la section 2 du programme d'entretien v18 ou à une ligne du registre ; chiffres exacts. |
| 4. Les 25 contradictions | Toutes réelles, sources exactes, sans exagération. Deux lissages (mineures 5 et 6) ; deux tensions non listées (mineures 7 et 10). |
| 5. Glossaire | Définitions techniques justes (Ville, processus e, toujours valide, copule, marginale, Slepian, détecteur de rupture, sonde, activation, calibrage conforme, aire sous la courbe). Une glose non sourcée (mineure 9). |
| 6. Interdits de contenu | **Aucune violation trouvée.** Aucun résultat de la mesure unanime : seules ses prédictions préenregistrées et ses seuils figurent. Aucun contenu du coffre, aucun nom de mode tenu à l'écart ni de candidat. Aucun chiffre de la course 7a, de l'épreuve v2 de l'étiqueteur, des synthèses du collisionneur ni des fiches de l'organisme d'idéation. Une observation en section 5. |

## 2. Erreurs bloquantes

Aucune.

## 3. Erreurs majeures

### Majeure 1 — Section 4.8, « Le théorème (T) » en mots simples : les classes C et K sont confondues

- **Endroit** : l. 540. « Si le sabotage ne change pas les scores eux-mêmes mais seulement leur ordre ou leurs liens, aucune statistique qui ignore l'ordre ne peut le voir, et, si l'attaquant brasse au hasard, rien ne le peut. »
- **Ce que dit la source** :
  - « leurs liens » est la classe K. Or en classe K, sous dépendance positive, la somme et le processus e passent **au-dessus** de leur taux : [T] l. 81-83 ; `docs/decisions/decision-N-003-N-004-v1.md` l. 32-34.
  - N-003 l. 36 corrige précisément cet énoncé du programme : « vrai en classe C pour les statistiques symétriques, faux en classe K ». Le document le dit lui-même en 3.3 (l. 342, 403, 406). Le résumé de 4.8 réintroduit l'erreur corrigée.
  - « si l'attaquant brasse au hasard, rien ne le peut » omet la condition : la loi honnête doit être échangeable sous le groupe du brassage ([T] l. 77-78, « The group matters » ; N-003 l. 30). L'exemple 4 du document (l. 402) montre un brassage total détecté à 0,9673.
- **Correction** : « Si le sabotage garde les mêmes valeurs et ne change que leur ordre (classe C), aucune statistique qui ignore l'ordre ne peut le voir ; si, de plus, l'attaquant rebrasse dans un groupe sous lequel les scores honnêtes sont déjà échangeables, aucun moniteur de scores ne le peut. Si le sabotage change les liens entre scores sans changer la loi de chacun (classe K), les sommes ne sont plus aveugles : elles montent ou descendent selon le signe de la dépendance, et le maximum reste à son taux ou en dessous. »

### Majeure 2 — La mesure unanime est dite « courue » ; les pièces n'attestent que son lancement

- **Endroits** : l. 427 (« courue une seule fois le même jour à 10:01 ») ; registre 4.2, ligne « L et T sur activations » (état « couru, tenu à l'écart ») ; 4.6, lignes M1, M2 ter et M3, M4 (« Courue une fois », état « couru, tenu à l'écart ») ; l. 671 (« la course a eu lieu ») ; l. 681 (« courue, tenue à l'écart ») ; glossaire l. 788 (« courue le 10 novembre »).
- **Ce que dit la source** : `registres/passations/2026-11-10-1002-lancement-course-mesure-unanime-quarantaine.md` l. 1 (« Lancement de la course unique ») et l. 15-16 (« en arrière-plan, délai de deux heures »), l. 26 (« Processus local : la séquence, en arrière-plan »). Le commit `8b43675a` dit « lancée à 10:01 UTC ». Le document est commité à 10:05:53 UTC. Aucune pièce de la branche ne dit que la course a fini, ni avec quel code de sortie. L'en-tête du document (l. 13) dit d'ailleurs « lancée », correctement.
- **Correction** : partout « lancée le 10 novembre à 10:01, en quarantaine ; fin de course et code de sortie non attestés par les pièces lues » ; état du registre : « lancée, tenue à l'écart ». En 6.3 : « la course est lancée ».

### Majeure 3 — Exemple chiffré 2 : 0,16 n'est pas « la puissance de la somme finale »

- **Endroit** : l. 329. « Saboter tard ne laisse que la puissance de la somme finale. »
- **Ce que dit la source** : 0,1591 est P(E⁺_{n₀} ≥ 1/α) = Φ̄((s* − B)/√n₀), avec s* = 39,1146 : `prereg/T0.3-simulation-lemme-theoreme-v1.md` l. 121 et 129. C'est la valeur terminale du pari, la « borne terminale » de N-003 l. 65-66. La puissance de la somme terminale, au seuil 1,645 × √200 ≈ 23,3, vaut pour le même B = 25 : Φ̄(1,645 − 25/√200) = 0,549 (formule de P1.2, préenr. l. 88 ; mon calcul). L'écart entre 0,549 et 0,159 est justement le « prix de la garantie toujours valide » que N-003 l. 66 dit chiffré.
- **Correction** : « Saboter tard ne laisse que la valeur finale du pari : 0,16. Un test à horizon fixe sur la somme aurait 0,55 pour le même budget (calcul d'illustration, formule de P1.2) ; l'écart est le prix de la garantie valable à tout instant. »

### Majeure 4 — Sections 1.5 et 4.8 : la résistance du maximum et de l'attention est présentée comme acquise

- **Endroits** : l. 62 (« parce que la moyenne et la médiane se laissent évader par apprentissage par renforcement sur les poids, et que le maximum et l'attention résistent ») ; l. 544 (« alors qu'on sait qu'il n'y arrive pas facilement au niveau du jeton »).
- **Ce que dit la source** : la phrase de 1.5 est bien celle du programme v2 (`docs/programme-controle-ia-v2.md` l. 13, 14 septembre). Mais [T] l. 147-149, postérieur et lu par le jury, la nuance : « one study found » ; « its authors note that this may reflect optimisation difficulty, and other work weakens the premise (2412.09565, 2511.00554, 2507.12691, 2609.36490) ». Le document cite lui-même cette réserve en 5.1 (l. 560). « Tr » existe parce que la prémisse est incertaine.
- **Correction** : en 1.5, « parce qu'une étude a trouvé que l'apprentissage par renforcement sur les poids n'évadait pas les sondes agrégées par maximum ou attention ; ses auteurs notent que cela peut tenir à une difficulté d'optimisation, et d'autres travaux affaiblissent la prémisse ([T] l. 147-149) ». En 4.8, « alors qu'une étude publiée ne l'a pas vu réussir au niveau du jeton ».

## 4. Erreurs mineures

1. **Section 1.7, renvoi du pari** (l. 79). Le facteur exp(λz − λ²/2) est cité « préenr. T0.3, l. 232 ». Cette ligne décrit le **détecteur e** (mélange de sommes cumulées avec remise à zéro : log M_n = max(log M_{n−1}, 0) + λz_n − λ²/2), pas un processus e. Les processus e du programme sont des mélanges normaux (préenr. l. 121, 233). L'illustration (λ = 0,5 ; ±0,125 par action ; ≈ 24 actions) est juste et bien marquée. **Correction** : écrire que le pari à λ fixe est une illustration, que le programme utilise un mélange sur λ, et que la l. 232 est la brique du détecteur e.

2. **Figure 2, légende** (l. 398). « trois réarrangements de ce type ». Le préenregistrement en liste **quatre** (l. 136-140 : tri croissant ; suite des 5 plus hautes ; 10 plus hautes en fin ; suite plus appariement adaptatif, N = 1 seulement), soit 7 cellules (l. 142 ; verdict T0.3 l. 114). **Correction** : « quatre réarrangements (sept cellules) ».

3. **Registre 4.2, ligne H8** (l. 471). « Diagnostic mesuré à chaque cycle, plus une bascule » se lit dans les deux sens. La source dit « H8 devient un diagnostic, non une bascule » (`decision-N-062-v1.md` l. 22). **Correction** : « et non plus une bascule ». À ajouter, ici ou en contradiction 6 : la bascule du brief reste une issue possible si Lazar arrête les cycles (N-062 l. 26), et chaque cycle échoué est rapporté (l. 25).

4. **Section 5.6, oracle de couverture** (l. 625). « conçu sur le papier, non construit ». La source citée dit « fixed in principle, not yet designed in detail nor built » (`programme-entretien-taif-v18.md` l. 432-433) et « oracle de couverture non conçu » (l. 113). **Correction** : « décidé dans son principe (N-060 v3), ni conçu en détail ni construit ».

5. **Section 2.4 (porte G1) et contradiction 7** (l. 132, 720). « la règle de décision devient un pari apparié […] (confirmé le 28 octobre) ». N-055 l. 29 retient (c) mais ajoute « reste une pièce du préenregistrement de G1 (nœud de porte) » ; le brouillon 4 de G1 l. 59 porte encore « [À DÉCIDER : D-S11] ». La confirmation du 28 octobre porte sur le nœud 2 de N-056 (intervalle de l'expérience de lecture de N-054 point 4, l. 47-51) et sur D-S29, pas sur D-S11. **Correction** : « retenu par Lazar (N-055), à fixer au préenregistrement de G1, non scellé ».

6. **Contradiction 3** (l. 716). La phrase entre guillemets, « la revue de sécurité extérieure a été réalisée et a donné son go », est attribuée au « mot de Lazar ». C'est le titre de la ligne R-888. Le verbatim est : « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel » (`registres/decisions.md` l. 1117). **Correction** : citer le verbatim, ou ôter les guillemets.

7. **Registre 4.3, ligne HC1, et section 7.2, critère 7** (l. 480, 701). « un article (Panin) à lire avant scellement » ; « un article attendu de Lazar ». Les renvois sont exacts (N-005/N-006 l. 72-73 ; v18 l. 168), mais l'état semble périmé : le PDF est sur disque depuis le 20 octobre (`docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf` ; `provenance-voisin-panin-v1.md` l. 3). De plus [T] l. 181-183 décrit déjà son contenu le 7 octobre, treize jours avant ce dépôt, alors que [T] l. 400 dit les descriptions fondées sur des rapports de vérification à la page. **Correction** : écrire l'état vérifié sur disque, et ajouter cette tension à la partie 8 ; à faire trancher, je ne l'ai pas instruite plus loin.

8. **Section 1.2, invariants du protocole** (l. 48). La liste omet deux invariants de [T] l. 253-254 : le trafic de couverture (« cover traffic », ablaté au papier B) et l'hygiène de l'état persistant. **Correction** : les ajouter.

9. **Glossaire, « Dose-réponse »** (l. 769). « (proportion d'actions sabotées, intensité) » n'a pas de source. Pour l'organisme (ii), la dose est celle de l'adaptateur de bas rang ([T] l. 279 : « LoRA with an adjustable dose ; dose 0 reproduces the base model » ; doses `S25` à `S100`, `decision-N-063-v2.md` l. 14). **Correction** : « la dose de l'adaptateur pour (ii) ».

10. **Section 3.5 et ligne « L et T sur activations »** (l. 427, 468). Le renvoi au brief v2 l. 226-227 est exact, mais la prédiction de cette ligne (« la somme cumulée échoue, l'agrégateur d'autocorrélation récupère le signal ») est la forme d'avant N-003. Depuis, en classe K, la somme monte au-dessus de son taux (N-003 l. 33-36), et M4 est écrite ainsi. **Correction** : le signaler, ou l'ajouter à la partie 8.

11. **Registre 4.1, lignes L2 et T4** (l. 446, 455). L2 : « P2.1 à P2.3 hors de leurs formes closes » ; seule P2.1 est une forme close, P2.2 est « aucune hausse entre m consécutifs », P2.3 « plancher au-dessus du taux » (préenr. l. 103-117). T4 : P7.3 (l. 201) manque à côté de P7.1 et P7.2. **Correction** : « P2.1 (forme close), P2.2, P2.3 » ; « P7.1 à P7.3 ».

## 5. Interdits de contenu : détail

- **Mesure unanime.** Les seuls nombres liés à la mesure sont ceux du préenregistrement v15 scellé : prédiction de M1 (0,073 à 0,077 ; l. 139-142, 184), seuils (0,03 ; 0,02 ; 0,08 ; 0,5 ; B = max(2 L ; 0,10) ; l. 251-262), et les heures de scellement, de dépôt et de lancement. Aucun taux observé, aucune issue, aucun r₀ mesuré.
- **Coffre, mode tenu à l'écart, candidats.** Rien. Seuls les modes publics sont nommés (« coût », « affaiblir les contrôles »).
- **Courses exploratoires.** Aucun chiffre. Les nombres présents viennent tous de pièces scellées : P3 (1,5227 ; 0,6315 ; 0,5966), N-029 (0,8878), verdict R1-R2 (0,523), R-788 (167 sur 180), verdict de l'étiqueteur phase 1 (11 sur 120), T0.5 (0,04 à 0,17), table des dépenses, table de calibration.
- **Observation, sans violation.** La contradiction 4 (l. 717) dit que deux lignes du registre nomment des candidats en clair, et la liste finale (l. 908) donne leurs numéros. Aucun nom n'est reproduit, et la règle du jeu scellée le dit déjà (l. 153). Si le document circule au-delà de Lazar, c'est un pointeur pour un concepteur de moniteurs.

## 6. Ce qui a été trouvé exact

- **Calculs refaits.** Somme terminale à n₀ = 200 : 0,1742 ; 0,4088 ; 0,6831. À n₀ = 1 000, B = 10 : 0,0920. Seuil du maximum : 3,4739. Les 24 valeurs du maximum de la table de la figure 1. Classe K : 0,00226 ; 0,01697 ; 0,10101 ; 0,17034. Borne terminale : 0,1591. Illustrations : 1 − 0,99¹⁰ = 0,096 ; 1 − 0,99¹⁰⁰ = 0,634 ; log 20/0,125 ≈ 24 ; Φ̄(0,938) ≈ 0,174. Figure 2 : somme 5,2 ; moyenne 0,87 ; deux scores au-dessus de 1.
- **Chiffres de la simulation** (verdict T0.3 l. 12-28, 130-137, 152, 235-253) : 31 sur 31 ; 886 cellules (342 et 544) ; 19, 8 et 4 ; 0,01665 à 0,01935 ; 0,2105 ; 0,35145 ; 0,1656 ; 0,0661 ; 0,04605 à 0,05455 pour 0,04995 ; 0,9673 et 0,9674 ; 37 jours.
- **Classique contre revendiqué** : conforme à [T] l. 84-88 et à N-003 l. 43, 51, 75, 77.
- **Table des sources** : les 68 empreintes recalculées sont égales à celles du document ; les 68 mentions « compagnon conforme » ou « sans compagnon » sont exactes.
- **Dates des commits** : `bdf8f287` à 09:41:11 UTC, `0ff3d42d` à 09:44:02 UTC.

## 7. Non vérifié

- Les dates de quatre verdicts (agrégateurs, audit de fuite, échelle de la conscience d'évaluation, A1-v3) : je n'ai lu que leurs en-têtes, qui ne les portent pas toutes.
- La ligne R-2130 : absente du registre de cette branche (le document la dit « non lue ici », ce qui est exact).
- L'identité des sections « Hypothèse » et « Prédiction » entre les versions 14 et 15 du préenregistrement de la mesure unanime.
- Le brouillon 4 de G1, l. 42-50 ; le brouillon 6, hors de cette branche.
- Les chiffres du programme précédent de Lazar ; l'article arXiv 2606.10456 sur son PDF ; la publication de Bailey et collègues. Le document les dit lui-même non vérifiés.
- Le PDF du brouillon (commit `132b4d6b`) : non lu.

## 8. Décompte

- **Énoncés du registre vérifiés sur source primaire : 48 sur 48** pour la citation du jury et sa ligne dans [T] ; 46 sur 48 pour la version actuelle, la réfutation et l'état. Les deux restants (H4′ et H3) n'ont que la mention « inchangé » de N-013 l. 90, vérifiée.
- **Renvois vérifiés sur source primaire : environ 330**, estimation et non décompte ligne à ligne : environ 95 vers [T] ; environ 80 vers les 18 fichiers de décisions ; environ 40 vers le préenregistrement et le verdict de T0.3 ; environ 115 vers les autres préenregistrements, verdicts, la règle du jeu, le programme d'entretien v18, la consigne v19 et son addendum, les 13 passations du 10 novembre, le programme v2, le brief v2 et le registre.
- **25 contradictions sur 25** vérifiées sur leurs deux côtés.
- **68 empreintes sur 68** recalculées.
