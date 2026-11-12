# Synthèse du tour du collisionneur — règle de repli de la porte G0 — v1

Sous-agent neuf (Fable 5.1), lancé par « session-depot » ; il n'a écrit ni la question ni aucune cellule. Lecture dès
2026-10-29 10:28 UTC, rédaction finie 10:45 UTC (`date -u`). GO-2026-10-29-10. Ni réseau, ni commit, rien d'interdit ouvert.
Longueur : ≈ 2 480 mots hors renvois (fichier, ligne), ≈ 3 060 avec. **Matériau pour la décision de Lazar ; ne tranche rien.**

**Pièces.** Run v2, neuf cellules valides, empreintes vérifiées, modèles servis comme demandés, 6,83 USD :
`…/collisionneur-repli-g0/tour-v2/run-repli-g0-e3-v2/cellules/E3-{T1-conception,T2-redteam,T3-riposte}-{A,B,C}.md`, notées
T1-A … T3-C (A = Claude Fable 5.1, B = Claude Opus 5.5, C = Gemini Argon) ; « l. n » = ligne du fichier. Run v1 (trois T1,
deux T2 valides, 3,19 USD) : secondaire, § 6. Avis Fable `docs/notes/porte-g0-repli-v1/avis-fable-repli-g0-v1.md`
(`f3435cfd…`, recalculée) ; avis conv-audit sur le canal (`62cc6fbf…`, recalculée). Grille brouillon
`prereg/brouillon-G0-grille-lecture-v1.md` (`320af9b0…`), son avis Fable, n° 199 de conv-audit. Priment : N-027 (critères
inchangés) ; R-750 (report unique borné au 31 janvier 2027, 23:59 UTC).

**Critères de lecture gelés** (question v2, l. 29-33) : « commune » = même option principale **et** même borne chez deux
modèles au moins ; modifier, assouplir, réinterpréter un critère = « hors cadre » ; décision laissée au lecteur = « non
scellable ».

## 1. Table des neuf cellules

T2-A, T2-B, T2-C (équipe rouge croisée) ne proposent rien : § 3. Borne : 31 janvier 2027, 23:59 UTC chez les six autres
(servie comme fait, question l. 12-13 : convergence par construction). Mots des clauses recomptés ici.

| Cellule | Option principale | Déclencheur | Pendant le report | Second verdict | Interdit le second report | Clause | Anglais |
|---|---|---|---|---|---|---|---|
| T1-A | report unique **sauf** « non tenu définitif » (liste d'arrêt scellée déclenchée) → non franchie sans report (l. 116, 121) | tenu / provisoire / définitif / non concluant ; NC = provisoire → report (l. 109-116) | table l. 128-135 ; ρ pour 6 seul ; plafond 1 400 USD (l. 138) | tout ≠ franchie = définitif ; nouveau programme (l. 145) | « unique », empreinte, R12, R4 (l. 147) | l. 151, 142 mots | l. 157, 39 |
| T1-B | report unique **sauf** NT-réfuté sur 2 ou 3 → non franchie sans report (l. 65-74, confiance 0,55) | T / NT-absent / NT-réfuté / NC ; NT domine (l. 37-57) | table l. 92-100 ; 3-4 sur « dossier 2 scellé » ; 250 USD illustratif (l. 106-110) | NC = NT ; nouveau brief (l. 120-124) | gel par empreinte, horodatage, abrogation consignée (l. 146-150) | l. 156, 147 | l. 160, 40 |
| T1-C | NC → report ; NT → fermeture dès le 30 nov. sauf « repli technique pré-inscrit » (l. 103-106) ; **la clause dit l'inverse** (l. 174) | TENU / NON TENU (run valide, seuil manqué) / NON CONCLUANT (run non fait) (l. 87-97) | table l. 116-123 ; min(250 USD ; 5 %), tranches sur « empreinte de réussite » (l. 129-134) | NF ou NC → arrêt, restitution (l. 143-153) | empreintes en dur, « dead-man switch » (l. 164-166) | l. 174, 148 | l. 183, 39 |
| T3-A | report unique **sauf** définitif **élargi** : liste d'arrêt déclenchée, **ou** 2/3/4 sans préenreg. scellé à liste d'arrêt, **ou** run sans résultat scellé (l. 118-120) ; arrêt anticipé = second verdict avancé (l. 24) | « non concluant » n'est pas une issue de porte, vaut provisoire (l. 122) | 3-4 après « dossier 2 scellé » ; ρ après 3-4 et cécité ; plafond < 300 USD, coupe-circuit fournisseur (l. 128-130) | tout ≠ franchie = définitif ; rapport liste tout résultat lu (l. 134) | empreinte complète au registre ; « aucun ajout de condition » (l. 20) | l. 138, **159** | l. 142, 39 |
| T3-B | **report uniforme** : tout ≠ franchie → report ; critère réfuté **gelé** (l. 68-69) ; C5 retirée (l. 25) | T / NT / NC ; garde rouge = NC (un rerun) ; monotonie ; rétention (l. 66-76) | table l. 80-88 ; 3-4 si 2 est **T** par script ; ρ si 3 et 4 T ; montant à Lazar ; plafond chez le fournisseur (l. 38, 52) | tout ≠ franchie = définitif ; GO confirme ou une contre-expertise, la moins favorable prévaut (l. 31, 92) | empreintes hors dépôt chez Lazar ; horodatage choisi par Lazar (l. 27, 33) | l. 92, 142 | l. 96, 37 |
| T3-C | NC seule → report ; un NT → fermeture dès le 30 nov. ; NT élargi à « pas de préenreg. pour 2/3/4 », « brief v3 cité » (l. 89-91) ; arrêt anticipé si 2 devient NT (l. 94) | TENU / NON TENU / NON CONCLUANT, cause consignée (l. 88-90) | 6-7-8 sans GPU ; 3-4 après verdict R13 « 2 tenu » ; 250 USD (l. 94-95) | NF ou NC → arrêt de G1 ; papier C : SUPPOSÉ (l. 98) | empreintes hors dépôt ; caducité ; silence du GO 48 h (l. 91, 100) | l. 103, **197** | l. 106, 37 |

## 2. Commun, divergent, hors cadre, non scellable

**Commun après le tour 3** (deux modèles au moins, même option, même borne) :
1. Report **unique au 31 janvier 2027, 23:59 UTC**, critères inchangés : 3/3 (T3-A l. 138 ; T3-B l. 92 ; T3-C l. 103).
2. Second verdict : **toute issue autre que « franchie », « non concluante » comprise, vaut non franchie définitivement ;
   aucun troisième verdict** : 3/3 ; absence de verdict scellé à l'heure butoir vaut non franchie (T2-B l. 193 ; T3-C l. 100).
3. **Un critère réfuté par résultat scellé n'est jamais retenté** (R3, R-680) : 3/3 (T3-A l. 65 ; T3-B l. 69 ; T3-C l. 13).
4. **Aucune expérience décisive de G1 ni du papier C, aucune lecture de f_A pendant le report** : 3/3.
5. **Le GO ne requalifie jamais une issue** ; aucun état « suspendu » : 3/3 (T3-A l. 124 ; T3-B l. 31 ; T3-C l. 91).
6. **Verrou anti-réécriture** : non le hachage de v2 (vide sous R12, T2-B l. 17-21) mais l'empreinte complète tenue **hors
   dépôt par Lazar** (T3-B l. 33 ; T3-C l. 16) et chaque préenregistrement citant v2 **sans ajout de condition** (T3-A
   l. 20 ; T3-B l. 127 ; T3-C l. 89).
7. **Préenregistrements de 2, 3, 4 scellés, contre-lus, à liste d'arrêt, avant le 30 novembre**, leur absence valant « non
   tenu » : A et C (T3-A l. 118 ; T3-C l. 89) ; hypothèse chez B (T2-B l. 194).
8. **Plafond absolu fixé avant le 30 novembre, séquencé (2 d'abord), appliqué chez le fournisseur** : 3/3 sur la forme.
   250 USD chez A et C = artefact d'un même calcul heures-GPU (T2-A l. 8) ; B renvoie le montant à Lazar (T3-B l. 38) ; A le
   borne sous les 300 USD de la banque (T3-A l. 130).
9. **Déblocage de 3 et 4 par un statut « 2 tenu » prononcé, jamais par empreinte ni dossier scellé** : B et C (T3-B l. 32 ;
   T3-C l. 22). **A diverge** (« dossier complet scellé », T3-A l. 128) : faille F-B8 gardée (T2-A l. 31).
10. Rapport de porte : union de T1-A l. 146, T1-B l. 135-142, T1-C l. 157-161, cause de chaque preuve manquante (T3-B
    l. 27), tout résultat lu (T3-A l. 134).

**Divergence principale, non résolue** : *ce qu'un négatif scellé fait à la porte*. A et C ferment sans report (au 30
novembre ou pendant le report, verdict avancé) ; B ouvre le report uniforme et gèle le critère, la porte ne pouvant plus
être franchie (T3-B l. 69). A et C sont « commun » au sens gelé ; les deux avis indépendants vont du côté de B (§ 4). Effet :
sous B, deux mois sur 6, 7, 8 à issue connue ; sous A et C, fermeture par un résultat, non par une date. Réalisme (T2-A
l. 17) : un négatif scellé au 30 novembre est improbable (aucun organisme, calcul échu le 1er novembre) ; la divergence porte
surtout sur l'**arrêt anticipé du report**.

Secondaires : rôle du GO (A : confirme ; B : une contre-expertise ; C : silence 48 h) ; pilote ρ pendant le report (A, B :
oui, conditionné, aveugle ; C : non, T1-C l. 121) ; corpus du critère 8 (A : règle par répertoires, `brouillons/` inclus,
T3-A l. 44 ; B : tout fichier versionné, quarantaine à trancher, T3-B l. 59-64).

**Hors cadre, écarté** : seuils chiffrés des critères 2 et 3 dans la règle (T1-C l. 38, 200 ; T2-A l. 70 ; retirés T3-C
l. 14) ; « repli technique pré-inscrit », « pas le même protocole » (T1-C l. 105, 174 ; retirés T3-C l. 13) ; discrétion
exigée au critère 2 (T1-A l. 84 ; T2-B l. 23 ; retirée T3-A l. 21) ; « scores finis ≥ 0,99 » importé dans le critère 2
(T1-C l. 118 ; T2-A l. 72 ; retiré) ; manifeste du critère 8 choisi à la main (T1-B l. 173 ; T1-A l. 90 ; remplacés) ;
condition de progrès (T1-A l. 76 ; retirée T3-A l. 86).

**Non scellable, écarté** : GO qui « suspend » sans échéance (T1-B l. 81 ; T2-A l. 29) ; GO qui « invalide pour vice de
forme », audit R4 postérieur (T1-A l. 124, 147 ; T2-B l. 48-50 ; retirés T3-A l. 26-27) ; exception « NT-réfuté » sans gardes
pré-scellées (T1-B l. 74 ; T2-A l. 17 ; retirée T3-B l. 25) ; nœud de réorientation (T1-B l. 129-131) ; pivot papier C après
lecture (T1-C l. 152) ; clause de C contredisant son point 1 (T2-A l. 66) ; plafond « min(250 ; 5 %) » valant 0 sans
financement (T2-A l. 76) ; « dead-man switch sans intervention humaine » (T2-A l. 74 : convention, pas mécanisme).

## 3. Attaques qui tiennent, et ripostes

| cible | attaque (tour 2) | riposte (tour 3) |
|---|---|---|
| A | inaction récompensée : résultat plat non scellé, aucune liste d'arrêt → tout reste « provisoire » (T2-B l. 57-58 ; T2-C l. 35-38) | absence de liste d'arrêt et run sans résultat scellé valent définitif (T3-A l. 24, 42) ; limite admise : « seul le harnais écrit des manifestes » non prouvé (l. 165) |
| A | E1 teste « (i) ou (ii) » contre la conjonction (T2-C l. 16-18) ; hacher v2 ne teste que R12 (T2-B l. 17-21) | corrigé (l. 37) ; verrou déplacé (l. 20) |
| A | 1 400 USD = banque de G1, frontière de fuite (T2-B l. 44 ; T2-C l. 13-15) | plafond < 300 USD (l. 25, 36) |
| A | E2 lit le paquet réel, corrige le manifeste jusqu'à l'accord (T2-B l. 34-37 ; T2-C l. 19-20) | paquets synthétiques par instance neuve, vérificateurs exclus (l. 23, 38) |
| A | pas d'antériorité ; pilote ρ confondu, fuite sur G1 (T2-C l. 53-54, 23-25, 59-60) | horodatage externe SUPPOSÉ (l. 45) ; conditions, cécité (l. 40, 48) |
| B | C5 exige un audit après lecture (T2-A l. 17) ; report déclenché par qui en profite, via NC (l. 21) | C5 retirée (T3-B l. 25) ; NC ne rapporte plus rien ; cause consignée (l. 27) |
| B | scellé ≠ tenu (T2-A l. 31 ; T2-C l. 68-70, 89-92) ; un vice de forme blanchit un négatif (T2-C l. 71-73, 85-88) | statut T par script (l. 32) ; monotonie (l. 71-73) |
| B | GO « suspend » (T2-A l. 29 ; T2-C l. 74-76) ; références dans le dépôt (T2-A l. 33) | supprimé (l. 31) ; copie chez Lazar (l. 33) |
| B | critère 6 sans dépense, ρ impossible (T2-C l. 77-79) ; annexe de code (l. 93-96) ; dépassement fournisseur (l. 97-100) | dépense si 3 et 4 T (l. 47) ; fermeture transitive (l. 51) ; plafond dur SUPPOSÉ (l. 52) |
| B | acteur unique (T2-A l. 114) | réduit, pas supprimé (l. 36) ; résidus : garde rouge à dessein, a priori de famille (l. 209-212) |
| C | clause contre point 1 (T2-A l. 66 ; T2-B l. 108-111) ; repli technique = chasse au signe positif (T2-A l. 68 ; T2-B l. 113-116) ; seuils dans la règle (T2-A l. 70) | alignée sur 1B pure (T3-C l. 12) ; supprimé (l. 13) ; retirés (l. 14) |
| C | verrous fictifs (T2-A l. 74) ; phrase au financeur fausse et promettante (T2-A l. 78 ; T2-B l. 138-140) ; empreinte ≠ réussite (T2-B l. 128-131) | copie externe (l. 16) ; réécrite (l. 18) ; verdict R13 intermédiaire (l. 22) |
| C | NC récompense l'incomplétude (T2-B l. 117-121) | préenregistrement obligatoire accepté ; **rejeté sur le calendrier** : des runs complets exigés avant le 30 novembre rendraient le report impossible (l. 21) — vrai pour toute clause |

**Tient encore** (lecture de la synthèse) : dépendance résiduelle à un acteur unique, admise par les trois ; horodatage
externe et plafond fournisseur SUPPOSÉS ; chez A, déblocage sur dossier scellé (§ 2, 9) et clause de 159 mots ; chez C,
clause de 197 mots et règle en états de porte, incompatible avec la grille (§ 4) ; chez A, « si E2′ échoue, la table se
réduit au script » (T3-A l. 150), alors qu'un script outille R13 sans le remplacer (T2-B v1 l. 30).

## 4. Comparaison avec les deux avis indépendants

| point | avis Fable | avis conv-audit | collisionneur v2 |
|---|---|---|---|
| forme | porte **prononcée** non franchie, phase 0 poursuivie une fois, seconde et dernière lecture (l. 13-15, 68-74) | report une seule fois, puis clôture (l. 39-46) | report unique, puis clôture : 3/3 |
| borne | 31 déc. 2026, « un choix » (l. 102-104) | 31 déc. 2026, « 31 janvier à Lazar » (l. 49-51) | 31 janv. 2027 (R-750) |
| NF / NC | porte binaire ; porte « non concluante » = « on verra » (l. 48-49) | même clause pour les deux (l. 23-25) | même suite (A, B) ; C diverge |
| négatif scellé au 30 nov. | note négative publiable, reprise sur les critères non prouvés (l. 86-87) : **pas de fermeture** | non dit | A, C : fermeture ; B : gel |
| conditions | préenreg. de reprise ≤ 7 déc. ; grille ≤ 15 nov. ; devis joint au verdict (l. 76-85) | table de dépendance scellée par une main sans accès aux résultats (l. 56-57) | préenreg. de 2, 3, 4 ≤ 30 nov. (A, C) ; table scellée : 3/3 |

Convergence forte sur la structure : une seule seconde lecture, même grille, clôture, aucune suite propre pour « non
concluante », grille et table scellées d'avance, lecteur d'une autre lignée (avis Fable l. 133 ; D-G0-6). La borne des avis
cède au mot de Lazar. Seul écart avec la majorité du collisionneur : la divergence du § 2. **Grille** : elle expose les
sous-états « absent / négatif / invalide / non concluant » pour qu'une clause en dépende sans décision du lecteur (brouillon
l. 426-433) ; n° 199 la juge sûre. Une clause en sous-états (A, B) y est compatible ; celle de C, en états de porte, non :
sous la grille, un préenregistrement sans run est « non tenu — absent », la porte serait « non franchie » le 30 novembre et
le report ne s'ouvrirait jamais.

## 5. Clause recommandée, dépendances, choix, phrase

**Clause (150 mots), vocabulaire de la grille ; confiance 0,6 sur la structure, 0,5 sur (a).**

> Si le verdict scellé de G0 (R13), rendu au plus tard le 30 novembre 2026 à 23:59 UTC, n'est pas « franchie », la porte
> est reportée une seule fois au 31 janvier 2027 à 23:59 UTC, sur les huit critères inchangés du brief v2 (empreinte tenue
> hors dépôt), sous conditions : (a) un critère « non tenu — négatif » (liste d'arrêt scellée déclenchée) n'est jamais
> retenté et rend la porte non franchie définitivement, même pendant le report ; (b) un critère 2, 3 ou 4 sans
> préenregistrement scellé à liste d'arrêt au 30 novembre vaut « non tenu — négatif » ; (c) pendant le report, seules les
> tâches de la table de dépendance scellée continuent, sur devis sous un plafond fixé d'avance, sans expérience décisive de
> G1 ni du papier C ; (d) au second verdict, toute issue autre que « franchie », « non concluante » comprise, vaut non
> franchie définitivement ; aucun troisième verdict ; toute reprise exige une nouvelle version du programme.

Variante B et avis pour (a) : « … n'est jamais retenté ; son statut est reporté tel quel au second verdict ».

**Table de dépendance** (commun ; divergences marquées) :

| critère | continue (sans dépense) | dépense sur devis | gelé |
|---|---|---|---|
| 2 | préenreg. R1, R2, liste d'arrêt, gardes pré-scellées | (i) et (ii), dose-réponse (pilote, pas la banque) | banque de G1 ; toute tentative après un négatif scellé |
| 3 | code, run factice | sondes v0, plancher apparié, **après « 2 tenu » prononcé** (B, C ; A : dossier scellé) | comparaison contre les bases (G1) |
| 4 | code, déterminisme, scores finis sur notations rejouées | juges sur les épisodes de 2, même condition | lecture par mode, f_A, banque |
| 6 | trancher N2, N3, bris d'égalité ; rédiger, contre-lire ; simulations | pilote ρ seul, après 3 et 4 tenus, sortie aveugle (A, B ; C : rien) | f_A, mode tenu à l'écart, toute cellule décisive |
| 7 | rédiger, contre-lire | aucune | expériences HC1–HC3 |
| 8 | inventaire par règle, vérification PDF et page (R7) | aucune (accès payant : SUPPOSÉ) | — |
| 1, 5 | gel du code | ré-exécution au 31 janvier si l'environnement a bougé (T3-B l. 56) | — |

**Liste fermée des choix à fixer avant le 30 novembre.**
1. (a) : fermeture sans report (A, C) ou report avec critère gelé (B, deux avis).
2. (b) : absence de préenregistrement pour 2, 3, 4 = « négatif » (A, C) ou = « absent », report ouvert (B).
3. Grille scellée au plus tard le 15 novembre, D-G0-1 à 9 tranchés ou échus, même grille aux deux lectures ; le verdict rend
   constatable « préenregistrement scellé présent » par critère.
4. Empreintes de référence (brief v2 complète, clause, grille, script de verdict) hors dépôt chez Lazar ; horodatage externe
   (SUPPOSÉ disponible).
5. Plafond : montant (250 USD illustratif, sous 300), séquence 2 puis 3-4, application chez le fournisseur ; remplacement de
   GO-2026-10-04-08 (échu le 1er novembre) ; imputation hors budget financé jusqu'à G0 (SUPPOSÉ).
6. Table de dépendance scellée par une main sans accès aux résultats ; pilote ρ pendant le report : oui ou non.
7. Périmètre du critère 8 (D-G0-9) ; statut des branches en quarantaine.
8. GO après verdict : confirme ; ou une contre-expertise, la moins favorable prévalant ; ou silence vaut confirmation.
9. Sous-agents R13 (30 novembre, 31 janvier, verdict avancé), d'un autre modèle, exclus des tests de la règle.
10. Tests de la règle sur dossiers synthétiques écrits par une instance neuve, avant le 30 novembre, sur processeur (T3-A
    E2′, E6, E7 ; T3-B E1′ à E5′ ; T3-C Exp. 1).
11. Gabarit du rapport de porte écrit d'avance ; R-750 porté dans `docs/decisions/` près de N-027 ; aucune condition de
    progrès (décision explicite).
12. Sort du papier C et du palier GC fin M2 si G0 échoue ; défaut de l'avis Fable : rien ne s'ouvre avant G0.

**Phrase pour le financeur (39 mots)** : « If gate G0 is not passed on 30 November 2026 on its eight unchanged criteria, it
is re-assessed once, by 31 January 2027; no G1 experiment runs meanwhile; any other outcome then closes this program
version. Nothing is promised. » Tant que rien n'est scellé, la phrase vraie reste « no fallback rule is written yet »
(pièce C, point 12 ; avis Fable l. 144-145).

## 6. Réserves

- **SUPPOSÉ** : financement au 1er décembre (la pièce C servie est coupée et ne le dit pas : T1-B l. 17, T1-C l. 11) ;
  horodatage externe ; plafond fournisseur ; dépendance du critère 4 aux organismes ; indépendance de HC1–HC3.
- **Illustratifs** : 250, 150, 100 USD ; 7 jours ; 48 heures ; tous les seuils d'expériences. 300–1 400 USD et 90 USD :
  RAPPORTÉS de la pièce B, non vérifiés ici.
- **Empreinte fausse de la pièce A** : faits v1 et v2 citent le brief v2 sous `d5ac34db…` ; le fichier vaut
  `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` (conforme à `docs/sha256sums-lancement-v2.txt`). Le
  texte servi est identique aux lignes 190-201 du brief (comparé ligne à ligne) : bon texte, mauvaise empreinte ; toute
  clause citant « d5ac34db » est à corriger.
- **Pièces B et C coupées** (signalé par toutes les cellules ; constaté dans `faits-repli-g0-v2.md`).
- **Run v1** : arrêté par un refus de Fable en T2-A, classé « bio » (R-748, R-750), faux positif probable sur « organisme »,
  « dose-réponse », « sabotage ». Sa question diffère de la v2 au-delà du glossaire et de la borne (quatre livrables, non
  six). Ses conceptions convergent déjà sur une seconde lecture unique (A v1 : 31 décembre ; B v1 : 31 janvier ; C v1 :
  « G0-bis » le 21 décembre, report sous un autre nom selon T2-B v1 l. 74) ; ses attaques anticipent celles du v2 (T2-B v1
  l. 15-40).
- **Non vérifié** : sources derrière la pièce B ; GO-2026-10-24-05 échu le 30 novembre selon l'avis Fable (l. 130) ; table
  de dépendance de conv-audit (`e2480618…`) ; qu'un préenregistrement de T0.6, T0.7 ou T0.8 puisse être scellé avant le
  30 novembre.
- Coût des deux runs : 3,19 + 6,83 = 10,02 USD, sous les 15 USD de GO-2026-10-29-07 et les 11,8 de GO-2026-10-29-10.
