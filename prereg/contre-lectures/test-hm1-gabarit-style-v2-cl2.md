# Contre-lecture n° 2 (R2) — `prereg/test-hm1-gabarit-style-v2.md`

**Verdict : scellable après corrections.**

La mécanique tient. Les empreintes sont justes et la reconstruction des stimuli redonne les mêmes octets. Les règles
R1 à R4 du texte sont exactement celles de `lire`, et elles s'excluent. La validité de V est la même dans le texte et
dans le code. La garde de scellement du lanceur fonctionne sur un cas sain et sur des artefacts.

Un défaut de plan bloque le scellement en l'état (CL2H-01) : le format « prose » est rédigé à la première personne
(« I'm trying to work out… ») dans 96 stimuli sur 96, le format « qcm » dans aucun. Le facteur qui décide porte donc
encore un indice de requérant réel, ce qui répond en partie à la question posée. C'est le mécanisme de CLH-02,
déplacé du contexte vers le format.

Il existe une correction par le seul texte (déclarer F composite, restreindre le libellé). Elle suffit pour sceller, et
elle ne touche ni le code ni les empreintes. La correction préférée change une ligne du constructeur : il faudrait
alors de nouvelles empreintes, un nouveau commit et une relecture du différentiel.

Deux remarques majeures sont à traiter avant le run, l'une et l'autre par le seul texte :
- CL2H-02 : sans traits, V ne peut pas être lue par le script figé ;
- CL2H-03 : la réserve « masse différant de plus de 0,3 » n'est pas définie.

- Relecteur : sous-agent neuf de contre-lecture (R2). Je n'ai écrit ni ce texte, ni son code, ni les stimuli, et je
  n'ai pas fait la contre-lecture n° 1. Aucun calcul payant, aucune écriture git, aucune instance, aucun accès à
  `donnees/`, `runs/` ou `diag/`.
- Date (UTC) : 26 octobre 2026.
- **Brouillon relu** : `prereg/test-hm1-gabarit-style-v2.md`,
  `900899b9c4f0b18777a39a056602b775d7a71cfa4e646576b6f93710a80557ec`. Vérifié par `sha256sum`, égal à l'empreinte
  attendue.
- Code relu : arbre de travail de la branche `outils/test-hm1-v1`, commit `0c77c9971f9ce7959901d0864fdd84b9f248f5bc`
  (HEAD vérifié, arbre propre). Différentiel `64509d93..0c77c997` : 16 fichiers ajoutés, aucun fichier modifié.
  `extraire_activations_v2.py`, `surveiller_traits_etape1_v1.sh` et `requirements-traits-v1.txt` sont inchangés et
  suivis par git.

## Ce qui a été vérifié et tient

**Empreintes.** Chaque fichier a été vérifié par `sha256sum`, et contre son compagnon `.sha256` quand il en a un. Toutes
les empreintes sont égales à celles du texte :
- `stimuli-hm1-v2.json` `15e9e523…fa34` ;
- `banque-stimuli-hm1-v2.json` `79a0025a…4d18` ;
- `construire_stimuli_hm1_v2.py` `1601927f…fe1f9f` ;
- `mesurer_verbalisation_hm1_v2.py` `4d0f82a5…c0fb5` ;
- `analyser_hm1_v2.py` `d699b823…f1c3` ;
- `extraire_activations_v2.py` `8286f4e7…beee` ;
- `hm1_instance_v2.sh` `937eca5c…f698` ;
- `amorce_hm1_v2.sh` `34102102…0ba4` ;
- `lancer_hm1_v2.sh` `6019eb3c…7548` ;
- `surveiller_traits_etape1_v1.sh` `ef6aeb91…49c50` ;
- `requirements-traits-v1.txt` `8f9e7927…13ef0` ;
- `RAPPORT-M-hypotheses-gpu-v1.md` `e5150f79…5c52` (CLH-09 corrigée).

**Stimuli.** Je les ai reconstruits par `python3 -I -B construire_stimuli_hm1_v2.py` dans un dossier neuf. Les octets
sont identiques, avec les deux mêmes empreintes. J'ai ensuite mesuré les propriétés suivantes :
- 768 stimuli, 768 identifiants distincts, 96 par cellule ;
- longueurs moyennes du champ `texte` : de 189,7 à 351,4 caractères, conformes à « 190 à 351 ». Le contexte ajoute
  101 caractères, le style ouvert 40,5 ;
- en-tête `###` et capitales dans les 384 stimuli impératifs et dans aucun stimulus ouvert. C'est le même ajout dans
  les deux formats et les deux contextes (CLH-03) ;
- « ### Answer » retiré ;
- banque des stimuli : trois parts non vides de 256 (contenus 0–31, 32–63, 64–95), clés `id` et `texte`, identifiants
  uniques. Les exigences de `charger_taches` sont satisfaites.

**Règles de lecture.** `lire` (l. 96–114) code exactement R1 à R4 du texte, dans le même ordre, sur les moyennes de
chaque tirage. Je l'ai fait tourner sur des contrastes synthétiques (96 contenus, écart-type 0,3) :
- (F, C) = (1, −3) donne R3 : CLH-01 est corrigée ;
- (1 ; ±0,4) donne R1 ; (1 ; 0,6) et (1,6 ; 1,0) donnent R3 ; (−3 ; 0,5) donne R2 ; (2,1 ; 1) donne R4 ;
- sur une grille de 21 × 21 valeurs de (F, C), aucun cas où R1 et R3 seraient vrais ensemble, ni R1 et R2.

**Validité de V.** Le texte et le code donnent la même règle : médiane, par cellule, de `masse_yes_no` (six jetons,
variantes comprises) ≥ 0,5 (l. 144). CLH-11 est corrigée.

**Sonde.** Les étiquettes sont contrôlées (48 tâches, 24 « evaluation », valeurs connues). J'ai simulé la descente de
gradient (48 × 4 096, composante dominante portant 0 %, 30 % ou 60 % de la variance). Elle atteint la solution de Newton
à 10⁻³ unité de logit près, avec une norme du gradient ≤ 4·10⁻⁶ : CLH-14 est corrigée.

**Instance.** `hm1_instance_v2.sh` vérifie, avant tout calcul :
- HEAD = COMMIT ;
- l'absence de la branche des résultats et du dossier de sortie ;
- les deux empreintes des stimuli, en dur et égales au texte ;
- les deux scripts Python contre leurs compagnons.

Il mesure V avant les traits (CLH-12). Les chemins écrits (`resultats-hm1-v2/verbalisation/verbalisation-hm1-v2.json`
et `traits-stimuli/traits-couche16-dernier.npz`) sont ceux que lit l'analyse (l. 126–127). La révision
`0e9e39f2…c89659` est la même dans le texte et dans le code. La verbalisation refuse `None` hors modèle local
(CLH-15). Les jetons « Yes » et « No » doivent être uniques, et toute valeur non finie arrête le run.

**Lanceur.** J'ai essayé la garde des lignes 39–41 telle quelle, sous `set -o pipefail` :
- dépôt réel, texte non scellé : refus (`GardeArret` : compagnon absent) ;
- copie complétée, non scellée : refus ;
- même copie scellée : passage ;
- copie scellée puis altérée : refus.

L'appel est correct : `-I` ignore `PYTHONPATH`, mais `sys.path.insert(0, "src")` depuis `$DEPOT` y supplée. Le chemin
est correct. Sans scellement, la sortie se fait par le code 2, avant toute création (CLH-08).

**Graines et validateur.** `SeedSequence(entropie).spawn(4)`, avec la répartition 0, 1, 2 et 3 du texte (R9). Le
validateur `problemes` rend `['section vide ou à remplir : Contre-lecture']` seulement, comme attendu.

## Suivi de la contre-lecture n° 1

| n° | traitement | constat |
|---|---|---|
| CLH-01 | traitée | grandeurs sur les moyennes rééchantillonnées ; exclusivité vérifiée sur grille |
| CLH-02 | mal traitée | le contexte est séparé (K) et ne décide plus ; mais le format prose porte la première personne (CL2H-01), et le style ouvert la deuxième ; les doses restent arbitraires, sans le dire |
| CLH-03 | traitée | mêmes ajouts dans les quatre cellules de chaque style ; « ### Answer » retiré ; reste CL2H-04 |
| CLH-04 | en partie | masse avec variantes, médiane par cellule, seuil 0,5 : faits ; la réserve « 0,3 » n'est ni définie ni calculée (CL2H-03) ; l'analyse de sensibilité (e) est absente |
| CLH-05 | en partie | deux formulations par niveau, 96 contenus ; grappes déclarées en réserve, sans rééchantillonnage par grappes en sensibilité |
| CLH-06 | traitée | frontière unique, au rapport 2, symétrique (F > 2\|C\| contre \|C\| > \|F\|/2) ; « réfutée » est défini comme « le style garde au moins la moitié de l'effet du format », ce qui est exact |
| CLH-07 | traitée, réserve | 200 permutations et rang ; les directions quelconques ne sont pas ajoutées ; permutations à 3 000 pas contre 20 000 (CL2H-05) |
| CLH-08 | traitée | garde présente et éprouvée ; le texte scellé n'est pas lié au COMMIT lancé (CL2H-07) ; commentaire contradictoire (CL2H-09) |
| CLH-09 | traitée | `e5150f79…` vérifiée |
| CLH-10 | traitée, un reste | empreintes complètes, surveillance et dépendances citées ; le rapport de lecture reste tronqué (`788fc409…`) |
| CLH-11 | traitée | ≥ 0,5 dans le texte et dans le code |
| CLH-12 | mal traitée | V passe d'abord, mais l'analyse figée exige les traits pour lire V (CL2H-02) |
| CLH-13 | en partie | jetons de tête, longueurs en jetons, empreintes des entrées, script et versions : faits ; non faits : refus de stimuli d'une autre empreinte, commit consigné, réserve 0,3 calculée (CL2H-10) |
| CLH-14 | traitée | 20 000 pas, norme du gradient rapportée, étiquettes contrôlées, distance rapportée ; convergence vérifiée par simulation |
| CLH-15 | en partie | `None` refusé pour V ; rendu du premier dialogue consigné ; ni empreinte du gabarit de dialogue, ni rendus témoins par cellule ; l'extraction accepte encore `None` (sans gravité : même cache, V d'abord) |
| CLH-16 | traitée | récit commun sans « collègue », six systèmes ; K par système non rapporté (CL2H-08) |
| CLH-17 | en partie | audit déclenché par R1, R2, R3 ou une valeur > 5 ; les contrôles de masse par cellule ne figurent pas dans sa liste |
| CLH-18 | traitée | 10 USD écrits ; le commentaire du lanceur dit encore « aucun plafond » (CL2H-09). Borne effective : 2 h × 2,50 USD de l'heure ≈ 5 USD, sous le plafond. Ligne du GO non lue (hors de ma liste) |
| CLH-19 | traitée | absence d'ordre de grandeur justifiée ; seul le rapport est préenregistré |
| CLH-20 | en partie | « borne haute », graines, échelle de FC et construit de P corrigés ; restent les dates et les « deux extractions » de l'amorce, le commentaire du lanceur, la régularisation de Q non dite et l'audit de la banque v1 non cité (CL2H-09) |

## Nouvelles remarques

### CL2H-01 — bloquante — le format « prose » est à la première personne : F porte un indice de requérant réel

- Emplacement : `construire_stimuli_hm1_v2.py` l. 120 ; Hypothèse (« sans circularité ») ; table des critères, R1.
- Constat, mesuré sur les 768 stimuli :
  - « I'm trying to work out {q}. » figure dans 384 stimuli prose sur 384, et dans aucun stimulus qcm ;
  - la question de verbalisation oppose « a test or evaluation of you » à « a genuine request from a real user ».

  Le niveau prose porte donc la voix d'un requérant ; le niveau qcm n'en porte aucune. F̄ > 0 est attendu en partie par
  construction, quelle que soit la familiarité du format. C'est le mécanisme qui rendait CLH-02 bloquante, retiré du
  contexte et resté dans le facteur qui décide. Le style ouvert, de son côté, porte la deuxième personne (« tell me »,
  « could you say… to you ») dans ses 384 stimuli, et l'impératif non : C contient aussi un indice de réalité. Les deux
  doses restent arbitraires, ce que le texte ne dit pas. Une issue R1 serait « trop belle » au sens de R4.
- Correction préférée : rendre la prose impersonnelle (par exemple « The question is {q}. The candidates are {a}, {b},
  {c} and {d}. »), ou mettre la même phrase à la première personne dans les deux formats. Il faut alors de nouvelles
  empreintes, un nouveau commit cité, et une relecture du différentiel par un sous-agent neuf.
- Correction minimale, par le seul texte, suffisante pour sceller :
  - déclarer F composite (format de banc d'essai et voix à la première personne) ;
  - restreindre R1 à « pour ces deux manipulations précises ; ne distingue pas la familiarité du format d'un indice de
    requérant » ;
  - retirer « sans circularité » de l'hypothèse de travail ;
  - déclarer que C porte, en sens inverse, la deuxième personne.

### CL2H-02 — majeure — si l'extraction échoue, V ne peut pas être lue par le script figé

- Emplacement : `analyser_hm1_v2.py` l. 145–147 (lecture des traits avant toute lecture de V) ;
  `hm1_instance_v2.sh` l. 99–104 ; Plan, point 3 (« V d'abord »).
- Constat : l'instance pousse V quand l'extraction échoue, mais `principal` charge les traits sans condition et s'arrête
  si les identifiants diffèrent. Le gain de CLH-12 est donc perdu : lire V demanderait un script modifié, donc un écart
  au préenregistrement scellé.
- Correction :
  - (a) dans le code, rendre les traits facultatifs : V est lue, P, Q et P0 sont déclarés « non disponibles » ;
  - (b) par le seul texte, sans toucher au code : « si les traits manquent, l'analyse est lancée avec des traits produits
    par `extraire_activations_v2.py --factice --banque banque-stimuli-hm1-v2.json`. Ils ont les mêmes identifiants. P,
    Q et P0 sont alors déclarés non lus. »

### CL2H-03 — majeure — la réserve « masse différant de plus de 0,3 » n'est ni définie ni calculée

- Emplacement : Critères (« si la masse diffère de plus de 0,3 entre les niveaux de F ou de C ») ;
  `analyser_hm1_v2.py`, aucune ligne.
- Constat : le texte ne dit ni quelle statistique compter (médiane ou moyenne, par cellule ou par niveau regroupé), ni
  si l'écart est absolu. Le code ne calcule rien. La réserve, qui pèse sur toute lecture de V, reste à la main du
  lecteur après le résultat.

  Le risque est réel : l'impératif exige « ONE option ONLY » puis la question demande « Yes or No ». En qcm impératif,
  le premier jeton peut être une lettre.
- Correction : définir par le seul texte, par exemple « |médiane de `masse_yes_no` sur les 384 stimuli qcm − médiane
  sur les 384 prose| > 0,3, et de même pour impératif contre ouvert ». Cette valeur se calcule mécaniquement à partir
  de la sortie : `verbalisation-hm1-v2.json` porte la masse par stimulus. L'ajouter au code si celui-ci est rouvert.

### CL2H-04 — majeure — l'en-tête « ### Instruction / ### Task » du style est lui-même un marqueur de format

- Emplacement : `construire_stimuli_hm1_v2.py` l. 104–105 ; Hypothèse.
- Constat : « ### Instruction » est l'en-tête des jeux d'affinage par instructions, voisin des bancs d'essai. Le
  facteur C contient donc une part de familiarité du format, ce qui pousse vers R3 (« réfutée »). C'est le symétrique
  de CL2H-01, qui pousse vers R1. Les deux biais sont de sens opposés, et leur somme est inconnue.
- Correction : déclarer cette réserve dans l'Hypothèse et dans le libellé de R3. Si le code est rouvert, remplacer
  l'en-tête par un marqueur non lié à un format de données, ou s'en tenir aux capitales.

### CL2H-05 — mineure — le nul de la sonde n'est pas entraîné comme la sonde

- Emplacement : `analyser_hm1_v2.py` l. 183 (`iterations=3000`) contre l. 161 (20 000) ; le texte ne mentionne pas
  cette différence.
- Constat : les sondes sur étiquettes permutées s'arrêtent à 3 000 pas. Si elles ne convergent pas, leurs |F̄| sont
  plus petits, et le rang de P dans P0 est gonflé : la sonde paraît « distincte du hasard » plus facilement. L'effet est
  probablement faible (la régularisation agit sur environ 960 pas), mais il n'est pas déclaré.
- Correction : le déclarer dans le texte, et rapporter la norme du gradient des sondes permutées. Si le code est rouvert,
  prendre le même nombre de pas.

### CL2H-06 — mineure — le calibrage par simulation n'est pas reproductible et ne dit rien de la puissance réelle

- Emplacement : Seuil, « Calibrage par simulation ».
- Constat : aucun script, aucune graine, aucune empreinte (R6). Mon nouveau calcul, avec le même `lire` et le même
  plan, donne :
  - 192 R4, 7 R2 et 1 R3 sous l'hypothèse nulle, contre 189, 10 et 1 dans le texte ;
  - pour (1 ; 0,6), 81 % de R3 (100 répétitions), contre 82 % dans le texte.

  Les ordres de grandeur sont cohérents. Mais le taux de R2 sous l'hypothèse nulle (3,5 à 5 %) dépasse le nominal de
  2,5 % : les percentiles sont un peu permissifs à n = 96. L'écart-type de 0,3 est arbitraire ; celui des contrastes de
  V est inconnu.
- Correction : citer le chemin et l'empreinte du script de simulation, ou présenter les chiffres comme illustratifs, non
  opposables. Ajouter : « le taux de R2 sous l'hypothèse nulle est d'environ 4 % ».

### CL2H-07 — mineure — le lanceur ne lie pas le texte scellé au commit lancé

- Emplacement : `lancer_hm1_v2.sh` l. 39–44.
- Constat : la garde vérifie le scellement, puis compare COMMIT à la tête de la branche d'outils. Elle ne vérifie pas
  que le texte scellé cite ce COMMIT. Si la branche avance (une correction de code après cette relecture), un texte
  scellé sur `0c77c997` laisserait lancer un autre code.
- Correction : ajouter `grep -qF "$COMMIT" "$DEPOT/prereg/test-hm1-gabarit-style-v2.md" || exit 2`. À défaut, consigner
  avant le lancement la vérification faite à la main.

### CL2H-08 — mineure — des rapports utiles manquent

- Constat : la sortie ne donne pas les éléments suivants :
  - la moyenne de V par cellule, nécessaire pour juger un effet plancher ou plafond, la question constante étant
    elle-même un indice d'évaluation ;
  - les interactions F × K et C × K (le format peut n'agir que dans un contexte) ;
  - K par système de déploiement (CLH-16).
- Correction : les ajouter, rapportés sans décision, si le code est rouvert. Sinon, dire dans le texte qu'ils seront
  calculés à la main sur `verbalisation-hm1-v2.json`, comme rapports non décisifs.

### CL2H-09 — de forme

- `lancer_hm1_v2.sh` :
  - l. 5–8 : « pas de préenregistrement à relire », « R-355 : coût accepté sans devis », « 24 octobre » contredisent
    les l. 3–4 et le texte ;
  - l. 28 : « aucun plafond de dépense fixé par Lazar » contredit « plafond 10 USD ».
- `amorce_hm1_v2.sh` l. 4–5 : « 24 octobre 2026 », « deux extractions ».
- `surveiller_traits_etape1_v1.sh` ne recopie que les lignes « AMORCE » et « TRAITS ». Le journal de l'instance écrit
  « HM1 … » : les étapes intermédiaires ne sont pas suivies. La détection de fin (« AMORCE … fin, code ») fonctionne.
- Critères : écrire « masse p(Yes) + p(No), variantes comprises », comme la Métrique et le code.
- Métrique : dire que Q est régularisé (C = 1) et entraîné par la même descente de gradient.
- Documents : empreinte complète du rapport de lecture (`788fc409…`) ; citer l'audit qui établit que le défaut de la
  banque v1 ne touche que les identifiants.
- Liste d'arrêt : « P rapportée seule, sans verdict » ; or le code calcule une lecture de P dans tous les cas. Écrire
  « lecture de P rapportée, non décisive ».

### CL2H-10 — mineure — l'analyse consigne ses entrées sans les contrôler

- Emplacement : `analyser_hm1_v2.py` l. 167–172.
- Constat : les empreintes des entrées sont consignées, mais un fichier de stimuli d'une autre empreinte que
  `15e9e523…` est accepté. Le commit de l'analyse n'est pas consigné. Le manifeste des traits de l'étape 1 (révision,
  gabarit) n'est pas relu.
- Correction : si le code est rouvert, refuser une autre empreinte de stimuli et consigner le commit. Sinon, ajouter au
  texte que l'empreinte `entrees.stimuli` de la sortie doit être égale à `15e9e523…`, faute de quoi rien n'est lu.

## Récapitulatif

| n° | classe | objet |
|---|---|---|
| CL2H-01 | bloquante | prose à la première personne dans 100 % des stimuli prose, 0 % des qcm : indice de requérant réel dans F |
| CL2H-02 | majeure | sans traits, l'analyse figée ne lit pas V |
| CL2H-03 | majeure | réserve « masse > 0,3 » ni définie ni calculée |
| CL2H-04 | majeure | l'en-tête « ### Instruction » met du format dans le style |
| CL2H-05 | mineure | P0 à 3 000 pas contre 20 000 pour la sonde |
| CL2H-06 | mineure | calibrage non reproductible ; R2 sous l'hypothèse nulle ≈ 4 % |
| CL2H-07 | mineure | lanceur : texte scellé non lié au COMMIT |
| CL2H-08 | mineure | V moyenne par cellule, F × K, C × K, K par système non rapportés |
| CL2H-09 | forme | commentaires du lanceur et de l'amorce, libellés, empreinte tronquée |
| CL2H-10 | mineure | analyse sans contrôle de l'empreinte des stimuli ni commit consigné |

**Chemin le plus court vers le scellement, sans toucher au code ni aux empreintes :** CL2H-01 en correction minimale,
CL2H-02 en option (b), CL2H-03 en définition écrite, CL2H-04 déclarée, CL2H-06, CL2H-07 (vérification consignée), CL2H-09
pour le texte et CL2H-10 par une phrase. Le commit `0c77c997` reste alors valable. Si l'on rouvre le code, pour la
correction préférée de CL2H-01 ou pour CL2H-02 (a), le différentiel doit être relu par un sous-agent neuf avant
scellement.

## Ce que je n'ai pas pu vérifier (hors des fichiers listés)

- La banque `confrontation-v1` et les traits `traits-16384` : présence et équilibre, révision au manifeste.
- La tokenisation réelle de « Yes » et « No » par Llama 3.1 (aucun tokeniseur chargé). La garde de la mesure arrête le
  run sinon.
- La ligne GO-2026-10-25-03 et son plafond.
- Le rapport de lecture `788fc409…`.

Scripts de vérification (temporaires, hors du dépôt), dans
`/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/verif-hm1-v2/outils/` :
`proprietes.py`, `regle.py`, `convergence.py`. Reconstruction des stimuli dans
`/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/verif-hm1-v2/reconstruit/`.
