# Critères de lecture — collisionneur « D-ML-1 » (taille du jeu bénin de l'estimation de la malléabilité) — v1

session-depot, 31 octobre 2026, ≈ 13:45 UTC. **Scellés avant l'ouverture de toute cellule** : aucune cellule du run
`donnees/collisionneur-dml1-v1/run-dml1-e3-v1/` n'a été lue par l'auteur de ces critères. Ils s'appliquent à la lecture des
neuf cellules valides (E3-T1, E3-T2, E3-T3 de B, C, D) et ne sont pas modifiés après scellement : une correction se fait dans
une version nouvelle, avant toute lecture des cellules (R12). Modèle : les critères du collisionneur des protocelles
(`docs/notes/protocelles-collisionneur-v1/criteres-lecture-protocelles-tour1-v1.md`, `aed5f593…`), réduits à une question
de statistique et de méthode.

Pièces : question `donnees/collisionneur-dml1-v1/question-dml1-v1.md` (identique à `question-etage3.md` du run) ; faits
`donnees/collisionneur-dml1-v1/faits-dml1-v1.md` (identiques à `faits.md` du run) ; calcul servi
`docs/notes/anteriorite-P-041-v1/calcul-taux-fausses-alertes-benins-v1.py` et sa sortie
`…/calcul-taux-fausses-alertes-benins-v1.sortie.txt` (empreintes dans leurs compagnons) ; état du run `etat.md`.

## A. Garde, absences, statuts

1. **Absence de Fable (A).** Ses trois cellules sont absentes (refus dès la première, règle R-831). A ne compte ni dans un
   accord ni dans une divergence ; aucune position ne lui est prêtée.
2. **Niveau.** La question demande la statistique et la méthode seulement. Tout passage qui sortirait de ce niveau (méthode
   d'attaque, paramètre d'évasion) est compté et signalé par sa seule classe, jamais reproduit ni résumé.
3. **Statuts des affirmations.** Chaque affirmation retenue reçoit un statut : **VÉRIFIÉ** (recalculé par le lecteur, ou lu
   dans les faits ou le calcul servis, renvoi donné) ; **RAPPORTÉ** (jeu public, papier ou outil cité par l'espèce, non
   vérifié : aucun chiffre opposable, R7) ; **SUPPOSÉ** (l'espèce le dit elle-même, ou rien ne le fonde). Les jeux bénins
   publics nommés (nom, taille, licence) sont RAPPORTÉS tant qu'aucun n'est versé et empreinté.

## B. Accord, divergence, apport seul

4. **Accord indépendant** : porté par au moins deux espèces sur trois au sous-tour T1, sur le même objet (choix (A), (B) ou
   troisième option ; un sous-point des questions 2 à 4).
5. **Convergence née de la critique** : portée par une espèce en T1, adoptée par une autre en T2 ou T3 (ou abandonnée par son
   auteur). On note qui a cédé à qui.
6. **Divergence** : choix ou signes opposés sur le même objet ; « résolue » seulement si une espèce cède en T3 en donnant une
   raison.
7. **Apport d'une seule espèce** : gardé s'il n'est pas réfuté, marqué « une source ».
8. **Vrai par construction (jamais un accord)** : ce que la question impose ou suggère : les options (A) et (B), les
   découpages 1 000 / 1 000 et 400 / 300 / 300, et les exemples de troisième option qu'elle cite (validation croisée,
   rééchantillonnage, seuil fixé sur une autre statistique, autre découpage). Choisir l'un de ces exemples n'est pas une
   invention.
9. **Symétrie (R4)** : un accord unanime à trois, ou des formulations presque identiques, est une **réserve**, pas une
   preuve ; la critique croisée homogénéise.

## C. Calculs

10. **Intervalles.** Tout intervalle ou taux de fausses alertes donné par une espèce est recalculé par le lecteur (méthode
    nommée : Clopper-Pearson ou Wilson) et comparé à la sortie du calcul servi ; écart au-delà de l'arrondi = « inexact ».
    La question 1 demande de vérifier le calcul servi : on rapporte, par espèce, si elle l'a fait et ce qu'elle a trouvé.
11. **Pire cas et changement d'avis (question 4).** Par espèce ; un choix sans pire cas ni condition de changement est
    « incomplet » (noté, pas écarté).
12. **Test de ressemblance de distribution (question 2).** Retenu s'il nomme la statistique, le seuil fixé d'avance et
    l'issue en cas d'échec ; sinon « non préenregistrable en l'état ».

## D. Synthèse

13. **Traçabilité** : chaque chiffre renvoie à une cellule et sa section, aux faits, au calcul servi (empreinte) ou à un
    recalcul montré en une ligne.
14. **Rien n'est tranché** : la synthèse présente les options et leurs conditions ; la décision est à Lazar (D-ML-1), et la
    question est aussi posée à conv-audit.
15. **Ordre** : la synthèse s'écrit après la lecture complète des neuf cellules.
