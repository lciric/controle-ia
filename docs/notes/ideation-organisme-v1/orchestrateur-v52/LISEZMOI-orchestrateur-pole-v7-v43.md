# Orchestrateur du pôle, version 0.7.0 — v43 : réponse courte à la contre-lecture CL9 de la v42 — LISEZMOI v43

Lignée conv-audit (instance de reprise, Opus 5.5), écrit après le relevé `date -u` de **07:12 UTC** le 29 octobre 2026 (travail
commencé à 06:13 UTC) ; v1 à v42 gardées (R12). Répond à la contre-lecture CL9 de la v42 (Opus 5.5,
`contre-lecture-v42-cl9.md` : aucun bloquant de sécurité ni de dépense hors plafond total ; CL42-01 majeur, option (a) du
devis v7 sexies non lançable ; CL42-02 majeur pour le devis ; CL42-04 majeur, protocole ; CL42-03, 05, 06, 07 mineurs ; 10
défauts réintroduits survivants), dans le périmètre de la v43 courte demandée par session-depot (message n° 156, **choix
fixés**), complété en cours de travail par **deux décisions de Lazar relayées par session-depot** : CL40-01 → option (c)
(ne pas rejouer à la relance les contrôles déjà réussis) ; CL42-04 → « retirer » la borne de 12 000 caractères par fiche.
CL42-02 est une affaire de devis (aucun code). **Un point de la seconde décision n'est pas appliqué tel quel** (la provision
de sortie à huit fiches maximales : elle annule la garde ; voir plus bas). **v43 n'est pas contre-lue.**

| constat | correction | essai qui le démontre (`TestV43`, échoue sur la v42, passe sur la v43, sauf mention) |
|---|---|---|
| **CL42-01** garde de la course réglée sur le seul contrôle d'Argon ; la passe 2 (plafond 2,5) non couverte | garde par défaut = **plus petit plafond des sessions d'Argon qui reçoivent sa plus grosse consigne** : contrôle (entrée seule, il rend « OK ») et passe (plafond `proposeur_ideation` d'Argon, 2,5, **moins la provision de sortie** : `--nombre` fiches de 12 000 caractères au rapport sortie/entrée 5 du barème du code) — `idn.taille_max_consigne_course_par_defaut`, `provision_sortie_caracteres` ; **520 000 caractères** au prix prudent, et toujours 520 000 avec `--budget-controle-externe-usd 3.0` seul ; en plus, le cœur **garde chaque passe d'Argon sur sa consigne réelle avant son envoi** (`garder_sessions_externes`, toujours donné par le lanceur) contre la taille donnée (`--taille-max-consigne-externe`) ou, sinon, contre son propre plafond moins la provision ; refus sans envoi, manifeste de fin scellé en erreur, gardes au journal (`gardes_taille_sessions`) | `test_cl42_01_controle_releve_seul_refuse_sans_depense_et_garde_donnee_passe` (pièce de 750 000, matériau de 350 000, Argon au tarif du devis : refus scellé, garde 520 000, ni Argon ni Claude appelés ; v42 : contrôle 2,725, passe 1 1,71, passe 2 2,511 > 2,5, course perdue ; au prix 8,3 : garde 724 819, refus aussi ; cas sain : `--taille-max-consigne-externe 1500000`, Argon au pire cas, course et bras passent, classement à trois juges, les deux passes gardées à 1 500 000) ; `test_cl42_01_passe_gardee_contre_son_propre_plafond_avant_envoi` (plafond qui tient la passe 1 et pas la passe 2 : passe 2 jamais envoyée, aucune passe Claude, 0,1 compté ; cas sain à 2,5 : deux gardes à 520 000) |
| **CL42-05** sous (c), le bras reprend la taille de la course ; un refus de taille au bras ne compte rien et n'écrit aucun classement ; W07 | option propre au bras `--taille-max-consigne-externe-bras` ; **défaut : plafond du juge / prix moins une provision de sortie par fiche servie** (2 000 caractères de note au rapport 5, `provision_sortie_juge_caracteres` : voir plus bas) ; **la valeur de la course ne s'applique plus au bras** (`--taille-max-consigne-externe` donné au bras : refusé par l'analyseur, code 2) ; un refus de taille au bras **compte une tentative non relançable** (`manifeste-bras-refus-taille-N.json`, N = numéro de tentative, `tentative_comptee` vrai, `relancable` faux, rien payé), écrit le classement sans bras et lève `SansJugeExterne` (code 5) | `test_cl42_05_garde_du_bras_de_bout_en_bout_par_le_lanceur` (chaîne lanceur → manifeste → bras : course avec `--taille-max-consigne-externe 150000`, consigné « option » ; bras sans option sur une consigne de juge de ≈ 210 000 caractères : garde par défaut du bras, classement à trois juges ; v42 : refus « donnée à la course » ; avec `--taille-max-consigne-externe-bras 1000` : code 5, refus compté, classement sans bras, Argon jamais appelé ; relance sans option en tentative 2) |
| **CL42-06** échec du classement de repli silencieux (S14) ; W36 | `repli_impossible` : l'échec est **scellé** (`classement-sans-bras-impossible-N.json`, champ `classement_sans_bras_impossible`) et **dit dans l'exception levée** (au lanceur, sur la sortie d'erreur, clé `classement_sans_bras_impossible`) ; même chose après envoi (manifeste du bras, exception) ; un classement de repli déjà écrit n'est jamais réécrit et l'exception le dit (« déjà écrit par une tentative précédente : non réécrit (R12) ») | `test_cl42_06_echec_du_classement_de_repli_dit_et_scelle` (S14 par le lanceur : troisième bras non joué, `_classer` qui lève → code 2, motif sur la sortie d'erreur, fichier scellé ; v42 : rien ; après envoi : verrouillé, scellé, dit) ; `test_cl42_06_w36_deux_tentatives_non_relancables_sans_ecrasement` (refus de taille puis contrôle « KO » payé 0,9 qui épuise le plafond : second repli joué, classement inchangé, refus d'écrasement dit) |
| **CL42-07** W30, W35b ; refus pour taille par proposeur | essais ; **refus pour taille comptés par proposeur et par passe** (`FicheTropLongue` : un champ trop long, une liste au-delà de sa borne ; `refus_pour_taille_par_proposeur` au journal et au manifeste de fin) | `test_cl42_07_w30_plafond_externe_non_fini_au_bras_sur_sortie_fraiche` (NaN, +∞, −1, `True` sur une SORTIE fraîche, cœur et lanceur : refus avant tout appel, aucun fichier du bras ; **passe sur la v42**, dont le code était juste, et tue W30) ; W35b : remplacé, voir CL42-04 |
| **CL42-04** (décision de Lazar : « **retirer** ») borne de 12 000 caractères par fiche | **plus de borne sur la fiche entière** : seules restent les bornes par champ (3 000 ; nom 200 ; question 80 ; référence 500) et de listes (9 questions, 12 antériorités) ; la phrase « 12000 caractères au plus par fiche » est retirée de la consigne ; `fiche_maximale()` redevient le pire cas aux bornes par champ (**44 259** caractères servis) et la marge du contrôle de la course = `--nombre` × `fiche_maximale()` ; **prix de la garde réglable** : `--prix-entree-usd-par-million-jetons` (défaut 10,0, le barème prudent du code ; 4 caractères par jeton ; devis : 8,3) pour la course, les passes et le bras ; la passe 2 reste gardée sur sa consigne réelle avant envoi (ci-dessus) | `test_cl42_04_borne_de_fiche_retiree_et_refus_pour_taille_par_proposeur` (la phrase n'y est plus, consigne construite et reçue par Argon ; une fiche de 44 259 caractères aux champs dans leurs bornes est admise ; refus pour taille Argon 2, Opus 1, Fable 0 ; v42 : phrase présente, fiche refusée, aucun compte) ; prix : `test_cl42_01_…` (garde 724 819 à 8,3 ; prix 0, NaN, −1 refusés) et `test_cl42_03_…` |
| **CL40-01** (décision de Lazar : option **c**) relance après une tentative scellée | les contrôles **réussis** (statut ok, « OK », aucun problème) scellés dans `tentative-N.json` ne sont **pas rejoués** : clé = rôle, modèle, empreinte de la consigne de contrôle, identité de ce qui le joue (commande externe et empreintes de ses fichiers, ou moteur et adresse du relais) ; seuls les contrôles échoués ou non faits sont (re)payés ; `relancable` compte les coûts imputés, les plafonds des seuls contrôles à refaire et les sessions (`controles_a_refaire`, `sommes_de_la_relance_hors_cette_tentative`) ; manifeste de départ (`versions.controles_repris`), journal du cœur (`controles_repris`) et tentative suivante disent quels contrôles sont repris (numéro de tentative, empreinte du fichier scellé, empreinte de la consigne, coût déjà imputé) | `test_cl40_01_c_relance_sans_rejouer_les_controles_reussis` (contrôles Claude payés 0,2 et réussis, Argon « OK », panne du cœur → tentative 1 relançable, 40,0 ≤ 40 ; v42 : 40,4, non relançable ; tentative 2, autre commande d'Argon « KO » : Argon rejoué, Claude jamais rappelé ; tentative 3 : **seul Argon repayé**, aucun contrôle Claude rejoué, coûts imputés Claude 0,4, Argon 0,15 + 0,15 + 2,5, reprises écrites au manifeste et au journal) |
| **CL42-03** mesurer la consigne avec les vrais fichiers avant le GO | `--mesurer-consignes` (lanceur) et `idn.mesurer_consignes` : tailles réelles des consignes de passe 1, passe 2 maximale, contrôle d'Argon, juge au maximum, contrôle du bras ; coûts d'entrée au prix donné ; gardes de la course et du bras ; figures de la provision demandée et non appliquée ; **aucun appel, aucun adaptateur construit, aucun fichier** (SORTIE n'est pas créée), code 0 ; pièce refusée : code 2 | `test_cl42_03_mesurer_consignes_sans_appel` (adaptateurs piégés, commande jamais lancée, même avec `--moteur claude-sdk` non armé ; contrôle mesuré = celui que reçoit Argon dans la course lancée ensuite ; juge réel sous le maximum mesuré ; prix 8,3 : garde 724 819 ; v42 : option inconnue) |
| CL42-02 option (b) refusée par la garde | aucun code (devis) | — |

**Gardes de taille : valeurs prises.** Prix d'un caractère d'entrée = `--prix-entree-usd-par-million-jetons` / 10⁶ / 4
(défaut 10,0 → 2,5 × 10⁻⁶ ; 8,3 → 2,075 × 10⁻⁶) ; rapport sortie/entrée : 5 (`BAREME_INCONNU`, 50 / 10).
- **Course** : `min(plafond du contrôle / prix ; plafond de la passe / prix − provision)`, provision = `--nombre` × 12 000 × 5
  = **480 000** caractères pour huit fiches. À 10 : min(1 000 000 ; 520 000) = **520 000** ; à 8,3 : min(1 204 819 ;
  724 819) = **724 819**. La provision n'est déduite que de la passe (le contrôle rend « OK ») ; quand les deux plafonds
  valent 2,5, cela revient au calcul « plus petit plafond moins la provision ».
- **Passes d'Argon dans le cœur** : taille donnée, sinon plafond de la passe / prix − 480 000.
- **Bras** : plafond du juge / prix − fiches servies × 2 000 × 5 (`PROVISION_SORTIE_PAR_NOTE`, convention) : 3,5 et 52 fiches
  → **880 000** à 10, **1 166 746** à 8,3. La provision de la course appliquée au juge (1,2 dollar) annulerait la garde de
  tout juge sous 1,2 dollar (onze essais anciens, juge à 1,0) et ne suit pas le nombre de notes.
- **Provision demandée avec CL42-04 et non appliquée** : « sortie au rapport 5, huit fiches à `fiche_maximale()` » =
  8 × 44 259 × 5 = **1 770 360** caractères équivalents, soit **4,43 dollars à 10 et 3,67 à 8,3** : plus que le plafond
  2,5 d'une passe d'Argon. La garde par défaut vaudrait **0 aux deux prix** : toute course avec Argon serait refusée par
  défaut, et la garde de la passe 2 sur son propre plafond refuserait toujours (et la plupart des essais du lanceur avec
  Argon tomberaient). Je garde la provision de huit fiches de 12 000 (`PROVISION_SORTIE_PAR_FICHE`, l'ancienne borne gardée
  comme taille provisionnée, plus du double des fiches réelles relevées par CL8) en attendant le choix de Lazar : (i) la
  provision demandée, avec des plafonds de passe d'Argon d'au moins ≈ 4,4 dollars plus l'entrée (dépense) ; (ii) une
  taille de fiche provisionnée fixée au devis ; (iii) la garde donnée (`--taille-max-consigne-externe`). `--mesurer-consignes`
  rapporte les deux.

**Tailles réelles aux réglages du devis** (`--mesurer-consignes`, pièce de 750 000, matériau de 350 000, question de 19,
huit fiches à `fiche_maximale()`, seconde passe, Argon proposeur et juge, témoins des scénarios de CL9) :

| consigne | caractères | coût d'entrée à 10 / à 8,3 | garde par défaut à 10 / à 8,3 | passe ? |
|---|---|---|---|---|
| passe 1 d'Argon | 752 440 | 1,881 / 1,561 | — | — |
| passe 2 maximale (huit fiches de 44 259) | 1 456 692 | 3,642 / 3,023 | 520 000 / 724 819 (cœur) | non |
| **contrôle d'Argon (course)** | **1 457 167** | **3,643 / 3,024** | **520 000 / 724 819** | **non** (provision demandée : garde 0 / 0) |
| juge au maximum (52 fiches de 44 259, sans pièce de juge) | 2 131 096 | 5,328 / 4,422 | 880 000 / 1 166 746 | non |
| contrôle du bras | 41 | — | — | — |

Au barème du devis (8,3), le contrôle d'Argon dépasse à lui seul le plafond 2,5 de sa session (3,02) : quelle que soit la
garde, la course aux réglages du devis exige un plafond du contrôle d'Argon d'au moins ≈ 3,03 dollars (dépense neuve, mot de
Lazar), et la passe 2 au maximum du gabarit autant plus sa sortie.

**Rejoué avec les outils de CL9** (`scenarios_cl9.py`, `argon_factice_cl9.py`, `lanceur_pire.py`, `sonde_repli_silencieux.py`,
`mutations_cl9.py`, lancés par `python3 -I -B` hors de P, environnement propre, sur une copie de l'arbre v43 ; Argon factice
local ; variantes par `scenario_c_variante.py`, dans mon brouillon) :

| scénario | v42 (CL9) | v43 |
|---|---|---|
| **D-a-devis** (`--budget-controle-externe-usd 3.0 --budget-externe-usd 12.1`, tarif du devis) | contrôle 2,725, passe 1 1,710, passe 2 2,510 > 2,5 ; Claude 0,4, Argon 6,95, aucun classement | **refus de garde** (1 457 167 > 520 000) avant tout appel : Claude 0, Argon 0, `refus-taille-1.json` scellé, pas de SORTIE |
| **D-a-haut** | Argon 7,68, même issue | **refus de garde**, Claude 0, Argon 0 |
| **D-c-plafond** (`--taille-max-consigne-externe 1200000`, pire cas) | Claude 40,00, Argon 11,2, trois juges | **refus de garde** (1 457 167 > 1 200 000, conséquence de CL42-04) : Claude 0, Argon 0 |
| D-c-devis | contrôle 2,725 refusé, 2,73 comptés | refus de garde, Claude 0, Argon 0 |
| pièce de 750 000, garde 1 500 000, pire cas | — | code 0 ; **Claude 40,00, Argon 11,2** (contrôle 2,5 ; passes 2,5 et 2,5 ; bras 0,2 + 3,5) ; **classement à trois juges** ; garde du bras par défaut |
| pièce de 750 000, garde 1 500 000, tarif du devis | — | contrôle 3,312 > 2,5 refusé : Argon 3,31 comptés, Claude 0, code 2 |
| pièce de 390 000, garde 1 200 000, tarif du devis | — | code 0 ; contrôle 1 097 167 → 2,494 ; passes 0,892 et 1,692 ; bras 0,0001 + 0,046 ; **Claude 40,00, Argon 5,12, classement à trois juges** |
| **S14** (repli en panne au troisième bras non joué) | code 2, aucun fichier ni message | code 2 ; sortie d'erreur : « classement sans bras impossible : RuntimeError : panne simulée … (classement-sans-bras-impossible-3.json scellé) » et clé `classement_sans_bras_impossible` ; fichier scellé trouvé par la sonde |
| défauts W07, W30, W35b, W36 (`mutations_cl9.py`, suite entière) | survivants | **tués** : W07, W30, W35b, W36 sur l'état de la v43 avant les deux décisions de Lazar ; W07, W30, W36 rejoués sur l'arbre final, tués (W35b n'a plus d'objet) |
| défauts sur le code neuf (`mutations_v43.py` dans mon brouillon, module `test_v7_ideation`) | — | six : aucun contrôle repris, prix ignoré par la garde, borne de fiche rétablie, relance comptée sur tous les contrôles : **tués** ; passes jamais gardées par le cœur, refus de taille au bras non compté : **survivaient**, essais complétés (`test_cl42_03_…`, `test_cl42_06_w36_…`), **tués** |

## Restes déclarés

- **Provision demandée avec CL42-04 non appliquée** (ci-dessus) : décision de Lazar à prendre.
- **Devis** : aux réglages du devis, la course est refusée par défaut aux deux prix, et la garde donnée de 1 200 000 ne suffit
  plus (contrôle 1 457 167, CL42-04) ; au barème 8,3 le contrôle seul coûte 3,02 > 2,5. Le devis doit relever le plafond du
  contrôle et des passes d'Argon (dépense) ou réduire les pièces (au tarif du devis et plafond 2,5, pièces et matériau ≤
  ≈ 740 000 caractères : la variante à 390 000 passe).
- **Juge au maximum du gabarit** : sans borne de fiche, 52 fiches de 44 259 caractères font 2,13 millions de caractères,
  au-dessus de la garde du bras aux deux prix ; un tel bras serait refusé (tentative comptée, classement sans bras) ; les
  fiches réelles (3 000 à 5 000 caractères, CL8) en sont loin.
- **Provision du juge** : convention (2 000 caractères de note par fiche servie), à confirmer au devis.
- **CL40-01 (c)** : la clé d'un contrôle Claude porte le moteur et l'adresse du relais, pas son identité : un relais relancé
  à la même adresse n'est pas vu, son contrôle réussi est repris ; une tentative scellée par la v42 (lectures sans clé) n'est
  jamais reprise ; le plafond d'un contrôle n'entre pas dans la clé ; pour calculer la clé d'Argon, la consigne de contrôle
  est construite une fois de plus (sans garde ni somme) quand une tentative antérieure a des contrôles réussis.
- **Garde des passes dans le cœur** : jouée quand le lanceur la demande (`garder_sessions_externes`, toujours en production)
  ou quand une taille est donnée ; un appel direct du cœur sans ces arguments garde le comportement de la v42. Un refus de
  la passe 2 dans le cœur arrête une course déjà partie : il est scellé au manifeste de fin, la SORTIE existe, la relance
  exige un mot de Lazar.
- **Refus de taille au bras compté** : il compte parmi les trois tentatives ; un refus scellé par un bras v42
  (`tentative_comptee` faux) serait compté aussi (aucune course réelle n'en a). Un classement sans bras et un
  `classement.json` peuvent coexister si une relance réussit (inchangé : le second fait foi).
- Après envoi, une **interruption** dont le repli échoue : le fichier scellé et le manifeste du bras le disent ; l'exception
  reste l'interruption (code 2).
- `--mesurer-consignes` imprime seulement (rien n'est scellé) : pour un chiffre de devis (R6), rediriger la sortie et la
  sceller. Les refus pour taille par proposeur ne sont pas imprimés au bilan du lanceur.
- Non traités : W03 (égalité), W28 (course concurrente), W35 (presque équivalent) ; M28, N28, V27 non repris ; W35b n'a plus
  d'objet (phrase retirée) ; W06, W11, W12 et quelques autres défauts de CL9 ne s'appliquent plus tels quels (code réécrit).
- Non vérifié : vraie commande d'Argon, son barème, sa limite de taille ; sessions Claude réelles ; relais réel.

**Essais** : six essais anciens changés par les choix et décisions de la v43, chacun dit dans sa docstring —
`TestV41.test_controle_a_la_taille_reelle_de_la_passe_2_et_ordre_d_argon` (CL42-04 : retour aux assertions de la v41) ;
`TestV41.test_relancable_calcule_avec_un_controle_claude_paye` (CL40-01 c : relance 39,82 relançable, seul le contrôle « KO »
rejoué ; Argon appelé une fois au lieu de trois) ; `TestV42.test_cl41_01_consigne_du_juge_de_243000_au_bareme_haut`
(CL42-05 : garde 1 400 000 − 60 000 ; refus de taille comptés et classés ; la taille de la course ne vaut plus au bras) ;
`TestV42.test_cl41_01_garde_de_taille_de_la_course_avant_tout_controle` (CL42-01 : défaut 520 000 au lieu de 1 000 000) ;
`TestV42.test_cl41_02_fiche_bornee_et_marge_realiste` (CL42-04 : fiches de plus de 12 000 admises, fiche maximale 44 259) ;
`TestV42.test_n04_n07_n08_couts_des_tentatives_precedentes` (CL40-01 c : Argon repris, somme 9,0 refusée sous 8,9 ;
coûts imputés 0,03 et 2,8 au lieu de 0,04 et 3,1).

**405 essais passent** (405 = 396 + 9 : `TestV43` dans `test_v7_ideation`) ; deux exécutions complètes sur l'arbre final,
227,3 s et 186,4 s (deux exécutions antérieures, avant les deux derniers compléments d'essais : 185,6 s et 255,2 s), aucun
processus survivant (`ps`), `essais/_tmp` retiré, aucun `__pycache__` réécrit (empreintes comparées au relevé de début).

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v43.txt
```
