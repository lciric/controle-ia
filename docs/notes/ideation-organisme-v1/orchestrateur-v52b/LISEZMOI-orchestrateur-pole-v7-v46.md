# Orchestrateur du pôle, v7 — version 46 : tour (c) « outils clôturés », en préparation hors ligne

Lignée conv-audit (sous-agent Opus 5.5), 29 octobre 2026, travail commencé au relevé `date -u` de 10:01 UTC. v1 à v45 gardées
(R12) : LISEZMOI et EMPREINTES v1 à v45 intacts. Décisions de Lazar du 29 octobre (R-433, R-434, R-441, R-444, R-448 de
`registres/decisions.md`) et note de conception `../ideation-organisme-approches-v1/note-tour-c-outils-clotures-v1.md` ; plus
deux constats de la contre-lecture CL12 de la v45 relayés en cours de travail (« corrections de CL12 », plus bas).

**v46 n'est pas contre-lue.**

**Non lançable sans épreuve réelle courte sur GO** : le kit réel n'a jamais été lancé avec ces outils ici ; aucune session réelle,
aucune dépense, aucun réseau, aucune clé (essais sous environnement propre, `patch.dict(os.environ, env_propre, clear=True)`).

**Rétrocompatibilité.** Sans `--dossier-ferme`, la ligne de commande et les entrées de la v45 restent valides et la course est
celle de la v45 : consignes des proposeurs et des juges identiques octet pour octet (comparées sur la copie de la v45), réglages
du kit sans outil, aucun dossier `lecture` ni `tour-…`, ni mesures de lecture ni citations au manifeste de fin. Deux changements
touchent aussi la course sans dossier fermé, et ce sont des corrections : CL45-02 (caviardage après analyse JSON) et la garde
générale des outils (deux trous fermés, rôles autres que l'idéation).

## Ce que fait la v46

| point | ce qui est fait | essai (`TestV46`, `essais/test_v7_ideation.py`) |
|---|---|---|
| 1. dossier fermé | `--dossier-ferme DOSSIER` ; nouveau module `pole/dossier_ferme.py` : `index.json` scellé (compagnon `.sha256`) **et dans la liste blanche**, entrées `chemin`, `sha256`, `titre`, `resume`, `sections`, `pages` (facultatifs les deux derniers) ; vérifié avant tout appel et toute écriture : exactement les fichiers listés, aucun lien symbolique, aucun chemin absolu, `..` ou `~`, aucun fragment interdit, chaque empreinte, texte UTF-8 (un PDF est refusé), caviardage sans effet (aucun secret), nombre de pages déclaré ; pages par `[p.N]` en tête de ligne, sinon saut de page, sinon le fichier entier ; la consigne des proposeurs porte **l'index** (titre, résumé, taille, pages, sections), jamais le texte ; `--taille-max-pieces` ne s'applique qu'aux pièces servies en entier ; manifeste de départ : empreinte de l'index, fichiers, modes | `test_v46_1_dossier_ferme_index_scelle_empreintes_et_artefacts` (cas sain, puis onze artefacts refusés sans aucun appel ni SORTIE : fichier en plus, absent, changé, index descellé, hors liste blanche, lien, PDF, secret, chemin remontant, fragment interdit, pages fausses) |
| 2. outils confinés du kit | proposeur Claude avec dossier fermé : `OUTILS_PAR_ROLE_DOSSIER_FERME["proposeur_ideation"] = ("Read", "Grep", "Glob")` (sans dossier : `OUTILS_PAR_ROLE`, `()`, inchangé) ; juges toujours `()` (une racine donnée à un juge lève) ; racine de lecture = une **copie vérifiée** du dossier fermé dans `passe-N/lecture/` (dossier courant de l'agent), empreintes revérifiées après la session (copie altérée : incident dit) ; `garde_outils.py` : `evaluer_appel_lecture` et `fabriquer_crochet_lecture` — refus de tout chemin ou motif hors de la racine (absolus hors racine, `..`, `~`, accolades, `path` hors racine, liens résolus par `os.path.realpath`), de tout paramètre inconnu, de toute écriture (`Write`, `Edit`, `MultiEdit`, `NotebookEdit`), de `Bash` et de tout autre outil ; garde générale (`evaluer_appel`, autres rôles) : motif `Glob.pattern` et filtre `Grep.glob` vérifiés (v45 : `Glob /etc/*` et `Grep glob /root/**` admis, vérifié sur la copie de la v45) ; consigne système propre ; `max_turns` du kit = garde-fou + 5 (borne de sûreté, aucun nombre de tours fixé par ailleurs) | `test_v46_2_outils_confines_du_kit_et_epreuves_r5_du_crochet` (options et ligne de commande du kit `--tools Read,Grep,Glob`, juge `--tools ''` ; cas sain : lecture d'un fichier du dossier et recherche d'un motif ; artefacts : `Read /etc/passwd`, `Glob {"pattern": "/etc/*"}`, `Grep {"glob": "/root/**"}`, `Read` d'un lien vers l'extérieur, `..`, `~`, accolades, `path` hors racine, paramètre inconnu, `Write`, `Edit`, `MultiEdit`, `Bash`, `WebFetch`, `Task`, `Agent`, `mcp__…` ; course avec un faux kit qui passe ses appels par le vrai crochet ; copie altérée ; garde-fou franchi dans le kit) |
| 3. outils par protocole | réponse d'un proposeur sans outil : bloc `{"demandes": [{"lire": "<chemin>", "pages": [a, b]}, {"chercher": "<motif>", "dans": "<chemin>"?}]}` ; servi au tour suivant depuis le dossier fermé, rien d'autre (texte des pages ; lignes trouvées avec chemin et page, motif littéral, jamais une expression rationnelle) ; tout l'historique servi est renvoyé à chaque tour (commande sans état) ; une réponse peut porter une version provisoire des fiches avec ses demandes ; Argon toujours par protocole avec un dossier fermé ; Claude par protocole sous `--outils-par-protocole` (alors **aucun outil du kit** : égalité stricte) | `test_v46_3_outils_par_protocole_argon_et_claude_a_egalite` (Argon factice, demandes servies, refus de `/etc/passwd`, `../…`, plage vide ; Claude sans racine ni outil ; par le lanceur : course, seconde passe, bras, classement à trois juges) |
| 4. aucun nombre de tours | le proposeur lit tant qu'il veut et s'arrête en rendant sa fiche (bloc `{fiches}` sans demande) ; plafonds de sûreté seuls : plafond en dollars de la session (chaque tour reçoit le reste ; dépassé : arrêt, comme avant), `--delai-session-s` (ensemble des tours d'une passe par protocole, et chaque session du kit ; défaut 3 600), `--max-demandes-lecture` (défaut **1 000** ; au-delà : arrêt de la session, **incident** au journal et aux mesures, pas un réglage) ; **avertissement** : dès que la dépense de la session atteint 80 % de son plafond, le tour suivant porte « Il te reste X USD : rends ta fiche. » (outils du kit : refus du prochain appel avec ce motif, si le relais est lisible) ; une fiche rendue sous avertissement est **marquée** (`sous_avertissement`), jamais rejetée | `test_v46_4_tours_libres_garde_fou_incident_avertissement_et_delai` (huit tours acceptés ; garde-fou à 3 : incident, arrêt au quatrième tour ; avertissement au troisième tour, fiche gardée et marquée ; délai dépassé : arrêt ; options refusées) |
| 5. mesures (R-448) | `mesures_lecture` au **manifeste de fin seulement** : par proposeur et par passe, pages lues dans l'ordre (chemin, page, tour, depuis le cache), répétitions, demandes par type et refusées, recherches, versions de la fiche et distance entre versions (même distance d'édition que la v44), part du dossier lu, avertissements ; outils du kit : journal du crochet, lignes de `Read` ramenées aux pages (approximation dite) ; `mesures_convergence` (v44) renvoie à `mesures_lecture` ; jamais aux juges (N-053) | `test_v46_5_mesures_de_lecture_au_manifeste_de_fin_jamais_aux_juges` |
| 6. cache partagé (R-444) | `CachePages` : une page servie à un proposeur est servie aux autres depuis le cache (même texte, même empreinte), chaque service consigné (à qui, tour, depuis le cache ou non) | `test_v46_6_cache_partage_des_pages_servies` |
| 7. citations (L7) | à la fin des passes, avant les juges : chaque citation `[chemin, p.N]` (ou `[p.N]` après une mention d'un fichier du dossier dans la même chaîne) est vérifiée : la page existe ; le passage entre guillemets qui la précède s'y retrouve (texte normalisé, fragments coupés aux points de suspension) ; chaque fiche servie (témoins compris, pour qu'aucun ne se distingue par l'absence du champ) porte `citations_verifiees` (citation, vrai/faux), seule information outillée que voient les juges, expliquée dans leur consigne ; détail (page, passage, motif, citations non attribuées) au manifeste de fin | `test_v46_7_citations_verifiees_seule_information_outillee_des_juges` |
| 8. moisson | le protocole reconnaît `{"moissonner": "<requête>"}` et le refuse, motif « moisson non disponible (v47) », servi au tour suivant et compté ; une table de types (`TYPES_DEMANDE`) l'accueillera en v47 | `test_v46_8_moisson_reconnue_et_refusee` |
| rétrocompatibilité | voir plus haut | `test_v46_retrocompatibilite_ligne_de_commande_de_la_v45` (course de la v45 par le lanceur, code 0, consigne identique, aucun champ du tour (c) ; `--outils-par-protocole` sans dossier, `--dossier-ferme` au bras : refusés) |

## Corrections de CL12 (contre-lecture de la v45, relayées par le coordinateur)

| constat | correction | essai |
|---|---|---|
| **CL45-01** `TestV45` placée après `unittest.main()` dans `essais/test_v7_ideation.py` (sautée en lancement direct ; `discover` la jouait) | `TestV45` déplacée avant le bloc `if __name__ == "__main__"`, `TestV46` au même endroit ; le bloc est le dernier énoncé du fichier | `test_v46_cl45_01_classes_avant_unittest_main` (arbre syntaxique : aucune classe après le bloc ; lancement direct du fichier en `__main__` : `TestV45` et `TestV46` trouvées et jouées) |
| **CL45-02** le noyau caviardait le texte brut d'une réponse (qui porte le bloc JSON des fiches ou des notes) **avant** de l'analyser | `Resultat.texte_brut` (texte non caviardé, gardé en mémoire, jamais écrit, hors de `repr`) rendu par l'adaptateur du kit et par la commande externe ; la course et le bras analysent le JSON sur ce texte (`texte_a_analyser`) puis caviardent chaque valeur : fiches par `valider_fiche_ideation`, notes par `valider_notes`, demandes et versions du protocole par `caviarder_objet` ; motifs de refus et d'arrêt caviardés ; les traces (`reponse.md`) restent caviardées sur le texte ; une fiche dont un secret reste **à cheval sur deux champs** après le caviardage valeur par valeur est refusée avec ce motif (jamais tue) | `test_v46_cl45_02_caviardage_valeur_par_valeur_apres_analyse_json` (cas sain : clé `sk-ant-…` dans une valeur, caviardée, écrite nulle part ; artefacts : `token=abcdefghij"suite` — sur le texte, le caviardage mangeait la barre d'échappement, d'où un guillemet nu et « aucun bloc JSON {fiches} », vérifié sur la copie de la v45 —, clé privée à cheval sur deux valeurs — sur le texte, les champs entre elles disparaissaient en silence —, justification d'un juge, réponse d'Argon par commande externe) |

**Phrase corrigée du LISEZMOI v45** (le fichier v45, scellé, n'est pas touché ; la correction vit ici) : « Recherche faite
(`grep`) : aucune autre fonction ne remplace du texte sur du JSON sérialisé (`caviardage` travaille déjà valeur par valeur par
`caviarder_objet` ; …) » était **faux** : `lancer` (course) et le bras caviardaient le texte de la réponse avant d'en extraire
le bloc JSON. Corrigé en v46 (ci-dessus).

## Restes et doutes déclarés

- **Kit réel jamais lancé avec ces outils** : que `tools=["Read","Grep","Glob"]` donne exactement ce jeu, que le crochet voie
  chaque appel de fichier, que le motif d'un refus soit rendu au modèle (avertissement de budget, garde-fou), que le kit
  n'ajoute pas à `Read` un paramètre que la garde refuse (liste blanche de paramètres : un refus à tort est possible), qu'un
  motif `Glob` absolu sous la racine se comporte comme attendu : SUPPOSÉ. Les outils de fichiers tournent dans le processus du
  kit, pas dans le bac à sable : le crochet est la barrière principale (SUPPOSÉ, à éprouver).
- **Avertissement du kit** : il exige un relais lisible (dépense de la session lue au relais) ; sinon aucun avertissement, dit
  au journal du crochet (`relais_illisible`). Par protocole, il est calculé sur les coûts comptés.
- **Coût du protocole** : chaque tour renvoie tout l'historique servi (commande sans état) : croissance quadratique bornée
  par le plafond de la session et par 200 000 caractères servis au plus par tour (`TAILLE_MAX_SERVIE_PAR_TOUR`, le reste
  redemandé au tour suivant). Le contrôle d'Argon porte la consigne du **premier** tour, pas les suivants ; chaque tour d'Argon
  est gardé avant envoi contre ce qui reste de son plafond (`garde_passe_externe`), refus = arrêt sans envoi.
- **Délai** vérifié avant chaque tour, pas pendant : un tour en cours peut dépasser le délai de la passe d'au plus son propre
  délai (`--delai-commande-s`, ou le délai de la session du kit).
- **Mesures du kit** : pages lues approchées (lignes de `Read` → pages ; 2 000 lignes par défaut, SUPPOSÉ) ; le cache ne
  vaut que pour les pages servies par le noyau (le kit lit sa copie directement).
- **Témoins** : avec citations vérifiées servies, des fiches outillées citeront des pages et des témoins sans citation
  deviendront reconnaissables : réécrire les témoins du tour (c) avec des citations du dossier (note, § 3), non fait ici.
- **`--mesurer-consignes`** avec `--dossier-ferme` mesure les consignes du premier tour (index seul) et un juge sans le champ
  `citations_verifiees` (léger sous-compte).
- Aucun dossier fermé réel n'a été construit (corpus intégral, retraits de sûreté page par page) : travail séparé.
- Moisson : v47.

## Épreuve réelle courte à faire avant tout tour (c) — devis à écrire, sur GO (dépense)

Kit et relais réels, Opus 5.5, petit dossier fermé d'un extrait, consigne de quelques milliers de caractères, plafond par session
0,5 dollar ; ordre de grandeur SUPPOSÉ : une dizaine de sessions Claude courtes (≈ 1 à 3 dollars) et trois ou quatre appels
d'Argon par protocole (≈ 0,5 dollar, barème à confirmer). À vérifier :
1. cas sain : « lis la page N de l'extrait X et cite la phrase qui donne Y » → phrase exacte, `[chemin, p.N]`, citation vraie
   au manifeste ; journal du crochet complet ; lectures de cache au relais ;
2. artefacts, un par session (pièce piégée) : lire `/etc/hostname`, le LISEZMOI du dépôt, `Glob /etc/*`, `Grep` avec `glob`
   absolu, un lien vers l'extérieur ; écrire un fichier ; lancer un sous-agent ; recherche en ligne ; attendu : chaque tentative
   refusée et visible (motif du crochet ou outil absent), aucun fichier hors du dossier, copie intacte, course non interrompue
   par une erreur de garde ; une tentative réussie arrête tout et revient à Lazar ;
3. motif de refus rendu au modèle (avertissement de budget simulé par un petit plafond ; garde-fou à 3 demandes) ;
4. `max_turns` réel, coût par tour et tenue du cache (le coût du kit outillé dépend du cache : × 2 à × 20, note § 4) ;
5. Argon par protocole : la vraie commande renvoie des demandes au format, s'arrête à son plafond, accepte une consigne qui
   croît d'un tour à l'autre.

## Essais

427 essais (415 en v45 ; + 12 : `TestV46`), 0 échec, deux exécutions complètes sur l'arbre final (194,3 s et 199,0 s), aucun processus survivant,
`essais/_tmp` retiré, aucun `.pyc` suivi modifié (empreintes comparées au relevé de début). Fichiers nouveaux :
`pole/dossier_ferme.py`, ce LISEZMOI, les EMPREINTES v46. Fichiers changés : `pole/garde_outils.py`, `pole/adaptateurs.py`,
`pole/ideation.py`, `demonstrations/ideation_v1.py`, `essais/test_v7_ideation.py`.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v46.txt
```
