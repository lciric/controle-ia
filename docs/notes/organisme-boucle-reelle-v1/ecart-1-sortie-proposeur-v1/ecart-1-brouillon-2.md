# Écart 1 au texte scellé de la course réelle de l'organisme — sortie du proposeur — brouillon 2 (option 2 ; non scellé, non contre-lu)

**Statut : brouillon 2, non scellé, non contre-lu (R2 à faire par un sous-agent neuf).** Le brouillon 1
(`ecart-1-brouillon-1.md`, `6e18fc335d4d5833dfb2f78eb83a45fcf1deb1971f724cea521336806676e051`) reste intact ; il établit le motif, le
calcul de la borne, la réserve du délai de 1 800 s et les trois options. Ce brouillon 2 décrit **l'option 2, décidée par Lazar**
(R-2426, 12:26 UTC, verbatim : « Recommandation : option 2 : go ; Recommandation : (a), confiance 0,75 go ; ») et la ligne
**GO-2026-11-12-06** inscrite dans `registres/go.md` (`main`, commit `6b1d3124`).

- **Rédacteur et développeur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; même rédacteur que le brouillon 1. Aucun appel payant, aucune machine, aucune clé lue,
  rien écrit dans `registres/`.
- **Arbre de l'organisme** : `7e415cba` (code v66) reconstruit depuis `94bfd92` et les paquets v65 et v66, puis un commit
  neuf **`ab53b7f482df5149d9f672f40e04220dffb4173a`** (code v67), versé en paquet git `code-v67/organisme-v67-boucle-reelle-v1.bundle` (`8bfcd5936285da8bae2a57ff9e72c82950e21b370af01a7fcb90f8d018179cab`, prérequis
  `7e415cba`) et en patch `code-v67/organisme-v67-contre-7e415cb.patch` (`195e4e63b48025e14d31942f3c34c94bf6bb0d1b8b56e7c44b33ef2821e96c6b`).

## 1. Ce qui change, et cela seul

| pièce | changement | où |
|---|---|---|
| code v67 | `pole/adaptateur_commande_v67.py` (neuf) : `commandes_v67` = `commandes_v64` + `delai_s` de la configuration passé à l'adaptateur ; **garde 24** (`verifier_delais_v67`) : `fournisseurs.<nom>.delai_s` réel fini (nombre JSON, jamais un booléen ni une chaîne), > 0, ≤ 7 200 s ; `--delai-s` de la commande présent une seule fois, suivi d'une chaîne qui se lit en réel fini > 0, inférieur au délai de l'adaptateur d'au moins 30 s ; entrée d'un autre type ignorée | arbre de l'organisme |
| code v67 | `demonstrations/boucle_reelle_v67.py` (neuf, copie du lanceur v66) : `roles_reels_v67` (copie de `tour_ferme_v64.roles_reels`, `commandes_v67` au lieu de `commandes_v64`, refus de la garde 24 nommé, code 2) ; `verifier_configuration_v67` (v66 + garde 24, avec le contenu de la configuration, avant la garde 17) ; blocs `empreintes-du-code-v67` (99 fichiers) et `plan-gele-v67` (mêmes clés, mêmes contrôles) ; manifeste : `lanceur` et `configuration.delais_v67` ; préfixes et messages « v67 » | arbre de l'organisme |
| essais | `essais/test_boucle_reelle_v67.py` (neuf) : la suite du lanceur v66 rejouée contre le lanceur v67 (module d'essais v66 chargé une seconde fois, son `LANCEUR` remplacé ; trois essais remplacés : deux visaient `L64.roles_reels`, la fermeture part du lanceur v67) et les essais neufs (garde 24, `commandes_v67`, délai passé jusqu'à `Popen.communicate`, vraie commande locale tuée au délai de l'adaptateur, rôles réels v67, garde 24 au lanceur, blocs non interchangeables, exemple v8, manifeste) | arbre de l'organisme |
| banc | `essais/mutations_boucle_reelle_v67.py` (neuf) : le banc v66 chargé tel quel, ses 133 mutations portées (le lanceur v66 → sa copie v67 ; essais du fichier v67), et 18 mutations neuves | arbre de l'organisme |
| exemple | `exemples/configuration-boucle-reelle-v8.json` (neuf, octets égaux à la configuration v8 du dossier de course) | arbre de l'organisme |
| configuration v8 | v7 (`e45f3a71…`) + `fournisseurs.kimi.delai_s` 1 800 → 7 200, `--delai-s` de Kimi 1 750 → 7 150, `arrets.a3_delai_s.kimi` 1 800 → 7 200 (non lu sur le chemin de la course, relevé par cohérence) : **`eb6262890927bfc351bf2a32c21d0dcf121445256a5ebe6c4eaee70b9265b31d`** ; v7 elle-même = v6 + plafond de session 1,5 USD + borne 131 072 | `configuration-v8/` |
| relais Kimi | `--delai-amont-s 7200` et `--delai-silence-s 1800` (options existantes de `relais_kimi_v3.py`, défauts 1 800 et 600 s : une pause de plus de 10 minutes du flux de l'amont couperait l'appel, compté au pire cas) | texte v2, section 12.3, point 6 |
| Argon | **rien** : commande 1 750 s, adaptateur 1 800 s, relais lancé comme sous le v1 ; dit dans la configuration v8 (`_lisez_moi`) et le texte v2 | — |
| texte | `preenregistrement-boucle-reelle-organisme-v1-v2-brouillon1.md` (`fbdb14d32a26ab89cb2e4888f4a953ab27408023110afe7a59f1fae78ca2d024`) : le v1 à l'octet sauf l'en-tête, une section « Écart 1 », les sections 12.3, 12.4, 16 et, en 13, le paragraphe du GO et la ligne | ce dossier |

Ordre des délais sous la v8, pour un appel de Kimi : commande 7 150 s (code 6, coût compté au pire cas réservé, ligne `fin` au
registre) < adaptateur 7 200 s (groupe tué) = relais 7 200 s ; Argon inchangé (1 750 < 1 800). Au débit de la course 2
(≈ 30,1 jetons par seconde), 131 072 jetons demandent ≈ 4 360 s : la borne effective redevient la borne de jetons.

## 1 bis. Livraison du code et noms

- **Paquet git** : `code-v67/organisme-v67-boucle-reelle-v1.bundle` (`8bfcd5936285da8bae2a57ff9e72c82950e21b370af01a7fcb90f8d018179cab`),
  un commit, prérequis `7e415cbaaa3ff602db43a44dad6b4307c08352c7`. **Chaîne vérifiée depuis le dépôt distant** (clone neuf de
  `https://github.com/lciric/ideation-organism`) : `94bfd92` (public) → paquet v65 `organisme-v65-boucle-reelle-v2.bundle`
  (`4660197e…`, branche `prep/organisme-v65-v1` du dépôt de travail) → paquet v66 `code-v66/organisme-v66-boucle-reelle-v1.bundle`
  (`84ab119f…`, `main`) → paquet v67 (`git bundle verify` réussi), tête `ab53b7f4`, **497 fichiers suivis** (492 + 5) ; bloc
  `empreintes-du-code-v67` : **99 empreintes** (98 du v1 − lanceur v66 + lanceur v67 + `pole/adaptateur_commande_v67.py`).
  Patch : `code-v67/organisme-v67-contre-7e415cb.patch` (`195e4e63…`).
- **Noms** : le **lanceur** change de nom, `demonstrations/boucle_reelle_v67.py` (le v66 reste, intact, et refuse le texte v2) ;
  la **lecture** garde ses noms v66 (`demonstrations/lire_boucle_reelle_v66.py`, `pole/lecture_boucle_reelle_v66.py`), comme le
  cœur (`VERSION` « boucle-reelle-v66 », relevé `boucle-reelle-v66.json`). La règle de nom du texte est celle de la v66
  (`prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`, sans « brouillon ») : le texte v2 s'appellera
  `preenregistrement-boucle-reelle-organisme-v1-v2.md`. Options du lanceur : **aucune ajoutée ni retirée** (mêmes options que
  la v66) ; commande de la course : `demonstrations/boucle_reelle_v67.py`, `--preenregistrement …-v1-v2.md`, `--configuration
  …/configuration-boucle-reelle-v8.json`, `--go GO-2026-11-12-06`.
- **Déjà dépensé** : le lanceur v67 n'a **aucune option de déjà-dépensé** (vérifié : aucune dans le fichier) ; le registre de
  dépense cumulée est neuf dans chaque dossier de sortie, et chaque relais compte depuis zéro sous son plafond (Kimi 33,
  Argon 7). La dépense du v1 (≈ 1,19 USD) reste sous GO-2026-11-10-11.

## 2. Ce qui ne change pas

Aucun fichier v66 ni antérieur de l'arbre n'est modifié (vérifié : `git diff --stat 7e415cba ab53b7f482df5149d9f672f40e04220dffb4173a` ne nomme que des
fichiers neufs). Le cœur v66 (`VERSION` « boucle-reelle-v66 », relevé `boucle-reelle-v66.json`), la lecture gelée v66, le
lecteur du registre des GO v66, les gardes 1 à 23, le mode à blanc, les commandes v6, les pièces, les prix, les modèles, les
plafonds et parts, la durée de 72 heures, le monde, le jeu planté, l'héritage de départ, les critères de lecture.

## 3. Essais et banc

Résultats : `verifications-v2/` (sorties versées avec leurs compagnons).

- Suite de l'orchestrateur (dix fichiers : le v67 et les neuf de la section 12.3 du v1), `POLE_ESSAI_BAC_REEL_NON_JOUE=1`, Python
  3.13.18 de l'environnement de travail, numpy 2.4.6, scipy 1.17.1, pytest 9.1.1, à l'arbre `ab53b7f4` : **408 passés, 5 sautés**
  (les cinq motifs du rapport de course v1 : vrai bac à sable non joué ici, `bwrap` absent), 418 sous-essais ; sortie
  `verifications-v2/sortie-suite-v67-v1.txt`.
- Banc v67 : **151 tuées pour la raison attendue sur 151** (banc v66 porté : 133 sur 133 ; neuves v67 : 18 sur 18), code 0 ; sortie `verifications-v2/sortie-banc-v67-v1.txt`.
- Points de garde 24 sans mutation tuable, dits : le refus d'un délai booléen et le contrôle `isfinite` sont **redondants** avec
  la marge et le plafond de 7 200 s (un booléen vrai vaut 1 s, refusé par la marge ; l'infini est refusé par le plafond) ; gardés
  par prudence, sans mutation au banc.

## 4. Vérification hors ligne du lanceur v67 sur les vraies pièces

`verifications-v2/verifier-lanceur-v67-texte-v2-v1.py`, sortie `verifications-v2/sortie-verifier-lanceur-v67-v1.txt` : sur une copie
jetable de l'arbre `ab53b7f482df5149d9f672f40e04220dffb4173a`, le brouillon du texte v2, copié sous le nom `preenregistrement-boucle-reelle-organisme-v1-v2.md`
et scellé dans la copie seulement, la configuration v8 de son dossier de course, le vrai `registres/go.md` de `main` et
l'héritage de départ : le cas sain s'arrête à la garde 22 (`MachineRefusee`, bwrap simulé absent), donc après le texte, le monde, l'empreinte de la configuration, le GO (GO-2026-11-12-06, 45 USD, lu dans le vrai registre), le contenu de la configuration et la garde 24, et la garde 17 ; artefacts refusés en code 2 avant la machine : texte v1 (`PreenregistrementRefuse`, bloc `empreintes-du-code-v67` absent), configuration v7 et v6 (`ConfigurationRefusee`, empreinte), GO-2026-11-10-11 (`GoAbsent`, autre que celui du texte) ; garde 24 sur la v8 : Kimi 7 200 / 7 150 s, Argon 1 800 / 1 750 s ; rôles réels v67 sans porte : adaptateurs Kimi 7 200 s, Argon 1 800 s, budget d'appel 1,5 USD. Bilan « tout tient ».

## 5. Effet sur les critères de lecture et la dépense

Inchangés depuis le brouillon 1, sections 6 et 8 : aucun effet sur les critères ; pire cas des modèles 39,00 USD (Kimi 32,30,
Argon 6,70), sous les parts ; ligne de 45 USD, montant inchangé ; dépense du v1, ≈ 1,19 USD, sous GO-2026-11-10-11.
Machine : un appel du proposeur Kimi peut durer jusqu'à ≈ 2 heures ; la course reste sous 72 heures et ≈ 0,06 EUR par heure.

## 6. Réserves

- Le débit de Kimi n'est mesuré qu'une fois ; une réponse au-delà de 131 072 jetons serait coupée comme en course 2 (code 5).
- Le délai du relais Kimi n'est pas vu par la garde 24 : la consigne du poste doit faire relever la ligne « relais prêt »
  (« délai 7200.0 s »).
- Argon garde 1 750 s pour une borne effective portée à ≈ 29 000 jetons ; aucun débit d'Argon mesuré.
- `test_vrai_registre_lu` (hérité de la suite v66) lit le vrai `registres/go.md` s'il est sur la machine ; il vise
  GO-2026-11-08-02, comme en v66.

## 7. Ce qui reste avant la relance

1. Contre-lecture (R2) du code v67, de la configuration v8, de ce brouillon et du texte v2 ; vérification courte du différentiel
   v1 → v2 ; scellement du texte v2 sous son nom ; copie à l'octet sous `orchestrator/prereg/` de l'arbre de la course.
2. Consigne v4 du poste (rédigée à part) : paquets v65, v66 puis v67 ; dossier `configuration-v8/` ; relais Kimi avec
   `--delai-amont-s 7200` ; suite de dix fichiers et banc v67 en préalables 1 et 2 ; GO-2026-11-12-06.
