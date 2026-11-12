# Contre-lecture R2 — brouillon 1 de l'addendum 2 de P3 (audit des remarques 1 à 3 du verdict) — v1

**Verdict : scellable après corrections.** Aucun constat bloquant. Trois constats majeurs (RB-01 à RB-03) sont à
corriger avant le scellement : une réserve due omise (mention), un cas de lecture non écrit (ampleur non résolue) et une
liste de clés qui ferait arrêter l'unique passage. Les autres sont mineurs ou pour information. Les nombres que le
brouillon tire du verdict sont justes ; B3 se recalcule à l'identique.

## Cadre

- Contre-lecteur : sous-agent neuf (R2). Je n'ai écrit ni ce brouillon, ni le verdict, ni le premier addendum, ni leur code.
- Brouillon relu : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon1.md`,
  sha256 `2698af04fdd1c9c3fafb97e4835bf0e85dbabd145156dbbda06515602d23ab90` (464 lignes) ; notes de rédaction lues.
- Lu : [V] en entier ; [P] en entier ; [PA] en entier ; [N25] ; lignes N-024, R-256 à R-260, N-025, N-026 du registre des
  décisions ; GO-2026-10-20-01 à 03 ; `prereg.py` ; `lecture.py` en entier ; `statistiques.py` l. 1-140 ; `conditions.py`
  en entier ; `propositions.py` l. 95-156 ; `sondes/evaluation.py` en entier ; `run.py` l. 70-85 et 305-350 ; `manifeste.py`
  l. 68-117 ; `harnais/validation_reelle.py` l. 60-80 et 210-250 ; `puissance_p3.py` et `puissance-p3-v1.txt` ;
  `docs/notes/brainstorm-suite-P3-v1/objections/objections-2.md` l. 1-60, et une recherche par mots dans tout ce dossier ;
  une recherche par mots dans les scripts du verdict (bloc-notes `verdict-p3/verdict-v1/`) et dans le module du premier
  addendum (A6, A9).
- **Non lu** : `prereg/P3-consignes-v1.md`, le fichier des textes d'action, toute clé ; aucune donnée du run ([S], [J],
  [T]) ; aucune sortie de lecture ([L], [A]) ; aucune sortie des outils du verdict. Seuls les fichiers compagnons
  `.sha256` des entrées ont été ouverts. Aucun calcul sur les données ; aucune grandeur de B1 ni de B2 calculée.
- Travail en lecture seule. Git en lecture seulement (`rev-parse`, `log`, `show`, `diff --quiet`, `status`). Le
  validateur `prereg.problemes` a tourné hors du dépôt, avec `PYTHONDONTWRITEBYTECODE=1`.

## Vérifications faites (conformes)

- **Empreintes de tête** : [P], [PA], [V], [N25], [N26], [PW] et son script, les six modules gelés cités : égales au
  disque. [D] et [G] au commit `ec1d71b` : `ac9b2cdb…` et `1b762c12…`, égales. Les onze pièces de la table « Entrées » :
  égales à leurs compagnons (dont [T], `ba05fa13…`, compagnon lu ; la note de rédaction disait ne pas l'avoir ouvert).
- **Commits** : `97dd829…`, `e03df08…`, `f7cea56…`, `ec1d71b…` existent sous leur nom complet. Dépôt non superficiel.
  Arbre gelé à la tête actuelle (`6465711`) égal au commit cité `7a54d43` (`git diff --quiet`, code 0).
- **Validateur** : huit sections présentes et non vides ; seuls les marqueurs `<<…>>` restent, comme prévu.
- **Renvois de ligne** : tous ceux de [P], [V], [PA], `lecture.py`, `statistiques.py`, `conditions.py`, `propositions.py`,
  `run.py` que j'ai contrôlés tombent juste.
- **Nombres repris du verdict** : 1,5227 [1,2464 ; 1,8012] ; −0,3176 [−0,5704 ; −0,0650] ; −0,3229 [−0,5404 ; −0,1155] ;
  comptes des formes ; illisibles 140 et 134 ; lisibles 460 et 466 : justes. 10^1,5227 = 33,3.
- **B3 recalculé** (bibliothèque standard) : `z = 2,2414027276049464`, `z80 = 0,8416212335729144`, facteur
  1,3754886. Tromperie : `w` 0,0435, aire au seuil 0,6152, `A_80` 0,63153. Enjeux : `w` 0,04435, aire au seuil 0,57995,
  `A_80` 0,59660 (0,59543 à la distance basse). Hypothèses écrites : `A_80` de 0,55439 à 0,58089 ; aire au seuil de 0,545
  à 0,567. Marges sur 0,58089 : 0,0506 et 0,0157, loin de l'arrondi des entrées (≈ 1·10⁻⁴). Formule juste sous ses
  hypothèses : borne basse = Â − w ; détection si Â > Q + w ; puissance 80 % si A = Q + w (1 + z80 / z).
- **Demi-largeur** : `(haut − bas) / 2` est bien la définition du script de puissance de P3 (`puissance_p3.py`).
- **Calculabilité** : M1 à M9 se font avec `couts_par_tache`, `cout_de_tache`, `effet_cout_apparie` et les colonnes de
  [S] ; les clés de [L] lues pour B3 (`aire`, `bas`, `haut`, `niveau`, `plancher_quantile`, `n_positifs`, `n_negatifs`,
  `degeneres`) existent bien dans la sortie de `detection_etiquettes`. 47 clés de graines : compte juste.
- **Interdits** : aucune moyenne ni médiane sur les jetons ; la médiane de M6 porte sur des tâches. Aucun chiffre de
  l'état de l'art. Aucun bras « moyenne » (N-026 exige le même plancher de même agrégation ; les scores par jeton du
  plancher ne sont pas gardés : raison juste).
- **Remarque 4** : exclue ; le drapeau T2 n'est ni lu ni cité dans ce run.
- **Antériorité de B1 et B2** : les scripts des sceptiques et de l'auteur du verdict ne calculent ni effet par forme ni
  effet sans forme (recherche par mots dans les sources, sorties non ouvertes). Le brainstorm propose une distribution
  « tâche par tâche » (proposition A) sans la calculer.

## Constats, le plus grave d'abord

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| RB-01 | majeur | « Seuil », table des réserves, lignes `reserve_B2_temoin_hors_formes` et `reserve_B2_mention_hors_formes` ; « Critères de lecture gelés » ; plan, point 8 | **Réserve due omise ; asymétrie témoin et mention.** Le texte gelé de P3 traite les deux à l'identique : « témoin ou mention qui gonfle le coût si la borne basse de leur effet est strictement positive » ([P] l. 156, l. 282-283, l. 434-435), réserve de la lecture rattachée à la ligne, pas à une sonde. Le brouillon donne au témoin la cible P3-P1 (lue par la clause de H-P3a) mais à la mention seulement `T3/<p>`, donc « sans objet » dans ce run. Si `E_sf` (mention) a une borne basse > 0, l'addendum ne dirait rien, alors que la même lecture, faite sur le témoin, ajouterait une réserve. Contraire à « même traitement » (audit de symétrie, point 1). | Donner à `reserve_B2_mention_hors_formes` la cible `P3-P1` aussi (comme réserve de la lecture), en plus de `T3/<p>`, avec une phrase de lecture calquée sur celle de la réserve gelée (« la mention gonfle le coût hors des formes »). Ou créer, pour les deux, une cible commune « réserves de la ligne », établie dès que la ligne est écrite. Mettre à jour le compte du plan, point 8 (huit contrôles au plus). La note de rédaction posait la question (question 1) : la réponse prudente est l'égalité. |
| RB-02 | majeur | « Seuil », réserves de B1 ; « Critères de lecture gelés », ligne « aucune réserve sur une conclusion établie » | **Cas de lecture non écrit pour la remarque 1.** Si la borne basse de `E_sf` (saboteur) est dans ]0 ; log10 3] et la borne basse de `D` ≤ 0 (et `M` > 0), aucune réserve ne tombe. Le verdict complété lirait alors « contrôles de l'addendum 2 passés » sur P3-P1. Or l'intervalle décisif [1,2464 ; 1,8012] est entièrement au-dessus de log10 3 : l'ampleur ne serait ni rapportée aux formes ni établie hors des formes. Ce cas arrive dès que la restriction perd de la précision (la règle « au-delà » demande un résultat net : une perte de puissance l'éteint, sens non prudent). La remarque 1 serait close à tort. | Ajouter une réserve mécanique, par exemple `reserve_B1_ampleur_non_resolue`, cible `P3-P1` : borne basse décisive > log10 3, et ni `reserve_B1_ampleur_au_dela_de_la_consigne` ni `reserve_B1_ampleur_portee_par_les_formes` ne tombe. Lecture : « ampleur au-delà de la consigne dans la lecture décisive ; l'addendum 2 ne la rapporte ni aux formes ni au comportement hors des formes : remarque 1 non résolue ». Écrire la table complète des cas (`E_sf` : ≤ 0, dans ]0 ; log10 3], > log10 3 ; `D` : > 0 ou non) avec la lecture de chaque case. |
| RB-03 | majeur | « Métrique », Entrées, liste des clés lues de [L] ; « Liste d'arrêt », garde 9 | **Clé `etablie` prêtée à P3-P2 et à `cout_mention`.** La liste groupe `P3-P1`, `P3-P2`, `cout_mention` et leur prête à tous `calculable` et `etablie`. Dans le code gelé, seule l'entrée P3-P1 reçoit `etablie` (`lecture.py` l. 242) ; P3-P2 et la mention sont des sorties de `effet_ou_non_calculable` sans cette clé (l. 157, 243-245). Lue à la lettre, la garde 9 (« clé absente … arrêt ») arrêterait l'unique passage sur les vraies données. Un second passage exige un nœud de Lazar. De même, la table du verrou reprise de [PA] lit `P3-P4[p]["conforme"]` et `intention[p]["T<k>"]["etabli"]` quand l'amont est établi, mais ces clés ne sont pas dans la liste. | Écrire les clés lues entrée par entrée : `etablie` pour `P3-P1` seulement ; `calculable`, `effet`, `bas`, `haut`, `niveau`, `n_taches`, `taches_exclues`, illisibles et nuls pour les trois. Ajouter `P3-P4` et `intention`, lus seulement si la table du verrou les consulte (comme [PA], précision 18). Ajouter un test : une lecture synthétique produite par le `lecture.lire` gelé passe la garde 9 sans arrêt. |
| RB-04 | mineur | « Hypothèse », B3 ; « Prédiction », paragraphe « B3 n'est pas une prédiction » ; « Limites écrites », point 6 ; « Critères », ligne B3 | **B3 déjà calculé et versé ailleurs, non cité.** L'objecteur 2 du brainstorm a calculé la même grandeur par la même formule : `A_80` ≈ 0,632 (tromperie) et ≈ 0,597 (enjeux) (`docs/notes/brainstorm-suite-P3-v1/objections/objections-2.md`, fait 3) ; la note de décision les reprend (`note-decision-suite-P3-v1.md` l. 51). Le brouillon dit seulement que [V] ne l'a pas recalculée. Le choix de la formule (80 %, comparaison à la même formule aux hypothèses écrites) a donc été fait en connaissant ses valeurs : le texte le dit pour lui-même, pas pour ce précédent. De plus, la phrase de lecture « le nul ne dit rien d'une aire inférieure » est trop forte et sans référent (entre `Q + w` et `A_80`, la puissance va de 50 % à 80 %). | Citer ces deux fichiers avec chemin et empreinte (R6) ; écrire que B3 est une grandeur connue avant le scellement, choisie en connaissant ses valeurs, et le reporter dans la phrase de lecture (« réserve de puissance écrite sur des nombres déjà lus »). Remplacer par « le nul n'exclut pas une aire inférieure à `A_80(p)` ». |
| RB-05 | mineur | « Métrique », M3 et M4 | **Restriction mal définie dans ses comptes.** « Une valeur non finie » : NaN et +inf ne suivent pas le même chemin dans `couts_par_tache` (NaN devient None, +inf reste un nombre), même si les deux finissent illisibles. Les comptes `actions_illisibles_*` rendus par `effet_cout_apparie` incluront les actions retirées ; une action à forme et à coût nul (« 0-5 hours ») cessera d'être comptée parmi les nuls. | Écrire « NaN ». Dire que les illisibles rendus par la fonction gelée comptent les retirées, et rapporter à part : retirées (toutes, lisibles, nulles) et illisibles d'origine, par condition. |
| RB-06 | mineur | « Métrique », M5 ; « Liste d'arrêt », garde 15 ; audit de symétrie, déclencheur 3 | **Part `D / E0` : règles incohérentes.** La garde 15 rend « non lu » un « contrôle dépendant » de la part, mais aucun contrôle n'en dépend (la réserve lit `D`). `E0(b) = 0` exactement n'arrive presque jamais ; le vrai risque est `E0(b)` proche de 0, fréquent pour B2 (intervalle décisif du témoin jusqu'à −0,065) : l'intervalle de la part y est sans valeur. La part ponctuelle n'est pas définie si `E0 = 0` (déclencheur 3). | Écrire que la part est descriptive, qu'aucun contrôle n'en dépend, que l'échec de la part ne touche ni `D` ni ses réserves. Déclencheur 3 : « non calculé » si `E0 = 0`. Pour B2, rapporter la part avec la mention « instable : `E0` proche de 0 », ou ne rapporter que `D`. |
| RB-07 | mineur | « Métrique », M5 ; « Seuil », classement de `D` ; « Seuil », symétrie des repères | **Libellés ambigus pour un effet négatif.** « Actions à forme qui ajoutent à l'effet » si `D > 0` : pour B2 (`E0` < 0), `D > 0` veut dire que les formes rapprochent l'effet de 0, donc en réduisent l'ampleur. « Un `E_sf` (saboteur) compris entre 0 et log10 3 » vise en fait la borne basse. | Libellés signés : « les actions à forme élèvent la différence (D > 0) » / « l'abaissent (D < 0) ». Écrire « dont la borne basse est dans ]0 ; log10 3] ». |
| RB-08 | mineur | « Critères de lecture gelés », ligne `reserve_B1_ampleur_au_dela_de_la_consigne` | **Lecture causale non mesurée.** « Le saboteur ne suit pas la consigne à la lettre » : l'estimation honnête du saboteur n'est pas observée, l'unité n'est pas mesurée (limite 1), et le saboteur peut aussi changer l'échelle de ses propositions. | Écrire : « le coût lu chez le saboteur dépasse, hors des cinq formes mesurées, le facteur écrit dans la consigne (≈ 3) ; la cause n'est pas mesurée (unité, échelle des propositions, gonflement) ». |
| RB-09 | mineur | « Seuil », « un contrôle par test et par cible » ; plan, point 8 | **Unité de contrôle floue.** `hors_formes` et `au_dela_de_la_consigne` lisent le même test (`E_sf`) sur la même cible : « un contrôle par test et par cible » en ferait un seul, alors que le plan compte « quatre de B1 ». | Écrire « un contrôle par règle de réserve et par cible » ; recompter avec RB-01 et RB-02 (neuf au plus). |
| RB-10 | mineur | « Liste d'arrêt », gardes 4 et 5 ; liste des tests | **Définitions et tests incomplets.** Garde 5 : la « commande du module » n'est pas écrite (chaîne exacte versée au manifeste) ; « ou … avec » laisse la portée de la condition sur `config.run_source` ambiguë. Les tests de la garde 4 ne citent pas le cas « commit du manifeste ≠ tête vérifiée ». | Écrire la chaîne exacte de `commande` ; écrire la condition entre parenthèses (« (chemin = ce texte, ou commande = celle du module) et run source égal »). Ajouter ce cas aux tests de la garde 4. |
| RB-11 | information | « Statut » ; « Limites écrites », point 6 | La sortie du premier addendum [A] porte déjà des descriptifs voisins de B1 : A9, « écart type des différences appariées par tâche » et corrélations de `cout_de_tache` entre conditions ; A6, comptes des coûts changés par condition (`complements_p3_v1.py` l. 1456-1457, 1705-1732). Le verdict ne les a pas lus, le rédacteur non plus. L'aveuglement de B1 et B2 tient pour leurs propres grandeurs. | Le dire en une phrase, pour que « aucun agent ne les a calculées » soit exact. |
| RB-12 | information | « Prédiction », paragraphe B3 | Phrase mêlée : « avec la distance basse … à 50 % (aire au seuil), ≈ 0,6152 et ≈ 0,5800 ». À la distance basse, l'aire au seuil des enjeux vaut 0,5791 ; 0,5800 est la valeur à la demi-largeur. Sans effet sur aucune règle. | Écrire les deux valeurs, chacune avec sa définition. |
| RB-13 | information | « Hypothèse », B3 ; « Périmètre » | La remarque 3 du verdict (l. 355-357) parle de l'aire ponctuelle de la sonde de tromperie ; la puissance vient de la section 6, point 2 (l. 296-302). B3 suit le libellé de N-025 (3), plus large que la remarque littérale. Le choix est juste. | Le dire : « B3 répond à N-025 (3), remarque 3 lue avec la section 6, point 2 ; l'aire ponctuelle n'est pas relue ». |

## Réponses aux questions de la commande

- **Grandeurs définies et calculables** : oui, par le code gelé ou un code neuf simple, sauf les précisions de RB-03,
  RB-05 et RB-06.
- **Verrou** : aucune promotion possible, aucune ligne changée, aucune réserve antérieure retirée. Incomplet sur deux
  points : la réserve de la mention (RB-01) et le cas « ampleur non résolue » (RB-02).
- **Règles de réserve mécaniques** : oui, toutes lues sur une borne ou une comparaison fixe. Il manque la table complète
  des cas de B1 (RB-02) et l'unité de contrôle (RB-09).
- **Puissance du nul fixée avant lecture** : la formule est fixée par le texte. Ses entrées sont déjà lues, ses valeurs
  déjà connues et déjà versées au brainstorm (RB-04) : grandeur comptable, non aveugle, ce que le texte doit dire.
- **Gardes et R5** : complets pour l'essentiel (quinze gardes, chacune avec cas sain et artefact). Ajouts : RB-03 (test
  de la garde 9 sur une lecture produite par le code gelé), RB-10 (commit du manifeste).
- **R1** : le texte ne lit rien de nouveau. Il cite seulement des nombres du verdict, et B3 calculé à la main sur ces
  nombres. Le registre devra consigner qu'aucune grandeur de B1 ni de B2 n'a été calculée sur le réel avant S2.
