# Orchestrateur du pôle, version 0.7.0 — v42 : réponse courte à la contre-lecture CL8 de la v41 (« non lançable en l'état ») — LISEZMOI v42

Lignée conv-audit (instance de reprise, Opus 5.5), écrit après le relevé `date -u` de **05:03 UTC** le 29 octobre 2026 (travail
commencé à 04:27 UTC) ; v1 à v41 gardées (R12). Répond à la contre-lecture CL8 de la v41 (Opus 5.5,
`contre-lecture-v41-cl8.md` : aucun bloquant de sécurité, CL41-01 majeur et régression, CL41-02 et 03 majeurs à confirmer
sur Argon réel, CL41-04 à 08 mineurs, 12 défauts réintroduits survivants) dans le périmètre de la v42 courte demandée par
session-depot (message n° 151), **choix fixés par session-depot** : CL41-01 en option (B). **CL40-01 reste une décision de
Lazar** : politique inchangée, `relancable` toujours calculé. **v42 n'est pas contre-lue.**

| constat | correction | essai qui le démontre (échoue sur la v41, passe sur la v42) |
|---|---|---|
| **CL41-01** contrôle du bras à la consigne du juge sous 0,2 (régression) | option (B) : le contrôle du bras redevient **court** (`supplement=None`, 41 caractères : il éprouve la commande) ; **garde de taille sans dépense** avant tout appel, course et bras : `--taille-max-consigne-externe` (cœur : `taille_max_consigne_externe`), défaut = plafond de la session qui reçoit la plus grosse consigne / prix prudent d'un caractère (voir plus bas) ; refus scellé (`SORTIE-controle/refus-taille-K.json`, `manifeste-bras-refus-taille-K.json`), rien payé, aucune tentative comptée ; le bras sans l'option reprend la valeur donnée à la course ; `--budget-externe-usd` **transmis au bras** s'il est donné (sinon le plafond du manifeste de départ), vérifié fini ≥ 0 ; **classement « sans juge externe » écrit dès qu'une tentative du bras est scellée non relançable** (payée ou non jouée), sans verrou (un plafond relevé par Lazar peut encore relancer), `SansJugeExterne`, code 5 | `TestV42.test_cl41_01_consigne_du_juge_de_243000_au_bareme_haut` (consigne du juge de 244 673 caractères, Argon factice au barème haut sans borne : contrôle court 0,10, juge 0,91, **classement à trois juges** ; v41 : contrôle 0,93 refusé, aucun classement ; variante : garde donnée à 100 000, puis par défaut sur un juge à 0,5, puis donnée à la course → refus avant tout appel, Argon jamais appelé, puis le bras se joue en tentative 1) ; `test_cl41_01_plafond_externe_donne_au_bras_et_classement_si_non_relancable` ; `test_cl41_01_classement_apres_le_dernier_bras_non_joue` ; `test_cl41_01_garde_de_taille_de_la_course_avant_tout_controle` |
| **CL41-02** contrôle d'Argon de la course ≈ 1,46 million de caractères | fiche **bornée au gabarit** : `questions_servies` ≤ 9, `anteriorite` ≤ 12, tailles par champ inchangées (3 000, nom 200, question 80, référence 500) **et** fiche servie ≤ **12 000 caractères** (`TAILLE_MAX_FICHE_SERVIE`, JSON tel que servi en passe 2, échappements compris ; une fiche plus longue est refusée seule, motif dans `fiches-refusees.json`) ; bornes dites aux proposeurs dans la consigne ; `fiche_maximale` = le maximum de ce gabarit borné (12 000 caractères servis, listes à leur borne) ; ordre « passe 2 d'Argon juste après sa passe 1 » gardé ; tailles écrites au manifeste de départ (`versions.marge_controle_externe`, `taille_fiche_maximale_servie`) et au journal (`marge_seconde_passe`) | `TestV42.test_cl41_02_fiche_bornee_et_marge_realiste` (10 questions, 13 antériorités, fiche de guillemets échappés, fiche de 12 000 + refusées ; passe 2 réelle d'Argon à huit fiches maximales ≤ consigne éprouvée ; tailles au manifeste et au journal) |
| **CL41-03** contrôles d'Argon qui finissent par les instructions de la tâche | `consigne_de_controle` : matériau entre les lignes `<<<<< DÉBUT DU MATÉRIAU DE TAILLE >>>>>` et `<<<<< FIN DU MATÉRIAU DE TAILLE >>>>>`, présenté comme non-consigne, et la consigne **se termine** par « Fin du matériau. Réponds exactement OK, sans rien d'autre. » ; au bras, le contrôle est court (il finit par « Réponds exactement OK, sans rien d'autre. ») | `TestV42.test_cl41_03_et_n13_consigne_de_controle_recue_par_la_commande` (ce que **reçoit la commande**, course et bras) |
| **CL41-07** contrôles Claude avant celui d'Argon | contrôle d'Argon **joué en premier**, puis les contrôles Claude | `TestV42.test_cl41_07_panne_d_argon_au_controle_ne_coute_rien_chez_claude` (réglages du devis, Argon « KO » à 0,15 : aucun contrôle Claude, tentative 0 côté Claude, relançable, la relance part ; v41 : 0,4 Claude, plus de relance) |
| **CL41-04** message « avant tout envoi des fiches » faux | redevient vrai (contrôle court) ; en plus, un contrôle du bras **non court** (il a pu recevoir les fiches) qui ne rend pas « OK » verrouille le bras comme un envoi : manifeste du bras, classement sans bras, aucune tentative relançable | `TestV42.test_cl41_04_controle_non_court_refuse_verrouille_le_bras` (contrôle court refusé : la commande n'a reçu que 41 caractères, message vrai ; contrôle long simulé qui rend des notes : verrouillé ; v41 : « relance permise ») |
| **CL41-06** interruption entre la création de SORTIE et le manifeste de départ | le cœur écrit le manifeste de départ dans un dossier provisoire (`SORTIE.depart-en-cours-…`) puis le **renomme** en SORTIE ; sur toute exception avant le renommage, le dossier provisoire est retiré ; au lanceur, une SORTIE sans manifeste de départ rend `relancable` faux, motif nommé | `TestV42.test_cl41_06_interruption_avant_le_manifeste_de_depart` (même coupure que `lanceur_fenetre.py` de CL8 : aucune SORTIE, tentative relançable, la relance passe ; v41 : relance refusée « SORTIE existe déjà » ; et SORTIE créée sans manifeste → `relancable` faux) |
| **CL41-05** `relancable` suppose un relais gardé | `relancable` reste calculé dans l'hypothèse « relais gardé », **écrite au motif** ; second calcul « relais relancé à neuf » (dépense 0, devis point 4) écrit à côté (`relance_relais_relance_a_neuf` dans `tentative-N.json` et imprimé), nommé au motif quand il dit la relance possible | `TestV42.test_cl41_05_relancable_relais_garde_et_relance_a_neuf` (sonde de CL8 : 36,6 < 37 relais gardé, 37 ≥ 37 à neuf) |
| **CL41-08** trous d'essais | un essai par trou | N03 : `test_n03_meme_controle_du_bras_au_lanceur_et_au_coeur` ; N04, N07, N08 : `test_n04_n07_n08_couts_des_tentatives_precedentes` (relance sous un total externe juste refusée avant tout contrôle ; `cout_deja_engage_usd` et `cout_externe_deja_engage_usd` lus au manifeste de départ et au journal) ; N13 : `test_cl41_03_et_n13_…` ; V12 : `test_v12_relancable_avec_le_cout_externe_de_la_tentative` ; V34 : `test_v34_relais_lu_avec_le_cout_claude_de_la_tentative` ; V20 : `test_v20_tentative_du_bras_scellee_au_cout_non_fini` ; V36 : `test_v36_listes_comptees_dans_fiche_maximale`. Le code de la v41 était juste à ces endroits : ces essais **passent sur la v41** et **tuent** les défauts réintroduits (ci-dessous) |
| **CL40-01** politique de relance | inchangée (décision de Lazar) ; `relancable` calculé | — |

**Garde de taille : valeur prise.** Prix prudent d'un caractère d'entrée = barème le plus haut du code
(`relais_reel.BAREME_INCONNU`, 10 dollars par million de jetons d'entrée, celui que le code applique à un modèle inconnu)
à 4 caractères par jeton, entrée seule (le contrôle rend « OK ») : **2,5 × 10⁻⁶ dollar par caractère**
(`idn.PRIX_CARACTERE_PRUDENT_USD`). Défaut : plafond de la session qui reçoit la plus grosse consigne / ce prix — course :
contrôle d'Argon 2,5 → **1 000 000 caractères** ; bras : juge d'Argon 3,5 → **1 400 000 caractères**. Au-delà, à ce barème,
cette session dépasserait son plafond sur la seule entrée. (À 3 caractères par jeton : 750 000 ; au taux implicite du devis,
2,5 pour 1,1 million : 1 100 000.)

**Taille et coût du contrôle d'Argon de la course aux réglages du devis** (pièces 750 000 + matériau 350 000, huit fiches,
seconde passe ; `sonde_tailles.py` de CL8, appel direct) :

| | v41 | v42 |
|---|---|---|
| fiche de la marge (JSON servi) | 44 163 | 12 000 |
| consigne de contrôle | **1 456 740** | **1 199 154** |
| coût au taux du devis (2,5 / 1,1 million) | 3,31 | **2,73** |
| coût au barème du code, 4 caractères par jeton ; 3 + 2 000 en sortie | 3,64 ; 4,96 | 3,00 ; 4,10 |
| pièces et matériau au maximum (750 000 + 750 000) | 1 856 735 | 1 599 149 |
| pièces et matériau de 2 000 (S1) | 360 737 | 103 151 |

Pièces et matériau font à eux seuls 1,1 million de caractères, soit 2,5 au taux du devis : toute marge de fiches dépasse
2,5. **Aux réglages du devis v7 quinquies, la garde par défaut refuse** (1 199 154 > 1 000 000), avant tout contrôle, rien
payé : il faut, au devis v7 sexies, soit `--budget-controle-externe-usd 3.0` (garde à 1 200 000 ; somme externe alors
3,0 + 2 × 2,5 + 3,5 + 0,2 = 11,7), soit `--taille-max-consigne-externe` donné après confirmation du barème d'Argon.

**Défauts réintroduits (ma vérification, sur copies hors de P, `mutations_v42.py` dans mon brouillon)** : 25 — les neuf trous
de CL41-08 réexprimés sur la v42 (N03, N04, N07, N08, N13, V12, V20, V34, V36) et seize sur les corrections de la v42
(contrôle du bras long, garde absente ou toujours passante côté course et côté bras, plafond externe non transmis,
classement absent après une tentative payée ou non jouée non relançable, bornes de la fiche retirées une à une, phrase
finale du contrôle retirée, Claude contrôlé avant Argon, contrôle non court non verrouillé, relais à neuf non calculé,
SORTIE sans manifeste relançable, dossier provisoire laissé) : **25 tués** (premier passage par les modules
`test_v7_ideation` et `test_adaptateurs` ; le seul survivant de ce passage, classement après le dernier bras non joué, a
reçu son essai et est tué sur la suite entière).

**Rejoué avec les outils de CL8** (`scenarios_cl8.py`, `lanceur_pire.py`, `argon_factice.py`, `scenario_fenetre.py`, sur
l'arbre v42, Argon factice local) :

| scénario | v42 |
|---|---|
| S1 pire cas, réglages du devis | course code 0 ; Claude **40,00** (8 sessions) ; Argon course 7,5 ; bras 3,7 (contrôle **41 caractères** à 0,2 + juge 3,5) ; **Argon 11,2** ; classement à trois juges ; contrôle d'Argon **103 167** caractères (v41 : 360 753) |
| S2 Argon « KO » au contrôle (0,15), contrôles Claude à 0,2, 0,01, 0 | **Claude 0** dans les trois cas (Argon d'abord) ; tentatives 1 et 2 relançables (11,35 ; 11,5 ≤ 11,6), la troisième non (« 3 tentatives », 11,65) ; quatrième refusée sans rappeler Argon. Argon cassé sans coût lisible : 2,5 comptés, Claude 0, non relançable (13,7 > 11,6) |
| S5b listes de 60 éléments | fiches d'Argon refusées (questions > 9, motif scellé) ; passe 2 réelle **42 623 ≤ contrôle 139 167** ; (a) casse sous le contrôle : refus au contrôle d'Argon, **Claude 0** (v41 : 0,4), 2,5 comptés ; (b) aucune taille entre le contrôle et la passe 2 ne casse : course complète |
| S10-grand consigne du juge de 244 673 caractères, barème haut | contrôle court 41 caractères à 0,0001 (4 caractères par jeton) et 0,100 (3 + 2 000) ; juge joué au plafond 3,5 ; **classement à trois juges** dans les deux barèmes ; Argon 11,0 et 11,1 (v41 : refusé, aucun classement) |
| S11 contrôle du bras qui rend des notes | n'a plus d'objet : le contrôle court ne porte aucune fiche ; l'Argon factice en mode « notes » plante sur la consigne courte (sortie ≠ 0, plafond 0,2 compté), tentative relançable, puis le bras normal écrit le classement à trois juges. Le cas d'un contrôle long qui rend des notes est couvert par l'essai CL41-04 |
| S12 interruption entre SORTIE et manifeste de départ | essai 1 : code 2, **aucune SORTIE**, tentative-1 relançable ; essai 2 : **code 0**, course complète (v41 : « SORTIE existe déjà ») |

## Restes déclarés

- **Devis** : aux réglages du devis v7 quinquies, la garde de taille refuse par défaut la course (ci-dessus) — c'est voulu
  (au barème prudent du code, le contrôle d'Argon dépasserait son plafond de 2,5), mais le lancement exige un chiffre du
  devis v7 sexies : plafond du contrôle d'Argon (≈ 3,0, somme externe 11,7) ou taille donnée sur le barème réel d'Argon.
- **CL40-01** (décision de Lazar) : politique inchangée. Effet de CL41-07 : une panne d'Argon au contrôle ne coûte plus
  rien chez Claude, et la relance redevient permise aux réglages du devis tant que la somme externe tient (S2).
- **Risque de taille du juge** (choix B) : il tombe désormais sur la session du juge (3,5 comptés, bras verrouillé,
  classement sans bras écrit) ; la garde du bras le borne d'avance à 1 400 000 caractères (entrée seule ; la sortie du
  juge n'est pas comptée). La plus grosse consigne de juge que le gabarit borné permet (52 fiches de 12 000 et pièces de
  juge de 750 000) fait ≈ 1,38 million de caractères, sous cette garde.
- **Fiche bornée à 12 000 caractères servis** : règle neuve de validation (une fiche plus longue est refusée seule) ; la
  valeur (plus du double des fiches réelles de 3 000 à 5 000 caractères relevées par CL8) est à confirmer au devis.
- **Classement sans bras sans verrou** : si un bras jugé non relançable est ensuite relancé sur mot de Lazar (plafond
  relevé) et réussit, `classement-sans-bras.json` et `classement.json` coexistent ; le second fait foi.
- Arrêt brutal (SIGKILL, coupure) entre la création du dossier provisoire et son renommage : le dossier
  `SORTIE.depart-en-cours-…` reste (rien n'y a été dépensé), SORTIE est absente, la relance passe ; si SORTIE apparaît
  entre la vérification et le renommage (vide), Linux la remplace (course concurrente sur la même SORTIE, non traitée).
- La garde compte des caractères, pas des jetons ni des octets ; le barème réel d'Argon, sa limite de taille et son
  comportement devant la consigne de contrôle neuve ne sont pas vérifiés (comme CL8, § 7).
- Non vérifié : vraie commande d'Argon, kit réel sous SIGTERM, relais réel. M28, N28 et V27 (déclarés incertain,
  équivalent, presque équivalent par CL8) ne sont pas repris.

**Essais** : trois essais de la v41 changés par les choix de la v42, chacun dit dans sa docstring —
`TestV41.test_controle_du_bras_porte_la_consigne_du_juge` (**inversé** par l'option B : le contrôle reçu est court) ;
`test_controle_a_la_taille_reelle_de_la_passe_2_et_ordre_d_argon` (fiche maximale de 12 000 au lieu de « > 13 × 3 000 » ; la
grosse fiche d'Argon a trois champs de 3 000 au lieu de quatre, pour tenir sous la borne) ;
`test_relancable_calcule_avec_un_controle_claude_paye` (Argon contrôlé d'abord à 0,15 ; l'échec vient du second contrôle
Claude, payé, au lieu d'Argon « KO » après les contrôles Claude ; mêmes sommes 40,02 et 40,40, mêmes conclusions).

**396 essais passent** (396 = 380 + 16 : `TestV42` dans `test_v7_ideation`) ; trois exécutions complètes, 172 s (395 essais, avant le seizième), 170 s et 176 s (396),
aucun essai instable, aucun processus survivant (`ps`), `essais/_tmp` retiré, aucun `__pycache__` réécrit.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v42.txt
```
