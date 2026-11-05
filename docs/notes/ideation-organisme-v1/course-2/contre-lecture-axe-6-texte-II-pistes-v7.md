# Contre-lecture R2 — axe 6, texte II, bras « avec pistes » — v7

- Date : 30 octobre 2026, 7 h 48 UTC (`date -u` : Fri Oct 30 07:48:38 UTC 2026).
- Contre-lecteur : sous-agent Claude, modèle Opus 5.5 (identifiant `claude-opus-5-5`), lancé par session-depot. **Neuf** : n'a écrit aucune pièce de la course, n'a lu aucune version antérieure de ce texte, n'a conçu ni lu aucun moniteur.
- Pièces lues :
  1. `axe-6-texte-II-pistes-v7.md`, lu par `git show` sur `origin/donnees/course-2-axe-6-v1` ; empreinte recalculée `908abd79147091f34eafbaee55634a44ee5d9a06e8883663c6c2acc853774c15`, égale au compagnon `.sha256` ; 165 lignes.
  2. `docs/notes/ideation-organisme-v1/course-2/axe-6-texte-II-v6.md`, empreinte `1b301c15…`, égale à celle que cite la v7 (ligne 4).
  3. `docs/notes/ideation-organisme-v1/course-2/contre-lecture-axe-6-texte-II-v1.md` (`14e51a3a…`, égale à celle que cite la v7), lignes 128 à 200. **Écart déclaré** : les lignes 1 à 5 de ce fichier (en-tête : date, contre-lecteur, pièces lues) ont aussi été affichées par inadvertance ; elles ne contiennent aucun contenu de la v2 ni des pistes.
- Aucune autre branche, aucun autre fichier. Le fichier des listes closes cité par la v7 (ligne 163, `08e391c9…`) et les registres cités (R-565, R-790, R-793) n'ont pas été ouverts : leur existence et leurs empreintes ne sont pas vérifiées ici.
- Ce rapport va sur `main` : il ne recopie aucune piste. Il ne cite que des numéros de ligne de la v7 et des catégories de défaut.
- Déclaration : ayant lu les pistes, ce contre-lecteur ne peut pas être le lecteur tenu à l'écart des sorties de ce bras, ni rédiger ses témoins.

## Verdict
**Servable après corrections locales** : aucun bloquant de sûreté ; trois défauts majeurs (protocole des deux bras non écrit, une piste dont la forme naturelle de condition est exclue par K2, une piste ambiguë dans sa notation), tous corrigeables sans refonte.

## Contrôles mécaniques
- Texte servi (entre les marqueurs, lignes 25 à 139) : 11 042 caractères (`LC_ALL=C.UTF-8 wc -m`, et décompte Python identique) ; la v6 en fait 10 356. Les deux mesures de l'en-tête (ligne 22) sont exactes. Hausse : +686 caractères, +6,6 %.
- `diff` du texte servi v6 contre v7 : seule différence, l'ajout des lignes 85 à 94 de la v7 (un intitulé et neuf pistes) suivies d'une ligne vide. Aucune autre ligne servie n'a changé (critère 6 rempli).
- `diff` du hors-texte : seule différence, l'ajout de la ligne 163 (interface).

## Table des constats CA6-V2

| Constat | Lignes de la v7 | Corrigé | Commentaire |
|---|---|---|---|
| CA6-V2-01 ancrage | 4, 20, 21, 85, 136 à 139, 158 à 160 | **partiellement** | L'option « deux bras séparés » est retenue (ligne 4) et les pistes sont placées après les facultatifs, sous un intitulé qui les dit sans effet sur la notation (ligne 85). Mais la correction demandait aussi de **compter séparément** les fiches notables des deux bras pour faire de l'ancrage une mesure : rien n'est écrit sur l'attribution des bras aux proposeurs, le comptage par bras, l'application du critère de mort par bras ou en commun, ni la mesure de l'ancrage. Voir CA6P7-01. |
| CA6-V2-02 notabilité | 85, 121 à 129 | **oui** | Plus aucune clause de notabilité liée aux pistes ; « notable » reste K1 à K6, binaire (ligne 129) ; aucun critère K ne mentionne les pistes. |
| CA6-V2-03 sous-type concentré | 91 | **oui** | Aucune piste ne décrit plus de déplacement concentré ; les sous-types restants de la ligne 91 sont compatibles avec la définition de « diffus » (ligne 41). |
| CA6-V2-04 architecture du moniteur | 92, 94 ; voir aussi 86 et 88 | **oui pour la ligne visée**, défaut de même catégorie ailleurs | La ligne 92 est réécrite comme propriété des lois images, sans composant nommé, conformément à la correction. La ligne 94 est neutre (ni construction d'un déplacement, ni procédé). En revanche, la ligne 88 définit encore sa classe par rapport à la statistique elle-même (CA6P7-02), et la ligne 86 nomme une forme d'agrégation (CA6P7-03). |
| CA6-V2-05 quantificateur | 87 | **partiellement** | Le quantificateur est restreint, mais la sous-classe nommée n'est pas définie dans la notation, et l'affirmation n'est exacte qu'asymptotiquement dans le régime diffus : à T fixé, la loi d'une statistique de la sous-classe peut encore changer sous la classe nommée, donc sa probabilité de rejet aussi. Correction : définir la sous-classe par la loi de la statistique (ou par sa loi limite) et ajouter « dans le régime diffus », ou dire que l'indiscernabilité vaut avec δ → 0 quand T → ∞. Gravité résiduelle : mineure. |
| CA6-V2-06 références | 88, 90 ; en-tête 15 | **partiellement** | Ligne 88 : Hunt-Stein limité à l'optimalité minimax, exact. Ligne 90 : l'antériorité la plus ancienne est ajoutée ; il reste à vérifier sur le document original que les deux références couvrent tout ce que la ligne leur attribue (à ma connaissance, la couverture n'est pas complète pour l'un des cas nommés). L'élément non vérifié de la v2 est retiré. Mais aucune trace de vérification sur PDF empreinté (R7) n'est consignée, et les références servies sont des noms seuls, sans titre ni année, alors que le texte servi exige ce format des proposeurs (lignes 57, 59). Correction : consigner la vérification (chemin, empreinte, page) au hors-texte, ou retirer les noms. |
| CA6-V2-07 intitulés | 145, 146, 163 | **oui** (sous réserve) | La taxinomie de l'interface est celle des listes closes de `main`, et les pistes ne créent aucune case (ligne 163). Réserve : le fichier des listes closes n'a pas été ouvert ici ; son indépendance vis-à-vis de la v2 repose sur la ligne 146. |
| CA6-V2-08 provenance | 4, 5 | **oui** (sous réserve) | Décision et provenance citées par numéros de registre (R-565, R-790, R-793) ; registres non ouverts ici. |
| CA6-V2-09 longueur | 22 | **oui** | Mesure consignée et exacte (voir plus haut) ; le matériau non vérifié de la v2 est retiré. |

## Critères transverses
- **Sûreté (critère 2)** : aucune piste ne décrit un procédé ; aucune ne prête d'intention au processus générateur ; vocabulaire purement statistique, peu exposé à un filtre. Les deux lignes les plus proches de l'architecture du moniteur sont 86 et 88 (CA6P7-02, CA6P7-03). La juxtaposition des lignes 86 et 87 se lit comme « une forme de statistique, puis la classe qui lui échappe » ; c'est la question même de l'axe, au niveau des lois, et le hors-texte assume que la classe servie est celle du programme (ligne 164). Pas bloquant.
- **Ancrage (critère 4)** : le caractère facultatif est dit (ligne 85) ; la notabilité est binaire et indépendante des pistes (lignes 121 à 129). Reste l'effet au niveau de l'axe : trois pistes (lignes 86, 87, 90) sont voisines des classes classiques de la liste close (ligne 145), si bien qu'un proposeur qui les suit rapproche ce bras du critère de mort (ii) (ligne 139). Cela rend indispensable une lecture par bras (CA6P7-01).
- **Fuite (critère 5)** : pas de fuite par l'interface (ligne 163) ; pistes seulement sur la branche de données ; lecteur des sorties distinct des contre-lecteurs (lignes 21, 156). Deux points de cohérence du hors-texte (CA6P7-05) et un contrôle lexical à éprouver sur les pistes (CA6P7-04).

## Constats nouveaux

### CA6P7-01 — Protocole des deux bras non écrit
- Gravité : majeur.
- Lignes : 4, 20, 21, 136 à 139, 158 à 160, 163.
- Défaut : la v7 dit que les deux bras sont séparés, sans dire (1) quel proposeur reçoit quel bras, ni combien de fiches par bras ; (2) si les deux bras forment une même génération ou deux générations numérotées à part ; (3) si le critère de mort de l'axe (lignes 136 à 139) s'applique par bras ou aux deux bras réunis ; (4) comment l'ancrage est mesuré (par exemple, part des fiches notables de chaque bras dont la classe C tombe dans une case non « autre ») ; (5) si un compte par bras passe à la défense, ce que la ligne 160 (comptes « totaux sur la génération, jamais croisés ») ne prévoit pas. Sans ces règles, la correction de CA6-V2-01 reste un biais et non une mesure.
- Correction proposée : au hors-texte, écrire l'attribution des bras, le comptage séparé des fiches notables, la règle de mort par bras (recommandation : lire les deux bras séparément, et le bras sans pistes seul pour le critère de mort), et la mesure d'ancrage, calculée par le lecteur tenu à l'écart et scellée sur la branche des sorties ; faire du passage d'un compte par bras vers la défense un nœud pour Lazar.

### CA6P7-02 — Une piste appelle une condition que K2 exclut
- Gravité : majeur.
- Lignes : 88, contre 70 et 123.
- Défaut : la ligne 88 définit sa classe par une propriété de la statistique S elle-même. La condition de perte de puissance qui en découle naturellement porte sur S, ce que la ligne 70 (« jamais S elle-même ») et K2 (ligne 123) excluent : une fiche qui suit cette piste risque d'être non notable, ou bien elle oblige le juge à trancher un cas limite. C'est aussi la catégorie de défaut de CA6-V2-04 (classe définie par rapport à la statistique, non par une propriété des lois). - Correction proposée : réécrire la piste comme propriété du problème de test (loi de référence et classe d'alternatives), ou des lois images par l'application lue, sans propriété de S ; sinon la retirer.

### CA6P7-03 — Notation non définie et lecture double
- Gravité : majeur.
- Lignes : 86, contre 38, 39 et 52.
- Défaut : (1) la ligne 86 emploie un objet indexé par la seule action, que la notation (lignes 38 et 39) ne définit pas ; (2) la ligne ne dit pas si elle nomme une classe de statistiques ou une classe de déplacements, alors que les autres lignes du matériau nomment des déplacements ; (3) lue comme une agrégation dans une action, elle contredit la contrainte de la ligne 52 et pousse vers une classe exclue ; lue comme une agrégation à travers les actions, elle est permise (ligne 53), mais c'est alors la ligne qui nomme le plus directement une forme d'agrégation de statistique.
- Correction proposée : soit la retirer, soit dire « à travers les actions » et remplacer l'objet non défini par H_Π ou par un trait au sens de la ligne 47, en précisant qu'il s'agit d'une classe de statistiques.

### CA6P7-04 — Contrôle lexical non éprouvé sur les pistes
- Gravité : mineur.
- Lignes : 85 à 94, contre 162.
- Défaut : si un terme de la liste lexicale scellée apparaît dans une piste, les fiches qui la suivent échouent à G par la condition (v) dans ce bras seulement : l'exclusion devient différentielle entre bras, et la piste elle-même serait exposée. Le contre-lecteur ne peut pas le vérifier (il ne lit pas la liste).
- Correction proposée : avant le service, un lecteur tenu à l'écart applique le programme du contrôle lexical aux lignes 85 à 94 ; seul le résultat (signalé ou non) est scellé ; un signalement renvoie la piste en réécriture.

### CA6P7-05 — Hors-texte non mis à jour pour ce bras
- Gravité : mineur.
- Lignes : 147, 152, 145 contre 163.
- Défaut : ligne 147, le rédacteur des témoins « n'a lu ni BA-002 ni la v2 » : pour ce bras, il faut aussi « ni la v7 » (la ligne 20 dit que les témoins de la v6 valent, ce qui est cohérent, mais la condition doit le dire). Ligne 152, la branche `donnees/course-2-axe-6-v1` est dite porter « la v2 » : elle porte aussi la v7. Ligne 145, les classes classiques sont « définies au scellement », alors que la ligne 163 cite un fichier déjà scellé (incohérence héritée de la v6).
- Correction proposée : mettre ces trois lignes à jour.

### CA6P7-06 — Objet de la dernière piste
- Gravité : mineur.
- Lignes : 94, 85.
- Défaut : la ligne 94 ne dit pas sur quoi portent les combinaisons (classes de déplacements, ou statistiques), et l'intitulé de la ligne 85 ne dit pas que le matériau mêle, s'il le fait, des classes de statistiques et des classes de déplacements.
- Correction proposée : préciser l'objet (recommandation : classes de déplacements, et la statistique jointe dans le champ (e)).

## Décompte
- Constats CA6-V2 : corrigés 6 (02, 03, 04, 07, 08, 09 ; 07 et 08 sous réserve de pièces non ouvertes) ; partiellement 3 (01, 05, 06) ; non corrigé 0.
- Constats nouveaux : bloquant 0 ; majeur 3 (CA6P7-01, 02, 03) ; mineur 3 (CA6P7-04, 05, 06).
- Après correction, un contrôle de conformité par `diff` des lignes modifiées, par un lecteur neuf, suffit ; pas de nouvelle contre-lecture complète nécessaire.
