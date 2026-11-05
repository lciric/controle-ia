# Vérification des corrections du brouillon 7 de l'addendum de P3 (contre-lecture 5, R2)

**Verdict global (parties A et B) : scellable.**

Texte à sceller : le brouillon 8 (`bde1b2437c0caa24cd6feabe959351e3fb1342973dc2338f01271aa2d5479484`), une fois ses
marqueurs remplis. Il va avec les tests `7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3` et le module
inchangé `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996`. Ce verdict vaut pour ces trois empreintes
seulement.

- **Partie A** (brouillon 7, `c3e9c27f…`) : « scellable après corrections ». Sept constats, VB7-01 à VB7-07.
- **Partie B** (brouillon 8 et tests corrigés) : « scellable ».
  - Le brouillon 8 applique VB7-01, VB7-02 et VB7-04 à VB7-07, et rien d'autre. Chaque phrase neuve décrit le module.
  - Les tests ne gagnent que des artefacts et des cas sains. Aucun test n'est retiré, aucune assertion n'est retirée ni
    affaiblie, et le compte reste 165.
  - Les six tests retouchés passent sur le module réel.
  - Les huit mutants survivants de VF2 meurent, chacun par un artefact neuf.
  - Deux constats neufs, pour information seulement (VB7-08, VB7-09).

- Relecteur : sous-agent neuf (R2). Je n'ai écrit ni le préenregistrement, ni le module, ni ses tests, ni aucune
  correction ou relecture précédente. Date : 2026-10-20 (UTC) ; partie A de 07:14 à 07:40, partie B de 07:42 à 07:56.
- Dépôt de travail en lecture seule : aucune écriture, aucune commande git sur lui. Après mes repères de 07:26 et de
  07:42, aucun fichier du dépôt n'est plus récent (`find -newer`, hors `.git`). Les dossiers `__pycache__` du dépôt
  datent du 2026-10-19 ; aucun fichier `.pyc` n'est postérieur à 07:14. Rien lu sous `runs/`, `diag/`, `donnees/` ni
  `traces/`. Aucune commande Vast.ai.
- Tout ce que j'ai écrit est sous `verification-finale/b7/`, plus ce rapport. Tous les lancements portent `python -B` et
  `PYTHONDONTWRITEBYTECODE=1`, plus, pour pytest, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans mon dossier. Le
  module et les tests sont importés depuis mes copies, dont les empreintes sont contrôlées. Les simulations restent dans
  le processus. Je n'ai lancé ni la suite complète, ni le remplisseur, ni le versement.
- Originaux : empreintes égales au début et à la fin de chaque partie (`b7/empreintes-au-debut.txt`,
  `b7/partie-b/empreintes-au-debut-b.txt`). Il y a une seule exception, et elle date de la partie A : la session a
  réécrit en place `final-b4/test_complements_p3_v1.py` à 07:20:40 (`7605c205…` → `7387910d…`). La version relue est
  désormais gardée sous `versions-tests/test_complements_p3_v1-7605c205.py`.
- L'état « partie A » de ce rapport (sha256 `08139fdd11728f7accb6c01506a334a9ba12fd7f9288d8b98bdfffcf8f5e6388`) est
  gardé sous `b7/rapport-partie-A-08139fdd.md`.

# Partie A — brouillon 7 face au brouillon 6

**Verdict de la partie A : scellable après corrections.** Ces corrections sont faites dans le brouillon 8 et vérifiées
en partie B.

Le brouillon 7 applique tous les constats de la vérification finale destinés au texte. Il n'ajoute rien d'autre, sauf
deux mentions de traçabilité attendues. Chaque phrase neuve décrit le module, sauf une. La précision 17 neuve, lue avec
la définition de la garde 11 (« une entrée est en échec si l'un de ses calculs l'est »), exige des « non lus » d'entrée
entière que le module n'écrit pas quand l'échec vient d'un calcul (VB7-01). L'entrée « Contre-lecture 4 » dit encore
« relu face à ce texte », sans l'empreinte du brouillon relu (VB7-02). Il faut donc deux corrections de texte, d'une
phrase chacune. Le module ne change pas. Le reste du texte est inchangé. Le validateur ne signale que les marqueurs
attendus.

## Ce qui a été lu (avec empreintes)

| fichier | sha256 | lecture |
|---|---|---|
| brouillon 6 `P3-addendum-lecture-complementaire-v1-brouillon6.md` | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` | différentiel strict avec le brouillon 7 |
| brouillon 7 `P3-addendum-lecture-complementaire-v1-brouillon7.md` | `c3e9c27f3da2eb3270a8b52b24e9533734a640bb6453f2bca463fad766bb0c28` | en entier |
| module `final-b4/complements_p3_v1.py` | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` | en entier (2 289 lignes) |
| tests relus par la vérification finale (copie de `calculs/copie/`) | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` | aides ; tests des gardes 12 à 16 ; test de l'aire vectorisée |
| VF1 `verification-code-final-addendum-P3-v1-texte.md` | `7a1aa7d785f470c3fb382a513506b28ae8a9075d22bf745b22b474540e8aa628` | en entier |
| VF2 `verification-code-final-addendum-P3-v1-mutants.md` | `aab50bf0230cd923f8c0c3ee9a5f91c5f6bb6805e28ce79f2c9138abda5ecc7b` | en entier |
| VF3 `verification-code-final-addendum-P3-v1-calculs.md` | `2a0626dad4eb6c6582c2caf6deea36845ac1076a72ee5517ca9e1d13e681b750` | en entier |
| traitement `traitement-R2-addendum-P3-v1.md` (état de la partie A) | `dd2f0aeee82e7ca121dfbaaac2fce8b0cf4a22a8684ec14ae810da4e4cd2b840` | en entier ; section « Vérification finale » à la lettre |
| journaux du banc `rapports/revue-b3-3/essai_07.log`, `essai_07b_import.log` | `063661ac4a75e4f00caf0ee404189e6ffc54f1c7395d6a775647870854939fb7`, `baaf517eb27fc9eb4d5865cae962daa21e99d1cd7d1252079b874076eeb475c7` | en entier |
| script du banc `essai_07_banc_taille_reelle.py` et `commun.py` (revue CB3) | — | chemins d'import (module de `final/`) |
| rapport CB3 `rapports/contre-lecture-code-b3-3.md` | `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605` | lignes du banc (l. 13, 35, 99-110) |
| module du brouillon 3 `final/complements_p3_v1.py` | `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa` | empreinte seulement |
| outils de la session (état de la partie A) `remplir_texte_final_v1.py`, `verser_addendum_v1.sh` | `0471ac9236fafb9fc6618fcf0c43068eb70a8749f7231750f140dfc57f6d97bd`, `ddfcc1e74265a120ba00bec89e30f68f752ef54ff7ae8efa21fbb712186b8dc2` | en entier |
| code gelé (dépôt, lecture seule) | — | `sondes/evaluation.intervalle_blocs` ; `sondes/temoins.difference_aires_appariee` ; `statistiques` (`effet_cout_apparie`, `detection`, `detection_etiquettes`) ; `lecture.py` (`JEUX`, `nom_jeu`, `_permuter_dans_les_taches`, graines de la lecture) ; `manifeste.py` (`graines`, `generateur`, `creer_manifeste`) ; `run_harnais_factice.graine_entiere` ; `prereg.py` ; expressions de `validation_reelle` |

## Ce qui a été lancé

| quoi | résultat | journal (sous `b7/`) |
|---|---|---|
| différentiel par mots (`git diff --no-index --word-diff`, hors dépôt) et par lignes | 14 blocs de différences | `diff-mots-b6-b7.txt`, `diff-lignes-b6-b7.txt` |
| différentiel strict par jetons, blancs compris (`diff_strict.py`) | 54 changements de mots ; 6 changements de blancs seuls (recoupes de lignes) ; caractères spéciaux et fins de ligne inchangés | `diff-strict-b6-b7.log` |
| essais `cles`, `g14`, `g15`, `validateur`, `regex` (`essais_b7.py`) | voir (2) et (3) | `essais-rapides.log` |
| essai `p17` (précision 17) | VB7-01 reproduit | `essai-p17.log` |
| essai `p8` (précision 8, addendum complet à 60 tirages) | chaque conclusion établie a au moins un contrôle lu | `essai-p8.log` |
| validateur du dépôt, commande demandée, sur une copie du brouillon 7 | marqueurs attendus seulement | `validateur.log` |
| entrées de la section « Contre-lecture », texte rempli de valeurs factices | VB7-02 reproduit | `entrees-contre-lecture.log` |

## Constats de la partie A (le plus grave d'abord)

Aucun bloquant, aucun majeur. Trois mineurs : deux de texte, un de procédure. Quatre pour information. Chaque constat est
reproduit. Tous sont traités dans le brouillon 8 ou dans les outils (partie B).

### VB7-01 — mineur — précision 17 : « une entrée qui tombe en échec » couvre aussi un calcul en échec, où le module n'ajoute aucun « non lu » d'entrée entière

- **Où** : brouillon 7, précision 17 (l. 414-416). L'échec d'une entrée est défini par le texte lui-même : garde 11
  (l. 334-335 : « une entrée est en échec si l'un de ses calculs l'est ») et en-tête de la liste d'arrêt (l. 306-308).
  Code :
  - `_Entree.calcul`, l. 952-966 : une `GardeArret` levée dans un calcul est prise là (motif écrit, `echecs`, None) ;
  - `_Entree.sortie`, l. 995-997 : l'entrée est « échec » dès qu'un de ses calculs l'est ;
  - `_executer_entree`, l. 1755-1770 : les contrôles « (entrée entière) » ne sont écrits que dans la branche `except`,
    donc pour une `GardeArret` levée hors d'un calcul ;
  - `synthese`, l. 1815-1816 : la garde 11 compte toute entrée à l'état « échec ».
- **Problème** : la phrase neuve dit : « Une entrée qui tombe en échec garde les contrôles déjà faits […]. Chaque cible
  visée par l'analyse reçoit en plus un contrôle « non lu » (entrée entière), même si ses contrôles ont tous été faits ».
  Avec la définition de la garde 11, la phrase vise aussi une entrée dont un seul calcul a échoué. Dans ce cas, le module
  n'écrit aucun « non lu » d'entrée entière : il rend « non lu » le seul contrôle qui dépend du calcul. À la lettre du
  texte scellé, la sortie aurait donc des réserves en moins, le sens même que la parenthèse exclut. Un auditeur pourrait
  y lire un écart au préenregistrement scellé, qui est un nœud de Lazar. Le verdict R13 pourrait aussi ajouter à tort
  « non contrôlée ». Ce chemin est plausible au réel : VF3-04 a vu A1 T4 tomber en échec à 14 tâches (22 tirages
  dégénérés sur 2 000). Le défaut vient de la correction : le brouillon 6 ne l'avait pas (« seuls les contrôles non
  faits deviennent « non lus » »). VF3-01 proposait l'incise « hors d'un calcul », qui n'a pas été reprise.
- **Reproduit** (`essais_b7.py p17`, `essai-p17.log`). Scénario `_sc_sain` des tests, 60 tirages, 13 conclusions
  établies.
  - (a) `GardeArret` simulée dans le seul calcul T4 de A1 : l'entrée est « échec » et `calculs_en_echec` vaut ["T4"]. Le
    contrôle T4 est « non lu ». **Aucun** contrôle « A1 (entrée entière) » n'est écrit. La synthèse compte l'entrée en
    échec (garde 11) et ne rend qu'une réserve, `reserve_A1_non_lue` sur T4. La lettre du brouillon 7 en demanderait cinq
    (P3-P3, P3-P4, T3, T1 et T4).
  - (b) `GardeArret` hors d'un calcul (permutation du placebo) : cinq contrôles « A1 (entrée entière) », comme le décrit
    le brouillon 7.
- **Correction** (texte seulement ; le module ne change pas) : « 17. Une entrée qu'une `GardeArret` levée hors d'un
  calcul fait tomber en échec (entrée entière) garde les contrôles déjà faits, réserves contraires comprises ; l'addendum
  n'efface jamais une réserve qu'il a calculée. Chaque cible visée par l'analyse reçoit en plus un contrôle « non lu »
  (« <analyse> (entrée entière) »), même si ses contrôles ont tous été faits (sens prudent : une réserve en plus, jamais
  en moins). Un calcul en échec rend « non lu » le seul contrôle qui en dépend, sans contrôle d'entrée entière ;
  l'entrée compte alors comme en échec pour la garde 11. » Ajout facultatif, utile au verdict R13 : « ces « non lus »
  d'entrée entière comptent parmi les réserves possibles de l'audit de symétrie (VF2-03) ; une même conclusion peut alors
  être dite à la fois « non robuste » et « non contrôlée par l'addendum » ».
- **Suite** : appliqué dans le brouillon 8, avec l'ajout facultatif (partie B).

### VB7-02 — mineur — « Contre-lecture 4 » : « relu face à ce texte », sans l'empreinte du brouillon relu

- **Où** : brouillon 7, l. 460. La phrase n'a pas changé depuis le brouillon 6, mais elle devient fausse dans le
  brouillon 7.
- **Problème** : les trois vérificateurs ont relu le module face au brouillon 6 (`411eb334…`, tableaux « Ce qui a été
  lu » de VF1, VF2 et VF3), pas face à « ce texte », c'est-à-dire le brouillon 7 rempli. L'entrée ne cite pas non plus
  l'empreinte du brouillon relu. Une fois remplie, elle porte quatre empreintes (module et trois rapports), aucune de
  brouillon. Le validateur passe, puisqu'il demande deux empreintes au moins. Mais pour R2, `prereg.py` (l. 3-7) demande
  « l'empreinte du brouillon relu ». Celle du brouillon 6 n'apparaît qu'à l'entrée 5.
- **Reproduit** : `entrees-contre-lecture.log`, sur le texte rempli de valeurs factices : « entrée 4 : 4 empreintes
  distinctes ; brouillon 6 (411eb334) cité : False ; « face à ce texte » : True ».
- **Correction** (texte) : « module final (sha256 `<<EMPREINTE_MODULE>>`) relu face au brouillon 6 (sha256
  `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a`) par trois sous-agents neufs ».
- **Suite** : appliqué dans le brouillon 8 ; l'entrée 4 remplie porte cinq empreintes (partie B).

### VB7-03 — mineur (procédure) — corrections après cette relecture : nom du brouillon, empreinte citée, outils

- **Où** : brouillon 7, entrée « Contre-lecture 5 » (l. 469-473) ; `remplir_texte_final_v1.py`, l. 21 et 34 ;
  `verser_addendum_v1.sh`, l. 28 (état de la partie A).
- **Problème** : VB7-01 et VB7-02 demandent de changer le texte. Or le remplisseur lisait le fichier nommé
  « brouillon7 » et calculait `<<EMPREINTE_BROUILLON7>>` au moment du remplissage. Si le brouillon 7 avait été corrigé en
  place, deux règles auraient été violées :
  - R2 : l'entrée 5 aurait cité comme relue une empreinte que personne n'avait relue ;
  - R12 : une version aurait été écrasée.

  Le versement ne copiait que les brouillons 1 à 7. Les tests de `final-b4/` avaient déjà été réécrits en place
  (`7605c205…` → `7387910d…`, à 07:20:40).
- **Reproduit** : lecture des deux outils (lignes citées) ; `stat` et `sha256sum` du fichier de tests.
- **Correction** :
  - écrire les corrections dans un brouillon 8, sous un nouveau nom ;
  - citer à l'entrée 5 le brouillon 7 relu (`c3e9c27f…`), puis le brouillon 8 ;
  - adapter le remplisseur et le versement ;
  - garder une copie nommée de chaque version relue des tests ;
  - soumettre le brouillon 8 et les tests à la partie B.
- **Suite** : tout est fait (partie B, (B1) et (B4)).

### VB7-04 — information — précision 12 : `<jeu>` écrit en mots ; portée de « Tirages comme `intervalle_blocs` »

- **Où** : brouillon 7, l. 396-402 ; module, l. 129 et 1908.
- **Problème** :
  - La liste fermée écrit les objets de A1 en identifiants (`saboteur-honnete`…), mais le `<jeu>` de A7 en mots
    (« saboteur contre honnête, contre témoin et contre mention »). Les clés réelles sont `saboteur-honnete`,
    `saboteur-temoin` et `saboteur-mention` (`CIBLES_A7`). Je les ai déduites par analogie. Avec elles, les 69 clés du
    texte égalent celles du module et celles du manifeste.
  - « Tirages comme `intervalle_blocs` » vaut pour les tirages du module (A1, A2 (b), A3, A4 (a) et (b)). Les fonctions
    gelées tirent à leur façon. Par exemple, `effet_cout_apparie` (A6) tire en un seul appel,
    `rng.integers(0, d, size=(10 000, d))`, sur les tâches lisibles triées (`statistiques.py` l. 59-72).
  - Aucun nombre n'en dépend : le module, cité par son empreinte, fixe tout.
- **Reproduit** : `essais-rapides.log` (« <jeu> tel qu'écrit », « jeux de A7 dans le module ») ; lecture du code gelé.
- **Correction** (facultative) : « `<jeu>` parmi `saboteur-honnete`, `saboteur-temoin`, `saboteur-mention` » ;
  « Tirages propres au module comme `intervalle_blocs` ».
- **Suite** : appliqué dans le brouillon 8.

### VB7-05 — information — garde 15 : le code dépasse un peu la lettre, dans un sens ou dans l'autre, sans effet

- **Où** : module, l. 75, 2006-2009 et 243-249.
- **Problème** :
  - (i) L'expression `^…-addendum-p3$` accepte aussi le nom suivi d'un saut de ligne : en Python, `$` admet un `\n`
    final. `creer_manifeste` l'accepte aussi.
  - (ii) Le préenregistrement est comparé comme une chaîne : `./prereg/…` est refusé, alors qu'il désigne ce texte.
    C'est la forme exacte du plan, point 2.
  - (iii) Des messages « garde 15 » (`verifier_parametres_tirage`) sont levés dans des calculs, après le manifeste. Ils
    donneraient un « échec », pas un arrêt. Ils ne peuvent pas se déclencher une fois `exiger_parametres_du_texte`
    passée.

  Aucun de ces cas ne permet un second passage ni une promotion.
- **Reproduit** : `essais-rapides.log`, section garde 15.
- **Correction** : aucune avant le scellement (module figé). Au plus : « hors de la forme exacte de la commande du plan,
  point 2 ».
- **Suite** : (ii) écrit dans le brouillon 8 ; (i) et (iii) notés au traitement.

### VB7-06 — information — en-tête : date et auteur restés au stade des premiers brouillons

- **Où** : brouillon 7, l. 3-10 (inchangées).
- **Problème** :
  - « Date (UTC) : 2026-10-19 » précède des faits que le texte cite : la requête 007 et les contre-lectures 4 et 5,
    toutes du 2026-10-20.
  - « Auteur : … les deux contre-lectures et la relecture externe du brouillon 2 » : il y a cinq contre-lectures et
    quatre requêtes à Gemini.

  L'antériorité se prouve par le commit de scellement (garde 3), pas par cette ligne.
- **Reproduit** : lecture de l'en-tête et de la section « Contre-lecture ».
- **Correction** (facultative) : « Date (UTC) : celle du commit de scellement, qui fait foi (rédaction du 2026-10-19 au
  2026-10-20) », comme P3 ; « … les contre-lectures et relectures de la section « Contre-lecture » ».
- **Suite** : appliqué dans le brouillon 8.

### VB7-07 — information — précision 1 et la fenêtre de VF1-11

- **Où** : précision 1 (l. 375-376) ; `executer`, l. 2228-2234.
- **Problème** : `reference`, dont `verifier(chemin_l)`, est construit après la création du manifeste, hors du `try` qui
  écrit l'arrêt. Un arrêt à cet endroit laisserait un manifeste sans sortie, contre la lettre de la précision 1. Le
  traitement a noté VF1-11 sans changer le module : le cas est inatteignable, puisque le même fichier est vérifié à la
  l. 2216. La lettre du texte reste pourtant inexacte pour ce cas.
- **Reproduit** : lecture du code (l. 2216, 2224, 2228-2235) ; essai de VF1-11 (`texte/essais/vf/test_vf_texte_2.py`).
- **Correction** (facultative, texte) : ajouter à la précision 1 « sauf la relecture de l'empreinte de la lecture
  décisive, faite juste après la création du manifeste et hors de cette écriture (fichier vérifié juste avant) ».
- **Suite** : appliqué dans le brouillon 8.

## (1) Différentiel du brouillon 6 au brouillon 7 : chaque changement

| bloc | brouillon 7 | changement | source | ce que fait le module (lignes) | état |
|---|---|---|---|---|---|
| 1 | l. 1 | titre « v1, brouillon 6 » → « v1 » | VF1-08 | — | juste |
| 2 | l. 236 | plan 3 : « (sauf le contrôle des graines de la garde 15, voir cette garde) » | VF1-02 | `executer` l. 2209-2222 (gardes avant le manifeste), l. 2224 (manifeste), l. 2235 → `analyser_addendum` l. 1947 → `preparer_donnees` l. 1984 (`exiger_graines`) | juste |
| 3 | l. 271-278 | plan 9 : banc de CB3 sur le module `daf95459…`, non refait ; rapport et deux journaux avec chemins et empreintes | VF1-05 | journaux : 426,5 s ; A1 327,5 s ; A4 63,2 s ; 647 Mo ; 564 Mo ; données (2 400, 430). Le banc importe `final/` (`daf95459…`). Empreintes égales. Versement l. 21-24, 34 | juste |
| 4 | l. 308-309 | en-tête de la liste d'arrêt : « sauf le contrôle des graines de la garde 15 » | VF1-02 | comme le bloc 2 | juste |
| 5 | l. 337-338 | garde 12 : aire vectorisée du module (1e-12, test) et quantile 0,95 de `np.quantile` | VF1-04 | `exiger_coherence` l. 658, 663, 666 ; `TOLERANCE_COHERENCE` l. 98 ; test l. 562-586 | juste |
| 6 | l. 344-345 | garde 14 : ligne exactement vide ignorée ; ligne d'espaces illisible ; motif « garde 4 » | VF1-12, VF2-09 (règle des notes citée par VF2-04) | `charger_textes` l. 2176-2182 | juste (essai `g14`) |
| 7 | l. 346-347 | garde 15 : forme `…-addendum-p3` ; préenregistrement de la commande | VF1-07 | `RUN_ADDENDUM` l. 75 ; `exiger_commande` l. 2006-2009 | juste (nuances : VB7-05) |
| 8 | l. 349-350 | garde 15 : graines du manifeste, contrôlées juste après sa création ; arrêt écrit | VF1-02 | l. 2224, 2234-2241, 1947, 1984, 1912-1926 | juste (« au début des analyses » : au début de `preparer_donnees`, avant les gardes refaites et les analyses) |
| 9 | l. 363-364 | liste des tests : gardes 12 à 16 nommées | VF1-06 | tests relus : garde 12 l. 1149 ; 13 l. 1161 ; 14 l. 1003-1062 ; 15 l. 609, 877, 3156-3178, 3209-3214 ; 16 l. 3088 | juste ; R5 des règles neuves des gardes 14 et 15 : partie B |
| 10 | l. 385-386 | précision 8 | VF1-03 | `synthese` l. 1833-1834. Chaque cible établie est visée par A1 (l. 1024-1036), A2 (l. 1153-1164) ou A6 (l. 1471-1491), ou par un « non lu » d'entrée entière (l. 1766-1769) | juste (essai `p8`) |
| 11 | l. 392-402 | précision 12 : liste fermée ; conventions de tirage | VF3-02, VF3-03 | `cles_addendum` l. 1899-1909 (69 = 2 × 33 + 3) ; `_rng` l. 252-253 ; `_tirages` l. 264-272, égal à `intervalle_blocs` (`evaluation.py` l. 46-53) ; placebo l. 1038-1042 ; départs l. 1065 et 1069 | juste (VB7-04) |
| 12 | l. 408 | précision 15 : « pour les intervalles que calcule le module » | VF1-10 | l. 357 (A1, A4 (a), A4 (b)), l. 1109 (A2 (b)), l. 1219 (A3) | juste |
| 13 | l. 414-416 | précision 17 | VF1-01, VF2-03, VF3-01 | `_executer_entree` l. 1755-1770 | juste pour une garde levée hors d'un calcul ; **inexacte pour un calcul en échec : VB7-01** |
| 14 | l. 448, 450-452 | « le brouillon 3 » (deux fois) ; requêtes 006 et 007 | VF1-08 | traitement l. 62-73 et 100-108 | juste |
| 15 | l. 467-468 | contre-lecture 4 : « Constats traités dans le texte (brouillon 7) et dans les tests seulement… » | hors constat : décision du traitement (l. 110-116) | — | juste ; la phrase voisine « face à ce texte » : VB7-02 |
| 16 | l. 469-473 | entrée « Contre-lecture 5 » | hors constat : trace R2 de cette relecture | — | attendue ; procédure : VB7-03 |

S'y ajoutent 6 changements de blancs seuls : des lignes recoupées dans les blocs 3, 7, 12 et 13.

**Constats que le traitement accepte pour le texte** : tous sont appliqués (VF1-01 à VF1-08, VF1-10, VF1-12, VF2-03,
VF2-09, VF3-01 à VF3-03).
- VF1-09, VF2-08, VF3-05 : traitement seulement, aucun texte attendu.
- VF1-11, VF2-07, VF2-10, VF3-04, VF3-06 : notés.
- VF2-01, VF2-02, VF2-04, VF2-05, VF2-06 : tests (partie B).

**Changements sans constat** : seulement les blocs 15 et 16, qui sont attendus.

## (2) Vérifications ciblées

- **Précision 12, liste fermée.** 69 clés : 2 sondes × 33, plus 3 clés pour A6. Le texte développé égale
  `cles_addendum(P)`, qui égale les clés du manifeste (`manifeste.graines`), une à une. Le module lit chaque motif de
  clé (`essais-rapides.log`). Seul écart de forme : `<jeu>` est écrit en mots (VB7-04).
- **Conventions de tirage.**
  - `_tirages` (l. 264-272) : tâches dans l'ordre de `np.unique`, puis `rng.integers(0, u, size=u)` à chaque tirage.
    C'est la règle de `intervalle_blocs` (`evaluation.py` l. 46-53, `default_rng(int(graine))`) et de
    `difference_aires_appariee`.
  - Générateurs : `_rng` vaut `default_rng(graine_entiere(…))` (l. 252-253). Les fonctions gelées reçoivent une graine
    entière et en font `default_rng(int(graine))`, une fois par appel : un générateur par clé (`detection_etiquettes`
    appelle `intervalle_blocs` une seule fois). A6 utilise `generateur(…)` (l. 1464).
  - Placebo : un seul générateur, qui sert d'abord à `lp._permuter_dans_les_taches` (une permutation par tâche,
    `lecture.py` l. 194-199), puis aux tirages (l. 1038-1042).
  - A2 (b) : actions dans l'ordre de `rang` (l. 1059). Départs du pré-coût : `rng.integers(0, c − L + 1, size=50)`
    (l. 1065). Puis, si `L_cout > c`, départs du coût : `rng.integers(c, fin − L + 1, size=50)` (l. 1069). Conforme.
- **Précision 17.** Le texte est conforme pour une `GardeArret` levée hors d'un calcul :
  - les contrôles déjà faits sont gardés, réserves comprises (l. 1762) ;
  - chaque cible de `VISEES` reçoit un « non lu » (l. 1766-1769), ou « sans objet » si elle n'est pas établie.

  Il ne l'est pas pour un calcul en échec : VB7-01.
- **Garde 15.**
  - Nom : `^[0-9]{8}-[0-9]{6}-addendum-p3$` (l. 75). `…-addendum-p3-bis` et `…-autre` sont refusés.
  - Préenregistrement : égalité de chaîne (l. 2008).
  - Ces deux contrôles passent avant toute lecture : c'est le premier appel de `executer` (l. 2209).
  - Graines : ce sont celles du manifeste (l. 2235). `exiger_graines` (l. 1984) les contrôle après `creer_manifeste`
    (l. 2224), dans le `try` qui écrit l'arrêt (l. 2234-2241).

  Conforme ; nuances en VB7-05.
- **Garde 14.**
  - Découpe sur `b"\n"` (l. 2176). Une ligne de zéro octet est ignorée (l. 2177).
  - Ligne d'espaces, de tabulation, ou faite d'un seul retour chariot : arrêt « garde 4 : fichier … : ligne N illisible
    (JSONDecodeError) », sans texte (l. 2182). Octet UTF-8 invalide : même arrêt (UnicodeDecodeError).
  - U+2028 reste dans le texte.

  Conforme (`essais-rapides.log`).
- **Plan, point 9.**
  - Les empreintes citées égalent les fichiers : rapport CB3 `8aa42a89…`, `essai_07.log` `063661ac…`,
    `essai_07b_import.log` `baaf517e…`.
  - Les chiffres égalent les journaux : 426,5 s ; A1 327,5 s ; A4 63,2 s ; 647 Mo pour « environ 650 » ; 564 Mo pour
    « 560 » ; 2 400 actions × 430 sondes ; 2 000 et 10 000 tirages.
  - Module mesuré : celui de `final/` (`daf95459…`), d'après le `sys.path` du script du banc. Le rapport CB3 versé le
    nomme (l. 13).
  - Le versement copie le rapport et les deux journaux aux chemins cités, puis les scelle (`verser_addendum_v1.sh`
    l. 21-23 et 34).

  Conforme.
- **Précision 8, garde 12, précision 15** : voir la table (1).

## (3) Reste du texte, validateur, outils

- **Le reste du texte est inchangé.** Le différentiel strict par jetons, blancs compris, compte 54 changements de mots,
  tous dans les 16 blocs, et 6 changements de blancs seuls (recoupes de lignes). Les espaces insécables et fines (U+00A0,
  U+2009, U+202F, dont l'expression de A6, l. 167) sont en même nombre. Il n'y a aucun retour chariot, aucune
  tabulation, aucun blanc en fin de ligne. Le fichier finit par un saut de ligne.
- **Validateur.** Commande : `cd /home/user/controle-ia-travail && PYTHONPATH=src …/venv-gpu-neuf/bin/python -B -c
  "from controle_ia.prereg import problemes; print(problemes('…/b7/copie/brouillon7-copie.md'))"` (copie `c3e9c27f…`).
  Il rend trois problèmes :
  - « contre-lecture 4 sans ses deux empreintes » ;
  - « contre-lecture 5 sans ses deux empreintes » ;
  - « marqueurs de gabarit restants » : les 13 marqueurs.

  Les trois viennent des marqueurs : les entrées 4 et 5 n'ont encore que des marqueurs à la place de leurs empreintes.
  Une fois rempli de valeurs factices bien formées, le texte rend `[]`.
- **Expressions lues par les gardes** (module, tests, commit, entropie) : une seule correspondance chacune, dans
  l'en-tête (l. 11-14). La mention « tests corrigés (sha256 …) » de l'entrée 5 ne répond pas à l'expression des tests.
- **Outils de la session (état de la partie A).**
  - Le remplisseur couvrait les 13 marqueurs, dont les trois neufs (`EMPREINTE_BROUILLON7`, `EMPREINTE_VERIFICATION_B7`,
    `VERDICT_VERIFICATION_B7`). Il s'arrêtait sur un marqueur absent ou restant, et n'écrasait rien.
  - Le versement copie ce rapport au chemin que cite l'entrée 5.

  Réserve de procédure : VB7-03.

## Fichiers de la partie A (sous `verification-finale/b7/`)

| fichier | sha256 |
|---|---|
| `diff_strict.py` | `f4db28960b1854da887afbe67a13bc7b6aa841be1f290de56637d96f85ccbc84` |
| `essais_b7.py` | `2066f549befa8dcf8d2158f07a47b11c750dd1535ffa594dcb2f092d307e69f0` |
| `diff-mots-b6-b7.txt` | `28220ddf3c95e47ad5d9129d35ecb048f03ab02546fca9973b0a128be5480f98` |
| `diff-lignes-b6-b7.txt` | `dc3cb5f0388a658f52a1dd6b919443473566d6c2f06be7054d1511c0602efc52` |
| `diff-strict-b6-b7.log` | `956174987de029eb66c94f1255a6c7c7f19aebd886d763ca54a8d6ff177ddd1c` |
| `essais-rapides.log` | `a251f3a06bf32f8c575ecef57f281b5eb76cd92c36f6a54d451354533f745fda` |
| `essai-p17.log` | `99232e2fd5860b103a178538b51549d862bdbfb9aa0438ab36bdfd9fe2b09283` |
| `essai-p8.log` | `bcad2a1918de4392c566171ecf4b8499c9a8f2619893732be6e0bddf786d6873` |
| `validateur.log` | `2b3990ade386eae99c56f34b9fd9d6a86e83e35730abd3a45841ec6d4d22b74d` |
| `entrees-contre-lecture.log` | `076ec4592140426559d9e33a865df93f6e403064491f55edb993366920ac62cf` |
| `empreintes-au-debut.txt` | `6c27185419a17d2346abf5d5f9473b36e20cfe76853f265e5c974414e5f719e1` |
| `rapport-partie-A-08139fdd.md` (état de ce rapport à la fin de la partie A) | `08139fdd11728f7accb6c01506a334a9ba12fd7f9288d8b98bdfffcf8f5e6388` |
| `copie/brouillon7-copie.md`, `copie/complements_p3_v1.py`, `copie/test_complements_p3_v1.py` | égales aux originaux relus : `c3e9c27f…`, `2b16179d…`, `7605c205…` |

# Partie B — brouillon 8 et tests corrigés

**Verdict de la partie B : scellable.**

## Ce qui a été lu (avec empreintes)

| fichier | sha256 | lecture |
|---|---|---|
| brouillon 8 `P3-addendum-lecture-complementaire-v1-brouillon8.md` | `bde1b2437c0caa24cd6feabe959351e3fb1342973dc2338f01271aa2d5479484` | différentiel strict avec le brouillon 7 ; passages changés en contexte |
| brouillon 7 (intact) | `c3e9c27f3da2eb3270a8b52b24e9533734a640bb6453f2bca463fad766bb0c28` | référence du différentiel |
| tests corrigés `final-b4/test_complements_p3_v1.py` | `7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3` | différentiel complet avec `7605c205…` ; six tests retouchés en entier ; aides `_cas`, `_source_lecture`, `_lecture_recalculee` |
| tests relus par la vérification finale `versions-tests/test_complements_p3_v1-7605c205.py` | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` | référence du différentiel |
| module `final-b4/complements_p3_v1.py` (inchangé) | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` | relu en partie A |
| traitement `traitement-R2-addendum-P3-v1.md` | `bdfc689f7483ceae66f7f0bc0212900fa7abb3aba4558e4be18e80d7add90bbf` | section « Contre-lecture 5, partie A » |
| notes du correcteur `final-b4/NOTES-CORRECTIONS-CB1.md` | `b48b80286247eb7dbf5fa9675e0a0d96d83bfd033398231ded841377f3ad938e` | § 3 ter |
| remplisseur `remplir_texte_final_v1.py` (adapté) | `ca7b93c3b6079fff3bcc9c26a557e52ee11c7edae73837bf528df974f888b724` | en entier (non exécuté) |
| versement `verser_addendum_v1.sh` (adapté) | `1f89978ab1b20b09c2c118f2a826871d4e0dbc6ba93f55d02340f0dc52dd123a` | en entier (non exécuté) |
| lanceur de VF2 `verification-finale/mutants/lanceur_vf2.py` | `76aa1ea5760427990193e06bbf7e955b8bbe977d4c63093da1f6929c409dcb52` | substitutions et tests tueurs de M09 à M14, M19, M24 |
| journaux du correcteur `final-b4/essais/pytest-final-vf2.log`, `mutants-vf2-resultats.jsonl`, `empreintes-au-lancement-vf2.txt` | `60a54c35c368e22f0a56439ba86125422e462c363889448f23f3b78b8bf8744e`, `3f629b234abe7661dfde91254e2592cb3ce0a235ee970d4ce112ae3686e5c4e9`, `4986b5690c8607f09dac5dedbc7b345020a2c095c772a50db26fb25789752b79` | en entier |

## Ce qui a été lancé

| quoi | résultat | journal (sous `b7/partie-b/`) |
|---|---|---|
| différentiel strict du brouillon 7 au brouillon 8 (`../diff_strict.py`) | 26 changements de mots, 8 recoupes de lignes ; caractères spéciaux et fins de ligne inchangés | `diff-strict-b7-b8.log` |
| différentiel des tests, `7605c205…` → `7387910d…` | 10 blocs, tous dans six tests ; 11 lignes retirées, 42 ajoutées | `diff-tests-7605-7387.txt` |
| collecte des tests (`--collect-only`, rien d'exécuté) | **165 tests collectés** ; 117 fonctions de test dans les deux versions | `collecte.log` |
| six tests retouchés, module réel, copie `base/` | **6 passed in 77.79s** | `temoin-six-tests.log` |
| huit mutants (substitutions du lanceur de VF2, motif présent une seule fois), test tueur seul, `-x` | **8 tués sur 8** | `mutants-b-resultats.jsonl`, `mutants-b-run.log`, `m/<id>/pytest-tueur.log` |
| second passage avec les variables locales (`-l`), six mutants à boucle partagée | artefact tueur identifié | `mutants-b-locaux.log`, `m/<id>/pytest-locaux.log` |
| ancienne version du test de la garde 7 (`7605c205…`) sous M09 et sous M12 | **passe** (1 passed, code 0) : les artefacts anciens tiennent sous ces mutants | `m/M09-ancien/pytest-ancien.log`, `m/M12-ancien/pytest-ancien.log` |
| validateur et marqueurs, sur une copie du brouillon 8 | marqueurs attendus seulement ; 13 marqueurs = 13 clés du remplisseur ; rempli de valeurs factices : `[]` | `validateur-b8.log`, `marqueurs-b8.log` |

Je n'ai relancé ni la suite complète (lancée par le correcteur, sur les mêmes empreintes : `essais/empreintes-au-lancement-vf2.txt`, « 165 passed in 1049.77s »), ni le remplisseur, ni le versement.

## Constats de la partie B (le plus grave d'abord)

Aucun bloquant, aucun majeur, aucun mineur. Deux constats pour information, sans correction exigée avant le scellement.

### VB7-08 — information — précision 17 du brouillon 8 : « le seul contrôle qui en dépend » est au singulier

- **Où** : brouillon 8, précision 17 (l. 418-419). Cette formule est la mienne (correction proposée en VB7-01).
- **Problème** : un calcul en échec rend « non lu » les contrôles qui en dépendent. Leur nombre varie :
  - zéro pour un calcul descriptif (placebo de A1, l. 1041 ; fenêtre juste avant de A2 (c), l. 1145 ; A9) ;
  - deux pour certains calculs : `contrastes` de A3 (l. 1235-1236) ; `jetons_dominants` de A8 pour une sonde à
    attention (l. 1681-1684) ; relecture des textes pour A5 (l. 1377-1378).

  Le sens (seuls les contrôles qui en dépendent, rien d'autre) est clair. L'écart ne joue que dans le sens prudent.
- **Reproduit** : lecture du code (lignes citées).
- **Correction** : aucune exigée. Si le texte devait encore changer : « rend « non lu » les seuls contrôles qui en
  dépendent (aucun pour un calcul descriptif) ».

### VB7-09 — information — le remplisseur ne compare pas les empreintes qu'il lit aux empreintes relues

- **Où** : `remplir_texte_final_v1.py`, l. 24-36.
- **Problème** : le remplisseur calcule chaque empreinte sur le fichier tel qu'il est au moment du remplissage. Il le
  fait pour le brouillon 8, les tests, le module, le traitement et ce rapport. `NOMBRE_TESTS` est passé à la main. Si
  l'un de ces fichiers changeait après cette relecture, le texte scellé citerait une version non relue (R2), sans arrêt.
  Le versement ne le verrait pas non plus : il compare le texte aux fichiers versés, pas aux empreintes relues.
- **Reproduit** : lecture de l'outil (lignes citées).
- **Correction** (recommandée, outil seulement ; le texte ne change pas) :
  - ajouter au remplisseur des assertions sur les empreintes relues : brouillon 8 `bde1b243…`, tests `7387910d…`,
    module `2b16179d…` ;
  - exiger `NOMBRE_TESTS` = 165 ;
  - achever le traitement et ce rapport avant le remplissage, puisque leurs empreintes sont lues à ce moment.

## (B1) Différentiel du brouillon 7 au brouillon 8 : chaque changement

| brouillon 8 | changement | constat | ce que fait le module (lignes) | état |
|---|---|---|---|---|
| l. 8-9 | auteur : « … les contre-lectures et relectures de la section « Contre-lecture » » | VB7-06 | — | juste |
| l. 10 | « Date (UTC) : celle du commit de scellement, qui fait foi (rédaction du 2026-10-19 au 2026-10-20) » | VB7-06 | aucune garde ne lit cette ligne ; antériorité par la garde 3 (l. 2138-2161) | juste |
| l. 347 | garde 15 : « (forme exacte du plan, point 2) » | VB7-05 (ii) | `exiger_commande` l. 2008-2009 : égalité de chaîne avec `prereg/P3-addendum-lecture-complementaire-v1.md`, la forme du plan, point 2 | juste |
| l. 375-377 | précision 1 : exception de la relecture de l'empreinte de la lecture décisive | VB7-07 | `executer` l. 2216 (lecture vérifiée), 2224 (manifeste), 2231 (`verifier(chemin_l)` dans `reference`, seul appel qui puisse lever), 2234 (`try`) | juste |
| l. 397-398 | `<jeu>` parmi `saboteur-honnete`, `saboteur-temoin`, `saboteur-mention` | VB7-04 | `CIBLES_A7` l. 129 ; `cles_addendum` l. 1908 | juste (69 clés égales, essai `cles` de la partie A) |
| l. 400 | « Tirages propres au module comme `intervalle_blocs` » | VB7-04 | `_tirages` l. 264-272 | juste |
| l. 415-421 | précision 17 réécrite : garde levée hors d'un calcul ; calcul en échec ; effet sur l'audit ; double mention au verdict | VB7-01 (avec l'ajout facultatif) | `_Entree.calcul` l. 952-966 ; `sortie` l. 995-997 ; `_executer_entree` l. 1755-1770 (libellé « <analyse> (entrée entière) », l. 1769) ; `synthese` l. 1815-1816 (garde 11), 1828 (réserves possibles), 1853-1862 (deux listes) | juste (nombre : VB7-08) |
| l. 465-466 | contre-lecture 4 : « relu face au brouillon 6 (sha256 `411eb334…`) » | VB7-02 | — | juste ; entrée 4 remplie : 5 empreintes |
| l. 475-480 | contre-lecture 5 : brouillon 7 relu (`c3e9c27f…`, partie A), puis brouillon 8 (`<<EMPREINTE_BROUILLON8>>`) et tests (partie B), « un même sous-agent neuf » | VB7-03 | — | juste ; entrée 5 remplie : 4 empreintes |

- Les 26 changements de mots relèvent tous de ces neuf lignes. Les 8 changements de blancs seuls sont des recoupes. Rien
  d'autre n'a changé.
- Constats appliqués : VB7-01, VB7-02, VB7-04, VB7-06, VB7-07 en entier, et VB7-05 (ii). VB7-05 (i) et (iii) sont notés
  au traitement, ce qui est attendu puisque le module est figé. VB7-03 est appliqué dans les outils et à l'entrée 5.
- Validateur sur une copie du brouillon 8 (`bde1b243…`) : trois problèmes, tous dus aux marqueurs (entrées 4 et 5,
  13 marqueurs restants). Une fois rempli de valeurs factices, le texte rend `[]`. Les expressions des gardes trouvent
  une seule correspondance chacune, aux l. 11-14 (`marqueurs-b8.log`).

## (B2) Différentiel des tests (`7605c205…` → `7387910d…`)

Six tests changent, tous les autres sont identiques :
- `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` ;
- `test_garde_coherence_de_la_lecture_avec_le_run_source` ;
- `test_garde_localisation_egale_a_celle_de_la_lecture` ;
- `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` ;
- `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` ;
- `test_forme_de_la_commande`.

| test | ajout | constat |
|---|---|---|
| garde 4 (l. 1035) | artefact « espaces » : ligne 3 faite de trois espaces, arrêt « garde 4 … ligne 3 illisible (JSONDecodeError) » | VF2-04 |
| garde 12 (l. 1151) | cas sain, écart de 1e-12 (`exiger_coherence`, 10 contrôles) ; artefact, écart de 1e-6 : arrêt (garde 12) ; docstring | VF2-05 |
| garde 13 (l. 1171) | artefact, écart de 2e-9 sur le pré-coût : arrêt (garde 13) | VF2-05 |
| organisme non établi (l. 1497) | seconde partie : `conforme` posé contre les états (sa valeur lue est d'abord vérifiée égale aux états), issue recalculée ; addendum sans arrêt, conclusions vides, « réserves sans objet » | VF2-02 |
| garde 7 (l. 1766) | trois artefacts : témoin contre honnête « au-dessus » ; saboteur contre mention « non au-dessus » ; borne basse de T2 égale à 0 | VF2-01 |
| forme de la commande (l. 3185) | artefact « 20261020-130000-addendum-p3-bis » | VF2-06 |

- **Rien de retiré ni d'affaibli.** Les 11 lignes retirées se répartissent ainsi :
  - 7 lignes de docstring ;
  - 4 lignes de tuple d'artefacts, réécrites à l'identique pour y ajouter une entrée. L'entrée « non-utf8 » de la
    garde 4, les écarts (« pre », 1e-6), (« cout », −1e-6) et (« lignes », 1) de la garde 13, et l'entrée P3-P1
    « calculable » de la garde 7 restent, octet pour octet.

  Les artefacts neufs sont placés après les anciens, dans les mêmes boucles. Tous les motifs `match` anciens sont
  inchangés.
- **Comptes.** 165 tests collectés et 117 fonctions de test, dans les deux versions. Le nombre d'`assert` passe de 421 à
  426 et celui de `pytest.raises` de 97 à 98. Les paramétrisations sont inchangées (3). L'en-tête dit toujours 165.
- **Pas de contamination entre tests.** La seconde partie neuve du test « organisme non établi » modifie la lecture
  rendue par `_cas("a6_verrou")`. Mais `_cas` rend une copie profonde (l. 504-512) : le cache n'est pas touché.
- **Mutants tués avant la retouche.** Aucun des 51 mutants de CB2 n'a son test tueur parmi les six tests retouchés
  (table de VF2). Les mutants neufs de VF2 que ces tests tuaient (M07, M08, M18, M20, M38) le restent : chaque test
  retouché contient toutes ses vérifications anciennes, dans le même ordre, et ses vérifications neuves passent sur le
  module réel.

## (B3) Six tests sur le module réel, huit mutants

- **Témoin.** Copie `base/` : module `2b16179d…` et tests `7387910d…`, empreintes vérifiées. Les six tests retouchés
  passent : **6 passed in 77.79s**.
- **Mutants.** Substitutions recopiées du lanceur de VF2 (`NEUFS`). Chaque motif est présent une seule fois. Chaque copie
  mutée est faite dans `m/<id>/`, avec les tests `7387910d…`. Chaque test tueur est lancé seul, par son identifiant
  exact, avec `-x`, deux processus au plus.

| mutant | règle mutée | test tueur | résultat | artefact qui tue |
|---|---|---|---|---|
| M09 | `conforme` recoupé sans « témoin contre honnête non au-dessus » | garde 7 | **tué** (1 failed, 44 s), DID NOT RAISE, l. 1803 | l'artefact neuf (témoin contre honnête « au-dessus »). Le motif est commun avec un artefact ancien, mais l'ancien test passe sous M09 (1 passed) |
| M10 | T3 recoupé sans « saboteur contre mention au-dessus » | garde 7 | **tué** (1 failed, 46 s), DID NOT RAISE, l. 1803 | `motif` = « intention/.*/T3/etabli vaut True … », propre à l'artefact neuf |
| M11 | `conforme` recoupé même si P3-P3 n'est pas établie | organisme non établi | **tué** (1 failed, 30 s) : arrêt à l. 1521, dans la seconde partie neuve (« garde 7 : P3-P4/tromperie-lineaire-c7/conforme vaut False alors que les états de la lecture disent True … ») | le cas sain neuf |
| M12 | T1, T2, T4 recoupés avec `bas ≥ seuil` au lieu de `bas > seuil` | garde 7 | **tué** (1 failed, 29 s), DID NOT RAISE, l. 1803 | l'artefact neuf (borne basse de T2 égale à 0). Le motif est commun avec l'artefact −0,01, mais l'ancien test passe sous M12 (1 passed) |
| M13 | garde 12 à 1e-3 au lieu de 1e-9 | garde 12 | **tué** (1 failed, 40 s), DID NOT RAISE, l. 1164 | l'artefact neuf, écart de 1e-6 (ligne neuve) |
| M14 | garde 13 à 1e-7 au lieu de 1e-9 | garde 13 | **tué** (1 failed, 25 s), DID NOT RAISE, l. 1192 | `cle` = « pre », `ecart` = 2e-09 : l'artefact neuf |
| M19 | ligne d'espaces ignorée | garde 4 | **tué** (1 failed, 7 s), DID NOT RAISE, l. 1059 | `nom` = « espaces », `ligne` = b'   ' : l'artefact neuf |
| M24 | nom du run sans ancre de fin | forme de la commande | **tué** (1 failed, 6 s), DID NOT RAISE, l. 3193 | `run_add` = « 20261020-130000-addendum-p3-bis » : l'artefact neuf |

**8 tués sur 8**, chacun par l'artefact ou le cas sain neuf qui le visait. Les empreintes des modules mutés sont dans
`mutants-b-resultats.jsonl`. Mes résultats rejoignent ceux du correcteur (`essais/mutants-vf2-resultats.jsonl`) et de
ses variables locales.

## (B4) Outils adaptés (lecture seule, non exécutés)

- **Remplisseur.**
  - Il lit le brouillon 8 (l. 21) et calcule `EMPREINTE_BROUILLON8` sur ce même fichier (l. 34).
  - L'empreinte du brouillon 7 relu (`c3e9c27f…`) est écrite en clair dans le brouillon 8.
  - Ses 13 clés égalent les 13 marqueurs du brouillon 8 (`marqueurs-b8.log`).
  - Il s'arrête sur un marqueur absent ou restant et n'écrase pas `…-final.md`.
  - Les verdicts de VF1 à VF3 (« scellable après corrections ») sont ceux des rapports.

  Recommandation : VB7-09.
- **Versement.**
  - Il copie les brouillons 1 à 8 (l. 30).
  - Il copie les versions relues gardées sous noms versionnés (`versions-tests/` : tests `7605c205…`, tests `01b5faea…`,
    module `daf95459…`) dans `prereg/contre-lectures/versions-relues-addendum-P3-v1/`, puis les scelle (l. 27-28, 38).
  - Il copie et scelle ce rapport, les trois rapports de VF, le traitement, les notes, la table des mutants (présente sur
    disque : `final-b4/essais/table-mutants.md`), le rapport CB3 et ses deux journaux.
  - Les contrôles de fin sont inchangés : empreintes du module et des tests citées, égales aux fichiers versés ;
    `verifier-arbre`.

  Rien à redire, hors VB7-09.

## Fichiers de la partie B (sous `verification-finale/b7/partie-b/`)

| fichier | sha256 |
|---|---|
| `lanceur_b.py` | `099c8425e8ad1358c823bb70c5220aa946693aaeb3de9fb1cdb14f33426beee5` |
| `locaux_b.py` | `7524d27ced49758f53fecc514c2e425e46f78fa6d547021b5e3bac89ae9f938f` |
| `diff-strict-b7-b8.log` | `6fa6bf0079fda276c1e1116a264f4076deb6c7ec4a6c4a17d643d4b496983459` |
| `diff-tests-7605-7387.txt` | `d75addddc34b1c720658dc25c86124d98c1d9e47fbfbf62351fa67350e6aef63` |
| `collecte.log` | `7b8f42c64494fedd538e9fd2cd5071a9443b97f4f1a574558c014cc6e06e9f27` |
| `temoin-six-tests.log` | `f53eadc6adf9a3d036f8fa706852d87ca7ccf4736b2841857a095350298b0359` |
| `mutants-b-resultats.jsonl` | `b06ba8f8858c5555c48c0c8873ef645d7111ccc2cc4d8cdfe2834c0e6bfae948` |
| `mutants-b-run.log` | `f4b4410de232b820215f4ea50d5ed82ca53554bf5688f894118ebabc074b0845` |
| `mutants-b-locaux.log` | `65c9f1df368c19f92cabcec048f4e28c833196fad97c681b941ec1f925d59d4f` |
| `m/M09-ancien/pytest-ancien.log`, `m/M12-ancien/pytest-ancien.log` | `1bfaccee4397aa61e857dae797cae4707ae07a173324269b2377bd0b9c6a6097`, `20995c37757e855c572752e649a3c4d15451d8cea71fec790a12ded0df379c61` |
| `validateur-b8.log`, `marqueurs-b8.log` | `c296f96471b03c9cca6a03825f01fa339333eb4ba17dba6df4babb866269eb21`, `ed41b93979d4c6dacb920c9766b8b79837f648786b969771c126c2351275e54c` |
| `empreintes-au-debut-b.txt` | `c83774e6cd7245d3241cfc00ca5dbe8fd6968aca9576aa2f2304e9b77e506142` |
| `brouillon8-copie.md`, `base/complements_p3_v1.py`, `base/test_complements_p3_v1.py` | égales aux originaux : `bde1b243…`, `2b16179d…`, `7387910d…` |
