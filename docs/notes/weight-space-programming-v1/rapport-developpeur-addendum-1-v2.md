# SPARKS-EXP7-NUL — rapport du rédacteur-développeur : brouillon 2 de l'addendum n° 1 et code v2

Rédacteur-développeur neuf (sous-agent Claude, Opus 5.5) ; n'a écrit ni le texte v1, ni le brouillon 1, ni le code à
`55399606`, ni les contre-lectures. Consigne `consigne-developpeur-addendum-1-brouillon2-et-code-v1.md`, sha256
`3ea5cdba173ca33118d29c6766821e4f60a4982b1caf84b170b95a37b0ee2d72` (compagnon « OK » avant lecture). Travail ouvert le
4 novembre 2026 à 08:30 UTC ; interrompu par la limite d'usage (≈ 08:50 → 10:21) et par un redémarrage du conteneur
(≈ 12:20) ; rapport écrit vers 12:40 UTC (`date -u`). Aucune poussée, aucun `.sha256` sur `main`, aucun fichier
existant modifié (ni sur `main`, ni à `55399606`), rien sous `donnees/` ni `/home/claude/coffre-*`, aucun réseau,
aucun modèle téléchargé ni appelé, aucune dépense, aucune clé lue.

**Verdict.** Brouillon 2 écrit par script (29 couples dans l'ordre, puis D-1 à D-8, trois marqueurs « À REMPLIR »).
Code v2 sur la branche locale `prep/sparks-exp7-nul-v2`, commit `50fb15cd301d0cce63058261f5916ae3a601a638` (trois commits
sur `55399606` : `97c5d8ed`, `ee91412d`, `50fb15cd`), 48 fichiers ajoutés, aucun modifié. Essais et banc : section 3. Les scripts d'instance n'ont **pas** pu
être joués de bout en bout en `MODE=jouet` (section 4) : réserve.

## 1. Fichiers et empreintes

Sur `main` (arbre de la session, fichiers neufs, sans compagnon, à empreinter par la mère) :

| Fichier | sha256 |
|---|---|
| `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon2.md` | `7e98397e53784637c03c1f1f7450e582c25939a46d15ca53380ebf8b70958170` |
| `docs/notes/weight-space-programming-v1/appliquer-couples-addendum-1-brouillon2-v1.py` | `a84c857698cd021e4aa80bf2b241abc947d095df9a48e1ee030ac3c2339e61a3` |
| `docs/notes/weight-space-programming-v1/sortie-appliquer-couples-addendum-1-brouillon2-v1.txt` | `7775cbca0ca3a9211e3da60514b22736ec44d0863878c495c6fe75b8936957bf` |
| `docs/notes/weight-space-programming-v1/essais-et-banc-sparks-v2/` (sorties brutes des essais et des bancs, copiées du bloc-notes) | empreintes en section 3 |
| ce rapport | — |

Le script vérifie les empreintes d'entrée (brouillon 1 `80e3dc4b…`, couples `16ff3d94…`), exige chaque « ancien » une
seule fois au moment de son application, refuse d'écraser la sortie, exige trois marqueurs. Contrôle croisé : le texte
après les 29 couples a l'empreinte `141f1684e9ad0b8c…`, **égale au texte d'essai du contre-lecteur** (`141f1684…`).

Sur la branche `prep/sparks-exp7-nul-v2` au commit `50fb15cd` (chaque fichier avec son compagnon `.sha256`, comme à
`55399606` ; la liste fermée `liste-fermee-v1.txt` nomme les 48 chemins, compagnons compris ;
`garde_code liste . 50fb15cd…` → « LISTE FERMÉE CONFORME : 48 fichiers ») :

| Fichier | sha256 |
|---|---|
| `docs/notes/sparks-exp7-nul-v1/consigne-lecteur-principal-v2.txt` | `c74c13276776b88610b6744232971d87eeefaf685e109e516a09fd5cafedfe48` |
| `docs/notes/sparks-exp7-nul-v1/procedure-lecteurs-v2.md` | `fce690bf94fdbdd017c2ebb7834bcae5747191bfe0fc76bcc1b7da2237072053` |
| `scripts/amorce_instance_sparks_exp7_nul_v2.sh` | `d85ef620a63d9c2ef6d932f0864cbb7750d135194cfec95823e1a931da40fb6d` |
| `scripts/banc_mutations_sparks_exp7_nul_v2.py` | `0a5c56415d0dcd5b94d60f51af5f723c3ce3b18d18144e75a097a8fbfdcae6dd` |
| `scripts/lancer_sparks_exp7_nul_v2.sh` | `1050857a025dea2f653b09e5dfe4a120214cf2b272519bc5fdf28f9f747cb490` |
| `scripts/sparks_exp7_nul_instance_v2.sh` | `efc1cf44f0e2041d8056a3921f831b6cd262741fd2c489941cfd712c7a4556aa` |
| `src/controle_ia/sparks_exp7_nul_v2/__init__.py` | `c5dbe6f12d17d23dee7f347090c15aeb9e139797ae0dadc5d05267ad0f3a5864` |
| `src/controle_ia/sparks_exp7_nul_v2/analyse.py` | `b5531bb8de7558a17142c66d8dab08e97219f88dc0bac7688c9718208c4fb415` |
| `src/controle_ia/sparks_exp7_nul_v2/aveugle.py` | `dbd4e4afb66fe666be60393a1e0c32b4ea37dfd3e34e466e0ae591b9c8b82fb0` |
| `src/controle_ia/sparks_exp7_nul_v2/bac_a_sable.py` | `367269e957e75aedd8838d9542ed50d6fa5aaaaf0110ab8a5bbf1d41e2af6edb` |
| `src/controle_ia/sparks_exp7_nul_v2/bases.py` | `e7bfaf447f5f83348bdaa00d943c422191d7e8e75eb305fa58dc97b5e289e71a` |
| `src/controle_ia/sparks_exp7_nul_v2/causal.py` | `4ff146474ec001192deff1acf23131ccd0dce9b26d13bbd25db04f0367641324` |
| `src/controle_ia/sparks_exp7_nul_v2/comportement.py` | `82c04bf24fee8b7b7157dcb74796233152a5b35bfe85ee2fd71296249188dc66` |
| `src/controle_ia/sparks_exp7_nul_v2/consignes.py` | `e9ebdb74e7adbd575232a49a342fbf87a30a795173a205f4f6aaeb5eb799307e` |
| `src/controle_ia/sparks_exp7_nul_v2/depense.py` | `2d192caa4fcff99b20ae4de44ec3f12f8bece73a850c8380c3414d620ad4daf1` |
| `src/controle_ia/sparks_exp7_nul_v2/garde_code.py` | `daad4a09d8af83741dc8e7aa8d7ec8b3665e4531706a7d24a8386d70179cf98b` |
| `src/controle_ia/sparks_exp7_nul_v2/go.py` | `66d9071c29aa7ff55b96d51abd9e4eba67679f72e9442c8ab4c2416a8f5434ad` |
| `src/controle_ia/sparks_exp7_nul_v2/harnais.py` | `8eeefc874126a59e70dfa9e2b107e181bf65a3857cecd8681edeb2353d0f45b9` |
| `src/controle_ia/sparks_exp7_nul_v2/instance.py` | `c10ca6b5e697bbe84c26b4bca4c366e58f9d8b0e914f32bbce945600aa51d273` |
| `src/controle_ia/sparks_exp7_nul_v2/liste-fermee-v1.txt` | `a486d21194c852dad1cfa9bf54fc53fa33c97587047478fe151c9831f6d85b2a` |
| `src/controle_ia/sparks_exp7_nul_v2/mise_a_disposition.py` | `c9b7d79be53242f0221def37a1aa0989c05603fcfaabf29d2decc367de25440a` |
| `src/controle_ia/sparks_exp7_nul_v2/outil_attention.py` | `2a68db7a216ada82f448cbcd2f0f8d717ae55edb297ace75f20b7b61994249b9` |
| `src/controle_ia/sparks_exp7_nul_v2/plan.py` | `bfa234b014cc63de37b7cc85fa5da3c0b9e56acc1306800f090e3ba901a5c061` |
| `tests/test_sparks_exp7_nul_v2.py` | `95a7bc7ff0cf1e1dc4db9e3d1ee8b5fa3041dd871d149070672d1361adb0720a` |

Usage du dépôt suivi (R12) : paquet neuf `sparks_exp7_nul_v2`, versions neuves des seuls modules changés ; modules
inchangés (recette, jouet, données des auteurs, statistiques) importés de la v1 ; anciens scripts et essais gardés et
toujours joués. Arbre de travail clairsemé `/home/claude/wt/sparks-exp7-nul-v2` (≈ 4 Mo ; un arbre complet ferait
2,4 Go, au-delà de la limite de 2 Go).

## 2. Différence de code, fonction par fonction (tout est neuf ; « v1 » = `sparks_exp7_nul_v1` à `55399606`)

- `plan.py` : réexporte le plan v1 (entropie inchangée, `4bacf20d…`) ; `TACHES_NEUVES` (six clés), `generateurs_neufs()`,
  constantes `COMMIT_BASE`, `CHEMIN_ADDENDUM` (`prereg/SPARKS-EXP7-NUL-addendum-1.md`, nom final supposé), GO, 40 USD.
- `go.py` (bibliothèque standard) : `verifier` exige la première ligne (calcul, 25 USD, Lazar) **et** une extension à
  40 USD ; toute ligne de plus au même identifiant doit suivre R-389 (périmètre « extension… », même type, Lazar, ni
  antérieure ni plus longue), sinon refus ; dates de la première ligne ; révocation.
- `depense.py` (bibliothèque standard) : `projeter`/`exiger` (formule du couple 26 ; pire cas restant : fabrication
  6 h, étape 0 0,5 h, copies × 0,5 h, causal 4 h ou 16 h, état d'égalité inconnu → refus ; stockage jusqu'à la fin du
  18 novembre ; facture si plus grande) ; `duree_max_minutes` (borne de l'amorce) ; `decision_instance` (garder,
  nœud du 16, copier, détruire) ; **`commande_destruction` → `vastai destroy instance <id> -y`** (leçon du jour,
  R-1482 ; identifiant en chiffres seuls, R10 ; aucune sortie brute de `vastai`, R-1480).
- `garde_code.py` (bibliothèque standard) : `verifier_liste_fermee` (`--name-status --no-renames`, égalité stricte
  avec la liste, refus de D, R, C, T) ; `verifier_lancement` (commit lancé descendant du code, rien sous `src/`,
  `tests/`, `scripts/` après lui, addendum présent, compagnon conforme, commit du code cité en entier).
- `bases.py` : `positions` (décalage 1 seulement s'il existe un jeton de début), `b1_tableau` avec l'outil v2 ;
  `arrondi_bf16`, `lire_safetensors` (sans torch) ; `controler` (13 suffixes chez Gemma, ceux du départ au secours ;
  formes égales au départ) ; `distance_depart` (θ_0 arrondi en bf16, float64), `normes_sans_depart`, `scores_poids` ;
  `orientation_b3` (a priori +1, −1 si aire < 0,5, égalité +1 ; seuil ; marque « parfaite », sans arrêt) ;
  `orientation_b4_etalonnage` (descriptif) ; `orientation_b4_test` (D-1 : signe qui maximise l'aire sur le test,
  égalité +1, seuil recalculé sur l'étalonnage avec ce signe) ; `etalonnage_b3_b4`.
- `outil_attention.py` : `jetons_texte` sans préfixe sans jeton de début ; `appeler` comme la v1.
- `comportement.py` : `logp_lot` (lots complétés à droite, masque) ; `mesurer(lots=True)` (même ordre que la v1 : six
  réponses par fait), `lots=False` = mesure v1 ; `egalite_lots` (fractions à 10⁻⁶ ; marges rapportées, non exigées).
- `causal.py` : `architecture`, `formes_attendues`, `verifier_noms` (noms **et formes** ; chez Gemma, formes de
  l'addendum en plus) ; `tranches` pilotées par l'architecture (biais de q dans la tête, biais et normes q/k du bloc
  s'ils existent) ; `modifier`, `ecart_tranches`, `temoin_ampleur`, `unite_causale` recopiés de la v1 avec l'architecture.
- `aveugle.py` : `exiger_coffre`, `ajouter_bases_coffre` (ajout seul, 600, refus hors coffre ou coffre mêlé, seconde
  valeur différente refusée, scores jamais journalisés), `engager_bases`, `ouvrir_coffre` (exige l'empreinte des bases,
  copie scellée `bases-poids-principal-ouvert-v1.json`, puis ouverture v1).
- `mise_a_disposition.py` : `taille_lot`, `lots`, `recevoir_couches_depart` (empreinte, emplacement hors servi, sessions,
  dépôt), `bases_poids_cas` (dossier servi et couches du départ seulement, au coffre, rien rendu) ; commande `servir`
  (service v1, puis bases), commande `lots`.
- `bac_a_sable.py` : `executer` de la v1 avec le prélude en paramètre (chemin et empreinte).
- `consignes.py` : `deriver_principale_v2`, `differences_admises` (ligne à ligne), `format_conversation` (jeton de début
  retiré en tête : lecture retenue), `type_tokeniseur`, `deriver_secours` (quatre substitutions fermées ; prélude porté
  exigé hors du type de Gemma), `eprouver_prelude` (encodage et décodage contre `tokenizers`).
- `harnais.py` : consignes v2 (empreintes figées ; secours par manifeste du portage) ; `valider_composants` (clé de trop
  dans un élément refusée) ; `valider_reponse` → (réponse, statut, erreur) ; `ouvrir`, `tour` (un rappel pour toute
  faute ; « invalide » ou « composants_invalides » ensuite ; `reponse-v2.json`).
- `analyse.py` : `echec`, `probabilites` (composants invalides : probabilités comptées, composants vides),
  `parts_lecteur` (10 % = infractions et « invalide ») ; `rangs` (croissants, moyens), `aire`, `gain`,
  `etat_increment` (préséance de « tenu »), `increment` (rééchantillonnage des 48 cas, permutation des couples entre
  cas, p_perm), `secondaires_increment`, `paires_discordantes` (D-2) ; `scores_b3_b4`, `mesures_base_poids` (table v1
  sur la base seule, générateurs `bases-<b>-…`) ; `lecture_principale` (table de l'addendum), `audit_requis` (deux
  déclencheurs neufs, G_b ≥ 0,20 inchangé, D-4) ; `analyser`.
- `instance.py` : `partages_depart`, `etat_depart_bf16`, `exporter_couches_depart`, `charger_candidat_hf` (révision
  fixée, quatre fichiers, `trust_remote_code` faux ; non joué : aucun réseau), `etape0` (« non mesuré » sans arrêt),
  `bases_etalonnage`, `fabriquer` (v1, puis étape 0, B3 et B4, noms et formes, export ; `fabrication-complement-v2.json`),
  `egalite_lots_jouet`, `causal_instance` (lots ou non, `causal-v2.json`).
- Scripts : amorce v2 (GO v2, garde du code, durée par `depense duree`, clone partiel et clairsemé) ; instance v2 (essais
  v1 et v2, `egalite-lots` → `--sans-lots` déclaré, manifeste avec les six tâches neuves) ; lancer v2 (GO, sceau, code,
  dépense, commande littérale ; destruction `-y`) ; banc v2.
- Consigne principale v2 (deux phrases, aucune autre) ; procédure v2.

## 3. Essais et banc

Rejoués au commit final `50fb15cd` (sorties brutes dans `essais-et-banc-sparks-v2/`, même dossier que ce rapport) :

| Mesure | Compte | Sortie (sha256) |
|---|---|---|
| Essais v1 (`test_sparks_exp7_nul_v1.py`, inchangés) et v2 (`test_sparks_exp7_nul_v2.py`, 45 fonctions, 69 cas) | **159 passés sur 159** (90 + 69), 0 sauté, 0 échec | `essais-sparks-v2-50fb15cd.txt` `5682dfb6…` |
| Banc v2 : 22 mutations du banc v1 (code et essais v1) | **22/22 tuées** | `banc-sparks-v2-50fb15cd.txt` `acac936a…`, `.json` `22c10add…` |
| Banc v2 : mutations neuves (gardes et règles de l'addendum, dont les deux de la destruction `-y`) | **50/50 tuées**, témoins v1 et v2 verts, 0 inapplicable | idem |
| Essai d'égalité des lots sur le jouet (`instance egalite-lots`) | « EGALITE LOTS OK », code 0 | `egalite-lots-jouet.txt` `5aab652a…` |
| Fabrication jouet par module (`instance jouet`) | arrêt gardé, code 3 : « 0/28 modèles dans les bornes (< 90 %) » (modèles jouets de deux époques, même issue qu'en v1 ; la garde d'arrêt joue, aucun repli) | `instance-jouet.txt` `9d3324f2…`, `instance-jouet-err-sans-progres.txt` `52fbe690…` |

Historique, pour mémoire (R4 : tout run compté) : au commit `ee91412d`, banc 22/22 et **49/50** — une survivante,
« prélude : encodage non comparé » (l'essai de l'épreuve du prélude n'avait pas d'artefact d'encodage) ; corrigée au
commit `50fb15cd` par un artefact (prélude dont les fusions sont ignorées : refus « encodage ») ; sorties
`banc-sparks-v2-ee91412d.txt` `b5fc4f9a…` et `.json` `c4d5be1b…`, essais `essais-sparks-v2-ee91412d.txt` `b34aa532…`
(159/159). Deux runs incomplets, non comptés comme résultats et gardés au bloc-notes : un passage des essais tué par
le noyau (mémoire, pendant le clone de la section 4) et un banc aux témoins rouges lancé au même moment, arrêté par
son identifiant de processus puis relancé en entier ; un banc interrompu par le redémarrage du conteneur (39 tuées sur
41 lignes, aucune survivante), relancé en entier.

## 4. Scripts d'instance en `MODE=jouet` : non joués de bout en bout (réserve)

Les scripts clonent le dépôt au commit lancé. Un arbre complet fait 2,4 Go (au-delà de la limite de 2 Go) ; les scripts
v2 font donc un clone partiel et clairsemé. Le dépôt local est superficiel (`.git/shallow`) : un clone nu `--shared`
s'est mis à recopier tous les objets (arrêté par son identifiant de processus, nettoyé) ; un dépôt nu à alternats
(136 Ko) a été fait, mais le clone partiel en transport local n'a pas fini en 600 s (arrêté). Joué à la place :
`bash -n` des trois scripts ; les gardes appelées par les scripts, chacune par ses essais (GO, code, dépense) ;
`instance egalite-lots` et `instance jouet` par module (section 3). **À faire avant le scellement**, sur
une machine où le clone tient : le lancement jouet complet (amorce → instance) contre un dépôt nu local.

## 5. Lectures retenues et écarts à signaler (aucune n'est dans le brouillon 2 ; à reporter au brouillon 3)

1. Leçon du jour (consigne de la mère, après le brouillon 2) : destruction par `vastai destroy instance <id> -y`
   (R-1482) et aucune sortie brute de `vastai` (R-1480) : dans le code, la procédure et le lanceur ; **à ajouter à la
   ligne de destruction de la liste d'arrêt et à la liste de code au brouillon 3** (le brouillon 2 n'est pas réécrit, R12).
2. Le rappel de forme sert aussi pour une faute des seuls composants (le texte dit « un rappel », sans le restreindre).
3. Une clé de trop dans un élément de composant est désormais « composants invalides » (la v1 l'admettait) : couple 12.
4. o₄ fixé une fois, non recalculé dans les tirages (écrit au brouillon 2, D-1) ; seuil de B4 recalculé avec o₄.
5. Secondaires de l'incrément tirés sur les générateurs `increment-<b>-…` après le principal (ordre écrit en tête
   d'`analyse.py`), sans clé de tâche neuve.
6. Format de conversation du secours : jeton de début retiré en tête de la sortie de `apply_chat_template`.
7. Égalité des lots : fractions à 10⁻⁶ ; marges (sommes de log-probabilités) non exigées ; parts rouvertes et décisions
   « porteur » égales vérifiées par l'essai d'unité causale.
8. `CHEMIN_ADDENDUM` = `prereg/SPARKS-EXP7-NUL-addendum-1.md` (nom au scellement supposé, R-021) : à confirmer.
9. Clone partiel et clairsemé dans les scripts (nouveau par rapport à la v1) ; vérifier sur l'image de l'instance que
   `git` accepte `--filter=blob:none` et `sparse-checkout --no-cone`.
10. `liste-fermee-v1.txt` compte les compagnons `.sha256` ; la garde exige l'égalité exacte (un fichier changé non listé,
    ou listé non changé, refuse).

## 6. Dix points pour un contre-lecteur neuf du delta de code (le premier d'abord)

1. `analyse.increment` et `etat_increment` : rangs croissants recalculés dans chaque tirage, tirage des 48 cas (A et B
   ensemble), permutation des couples A sur A, p_perm, préséance de « tenu », marque de plafond.
2. `analyse.scores_b3_b4` et `bases.orientation_b4_test` : passage des noms servis aux modèles par la clé ouverte ; o₃ de
   l'étalonnage, o₄ du test (D-1) ; aire de B3 « sur l'étalonnage » comparée orientée au déclencheur d'audit.
3. `analyse.lecture_principale` contre la table gelée du brouillon 2 (lignes, « non concluant » si plusieurs).
4. `analyse.probabilites`, `echec`, `parts_lecteur` : « composants_invalides » ni échec, ni dans les 10 %.
5. `harnais.valider_reponse` et `tour` : frontière bloc (invalide) / éléments (composants invalides), rappel unique.
6. `mise_a_disposition.bases_poids_cas` et `aveugle.ajouter_bases_coffre` : aucune lecture de la clé, aucun score
   imprimé ni journalisé, refus hors du coffre ; `ouvrir_coffre` exige l'empreinte engagée.
7. `go.verifier` contre R-389 et `.claude/hooks/garde_calcul.py` ; `depense.projeter` contre le couple 26 (heures du
   devis, échéance de fin du 18) ; `commande_destruction` (`-y`).
8. `garde_code` : égalité stricte de la liste ; contrôle « code inchangé après le commit du code » ; sceau de l'addendum.
9. `comportement.logp_lot` (alignement des positions avec le complément à droite) et `causal.tranches` génériques.
10. Ce qui n'a pas tourné : scripts d'instance de bout en bout en `MODE=jouet` (section 4), `charger_candidat_hf`,
    portage réel au secours (aucun réseau) ; essai d'isolement du bac lancé sur cette machine seulement.

## 7. Ce qui reste à la mère avant le scellement

Contre-lecture du delta de code par un sous-agent neuf ; lancement jouet complet des scripts ; brouillon 3 : commit
final, liste fermée et empreintes, comptes (section 3), lignes de la leçon `-y` et de la sortie brute de `vastai` ;
scellement ; empreintes compagnons des fichiers de `main` listés en section 1.
