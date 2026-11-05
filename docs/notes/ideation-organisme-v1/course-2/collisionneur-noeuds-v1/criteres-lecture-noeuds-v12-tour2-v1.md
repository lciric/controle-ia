# Critères de lecture — collisionneur des nœuds de décision, question v12, tour 2 (attaque des recommandations ; sous-tours E3-T1, E3-T2, E3-T3) — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 08:07 UTC. **Scellés avant l'ouverture de toute cellule** : le run
`donnees/collisionneur-noeuds-v1/run-noeuds-v12-tour2-e3-v1/` est **en cours** à l'heure du scellement (lancé 08:00 UTC sous
GO-2026-11-01-02) ; aucune cellule n'a été lue par l'auteur de ces critères, qui ne lira que le journal de lancement, `etat.md`
et la sortie de `collisionneur_v7.py verifier` à la fin du run. Ils ne sont pas modifiés après scellement (R12). Modèle : les
critères du tour 1 (`criteres-lecture-noeuds-v12-tour1-v1.md`, `22edbf47…`), dont les critères 1, 3, 4, 5, 10, 11, 13, 22, 23 et 25
s'appliquent tels quels ; ce qui suit les complète pour un tour d'attaque des recommandations.

Pièces : question du tour 2 `donnees/collisionneur-noeuds-v1/question-noeuds-v12-tour2-v1.md` (`19ff79d9…` ; consigne des
verdicts puis l'annexe v5 de conv-audit, servie telle quelle, avec les confiances d'auteur) ; faits servis = **synthèse v2 du
tour 1** `synthese-noeuds-v12-tour1-v2.md` (`d313b482…`, 14 318 mots, seule pièce de faits ; identique à `faits.md` du run) ;
erratum `erratum-synthese-noeuds-v12-tour1-v1.md` (`24f9900b…`) pour savoir ce qui a changé entre v1 et v2 ; question v12
(`a7fac44b…`) et faits v2 du tour 1 (`ea85dad6…`) pour recouper un chiffre que la synthèse attribue au tour 1 ; cellules du tour 1
(`run-noeuds-v12-tour1-e3-v1/cellules/`) pour vérifier ce qu'une espèce dit de sa propre position du tour 1. Le lecteur ne lit
rien d'autre (ni `donnees/mode-tenu-a-l-ecart-v1`, ni `donnees/collisionneur-evasion-moniteurs-v1`, ni `donnees/bras-attaque-*`,
ni `quarantaine/`, ni `donnees/runs/`, ni `diag/`, ni `prereg/P3-consignes-v1.md`).

## A. Garde

1. **Quatre espèces présentes** ou absences acceptées : `etat.md` fait foi ; une absence (R-831) est « non rendue », pas
   « contre ». Si le run est arrêté par la garde de plafond, les cellules manquantes sont listées et la synthèse dit ce qui
   ne peut pas être conclu sans elles.
2. **Les faits sont la synthèse v2, pas les cellules du tour 1.** Toute affirmation qu'une espèce attribue « au tour 1 » est
   recoupée sur la synthèse v2 (section, ligne) ; si la synthèse v2 ne la porte pas, elle est « hors des faits servis »
   (comptée par espèce) même si une cellule du tour 1 la contient. Un chiffre que l'espèce reprend du tour 1 et qui diffère
   de la synthèse v2 est « inexact sur les pièces » (critère 5 du tour 1).
3. **Position du tour 1 vérifiée.** Ce qu'une espèce dit de sa propre position du tour 1 est recoupé sur la synthèse v2
   (tables par nœud) puis, en cas de doute, sur ses cellules du tour 1 ; un écart est « récit inexact de sa position »
   (compté, pas écarté). Un changement d'avis sans raison est « changement non motivé ».
4. **Confiance d'auteur.** La question le dit : une confiance d'auteur n'est pas un argument. Un verdict qui s'appuie sur
   la confiance de l'annexe (« 0,85 donc tenue ») est noté « s'appuie sur la confiance d'auteur » ; un verdict qui s'appuie
   sur l'identité de l'auteur (« session-depot recommande donc… ») est noté « s'appuie sur l'auteur ».
5. **Niveau et classes.** Critère 3 du tour 1 : tout passage qui donnerait une méthode ou un paramètre d'évasion (N10) est
   compté par classe, jamais reproduit. La synthèse v2 signale déjà deux passages hors niveau de C au tour 1 ; toute reprise
   en tour 2 est comptée de la même façon.

## B. Verdicts sur les recommandations (partie principale)

6. **Unité : la recommandation** (une par nœud : N1 B ; N3 D-j oui ; N4 (a) ; N5 (a) ; N6 DL-1 à DL-13, une par décision ;
   N9 (a) ; N10 (b) ; N11 : deux propositions concurrentes, session-depot et conv-audit, chacune jugée). Pour chacune et par
   espèce, en T1 puis en T3 : le verdict parmi les cinq de la question (tenue ; tenue sous condition ; renversée, avec
   l'option de remplacement ; aucune option ne tient ; indécidable sans la pièce X), la raison en une à trois phrases, le
   pire cas si la recommandation est suivie et la garde qui le ferme, et si l'avis du tour 1 change. Un verdict sans l'un de
   ces éléments est « incomplet » (noté, pas écarté). Un verdict hors des cinq formes est reclassé dans la plus proche, avec
   la mention « forme libre ».
7. **Table espèce × recommandation** : une table par nœud, verdict final (T3) par espèce, avec la condition ou l'option de
   remplacement en clair. Accord = même verdict (et, pour « tenue sous condition », condition de même nature) chez au moins
   deux espèces ; « large » à trois ou quatre ; réserve R4 (critère 10 du tour 1) sur tout accord à quatre et sur tout
   verdict « tenue » rendu sans pire cas (accord par défaut).
8. **Recommandation renversée** : l'option de remplacement est recoupée sur la question v12 (option listée) ou notée « option
   nouvelle » ; le lecteur relève si la synthèse v2 portait déjà cette option au tour 1 (chez qui) ou si elle naît au tour 2.
9. **« Indécidable sans la pièce X »** : retenu seulement si la pièce est nommée (fichier, calcul, lecture), avec ce qu'elle
   doit montrer pour chaque verdict ; obtenable sans GO (processeur, lecture, PDF versé) ou « avec dépense » (critère 13 du
   tour 1).
10. **N6 (treize décisions)** : une sous-table DL-1 à DL-13, verdict par espèce ; les trois décisions marquées « option :
    demander au collisionneur » (DL-5, DL-12, DL-13) sont relevées à part ; pour DL-12, le lecteur note si l'espèce tient
    compte de la mention « VS5-01 conteste l'avantage » (fait de l'annexe) ; les heures et le calendrier restent SUPPOSÉ.
11. **N11 (deux propositions)** : par espèce, pour chacune des deux propositions (session-depot, conv-audit) : tenue, sous
    condition, renversée ou « aucune » ; le lecteur relève si l'espèce tient compte de l'**erratum E1** tel que la v2 le
    porte (corrélation par paire non jugeable ; concordance à trois instruments jugeable seulement par l'unanimité) ; une
    espèce qui reprend la phrase fautive de la v1 (« p < 0,05 impossible », « W ≥ 0,7 rejette le seul état intermédiaire »)
    est « s'appuie sur un énoncé corrigé » (compté). N-058 : une proposition qui s'appuierait sur le verdict du juge est
    « contraire à N-058 » (notée, pas écartée).
12. **N10** : critère 18 du tour 1 ; le verdict sur (b) est relevé avec le levier et la mesure proposés, classes seulement.

## C. Divergences non résolues, accords trop propres, ordre

13. **Seize divergences** (liste de la synthèse v2, section « Questions pour le tour 2 », première liste) : par espèce, une
    position par divergence (une ligne) ; « résolue au tour 2 » seulement si les espèces présentes convergent avec raison ou
    si celles qui tenaient une position la retirent avec raison ; sinon « maintenue », positions finales par espèce.
14. **Accords trop propres** (seconde liste) : par espèce, confirme / infirme / nuance, avec la raison ; un accord trop propre
    « confirmé » à quatre reçoit de nouveau la réserve R4.
15. **Ordre** : par espèce, l'ordre proposé pour trancher s'il diffère du tour 1 ; comparaison étape par étape ; la raison de
    chaque déplacement.

## D. Synthèse

16. **Forme** : en tête, auteur (lecteur neuf, modèle nommé), date UTC relevée après la lecture complète, empreintes
    recalculées de tout ce qui a été lu, état du run ; décompte : verdicts par forme (tenue / sous condition / renversée /
    aucune / indécidable), accords et accords larges, changements d'avis motivés et non motivés, récits inexacts, affirmations
    hors des faits servis, inexactitudes sur les pièces, appuis sur la confiance ou l'auteur, appuis sur un énoncé corrigé,
    passages hors niveau (classes) ; puis une table par nœud (critère 7), la sous-table N6, la table N11, la liste des seize
    divergences avec leur statut, la liste des accords trop propres, les ordres ; enfin **la liste des recommandations telles
    que les espèces les laissent** (tenues, conditions, renversements) sans ajout du lecteur, pour Lazar.
17. **Traçabilité** : chaque affirmation renvoie à une cellule (`E3-Tn-…-X.md`, section), à la synthèse v2 (section, ligne),
    à la question v12 ou à l'annexe (ligne) ; recalcul montré en une ligne quand il y en a un.
18. **Rien n'est tranché ; aucune recommandation du lecteur** : les décisions sont à Lazar (question v12 : le collisionneur ne
    décide rien).
19. **Ordre et lecteur** : lecture complète de toutes les cellules valides avant d'écrire ; lecteur neuf, qui n'a écrit ni ces
    critères, ni la synthèse v1 ou v2, ni l'erratum ; modèle nommé ; si son modèle est celui d'une espèce, il le dit en tête.
