# Contre-lecture (R2) — mini-course d'idéation réelle, Kimi et Argon seuls (GO-2026-11-01-12), v1

Contre-lecteur neuf, auteur d'aucune pièce ; 1er novembre 2026 ; aucun appel payant ni réseau, aucune pièce modifiée.

**Verdict : scellable après corrections** (un bloquant, trois majeurs).

## Ce que j'ai vérifié par exécution (hors réseau)

- Essais des gardes : 16 réussis ; copie v56 conforme ; table des pièces gelées « conforme » ; empreinte du devis exacte.
- Mode `verifier` : GO-2026-11-01-12 à 10 USD exactement, une ligne extraite, 22 gardes rejouées.
- Répétition `finale2` : 68 débuts au registre (66 appels de course, 2 contrôles) ; relais Kimi 27, Argon 41 ; aucun appel « tableau ».
- Deux arrêts simulés passés à l'agrégateur : trace « conforme », motif `trois_echecs_consecutifs`, aucun verdict ouvert.
- Commande factice en code 5 avec un modèle servi faux : `ArretModeleServiDifferent` levé.
- Piège shell : essai dans le bloc-notes, voir CLM-01.

## Bloquant

**CLM-01 — L'arrêt par le piège ne marche pas pendant la course.**
Citations :
- LISEZMOI : « Arrêt (R10) : `kill <PID du lanceur>` (le piège arrête les relais par leur PID, écrit leur état final) » ;
- préenregistrement, liste d'arrêt : « signal reçu (SIGTERM, SIGINT) | `ArretSurSignal` ; trap du lanceur | arrêt propre […] relais arrêtés par PID ».

Constat :
- La course tourne au premier plan (`env -i … timeout 12600 "$PY" … lancer`). Bash n'exécute un piège qu'à la fin de la commande au premier plan qu'il attend.
- Le processus Python ne reçoit pas le signal d'arrêt.
- Essai fait : `kill` envoyé à t+0 ; le piège s'est exécuté à t+5 s, quand l'enfant a fini de lui-même. Cette nuit, l'attente irait jusqu'à 3 h 30, avec la dépense qui continue.
- Ensuite, `exit 130` saute l'agrégateur et la recherche des clés.

Correction (nouveau nom de lanceur, R12) :
- lancer la course en arrière-plan (`… & PID_C=$!`), écrire `PID_C` au journal, puis `wait "$PID_C"` ;
- dans le piège : `kill -TERM "$PID_C"` (`timeout` relaie le signal au Python, qui lève `ArretParSignal`), puis `wait`, puis l'arrêt des relais par leur identifiant de processus ;
- après un signal, lancer quand même l'agrégateur et la recherche des clés ;
- éprouver ce chemin dans la répétition : `kill` en pleine course, devant les faux amonts ; il faut un bilan « signal », des relais arrêtés et une trace écrite.

## Majeurs

**CLM-02 — La « garantie : 10 USD au plus » est conditionnelle, et un dépassement de réserve n'arrête pas la course.**
Citations :
- « garantie : 10 USD au plus, par la garde cumulée » ;
- liste d'arrêt : « coût lu au-dessus du pire cas réservé | commandes (`depassement_reserve`) | appel rendu non conforme (code 5), compté au registre ».

Constat :
- La garde cumulée est juste. Mais elle compte en dollars **au barème supposé** d'Argon (10 et 50 USD par million).
- Elle tient seulement si chaque appel coûte moins que son pire cas, ce qui repose sur deux hypothèses :
  - jetons d'entrée d'Argon ≤ caractères / 3 ;
  - jetons de réflexion d'Argon bornés par `maxOutputTokens`.
- Un dépassement n'est qu'un appel inexploitable : la course continue. Ce motif figure pourtant dans une « liste d'arrêt ».

Corrections :
1. Écrire « 10 USD au plus au barème supposé d'Argon ; facture réelle à relire au tableau de bord du fournisseur » et garder la réserve.
2. Faire d'un `depassement_reserve` un arrêt de la course : l'adaptateur de la nuit lève une exception dès qu'il lit `depassement_reserve: true`, et la trace en donne le motif codé.
3. Optionnel : réserver l'entrée d'Argon à caractères / 2, ou fixer le plafond cumulé des commandes à 9,5 USD.

**CLM-03 — Affirmation R5 inexacte : plusieurs gardes de la liste d'arrêt n'ont jamais été éprouvées.**
Citation : « Chaque garde a été éprouvée sur un cas sain et sur un artefact pendant la répétition (R5 ; liste au LISEZMOI) ».

Gardes sans essai sur un artefact :
- le piège (CLM-01) ;
- `depassement_reserve` ;
- la réponse 502 « modèle servi » du relais Kimi, convertie par `commande_kimi_v2.py` (la conversion n'est éprouvée que dans l'adaptateur) ;
- le refus d'Argon par la garde cumulée (seul Kimi est éprouvé) ;
- les plafonds propres du relais Argon (402, 429, modèle non permis) et son refus sans clé ;
- la révocation de la ligne de GO lue à travers l'extrait (voir ci-dessous) ;
- la recherche des clés et le contrôle en échec (reconnus « non éprouvés »).


Correction : ajouter ces essais, chacun avec un cas sain et un artefact (tous faisables sans réseau, avec des commandes et des amonts factices). Sinon, retirer l'affirmation et lister les gardes non éprouvées en réserve.

**CLM-04 — Le nom du rapport de contre-lecture empêche le lancement.**
Citations : lanceur Python, `CONTRE_LECTURE = …/contre-lecture-preregistrement-mini-course-kimi-argon-v1.md` ; le lanceur shell vérifie `contre-lecture-preregistrement-mini-course-kimi-argon-v1.md.sha256`.

Constat :
- On m'a demandé `contre-lecture-mini-course-kimi-argon-v1.md`. En l'état, le lanceur refuserait de partir (code 2). C'est sans danger, mais cela bloque la nuit.

Correction :
- en déposer une copie identique octet pour octet sous le nom attendu, et la sceller : l'empreinte est la même ;
- citer cette empreinte dans le préenregistrement.

## Point 4 — lecture du registre des GO : aucun affaiblissement trouvé

- L'extrait garde la ligne du GO et toute ligne de révocation qui le cite, avec la même expression régulière : la règle de révocation de la v56 ne voit rien de moins.
- Type, Lazar, validité et montant unique sont relus par `verifier_go_v56` ; une extension est refusée.
- Restent deux manques : la révocation n'est pas éprouvée (CLM-03), et `garde_calcul.py` n'est pas gelé (CLM-08).

## Mineurs

**CLM-05 — Plafonds des relais.**
Citation : « `--plafond-usd 10` » pour chacun des deux relais.
Constat : 20 USD à eux deux ; le second barrage ne borne pas le total, et un appel local direct aux ports 8804 et 8805 contourne le registre.
Correction : par exemple 3,5 USD pour Kimi et 6,5 USD pour Argon (somme de 10, au-dessus du pire cas de chaque fournisseur au scénario B).

**CLM-06 — Clés dans l'environnement de processus hors relais.**
Citation : « grep -rqF -- "${!v}" "$RA" ».
Constat :
- la clé passe en argument de `grep`, et `/proc/<pid>/cmdline` est lisible par tous ;
- l'agrégateur, `registre_depense_cumulee_v1.py` et `etat_relais` ne tournent pas sous `env -i`, donc ils héritent de toutes les clés de la session.
Correction : chercher les clés par un Python qui les lit dans son environnement ; lancer ces trois outils sous `env -i`.

**CLM-07 — Pas d'épreuve R5 sur le run réel.** Citation : « `--artefacts-sur-run` injecte, dans une copie de la trace d'un run […] (chacun doit être vu) ». Seule la répétition l'appelle. Correction : l'ajouter au lanceur réel, sortie au journal.

**CLM-08 — Garde du dépôt non gelée.** `.claude/hooks/garde_calcul.py` lit le registre des GO ; son empreinte est notée, jamais comparée. Correction : l'ajouter aux « Pièces gelées ».

**CLM-09 — Les motifs codés risquent d'être mal étiquetés.**
Constat :
- un refus de la garde cumulée (code 4) apparaîtra comme `trois_echecs_consecutifs` ou comme nœud, et non comme `plafond_cumule` ;
- le délai `timeout 12600` apparaîtra comme `signal_recu`.
Correction : le dire dans L1, ou ajouter des motifs distincts.

**CLM-10 — Arrêt et verdicts.** L'agrégateur n'ouvre aucun verdict hors de `generation_terminee` (vérifié : L3 et L4 vides). Correction : écrire à la ligne `arret_motif_code` : « L3 et L4 non calculés (O12) ».

**CLM-11 — Troncatures prévisibles.**
Constat :
- les appels courts d'Argon ont 4 000 jetons de sortie, réflexion comprise ; son contrôle en a 998, et le devis supposait 1 500 ;
- les appels courts de Kimi ont 16 000 jetons ;
- toute troncature donne un appel inexploitable, donc A14 et un nœud, ou un contrôle en échec.
Correction : l'ajouter aux réserves comme cause d'arrêt prévisible, au même titre que A14.

**CLM-12 — Répétition incomplète.** Ni le vrai `lancer-mini-course-v1.sh` (une copie modifiée a servi) ni le chemin réel de `servir` (appelant injecté) n'ont tourné. Correction : le dire au préenregistrement.

**CLM-13 — Fusion dans L4.** Comptée comme fiche d'Argon alors qu'elle peut naître d'une paire Kimi et Argon. Correction : le noter dans la réserve de L4, ou l'exclure de L4.

## Conformes

R3 ; L1 à L4 gelés et descriptifs ; symétrie R4 ; réserve « deux familles, pas de juge d'une autre lignée » ; anti-fuite (liste blanche stricte, canaris des cinq consignes, titres, suites de six mots, garde rejouée) ; relais sous `env -i` et contrôle de leur identifiant de processus ; scénario B fidèle.

## Non vérifié

- Le prix réel d'Argon.
- Si `thoughtsTokenCount` est borné par `maxOutputTokens` chez `gemini-4-argon`. Dans 23 appels journalisés, aucune sortie ne dépasse `max_tokens`, mais aucune ne s'en approche.
- Le rapport réel jetons d'entrée / caractères. Les journaux existants n'ont pas la longueur des invites : leur champ `caracteres` est celui de la réponse.
- Les formats réels de Moonshot et de Gemini, et le passage du relais Kimi par le mandataire du conteneur.
- La durée réelle des appels.
- Le lancement réel avec la vraie spécification scellée.
- `repetition_complete_v1.sh` non rejoué (ports 8804 et 8805).
