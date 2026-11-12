# Journal du rédacteur — candidat 3 de T0.7 et ordre d'exécution brouillon 7 (v1)

Modèle : Opus 5.5 (claude-opus-5-5), rédacteur du candidat 2 et du brouillon 6 (même sous-agent). Mandat : message de la mère (corrections du code, R-2305, R-2309), mêmes interdits et mêmes chemins d'écriture que la consigne `d29c7858…`, aux noms près. Heures relevées par `date -u`. Journal tenu au fil.

- 2026-11-11T04:05:31Z — mandat reçu ; journal ouvert ; bac à sable `…/scratchpad/agents/t07-candidat3/`.
- 2026-11-11T04:06:55Z — lus : R-2305, R-2306, R-2309 ; rapport du code v2 (71cc3b89…, entier) ; vérifiés par sha256sum -c : configuration v8 (e31c7a79…), rapport v2, rapport v1 (cb31edc8…, intact), configuration v7 (3701407c…, intacte), repetition-jouet-v3-journal.txt (3d1421e7…) et -resume.json (691b98cf…).
- 2026-11-11T04:07:18Z — module au commit 7e23a554 : 26 fichiers (liste au rapport final) ; dix-huit anciens égaux à CODE-T07-v1.json ; quatre neufs changés depuis 0d0c5da4 (lecture_v4 f193f1b1…, passe_blanc_v2 8e24642f…, reextraction_p3_v1 66b6684c…, repli_etapes_v2 fe08aaa1…), quatre inchangés (plancher_v2, lecture_v3, lectures_t07_v2, plancher_v3) ; script v3 a19c594d… au commit. Configuration v8 : lecture_v4 (copie de src/ à 7e23a554 par git show) rend 0f32c6de… (code 0) et refuse la v7 (tolérances) ; v7 → v8 : seules les tolérances carte changent (10⁻³, 10⁻²).
- 2026-11-11T04:09:24Z — plan : changements gelés limités à G3-01 (Plan d'analyse, étape A, point 1 bis : paliers « carte » 10⁻³ et 10⁻², réserve « cause non établie », la garde n'arrête pas toute faute) et G3-02 (Liste d'arrêt : libellé de la réserve) ; la passe à blanc et l'étape B ne sont décrites que hors de l'empan gelé (Module, Calcul et dépense, ordre) : CLP3-03 et notes 05, 07, 10 y vont. Ordre brouillon 7 écrit d'abord (le candidat 3 cite son empreinte).
- 2026-11-11T04:11:56Z — ordre brouillon 7 écrit par son script (essai sur racine factice puis dépôt : code 0, « TOUT PASSE », 24 couples O7-01 à O7-24, couples défaits → brouillon 6 octet pour octet, 12 marqueurs dont ATT_C7_T07 neuf et SHA_SCRIPT_V3_T07 rempli, § 6 égal au brouillon 6, répétition v3 : 17 verdicts sur 17 vrais) ; brouillon 7 et son script scellés ; brouillon 6 et son script intacts.
- 2026-11-11T04:14:50Z — générateur des couples du candidat 3 (bac à sable) joué en essai : 23 couples, 2 gelés, un seul marqueur restant.

## Couples du candidat 3 (dans l'ordre d'application)

| id | section | gelée | motif |
|---|---|---|---|
| C3-01 | titre | non | numéro : candidat 3 |
| C3-02 | statut | non | statut du candidat 3 ; statut du candidat 2 gardé pour mémoire |
| C3-03 | table « du candidat 2 au candidat 3 » (neuve) | non | table des changements du candidat 3 |
| C3-04 | En-tête (auteur) | non | auteur du candidat 3 |
| C3-05 | En-tête (commit du code : état au candidat 3) | non | code corrigé au commit 7e23a554 ; vingt-six modules (R-2305, R-2309) |
| C3-06 | En-tête (configuration : empreinte canonique de la v8) | non | EMPREINTE_CONFIG_T07 → configuration v8 (R-2305, R-2309) |
| C3-07 | En-tête (configuration : v8) | non | configuration v8 acceptée par la v4 seule |
| C3-08 | En-tête (configuration : chemin final de la v8) | non | chemin final nommé par l'ordre, brouillon 7 ; v8 = v7 aux tolérances près |
| G3-01 | Plan d'analyse | **oui** (Plan d'analyse) | R-2305 (CLP3-01 : seuils de garde d'un texte non scellé, dans le périmètre de (a'), R-2285 : définition et plancher) ; R-2309 (configuration v8) |
| G3-02 | Liste d'arrêt | **oui** (Liste d'arrêt) | R-2305 (CLP3-01 : libellé de la réserve) ; R-2285 (définition et plancher) |
| C3-09 | Calcul et dépense (devis) | non | script v3 écrit ; devis inchangé (rapport v2) |
| C3-10 | Calcul et dépense (script de l'instance) | non | script v3 écrit et répété (R-2309) |
| C3-11 | Module (introduction) | non | état du module au candidat 3 (R-2305, R-2309) |
| C3-12 | Module (configuration) | non | configuration v8 |
| C3-13 | Module (point 18, passe à blanc) | non | CLP3-03 : contrôle avant l'ouverture (R-2305) |
| C3-14 | Module (points d'entrée) | non | configuration v8 ; la v4 refuse la v7 |
| C3-15 | Module (ordre d'exécution) | non | EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07 → ordre, brouillon 7 |
| C3-16 | Reste (1 decies) | non | fait et reste au candidat 3 |
| C3-17 | Contre-lecture | non | vérification courte neuve du candidat 3 |
| C3-18 | Marqueurs (paragraphe) | non | compte du candidat 3 |
| C3-19 | Marqueurs (table : EMPREINTE_CONFIG_T07) | non | configuration v8 |
| C3-20 | Marqueurs (table : EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07) | non | ordre, brouillon 7 |
| C3-21 | Marqueurs (table : C7_ET_CODE_T07_26_MODULES) | non | règle de C7 (R-2306) |

## Sortie du script faire du candidat 3 (dépôt, 2026-11-11, 04:16:50 à 04:16:57 UTC ; code 0)

```
brouillons/T0.7-sondes-v0-v1-candidat2.md : 9de13f6a9a40267f… (égale)
brouillons/T0.7-sondes-v0-v1-candidat3-pieces/T0.7-sondes-v0-v1-candidat3-couples-v1.json : 4e5fc8b05dbbf688… (égale)
docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md : 92d9aebee0634c91… (égale)
docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md : d799a01bd6008d73… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json : 3701407cf96f2851… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json : e31c7a79dc1b68d5… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v2.md : 71cc3b89c2df3c8f… (égale)
registres/code-t07/CODE-T07-v1.json : 9ef4ede751fcceb5… (égale)

# configuration v8 et code au commit 7e23a554
v7 → v8 : clés ['plancher_figees'], sous-clés ['tolerances'], tolérances {'processeur': 1e-06, 'carte_sonde': 0.001, 'carte_directions': 0.01} : True
module recopié au commit 7e23a554 (196 fichiers) ; `lecture_v4 empreinte-config` v8 : code 0, 0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12 ; v7 : code 2, « REFUS : mode réel : plancher_figees.tolerances = {'processeur': 1e-06, » : True
reextraction_p3_v1.py au commit : TOLERANCES de la v8 et réserve « cause non établie » : True

# application (23 couples) (id ; ligne ; sections touchées ; gelée)
C3-01 ; l. 1 ; (avant la première section) ; non
C3-02 ; l. 3 ; (avant la première section) ; non
C3-03 ; l. 182 ; Table « ce qui change du candidat 1 au c ; non
C3-04 ; l. 644 ; En-tête ; non
C3-05 ; l. 645 ; En-tête ; non
C3-06 ; l. 699 ; En-tête ; non
C3-07 ; l. 699 ; En-tête ; non
C3-08 ; l. 699 ; En-tête ; non
G3-01 ; l. 1390 ; Plan d'analyse ; OUI
G3-02 ; l. 1935 ; Liste d'arrêt ; OUI
C3-09 ; l. 2035 ; Calcul et dépense (aucun épisode joué ;  ; non
C3-10 ; l. 2035 ; Calcul et dépense (aucun épisode joué ;  ; non
C3-11 ; l. 2176 ; Module de lecture `src/controle_ia/t07/` ; non
C3-12 ; l. 2250 ; Module de lecture `src/controle_ia/t07/` ; non
C3-13 ; l. 2611 ; Module de lecture `src/controle_ia/t07/` ; non
C3-14 ; l. 2616 ; Module de lecture `src/controle_ia/t07/` ; non
C3-15 ; l. 2622 ; Module de lecture `src/controle_ia/t07/` ; non
C3-16 ; l. 2947 ; Reste avant le scellement (au plus tard  ; non
C3-17 ; l. 2984 ; Contre-lecture ; non
C3-18 ; l. 3280 ; Marqueurs à remplir avant le scellement ; non
C3-19 ; l. 3325 ; Marqueurs à remplir avant le scellement ; non
C3-20 ; l. 3336 ; Marqueurs à remplir avant le scellement ; non
C3-21 ; l. 3320 ; Marqueurs à remplir avant le scellement ; non
couples gelés : {'G3-01': "Plan d'analyse", 'G3-02': "Liste d'arrêt"} ; égaux au mandat : True

écrit : brouillons/T0.7-sondes-v0-v1-candidat3.md (1b9b75f0611aab05b9edf61acb49d72f3d606af25024100bda1f0fe75adda4a6 ; 3337 lignes)

# vérifications
(1) titre et premier statut : True
(2) couples défaits dans l'ordre inverse → candidat 2 octet pour octet : True
    « Hypothèse » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Règle « mots et coût » de T0.6 (CLT7-02 ; lue, j » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Prédiction chiffrée et signe attendu » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Métrique » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Seuil » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Plan d'analyse » : couples ['G3-01'] ; 2 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Écrits exigés par P3-bis avant toute ouverture ( » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Critères de lecture gelés » : couples [] ; 0 lignes de différence ; égale au candidat 2 une fois défaite : True
    « Liste d'arrêt » : couples ['G3-02'] ; 2 lignes de différence ; égale au candidat 2 une fois défaite : True
(3) sections neuves : ['Table « ce qui change du candidat 2 au candidat 3 »'] ; disparues : []
(4) marqueurs restants : {'<<C7_ET_CODE_T07_26_MODULES>>': 1}
(5) controle_ia.prereg.problemes(candidat 3) : ['marqueurs de gabarit restants : <<C7_ET_CODE_T07_26_MODULES>>'] ; à valeur factice : []
(6) module au commit 7e23a554 : 26 fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : True
(7) ordre, brouillon 7 : `ATT_C7_T07` présent, `SHA_SCRIPT_V3_T07` rempli (a19c594d…), chemin final de la v8 : True
(8) phrases exigées : 18 sur 18 ; passages retirés encore présents : []
(9) différentiel candidat 2 → candidat 3 : 17 lignes retirées, 45 lignes ajoutées ; 23 couples, dont 2 gelés

TOUT PASSE
```

## Sortie du script de l'ordre, brouillon 7 (dépôt ; code 0)

```
brouillon 6, configurations v7 et v8, répétition v3 et rapport v2 vérifiés ; v7 → v8 : seules les tolérances du palier « carte » changent ({'processeur': 1e-06, 'carte_sonde': 0.001, 'carte_directions': 0.01}) ; six chemins cités
répétition v3 : conforme, 17 verdicts sur 17 vrais
24 couples appliqués, chacun à une occurrence
tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 6 retrouvé (610 → 668 lignes)
marqueurs : 12, une occurrence chacun (`ATT_C7_T07` neuf ; `SHA_SCRIPT_V3_T07` rempli), aucun autre
phrases exigées : 19 présentes
§ 6 (devis, plafond, marge) égal à celui du brouillon 6
blocs bash : 8, bash -n sans erreur ; extraits Python : 10, ast.parse sans erreur
§ 4.3 : choix de l'offre essayé sur trois cas factices : conforme (bloc inchangé depuis le brouillon 6)
écrit : docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md (d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916)
TOUT PASSE
```

## Sorties (compagnons `.sha256` écrits par `controle_ia.scellement sceller`)

- `brouillons/T0.7-sondes-v0-v1-candidat3.md` : `1b9b75f0611aab05b9edf61acb49d72f3d606af25024100bda1f0fe75adda4a6` (3 337 lignes ; 23 couples, 2 gelés) ;
- `brouillons/T0.7-sondes-v0-v1-candidat3-pieces/T0.7-sondes-v0-v1-candidat3-couples-v1.json` : `4e5fc8b05dbbf688c294bd7f10296c89d742eb8cfb0d7887732f5f2ea364ffed` ;
- `brouillons/T0.7-sondes-v0-v1-candidat3-pieces/T0.7-sondes-v0-v1-candidat3-faire-v1.py` : empreinte à son compagnon ;
- `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md` : `d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916` (668 lignes ; 24 couples) ;
- `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7-appliquer-v1.py` : `478dde84100e1a32635f628d9019ed7d4dbbae914917b75c2908cbe4419c21a4` ;
- non versé : générateur `…/scratchpad/agents/t07-candidat3/gen/gen_couples_c3.py` (`393b14ce…`).
- Candidat 2, brouillon 6 et leurs scripts intacts (`sha256sum -c`).

## Points ouverts

1. G3-01 et G3-02 : seuls changements gelés (R-2305 dans le périmètre de R-2285) ; à juger par la vérification courte.
2. Ordre, brouillon 7 : marqueurs laissés à la mère : `COMMIT_SRC_CONTRE_LU_T07` (`SRC7` : commit de `main` qui fusionne la branche finale), `ATT_C7_T07` (neuf ; P12 compare désormais les arbres de S7 à ceux de C7), et les dix du brouillon 5.
3. Le script v3 (`a19c594d…`) est au commit `7e23a554`, non fusionné ; P9 exige qu'il soit sur `main` à cette empreinte.
4. Contre-lecture courte différentielle `0d0c5da4..7e23a554` en cours : si elle change un module, les empreintes de l'en-tête (« état au candidat 3 ») et la cellule de l'ordre changeraient.

## Interdits tenus

Mêmes que pour le candidat 2 : aucun chemin interdit ouvert ; aucune valeur de sonde de 7a ; aucune recherche récursive ; aucune clé lue ; aucun appel externe ; aucun `vastai` ; aucune dépense ; git en lecture seule, rien committé ; écritures sous `brouillons/` et `docs/procedures/` seulement, noms neufs ; aucun pytest lancé ; aucun refus.
- 2026-11-11T04:17:16Z — journal clos ; scellé ensuite.
