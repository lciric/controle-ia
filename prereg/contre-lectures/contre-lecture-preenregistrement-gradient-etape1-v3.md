# Contre-lecture n° 3 (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v3

- Relecteur neuf : sous-agent de contre-lecture R2 n° 3. Il n'a écrit ni le brouillon v1, ni la v2, ni la v3, ni le
  code, ni les sections de conception et de moisson, ni les deux contre-lectures précédentes. Date (UTC, lue par
  `date -u`) : 2026-10-24, de 20:21 à 21:12.
- **Texte relu : `gradient-etape1-sondes-v3.md`, empreinte SHA-256
  `41feda40a5f51858afd8c5167a4b86c3b495ec059929c6ff1f8aa59c8ad1b2d5`** (compagnon vérifié : OK).
- Pièces relues : la v2 (`6ae4a8b3…`), les rapports des contre-lectures n° 1 (`2efeb8db…`) et n° 2 (`c377b2e3…`), le code
  au commit cité `4f02bd8` (arbre des pièces), les sections de « conv-audit » (`180a39af…`), le lanceur
  (`4939c9bebe164ff024b545ecf3b39977993e03f3954f4bd40bd51678b9242039`), les manifestes des traits, la documentation de
  la banque, celle des lignées imposées, les décisions et messages de Lazar, les messages n° 13 à 18 de « conv-audit »,
  l'extrait des registres v4, le validateur et le gabarit du dépôt. Le brouillon v6 de la confrontation (`0ce8c396…`)
  est dans l'arbre des pièces : seules ses bornes et sa table de devis ont été lues, pour vérifier l'alignement annoncé.
- Empreintes citées par la v3, recalculées et **concordantes** : `analyse_gradient.py` `2e59ace6…`, `boucle.py`
  `34897572…`, `analyse.py` `1cef7c0f…`, `entrainement.py` `95497600…`, `moisson.py` `861cbb0d…`, collisionneur
  `213b52ef…`, MISSION `bd2c6a15…`, note du programme `6b415104…`, brouillon v1 `2b6e5dcb…`, sections `180a39af…`,
  empreintes des traits `add13e09…`, manifeste `traits-16384` `034d8460…`, script d'extraction `8286f4e7…`, puissance
  `eaf4ea5d…`, v2 `6ae4a8b3…`, rapports `2efeb8db…` et `c377b2e3…`. Banque `f1387a20…` : seul son compagnon est dans
  les pièces (fichier absent, comme prévu). Tous les compagnons des pièces : OK.

## VERDICT : **scellable après corrections**

Deux **bloquantes**, nées toutes deux de l'ajout de la phase de conception, et qui touchent la lecture de H-G1 :

1. **CE3-01** — la mémoire de la phase de conception (historique et vue d'archive `c001`…`c008` : documents moissonnés,
   notes, traces) n'est servie qu'au bras A ; le bras B relance le même code g000 sans elle. Δ mesure alors
   l'entraînement **et** cette mémoire, et l'écart favorise le signe prédit. **Rejoué.**
2. **CE3-02** — le code d'analyse gelé (`generations_valides`) compte les rondes de conception comme des générations
   notées : quand la lignée de A s'arrête avant celle de B, la paire est lue à une génération que A n'a pas
   (réponses absentes comptées comme erreurs : Δ = −0,5 au lieu de 0,0 dans l'essai) ; une génération invalidée est
   relue ; des paires qui devraient être « coupées » ne le sont plus. **Rejoué.**

Six **majeures** : audit de symétrie déclenché par une simple absence de réponses et sans sortie gelée (CE3-03) ;
recherche de provenance des textes publics du test final par la moisson (CE3-04) ; conditions extérieures
(crédit, quotas, débit, clé Brave) non appariées entre les bras (CE3-05) ; vues d'archive lisibles hors de la lignée et,
dans un dossier des courses ordinaire, lecture du bras A et des traits par le bras B (CE3-06) ; dossiers du noyau
renommables par l'organisme (index du corpus scellé falsifiable, journal absent sans signal) (CE3-07) ; lanceur qui
s'arrête au contrôle des traits (CE3-08).

Décompte : **2 bloquantes, 6 majeures, 7 mineures, 3 de forme.**

Les neuf corrections de la contre-lecture n° 2 sont réelles, dans le texte et dans le code (tableau plus bas) ; les
deux essais demandés prouvent ce qu'ils disent (l'essai d'ordre de ronde échoue sans le tri ; chaque artefact de
`_lire_resultat` échoue pour sa raison). La puissance se rejoue à l'identique. Les options du texte pour A_r sont
exactement celles du lanceur ; l'analyseur du noyau accepte les quatre lignes de commande.

**Condition du scellement.** CE3-01 et CE3-02 (et CE3-03, CE3-07 si elles sont corrigées dans le code) changent le
commit cité : le texte corrigé doit citer le nouveau commit et l'empreinte du lanceur corrigé, et ces corrections de
code doivent être revérifiées par un sous-agent neuf (R2), limité aux corrections, avant le scellement. Le reste est du
texte.

**Validateur du dépôt** (`prereg.py` des pièces, bouchons inoffensifs pour `gardes` et `scellement`) : sur la v3, une
seule plainte — « contre-lecture 3 sans ses deux empreintes (brouillon relu et rapport) » ; sur une copie où l'entrée 3
porte l'empreinte du texte relu et celle d'un rapport, **aucun problème**. Confirmé (E6). Au scellement, inscrire dans
l'entrée 3 : texte relu `41feda40…`, ce rapport (compagnon `.sha256`), puis E et les graines au format de CE3-16.

---

## Corrections

### Bloquantes

**CE3-01 — bloquante — La mémoire de la phase de conception n'est servie qu'au bras A ; le bras B relance le même code
sans elle, et la différence va dans le sens de la prédiction.**

- Fichiers : texte l. 48-52 (H-G1 : « toutes choses égales par ailleurs »), l. 91-101 (« B_r la relance telle quelle
  (mêmes empreintes, sans conception) » ; liste de ce qui reste différent), l. 147-151 (Plan, point 3) ;
  `boucle.executer_generation` l. 457 et 469 (`dossier_archive` = vue de la lignée ; `historique` = toutes les lignes de
  la lignée, rondes de conception comprises) ; `archive.Archive.deposer` l. 117-123 (vue `cNNN` avec le dossier de
  travail de la ronde) ; `boucle.organismes_g000` l. 54-85 et `cli._imposes_et_especes` l. 71-77 (seul l'organisme
  g000 passe de A à B) ; `contrat.CONTRAT` § 5 bis, l. 121-129 (« Les rondes sont archivées (`cNNN`) dans ta vue » ; la
  génération 0 est celle « que le bras témoin relance à l'identique »).
- Défaut : dans A_r, la génération 0 (puis g1, g2) lit sa phase de conception — jusqu'à huit entrées « conception »
  dans `historique`, et `c001`…`c008` dans sa vue, avec les documents moissonnés, notes et résultats écrits pendant
  les rondes ; `rondes_conception_max` vaut 8. Dans B_r (`--depuis`), le même code démarre avec un historique vide,
  une vue vide et `rondes_conception_max` = 0. Un organisme qui garde sa connaissance dans sa vue — le contrat l'y
  invite ; les sections de « conv-audit » le disent (« la génération suivante peut relire ce que la précédente a
  moissonné ») — perd en B ce que A garde. Δ mesure l'entraînement servi **et** l'accès à la mémoire de conception ;
  l'écart avantage A, donc le signe prédit (R3, R4). La liste des différences (CE2-03) ne le nomme pas ; le contrat
  promet à l'organisme une relance « à l'identique ».
- Preuve rejouée (E1, `travail/sortie-e1-memoire-de-conception.txt`) : simulation, isolation d'utilisateur, A avec
  trois rondes de conception, B `--depuis A` sans entraînement, organisme d'essai qui consigne ce qu'il voit. Même
  organisme g000 (`885fd7a3…`) ; A g000 : historique 3 entrées « conception », vue `{c001, c002, c003}`,
  `rondes_conception_max` 3 ; B g000 : historique vide, vue vide, `rondes_conception_max` 0.
- Correction (code, nouveau commit cité) : `--depuis` sans `--gel` importe aussi, pour chaque lignée, la mémoire de
  conception de la course d'origine — lignes d'index `phase = "conception"`, dossiers `archive/<lignée>/cNNN` et
  `archive_vue/<lignée>/cNNN`, marqués comme importés — avant la génération 0, et passe le même
  `rondes_conception_max` ; essai sain (historique et vue de g000 identiques entre A et B, hors `traits` et budget
  d'entraînement) et artefact (sans l'import, l'essai échoue). Texte : écrire dans « Métrique » que B_r reçoit le même
  organisme g000 **et** la même mémoire de conception, seul le service d'entraînement différant. Retirer cette mémoire
  de la vue de A contredirait le contrat § 5 bis et les sections : non recommandé.

**CE3-02 — bloquante — Le code d'analyse gelé compte les rondes de conception comme des générations notées.**

- Fichiers : `analyse_gradient.py` l. 50-53 (`generations_valides` ne filtre pas `phase`), l. 37-47 (`reponses_finales` :
  fichier absent → « aucune réponse », sans signal), l. 68-75 (`paires_h_g1`) ; `archive.deposer` l. 105 (une ronde est
  archivée avec `generation` = k et `phase` = "conception") ; texte l. 102-103 (« dernière génération valide commune »),
  l. 171-176 (Plan, point 6), l. 205 et 242 (règle d'un quart).
- Défaut : `generations_valides(A)` rend les générations notées **et** 1…8. (a) Si la lignée de A s'arrête avant celle
  de B (A : g0, g1 ; B : g0, g1, g2), la génération lue devient 2 (venue de `c002`) ; `g002` n'existe pas dans A ;
  toutes les réponses de A comptent comme des erreurs ; Δ = −score(B). (b) Une génération notée invalidée par le noyau
  (modèle non conforme) est relue dès qu'une ronde de même numéro est valide. (c) Une lignée de A sans génération notée
  valide n'est plus « coupée » : la règle « plus d'une paire sur quatre coupée » ne la voit pas (déduit du même code,
  non rejoué). Repli silencieux (R5) ; biais contre la prédiction en (a).
- Preuve rejouée (E2, `travail/sortie-e2-generations-valides.txt`) : `generations_valides(A2) = [0, 1, 1, 2, 3]` ;
  paire lue à la génération 2 ; `A2/archive/gemini-argon/g002` absent ; 0/8 réponses « avec » ; Δ lu par le code gelé
  **−0,5**, contre **+0,0** sur les seules générations notées (génération 1). E2b : g2 notée marquée invalide sur une
  copie → toujours lue (8/8 réponses de la génération invalidée).
- Correction : `generations_valides` : `and not l.get("phase")` ; `reponses_finales` : erreur si le fichier d'une
  génération dite valide manque ; essai avec phase de conception dans A (sain : génération 1 dans le scénario E2 ;
  artefacts : A plus court que B ; génération notée invalidée) ; nouveau commit cité. Vaut aussi pour les Δ des
  lignées imposées (mêmes fonctions).

### Majeures

**CE3-03 — majeure — L'audit de symétrie se déclenche sur une simple absence de réponses, y compris d'une lignée imposée
hors de H-G1 ; et la table gelée n'a pas de sortie après l'audit.**

- Fichiers : texte l. 202-214 (« la lecture attend le rapport d'audit » ; déclencheurs), l. 173-176 (Plan, point 6 :
  lignées « auto-écrite et imposée ») ; `analyse_gradient.declencheurs_audit_h_g1` l. 145-148 ;
  `analyse.exactitude_equilibree` (sans réponse = erreur) ; `lecture_h_g1` l. 115-116.
- Défaut : (1) une lignée qui ne répond à rien sur une famille obtient 0,0, sous le seuil de 0,30 qui vise des
  étiquettes inversées : l'audit part. Les deux lignées imposées, hors de H-G1, écrites avant le contrat v3 et
  réécrites huit fois sans score pendant la conception (CE3-10), ou une panne de fournisseur (CE3-05), peuvent ainsi
  suspendre la lecture de H-G1. (2) Rien ne dit ce qui suit l'audit : `lecture_h_g1` rend « audit … avant toute
  lecture » et s'arrête ; le sous-agent neuf du verdict (R13) n'a pas de critère gelé pour conclure.
- Preuve (E14, `travail/sortie-e14-audit-sans-reponse.txt`) : une lignée imposée sans réponse → deux faits
  (`… = 0.000`) → « audit de symétrie (R4) avant toute lecture » ; la même lecture sans ce fait rendrait « confirmé ».
- Correction : (a) seuil bas calculé sur les tâches répondues, avec une couverture minimale (≥ 80 % par famille, comme
  H-G0) ; sous la couverture, la lignée est « sans réponse », rapportée, et sa paire coupée (comptée dans la règle d'un
  quart) — pas un déclencheur ; (b) pour les lignées imposées, seul le seuil haut (> 0,95, signe possible d'une fuite du
  noyau, qui toucherait toutes les lignées) déclenche l'audit ; (c) sortie gelée : rapport d'audit scellé ; aucun défaut
  → table relue sans sa première ligne, verdict assorti d'une réserve (R4) ; défaut trouvé → paires touchées coupées
  (règle d'un quart) ou, défaut du noyau, « non concluant : défaut trouvé par l'audit ».

**CE3-04 — majeure — La moisson ouvre le test final à une recherche de provenance : la famille « conscience
d'évaluation » vient d'un jeu public, et rien ne le garde, ne le mesure ni ne le lit.**

- Fichiers : texte l. 189-196 (Plan, point 9), l. 211-214 (l'audit cherche « une fuite (vérités lisibles, vue de
  l'archive), des étiquettes inversées, un indice de surface ») ; `banque/PROVENANCE-eval-awareness-v1.md` (jeu public
  `jjpn2/eval_awareness` du papier arXiv 2505.23836, items de bancs d'essai et de transcriptions d'usage réel) ;
  `contrat.CONTRAT` § 2-3 (les textes de test sont dans le contexte ; `rechercher` accepte une requête libre de
  300 caractères, `recherche.REQUETE_MAX`, source `web` comprise) ; message n° 14 § 2 (« PDF 2505.23836 téléchargé et
  extrait »).
- Défaut : en génération notée, un organisme peut envoyer un extrait d'une tâche de test à la recherche web, retrouver
  la page d'origine (banc d'essai public, transcription publiée) et en déduire l'étiquette des 36 tâches de cette
  famille au test final, sans lire aucune vérité de la banque. Les deux bras ont la même moisson : ce n'est pas d'abord
  un biais de Δ, mais cela change ce que H-G1 mesure (la sonde contre la recherche), peut saturer la famille (Δ écrasé)
  et déclencher le seuil haut de l'audit sans que la fuite soit de celles que l'audit cherche. Non mesurable ici
  (aucun réseau).
- Correction : (a) garde du noyau, borne de sécurité et non stratégie : une recherche dont la requête partage un passage
  long (par exemple ≥ 8 mots consécutifs ou ≥ 50 caractères) avec une tâche de test ou de test final est refusée
  (`REFUSE`, journalisée) ; essai sain (passage d'une tâche d'entraînement : servi) et artefact (passage d'une tâche
  de test : refusé) ; ou, si Lazar juge cette borne contraire à « ne lui suggère rien », (b) mesure gelée : requêtes
  qui recoupent un texte de test comptées par lignée, bras et génération (le journal des recherches garde la requête
  en clair), H-G1 rapportée aussi par famille, ces requêtes ajoutées aux déclencheurs de l'audit. Recommandation :
  (a), avec l'accord de Lazar si la borne lui semble toucher à sa décision.

**CE3-05 — majeure — Les conditions extérieures qui dépendent de l'heure ne sont pas appariées entre les bras ; aucune
règle pour une panne en cours de course.**

- Fichiers : texte l. 150-152 (« tout le reste identique (moisson … compris) » ; « A_1 et A_2 tournent ensemble ; B_1 et
  B_2 ensuite »), l. 154-156 (`BRAVE_API_KEY` « si elle est dans l'environnement de la session »), l. 194-196 (débit
  d'OpenAlex), l. 237 (appel de contrôle avant la course seulement) ; lanceur l. 117 et 125 (présence de la clé Brave
  ni exigée identique, ni consignée) ; `recherche.Rechercheur.rechercher` l. 155-168 (un échec consomme une recherche) ;
  `boucle.py` l. 219 (le manifeste écrit `"recherche": "arxiv"` et ne consigne pas les sources servies) ; un
  `ECHEC_API` est un statut rendu, rien n'invalide la génération ; message n° 15 § 2 (clé Brave « avec une limite
  d'usage ») ; message n° 18 § 5 (crédit Gemini épuisé, HTTP 402, le jour même) ; brouillon v6 (≈ 4 400 requêtes web
  pour la confrontation seule).
- Défaut : A_r et B_r tournent à des heures différentes, B_r seulement après la fin de A_r (huit rondes de conception
  plus trois générations). Le crédit d'un fournisseur, le quota Brave (au pire ≈ 1 650 requêtes web par course A et
  450 par course B, ≈ 4 290 pour l'étape avec la répétition), le débit des interfaces ouvertes et la présence de la clé
  Brave au lancement peuvent différer entre les deux bras d'une paire. Une panne en cours de course ne laisse que des
  statuts d'échec, que la table gelée lit comme un effet, dans un sens ou dans l'autre, tant que |Δ| ≤ 0,40.
- Correction : (1) lanceur : même présence ou absence de `BRAVE_API_KEY` pour A_r et B_r (refus de B sinon), consignée
  dans `lancements.txt` ; manifeste : sources servies ; (2) règle gelée : à la génération lue, taux d'appels en
  `ECHEC_API` et de recherches en `ECHEC_RECHERCHE` par source et par bras, tirés des journaux ; une paire dont les deux
  bras diffèrent de plus d'un écart fixé maintenant (par exemple 10 points) est coupée (« panne extérieure ») ; un HTTP
  402 en cours de course arrête la course (liste d'arrêt) ; (3) le dire dans la liste des différences de « Métrique » ;
  (4) à considérer : lancer B_r dès que les g000 de A_r existent, pour réduire l'écart d'heure.

**CE3-06 — majeure — « Vues de la seule lignée » n'est pas tenu par les permissions ; dans un dossier des courses
ordinaire, le bras B lit les vues du bras A, les traits d'activation et les sorties.**

- Fichiers : texte l. 157-159, 189-193 (« vues de la seule lignée » ; corpus « visibles de la lignée seule ») ;
  `archive.Archive.__init__` l. 66-70 et `boucle._vue_pour` l. 294-296 (vue et vue de chaque lignée en 0755 : listables
  et lisibles par tout utilisateur) ; `bac_a_sable.espace_organismes` l. 106-123 (l'espace des organismes est la racine
  de la course quand elle est traversable) ; `bac_a_sable.uid_lignee` l. 85-86 (même utilisateur pour la même lignée
  dans A_1 et A_2, qui tournent ensemble) ; lanceur l. 16, 28, 44-53, 126 (dossier des courses créé par `mkdir -p`
  sans mode ; `entrees/traits/` et `<course>.sortie.json` lisibles). `/home/user` et `/var/tmp` sont traversables dans
  ce conteneur (modes lus).
- Défaut : (a) dans toute course, l'organisme d'une lignée liste `archive_vue/` et peut lire les vues des autres
  lignées (rondes, corpus, code) : les paires d'une réplique ne sont pas étanches, alors que le bootstrap les tire comme
  indépendantes ; (b) si le dossier des courses et ses ancêtres sont traversables, l'organisme de B_r liste ce dossier
  et peut lire la vue de sa lignée dans A_r (rondes de conception et générations à gradient), les traits d'activation des
  200 tâches sous `entrees/traits/` — avec les 80 vérités d'entraînement de son contexte, il peut apprendre lui-même une
  sonde en numpy : le bras « sans gradient » ne l'est plus — et `A_r.sortie.json` (scores) ; dans A_1 et A_2, la même
  lignée a le même utilisateur et peut écrire dans le dossier de travail (0700) de sa jumelle. Ni le texte ni le
  lanceur ne fixent l'emplacement. Une consigne glissée dans une page moissonnée peut aussi y pousser l'organisme : les
  sections disent à tort qu'elle « ne peut rien faire d'autre que tromper l'organisme ».
- Preuve (E3, `travail/sortie-e3-lectures-hors-de-la-lignee.txt`) : dossier des courses traversable (`/srv` en 0755,
  dans un espace de noms de montage privé) : B/gemini-argon/g000 liste `/srv` = {A, A.sortie.json, B, B.sortie.json,
  entrees}, liste la vue de sa lignée dans A {c001, g000, g001} (dossiers 0755, fichiers 0444 : lisibles), lit
  `entrees/traits/traits-x.npz` (4 096 octets) et `A.sortie.json` (505 octets) ; dans les deux dispositions,
  gemini-argon liste la vue de claude-opus-5-5 de la même course. Correction rejouée : dossier
  des courses en 0700 → espace sous `/var/tmp/essaim-m3/<empreinte>` ; listes et lectures hors de la course :
  `PermissionError`.
- Correction : (1) lanceur : `chmod 0700` du dossier des courses (et `entrees/`, sorties `*.sortie.json` en 0600), refus
  si une racine de course est traversable ; (2) code (recommandé) : vue de chaque lignée lisible de sa seule lignée
  (groupe propre à la lignée, 0750 ; `archive_vue/` en 0711) ; utilisateurs distincts par course pour A_1 et A_2 ;
  (3) texte : écrire ce qui est réellement tenu ; ajouter la condition d'emplacement à la liste d'arrêt.

**CE3-07 — majeure — Les dossiers du noyau (`noyau/`, `corpus/`) sont rangés dans le dossier de travail de l'organisme,
qui peut les renommer : index du corpus scellé falsifiable, journal des appels absent sans signal, « lecture
invalidée » déclenchable par l'organisme.**

- Fichiers : `boucle.executer_generation` l. 472-484 (journaux d'appels, de recherches et d'entraînements, modèles
  validés et corpus rangés dans `travail/`), l. 496-500 (scellement de `travail/corpus/index.jsonl` en fin de
  génération) ; `bac_a_sable.preparer` l. 198-202 (`travail` appartient à l'utilisateur de l'organisme, 0700 : il peut
  renommer ce qu'il contient, même ce qui appartient à root) ; `archive.deposer` l. 94-96 (journal copié s'il existe :
  silence sinon) et l. 123 (la vue n'exclut que le nom exact `noyau`) ; texte l. 192-194 (provenance, « corpus et index
  scellés »), l. 241 et 243 (liste d'arrêt).
- Défaut : l'organisme peut renommer `corpus/` et y mettre son propre index : le noyau y ajoute ses lignes et scelle le
  tout. Il peut renommer `noyau/` en fin d'exécution : le journal des appels manque au dépôt, sans événement, et les
  journaux d'entraînement et modèles validés passent dans la vue de la génération suivante — ce qui déclenche la
  vérification humaine « vue de l'archive contenant … → lecture invalidée » pour toute H-G1. Une routine de rangement
  ordinaire suffit.
- Preuve (E4, `travail/sortie-e4-falsification-corpus-noyau.txt`) : index scellé (compagnon : OK) qui commence par une
  notice forgée `doc-9999` jamais téléchargée ; l'index réel, non scellé, dans `corpus-pris/` ; `journal-appels.jsonl`
  absent du dépôt de g000 ; aucun événement du noyau ; la commande `find` de la liste d'arrêt rend
  `…/noyau-pris/journal-entrainements.jsonl` et `…/modele.npz`.
- Correction : (code) ranger les fichiers du noyau hors du dossier inscriptible par l'organisme (par exemple
  `espace/noyau/<lignée>/<gNNN>/` en 0700 et `espace/corpus/<lignée>/<gNNN>/` en 0755, à root, chemin donné dans le
  contexte) ; vérifier en fin de génération la présence de ces fichiers (absence = statut consigné) ; essai sain et
  artefact (cet organisme). (Texte) la ligne « vue de l'archive contenant … » invalide la paire touchée, pas toute la
  lecture.

**CE3-08 — majeure — Le lanceur extrait les traits avec `--strip-components=3` : chaque course s'arrête au contrôle des
traits.**

- Fichier : `procedure/lancer_courses_etape1_v1.sh` l. 49 (`git archive 6479769 essaim-m3-refonte-v1/traits/etape1-v1
  | tar -x -C "$EN/traits" --strip-components=3`) contre l. 55-56 et 72 (qui attendent `$EN/traits/etape1-v1/…`).
- Défaut : `git archive <commit> <chemin>` rend des chemins depuis la racine du dépôt (les lignes 50-51 le supposent :
  `--strip-components=2` → `organisme/…`). Ôter trois composants ôte aussi `etape1-v1/` : les fichiers arrivent sous
  `$EN/traits/`, la ligne 55 ne trouve pas `EMPREINTES-traits-etape1-v1.txt`, la course s'arrête (« traits : empreintes
  différentes », code 2) — avant toute dépense, mais aussi avant toute course, répétition comprise.
- Preuve (E5, `travail/sortie-e5-lanceur-extraction-traits.txt`, archive de même forme fabriquée par `tar`, sans git) :
  avec 3, la ligne 55 échoue ; avec 2, elle passe et `$EN/traits/etape1-v1/traits-16384` existe.
- Correction : `--strip-components=2` ; rejouer le lanceur jusqu'au § 5 bis exclu (sans appel) avant la répétition.

### Mineures

**CE3-09 — mineure — Le lanceur n'est pas empreinté dans le texte ; son en-tête est périmé ; une graine absente le fait
sortir en code 1 sans note.**
- Texte l. 24-26 et 237 : le lanceur est cité par son chemin, sans empreinte, alors qu'il porte une garde de la liste
  d'arrêt (§ 5 bis) et les options exactes des courses, et qu'il vit dans `docs/`, hors du commit `4f02bd8` (R1, R6).
- Lanceur l. 3 (« `prereg/gradient-etape1-sondes-v2.md` »), l. 5-6 (répétition « une génération, 20 appels, 2 USD … »,
  contre l. 81-83 : 3 USD par génération, deux rondes à 2 USD, plafond 10), l. 76 (« entrée 2 »).
- l. 85 et 90 : si la graine manque, `g=$(graine "$r")` échoue sous `set -euo pipefail` : sortie en code 1, sans la
  note ni le code 2 annoncés (E15, `travail/sortie-e15-lanceur-graine-absente.txt`).
- Correction : corriger ; citer chemin et empreinte du lanceur corrigé dans « Documents qui font foi » ; dire que tout
  changement après scellement passe par un addendum scellé et contre-lu.

**CE3-10 — mineure — Les lignées imposées passent par la phase de conception : ce n'est pas dit.**
- `boucle.concevoir` l. 606 (toutes les lignées actives) ; texte l. 62-71, 135-139, 164-165 (les 5 lignées × 8 rondes
  du plafond le supposent sans le dire) ; le brouillon v6 le dit (« elles feront les 8 rondes »).
- Écrites avant le contrat v3, elles ne déclarent pas la fin : huit rondes (≈ 160 USD et jusqu'à 2 × 8 × 2 400 s par
  course A), réécrites huit fois sans score ; leur g000 notée (et celle de B par `--depuis`) n'est plus l'organisme
  d'arbre `3e6fe2e9…` / `bceb1332…` du Plan, point 2. Leur conduite sans tâche de test n'est exercée par aucune
  répétition.
- Correction : le dire ; rapporter l'empreinte d'arbre de leur g000 ; choisir (même traitement, comme la v6, ou
  exemption par une option de code).

**CE3-11 — mineure — Temps : aucune durée, aucune règle pour une course interrompue hors garde ; la garde CE-07 ignore
la moisson ; contention du processeur propre au bras A.**
- Les lignées passent l'une après l'autre dans chaque ronde (`boucle.concevoir` l. 613-616, `boucler` l. 641-644) :
  au pire ≈ (8 + 3) × 5 × 2 400 s ≈ 36,7 h pour une course A, ≈ 10 h pour une course B ; rien ne borne la durée d'une
  course ; une interruption hors garde (conteneur relancé, fin de session) n'a pas de règle (« rapportée telle quelle »
  ne vise que les gardes ; « aucune relance »).
- La garde CE-07 (10 × 120 + 300 ≤ 2 400 s) ne compte pas la moisson : 30 recherches et 20 téléchargements à 25 s de
  délai chacun (`recherche.DELAI_S`, `moisson.DELAI_S`) font ≈ 1 250 s au pire.
- A_1 et A_2 tournent ensemble avec des entraînements bornés en temps d'horloge ; B_1 et B_2 n'entraînent pas : la
  contention pèse sur A seulement.
- Correction : durées attendue et au pire ; règle gelée pour une course interrompue (rapportée telle quelle, paires lues
  à la dernière génération valide commune ou coupées, aucune relance) ; dire que la garde ne couvre que l'entraînement ;
  consigner le nombre de cœurs et les `DELAI_DEPASSE` par bras.

**CE3-12 — mineure — La ligne d'arrêt « plafond total atteint pendant la conception » cite un essai qui ne l'exerce pas ;
son effet n'est presque jamais atteint ; la raison consignée peut tromper.**
- Texte l. 239 ; `test_phase_de_conception_a_critere_d_arret_de_l_organisme` (fin déclarée, borne, g000, bras gelé,
  confrontation : pas de plafond) ; `boucle.concevoir` l. 603-605 (`_plafond_restant() <= 0`), alors que la réservation
  au pire cas (`appels._reserver`) garde la dépense sous le plafond : près de l'épuisement, les appels rendent
  `PLAFOND`, et rondes et générations continuent sans budget.
- E9 (`travail/sortie-e9-plafond-pendant-la-conception.txt`) : aucune course simulée (plafond de 1,75 à 4 USD)
  n'atteint `arret_conception` ; à 0,15–0,4 USD l'amorçage est refusé (réservation au `max` du modèle) et l'événement dit
  « toutes les lignées ont déclaré la fin de leur conception » alors qu'aucune lignée n'existait.
- Correction : essai sain et artefact de cette garde (R5), ou ligne réécrite selon le comportement réel ; raison
  d'événement juste. Sans effet attendu à l'étape 1 (plafond = pire cas).

**CE3-13 — mineure — Répétition mécanique : banque réelle, test final noté et écrit ; Gemini non exercé.**
- Texte l. 184-188 ; lanceur l. 71-73 et 81-83 (banque réelle), l. 98 (contrôle : Opus seul), l. 126 (la sortie du noyau,
  qui imprime `courbes` et `scores_finaux` — `cli.lancer` l. 230 —, va dans `repetition.sortie.json`).
- « Aucun score » : le noyau note la génération sur le test de développement et sur le test final et l'écrit ;
  l'opérateur, qui est l'auteur, le lit en ouvrant la sortie. Gemini (Argon, lignées imposées sous conception) n'est
  exercé qu'au lancement de A_1, alors que son crédit était épuisé le jour même (n° 18 § 5) ; la répétition de la v6 en
  tient une lignée Gemini.
- Correction : sortie du noyau dans un fichier 0600 scellé, non ouvert avant la lecture ; statuts lus par un filtre qui
  écarte `score` ; appel de contrôle des trois espèces à la répétition et, si possible, une lignée Gemini et une lignée
  imposée sur deux rondes.

**CE3-14 — mineure — Les sections de « conv-audit », « insérées ici telles quelles », contredisent la v3 ou les faits
sur trois points.**
- Texte l. 189-190 ; sections l. 22-23 (la génération 0 est « relancée à l'identique par le bras gelé (`--gel
  --depuis`, mêmes empreintes) » : à l'étape 1, B = `--depuis` sans `--gel`) ; l. 27-28 (« Proposition pour l'étape 1 :
  … `usd_max_conception` = `usd_max` de génération » : la v3 prend 10 USD et non 37) ; l. 59-62 (injection : une
  consigne cachée « ne peut rien faire d'autre que tromper l'organisme », menace « mesurée » par le seul nombre de
  documents par source : CE3-06 et CE3-07 montrent plus, et rien ne la mesure).
- Correction : dire que les points 3 et 4 priment ; énumérer ce qui vaut des sections ; retirer ou nuancer la phrase
  sur l'injection.

**CE3-15 — mineure — Clé Brave, nombre de requêtes web et consignation des lancements (GO-2026-10-24-05).**
- GO-2026-10-24-05 nomme les clés « selon GO-2026-10-24-04 (Anthropic) et `GEMINI_API_KEY` » et exige « chaque
  lancement consigné avant dans `registres/depenses.md` » ; la v3 sert `BRAVE_API_KEY` (posée par Lazar à 21:06, heure
  de Paris, avec une limite d'usage : R-363, n° 15 § 2) sans citer R-363 ni borner les requêtes web (≈ 4 290 au pire
  pour l'étape), et ni le texte ni le lanceur ne prévoient la consignation.
- Correction : citer R-363 ; borne du nombre de requêtes web ; consignation avant chaque lancement (routine).

### Forme

**CE3-16 — forme — Graines : « entrée 2 » et format d'inscription.**
- l. 166-167 : « inscrite dans la section « Contre-lecture », entrée 2 » → entrée 3 (l. 294-295). Le lanceur lit
  `graine_r = <entier>` à la lettre (l. 76-77) : « `graine_1` = … » entre balises de code échoue (E6).
  `entropie_analyse` : dire « entier `generate_state(1, uint64)[0]` du troisième enfant » (`difference_h_g1` fait
  `SeedSequence(entropie)` puis `int(entropie)`).
- Correction : « entrée 3 » ; format littéral gelé `graine_1 = <entier>`, `graine_2 = <entier>`,
  `entropie_analyse = <entier>`, hors balises de code.

**CE3-17 — forme — Une ronde de conception et la génération de même numéro tirent les mêmes graines (R9).**
- `boucle.graine` l. 270-276 ; `executer_generation` l. 441 (en conception, g = numéro de ronde). E1 (suite) :
  `ordre_train`, `ordre_test` et `organisme` identiques pour c001/g001 et c002/g002. Sans effet sur l'appariement.
- Correction : la phase dans la clé de dérivation (version suivante du noyau), ou le dire.

**CE3-18 — forme — Menues inexactitudes.**
- l. 8 et 160 « alignées sur la v6 » : le temps de ronde diffère (2 400 s contre 1 800 s) ; le dire.
- l. 150 « tout le reste identique » : en B, le lanceur omet aussi `--usd-max-conception` et `--appels-max-conception`
  (sans effet sans rondes ; E13).
- l. 233 « sain et cinq artefacts » : six (cinq linéaires, une à couche cachée).
- l. 195 « mesuré le 24 octobre entre 19:40 et 19:46 UTC » : sans pièce ni empreinte (R6) ; le n° 14 (19:05 UTC)
  rapportait déjà ces 429.
- l. 65-66 « Lazar, 20:32 à 20:46 … « ne lui suggère rien » » : la phrase est de 20:42 (n° 14 § 1).
- l. 53 « H-G0 (… condition de lecture) » et l. 215 « ne change pas la table » : écrire « condition mécanique
  rapportée ».
- l. 191 « fin déclarée ou non (consigné) » : aucun événement ne consigne la borne atteinte sans déclaration ; elle se
  déduit (aucun `fin_conception`, huit rondes).
- `boucle.py` l. 219 : `"recherche": "arxiv"` au manifeste alors que quatre sources sont servies.
- `moisson.py` l. 285 : après une référence permise, les redirections ne sont contrôlées que pour https, pas pour l'hôte ;
  « hôte interdit » (l. 241) ne vaut que pour la référence initiale (l'adresse finale est consignée).
- `boucle.py` l. 557-564 : `fin_conception.json` lu sans borne de taille et recopié entier dans `evenements.jsonl`.

---

## Suivi des neuf corrections de la contre-lecture n° 2 (CE2-01 à CE2-09)

| remarque | état | vérification |
|---|---|---|
| CE2-01 nom de la lignée Gemini auto-écrite | **traitée** | texte l. 89-91 et 172 : `gemini-argon` ; le noyau forme bien ce nom (E1 : index « gemini-argon ») |
| CE2-02 commande du bras B refusée | **traitée** | texte l. 147-151 ; lanceur l. 94-95 sans `--organisme-impose` ; l'analyseur du noyau accepte B (E13) |
| CE2-03 « toutes choses égales » | **traitée en partie** | différences nommées (l. 94-101) ; tri de l'ordre de ronde (`boucle` l. 626-628) ; l'essai **échoue sans le tri** (E7). Mais la phase de conception ajoute une différence non nommée (CE3-01) et des différences d'heure (CE3-05) |
| CE2-04 artefact de `_lire_resultat` | **traitée** | `test_lire_resultat_modele_non_conforme_refuse` passe ; chaque artefact échoue pour sa raison (formes, non fini, objet Python refusé au chargement, clé en trop, courbe), aucun modèle copié (E12) ; « cinq » artefacts : six (CE3-18) |
| CE2-05 en-tête d'espace de travail | **traitée** | appel de contrôle par espèce avant chaque course (lanceur § 5 bis), même client que les courses ; la bibliothèque cliente `anthropic` 2.3.0 de l'environnement des courses place `anthropic-workspace-id` lu dans `ANTHROPIC_CUSTOM_HEADERS` dans ses en-têtes par défaut (E10, hors ligne, clé factice). La répétition n'exerce qu'Opus (CE3-13) |
| CE2-06 `revision_resolue` vide | **traitée** | divulgation gardée (l. 132-133) ; manifeste vérifié (`revision_resolue: null`) |
| CE2-07 script des sondes témoins | **traitée** | engagement l. 182-183 ; rappel : les témoins entrent dans les déclencheurs de l'audit (point 6), l'addendum doit précéder la lecture |
| CE2-08 empreintes de l'entrée 2 | **traitée** | `6ae4a8b3…` et `c377b2e3…` présentes et concordantes |
| CE2-09 déclencheurs d'audit | **traitée** | `declencheurs_audit_h_g1` (une fonction), essai sain et quatre artefacts, Plan point 6. Mais le seuil bas se déclenche sur l'absence de réponses et la table n'a pas de sortie (CE3-03) |

Bilan : 9 sur 9 réellement traitées ; deux (CE2-03, CE2-09) laissent un reste que la v3 rend sensible (CE3-01, CE3-03).

---

## Réponses aux sept points

**1. Les corrections CE2-01 à CE2-09 sont-elles réelles ? Les deux essais prouvent-ils ce qu'ils disent ?** Oui (tableau
ci-dessus). L'essai d'ordre de ronde prouve son énoncé : avec le tri retiré d'une copie du code, il échoue ; au commit
cité, il passe (E7). Il ne contient ni phase de conception ni lignée imposée, mais le tri rend l'ordre indépendant de
l'ordre d'insertion, donc la propriété vaut en général ; l'ordre des rondes de conception, lui, n'est pas trié, sans
effet sur l'appariement (B n'en a pas). L'essai de `_lire_resultat` prouve son énoncé au niveau de la fonction : le cas
sain copie le modèle, chaque artefact est refusé pour sa propre raison et rien n'est copié (E12).

**2. Conception dans A, absence de conception dans B : H-G1 reste-t-elle bien définie ?** Pas en l'état. Le g000 de B est
bien celui de A (même empreinte, E1), et le texte dit honnêtement que B retire l'entraînement à un organisme conçu en
l'ayant. Mais B ne reçoit pas la mémoire de conception (CE3-01) : Δ mélange deux causes, dans le sens prédit. Une fois
CE3-01 corrigée, H-G1 mesure ce que le service d'entraînement apporte en générations notées à un organisme et à sa
mémoire conçus avec lui : c'est bien défini. Effets de la conception : appariement (CE3-01) ; lecture (CE3-02 : les
rondes comptées comme générations) ; coût : +400 USD au pire par course A, arithmétique juste (l. 164-165), couverte
par GO-2026-10-24-05 sans plafond ; temps : jusqu'à ≈ 26,7 h de conception de plus par course A, et B attend la fin de
A (CE3-05, CE3-11). Les lignées imposées passent par la conception (code), ce que le texte suppose dans son plafond
sans le dire, avec ses conséquences (CE3-10).

**3. Moisson.** Bornes du texte = bornes du code (30 recherches, 20 téléchargements, 40 Mo, 8 Mo par document, 60 000
caractères rendus ; les tentatives échouées comptent). Provenance : la référence initiale doit venir d'une recherche de
la même génération ou ronde, d'un identifiant arXiv ou d'un hôte permis — tenu ; les redirections ne sont vérifiées que
pour https (CE3-18). Scellement : l'index est scellé en fin de génération, mais dans un dossier que l'organisme peut
réécrire (CE3-07). Texte rendu comme donnée : dit par le contrat ; le noyau n'exécute rien ; l'organisme n'a ni réseau
ni clé. Injection : elle peut faire plus que « tromper l'organisme » — le pousser à lire hors de sa lignée (CE3-06) ou à
toucher aux dossiers du noyau (CE3-07). Manque principal : la recherche de provenance des textes publics du test final (CE3-04). Essais sain et
artefact : `test_telechargeur_provenance_plafonds_et_extraction` et `test_moisson_de_bout_en_bout_en_simulation`
passent. Source indisponible : un 429 rend `ECHEC_RECHERCHE` et consomme une recherche ; une clé Brave absente retire la
source `web` (`SOURCE_INCONNUE`, non comptée) ; les deux peuvent différer entre les bras d'une paire (CE3-05).

**4. Plafonds par course et pire cas.** Arithmétique juste : A_r = 3 × 37 + 8 × 5 × 10 + 5 × 3 × 37 = 111 + 400 + 555 =
1 066 ; B_r = 555 ; total 3 242 USD. Cohérent avec le noyau : chaque génération ou ronde reçoit `min(usd_max,
plafond restant)` et chaque appel réserve son pire cas ; l'amorçage (pire cas ≈ 3,3 USD par espèce au `max` du
modèle, compté 37 dans le plafond) et les rondes (400 au plus) laissent dans A au moins 555 USD aux générations notées,
comme dans B : le plafond ne mord pas par construction. « 37 USD suffisent à
160 appels au pire cas » vaut pour des consignes d'une tâche (calcul de la v6) ; un organisme qui groupe ses tâches ou
demande plus de 4 096 jetons en fera moins — dans les deux bras. La garde de « plafond total pendant la conception »
est presque inatteignable et non essayée (CE3-12). Temps non borné par course (CE3-11). Le lanceur passe exactement les
options du texte pour A_r (E13 : égalité de toutes les options) ; pour B_r, il retire aussi deux options de conception
sans effet (CE3-18) ; répétition conforme au texte. Mais il s'arrête au contrôle des traits (CE3-08).

**5. Isolation pendant la conception et la moisson.** Même chemin de code que les générations notées : organisme sous
son utilisateur, espaces de noms neufs, réseau coupé ; entraîneur isolé sous son propre utilisateur (CE-02) ; aucune
tâche de test dans les rondes ; les accès réseau de la moisson sont faits par le noyau. L'essai d'isolation de
l'entraîneur et les essais de fuite de l'organisme passent en root. Restent : les vues lisibles hors de la lignée, et
hors de la course dans un dossier traversable (CE3-06) ; les dossiers du noyau renommables (CE3-07).

**6. Analyse et lecture.** Table du texte = `lecture_h_g1`, ligne à ligne ; « confirmé » = borne basse > 0 et Δ ≥ +0,10 ;
« réfuté » = borne haute < +0,10 ; déclencheurs du texte = `declencheurs_audit_h_g1` (0,95, 0,30, 0,40). Mais
`generations_valides` est faux en présence de conception (CE3-02), le seuil bas lit l'absence de réponse comme une
inversion et la table n'a pas de sortie après l'audit (CE3-03). H-C : les événements (`ronde_conception`,
`fin_conception` avec la déclaration, `conception_sans_successeur`, `arret_conception`) et la liste `rondes_conception`
du rapport permettent le rapport promis ; « documents moissonnés par source » demande de relier l'index du corpus au
journal des recherches (aucune fonction ; index falsifiable, CE3-07).

**7. Le reste.** R1 : huit sections ; prédiction chiffrée et signée ; table gelée sauf sa sortie (CE3-03) ; emplacement
des courses non fixé (CE3-06) ; sections insérées ambiguës (CE3-14). R2 : contre-lecture n° 3 par un sous-agent neuf,
pièces données. R3 : « run décisif exigé » (R-344) tenu ; la puissance modeste (44 % à l'effet prédit) est dite ; CE3-01
pousse vers le signe prédit : à corriger. R4 : audit bilatéral, mais déclenché par des pannes (CE3-03) ; asymétries
CE3-01, CE3-05. R5 : nouvelles gardes de moisson essayées ; garde de conception non essayée (CE3-12) ; deux replis
silencieux (CE3-02, CE3-07). R6 : lanceur sans empreinte (CE3-09) ; mesure du 429 sans source (CE3-18). R7 : 0,69 / 0,50
dits non audités ; annexe dite non opposable. R9 : graines par `SeedSequence`, E au scellement ; graines partagées entre
ronde k et génération k (CE3-17). R10, R12, R13 : tenus (arrêts par groupe de processus ; sortie déjà existante refusée ;
verdict de porte par un sous-agent neuf). Chiffres vérifiés : comptes de la banque, traits (12 407 jetons, aucune
troncature, 200 × 4 096, révision), puissance (identique), plafonds. Provenance des décisions de Lazar : 21:06, heure de
Paris (« oui oui il doit inclure la phase de conception et la moisson avant scellement ») = n° 15 (19:08 UTC,
`55e6f5f0…` vérifiée) = R-363 ; 20:32–20:46 = n° 14 § 1 ; clé Brave = n° 15 § 2 et R-363 ; GO-2026-10-24-05 de type
« calcul », sans plafond fixé par Lazar, couvre les courses « telles que le préenregistrement scellé les définit » ;
R-344, R-351, R-355, R-356 concordent avec l'extrait des registres v4 et les messages. Réserve : la clé Brave et la
consignation des lancements (CE3-15).

---

## Ce que j'ai rejoué

Tout sous `env -i PATH=/usr/bin:/bin HOME=<travail>`, `python -B`, avec l'environnement des courses
`/opt/essaim-m3-venv-v1` (Python 3.13.17, numpy 2.4.6, anthropic 2.3.0, pytest 9.1.1), sur une copie du code dans
`travail/code` ; les essais qui lancent des organismes isolés tournés dans un espace de noms de montage privé où
`/var/tmp` est lié à `travail/vartmp` (et, pour E3, `/srv` à `travail/exp/srv`) : rien n'a été écrit dans le vrai
`/var/tmp/essaim-m3` (vérifié : aucune empreinte de mes racines n'y figure ; les entrées nouvelles y viennent
d'ailleurs). Root dans le conteneur ; aucun processus laissé (vérifié pour les utilisateurs 60000 à 60020 et 61000 à
61020, et par nom de commande) ; aucune écriture dans les pièces ni dans le dépôt ; aucune commande git ; aucune clé lue
ni affichée (E10 n'a affiché que des noms d'en-têtes et la valeur factice « espace-factice », avec une clé factice).

**Appel réseau non voulu, à consigner.** La suite complète contient `test_sources_reelles_de_moisson_si_reseau`, qui
interroge arXiv « si le réseau le permet » : il est passé (87 essais = 82 réussis + 5 échecs, aucun sauté), donc une
connexion et une recherche publique en lecture seule ont été faites vers `export.arxiv.org` (« evaluation awareness
language models », 2 résultats demandés ; aucune clé, aucune dépense). Je ne l'avais pas désélectionné ; je ne l'ai pas
relancé (les relances partielles l'ont exclu).

| essai | ce qu'il montre | sortie (`travail/`) | empreinte |
|---|---|---|---|
| suite du noyau | 82 réussis ; 5 échecs par absence de données des pièces (2 exécutent `organismes/gemini-v2`, 3 lisent la banque réelle ou les traces) : cohérent avec « 85 passent, 2 désélectionnés » | `sortie-pytest-complet.txt` | `ba685e28…` |
| E1 | mémoire de conception en A seulement ; graines ronde k = génération k | `sortie-e1-memoire-de-conception.txt` | `5ec17cfd…` |
| E2, E2b | génération lue fausse ; génération invalidée relue | `sortie-e2-generations-valides.txt` | `015ede30…` |
| E3 | lectures hors de la lignée et hors de la course ; correction par 0700 | `sortie-e3-lectures-hors-de-la-lignee.txt` | `d83bb07b…` |
| E4 | index du corpus forgé et scellé ; journal absent ; vue « invalidante » | `sortie-e4-falsification-corpus-noyau.txt` | `05a8988c…` |
| E5 | extraction des traits du lanceur | `sortie-e5-lanceur-extraction-traits.txt` | `79d7ee4f…` |
| E6 | validateur : seule plainte, l'entrée 3 ; format de graine lu par le lanceur | `sortie-e6-validateur.txt` | `afc7a434…` |
| E7 | essai d'ordre de ronde : échoue sans le tri, passe avec | `sortie-e7-ordre-de-ronde.txt` | `090b734d…` |
| E8 | puissance : identique à `puissance-v1.json` (six cas) | `sortie-e8-puissance-rejouee.txt` | `5ccba5c8…` |
| E9 | plafond pendant la conception jamais atteint ; raison trompeuse | `sortie-e9-plafond-pendant-la-conception.txt` | `ad44c16c…` |
| E10 | en-tête d'espace de travail placé par la bibliothèque cliente (hors ligne) | `sortie-e10-en-tete-espace-de-travail.txt` | `aad2a4d7…` |
| E12 | raisons de refus de `_lire_resultat` | `sortie-e12-lire-resultat-raisons.txt` | `f369b472…` |
| E13 | lignes de commande du texte et du lanceur, analysées par le noyau | `sortie-e13-options-des-commandes.txt` | `7bfa38bd…` |
| E14 | audit déclenché par une lignée sans réponse | `sortie-e14-audit-sans-reponse.txt` | `9d30a8ea…` |
| E15 | graine absente : code 1 sans note | `sortie-e15-lanceur-graine-absente.txt` | `e25bd5a7…` |

Organismes d'essai écrits par moi (simulation seulement) : `travail/exp/explorateur/`, `travail/exp/falsificateur/` ;
scripts : `travail/exp/e1_e2.sh`, `e3.sh`, `e4.sh`, `e8_puissance.py` ; courses simulées gardées sous `travail/exp/`.
Après les essais, les espaces des organismes (`travail/vartmp/essaim-m3`), les dossiers temporaires de pytest et la
copie du code sans le tri ont été effacés. Aucun script de la relève de Gemini exécuté.

## Ce que je n'ai pas pu vérifier

- Les courses réelles, les espèces réelles, la moisson réelle (hors l'appel arXiv non voulu ci-dessus) : durées, coûts
  réels, débit, quotas, conduite des organismes en conception.
- Le code des deux lignées imposées (absent) : leur conduite en ronde sans tâche de test, leurs empreintes d'arbre
  `3e6fe2e9…` et `bceb1332…`, le chemin `outils/essaim-m3-debogage-v3/organisme` au commit `233fde6` supposé par le
  lanceur.
- Les trois essais qui exigent la banque réelle ou les traces (dont la référence de surface 0,69 / 0,50) ; la banque
  elle-même.
- La forme des chemins rendus par `git archive` : simulée avec `tar` (aucune commande git permise) ; la conclusion suit
  le comportement documenté de git et l'hypothèse que font les lignes 50-51 du lanceur.
- Les étapes 1, 2, 4, 5 bis et 6 du lanceur (elles lisent le dépôt, la garde de calcul ou appellent des interfaces
  payantes) ; seuls l'extraction des traits, la lecture des graines et les options ont été rejoués.
- L'acceptation de l'en-tête d'espace de travail par le serveur (seul le côté client, hors ligne).
- La recherche de provenance des textes du test final (CE3-04) : risque déduit des pièces, non mesuré (aucun réseau) ;
  l'accès conditionnel au jeu `jjpn2/eval_awareness` n'a pas été testé.
- La mesure du 429 d'OpenAlex entre 19:40 et 19:46 UTC (aucune pièce).
- Le brouillon v6 de la confrontation : seules ses bornes et sa table de devis ont été lues ; il n'est pas relu ici.
