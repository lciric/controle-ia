# Traitement de la contre-lecture R2 du lanceur v2 des notations — v1

Session 15, 2026-10-17. Rapport : `rapport-R2-lanceur-v2-v1.md` (même dossier), sous-agent neuf `abcf58405d69cf54f` ;
18 constats : 0 bloquant, 3 majeurs (LV-01, LV-02, LV-04), 9 mineurs, 6 pour information. Pièces relues : lanceur v2
`964ce4ca…`, banc v2 `1c0d6670…`, plan v2 `2b100bb4…` ; pièces corrigées : celles de ce dossier, au commit C3 (empreintes
dans leurs sceaux). Tous les constats sont acceptés ; LV-02 est un nœud pour Lazar, traité par l'option recommandée en
attendant sa décision (elle ne joue qu'en relancement, qui demande de toute façon son accord, R-185).

| Id | Sort | Ce qui a changé | Où c'est éprouvé |
|---|---|---|---|
| LV-01 | accepté | prix fini et strictement positif (`math.isfinite`, `p > 0`), en plus de « nombre non booléen » | O01 : offres à 0, −0,5, `-Infinity`, `true`, `"0.9"`, toutes moins chères que 112, écartées ; mutants M01, M02, M03 attrapés par O01 |
| LV-02 | accepté, **nœud** | routine : `machine_id` et `host_id` archivés dans `offre.json` et écrits dans la ligne des conformes ; option (a) recommandée : en relancement, offres de la machine ou de l'hôte de l'instance du premier lancement écartées (relus en forme filtrée ; instance absente, machine ou hôte illisibles : code 2) ; offres écartées écrites | R01 (seule offre sur la machine du premier : code 3, offre 111 écartée écrite), R02 (autre machine prise), R03 (même hôte écarté), R04 (machine illisible), R05 (instance absente de la liste), R06 (premier lancement : rien d'écarté) ; mutants M06, M14 attrapés |
| LV-03 | accepté | étape 2 : `PRIX_MAX`, `HEURES_CREDIT`, `PLAFOND_GO`, `PLAFOND_SURVEILLANCE_S`, `FILTRE`, `ARRETEES_TOLEREES` aux mêmes lignes que `lancer_notations_v1.sh` versé à S, sinon code 2 ; plan : la phrase du préenregistrement porte sur la copie v1, le v2 lui est lié mécaniquement | K01 (PRIX_MAX à 1,40 dans un lanceur versé et scellé à C3 : code 2) ; cas sains P00 et suivants ; mutant M07 attrapé |
| LV-04 | accepté | artefacts ajoutés pour les cinq gardes nouvelles | O01 (prix booléen, texte), O09 (identifiant −9 : « offre choisie illisible »), Q10 (ligne mal formée), Q11 (deux empreintes), Q12 (banc altéré et rescellé, journal à l'ancienne empreinte), Q13 (sceau du lanceur faux à C3) ; quatorze mutants, chacun privé d'une garde nouvelle, tous attrapés (M01 à M14 ; compte ci-dessous) |
| LV-05 | accepté | O08 refait : offres 111 à 1,10 (en tête de liste) et 112 à 1,04, crédit 9,00 : création, « minimum 9.00 USD » ; O08b à 8,99 : code 3 | O08, O08b |
| LV-06 | accepté | P13f joué dans le shell courant (`pushd`, `popd`) ; contrôle du clone des contrôles sur le dossier de traces réel du cas | P13f |
| LV-07 | accepté | 2 ter : exactement trois scripts éprouvés (lanceur v2, banc v2, module commun) ; module commun comparé à sa copie versée à S | Q14 (module absent du journal), Q15 (module sous une autre empreinte) ; mutants M10, M12 attrapés |
| LV-08 | accepté | `offres-relues.json` : extrait de toutes les offres lues (identifiant, machine, hôte, carte, mémoire, cartes, processeur, prix, téléchargement, date de fin), sur tous les chemins où la réponse est une liste ; réponse illisible : 2 000 premiers octets dans `offres-relues-brut.txt` ; versés aux traces | O01 (18 offres relues gardées), O05 (réponse illisible gardée) |
| LV-09 | accepté | conformes : `gpu_ram` nombre fini au moins 79 000 (Mo, comme le filtre), `num_gpus` entier égal à 1 | O01 (40 Go, deux cartes, mémoire nulle, `Infinity`, cartes booléennes, écartées), O10 (seule offre de 40 Go : code 3) ; mutants M03, M04, M05 attrapés |
| LV-10 | accepté | plan : liste « Remplacé dans le plan v1 » (chaîne, appels des étapes 4 et 7, identifiant prévu, veille) | relecture |
| LV-11 | accepté | plan : veille d'avant l'appel au prix plafond, 7,5 × (1,30 + autres projets en marche) + 1,2 USD, plus la marge de R-188 | relecture |
| LV-12 | accepté | plan : « six fois sur huit » (R-178, R-179, R-180, R-182, R-188, R-190) ; correction des comptes de R-188 et R-190 consignée par la ligne R-195 du registre, écrite avant C3 | relecture |
| LV-13 | accepté | plan, étape 4 bis : prix et machine de l'instance créée relus en forme filtrée et consignés ; au-dessus de 1,30 USD : arrêt par identifiant (R10) et nœud ; après un code 4 sans instance : nouvel appel, traces neuves, accord de Lazar | relecture ; appliqué à l'appel |
| LV-14 | accepté (routine) | coût de téléchargement et date de fin écrits dans la ligne des conformes et dans `offre.json` ; à consigner aux registres ; aucune borne ajoutée (ce serait changer le filtre : nœud) ; réserve écrite au plan | O01 (ligne des conformes) |
| LV-15 | accepté | C3 ne touche que le dossier v3 (sinon code 2) ; copie du sommet du dépôt distant égale au lanceur exécuté (sinon code 2) ; plan : un seul commit C3 pour tout le dossier, registres dans un commit suivant | Q16 (C3 qui touche un autre fichier), Q17 (version suivante au sommet du distant) ; mutants M08, M09 attrapés |
| LV-16 | accepté | en-tête du banc et plan : N06 retiré, couvert par O03 | relecture |
| LV-17 | accepté | Q02, Q03, Q04 : motifs propres à leur sous-garde (« dernière ligne non conforme », « éprouvé sous 7777 », « ligne d'échec avant le verdict ») | Q02, Q03, Q04 |
| LV-18 | accepté | dossier de traces purement numérique refusé (forme du v1) | A01 (dossier numérique), A02 (trois arguments, forme du v1) ; mutant M13 attrapé |

**Mutants** (R5 ; sortie de chaque banc hors dépôt, bloc-notes de la session, `mutants-v2/`) : chaque mutant retire une garde
nouvelle du lanceur corrigé ; le banc v2 corrigé doit compter au moins un cas non conforme. Résultat : M01 prix booléen (O01) ;
M02 prix positif (O01) ; M03 nombre fini (O01) ; M04 mémoire de 80 Go (O01, O10) ; M05 une carte (O01) ; M06 exclusion en
relancement (R01, R02, R03) ; M07 constantes du v1 (K01) ; M08 C3 hors du dossier v3 (Q16) ; M09 sommet du distant (Q17) ;
M10 trois scripts (Q14) ; M11 lignes mal formées (Q10, Q11) ; M12 empreintes éprouvées (Q03, Q12, Q15) ; M13 traces
numériques (A01) ; M14 machine illisible (R04). Quatorze sur quatorze attrapés.

**Relecture courte des corrections** (sous-agent neuf `a30d7b063bcd176a4`, rapport `relecture-courte-lanceur-v2-v1.md`, même
dossier) : 13 constats, 0 bloquant, 0 majeur, 7 mineurs (RC-01 à RC-07), 6 pour information (RC-08 à RC-13). Tous acceptés :

| Id | Sort | Ce qui a changé | Où c'est éprouvé |
|---|---|---|---|
| RC-01 | accepté | identifiants des offres lues tous distincts, sinon code 2 « offres : identifiant en double » (garde du v1, perdue dès le v2 relu) | O11 ; mutant M15 |
| RC-02 | accepté | en relancement, une offre dont la machine ou l'hôte n'est pas un entier lisible est écartée ; comparaison d'entiers | R07 (offre sans machine ni hôte, moins chère, écartée), R08 (machine 7001.0, écartée) ; mutant M16 |
| RC-03 | accepté en partie | différentiel de C3 sans détection des renommages (`--no-renames`), échec de `git diff` non avalé (piège d'erreur, code 2) ; **refusé** : le contrôle « différentiel vide », inatteignable par construction (C3 est le commit qui ajoute le sceau du lanceur) et donc sans artefact possible (R5) | Q16b (C3 qui déplace un fichier du dossier v2) ; mutant M17 |
| RC-04 | accepté | plan, étape 4 bis : prix relu comparé au prix de la ligne « offre choisie » ; plafond et crédit recalculés au prix relu ; arrêt par identifiant et nœud hors bornes | relecture ; appliqué à l'appel |
| RC-05 | accepté | plan : « change le lanceur et ce qui en découle » ; « règle du préenregistrement ; lanceur v2 en mode relance, avec l'exclusion de LV-02, nœud » ; « 4 bis, plus prix et machine » | relecture |
| RC-06 | accepté | plan et question à Lazar : après une instance perdue qui aurait disparu de la liste, ce lanceur refuse la relance ; options écrites (l'accepter, ou lire machine et hôte dans l'`offre.json` versé du premier lancement, par un lanceur v3) | nœud LV-02 |
| RC-07 | accepté | — (le lanceur gardait déjà l'extrait sur le chemin du code 3) ; artefact ajouté | O04 (extrait gardé sans offre conforme) ; mutant M18 (extrait écrit seulement s'il existe une offre conforme), attrapé |
| RC-08 | accepté | artefacts ajoutés : `offre.json` lu (machine 7100, hôte 8100) ; un cas par constante du devis et du filtre | O01 ; K02 à K06 ; mutants M19, M20 |
| RC-09 | accepté | journal officiel produit avec le banc du dépôt, après toutes les corrections ; copie du bloc-notes mise à jour | journal versé |
| RC-10 | accepté | R-195 écrite avant C3 | registre |
| RC-11 | accepté | plan, veille : au moins une offre conforme relue juste avant l'appel | relecture |
| RC-12 | accepté | instance du premier lancement du banc avec un champ secret (recherche des jetons affichés) ; motif propre de P13e | P13e ; « aucun jeton affiché » |
| RC-13 | accepté | C3 fait par `git add docs/procedures/notations-T0.5-v3` seulement | commit C3 |

**Mutants après la relecture courte** (hors dépôt, bloc-notes, `mutants-v2b/` ; générateur versé : `mutants-lanceur-v2-v1.py`) :
les quatorze premiers rejoués sur le banc corrigé, plus six : M15 identifiant en double (O11) ; M16 machine entière en
relancement (R07, R08) ; M17 renommages (Q16b) ; M18 extrait écrit seulement avec une offre conforme (O04) ; M19 `offre.json`
sans machine ni hôte (O01) ; M20 constantes réduites à `PRIX_MAX` (K02 à K06). Vingt sur vingt attrapés
(`mutants-lanceur-v2-v1.txt`).

**Banc corrigé** : 142 cas, 0 non conforme (essai du bloc-notes, 48 s) ; journal officiel `banc-lanceur-notations-v2.log`
(même dossier), produit par le banc du dépôt après toutes les corrections, versé à C3.

**Non vérifiable ici** (rapport, section « Ce que je n'ai pas pu vérifier ») : comportement réel du service de location
(réponse de `create instance --cancel-unavail` dans la fenêtre, offre qui change de prix sans changer d'identifiant, prix nul
ou non fini) ; enchaînement réel des contrôles avant dépense avec le v2 ; volumes réels téléchargés. Réserves écrites au plan.
