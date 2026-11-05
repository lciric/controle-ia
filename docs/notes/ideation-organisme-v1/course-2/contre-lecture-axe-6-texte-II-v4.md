# Contre-lecture R2 — axe 6, texte II (« domaine de validité des statistiques de détection ») — v4

- Date : 29 octobre 2026, 22 h 58 UTC (`date -u` : Thu Oct 29 22:58:28 UTC 2026).
- Contre-lecteur : sous-agent Claude, modèle Opus 5.5 (identifiant `claude-opus-5-5`). **Neuf, tenu à l'écart** : n'a écrit aucune pièce de la course ; n'est ni le contre-lecteur de la v1 et de la v2, ni celui de la v3 ; n'a conçu ni lu aucun moniteur ni aucune statistique de surveillance du programme ; n'a lu ni la v2, ni BA-002, ni aucune branche de données, de quarantaine ou de canal.
- Pièces lues, et rien d'autre (dossier `docs/notes/ideation-organisme-v1/course-2/`) :
  - `axe-6-texte-II-v4.md` (182 lignes), pièce contre-lue ;
  - `contre-lecture-axe-6-texte-II-v3.md` (145 lignes), constats CA6v3-01 à CA6v3-15 ;
  - `axe-6-texte-II-v3.md`, comparé par `diff`.
- Empreintes vérifiées (`sha256sum -c <fichier>.sha256`, lancé depuis ce dossier) : les trois « OK ».
  - v4 : `53a6b863790f545500e68c763537a7918b93851a5f07e521c084c9759bfade59` (conforme à `53a6b863…`).
- Mesure du texte servi (lignes 53 à 159, marqueurs exclus), refaite : 10 209 caractères (`LC_ALL=C.UTF-8 wc -m`), 10 616 octets, 1 836 mots. Conforme à la ligne 9.
- Recherche dans le texte servi des restes et termes exposés (`P_ε`, « sabotage », « riposte », « agent », « surveillance », « invisible », « honnête », « contourner », « évasion », « cacher ») : aucune occurrence. Seul reste de l'ancienne notation : « ε » nu à la ligne 113 (CA6v4-14).

## Verdict
**v4 : servable après corrections.** Aucun constat bloquant. Quatorze des quinze constats de la v3 sont corrigés ; un l'est partiellement (CA6v3-01 : la puce « procédé » de la garde n'est toujours testée par aucune condition de G). Six constats nouveaux majeurs : deux de sûreté sur G (puce « procédé » hors de G ; témoin de garde qui n'éprouve que la condition (i)), un de sûreté sur l'ordre entre G et la passe 2, un d'interface (contrôle lexical sans point d'application ni détenteur), deux de justesse issus de la réindexation par T (quantificateur en T absent de « indiscernable » et de (c1) ; classe C non tenue d'être diffuse, donc trivialement satisfaite). Neuf mineurs. Toutes les corrections tiennent en une ou deux lignes ; les coupes proposées (CA6v4-15) compensent à peu près les ajouts.

## Table des constats de la v3

| Constat | Lignes de la v4 | Corrigé | Commentaire |
|---|---|---|---|
| CA6v3-01 « sabotage », G non testé | 55-57, 64, 180 | partiellement | « Sabotage » retiré ; seconde puce réécrite ; condition (v) ajoutée ; noms des modes dans la liste lexicale. Mais le défaut (ii) de la v3 visait les **deux** exclusions de la garde : la première (« tout procédé par lequel un système produirait un déplacement ») n'est toujours testée par aucune condition de G (CA6v4-01). La liste lexicale n'a ni point d'application aux fiches ni conséquence dite (CA6v4-04). |
| CA6v3-02 ε contre T fixe | 67, 71-73, 76 | oui | Suite (P_T, ε_T) indexée par T, ε_T → 0, régime énoncé, « toute histoire », liminf ≥ c, « T fini pour chaque suite », exhaustivité « pour tout T ». Résidus de la réindexation : CA6v4-05 (quantificateur en T ailleurs), CA6v4-09 (Π fixe), CA6v4-14 (« ε » nu). |
| CA6v3-03 objet de (c) | 98-100, 122-123, 142 | oui | (c1) et (c2) séparées, rubriques séparées, « indiscernable » employé, K2 sous forme « si…, alors… ». Résidus : C n'est pas tenue d'être diffuse (CA6v4-06) ; condition tautologique admise quand l'application lue est S (CA6v4-07). |
| CA6v3-04 (b) contre K6 | 97, 108 | oui | (b) élargie ; (g) en condition nécessaire, dite telle. Résidu : K6 ne vérifie pas que la fiche le dit (CA6v4-10). |
| CA6v3-05 « autre », témoins | 148, 157-158, 166 | oui | « Hors la case autre » ; règle de classement ; témoins exclus de tout compte ; « de la génération ». Résidu : « la contient » non défini (CA6v4-12). |
| CA6v3-06 G sans artefact | 170 | oui | Témoin de garde scellé, qui doit être écarté, sinon génération non lue. Résidu : il n'éprouve que la condition (i), la plus facile (CA6v4-02). |
| CA6v3-07 juge, lecteur figé | 171 | oui | Lecteurs tenus à l'écart ou modèle à consigne scellée ; sorties sur `donnees/course-2-axe-6-*`. |
| CA6v3-08 « ripostes » | 83 | oui | — |
| CA6v3-09 attention | 82 | oui | « Pour toute entrée », k indépendant de la longueur. La seconde phrase est désormais une conséquence de la première (coupe, CA6v4-15). |
| CA6v3-10 notation | 68, 69, 72, 74 | oui | Activations causales, filtration et borne T, « toute histoire », H(X) défini. |
| CA6v3-11 résidus | 93, 102, 106, 115, 135-136, 153 | oui | Les sept points traités ; le minorant de (e) est uniforme sur C, ce qui est le bon objet (la v3 disait D, avant la séparation de (c)). Résidu mathématique : CA6v4-08. |
| CA6v3-12 K6, interface | 146, 178 | oui | Règle à trois issues ; deux comptes totaux, jamais croisés ; calcul au devis. Résidus : « du côté de » ambigu (CA6v4-10) ; population des comptes et croisement de fait aux petits effectifs (CA6v4-13). |
| CA6v3-13 G (ii), (iii) | 61-62 | oui | Repris tels que proposés. |
| CA6v3-14 mesure, exemples | 9, 97 | oui | Mesure refaite et conforme ; « exemples de forme, déjà connus ». |
| CA6v3-15 échantillons | 104 | oui | — |

## Réponses aux critères

1. **Constats de la v3** : 14 oui, 1 partiellement (CA6v3-01), 0 non.
2. **Sûreté** : le texte servi est entièrement en théorie de la détection ; plus aucun terme de registre adverse. La garde et G ne coïncident pas encore : la première puce de la garde n'est testée par aucune des cinq conditions (CA6v4-01) ; c'est aussi la seule phrase du texte servi qui évoque un système modifiant son comportement, et elle disparaît avec la correction proposée. Le témoin de garde éprouve G sur la seule condition (i), purement grammaticale ; la condition (v), ajoutée précisément pour la sûreté et la plus sujette au jugement, n'est éprouvée sur aucun artefact (CA6v4-02). L'ordre entre G et la passe 2 n'est pas dit : une fiche écartée par G pourrait être servie à l'autre fournisseur (CA6v4-03). La structure de (c2) (classe sur laquelle une statistique perd sa puissance) reste au niveau des lois, tournée vers le défenseur par (e) et (g) ; je ne la juge pas exposée.
3. **Justesse mathématique** :
   - Diffus : correct. En variation totale, la première condition donne d(P_T, P_0^(T)) ≤ T ε_T, ce qui est compatible avec liminf ≥ c dès que T ε_T ≥ c à partir d'un rang ; en Kullback-Leibler, la règle de chaîne donne la même compatibilité ; en Hellinger, le régime d'exemple T ε_T² → constante est le régime naturel. « Toute histoire » suppose les lois données par leurs noyaux conditionnels, ce qui est la lecture évidente.
   - (c1), (c2) : la séparation est juste, mais C n'est pas tenue d'être une classe de déplacements diffus, ce qui rend (c2) trivialement satisfiable (CA6v4-06) ; « indiscernable » et (c1) n'ont pas de quantificateur en T (CA6v4-05) ; « qui entraîne l'appartenance à C » est cohérent avec K2 une fois C diffuse, mais admet la condition tautologique « même loi de S » (CA6v4-07).
   - K2 : jugeable, sous CA6v4-07. K6 et sa règle : la règle existe, « du côté de » est ambigu ; K6 ne vérifie pas la mention « condition seulement nécessaire » (CA6v4-10).
   - Minorant uniforme : uniforme sur C, bon objet ; mais un minorant de puissance ne peut pas s'écrire en ε_T, qui majore l'écart par pas : il faut c (CA6v4-08).
   - Exhaustivité pour tout T : correcte, mais Π, ensemble fini fixé, ne peut pas suivre T → ∞ (CA6v4-09).
   - Notations : P_T, P_0^(T), ε_T cohérents partout, hors texte compris (témoin négatif, l. 169) ; aucun `P_ε`. Restes : « ε » nu (l. 113), collision de lecture P_0 / P_T, w employé deux fois (CA6v4-14).
4. **Jugeabilité** : G est binaire, mais incomplet (CA6v4-01) et peu éprouvé (CA6v4-02). K1, K3, K5 : sans réserve. K2 : CA6v4-07. K4 : « tourne sur processeur » ne peut être que déclaré, ce qui suffit. K6 : CA6v4-10. Témoins : bon contrôle du juge, mais leur échec mène tantôt à « l'axe n'a rien donné », tantôt à « génération non lue » (CA6v4-11). Critère de mort : binaire sous CA6v4-12.
5. **Interface et fuite** (hors texte) : fermée pour le contenu, sous trois réserves : la liste lexicale, qui contient les noms des modes, n'a ni détenteur ni branche ni point d'application (CA6v4-04) ; les marquages de passe 2 ne passent pas par G (CA6v4-03) ; population des comptes et croisement de fait aux petits effectifs (CA6v4-13).
6. **Clarté et longueur** : 10 209 caractères, soit 2 004 de plus que la v3 (+24 %). Les ajouts sont presque tous nécessaires ; trois redondances peuvent partir sans perte (CA6v4-15), ce qui libère environ 380 caractères, à peu près ce que coûtent les corrections ci-dessous.
7. **Défauts nouveaux** : CA6v4-03, CA6v4-04, CA6v4-05, CA6v4-06, CA6v4-11, CA6v4-13 sont nouveaux ou rendus visibles par la v4 ; les autres sont des résidus des corrections.

## Constats nouveaux

### CA6v4-01 — La première exclusion de la garde (« procédé ») n'est testée par aucune condition de G
- Gravité : majeur (sûreté, jugeabilité).
- Lignes : 55-57, 59-64.
- Défaut : G est la seule voie d'exclusion (l. 59). La garde exclut « tout procédé par lequel un système produirait un déplacement dans son comportement » (l. 56). Aucune des conditions (i) à (v) ne le teste : (iv) exige qu'un déplacement soit **défini** par une loi, pas qu'aucun procédé de production ne soit décrit à côté ; (iii) ne vise que tâches, outils, environnements ; (v) vise une intention ou un comportement « nommé », ce qui ne couvre pas un mécanisme. Une fiche qui définit son déplacement par une loi puis décrit comment un générateur le réaliserait satisfait G. C'est le défaut (ii) de CA6v3-01, corrigé pour la seconde puce seulement. Par ailleurs, la phrase de la ligne 56 est la seule du texte servi qui évoque un système modifiant son comportement.
- Correction : fondre l'exclusion dans (iv) : « (iv) chaque déplacement y est défini et construit seulement par une loi, un rapport de vraisemblance, un noyau de transition ou une opération sur échantillons ; aucun procédé par lequel un système le produirait n'y est décrit ; ». Réduire alors la garde à : « **Garde.** Niveau des lois de probabilité : les seules constructions admises sont des opérations sur des lois ou sur des échantillons, et rien n'est prêté au processus générateur au-delà de sa loi. » (les deux puces disparaissent ; voir CA6v4-15).

### CA6v4-02 — Le témoin de garde n'éprouve que la condition (i)
- Gravité : majeur (sûreté, règle R5).
- Lignes : 59-64, 170.
- Défaut : G est une conjonction de cinq conditions. Le seul artefact échoue par un impératif (condition (i)), qu'un lecteur figé repère par la grammaire. La condition (v), ajoutée pour la sûreté et la plus sujette au jugement, et la condition (iv) (avec CA6v4-01) ne sont éprouvées par aucun artefact : un lecteur figé qui n'appliquerait que (i) passerait le contrôle. De plus, le texte ne dit pas que le témoin est présenté dans le même lot, anonyme, avec la même consigne que les fiches ; présenté à part, il ne teste pas le lecteur dans ses conditions réelles.
- Correction : hors texte, « Témoins de garde (R5) : au moins deux, inoffensifs, complets et justes sauf une seule condition de G violée nettement : l'un par (i) (impératif anodin), l'autre par (v) (une phrase qui prête au processus générateur une préférence anodine et nommée, par exemple « le processus préfère les phrases courtes ») ; si CA6v4-01 est retenu, un troisième par (iv) (un procédé de production anodin). Ils sont glissés anonymement dans le même lot que les fiches, sous la même consigne. Si l'un n'est pas écarté, la garde est fautive et la génération n'est pas lue. »

### CA6v4-03 — Ordre entre G et la passe 2 non dit ; les marquages de passe 2 échappent à G
- Gravité : majeur (sûreté, interface).
- Lignes : 59, 150-153.
- Défaut : G s'applique « avant le juge » (l. 59), et le juge intervient après la passe 2 (il valide les preuves, l. 153). Rien n'empêche donc que la passe 2 précède G : une fiche qui échoue à G serait servie à l'autre fournisseur, ce qui est exactement l'exposition que la garde doit éviter (le texte voisin a été arrêté par un filtre). Les marquages et antériorités écrits en passe 2 sont eux-mêmes du texte de proposeur et ne passent par aucun contrôle.
- Correction : texte servi, « Passe 2 : vous relisez les fiches anonymes d'un autre modèle proposeur, retenues par G. » Hors texte : « G s'applique entre la passe 1 et la passe 2 ; les marquages et antériorités de passe 2 passent par G et par le contrôle lexical avant le juge ; un marquage qui échoue est écarté et compté. »

### CA6v4-04 — Contrôle lexical : point d'application, conséquence et détenteur non dits
- Gravité : majeur (interface, fuite ; résidu de CA6v3-01).
- Lignes : 175, 180.
- Défaut : (i) La v3 proposait la liste lexicale « pour attraper ce que (v) laisserait passer », donc appliquée aux fiches ; la v4 ne l'applique qu'à ce qui passe vers la défense (l. 175), c'est-à-dire à des effectifs et à des noms de cases déjà scellés, où elle n'attrape rien. Ce qu'il advient d'une fiche qui contient un terme de la liste n'est pas dit. (ii) La liste « comprend les noms des modes de sabotage du programme » : son auteur, sa branche et ses lecteurs ne sont pas dits. Scellée sur `main` comme les listes closes (l. 163), elle apprendrait ces noms à toute session du côté de la défense, y compris, s'il y figure, celui du mode tenu à l'écart de la conception des moniteurs (N-054).
- Correction : hors texte, « La liste lexicale est écrite et scellée par un lecteur tenu à l'écart, sur la branche `donnees/course-2-axe-6-*` ; seule son empreinte est sur `main`. Elle est appliquée par programme (1) aux fiches et aux marquages de passe 2, avant G : un terme trouvé fait échouer G par la condition (v), cas limites tranchés par un lecteur tenu à l'écart ; (2) à tout ce qui sort vers la défense. » Faire dire par l'auteur si le nom du mode tenu à l'écart y figure, et qui a le droit de le lire.

### CA6v4-05 — « Indiscernable » et (c1) sans quantificateur en T
- Gravité : majeur (justesse ; résidu de la réindexation de CA6v3-02).
- Lignes : 75, 99-100, 142.
- Défaut : un déplacement est désormais une suite (P_T) indexée par T, et la statistique, son seuil et peut-être n dépendent de T. « La probabilité de rejet sous P_T […] est au plus α + δ » (l. 75) et « S garde une puissance au moins 1 − β » (l. 99) ne disent pas pour quels T : tout T, à partir d'un rang, en limite supérieure ou inférieure. Selon la lecture, D et C changent, la disjonction D ∩ C = ∅ n'est plus vérifiable, et K2 compare des énoncés de portées différentes. Le lien entre n et T n'est pas dit non plus, alors que (e) donne un minorant « en T, n ».
- Correction : l. 75, « **Indiscernable au niveau α** : pour tout T ≥ T_0, T_0 annoncé par la fiche, la probabilité de rejet sous P_T, en espérance sur l'échantillon d'étalonnage de taille n (fixé, ou fonction de T énoncée), est au plus α + δ » ; (c1), « … garde, pour tout T ≥ T_0, une puissance au moins 1 − β ».

### CA6v4-06 — La classe C n'est pas tenue d'être diffuse : (c2) devient trivial
- Gravité : majeur (justesse, jugeabilité).
- Lignes : 99-100, 142.
- Défaut : (c1) parle de « déplacements diffus », (c2) seulement d'« une classe C ». Sans la seconde condition de « diffus » (liminf d(P_T, P_0^(T)) ≥ c), C peut contenir P_0 lui-même ou des déplacements dont la distance jointe tend vers 0 : toute statistique y est indiscernable, la condition « d(P_T, P_0^(T)) → 0 » passe K2, et la fiche devient notable sans rien dire. Or l'intérêt de (c2) est précisément une perte de puissance sur des déplacements **détectables en principe** (distance jointe au moins c).
- Correction : « (c2) une classe C de déplacements diffus, disjointe de D, sur laquelle S est indiscernable au niveau α, avec δ fixé. »

### CA6v4-07 — Condition de (c2) tautologique quand l'application lue est S elle-même
- Gravité : mineur.
- Lignes : 100, 142.
- Défaut : « par l'application lue par S (H_Π, ou S elle-même) » admet la condition « la loi de S sous P_T égale sa loi sous P_0^(T) », qui entraîne trivialement l'indiscernabilité et passe K2 sans rien délimiter.
- Correction : « par l'application lue par S (X, ou H_Π ; jamais S elle-même) ».

### CA6v4-08 — Le minorant de puissance de (e) ne peut pas s'écrire en ε_T seul
- Gravité : mineur (justesse).
- Lignes : 71-73, 102.
- Défaut : ε_T **majore** l'écart par pas ; la seule minoration de l'écart que donne la définition est liminf d(P_T, P_0^(T)) ≥ c. Un minorant de puissance uniforme sur C doit donc faire intervenir c ; « en ε_T, T, n et la distance d » oriente vers un énoncé impossible ou mal posé.
- Correction : « avec un minorant de puissance uniforme sur la classe C, en c, ε_T, T, n et la distance d choisie ».

### CA6v4-09 — Π, ensemble fini fixé, contre T → ∞
- Gravité : mineur (justesse).
- Lignes : 69, 76, 82-83.
- Défaut : Π est « un ensemble fini de triplets (t, ℓ, p) ». Fixé, il ne lit qu'un nombre borné d'actions quand T → ∞, ce qui contredit l'accumulation à travers les actions (l. 83) et rend « exhaustive pour tout T » (l. 76) presque toujours fausse. H, lui, dépend de T.
- Correction : l. 69, ajouter « Π peut dépendre de T (par exemple des couches et des positions fixées, à chaque action t ≤ T). »

### CA6v4-10 — K6 : « du côté de » ambigu ; la mention « seulement nécessaire » n'est pas vérifiée
- Gravité : mineur (jugeabilité).
- Lignes : 108, 146, 178.
- Défaut : (i) « confirmée si l'intervalle est du côté de la première valeur » admet deux lectures (intervalle au-delà de la première valeur, ou plus près d'elle que de la seconde) ; deux lecteurs figés peuvent classer différemment, et le compte transmis en dépend. (ii) K6 ne vérifie pas que la fiche dit « seulement nécessaire » quand l'hypothèse dépend de la classe de déplacements (l. 108) : une condition nécessaire présentée comme suffisante passe. (iii) Pour une condition seulement nécessaire, « confirmée » ne confirme pas l'hypothèse ; le compte « confirmées » (l. 178) mêle les deux sortes.
- Correction : K6, « … et une règle : avec v_1 la valeur qui confirme et v_2 celle qui infirme, confirmée si l'intervalle est entièrement du côté de v_1 opposé à v_2, v_1 comprise ; infirmée s'il est entièrement du côté de v_2 opposé à v_1, v_2 comprise ; indéterminée sinon ; si (g) n'est qu'une condition nécessaire, la fiche le dit. » Hors texte : « pour une condition seulement nécessaire, seul “infirmée” est compté ; “confirmée” est compté comme indéterminée ».

### CA6v4-11 — Témoin mal classé : mort de l'axe ici, génération non lue là
- Gravité : mineur (jugeabilité, symétrie R4).
- Lignes : 148, 159, 170.
- Défaut : un témoin mal classé par le juge rend « la notation fautive » (l. 148) et, en même temps, déclare que « l'axe n'a rien donné » (l. 159, (iii)). C'est une panne d'instrument comptée comme un résultat négatif de l'axe ; pour la panne symétrique de G, le hors-texte prévoit au contraire « la génération n'est pas lue » (l. 170).
- Correction : retirer (iii) du critère de mort ; l. 148, « Si l'un d'eux est mal classé, la notation est fautive : la génération n'est pas lue, et une seule notation refaite, par un juge corrigé et consigné, est permise. » Si Lazar préfère la mort de l'axe (pour interdire toute renotation), l'appliquer aussi au témoin de garde.

### CA6v4-12 — Classement dans les listes closes : « la contient » non défini
- Gravité : mineur (jugeabilité du critère de mort (ii)).
- Lignes : 158, 166.
- Défaut : « Une fiche est classée dans la première case de la liste qui la contient » : pour une classe C, « contenue » peut se lire inclusion de C dans la famille de la case, ou intersection non vide. Une classe C nouvelle qui contient des déplacements de moyenne tombe dans « déplacement de moyenne » sous la seconde lecture et dans « autre » sous la première ; le critère de mort (ii) bascule.
- Correction : hors texte, « une classe C est dans une case si elle est incluse dans la famille de la case ; une hypothèse porteuse, si elle lui est équivalente ou en est un cas particulier ; le lecteur tenu à l'écart tranche, et son classement est scellé ».

### CA6v4-13 — Interface : population des comptes et croisement de fait aux petits effectifs
- Gravité : mineur (interface).
- Lignes : 175-178.
- Défaut : (i) Les effectifs par case et les deux comptes de (g) portent-ils sur toutes les fiches, sur celles retenues par G, ou sur les notables ? Non dit. (ii) « Effectifs par case des listes closes » : marginales par liste, ou table croisée hypothèse × classe ? Non dit ; croisée, elle dirait quelles paires reviennent. (iii) Avec quatre fiches au plus par génération, si une seule fiche est notable ou une seule case non vide, les deux totaux de (g) se croisent de fait avec la case, ce que la ligne 178 veut éviter.
- Correction : « effectifs marginaux, liste par liste, sur les fiches notables ; deux comptes de (g), sur les fiches notables ; s'il y a moins de deux fiches notables ou une seule case non vide, les comptes de (g) ne passent pas ».

### CA6v4-14 — Restes de notation
- Gravité : mineur (clarté).
- Lignes : 69-76, 77, 82, 113.
- Défaut : (i) « quand ε croît » (l. 113) : ε n'est plus défini, et ε_T → 0 par définition. (ii) P_T est indexé par la longueur, P_0 désigne la référence : P_0 se lit aussi comme « P_T pour T = 0 ». (iii) w désigne les poids d'attention (l. 82) et le vecteur d'un trait linéaire (l. 77). (iv) c (constante), C (classe), (c), (c1), (c2) (champs) se côtoient dans les mêmes phrases.
- Correction : (i) « quand la constante du régime (par exemple T ε_T²) croît » ; (ii) au moins une incise, l. 71 : « (P_0, loi de référence, n'est pas un terme de cette suite) », ou renommer la suite Q_T ; (iii) poids d'attention λ ; (iv) facultatif : constante γ au lieu de c.

### CA6v4-15 — Longueur : coupes sûres
- Gravité : mineur (clarté, longueur).
- Lignes : 55-57, 64, 82.
- Défaut : trois redondances, environ 380 caractères : (i) les deux puces de la garde (l. 56-57, environ 245 caractères avec « Sont exclus : ») répètent G, qui seul s'applique, une fois CA6v4-01 retenu ; (ii) la seconde moitié de (v) (« ; chaque déplacement n'y est désigné que par sa loi ou son paramètre », 69 caractères) répète (iv) ; (iii) « La moyenne uniforme sur un ensemble de plus de k positions est exclue. » (71 caractères) découle de « entropie au plus log k » (la moyenne uniforme sur m positions a une entropie log m).
- Correction : (i) garde en une phrase (texte en CA6v4-01) ; (ii) « (v) elle ne prête au processus générateur ni intention, ni motif, ni comportement nommé. » ; (iii) remplacer la phrase par l'incise « (ce qui exclut la moyenne uniforme sur plus de k positions) », ou la retirer. Les corrections CA6v4-01, -03, -05, -06, -08, -09, -10 et -14 ajoutent à peu près autant ; le texte servi devrait rester autour de 10 200 caractères. Je ne propose pas d'autre coupe : la table des rubriques, les définitions et les exemples de (b) servent tous au juge ou à la liste close.

## Décompte (v4)
- Bloquant : 0.
- Majeur : 6 (CA6v4-01 à CA6v4-06).
- Mineur : 9 (CA6v4-07 à CA6v4-15).
- Constats de la v3 : 14 corrigés, 1 partiellement (CA6v3-01), 0 non corrigé.
