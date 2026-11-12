# Contre-lecture R2 — axe 6, texte II (« domaine de validité des statistiques de détection ») — v5

- Date : 29 octobre 2026, 23 h 02 UTC (`date -u` : Thu Oct 29 23:02:32 UTC 2026).
- Contre-lecteur : sous-agent Claude, modèle Opus 5.5 (identifiant `claude-opus-5-5`). **Neuf, tenu à l'écart** : n'a écrit aucune pièce de la course ; n'est aucun des trois contre-lecteurs précédents (v1 et v2, v3, v4) ; n'a conçu ni lu aucun moniteur ni aucune statistique de surveillance du programme ; n'a lu ni la v2, ni BA-002, ni aucune branche de données, de quarantaine ou de canal.
- Pièces lues, et rien d'autre (dossier `docs/notes/ideation-organisme-v1/course-2/`) :
  - `axe-6-texte-II-v5.md` (198 lignes), pièce contre-lue ;
  - `contre-lecture-axe-6-texte-II-v4.md` (149 lignes), constats CA6v4-01 à CA6v4-15 ;
  - `axe-6-texte-II-v4.md` (182 lignes), comparé par `diff`.
- Empreintes vérifiées (`sha256sum -c <fichier>.sha256`, lancé depuis ce dossier) : les trois « OK ».
  - v5 : `427c6f2215b4df42a318ddccb9e980d60d4ef613f5ee53fe11bb01b9458ae7f3` (conforme à `427c6f22…`).
- Mesure du texte servi (lignes 71 à 174, marqueurs exclus), refaite : 10 602 caractères (`LC_ALL=C.UTF-8 wc -m`), 11 028 octets, 1 849 mots. Conforme à la ligne 9.
- Recherche dans le texte servi des restes et termes exposés (`P_T`, `P_ε`, « ε » nu, poids `w`, « sabotage », « riposte », « agent », « surveillance », « honnête », « cacher », « évasion », « contourner », « attaque ») : aucune occurrence. « Système » n'apparaît que dans les conditions (i), (iii), (iv) de G ; « comportement » seulement dans (v) ; `w` seulement dans le trait linéaire (l. 93).
- Le `diff` v4 → v5 ne touche que les lignes annoncées par la table de traitement (l. 52-68) : aucun changement non déclaré.

## Verdict
**v5 : servable après corrections locales, sans nouvelle contre-lecture complète.** Aucun constat bloquant. Treize des quinze constats de la v4 sont corrigés, deux partiellement (CA6v4-02 : le témoin de garde de la condition (iv) ne viole pas (iv) à la lettre ; CA6v4-13 : « une seule case non vide » ne dit pas de quelle liste). Trois constats nouveaux majeurs, tous hors texte servi et tous en une ou deux lignes : témoin (iv) mal ciblé, contrôle des témoins de garde non placé avant la passe 2, garde G et contrôle lexical sans cas sain ni artefact au sens de R5. Six mineurs. Le texte servi lui-même n'appelle que des retouches mineures.

## Table des constats de la v4

| Constat | Lignes de la v5 | Corrigé | Commentaire |
|---|---|---|---|
| CA6v4-01 « procédé » non testé | 73, 79 | oui | Garde en une phrase ; l'exclusion du procédé est dans (iv). Garde et G coïncident désormais : « opérations sur des lois ou sur des échantillons » ↔ (iv) ; « rien n'est prêté au processus générateur au-delà de sa loi » ↔ (v). La phrase « un système modifiant son comportement » a disparu. |
| CA6v4-02 témoin de garde | 185 | partiellement | Trois témoins, un par condition (i), (iv), (v), dans le même lot, sous la même consigne. Mais le témoin (iv) porte « un procédé de production anodin, **sans rapport avec la question** » : (iv) n'exclut que le procédé par lequel un système produirait **le** déplacement de la fiche ; un procédé sans rapport ne viole pas (iv) à la lettre (CA6v5-01). |
| CA6v4-03 G et passe 2 | 168, 187 | oui | « Retenues par G » dans le texte servi ; ordre complet hors texte ; marquages soumis au contrôle lexical puis à G. Résidu : le contrôle des témoins de garde n'est pas placé avant la passe 2 (CA6v5-02). |
| CA6v4-04 liste lexicale | 196 | oui | Auteur, branche, empreinte seule sur `main`, lecteurs, deux points d'application, conséquence (échec de G par (v)). Résidus : nom de branche incohérent avec la table, exécutant du programme non dit (CA6v5-07) ; aucun artefact qui éprouve le contrôle (CA6v5-03). |
| CA6v4-05 quantificateur en T | 91, 115 | oui | T_0 annoncé ; « pour tout T ≥ T_0 » dans « indiscernable » et (c1) ; n fixé ou fonction de T. Résidu : le liminf de « diffus » n'est pas uniforme, alors que le minorant de (e) l'est (CA6v5-04). |
| CA6v4-06 C diffuse | 116 | oui | — |
| CA6v4-07 tautologie | 116 | oui | « X, ou H_Π ; jamais S elle-même ». K2 ne le rappelle pas (CA6v5-08). |
| CA6v4-08 minorant | 118 | oui | c ajouté. Voir CA6v5-04 pour l'uniformité. |
| CA6v4-09 Π et T | 85 | oui | — |
| CA6v4-10 règle de K6 | 162, 194 | oui | Règle à trois issues, sans ambiguïté ; « seulement nécessaire » vérifié par K6 ; compté indéterminé hors texte. Résidu : v_1 et v_2 non dites distinctes (CA6v5-08). |
| CA6v4-11 témoin mal classé | 164, 171-174 | oui | (iii) retiré du critère de mort ; génération non lue ; une renotation. Résidus : issue d'une seconde renotation fautive non dite ; asymétrie avec G, qui n'a pas de seconde application (CA6v5-05). |
| CA6v4-12 classement | 181 | oui | Inclusion, équivalence ou cas particulier ; classement scellé. Résidu : la liste des classes n'est pas dite « définie », contrairement à celle des hypothèses (CA6v5-06). |
| CA6v4-13 population des comptes | 192-194 | partiellement | Marginales, liste par liste, sur les notables ; comptes de (g) retenus aux petits effectifs. Mais « une seule case non vide » ne dit pas de quelle liste ; c'est la liste des hypothèses porteuses qui croise de fait les comptes de (g) (CA6v5-06). |
| CA6v4-14 notation | 87-92, 98, 116, 129, 184 | oui | Q_T partout, hors texte compris ; λ ; « constante du régime ». L'incise « (P_0 […] n'est pas un terme de cette suite) » est devenue inutile (coupe, CA6v5-09). |
| CA6v4-15 longueur | 73, 80, 98 | oui | Les trois coupes faites. Le texte croît de 393 caractères (10 209 → 10 602) au lieu de rester stable : les ajouts (T_0, Π en T, règle de K6, renotation) l'emportent. Nouvelles coupes en CA6v5-09. |

## Réponses aux critères

1. **Constats de la v4** : 13 oui, 2 partiellement (CA6v4-02, CA6v4-13), 0 non.
2. **Sûreté** :
   - La garde (l. 73) et G (l. 75-80) coïncident ; aucune phrase servie n'évoque plus un système qui modifie son comportement ; le texte servi reste entièrement en théorie de la détection (lois, rapports de vraisemblance, e-valeurs, puissance), tourné vers le défenseur par (e) et (g). Je ne trouve aucune phrase de nature à déclencher un filtre de sûreté ; « procédé par lequel un système le produirait » (l. 79) est une exclusion, énoncée en termes généraux.
   - Conditions (i) à (v) : binaires, applicables par un lecteur figé ; (iv) et (v) demandent du jugement, d'où l'importance de leurs témoins.
   - Témoins de garde : le principe est juste ; le témoin (iv) est mal ciblé (CA6v5-01) ; aucun cas sain n'éprouve G, et aucun artefact n'éprouve le contrôle lexical (CA6v5-03).
   - Ordre G / passe 2 : correct pour les fiches et les marquages ; mais si G est fautif (un témoin de garde non écarté), rien n'empêche que la passe 2 ait déjà servi à l'autre fournisseur des fiches retenues par un G fautif (CA6v5-02).
   - Contrôle lexical : bien défini ; voir CA6v5-03 et CA6v5-07.
3. **Justesse mathématique** :
   - Q_T, ε_T : cohérents. En variation totale, la condition par pas donne d(Q_T, P_0^(T)) ≤ T ε_T, compatible avec une distance jointe au moins c ; en Hellinger, le régime d'exemple T ε_T² → constante est le régime critique ; en Kullback-Leibler (divergence d'ordre quadratique), le régime critique est T ε_T → constante, et l'exemple unique du texte y place le déplacement dans le régime trivialement détectable (CA6v5-04, mineur).
   - liminf, T_0 : le liminf est propre à chaque suite, donc non uniforme sur une classe ; avec « pour tout T ≥ T_0 » (T_0 unique pour la classe) dans (c1) et dans le minorant « uniforme sur C » de (e), une classe qui contient des suites à convergence tardive rend (c1) et le minorant impossibles à tout T fini. Le proposeur peut restreindre ses classes, mais la définition l'y pousse mal (CA6v5-04, mineur).
   - (c1), (c2) : justes ; la disjonction D ∩ C = ∅ est automatique dès que 1 − β > α + δ, ce qui est sans dommage. « Qui entraîne l'appartenance à C » se lit mieux « qui entraîne, pour un déplacement diffus, l'indiscernabilité » (CA6v5-08).
   - K2 : jugeable ; ne rappelle pas « X ou H_Π » (CA6v5-08). Pour S(X, H_Π(X)), l'application lue est X ↦ (X, H_Π(X)), dont la loi image détermine celle de X : la condition ne peut alors être qu'une borne, jamais une égalité ; à dire en une incise si la place le permet (facultatif).
   - K6 et sa règle : juste et sans ambiguïté, sous v_1 ≠ v_2.
   - Minorant : bon objet (uniforme sur C), bonnes variables (c, ε_T, T, n, d), sous la réserve d'uniformité ci-dessus.
   - Exhaustivité : correcte, Π pouvant dépendre de T. (H(X), « tous les triplets », dépend de la longueur des actions de X ; c'est la lecture évidente.)
   - Notations : Q_T, P_0, P_0^(T), ε_T, T_0, λ, w, s_α cohérents dans tout le texte servi et dans le hors-texte (témoin négatif, l. 184). Restent la proximité c / C / (c) (facultatif, déjà signalé) et l'incise devenue inutile sur P_0 (CA6v5-09).
4. **Jugeabilité** : G binaire, mais éprouvé seulement sur des artefacts, dont un mal ciblé, et jamais sur un cas sain (CA6v5-01, CA6v5-03). K1, K3, K4, K5 : sans réserve. K2 : CA6v5-08. K6 : jugeable ; « si (g) n'est qu'une condition nécessaire » demande au juge de décider si l'hypothèse dépend de la classe de déplacements, ce qui reste un jugement, acceptable. Témoins du juge : bons ; issue d'une seconde renotation fautive à dire (CA6v5-05). Renotation : une seule, mais par qui le « juge corrigé » est-il corrigé et sur quoi (consigne, modèle) : « consigné » suffit. Critère de mort : binaire, sous CA6v5-06 (classement dans la liste des classes).
5. **Interface et fuite** (hors texte) : fermée pour le contenu. Réserves mineures : nom de branche incohérent (« branche de quarantaine » dans la table, l. 42 et 57 ; `donnees/course-2-axe-6-*` aux l. 186, 189, 196) et « la même branche » (l. 186) avant sa première mention ; exécutant du programme lexical non dit ; « une seule case non vide » sans liste ; les témoins de garde ne sont pas dits exclus du « nombre de fiches écartées par G » qui passe à la défense ; le compte des marquages écartés n'a pas de destination dite (CA6v5-05 à CA6v5-07). La ligne 196 dit l'existence du mode tenu à l'écart, pas son nom : sans dommage.
6. **Clarté et longueur** : 10 602 caractères. Coupes sûres d'environ 430 caractères (CA6v5-09), qui couvrent largement les ajouts servis de CA6v5-04 et CA6v5-08 (environ 150 caractères) : le texte servi redescendrait vers 10 300.
7. **Défauts nouveaux** : CA6v5-01 à CA6v5-03 (majeurs), CA6v5-04 à CA6v5-09 (mineurs) ; CA6v5-02 et CA6v5-03 sont nouveaux, les autres sont des résidus des corrections.

## Constats nouveaux

### CA6v5-01 — Le témoin de garde de la condition (iv) ne viole pas (iv) à la lettre
- Gravité : majeur (sûreté, règle R5) ; correction locale, hors texte servi.
- Lignes : 79, 185.
- Défaut : (iv) exige qu'« aucun procédé par lequel un système **le** produirait » ne soit décrit, « le » renvoyant au déplacement de la fiche. Le témoin porte « un procédé de production anodin, **sans rapport avec la question** » : un lecteur figé qui applique (iv) à la lettre le retient (garde déclarée fautive à tort, génération perdue), et un lecteur qui l'écarte le fait pour une raison étrangère à (iv) ; dans les deux cas, (iv) n'est pas éprouvée. C'est le cas que CA6v4-01 voulait couvrir : un déplacement défini correctement par une loi, puis un procédé de production de **ce** déplacement décrit à côté.
- Correction (l. 185) : « l'un par (iv) : le déplacement du témoin est défini correctement par une loi, puis un procédé anodin par lequel un système produirait ce déplacement est décrit (par exemple : tirer chaque action à une température d'échantillonnage légèrement plus haute) ; le témoin ne viole ni (i), ni (iii), ni (v) ». Le rédacteur du témoin vérifie, pour chacun des trois, qu'une seule condition est violée.

### CA6v5-02 — Le contrôle des témoins de garde n'est pas placé avant la passe 2
- Gravité : majeur (sûreté, interface) ; correction locale, hors texte servi.
- Lignes : 185, 187.
- Défaut : la ligne 187 met G avant la passe 2, mais ne dit pas quand on vérifie que les trois témoins de garde ont été écartés. Si un témoin passe G, G est fautif, et les fiches qu'il a retenues ont pu être déjà servies à l'autre fournisseur en passe 2 : c'est l'exposition que CA6v4-03 voulait fermer. « La génération n'est pas lue » arrive trop tard pour l'empêcher.
- Correction (l. 187) : « passe 1 ; contrôle lexical puis G ; **vérification des témoins de garde : si l'un n'est pas écarté, arrêt avant la passe 2, la génération n'est pas lue** ; passe 2 sur les fiches retenues ; … ».

### CA6v5-03 — G et le contrôle lexical sans cas sain, et le contrôle lexical sans artefact (R5)
- Gravité : majeur (règle gelée R5) ; correction locale, hors texte servi.
- Lignes : 183-185, 196.
- Défaut : R5 demande que toute garde soit éprouvée sur un cas sain **et** sur un artefact. (i) Les témoins positif et négatif « satisfont G » (l. 183-184), mais rien ne dit qu'ils passent par le contrôle lexical et G dans le même lot, ni ce qu'il advient si G les écarte : aucun cas sain n'éprouve donc G, et un G trop sévère (qui écarte tout) passerait les trois témoins de garde. (ii) Le contrôle lexical, appliqué par programme avec une liste secrète, n'est éprouvé par aucun artefact : une liste mal chargée ou un programme qui ne trouve rien passerait inaperçu.
- Correction : l. 183-184, « les témoins positif et négatif passent aussi par le contrôle lexical et G, dans le même lot ; si l'un est écarté, la garde est fautive et la génération n'est pas lue » ; l. 196, « avant chaque génération, le programme est éprouvé par le lecteur tenu à l'écart sur une fiche d'essai, non servie, qui contient un terme de la liste (il doit la signaler) et sur le témoin positif (il ne doit rien signaler) ; le résultat est scellé ».

### CA6v5-04 — Uniformité en T : liminf par suite contre T_0 unique ; régime d'exemple faux pour Kullback-Leibler
- Gravité : mineur (justesse) ; une ligne du texte servi.
- Lignes : 87-89, 91, 115, 118.
- Défaut : (i) « liminf_T d(Q_T, P_0^(T)) ≥ c » est propre à chaque suite ; une classe peut contenir des suites dont la distance jointe ne dépasse c qu'à des T arbitrairement grands. Or (c1) demande une puissance au moins 1 − β pour tout T ≥ T_0, T_0 unique, et (e) un minorant uniforme sur C en c : ces énoncés sont impossibles sur une telle classe. Le proposeur peut restreindre ses classes, mais la définition ne l'y invite pas, et la passe 2 pourra marquer faux un minorant pourtant voulu. (ii) L'exemple « T ε_T² → constante » est le régime critique en Hellinger ; en Kullback-Leibler, divergence d'ordre quadratique, la règle de chaîne donne une divergence jointe au plus T ε_T, qui tend vers l'infini dans ce régime ; le régime critique y est T ε_T → constante.
- Correction : l. 89, « pour tout T ≥ T_0, d(Q_T, P_0^(T)) ≥ c, où … ; T_0 est annoncé par la fiche » (et, l. 91, « pour tout T ≥ T_0 » sans répéter « T_0 annoncé par la fiche ») ; l. 87, « (par exemple T ε_T² → constante en Hellinger, T ε_T → constante en Kullback-Leibler) ». Si l'auteur tient au liminf, écrire au moins en (e) « uniforme sur C pour T ≥ T_0 ».

### CA6v5-05 — Témoins et renotation : bouts non dits
- Gravité : mineur (jugeabilité, symétrie R4).
- Lignes : 164, 185, 187, 193.
- Défaut : (i) si la renotation unique classe encore mal un témoin, l'issue n'est pas dite ; (ii) le juge a droit à une renotation, G à aucune (génération non lue directement) : l'asymétrie n'est pas motivée ; (iii) les témoins de garde ne sont pas dits exclus du « nombre de fiches écartées par G » (l. 193), qui compterait alors au moins trois de trop ; (iv) « un marquage qui échoue est écarté et compté » (l. 187) : on ne sait pas si ce compte passe à la défense.
- Correction : l. 164 ou hors texte, « si la renotation est encore fautive, la génération n'est pas lue, définitivement » ; dire si G a, lui aussi, une seule nouvelle application par un lecteur corrigé et consigné ; l. 193, « le nombre de fiches écartées par G, témoins exclus » ; l. 187, « compté et scellé, sans passer à la défense » (ou l'inverse, au choix de l'auteur).

### CA6v5-06 — Interface et listes : « une seule case non vide » ; liste des classes non dite définie
- Gravité : mineur (interface, jugeabilité du critère de mort (ii)).
- Lignes : 66, 174, 180, 194.
- Défaut : (i) « une seule case non vide » (l. 194) ne dit pas de quelle liste. Les comptes de (g) portent sur l'hypothèse porteuse : si toutes les notables tombent dans la même case de la liste des hypothèses, les comptes de (g) se croisent de fait avec cette case, même si la liste des classes a deux cases non vides. (ii) l. 180, les classes classiques ne sont pas dites « définies », alors que le classement par inclusion (l. 181) l'exige (déplacement de moyenne de quoi, dans quel espace). (iii) Table l. 66 : « comptes de (g) retenus » se lit « gardés » ou « retenus en arrière » ; la l. 194 dit « ne passent pas ». (iv) l. 174, « listes closes des classes classiques » désigne mal la liste des hypothèses porteuses.
- Correction : l. 194, « une seule case non vide dans l'une ou l'autre liste » ; l. 180, « classes de déplacements classiques, définies : … » ; l. 66, « comptes de (g) non transmis si … » ; l. 174, « dans les listes closes (hypothèses porteuses et classes classiques), scellées avant le service, hors la case « autre » ».

### CA6v5-07 — Branche et exécutant du contrôle lexical
- Gravité : mineur (interface).
- Lignes : 42, 57, 186, 189, 196.
- Défaut : les tables de traitement (l. 42, 57) parlent de « la branche de quarantaine », le hors-texte de `donnees/course-2-axe-6-*` ; « la même branche » (l. 186) précède la première mention de la branche (l. 189). L'exécutant du programme lexical n'est pas dit : la liste n'étant lisible que par des lecteurs tenus à l'écart, le programme doit être lancé par l'un d'eux.
- Correction : une seule désignation de branche partout (celle que veut l'auteur ; la table l. 57 ne se réécrit pas si le fichier est scellé, il suffit de le dire dans la v6) ; l. 186, « sur la branche `donnees/course-2-axe-6-*` » ; l. 196, « appliquée par programme, lancé par un lecteur tenu à l'écart, … ».

### CA6v5-08 — K2, (c2) et K6 : précisions de forme
- Gravité : mineur (jugeabilité).
- Lignes : 116, 158, 162.
- Défaut : (i) K2 ne reprend pas « par X ou H_Π » : une condition sur la loi de S elle-même, exclue en (c2), passerait K2 à la lettre. (ii) « qui entraîne l'appartenance à C » : C étant diffuse, une loi qui remplit la condition sans être diffuse n'y appartient pas ; K2 dit d'ailleurs « alors S est indiscernable », ce qui est le bon énoncé. (iii) K6 ne dit pas v_1 ≠ v_2 ; avec v_1 = v_2, la règle se contredit.
- Correction : K2, « si [égalité ou borne sur des lois images par X ou par H_Π], alors … » ; (c2), « … qui entraîne, pour un déplacement diffus, l'indiscernabilité » ; K6, « deux valeurs numériques distinctes ».

### CA6v5-09 — Longueur : coupes sûres
- Gravité : mineur (clarté, longueur).
- Lignes : 87, 98, 164, 173.
- Coupes (environ 430 caractères au total) :
  - l. 164, tout ce qui suit « Une fiche est **notable** si K1 à K6 sont vrais. » (312 caractères) : le régime des témoins ne sert pas au proposeur ; il vit déjà en partie hors texte (l. 182-185), où il faut seulement ajouter la renotation et « les témoins ne comptent dans aucun effectif ». La consigne du juge, scellée à part, le reprend. Retirer alors « , témoins exclus » de la l. 173 et ajouter « hors témoins » au hors-texte.
  - l. 87, « (P_0, loi de référence, n'est pas un terme de cette suite) » (environ 60 caractères) : devenu inutile depuis le renommage en Q_T.
  - l. 98, « (ce qui exclut la moyenne uniforme sur plus de k positions) » (environ 60 caractères) : conséquence directe de « entropie au plus log k » ; à garder seulement si l'auteur veut prévenir une lecture fautive.
- Je ne propose pas d'autre coupe : la garde, G, les définitions, les exemples de (b) (support de la liste close), la table des rubriques et l'effet de la passe 2 servent tous au juge, au critère de mort ou à la passe 2.

## Servabilité
Après les corrections locales de CA6v5-01, CA6v5-02 et CA6v5-03 (toutes hors texte servi, une ou deux lignes chacune), la v5 est **servable sans nouvelle contre-lecture complète** ; un contrôle de conformité des lignes modifiées (par `diff`) suffit. Les mineurs CA6v5-04 à CA6v5-09 sont recommandés ; seuls CA6v5-04 et CA6v5-08 touchent le texte servi, en une incise chacun, et les coupes de CA6v5-09 les compensent. Restent avant service, comme le dit la ligne 7 : le scellement des listes closes, de la liste lexicale et des témoins, le devis et le GO.

## Décompte (v5)
- Bloquant : 0.
- Majeur : 3 (CA6v5-01 à CA6v5-03), tous hors texte servi.
- Mineur : 6 (CA6v5-04 à CA6v5-09).
- Constats de la v4 : 13 corrigés, 2 partiellement (CA6v4-02, CA6v4-13), 0 non corrigé.
