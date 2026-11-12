# Journal — brouillon 2 du dessin et du devis de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — v2

- **Auteur** : même sous-agent rédacteur que le brouillon 1 (Opus 5.5, `claude-opus-5-5`), session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Le journal v1 (`f8c2b8c6…`) reste intact.
- **Ordre reçu de la mère** (message en cours de travail, après la remise du brouillon 1) : appliquer la contre-lecture 1 ; même
  consigne (`5403571b…`) et mêmes interdits ; décisions de la mère : couples et trois ajouts appliqués par programme ; C04 avec
  calcul refait sous un nouveau nom dans `calculs-v2/` ; CLP-06, CLP-09, CLP-07, CLP-04, CLP-05 traités comme dit ; D-3 (a), D-4
  (i) sous C01 et C02, D-5 (i) amendée et variante K1 exposée, D-6 non pour l'instant ; brouillon 1 intact ; aucun commit.
- **Produit** : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon2.md`
  (`05bcf094e3c26744242eb86c01b1c020e928dd6e7842eed34828d6f6b6de2af8`, scellé à 13:45:30 UTC) et, sous `calculs-v2/` (scellés) :
  `calculs_devis_essai_v4.py` (`9dc88b63…`), `sortie-calculs-devis-v4.txt` (`d44c4573…`), `appliquer_couples_cl1_v1.py`
  (`c09eeefc…`), `sortie-appliquer-couples-cl1-v1.txt` (`c992bbf6…`). Empreintes complètes : table du brouillon 2.
- Heures relevées par `date -u`.

## Chronologie

| Heure UTC | Fait |
|---|---|
| 13:30:55 | Contre-lecture 1 vérifiée (`f565d51cd39ae047d50a1774e79c67301f54ab5c1c107c4cba50193d33ba7744`, égale à son compagnon) ; brouillon 1 et journal v1 vérifiés intacts ; copies de `calculs-v1/` comparées à mon bac à sable : 12 fichiers sur 12 identiques et égaux à leurs compagnons. |
| ≈ 13:31–13:33 | Contre-lecture 1 lue en entier (397 lignes : verdict, ce qui tient, CLP-01 à CLP-15, avis sur les décisions, couples C01 à C14, annexe et sortie). Convention des marqueurs lue dans `prereg/gabarit-preregistrement-v1.md` (« À REMPLIR », refusé par le validateur). |
| 13:34:48–13:35:51 | `calculs_devis_essai_v4.py` écrit, lancé, complété (bloc 2c : erreur de famille des affirmations établies ; totaux par variante de modèle), relancé, scellé. Source du prix de borne haute vérifiée (`brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh`, `8cd40e08…`, l. 44). |
| 13:37:36 | `appliquer_couples_cl1_v1.py` écrit et lancé : **14 couples, chacun trouvé une fois dans le brouillon 1, aucun chevauchement** ; résultat écrit comme jalon 3 dans le bac à sable (`ff924956…`) ; script et sortie scellés ; copie du jalon 3 sous le nom du brouillon 2. |
| ≈ 13:38–13:44 | Retouches du rédacteur R01 à R48 par script (une occurrence chacune, blancs normalisés) ; table des empreintes régénérée par script, sans aucun chemin du bac à sable ; contrôle de présence des couples : deux échecs (C05, C10) dus à mes insertions au milieu du texte d'un couple, corrigés par déplacement (R49, R50) ; un échec attendu (C08, voir « Écarts aux couples »). |
| 13:44:27 | (fait de la mère, non du rédacteur) commit `b83345b22` « Essai Lean, brouillon 2 : fichiers EN COURS, NON SCELLÉS » : il contient un **état intermédiaire** du brouillon 2 et les quatre fichiers scellés de `calculs-v2/` ; la version scellée du brouillon 2 diffère de cet état (retouche R51 et table finale). |
| 13:45:30 | Retouche R51 ; brouillon 2 scellé (`05bcf094…`) ; vérification par `scellement verifier` de 19 fichiers du dossier (brouillons, journal v1, `calculs-v1/`, `calculs-v2/`) : tous `OK`. |
| (fin) | Présent journal écrit, puis scellé. |

## Application des couples (par programme)

- Script : `calculs-v2/appliquer_couples_cl1_v1.py`. Il lit les couples **dans la contre-lecture elle-même** (aucun texte retapé),
  cherche chaque chaîne « À remplacer » avec blancs normalisés, exige une occurrence unique dans le brouillon 1 et l'absence de
  chevauchement, remplace de la fin vers le début. Sortie : `calculs-v2/sortie-appliquer-couples-cl1-v1.txt` (positions et nombres
  de mots pour C01 à C14 ; « 14 couples appliqués, 0 défaut d'unicité, 0 chevauchement »).
- Reproductible depuis le dépôt seul : brouillon 1 (`9ccc9ac0…`) + contre-lecture 1 (`f565d51c…`) + script ⇒ jalon 3
  (`ff92495600cd094b821652d2a53bab16858e22a2eae2be12463760be25651719`).
- **Contrôle final** (script `table_et_controle_brouillon2_v1.py`, bac à sable) : le texte « Par » de chacun des 14 couples est
  présent **une fois** dans le brouillon 2 scellé, aux deux écarts près ci-dessous.

## Écarts aux couples (tous documentés, aucun ne change le sens d'un couple)

1. **C08** : le titre du paragraphe ajouté devient « Lignes absentes du tableau **du brouillon 1**, comprises dans le plafond
   (estimation de la contre-lecture, reprise telle quelle ; le tableau ci-dessus les chiffre par le script v4) », parce que le
   tableau du brouillon 2 contient désormais ces lignes. La phrase d'origine que C08 reprenait à sa suite (« Plafond proposé de la
   phase 1 : 450 USD ») est remplacée par le plafond de D-1b à 550 USD (R42) : le calcul v4 montre qu'à 450, au profil pire réaliste,
   la coupure A8 arrêterait le pilote (35 graines payables, sous le minimum de 40).
2. **C10** : « 192 à 300 aux effectifs du devis » devient « 150 à 300 aux scénarios du devis v4 » (conséquence de C04 : la règle
   d'effectif à 97,5 % donne 150 à 300).
3. Hors couples mais à côté : dans la puce « Correction » (§ 3.6), les mots « séquence fixe ; la classe 1 est lue au seuil plein ; »,
   qui précédaient le texte de C04 et le contredisaient, sont retirés (R28) ; les puces ajoutées après C05 (R46) et les phrases
   ajoutées après C10 (R26) ont été placées **après** le texte du couple (R49, R50), pour qu'il reste d'un seul tenant.

## Retouches du rédacteur (R01 à R51 ; script `retouches_brouillon2_v1.py`, bac à sable, sortie scellée)

- **En-tête** (R01 à R05) : titre « brouillon 2 » ; heures ; conflit (la contre-lecture ne trouve aucun avantage à Opus 5.5) ;
  statut (contre-lu une fois par Fable 5.2, non par Fable 5.1 : CLP-07, écart signalé) ; renvoi au journal v2.
- **Verdict** (R06) réécrit avec le devis v4 (D-1a, D-1b, phase 2) ; **§ 0** (R07) : paragraphe « ce qui change ».
- **§ 1** (R08 à R12) : piège du § 1.2 lié à C01 et C03 ; métriques de tête (motifs de `NON-ACCEPTE`, part au plafond, écart
  « rappel moins fausses alertes » : CLP-13, C12, C01) ; coût L/S « trois à huit fois » ; intervalles à 97,5 % (C04, C09) ;
  propriétés de O1, O1a, O1b au niveau 97,5 % (v4, bloc 2).
- **§ 2** (R13 à R16) : A6 étendu à la banque de confirmation (ligne de coût comptée) ; contre-lecteur réel (Fable 5.2) ; variantes
  de modèle par fonction (v4) ; **repli si GPT-6 Astra manque** (CLP-05 : R1 planteur Argon avec réserve écrite, ou R2 report ;
  recommandation R2 jusqu'à l'échéance de D-1b, puis R1).
- **§ 3** (R17 à R36) : délai en temps de processus et parallélisme fixé (CLP-12 c) ; gardes G-L6 (notations, macros, définitions
  imprimées) et G-L7 (axiomes et énoncés imprimés par un fichier du harnais) (CLP-12 a, b) ; artefacts R5 complétés (étape à
  hypothèses contradictoires prouvée à vide, CLP-12 d ; lecture hors du bac, appel réseau) ; `python(code)` dans l'environnement
  isolé (CLP-04) ; effectifs, issues, erreur de famille et borne des fausses alertes refaits à 97,5 % (v4) ; scénarios d'effectif
  (CLP-15 a : le « central 2 × 96 » est retiré) ; variante K1 de D-5 exposée ; vérification des deux bornes par la simulation de
  C09 ; A1 complété ; A6 étendu ; réserve de A7 chiffrée (32 USD) ; effet de A8 chiffré ; **A12** (aucun appel facturé sans GO de
  D-1b).
- **§ 4** (R37 à R46, R49) : sources (v4, CLP-15 b) ; multiplicateur d'écriture en cache « à vérifier » (CLP-10 a) ; durée de vie
  du cache ; lignes unitaires (adjudication, profil pire réaliste) ; **§ 4.3 réécrit** (D-1a, D-1b avec toutes les lignes, phase 2
  par scénario, plafonds, engagement, options) ; durées et calendrier ; **nature de la dépense** (CLP-05) ; **exigence d'isolement
  de la mère** (CLP-04) ; **machine chiffrée** par durée allumée × prix (CLP-10 b).
- **§ 7** (R47) réécrit : D-1 (enjeu commun, texte de C06 repris tel quel), **D-1a**, **D-1b**, D-2, D-3, D-4, D-5 (i amendée, i bis),
  D-6 (non pour l'instant). **§ 8 et § 9** (R48) : points ouverts mis à jour ; **marqueurs nommés « À REMPLIR »** (méthode
  d'intervalle, version de Lean, commit de Mathlib, seuils gelés, consignes, harnais et isolement, essais R5, script d'analyse,
  identifiants et prix vérifiés, machine, échéances).
- **R51** : formulation de l'avantage de D-1b (« complet au profil supposé, au moins 48 graines sur 60 au profil pire réaliste »).

## Ce que le calcul v4 a appris (et qui change le devis)

- **C04** : à 97,5 %, n_k = ⌈2,2414² · d⁺ / 0,01⌉ : 75 (6 discordantes sur 60), 102 (9), 129 (12), **150 dès 15** ; la phase 2 se
  lit donc au plafond d'effectif si les discordances sont celles que je suppose (0,25 à 0,30).
- **Erreur de famille** (bloc 2c) : pour l'affirmation établie par O1 (« Δ > 0 »), 0,020 à 0,026 pour deux classes ; O1a : 0,008 à
  0,024 ; mais « sous le seuil » (O3) : **0,027 à 0,060**, au-dessus de 0,025 avec le gabarit de Wald, surtout à discordance 0,20 :
  la simulation de C09 doit vérifier les deux bornes (écrit au § 3.6 et au § 8).
- **A8** (bloc 4) : avec la réserve de A7 et l'adjudication, au profil pire réaliste, 35 graines payables sous 450 (arrêt), 48 sous
  550 ; d'où le plafond de D-1b relevé à 550.
- **Phase 2** : 1 299,40 attendus au plafond d'effectif (profil supposé), 1 865,20 avec les lignes conditionnelles, 2 451,40 au
  profil pire réaliste ; plafond indicatif 1 900, à refaire au devis 2.

## Fichiers du bac à sable (scellés, non versés, non cités par la table du brouillon 2)

`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/` :
`jalon3-brouillon2-apres-couples-v1.md` (`ff924956…`, reproductible depuis le dépôt), `retouches_brouillon2_v1.py` (`6670b01c…`),
`sortie-retouches-brouillon2-v1.txt` (`5fd73ac8…`), `deplacer_bloc_c05_v1.py` (`1a8784b5…`), `deplacer_scenarios_c10_v1.py`
(`f14a393b…`), `table_et_controle_brouillon2_v1.py` (`32e222df…`). **Point pour la mère** : si ces scripts de retouche doivent
survivre (R6), les verser sous `calculs-v2/` ; je ne l'ai pas fait, la mère n'ayant nommé que le script v4 et sa sortie pour ce
dossier.

## Incident corrigé

L'import de `appliquer_couples_cl1_v1.py` par le script de contrôle a créé un dossier `__pycache__` dans `calculs-v2/` ; je l'ai
supprimé aussitôt (fichier produit par moi, hors de tout chemin interdit) et relancé le contrôle sans écriture de cache (`-B`,
`sys.dont_write_bytecode`). Le commit `b83345b22` de la mère ne le contient pas (vérifié : `git ls-files`).

## Exposition, cloison, interdits

- Lus : contre-lecture 1 (en entier) ; brouillon 1 et journal v1 (mes textes) ; gabarit de préenregistrement (l. 1–22) ; ligne 44 du
  lanceur cité ; `git log`, `git ls-files`, `git show --stat` sur le seul dossier de sortie (lecture). Rien d'autre.
- Aucun chemin des interdits communs ouvert ; aucune recherche récursive ; aucun appel de modèle ni d'interface ; aucun réseau ;
  aucune installation ; aucune dépense ; **aucune écriture git** (ni commit, ni index : le seul commit du dossier depuis le
  brouillon 1 est celui de la mère). Aucun refus rencontré. Aucune valeur de sonde de la course 7a.
- Conflit maintenu : je suis le modèle recommandé pour les deux bras ; la contre-lecture 1 n'y a vu aucun avantage indu.
