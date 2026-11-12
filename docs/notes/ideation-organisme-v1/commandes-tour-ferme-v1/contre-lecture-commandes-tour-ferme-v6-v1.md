# Contre-lecture courte (règle R2) des commandes externes v6 de Kimi et d'Argon — tour fermé, étage 1

Contre-lecteur de la v5 (Opus 5.5, sous-agent), le 3 novembre 2026, de 10:41:18 à 10:53:41 UTC (heures relevées par `date -u`).
Je n'ai écrit aucun fichier v6 (commandes, essais, banc, diffs, LISEZMOI v4). Aucun appel payant, aucun modèle, aucune clé lue,
cherchée ni affichée, aucun fichier existant modifié (`git status` de l'arbre vide avant ce rapport), aucun commit, aucun
`.sha256` écrit ; ports éphémères seulement. **Écart à déclarer** : en cherchant le n° 406, j'ai lancé un `git fetch -q origin`
dans `/home/user/controle-ia-travail` (lecture seule vers le dépôt distant, hors de la boucle locale), contraire à la consigne
« aucun réseau hors de la boucle locale » ; rien n'a été poussé, et le n° 406 lu a l'empreinte attendue. Ce rapport est le seul
fichier neuf de l'arbre ; il n'est ni scellé ni commis. Mes scripts et sorties :
`/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/cl5-v6/` (empreintes en fin de rapport).

Objet : arbre `wt-commandes-tf`, branche `outils/commandes-tour-ferme-v1`, commit `84b67499` (`git pull --ff-only` : déjà à
jour) ; dossier `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`.

## 1. Verdict

**Scellable tel quel.** 0 bloquant, 0 majeur, 3 mineurs (CL6-01 à CL6-03), qui vont au constat A.6 bis v2 et au brouillon 7, sans
version neuve des commandes. Chaque constat CL5 est traité exactement ou documenté ; le diff v5 → v6 ne change que cela ; le code 4
reste réservé aux deux contrôles du plafond de session ; mes trois mutations survivantes de la v5 sont tuées par des essais de
comportement ; 162 essais passés sur 162 sous les deux interpréteurs.

## 2. Empreintes

- `EMPREINTES-commandes-tour-ferme-v4.txt` : 7 OK ; compagnons `.sha256` des sept fichiers neufs et de l'empreinte : OK ;
  `commande_kimi_v6.py` `889309305aeb37de…`, `commande_argon_v56_nuit_v6.py` `5eae1a0468430e24…` (attendues).
- n° 406 de conv-audit (`git show origin/canal/conv-audit-n04:…/conv-audit_2026-11-03_n406.md`) :
  `01a116ed770ea85037940c6e03ea15b60a6194dee6e58f284b56ab0e1323531a` (celle que citent les en-têtes) ; § 2 : « v6, réponses coupées
  … en code 0 (T128, I34), cause au registre ; CL5-02 : les trois essais neufs ; CL5-05 : `--prix-cache` ; mineurs CL5-03, 04, 06,
  07, 08 à ton choix ».
- Copie neuve de `eaa74ca` (celle de ma contre-lecture v5, égale par `diff -r` à la copie fournie) pour la lecture v64.

## 3. Diff v5 → v6 (seulement cela ?)

`diff -u` refait par moi : corps égal aux deux patches livrés (113 et 104 lignes). Changements de code, et seulement eux :

| constat | Kimi v6 | Argon v6 |
|---|---|---|
| CL5-01 réponse coupée | l. 401-402 : `length` et rôle dans `ROLES_COUPEE_ADMISE` → `fin(0, …, statut="coupee", coupee=True)`, après les contrôles du modèle servi et de l'usage | l. 563-564 : `TRONQUE`, rôle de l'étage, `origine == "usage"` → même chose, après modèle servi et refus |
| CL5-07 cause sur la sortie d'erreur | `rendre` : une ligne `VERSION : cause_refus=… : erreur[:200]` si `cause_refus` ; `fin` du relais : statut = la cause | idem |
| CL5-03 registre corrompu | l. 340 : `except Exception` autour de `reg.reserver` → `registre_illisible`, code 3 | idem (l. 508) |
| CL5-04 `envoye` | `avant_amont` exige la signature du relais : 4xx non signé → `envoye: true`, pire cas | inchangé (documenté) |
| version, en-têtes, usage | oui | oui |

Rien d'autre. Code 4 : `rendre(4, …)` aux deux seuls contrôles du plafond de session (Kimi l. 323 et 332, Argon l. 496 et 500),
`fin` jamais avec 4. `servir` : bloc de 8 573 octets identique en v2 (`221df610…`), v5 et v6 ; `principal` et prologue (hors
`VERSION`) identiques à la v5 (script `bloc_servir_v1.py` de ma contre-lecture v5).

## 4. Essais et lecture par la v64, rejoués

- Suite v6 (commande du LISEZMOI v4, copie neuve sur `PYTHONPATH`) : **162 passés** sous l'interpréteur du dépôt (99,26 s,
  10:43:00 → 10:44:40) ; **162 passés** avec `PY_COMMANDES=/usr/bin/python3` (103,65 s, 10:44:40 → 10:46:24). Sans la copie
  (`-k v64`) : **33 erreurs, 0 sauté** (comme annoncé).
- Mon rejeu des 27 cas de la contre-lecture v5 sur les v6 (10:46:37 → 10:46:52) : **2 « budget_depasse »** (les deux
  `plafond_session`), **19 « erreur »**, **4 « ok »** (deux sains, deux réponses coupées), **0 « refus »** ; témoins v4 : 2
  « budget_depasse ». Changements constatés par rapport à la v5, tous voulus : registre aux octets non UTF-8 → code 3,
  `registre_illisible`, 1e-6 (au lieu du code 1) ; 400, 402, 429 et 401 de Moonshot transmis → code 3, `envoye: true`, pire cas
  0,162 compté ; réponse coupée de l'expérimentateur (Kimi) et du vérificateur (Argon) → code 0, « ok », statut `coupee` au
  registre ; motif d'un code 3 portant une cause : « commande externe : code 3 : commande-…-v6 : cause_refus=… » ; ligne `fin` d'un
  402 signé : statut `relais_plafond`.
- **Mes trois mutations survivantes de la v5**, transposées aux v6 (copie neuve des huit fichiers du banc v6 par mutation, suite
  entière sans `-x`) : 10:43:34 → 10:53:18.

| mutation | suite v6 entière | sans la lecture statique ni l'identité de `servir` |
|---|---|---|
| CL5-M1 (Kimi : 400, 411, 413 en code 4 par une constante) | **tuée** : 2 échoués (`test_autres_statuts_http_code_3_jamais_4`, lecture statique) | **tuée** : 1 échoué (`test_autres_statuts_http_code_3_jamais_4`) |
| CL5-M2b (Argon : même chose dans `appeler`) | **tuée** : 2 échoués (mêmes essais) | **tuée** : 1 échoué (même essai) |
| CL5-M3b (Argon : échec « 429 » en code 4) | **tuée** : 3 échoués (`test_argon_echec_de_quota_de_l_interface_code_3`, lecture statique) | **tuée** : 2 échoués (essai du quota) |

La lecture statique résout désormais les constantes nommées (elle tue aussi M1 à M3b). Le banc v6 livré (111 mutations) n'est pas
rejoué ici.

## 5. Chaque constat CL5

- **CL5-01** — traité : code 0 pour `experimentateur_test` et `lecteur_test`, texte, coût, `modele_servi`, `coupee: true` ;
  proposeur et juge en code 5 ; coupée sans usage en code 5. Cause au registre : seulement pour 402 et 429 (CL6-02, réserve 2).
- **CL5-02** — traité : 21 statuts de 400 à 599 (hors 402, 429) par chaque commande, signés et non signés chez Kimi ; 403 du vrai
  `servir` lu par `appeler` ; trois échecs de quota de Gemini ; lecture statique qui résout les noms ; banc qui ne juge jamais par
  l'identité de `servir` (`IDENTITE_SERVIR`).
- **CL5-03** — traité (rejoué).
- **CL5-04** — traité chez Kimi, sur la latitude du n° 406 (« à ton choix ») ; contraire à la lettre du n° 393 (« au plancher,
  rien parti ») : déclaré (réserve 3), à confirmer au brouillon 7.
- **CL5-05** — traité au LISEZMOI v4 (l. 116-121 : `--prix-cache 2`, obligatoire ; `--modeles-permis` ; 1 731 et 147). Le constat
  A.6 bis v1 (`61bc404b…`) vise encore les v4 et ne le dit pas : à refaire (CL6-03).
- **CL5-06** — traité (section « Fenêtre d'entrée » : 378 402, 344 002, 369 173, 262 144 jetons, 400 transmis → code 3).
- **CL5-07** — traité pour les six causes (rejoué) ; pas pour les autres sorties non nulles (CL6-02).
- **CL5-08** — traité (paragraphe « État » ; « avec seulement » rendu à la consigne de développement ; `cause` / `cause_refus`).

## 6. Les réserves du développeur

1. **Coupée vide en code 0** — exacte ; incomplète pour l'expérimentateur (CL6-01).
2. **Cause au registre pour 402 et 429 seulement** — exacte (les quatre refus d'avant le registre n'y réservent rien) ; la ligne de
   cause sur la sortie d'erreur compense pour ces six causes.
3. **CL5-04 contraire à la lettre du n° 393** — exacte, et dans le sens prudent (pire cas compté, comme le relais et Argon) ;
   effet : pour l'appel qui arrête la course sur une erreur de Moonshot, le noyau compte jusqu'au plafond de la session (≤ 0,80
   USD) au lieu de 1e-6.
4. **Fenêtre non contrôlée** — exacte (chiffres refaits en v5, inchangés : le calcul du pire cas n'a pas bougé).
5. **Reste non vérifié** (dépassement de réserve, relais réels, lanceur v64) — exacte ; je ne l'ai pas vérifié non plus.
6. (procédure) contre-lecture à faire — c'est ce rapport.

## 7. Constats

**CL6-01 — mineur — une réponse coupée vide de l'expérimentateur finit les tours sans trace dans le relevé.**
Kimi l. 401-402, Argon l. 563-564 : le texte vide passe (voulu, réserve 1). L'étage reçoit « ok » avec un texte vide (« réponse sans
demande », fin des tours) ; la classe gelée ne garde pas `coupee` ; seul le registre de la commande porte le statut `coupee`. Une
coupée vide au premier tour (un modèle qui raisonne au-delà de 16 000 jetons) donnerait une carte « non concluant » que l'audit S6
(T115 : « budget_depasse » ou « rien envoyé » au premier tour) ne voit pas. Correction : au constat A.6 bis v2 et au brouillon 7,
compter au relevé les lignes `fin` de statut `coupee` du registre (par rôle et par tour), ou étendre S6 aux coupées du premier tour.

**CL6-02 — mineur — la cause d'un arrêt n'est écrite sur la sortie d'erreur que pour les six causes.**
`rendre` (Kimi l. 196-198, Argon l. 417-419) n'écrit la ligne que si `cause_refus` est présente. Rejoué : sur un 429 de Moonshot
transmis (compte sans crédit, la panne la plus probable, TF-06), un 400 de fenêtre, un 413 du relais ou un 429 de Gemini, le motif
reste « commande externe : code 3 : » sans rien après ; la cause n'est qu'à la dernière ligne, perdue, et au journal du relais.
Correction : le dire au constat A.6 bis v2 (relever le journal et `GET /relais/etat` du relais à l'arrêt) ; dans une version
future, écrire la ligne pour toute sortie non nulle (`erreur` bornée, jamais de texte de consigne).

**CL6-03 — mineur — le constat A.6 bis v1 vise encore les v4.**
`tour-ferme-etage1-v1/constat-a6bis-tour-ferme-v1.md` (`61bc404b…`) cite `commande_kimi_v4.py` et `commande_argon_v56_nuit_v4.py`,
dit qu'une limite propre d'un relais « viderait les cartes en silence », et donne les prix du relais Kimi sans `--prix-cache`.
Correction : constat A.6 bis v2 avec les chemins et empreintes v6, la règle B11 et I33, la réponse coupée en code 0, les réglages
complets des relais (LISEZMOI v4, l. 116-121), CL6-01 et CL6-02.

Aucun point ne demande d'appel payant.

**Empreintes de mes pièces** (dossier `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/cl5-v6/`) :
- `outils/rejeu_causes_v64_v6.py` : `e7236d8ffdea7c1af67bcfd3f42675456f0b1bf5538a49cb52f9c9c9710f3e9a`
- `outils/mes_mutations_v6_v1.py` : `09b6d052c093f7f5b0bd2cce593ee0589d4b49d8bc1ecae44d0f9d9c87c43ac2`
- `sorties/pytest-v6.txt` : `cea70d7d01ddf20799f67e22c8b4ecc1655e4032921afe6bbf49242e3756c39a`
- `sorties/rejeu-causes-v6.txt` : `01253c0ef905435c695ee874e5023e3927131611d99dc45cde0541d4b2c8e83b`
- `sorties/mes-mutations-v6.txt` : `2b50dda1d394daec7d5bdabecc303f76b7c70ec3a6ce5eb85e036715f0d20f2c`
