# Relecture par Fable des deux contre-lectures de la version 2 (Opus et Argon) — v1

**Qui relit.** Une instance neuve de Fable 5.1, le 28 octobre 2026. Je n'ai écrit ni la conception (v1, v2), ni aucune
contre-lecture. Même modèle que l'auteur de la conception : le risque d'indulgence est traité en section 4.5.

**Fichiers ouverts, et eux seuls**, empreintes vérifiées par `sha256sum` : `conception-affinage-equipe-rouge-v2.md`
(`ba95bb83…`, 1 954 lignes) ; `contre-lecture-opus-v2.md` (`6a622a29…`) ; `contre-lecture-argon-v2.md` (`059ae917…`) ;
`consigne-contre-lecture-affinage-v2.md` ; `consigne-relecture-fable-v2.md` ; les trois rapports de `rapports-v1/` ; les six
fichiers de `lot/` ; la v1 (`conception-affinage-equipe-rouge-v1.md`), ouverte une seule fois pour les lignes 318-330 (liste
du gel v0, troisième rejet). Aucun appel réseau, aucune clé, aucun journal ni invite. « l. » renvoie aux lignes de la v2
telle qu'elle est sur le disque ; les lignes citées par Opus sont exactes (sondage : l. 263, 443, 464, 706, 755, 779, 789,
835, 1313, 1745) ; Argon cite des sections, justes.

---

## 1. Verdicts

**Contre-lecture d'Opus : juste.** Vingt-cinq entrées (seize constats, neuf attaques manquantes) : vingt et une fondées,
trois partiellement fondées (CL2-O-09, CL2-O-16, AM2-O-07), une à vérifier (CL2-O-14), aucune non fondée. Les deux
« bloquants » sont réels et correctement bornés (avant le codage du juge, avant celui de la mémoire). Deux glissements,
sans effet sur le verdict : l'option « différer aussi d'une génération la recombinaison » (CL2-O-07) casserait la condition
« trois générations consécutives » de 6.6 ; et sa table marque AM-A-05 « juste » alors que son propre AM2-O-05 en montre le
trou. Le tableau du traitement (quinze partiels) est le plus exact des deux.

**Contre-lecture d'Argon : juste avec erreurs.** Dix entrées (sept constats, trois attaques manquantes) : huit fondées, deux
partiellement fondées (CL2-A-01, CL2-A-05), aucune non fondée. Le fond est bon et, sur deux points, meilleur que celui
d'Opus (la strate comme unité d'indépendance pour `INTER_STRATE` ; le pas synchrone de déclaration des reprises). Mais :
les deux « bloquants » sont surévalués (une suppression d'une clause et une phrase d'unification) ; le tableau du
traitement dit « rejet 5 fondé » puis CL2-A-07 démontre que la preuve de ce rejet est fausse ; « intégralement codable
après sept corrections » passe à côté de l'amplitude (CL2-O-01) et de la monotonie en espace (CL2-O-02), que le texte
de la v2 porte aux l. 589-594 et 706 ; les nœuds 1 et 5 reçoivent un « d'accord » sans la réserve qu'ils méritent.

**Verdict révisé sur la v2 : prête à coder après corrections — avec une v3 courte avant le juge et la mémoire.** Les trois
défauts porteurs de la v1 sont fermés dans leur architecture ; deux le sont à moitié dans leur texte : la survie certifie
« effet > κδ » mais le proposeur choisit `alpha_refutation`, la faisabilité ne porte que sur la survie, l'arrêt se fait au
premier franchissement et κ = 0 est permis (l. 263, 409-414, 570, 589-594) ; l'empreinte est monotone en δ, mais la
l. 706 lui prête une monotonie en espace qu'elle n'a pas « par construction », et la table de 6.3 repose dessus. S'y
ajoutent une incohérence de texte (le différé d'A-11 contre 5.6, 6.2, 6.4, 6.10), deux objets statistiques indéfinis
(CL2-O-03), deux états impossibles ou indéfinis (confirmation indécise ; reprise « en cours » ou « hors »), un bogue
déplacé (le contenu croissant des lignées) et un trou d'invariant à la frontière des courses. Ce qui se code dès
maintenant est en section 7 ; ce n'est pas rien : l'oracle, le langage, les constructeurs, la course, la machine à
états, le courtier et le banc de mesure de puissance.

---

## 2. Tableau des constats des deux contre-lectures de la v2

Verdicts : **F** fondé, **PF** partiellement fondé, **NF** non fondé, **AV** à vérifier. « Gravité » : la mienne. « Défaut
nouveau ? » : si la correction proposée en créerait un.

### 2.1 Opus — constats CL2-O-01 à 16

| id | verdict | gravité | raison et endroit de la v2 | défaut nouveau ? |
|---|---|---|---|---|
| CL2-O-01 | F | **bloquant** (juge) | `alpha_refutation` est sur la grille publique « fait partie du dessin » (l. 263) et rien ne le fixe ; `RESSERRER_ALPHA(α')` ne dit pas quel alpha (l. 464) ; la faisabilité ne simule que la survie (l. 409-414) ; `JUGER` sort au premier franchissement (l. 589-594), donc `AMPLITUDE_REFUTEE` exige que les deux processus franchissent sur la même grappe ; κ ∈ [0, 1) (l. 570). Avec `alpha_refutation` minuscule, `E_ref` ne franchit jamais et un δ dans ]effet, effet/κ[ survit avec l'aptitude que la puissance simulée à « effet = δ » (gonflé) lui a achetée : la phrase « gonfler δ n'achète plus rien » (l. 1161) n'est vraie qu'avec une puissance de réfutation exigée. L'artefact de D-06 « effet entre κδ et δ → `AMPLITUDE_REFUTEE` ou `REFUTEE` » (l. 1164) échoue sous la règle écrite. | Non. La lecture jusqu'au budget est valide (Ville vaut à tout instant d'arrêt, le budget fixé en est un) et gratuite (épreuve brûlée en bloc l. 619, coût imputé = budget déclaré l. 216). |
| CL2-O-02 | F | **bloquant** (mémoire) | E(f) = mondes où la statistique sur les grappes filtrées viole l'affirmation (l. 704-709). Monotone en δ à espace fixé (E-10 le teste) ; **pas** en espace : la statistique d'un sous-espace n'implique pas celle de l'espace, c'est le paradoxe de Simpson que la v2 traite en C-11. La l. 706 affirme le contraire. Les lignes 1, 3, 5, 6 de la table (l. 719-731), C-09, E-07 et la condition de lignée (l. 779) lisent des inclusions comme des implications ; sur des mondes « mélanges » (l. 701) elles deviennent des coïncidences. | Non pour la couche syntaxique (implication décidable à espace égal). Réserve : la règle « sous-espace d'une loi établie jugé avec le nul décalé » n'a de sens que si CL2-O-11 est corrigé (sinon le décalage est vide). |
| CL2-O-03 | F | majeur (S) | (a) « martingale de permutation sur les seules grappes d'épreuve déjà lues » (l. 571-572) : lu comme test d'échangeabilité de la suite, il n'a aucune puissance contre une association et, par le minimum, éteint tout ; lu comme test séquentiel d'indépendance par permutation conditionnelle, il est correct ; le texte ne tranche pas. (b) Les nuls par permutation sont des nuls à effet nul ; le texte ne dit pas quel élément de B(f) est valide sous « effet ≤ κδ », alors que la certification de la l. 599 l'exige. (c) La statistique « bornée par grappe » n'existe pas si X est constant dans la grappe (descripteur de tâche, clé = tâche, H-1) ni pour CONTRASTE (une grappe est dans S1 ou S2). | Non. |
| CL2-O-04 | F | majeur (invariant) | Mainteneurs « entre les courses » (l. 247) ; taux scellés « jusqu'à la fin de la course » (l. 346-347, 657) ; H-06 « pendant la course » (l. 1438) ; 10.1 n° 8 l'avoue. Un réglage des invites du maison entre deux courses d'après les taux descellés est une sélection d'un agent sur les verdicts, par la main humaine, à l'échelle de la course. F-08 (l. 1313) ouvre une « comparaison entre proposeurs » sans dire qu'elle se tient en étalonnage. | Non : descellement au seul directeur pour le rapport et fiche de changement sur oracle et coût ne font que porter au niveau des courses la décision du directeur (composition sur oracle et coût). |
| CL2-O-05 | F | majeur (élimination d'un concurrent) | Table ligne 1 : `GELEE` en cours protège comme une vérité établie (l. 719) ; `GELER` tranche par « premier reçu de gel » (l. 514-516) ; la faisabilité est simulée à « effet = δ », donc un δ gonflé passe. Gel immédiat de fiches larges = `REDITE_CONCURRENTE` pour les lois étroites et vraies d'autrui. Contredit E-05 (« ne protège que les fiches à vérité établie », l. 1219). | Non pour « les deux sont jugées, chacune paie, crédit partagé ». Réserve : il faut alors écrire qu'une fille commune du recombineur n'est jugée qu'une fois (angle mort H, section 4.3). |
| CL2-O-06 | F | majeur | L. 755 « un transfert vers un domaine moins peuplé exclut moins de mondes et reste neuf » contre l. 779 « contenu strictement croissant entre versions gelées » : la lignée TRANSFERT perd la récompense ; le test sain de F-04 (l. 1288) échoue selon les tailles de domaines. L'annexe dit CL-A-04 « corrigé » alors qu'Argon visait expressément la condition 2 des lignées. | Non (contenu cumulé + cases neuves : la correction d'Argon v1). |
| CL2-O-07 | F | mineur | A-11 « étiquettes diffusées en différé d'une génération » (l. 986) ; 6.4 livre au paquet de g+1 des filles dont `parents` contient les confirmées de g (l. 757). Même objet que CL2-A-01 (Argon). | **Oui** pour l'option « différer aussi la recombinaison » : elle casse « trois générations consécutives » (l. 779). Renoncer au différé (option 1, et Argon) ne crée rien. |
| CL2-O-08 | F | mineur (codabilité) | Tout vérifié : `GELEE_PAR_PLAFOND` (l. 443) absent des statuts (l. 272-273) ; `GELER(f)` appelé après `REFUSEE` (l. 447-450) ; « δ + un pas » sous deux lignes de la table sans ordre (l. 719, 721 ; l. 1204-1205) ; l. 727 muette sur un autre proposeur ; « mémoire persistante » (l. 835) ; « tirée avec s » (l. 789) contre un calendrier scellé à la course (l. 888) ; collision D-6 / D-06 ; nul d'archive déclarable non exclu (4.1 étape 5). | Non. |
| CL2-O-09 | PF | mineur | Fondé : couverture « au moins N_min grappes » (l. 558-560, 772) contre puissance simulée « dans le budget » (l. 412) ; témoins silencieux sur unités fraîches (l. 804) absents du dimensionnement. Partiel : les ombres sont jugées sur les grappes de f (même espace, signe opposé) et n'ajoutent rien au tirage. | Non. |
| CL2-O-10 | F | mineur | « Dessins tirés dans la distribution empirique des fiches gelées » (l. 805) : si δ est redessiné, une confirmée certifiée à « > κδ » peut être fausse au nouveau δ ; la base d'`AUDIT_SYMETRIE` (l. 673) s'en trouve biaisée. Et les témoins silencieux mesurent la stabilité du juge, pas la qualité du pôle : à dire au nœud 1. | Non. |
| CL2-O-11 | F | mineur, mais porteur | Niveau certifié d'une `SURVIVANTE` f' = κδ' (l. 599) ; renforcement : δ > δ' donc max(κδ, κδ') = κδ (l. 643-644) : le décalage est vide. Le même vide rend inopérante la garde proposée par Argon pour AM2-A-02 (« nul décalé à κδ_f' sur l'intersection »). Correction juste : niveau certifié = borne basse scellée du processus de f', lue par le seul juge. | Non. |
| CL2-O-12 | F | majeur | H-03 exige « auteurs du juge et du proposeur maison de lignées différentes » (l. 1408) ; le maison est servi par Opus et Fable (l. 1417) ; le lot dit que le code de la boucle est côté conv-audit (famille Opus) et prévoit un « juge d'une autre lignée encore » (intégration, section 6). Le nœud 4 ne couvre pas l'auteur du juge. | Non. |
| CL2-O-13 | F | mineur (frontière, niveau règle) | G-K1 confronte des traits du schéma A (l. 845-848) ; les traits du schéma B sont des drapeaux du banc (l. 297-304). 8.1 dit que les simulateurs ne touchent aucun moniteur (l. 1586), pas que le banc n'en contient pas. Un test d'architecture suffit. | Non. |
| CL2-O-14 | AV | mineur (gouvernance) | Fait vérifié : l. 1745 résume la règle par « ne pousse pas sur main » alors que le brief dit « tu ne pousses rien » (brief 2 et 6) — la reformulation que le brief (section 7) nomme comme signal. Le préambule (l. 21-27) attribue « livraison sur la branche de travail » à la consigne du directeur sans la citer ; je ne peux pas vérifier cette consigne. Fondé sur le signal, à vérifier sur l'écart. | Non. |
| CL2-O-15 | F | mineur, bloquant pour l'admission | INVARIANCE (l. 287-288) : « l'effet est < δ » sans δ_max est vrai à bon marché ; aucun statut ne dit ce qui l'établit ; −log alpha_survie n'a pas de sens pour elle. Même réserve chez Argon (nœud 8). | Non. |
| CL2-O-16 | PF | mineur, nœud | Fondé : aptitude = −log alpha (l. 609), le recombineur pondère par l'aptitude seule (l. 745), une piste à δ_min sur un espace large vaut une loi forte. Partiel : c'est la règle de la passation (2.2, point 7), et la faisabilité à π_min borne la timidité par le budget (une loi à δ_min exige beaucoup d'unités, jusqu'à U_max). Nœud légitime ; le contenu C(f) est une propriété du dessin, donc le pondérer ne touche pas l'invariant. | Non. |

### 2.2 Opus — attaques manquantes AM2-O-01 à 09

| id | verdict | gravité | raison et endroit | défaut nouveau ? |
|---|---|---|---|---|
| AM2-O-01 | F | majeur (déni de service) | « Couvrir chaque espace gelé … sinon `VIVIER_INSUFFISANT` avant toute lecture » (l. 558-560) ; « arrêt, directeur » (l. 772-773) : F_max fiches sur des espaces rares mais non vides sur le développement (N_min, l. 397) arrêtent la génération de tous. | Non, à condition d'adopter avec elle CL2-A-05 (α_P débité avant le tirage, sinon `NON_TESTABLE` devient une manière de ne pas payer). |
| AM2-O-02 | F | majeur (composition) | La mesure du besoin compte « la part de lois gelées vraies » (l. 504-507) : un affineur qui gèle tout à δ_min sur des espaces larges la maximise. Le directeur a fixé la **source** (oracle et coût), pas la **métrique** : elle doit être préenregistrée et résister à la timidité. La v2 a déjà l'outil (taux par strate de probabilité a priori, l. 796-797, G-05) mais ne le branche pas sur 4.5 ni sur H-05. | Non (contenu et sévérité sont des propriétés du dessin). |
| AM2-O-03 | F | majeur avant tout proposeur modèle | Discernabilité testée sur le contenu des fiches gelées et le comportement (l. 813-815), jamais sur les lots ; un modèle peut reconnaître la statistique des données plantées. La garde « traits rééchantillonnés du développement réel, issues plantées » est cohérente avec la construction des mondes de référence (l. 697-699). | Non. |
| AM2-O-04 | F | majeur (revendications) | J-06 exige que toutes les courses soient rapportées (l. 1521-1522), mais une revendication « cite l'empreinte de sa course » : le contrôle en ligne du taux de fausses découvertes (nœud 2) doit porter sur la réunion des courses. | Non. |
| AM2-O-05 | F | majeur | Même attaque qu'AM2-A-01 (Argon), trouvée indépendamment : `INTER_STRATE` sur deux strates aux marginales décalées donne des survivantes certaines à pleine aptitude ; C-11 dit « survit et c'est juste » (l. 1121-1122). L'amorce de la mémoire avec les contrastes connus est complémentaire de la garde d'Argon (voir 2.4). | Non. |
| AM2-O-06 | F | majeur | Même constat que CL2-A-07 : le tirage « par espace gelé » (l. 558) devient le nul d'archive de g+1 (l. 619-620) ; qui choisit ses espaces à g façonne le nul de g+1, au détriment d'un concurrent. La garde « tirage de base uniforme, seul à alimenter l'archive, plus complément par espace » est meilleure que celle d'Argon (voir CL2-A-07). | Non. |
| AM2-O-07 | PF | mineur | Fondé : `verifier_mouvement` confronte la fiche aux `GELEE` en cours d'autrui et rend un code (l. 476-478, 719). Partiel : l'affineur est isolé (l. 240) et tué au gel (l. 513) ; l'information ne peut sortir que par la forme de la fiche gelée, quelques bits par fiche ; et « toute soumission compte dans Q_max » (l. 402-403) couvre les mouvements si l'on lit « soumission » au sens large — à écrire. | Non. |
| AM2-O-08 | F | mineur (limite déclarée) | H-07 compare l'identifiant **déclaré** par l'environnement (l. 1448) : une substitution non déclarée passe. Aucune garde mécanique n'existe ; la v2 doit le dire en 10.1. | Non. |
| AM2-O-09 | F | mineur | α_alarme réparti entre les classes (l. 1386) ; une faille survivante devient « une famille d'artefacts » après porte (l. 907) ; la liste des objets de la course (l. 886-889) ne nomme pas le catalogue des classes : une classe ajoutée en cours de course dilue l'alarme. | Non. |

### 2.3 Argon — constats CL2-A-01 à 07

| id | verdict | gravité | raison et endroit | défaut nouveau ? |
|---|---|---|---|---|
| CL2-A-01 | PF | majeur (point 3), mineur (points 1-2) | Fondé : le différé d'A-11 (l. 986) contredit 6.2 (« le statut de chacune », l. 685), 6.4 (`fille.parents` au paquet commun, l. 757) et 6.10 (`CONFIRMER` à la clôture de g, l. 877) ; retarder la recombinaison à g+2 casserait les « trois générations consécutives » (l. 779). Fondé et non vu par Opus : aucun statut `CONFIRMATION_INDECISE` (l. 272-273) et `GENERATION(g)` ne relance pas les confirmations en attente de seconde famille (l. 877) — un état impossible. Non fondé : « bloquant » ; une clause supprimée et un statut ajouté. | Non. |
| CL2-A-02 | F | majeur (bloquant pour coder la mémoire, avec CL2-O-02) | (1) Une MODULATION de novo et une fille d'INTERACTION ont la même forme (l. 286) ; 5.7 définit la statistique pour INTERACTION seulement (l. 641-642) ; la coupure de Z n'est figée nulle part (4.3, l. 425-426). Précision nécessaire, pas bloquante. (2) Vérifié : E(fille) \ (E(a) ∪ E(b)) n'est non vide que sur des mondes où a et b tiennent et où l'effet est constant en Z ; la grille de l. 700-701 ne le garantit pas → `SANS_NOUVEAUTE` systématique possible. (3) « Monde non évaluable … ne compte ni dans E(f) ni dans les comparaisons » (l. 708-709) rend l'inclusion dépendante du resserrement. La correction N_w = développement (mêmes grappes et traits, issues synthétiques) est propre, garde les colinéarités exactes et fait disparaître le cas dégénéré. | Non. |
| CL2-A-03 | F | majeur (point 1) ; conditionnel (point 2) | Point 1 : 4.1 étape 7 et 4.2 comptent et simulent sur `f.espace` entier (l. 397, 411-412) alors que 5.7 juge TRANSFERT « hors des espaces des parents » (l. 639-640) : une fille par union de contextes (l. 760-761) passe tout et finit `NON_TESTABLE`. Point 2 : vrai seulement si le décalage de 5.7 cesse d'être vide (CL2-O-11) ; alors la faisabilité doit simuler sous le nul décalé. | Non. |
| CL2-A-04 | F | majeur | La table distingue « `INDECISE` en reprise » (l. 719) et « hors reprise » (l. 729) sans dire quand la bascule a lieu ; 5.4 ne fixe pas le moment de la déclaration (l. 613-615) ; 6.10 lance les proposeurs en parallèle (l. 870). Soit squat gratuit d'une génération (E-08 rouvert), soit perte du droit de reprise. Le pas synchrone `DECLARER_REPRISES` après réception du paquet et avant l'émission est la bonne fermeture. | Non. |
| CL2-A-05 | PF | majeur (point 1) | Fondé : « débité au jugement » (l. 402), « au jugement de la treizième » (l. 1305-1306), `JUGER` sans ordre (l. 876) ; rien ne dit si une `NON_TESTABLE` paie son alpha (l. 583 : « un statut compté » vise le compteur de bits). Partiel : la « fuite » n'en est pas une (tous les statuts sont au paquet) et le sur-engagement est presque impossible sous D-19 — il redevient vivant avec AM2-O-01. Réserve : « ordre des horodatages des reçus » rouvre l'horloge que CL2-O-05 refuse ; rang déclaré ou H(empreinte ‖ s_g). | **Oui** par horloge ; non par rang déclaré. |
| CL2-A-06 | F | mineur | « Zéro fiche jugée alors que des fiches ont été gelées → `AUDIT_SYMETRIE(P)` » (l. 674) : une seule fiche refusée à `VERIFIER` ou `NON_TESTABLE` déclenche l'audit. Le défaut réel est qu'un audit n'est pas ici un test sur fenêtre W comme les autres (G-09). La reformulation précise d'Argon est discutable (« zéro survivante et zéro réfutée » n'est plus la symétrie du soupçon) ; la direction (fenêtre, test) est juste. | Non. |
| CL2-A-07 | F | mineur-majeur | Identique à AM2-O-06. Fondé, et il contredit la ligne « rejet n° 5 fondé » du tableau d'Argon (1.2). Réserve sur la correction : un tirage aléatoire simple « dont seule la taille globale est dimensionnée » pour couvrir les espaces rares à N_min coûte un vivier énorme et change le sens de `VIVIER_INSUFFISANT` ; la version d'Opus (base uniforme alimente seule l'archive, complément ciblé pour la couverture) couvre sans ce coût. | **Partiellement** (coût de vivier) ; non pour la version d'Opus. |

### 2.4 Argon — attaques manquantes AM2-A-01 à 03

| id | verdict | gravité | raison et endroit | défaut nouveau ? |
|---|---|---|---|---|
| AM2-A-01 | F | majeur | Vérifié sur C-11 (l. 1120-1122) : avec deux strates et des grappes permutées **à travers** elles, le décalage de niveau produit une corrélation de rang inter-grappes massive ; « c'est juste » n'est vrai que si l'unité d'inférence est la strate, et deux strates sont deux observations. La garde « strate comme unité, N_min,strate strates » est la bonne ; restreindre à CONTRASTE contre un nul stratifié revient à interdire les affirmations à deux strates, ce qui est juste aussi. Meilleure que l'amorce d'Opus (AM2-O-05), qui lui est complémentaire. | Non. |
| AM2-A-02 | F | majeur (promotion sans découverte) | Argon reconnaît que E(f) ⊊ E(f') tombe en `REDITE` (ligne 1). L'attaque vit par deux voies que la v2 laisse ouvertes : `LIBRE_PROCHE` avec `NUL_INFORME_INDISPONIBLE` jugée sur tout l'espace (l. 645-648), et le renforcement à décalage vide (CL2-O-11). Dans les deux cas une fiche qui chevauche largement une confirmée touche la pleine aptitude en re-testant l'effet connu. La garde « jugement par soustraction d'espace » (comme TRANSFERT en 5.7) est juste ; sa variante « nul décalé à κδ_f' » est vide tant que CL2-O-11 n'est pas corrigé. C'est 10.1 n° 9 devenu une attaque. | Non (avec CL2-O-11). |
| AM2-A-03 | F | mineur | `MIROIR` est défini syntaxiquement « mêmes variables (à classe près) » (l. 720) avec des classes **globales** (l. 711-713) ; deux traits colinéaires sur `f.espace` seulement échappent au test. Le dommage est limité (un miroir faux est réfuté et paie son alpha ; α_P somme tout) mais la précision est juste et peu coûteuse ; le « signe effectif compte tenu du signe de la corrélation » est une bonne addition. | Non. |

**Décomptes.** Opus, 25 entrées : 21 fondées, 3 partiellement fondées (CL2-O-09, CL2-O-16, AM2-O-07), 0 non fondée,
1 à vérifier (CL2-O-14). Argon, 10 entrées : 8 fondées, 2 partiellement fondées (CL2-A-01, CL2-A-05), 0 non fondée,
0 à vérifier. Gravités que je déplace : CL2-A-01 et CL2-A-02 de « bloquant » à « majeur » ; CL2-A-07 de « mineur » à
« mineur-majeur » ; AM2-O-01 et AM2-O-02 que je tiens pour majeurs ; CL2-O-11 « mineur » mais porteur (il vide deux gardes).

---

## 3. Le traitement des constats de la v1 : où les deux rapports divergent, et qui a raison

| constat de la v1 | Opus | Argon | mon tranchement, avec la preuve |
|---|---|---|---|
| CL-O-04 (amplitude) | partiel (CL2-O-01) | juste | **Opus.** L. 263 (`alpha_refutation` au choix du proposeur), l. 409-414 (faisabilité de la survie seule), l. 589-594 (arrêt au premier franchissement), l. 570 (κ = 0 permis). |
| CL-O-03 / CL-A-07 (empreinte) | partiel (CL2-O-02) | juste | **Opus.** L. 706 affirme une monotonie en espace que la définition de l. 704-705 ne donne pas ; C-11 en est la preuve interne. Argon le frôle (CL2-A-02 point 3) sans le voir. |
| CL-O-01 (mémoire, priorité) | partiel (CL2-O-05) | juste | **Opus.** L. 515 « premier reçu de gel » ; Opus v1 demandait une priorité déterministe par empreinte, et l'horloge se gagne en gelant vite. |
| CL-A-04 (TRANSFERT) | partiel (CL2-O-06) | juste | **Opus.** L. 755 contre l. 779 ; Argon v1 visait expressément la condition 2 des lignées et ne vérifie pas son propre point. |
| AM-A-01 point 2 / rejet 5 (archive) | preuve du rejet fausse, conséquence bornée | rejet fondé, puis CL2-A-07 | **Opus**, et Argon sur le fond malgré son tableau. Sous D-19 (l. 558) le tirage est dimensionné par espace gelé ; « union de tirages non sélectionnés par les fiches » (l. 1868) est faux ; la dépendance porte sur des choix faits avant les verdicts, pas sur des verdicts : le rejet devient « partiellement fondé », avec garde (base uniforme). |
| AM-A-05 (Simpson) | juste, puis AM2-O-05 | partiel (AM2-A-01) | **Argon.** Le traitement par le niveau déclaré ouvre la porte inverse ; la table d'Opus est incohérente avec son propre AM2-O-05. |
| AM-A-06 (échangeabilité) | partiel (CL2-O-03) | juste | **Opus.** L. 571-572 ne tranche pas entre deux lectures dont l'une éteint le juge. |
| CL-O-10 (c) / AM-O-08 (invariant) | partiel (CL2-O-04) | juste | **Opus.** « Jusqu'à la fin de la course » (l. 346-347, 657) et « entre les courses » (l. 247) laissent le réglage entre deux courses hors de toute garde ; 10.1 n° 8 l'admet. |
| CL-O-16 (audits comme tests) | juste | partiel (CL2-A-06) | **Argon.** La condition « zéro fiche jugée » (l. 674) n'est pas un test. Mineur. |
| CL-O-25 (confirmation) | partiel (normalisation absente de 4.1) | partiel (statut de confirmation indécise) | **Les deux**, pour des raisons différentes et complémentaires. Vérifié : « normalis » n'apparaît qu'à la l. 744. |
| AM-O-06 (différé) | partiel (CL2-O-07) | partiel (CL2-A-01) | **Les deux.** Seule correction sans défaut nouveau : supprimer le différé. |
| CL-O-06 (juger sur le neuf) | partiel (CL2-O-11) | partiel (AM2-A-02) | **Les deux**, convergents : le décalage est vide et `LIBRE_PROCHE` sur tout l'espace est une récolte d'aptitude. |
| Rejets 1, 2, 3, 4, 6 | fondés | fondés | **Fondés**, je confirme : minimum (min_j E[j] ≤ E[j*], Ville) ; aptitude = propriété du dessin (P-3, alpha public l. 344) ; v1 l. 325-326 sans la mesure ; unités non lues fonction des temps d'arrêt ; pénalité = sélection sur verdict. |
| Codabilité | juge, mémoire, oracle « à κδ près » pas encore codables | « intégralement codable » après sept corrections | **Opus.** Argon ne corrige ni l'amplitude ni la bibliothèque ; l'oracle « vraie à κδ près » au niveau `INTER_STRATE` n'est défini nulle part (l. 792, 1578). |
| Ordre de construction (8.4) | juge et mesure de puissance avant mémoire et recombineur | « excellent » tel quel | **Opus**, avec une nuance : une course et une machine à états minimales (graines, manifeste, reçus) sont nécessaires pour que la mesure de puissance soit reproductible ; les coder minces, d'abord. |

Résultat : sur les quinze traitements qu'Opus tient pour partiels, je confirme quatorze (CL-O-19 reste « à vérifier ») ;
sur les quatre d'Argon, je confirme quatre. Argon tient pour justes au moins sept traitements qui ne le sont pas.

---

## 4. Convergences, divergences, angles morts, défense de l'auteur, indulgence

### 4.1 Les convergences les plus fortes (trouvées indépendamment, exactes, lourdes de conséquences)

1. **La règle d'arrêt du juge et `alpha_refutation`.** Opus (CL2-O-01, désaccord sur le nœud 11) et Argon (nœud 11 :
   « doit être la règle par défaut », production comprise) disent la même chose avec la même preuve : lire jusqu'au budget
   ne coûte ni vivier (brûlage en bloc) ni coût imputé, et sans cela `AMPLITUDE_REFUTEE` est presque inatteignable. Opus
   ajoute ce qu'Argon ne voit pas : tant que `alpha_refutation` est au proposeur et que la réfutation n'a pas de puissance
   exigée, l'amplitude n'est pas certifiée. La fermeture de D-1 n'est pas finie.
2. **`INTER_STRATE` : le paradoxe de Simpson blanchi à pleine aptitude** (AM2-O-05 ≡ AM2-A-01). Même attaque, mêmes
   endroits (C-11, 5.2), deux gardes compatibles ; celle d'Argon (la strate comme unité, N_min,strate) est la structurelle.
3. **Le tirage par espace gelé façonne le nul d'archive** (AM2-O-06 ≡ CL2-A-07), et le rejet n° 5 de l'annexe repose
   sur une preuve fausse sous la v2 elle-même. Garde commune : un tirage de base non ciblé, seul à alimenter l'archive.

Ensuite : le différé d'A-11 incohérent avec 5.6, 6.2, 6.4, 6.10 (CL2-O-07 ≡ CL2-A-01) ; les mondes de référence
sous-spécifiés pour que les relations de la mémoire soient des implications (CL2-O-02 ≈ CL2-A-02 points 2-3) ;
INVARIANCE sans plafond (CL2-O-15 ≡ réserve d'Argon au nœud 8) ; « juger sur le neuf » incomplet (CL2-O-11 ≈ AM2-A-02 ≈
CL2-A-03) ; CL-O-25 partiel chez les deux ; la frontière respectée selon les deux (je ne trouve rien non plus).

### 4.2 Divergences

- **Gravité du différé** : bloquant (Argon) contre mineur (Opus). Opus : une suppression suffit.
- **Correction du différé** : Argon supprime ; Opus offre aussi « différer la recombinaison », qui casse 6.6. Argon.
- **Rejet n° 5** : Opus le dit non fondé dans sa preuve ; Argon le dit fondé puis le réfute. Opus (et Argon malgré lui).
- **Codabilité et ordre de construction** : voir section 3. Opus.
- **Nœud 1** : Argon sans réserve ; Opus avec (témoins silencieux = stabilité du juge). Opus.
- **Nœud 5** : Argon « déjà actée » ; Opus « métrique à préenregistrer, qui ne récompense pas la timidité ». Opus : la
  décision du directeur fixe la source de la mesure, pas sa formule.
- **Ordre du débit d'α_P** : Argon par horodatage des reçus ; Opus refuse l'horloge (CL2-O-05). Opus ; rang déclaré.
- **Garde du tirage d'épreuve** : Argon, aléatoire simple à taille globale ; Opus, base plus complément. Opus (coût).
- **Les 33 attaques** : Opus trouve sept gardes dont le test ne sépare pas sain et artefact ; Argon trois. Les sept
  d'Opus sont exactes.
- **Proportion** : Opus veut limiter `SUITE_INCOMPLETE` aux modules actifs de la course (« plus de 300 tests » est une
  estimation, non un chiffre du texte : 89 gardes × trois ou quatre tests) ; Argon ne le voit pas. Opus.

### 4.3 Ce que les deux ont manqué (défauts de la v2 ; aucun bloquant ; A, B, F changent une garde ou un contrat)

- **A. Les ombres-miroir n'ont ni statut en mémoire, ni budget, ni place au paquet.** `JUGER(ombre(f))` (l. 876) produit
  un statut ; la table de 6.3 agit sur « chaque fiche gelée f' de l'archive » ; une ombre `REFUTEE` bloque par inclusion
  (voulu ?), une ombre `INDECISE` n'a pas de proposeur pour la ligne 11 ; rien n'exclut les ombres d'α_P ni du paquet
  comme CC-A le fait pour les témoins. Texte.
- **B. Reprise et nul d'archive.** Une `INDECISE` reprise à g+1 continue ses processus (l. 613-615) ; l'élément « nul
  d'archive » de B(f) à g+1 est construit sur l'épreuve de g, qui contient les unités que la fiche a elle-même lues
  (l. 619-620). Le produit continué mélange deux nuls d'archive dont le second dépend des lectures de la fiche : c'est le
  cas que CL-O-14 voulait exclure, revenu par la reprise. Statisticien.
- **C. La mémoire pendant une génération d'étalonnage.** 6.7 dit que l'étalonnage « ne nourrit pas » la mémoire de
  production (l. 799) ; il ne dit pas si l'affineur en étalonnage **consulte** la mémoire de production. S'il ne la
  consulte pas, ses codes `REDITE` diffèrent et la génération est reconnaissable ; s'il la consulte, les fiches
  d'étalonnage sont conditionnées à l'archive réelle. À écrire. Texte.
- **D. « Faisabilité strictement supérieure »** (l. 730, 1221) n'est pas un ordre : la faisabilité est un prédicat à
  trois parties ; seule la puissance simulée est un nombre. Texte.
- **E. `H(s_g ‖ sel)`** (l. 552) : « sel » n'est défini nulle part ; avec CL2-O-08 (« tirée avec s »), le secret de course
  et le secret de génération sont à distinguer par leurs noms. Texte.
- **F. `AUDIT_RETRAITS`** (l. 1247) : « si un proposeur en accumule » sans seuil ni test, alors que G-09 fait de chaque
  audit un test préenregistré. Même défaut que CL2-A-06. Texte.
- **G. Proportion de l'étalonnage.** Le proposeur en étalonnage reçoit le paquet de la dernière génération de
  **production** (l. 800-801) : confirmées réelles, lots plantés. Si cette tension rend l'étalonnage reconnaissable,
  `GENERATION_RECONNUE` invalide la mesure du proposeur (l. 815-816), donc la mesure de composition que le directeur a
  choisie. À mesurer en 8.3 avant toute lettre. Texte.
- **H. Filles communes et squat.** Avec CL2-O-05, deux proposeurs qui gèlent la même fille commune sans mouvement seraient
  jugés deux fois : une fille commune est jugée une fois, créditée au recombineur (F-08) ; une fille amendée est une fiche
  distincte. Texte.

### 4.4 La position de l'auteur : où la v2 a raison contre ses critiques

- **Les rejets 1, 2, 3, 4, 6 tiennent** ; les deux contre-lecteurs et moi les confirmons avec les mêmes preuves.
- **D-22 c (routage sur le signe refusé)** et **D-22 a (aucune pénalité automatique)** : confirmés par les deux ; je
  confirme ; CL2-O-04 n'est que la logique de D-22 a portée entre deux courses.
- **Contre Argon sur les « bloquants »** : CL2-A-01 et CL2-A-02 point 1 sont des phrases à unifier ; l'intention de la v2
  est cohérente (seules les confirmées ensemencent, à la clôture de g).
- **Contre Opus** : CL2-O-16 suit la règle de la passation (2.2 point 7), le lieu de la question est un nœud ; AM2-O-07 est
  un canal de quelques bits par fiche, l'affineur étant isolé et tué au gel ; en CL2-O-09, les ombres partagent les grappes
  de f.
- **Sur CL2-O-14** : l'auteur a tout déclaré (préambule, 10.3) ; l'écart n'existe que si la consigne du directeur n'a pas
  dit « branche de travail », ce que je ne peux pas vérifier.
- **Le minimum des processus** reste valide (Opus 1.3 point 1, Argon CL-A-01, moi) ; il manque toujours le statisticien.

### 4.5 Signaux d'indulgence sur moi-même

- Je tranche presque toutes les divergences pour Opus et contre Argon : les erreurs sont chez Argon et chacune cite une
  ligne, mais c'est aussi le motif qu'une préférence de style produirait. Le lecteur jugera sur la section 3.
- J'ai baissé deux « bloquants » d'Argon et gardé deux « bloquants » d'Opus. Critère : un bloquant est un défaut qu'un
  codeur ne peut pas arbitrer seul ; une clause à supprimer n'en est pas un. Si le directeur compte « bloque le codage de
  la confirmation », CL2-A-01 point 3 redevient bloquant.
- J'ai défendu l'auteur (mon modèle) sur CL2-O-16 et AM2-O-07 ; je les ai laissés « partiellement fondés ».
- Sur la gouvernance (CL2-O-14), je renvoie au directeur, comme le troisième rapport v1 : le fait nu est que la v2 a été
  livrée sur une branche et que 10.3 reformule la règle.

---

## 5. Les treize nœuds, et ceux qu'ils ajoutent — ma position

1. **Régime des témoins** : d'accord avec réserve (Opus). Dire au directeur que les témoins silencieux mesurent la
   stabilité du juge, non la qualité du pôle ; ne pas redessiner δ (CL2-O-10) ; la lettre « à chaque génération » est tenue
   nominalement.
2. **α global** : d'accord ; le contrôle en ligne porte sur la réunion des courses (AM2-O-04).
3. **COMPOSITION retirée** : d'accord.
4. **H-04** : d'accord avec réserve : étendre à l'auteur du juge et du noyau (CL2-O-12) ; le lot suggère une troisième
   lignée (« juge d'une autre lignée encore »), à confirmer.
5. **Composition par l'oracle** : d'accord avec réserve : la décision du directeur fixe la source ; la métrique doit être
   préenregistrée, par strate a priori et pondérée par le contenu, sans jamais un verdict (AM2-O-02).
6. **Critère du duel** : d'accord, et urgent : le cadre dit que le duel « mesure déjà » en fiches promues par dollar
   sous un accord de dépense existant (intégration, section 9) ; à aligner sur la décision du directeur.
7. **Banque distincte de la famille tenue à l'écart** : d'accord ; l'enjeu est confirmé par le lot (« banque scellée v6,
   famille tenue à l'écart », intégration section 8).
8. **INVARIANCE** : d'accord avec réserve : δ_max, statuts propres, aptitude = −log alpha_refutation (les deux).
9. **Isolation des publiés** : d'accord.
10. **C_max** : d'accord.
11. **Règle d'arrêt** : **en désaccord** avec la recommandation de la v2 (« en étalonnage, puis décider ») : lecture
    jusqu'au budget partout, par défaut, et `alpha_refutation` à la course (Opus, Argon). Argon ajoute « ou jusqu'à ce que
    `E_ref` ne puisse plus franchir dans le budget restant », calculable pour une statistique bornée : optionnel.
12. **Gouvernance** : d'accord avec réserve : couvrir la v2 et la reformulation (CL2-O-14).
13. **L'utilisateur de la poussée** : d'accord.
- **Nœud 14 (Opus) — l'invariant entre deux courses** : d'accord ; c'est un nœud parce qu'il lie le directeur lui-même
  (qui lit les taux descellés, et sur quoi un changement de configuration peut se fonder).
- **Nœud 15 (Opus) — aptitude et contenu** : d'accord comme nœud, priorité basse ; ma recommandation : garder l'aptitude
  de la passation, rapporter le contenu à côté, et décider seul de la pondération du recombineur.
- **Nœud 16 (Opus) — κ_min et `alpha_refutation` à la course** et **nœud 14 d'Argon — `INTER_STRATE` et `LIBRE_PROCHE`** :
  d'accord, et je les fusionne en un seul nœud « sémantique des statuts » avec le nœud 11 et le nœud 8 : ce qu'une
  survivante certifie (κ_min, réfutation exigée, règle d'arrêt), sur quelle unité (strate ou grappe), sur quel espace (neuf
  ou entier), et pour quelle forme (INVARIANCE). Une décision, pas quatre.

---

## 6. Liste consolidée des corrections pour une version 3, dans l'ordre

Coût : **T** texte, **C** code, **S** statisticien, **D** décision du directeur.

1. **Fermer l'amplitude.** `alpha_refutation` hors du menu (paramètre de course, ou lié à `alpha_survie`) ; `RESSERRER_ALPHA`
   ne vise que `alpha_survie` ; faisabilité (iv) : puissance de réfutation ≥ π_min à « effet = κδ », sinon
   `REFUSEE_REFUTATION_INFAISABLE` ; lecture jusqu'au budget partout ; κ_min > 0 en section 9 ; tests de D-06 refaits.
   — CL2-O-01 ; nœuds 11 et 16. **T + S + D.**
2. **Spécifier les mondes de référence et refonder les relations de la mémoire.** Mondes = grappes et traits exacts du
   développement, issues synthétiques (N_w = développement) ; grille d'issues contenant, pour chaque structure, l'effet
   principal pur ; retrait de la l. 706 ; couche syntaxique (même forme, variables à classe près, niveau, espace égal :
   l'ordre de δ décide redite, renforcement, `REFUTEE_PAR_INCLUSION`) et mondes réservés aux quasi-redites ; test de
   non-monotonie en espace ajouté à E-10 ; ordre de priorité des lignes de la table ; statistique de MODULATION unifiée,
   coupure de Z figée au gel v0 ; colinéarité locale pour `MIROIR` ; « faisabilité strictement supérieure » défini.
   — CL2-O-02, CL2-A-02, CL2-O-08 (table), AM2-A-03, angle mort D. **T + C.**
3. **Compléter « juger sur le neuf ».** Niveau certifié d'une loi établie = borne basse scellée de son processus (lue par
   le seul juge) ; `LIBRE_PROCHE` sans nul informé et toute restriction d'une établie jugées par soustraction d'espace ou
   sous ce nul décalé réel ; faisabilité (4.1, 4.2, 4.4) alignée sur le domaine et le nul de 5.7. — CL2-O-11, AM2-A-02,
   CL2-A-03. **T + S (+ C).**
4. **Définir la bibliothèque du juge élément par élément.** Le nul exact de chaque élément ; l'élément « intra-épreuve » =
   test séquentiel d'indépendance par permutation conditionnelle aux grappes lues (attribution à vérifier) ; l'élément qui
   porte le décalage κδ ; statistiques par paires de grappes disjointes (X constant par grappe ; CONTRASTE) ;
   `INTER_STRATE` avec la strate comme unité (N_min,strate) ou restreint ; `BIBLIOTHEQUE_ETEINT` dès la course ; la
   continuation à la reprise avec un nul d'archive changé (angle mort B). — CL2-O-03, AM2-O-05, AM2-A-01. **T + S.**
5. **Squat et priorité dans la génération.** Entre proposeurs différents, aucun refus entre gelées en cours (les deux
   jugées, chacune paie, crédit partagé) ; même proposeur : refus ; priorité par H(empreinte ‖ s_g), jamais l'horloge ; à
   l'échelle 1 la mémoire des mouvements ne voit que l'archive close ; chaque mouvement compte dans Q_max ; une fille
   commune est jugée une fois. — CL2-O-05, AM2-O-07, angle mort H. **T + C.**
6. **Confirmation, reprise, budget : états codables.** Différé d'A-11 supprimé ; statut `CONFIRMATION_INDECISE` et relance
   dans `GENERATION(g)` ; pas synchrone `DECLARER_REPRISES` après le paquet, avant l'émission (`EN_REPRISE` / `RETIREE`) ;
   α_P débité à la sortie de `VERIFIER`, dans l'ordre d'un rang déclaré, avant tout tirage, `NON_TESTABLE` compris ;
   `GELEE_PAR_PLAFOND` ajouté ; `GELER` sur `EN_AFFINAGE` seulement ; ombres : statut, budget, mémoire, paquet définis.
   — CL2-O-07, CL2-A-01, CL2-A-04, CL2-A-05, CL2-O-08, angle mort A. **T + C.**
7. **Tirage d'épreuve et vivier.** Tirage de base non ciblé (stratifié sur les strates fixes seulement), seul à alimenter
   le nul d'archive ; complément par espace gelé pour la couverture, dimensionné au maximum des budgets déclarés sur
   l'espace, témoins silencieux compris ; espace non couvert → `NON_TESTABLE` de ses seules fiches, la génération
   continue ; quota d'épreuve par proposeur, `AUDIT_VIVIER` ; `VIVIER_INSUFFISANT` réservé à l'épuisement réel ; rejet
   n° 5 reclassé « partiellement fondé » dans l'annexe. — AM2-O-06, CL2-A-07, CL2-O-09, AM2-O-01. **T + C.**
8. **Tenir l'invariant entre les courses.** Taux de production descellés au seul directeur, pour le rapport ; rôle
   mainteneur sans lecture (test d'architecture) ; fiche de changement scellée, citant oracle et coût seuls, contre-lue ;
   F-08 restreint au rapport ; suites possibles d'un `AUDIT_*` listées ; revendications sur la réunion des courses ;
   nombre de classes d'artefacts fixé à la course. — CL2-O-04, AM2-O-04, AM2-O-09 ; nœud 14. **T + D.**
9. **Préenregistrer la mesure par l'oracle.** Métrique de composition et de besoin par strate a priori, pondérée par le
   contenu et la sévérité, rapportée avec la part de lois fausses ; discernabilité sur les lots ; monde planté à traits
   rééchantillonnés du développement réel, issues plantées ; témoins silencieux redessinés sans toucher δ ; nœud 1
   reformulé ; mémoire en étalonnage définie ; risque de `GENERATION_RECONNUE` mesuré en 8.3. — AM2-O-02, AM2-O-03,
   CL2-O-10, angles morts C et G ; nœud 5. **T + D.**
10. **Lignée et contenu.** Condition de lignée = cases neuves à chaque maillon et contenu cumulé croissant ; contenu
    rapporté à côté de l'aptitude ; pondération du recombineur par le contenu en nœud. — CL2-O-06, CL2-O-16 ; nœud 15.
    **T + D.**
11. **Lignées des rôles.** Nœud 4 étendu à l'auteur du juge et du noyau ; `LIGNEE_AUTEUR_JUGE` attesté dans la course ;
    AM2-O-08 déclaré en 10.1. — CL2-O-12, AM2-O-08. **T + D.**
12. **INVARIANCE bornée avant admission.** δ_max, statuts propres, aptitude = −log alpha_refutation. — CL2-O-15 ; nœud 8.
    **T + D.**
13. **Audits comme tests, complété.** `AUDIT_SYMETRIE` « zéro jugée » et `AUDIT_RETRAITS` sur fenêtre W, préenregistrés.
    — CL2-A-06, angle mort F. **T.**
14. **Cohérences de texte.** Renommer les décisions (DV-n) ; « mémoire persistante » ; « tirée avec s » et « sel » ;
    nul d'archive exclu des nuls déclarables ; normalisation avant dérivation écrite en 4.1. — CL2-O-08, CL-O-25,
    angle mort E. **T.**
15. **Frontière, schéma B.** Test d'architecture « le banc ne contient ni moniteur ni agent » ; sinon G-K1 étendu aux
    drapeaux. — CL2-O-13. **T + C.**
16. **Gouvernance.** Citer verbatim la consigne de livraison ; corriger la l. 1745 ; nœud 12 sur la v2. — CL2-O-14. **T + D.**
17. **Proportion.** Première course limitée aux modules actifs ; `SUITE_INCOMPLETE` évaluée sur leurs gardes ; schéma B,
    INVARIANCE, héritage, détecteur d'injection, témoins silencieux après la première expérience ; ordre de construction :
    oracle, langage, constructeurs, course et machine à états minces, juge et mesure de puissance, puis mémoire, affineur-M,
    routage, 8.3, recombineur. — Opus §6, Argon 4.3. **T.**

Les points 1 à 7 rendent le juge, la mémoire et la génération codables ; 8, 9, 11, 12 sont des nœuds ; 13 à 17 sont du
texte. Les corrections qui créeraient un défaut nouveau et ne sont pas reprises : différer la recombinaison (CL2-O-07,
option 2) ; débit d'α_P par horodatage (CL2-A-05) ; tirage aléatoire simple à taille globale (CL2-A-07).

---

## 7. Ce qui se code dès maintenant, sans attendre la v3

Rien de ce qui suit ne dépend d'une décision ouverte ; chaque pièce porte les paramètres contestés comme lettres.

- **L'oracle du monde jouet et le générateur de lois sur tout le langage** (8.4 étape 1), avec les traits rééchantillonnés
  d'une distribution de développement et les issues plantées (AM2-O-03 dès la conception) ; l'oracle rend « vraie à κδ
  près » au niveau `INTRA_STRATE` ; le niveau `INTER_STRATE` attend le point 4.
- **Le langage formel** : grammaire, listes blanches, niveau obligatoire, validation 4.1 (étapes 1 à 5, 7 à 9) ; l'étape 6
  codée avec `ARRET_NOYAU` sur sous-liste absente.
- **Les deux constructeurs de processus de pari** sur statistique bornée (survie à κδ, réfutation à δ) comme bibliothèque
  paramétrée, κ, `alpha_refutation` et la règle d'arrêt étant des paramètres, lecture jusqu'au budget par défaut ; et le
  **banc de mesure de puissance** sur fiches plantées servies directement au juge (priorité 5 d'Opus) : il mesure le
  risque de 10.1 n° 5 (« presque tout `INDECISE` ») avant toute lettre et avant la mémoire.
- **La course, la machine à états, la chaîne d'empreintes, le reçu, le courtier, l'isolation par fiche, la graine**
  (D-13, D-14 ; étape 4), minces, avec `GELEE_PAR_PLAFOND` dans la liste et `GELER` sur `EN_AFFINAGE` seulement.
- **Le calcul de l'empreinte sur mondes de référence** avec N_w = développement, le test de monotonie en δ (E-10) et son
  frère de non-monotonie en espace ; les **relations** de la table attendent le point 2.
- **Les tests d'architecture** (8.1 point 5) et la convention sain / artefact / exception ; les générateurs d'artefacts des
  gardes syntaxiques (A-03, A-04, B-03, C-05, C-06, C-08, E-09).
- **Ce qui attend la v3** : la table de la mémoire (point 2), la composition de B(f) (point 4), les conditions de lignée
  (point 10), les conditions d'audit (point 13), la métrique d'étalonnage (point 9), le recombineur (après 8.3).

---

## 8. Ce que je n'ai pas pu vérifier

- La consigne exacte du directeur pour la v2 ; l'identité de « l'utilisateur » ; l'état de la branche et de la demande de
  fusion ; le modèle servant au moment de chaque écriture.
- L'existence d'une troisième lignée pour les rôles de contrôle et l'auteur du juge (le lot la suggère).
- La validité statistique : minimum tenu séparément, continuation (y compris avec un nul d'archive changé, angle mort B),
  test séquentiel d'indépendance par permutation, pari sur moyennes bornées décalé de κδ, statistiques par paires de
  grappes ; toutes les attributions de littérature restent « à vérifier ».
- L'oracle « à κδ près » au niveau `INTER_STRATE` ; la perte de puissance réelle : à mesurer en 8.3.
- La compatibilité du code existant (pari apparié borné) avec deux processus, les mondes de référence et la course.
- La comparaison ligne à ligne v1 / v2 au-delà de la liste du gel v0 ; l'invite et le journal d'Argon, non ouverts.

---

Horodatage : écrit le 2026-10-28. Version 1. Rien n'est scellé par son auteur ; aucun fichier hors de la liste de tête n'a
été ouvert ; aucun appel réseau ; aucune clé lue.
