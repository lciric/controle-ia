# Vérification des corrections — brouillon 2 de l'addendum 2 de P3 (audit des remarques 1 à 3 du verdict) — v1

**Verdict : scellable après corrections.** Les treize constats RB-01 à RB-13 sont traités dans le brouillon 2. Onze sont
corrigés juste. Deux le sont en partie : RB-04 (précédent de B3 et phrase de lecture) et RB-06 (instabilité de la part pour
B2). Le différentiel mot à mot ne montre aucun changement hors des corrections, sauf une suppression non listée, sans
effet sur une règle. Douze constats nouveaux : aucun bloquant, aucun majeur, sept mineurs, cinq pour information. Le plus
utile à corriger avant le scellement : les gardes 7 et 9 se contredisent pour une entrée « non calculable » ou « en échec »
(VB2-01), et la liste fermée des tests ne couvre pas les règles de réserve ajoutées (VB2-02). Aucune grandeur de B1 ni de B2
n'apparaît dans le texte ; R1 tient.

## Cadre

- Vérificateur : sous-agent neuf (R2). Je n'ai écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture 1, ni le
  traitement, ni P3, ni son code, ni le premier addendum, ni le verdict.
- Brouillon vérifié : `…/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon2.md`, sha256
  `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615` (504 lignes), égal à l'empreinte de la commande.
  Brouillon 1 : `2698af04fdd1c9c3fafb97e4835bf0e85dbabd145156dbbda06515602d23ab90`. Contre-lecture 1 :
  `ad360e028ae0d9f08941bbab689631aea763e3966fe7f0be4fc5ed3cc3a112d1`. Traitement :
  `dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392`.
- Lu : les quatre fichiers de la commande en entier ; les notes de rédaction du brouillon 1 (questions 1 à 14) ;
  [P] l. 118-185, 205-216, 268-290, 318-324, 390-440 ; [PA] l. 125-140, 164-176, 196-262 et sa section « Contre-lecture » ;
  [V] l. 224-252, 280-305, 320-380 ; `lecture.py` l. 55-434 ; `statistiques.py` l. 1-130 ; `conditions.py` l. 28-34 et
  98-113 ; `run.py` l. 76-81 ; `prereg.py` en entier ; `manifeste.py` l. 68-98 ; `harnais/validation_reelle.py` l. 55-85 ;
  le module du premier addendum par recherche de mots (`COMMANDE`, garde de second passage) ; registre des décisions,
  lignes N-025, R-264 à R-268, N-028 ; brainstorm sur la suite de P3 : `objections-2.md` l. 30-40, `objections-1.md`
  l. 138-142, `reponses.md` l. 310-313, `note-decision-suite-P3-v1.md` l. 45-56.
- **Non lu** : `prereg/P3-consignes-v1.md` ; tout texte d'action ; toute clé ; aucune donnée du run ([S], [J], [T]) ; aucune
  sortie de lecture ([L], [A]) ; aucun manifeste de run. Les empreintes des onze entrées sont lues dans leurs fichiers
  compagnons `.sha256`, jamais recalculées sur les données.
- Calculé : B3 seulement, sur les nombres arrondis de [V] (l. 290-293), avec la bibliothèque standard ; aucune grandeur
  de B1 ni de B2, sur aucune donnée, réelle ou synthétique.
- Lecture seule. Git en lecture (`rev-parse`, `status`, `log`, `cat-file`, `merge-base --is-ancestor`, `diff --quiet`,
  `show <commit>:<registre>`). Validateur `prereg.problemes` lancé depuis `/tmp`, avec `-B` et `PYTHONDONTWRITEBYTECODE=1`.
  Seule écriture : ce rapport, dans le bloc-notes.

## Vérifications faites (conformes)

- **Empreintes de tête**, recalculées sur disque : [P], [PA], [V], [N25], [N26], [PW] et `puissance_p3.py`, les six modules
  gelés, `objections-2.md` (`34c47aa7…`, égale à son compagnon) : toutes égales. [D] et [G] au commit `ec1d71b` :
  `ac9b2cdb…` et `1b762c12…`, égales. Les onze entrées : égales à leurs compagnons.
- **Commits** cités (`97dd829`, `e03df08`, `f7cea56`, `ec1d71b`, `7a54d43`) : présents, tous ancêtres de la tête actuelle
  `116e8bc` (R-268). Dépôt non superficiel. Arbre de travail propre. **Arbre gelé** (`CHEMINS_GELES` entier) à la tête
  égal au commit cité `7a54d43` (`git diff --quiet`, code 0).
- **Validateur** : huit sections présentes et non vides ; seuls restent les marqueurs `<<…>>` attendus
  (`CHEMIN_RAPPORT_CODE`, `DUREE_MESUREE`, `EMPREINTE_MODULE`, `EMPREINTE_TESTS`, `NOMBRE_TESTS`, `SHA_BROUILLON_CODE`,
  `SHA_RAPPORT_CODE`, `SHA_TRAITEMENT_1`). La section « Contre-lecture » a ses deux empreintes pour l'entrée 1.
- **Renvois nouveaux du brouillon 2** : [P] l. 125-126 (clause du témoin), l. 156, l. 282-283, l. 434-435 (« témoin ou
  mention qui gonfle le coût ») ; `lecture.py` l. 148-157 (`effet_ou_non_calculable` : non calculable = `calculable`,
  `motif`, `effet`, `bas`, `haut` nuls), l. 240-246 (P3-P2 et mention passés par `descriptif`, sans `etablie`), l. 242
  (`etablie` sur P3-P1 seulement), l. 301-308 (`P3-P4[p]["conforme"]`), l. 323-357 (`intention[p]["T<k>"]["etabli"]`) ;
  `statistiques.py` l. 74-77 (clés de `effet_cout_apparie`) ; `couts_par_tache` (l. 144 : NaN devenu None) ; [V] l. 296-302
  (section 6, point 2) et l. 355-357 (remarque 3) ; `objections-2.md` l. 37 (fait 3 : 0,632 et 0,597, même formule) : tous
  justes.
- **B3 refait** : `z` = 2,2414027276049464 ; `z80` = 0,8416212335729144 ; facteur 1,3754886. Tromperie : `w` = 0,0435 ;
  distance basse 0,0435 ; aire au seuil 0,6152 (les deux définitions) ; `A_80` 0,63153. Enjeux : `w` = 0,04435 ; distance
  basse 0,0435 ; aire au seuil 0,57995 à la demi-largeur, **0,5791 à la distance basse** ; `A_80` 0,59660 et 0,59543.
  Hypothèses écrites : `A_80` de 0,55439 à 0,58089 ; aire au seuil 0,545 à 0,567. Les nombres de RB-12 sont justes.
- **Comptes** : 47 clés (3 × 9 + 4 × 5) ; treize constats de la contre-lecture 1 (trois majeurs, sept mineurs, trois pour
  information) ; « neuf contrôles lus au plus » dans ce run (voir VB2-06).
- **Table des cas de B1** : chaque case est égale aux conditions de la table des réserves (six cases contrôlées une à une).
- **R1** : aucun nombre nouveau dans le brouillon 2, hors de B3 (0,632, 0,597, 0,5791) et des empreintes. Aucune grandeur
  de B1 ni de B2. Le registre (R-264) dit qu'aucune n'a été calculée. Les registres R-265 à R-268 et N-028 n'en rapportent
  aucune.

## Corrections RB-01 à RB-13

| constat | état dans le brouillon 2 | où | remarque |
|---|---|---|---|
| RB-01 (majeur) | corrigé | table des réserves (l. 286) ; Critères (l. 369) ; Prédiction (l. 122) ; plan, point 8 | même règle et même cible `P3-P1` pour le témoin et la mention ; renvois [P] justes. La mention de `T3/<p>` « sans objet dans ce run » a disparu (VB2-09). |
| RB-02 (majeur) | corrigé | table des réserves (l. 287) ; table des cas (l. 294-304) ; Critères (l. 366) ; Prédiction (l. 121) ; symétrie des repères (l. 305-310) | la table est complète et cohérente avec les conditions. Conséquence non écrite : toute case porte une réserve (VB2-07). |
| RB-03 (majeur) | corrigé | Métrique, Entrées (l. 151-159) ; tests (l. 463-464) | clés écrites entrée par entrée, justes au code gelé. Reste un conflit avec la garde 7 (VB2-01). |
| RB-04 | **en partie** | Statut (l. 64-68) ; Critères (l. 370) ; Limites 6 (l. 492-493) | objecteur 2 cité avec chemin et empreinte ; « n'exclut pas une aire inférieure à `A_80(p)` » écrit. Manquent la note de décision demandée par RB-04 et le report dans la phrase de lecture (VB2-03). |
| RB-05 | corrigé | M3 (l. 170-175) | NaN ; comptes propres (retirées toutes, lisibles, nulles ; illisibles d'origine). Juste au code (`couts_par_tache`, `cout_de_tache`). |
| RB-06 | **en partie** | M5 (l. 190-193) ; déclencheur 3 (l. 393-394) ; garde 15 (l. 456-457) | part descriptive, échec sans effet sur `D`, déclencheur 3 « non calculé » si `E0` = 0 : justes. La règle « instable » pour B2 repose sur une attente sans fondement (VB2-04). |
| RB-07 | corrigé | M5 (l. 192-193) ; Seuil (l. 274-276) ; symétrie des repères (l. 307) | reste du vocabulaire ancien dans l'audit de symétrie (VB2-10). |
| RB-08 | corrigé | Critères (l. 365) | « la cause n'est pas mesurée (unité, échelle des propositions, gonflement) ». |
| RB-09 | corrigé | Seuil (l. 292) ; plan, point 8 (l. 348-349) | « un contrôle par règle de réserve et par cible » ; neuf. Le compte vaut pour ce run seulement (VB2-06). |
| RB-10 | corrigé | garde 5 (l. 423-428) ; tests (l. 461-462) | chaîne exacte, égale à la convention du premier addendum (`COMMANDE` du module, versée au manifeste) ; condition parenthésée ; test « commit du manifeste ≠ tête vérifiée ». |
| RB-11 | corrigé | Statut (l. 61-64) | A9 et A6 de [PA] l. 164-173 et l. 196-198 : description juste ; [V] l. 247-248 ne lit pas les descriptifs de [A]. |
| RB-12 | corrigé | Prédiction (l. 139-141) | 0,5800 et 0,5791, chacune avec sa définition : justes. |
| RB-13 | corrigé | Hypothèse, B3 (l. 103-104) | juste ([V] l. 296-302 et l. 355-357). |

## Décisions du traitement sur les questions ouvertes (1 à 14)

| question | écrite dans le brouillon 2 ? |
|---|---|
| 1. Cible de la mention | oui (RB-01). |
| 2. `ampleur_au_dela_de_la_consigne` réserve nommée, complétée par `ampleur_non_resolue` | oui. |
| 3. Unité : limite écrite | oui (Limites 1). |
| 4. Grandeur de B3 | oui (M10, Seuil). |
| 5. Valeurs attendues de B3 gardées, avec le précédent | oui (Prédiction, Statut) ; précédent cité en partie (VB2-03). |
| 6. Médiane par tâche avec réserve | oui. |
| 7. Restriction des actions principale ; tâches sans forme en descriptif | oui (M3, M7). |
| 8. Deux déclencheurs, sans retrait aléatoire | oui. |
| 9. Module neuf, n'important que le code gelé ; deux contre-lecteurs du code (texte ; mutants) | **non** : ni l'interdit d'importer le module du premier addendum, ni les deux contre-lecteurs (VB2-05). |
| 10. Noms | oui. |
| 11. Verdict complété en v2, la v1 inchangée | **non** (VB2-08). |
| 12. Antériorité contre N-025 ; entrées en dur | oui (gardes 2 et 4). |
| 13. Pas de réserve générale | oui (rien d'écrit, comme décidé). |
| 14. Bornes de P3-P3 non refaites | oui (rien d'ajouté ; M10, « Exclu »). |

## Différentiel mot à mot (brouillon 1 → brouillon 2)

`git diff --no-index --word-diff` : 77 lignes ajoutées, 37 retirées ; aucun changement d'espaces seul (`-w` donne les
mêmes blocs). Chaque bloc :

1. Tête : ligne « Brouillon 2 : écrit par la session 14 (R-264)… » ajoutée (attendu).
2. Statut : phrase sur [A] (RB-11) ; précédent de B3 et « B3 n'est donc pas aveugle » (RB-04).
3. Hypothèse, B3 : phrase sur N-025 (3) (RB-13).
4. Prédiction : ligne « ampleur non résolue » (RB-02) ; réserve de la mention ajoutée à la ligne de B2 (RB-01).
5. Prédiction, paragraphe B3 : deux valeurs de l'aire au seuil (RB-12).
6. Métrique, Entrées : clés entrée par entrée ; `P3-P4` et `intention` (RB-03).
7. M3 : NaN ; comptes propres (RB-05).
8. M5 : part descriptive ; « instable » ; libellés signés (RB-06, RB-07).
9. Seuil, classement de `D` : libellés signés (RB-07).
10. Table des réserves : cible `P3-P1` de la mention, et suppression de « sans objet dans ce run, T3 n'étant pas établi »
    (RB-01 ; suppression non listée au traitement, VB2-09) ; ligne `ampleur_non_resolue` (RB-02).
11. « Un contrôle par règle de réserve et par cible » (RB-09) ; table des cas de B1 (RB-02).
12. Symétrie des repères : « dont la borne basse est dans ]0 ; log10 3] » et renvoi à `ampleur_non_resolue` (RB-07, RB-02).
13. Plan, point 8 : neuf contrôles (RB-09).
14. Critères : lignes `au_dela` (RB-08), `ampleur_non_resolue` (RB-02), mention sur `P3-P1` (RB-01), B3 (RB-04).
15. Audit de symétrie, déclencheur 3 : « non calculé » si `E0` = 0 (RB-06).
16. Garde 5 : condition parenthésée et chaîne exacte (RB-10).
17. Garde 15 : réécrite (RB-06).
18. Tests : garde 4, commit du manifeste (RB-10) ; garde 9, lecture produite par le code gelé (RB-03).
19. Limites 6 : B3 non aveugle (RB-04).
20. Contre-lecture : empreintes et chemins remplis (attendu).

Rien d'autre n'a changé : tables des documents et des entrées, gardes 1 à 4, 6 à 14, M1, M2, M4, M6 à M10, Analyses,
Règles communes et Limites 1 à 5 sont identiques au brouillon 1.

## Constats nouveaux, le plus grave d'abord

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| VB2-01 | mineur | « Liste d'arrêt », gardes 7 et 9 ; liste des tests (garde 9, « entrée en échec ») | **Les gardes 7 et 9 se contredisent.** La garde 9 (RB-03) admet une entrée P3-P2 ou mention « non calculable » ou « en échec » dans [L], sans arrêt : le contrôle qui en dépend est « non lu ». La garde 7 exige pourtant, pour P3-P2 et la mention, `effet` égal à 10⁻¹² près et `n_taches`, `taches_exclues`, illisibles et nuls égaux. Ces clés n'existent pas dans une telle entrée (`lecture.py` l. 156, l. 166). Lu à la lettre, le test « entrée en échec … sans arrêt » serait arrêté par la garde 7. Sinon, le rédacteur du module invente la règle. | Garde 7 : « pour chaque entrée, même état que [L] (calculable, non calculable, en échec, même motif), sinon arrêt ; les nombres ne sont comparés que pour une entrée calculable ». Test de la garde 9 : l'entrée non calculable ou en échec est produite par `lecture.lire` sur des tables synthétiques qui la causent (par exemple témoin sans coût lisible), jamais en retouchant [L]. Cas sain et artefact (état différent de celui recalculé : arrêt). |
| VB2-02 | mineur | « Tests (liste fermée, R5) » | **Les règles ajoutées ne sont pas testées.** RB-01 et RB-02 ajoutent une cible (mention sur `P3-P1`), une réserve (`ampleur_non_resolue`) et une table de six cases. La liste fermée n'en teste aucune. Elle a seulement « B1 et B2 passent par la même fonction », les déclencheurs de l'audit et le jeu « 100 fois trop bas ». Une liste fermée ne laisse pas la contre-lecture du code les exiger. | Ajouter : chacune des six cases de la table des cas sur un jeu construit, avec ses réserves exactes ; une borne basse décisive ≤ log10 3 : pas de `ampleur_non_resolue` ; la réserve de la mention sur `P3-P1` et sur `T3/<p>`, par la même règle que le témoin (un cas construit pour chacun, un cas sain) ; `D` ou `E_sf` non calculable : `reserve_B1_non_lue`, sans arrêt. |
| VB2-03 | mineur | « Statut » (l. 64-68) ; « Critères », ligne `reserve_B3_puissance_du_nul` ; traitement, ligne RB-04 | **RB-04 corrigé en partie.** RB-04 demandait de citer deux fichiers (`objections-2.md` et `note-decision-suite-P3-v1.md` l. 51) et d'écrire dans la phrase de lecture que la réserve est « écrite sur des nombres déjà lus ». Le brouillon 2 ne cite que l'objecteur 2 ; la phrase de lecture n'en dit rien. Le traitement dit « accepté » sans signaler ce resserrement. La même grandeur a aussi été calculée par l'objecteur 1 (`objections-1.md` l. 141 : 0,632 et 0,595) et reprise par le répondeur (`reponses.md` l. 312). | Citer aussi, avec empreinte : `docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md` (`a023093e26865a919a05364478390ac9ccf80aa6ba3447bc79ed3a1c6bb7594e`, l. 51), `objections/objections-1.md` (`d6c7949075baf0560f93699e0557fc450989a6706e94df2609f60918d56ec7da`, l. 141), `reponses/reponses.md` (`2eaef7f41b0bf7c38a531a1fc09526bf58e84dda30d599e6f8eacaa288e28d64`, l. 312). Ajouter à la phrase de lecture de B3 : « grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) ». Ou bien noter au traitement pourquoi on s'en écarte. |
| VB2-04 | mineur | « Métrique », M5 (l. 191-192) | **Attente sans fondement pour B2.** Le texte dit « intervalle de `E0` qui contient 0, cas attendu pour B2 ». Or `E0` est la moyenne de `d_∅(t)` sur `T_sf`, sous-ensemble des mêmes tâches. Les intervalles décisifs du témoin et de la mention excluent 0 ([V] l. 331-333 : borne haute −0,0650 et −0,1155). Rien n'indique que celui de `E0` contienne 0. La mention « instable » ne s'appliquerait alors pas à B2, contre le but de RB-06. Effet limité : la part est descriptive. | Retirer « cas attendu pour B2 ». Puis choisir, et l'écrire : soit la règle actuelle seule (intervalle de `E0` qui contient 0) ; soit, comme RB-06 le proposait, la part de B2 toujours rapportée avec « instable » ou non rapportée (`D` seul). |
| VB2-05 | mineur | « Emplacement » (l. 53-56) ; « Contre-lecture » (l. 503-504) | **Décision 9 du traitement non écrite.** Le traitement décide : module neuf, qui n'importe que le code gelé, aucune fonction du module du premier addendum ; deux contre-lecteurs du code (texte face au code ; mutants). Le texte dit seulement « le module importe le code gelé de P3 sans le modifier » : il n'exclut pas `docs/procedures/P3-addendum-v1/`. Ce dossier est hors de l'arbre gelé et aucune garde n'en vérifie l'empreinte. La section « Contre-lecture » annonce un seul sous-agent pour le code. | Écrire dans « Emplacement » : imports limités au code gelé (arbre du commit cité), à numpy et à la bibliothèque standard ; aucun import de `docs/procedures/P3-addendum-v1/` ; tests : aides de `tests/test_premier_test_ia_lecture.py` permises. Dans « Contre-lecture » : deux sous-agents neufs, leurs angles et leurs rapports. |
| VB2-06 | mineur | Plan, points 7 et 8 | **Compte des contrôles juste pour ce run seulement.** Contrôles écrits : 13 (B1 : 5 sur `P3-P1` ; témoin : `P3-P1`, `P3-P4/<p>` × 2 ; mention : `P3-P1`, `T3/<p>` × 2 ; B3 : `nul/<p>` × 2). Dans ce run (ligne « aucune sonde générique… », donc `P3-P4/<p>` et `T3/<p>` non établies, [V] l. 241-242, l. 280), 4 sont « sans objet » et 9 lus au plus : le texte est juste. Sur une autre ligne (run synthétique « critères 2 et 3… » des tests), jusqu'à 11 sont lus (B3 « sans objet »). « Neuf au plus » ne le dit pas. Le total écrit n'est pas donné, ce qui empêche la contre-lecture du code de vérifier `nombre_de_controles`. | Écrire : « 13 contrôles écrits (détail) ; dans ce run, 4 sans objet et 9 lus au plus ; sur une autre ligne, 11 lus au plus ». Le dire aussi à côté de `nombre_de_controles` (point 7). |
| VB2-07 | mineur | « Seuil », table des cas de B1 ; « Critères », ligne « aucune réserve sur une conclusion établie » ; audit de symétrie (l. 396-397) ; plan, point 8 | **Au moins trois réserves sont certaines, ce que le texte ne dit pas.** Avec la borne basse décisive au-dessus de log10 3 (ce run), chaque case de la table porte au moins une réserve sur `P3-P1`. Un contrôle non lu en porte une aussi (`reserve_B1_non_lue`). La ligne « aucune réserve → contrôles passés » ne peut donc pas s'appliquer à `P3-P1`. B3 ajoute deux réserves connues d'avance. L'addendum 2 rend donc au moins trois réserves, quelles que soient les données. Ce choix est prudent et juste : la remarque 1 relève un écart déjà acquis. Mais un lecteur du verdict complété pourrait lire le nombre de réserves comme un résultat. | Écrire sous la table des cas : « dans ce run, B1 classe la source de l'ampleur ; il ne peut pas la clore : toute case porte une réserve ». Au plan, point 8 : « au moins trois réserves sont certaines (une de B1, deux de B3) ; seuls le nom de la réserve de B1, la médiane et les réserves de B2 sont informatifs ». Dans l'audit : « aucune » est impossible pour B1. |
| VB2-08 | information | Plan, point 1 ; dernière puce des « Critères » | **Décision 11 non écrite** : le verdict complété est une nouvelle version, `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (R12), et la v1 reste telle quelle. Le texte dit seulement « verdict R13 complété par des sous-agents neufs ». | Nommer la v2 et dire que la v1 reste inchangée. |
| VB2-09 | information | « Seuil », ligne `reserve_B2_mention_hors_formes` | **Suppression non listée au traitement** : « sans objet dans ce run, T3 n'étant pas établi ». Elle va avec RB-01 (la mention vise aussi `P3-P1`). Le fait n'apparaît plus nulle part, ni pour `T3/<p>` ni pour `P3-P4/<p>`. | Le redire une fois, pour les deux cibles, avec le compte de VB2-06. Ou bien signaler la suppression au traitement. |
| VB2-10 | information | Audit de symétrie, point 1 (l. 386) ; « Seuil », classement de `D` (l. 274-276) | **Reste du vocabulaire ancien (RB-07)** : « formes qui ajoutent ou retirent ». Libellés non parallèles : « élèvent » et « qui l'abaissent ». « sinon. » est en colonne 0 (l. 276). | « formes qui élèvent ou abaissent la différence » ; « élèvent » et « abaissent » ; indenter « sinon. ». |
| VB2-11 | information | « Contre-lecture » | `<<SHA_TRAITEMENT_1>>` reste à remplir (traitement actuel `dfce4cca…`, qui changera s'il reçoit le traitement de ce rapport). Comme pour [PA], il faut ajouter une entrée « Contre-lecture 2 » : brouillon 2 (`641b36c2…`), ce rapport, son chemin sous `prereg/contre-lectures/` et son empreinte. Les rapports versés doivent garder leur empreinte. | À faire avant le scellement. |
| VB2-12 | information | « Seuil », table des cas de B1 | La table n'est écrite que si la borne basse décisive est au-dessus de log10 3. C'est le cas ici (1,2464). Pour les runs synthétiques des tests, une phrase manque : sinon, la case `0 < b_sf ≤ r`, `b_D ≤ 0` ne porte aucune réserve (conforme à la prédiction écrite). | Ajouter la phrase ; la tester (VB2-02). |

## Réponses aux points de la commande

- **Corrections RB-01 à RB-13** : toutes traitées ; onze justes ; RB-04 et RB-06 en partie (VB2-03, VB2-04).
- **Décisions du traitement** : écrites, sauf la question 9 (VB2-05) et la question 11 (VB2-08).
- **Rien d'autre n'a changé** : vrai, sauf la suppression de VB2-09, liée à RB-01.
- **Verrou** : aucune promotion possible. La nouvelle cible `P3-P1` de la mention est dans la table du verrou. Les clés
  `P3-P4.<p>.conforme` et `intention.<p>.T<k>.etabli` existent au code gelé. `nul/<p>` reste juste : sur la ligne
  « aucune sonde générique… », l'état du jeu saboteur contre honnête ne peut être que « non au-dessus » (`lecture.py`
  l. 169-184, l. 412-415).
- **Mécanique des réserves** : mécanique et sans trou pour B1 (table des cas) ; conflit des gardes 7 et 9 (VB2-01) ; tests
  à compléter (VB2-02) ; réserves certaines à dire (VB2-07).
- **Comptes de contrôles** : 13 écrits ; 9 lus au plus dans ce run, juste ; à écrire (VB2-06).
- **R1** : tenu. Aucune grandeur de B1 ni de B2 dans le texte ni dans ce rapport. B3 est dit non aveugle.
