# Contre-lecture courte des ajouts de la v4 — texte A1-v3 (brouillon 1), lanceur durable v4, ordre de course v2 — v1

Contre-lecteur neuf (R2) : je n'ai écrit ni les textes v1 à v4, ni les lanceurs, ni aucune contre-lecture précédente. 5 novembre
2026, de 10:30:55 à 10:46 UTC (heures relevées par `date -u`). Consigne : `consigne-contre-lecture-courte-v4-v1.md` (dépôt privé,
main `1c6d7428`, qui ne change que la consigne depuis `4031f413`). Interdits tenus : aucun commit, aucun `.sha256`, aucun fichier
existant modifié, aucun réseau, aucune location, aucune clé lue, aucune dépense ; commandes sous `timeout 900 nice -n 10`, épreuves
dans le bloc-notes (`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/`), arbre du dépôt propre après coup.

## Verdict

**Scellable après couples** (4 couples, `couples-contre-lecture-courte-v4-v1.json` ; aucun bloquant de texte).
Ajouts conformes : 15 couples des lecteurs tels quels, 18 du rédacteur limités à la section 0.8 ; un seul marqueur ; texte accepté par le lanceur gelé ; lanceur v4 : 127 essais passés, corrections 1 à 8 conformes ; relais conforme à la commande d'Argon lue.
Avant la course (non avant le scellement) : deux nœuds de Lazar déjà déclarés (périmètre de GO-2026-11-04-06 pour la v4, publication de la v4) à porter dans l'ordre v2, qui doit aussi corriger l'ordre de ses étapes (`$D` utilisé avant d'être créé).

## Pièces vérifiées (sha256 recalculés, égaux à la consigne et au rapport)

- Brouillon 1 de la v4 `e0c90f39a675c7eeacdefa43301474ea71c3d6a42250a56a62ba3cd1713b2f34` ; v3 scellée `c697d0df…` (dépôt public
  `08ad8f35`) ; couples du rédacteur `couples-texte-v4-v1.json` `f76885c5…`, script `appliquer-couples-texte-v4-v1.py` `0918a4a3…`,
  sortie `1553aa13…`, `ecrire_couples_texte_v4.py` `e3e4c18a…` ; rapport `rapport-redaction-v4-v1.md` `b76f5bd3…` ; épreuve
  `epreuve-texte-v4-lanceur-gele-v1.py` `d9abd6e0…` et sa sortie `f2f22867…`.
- Lanceur v4 `src/controle_ia/hote_durable_a1_v3_v4.py` `8101d33b…`, amorce `a2cecc7e…`, essais `65b8cf6e…` ; différentiel
  `diff-lanceur-v3-vers-v4-hors-renommage.txt` `3f47c285…` ; v1 `5b853fde…`, v3, sondes v1 et v10 : inchangées depuis `bb35e87f`.
- Ordre v2 `db8b0735…`, ordre v1 `97f712a7…` ; contre-lectures complètes `06d6283d…` (texte), `ed4dc27e…` (lanceur), couples `16803c05…`.
- Commande d'Argon gelée, au commit `60656845` du dépôt privé (objet présent dans ce conteneur, sans branche locale) :
  `commande_argon_v56_nuit_v2.py` `221df610…` (406 lignes), `registre_depense_cumulee_v1.py` `8ba92066…`, collisionneur `c9725f02…` —
  lus sans exécution.

## Épreuves rejouées

1. `appliquer-couples-texte-v4-v1.py` sur la v3 scellée, sortie dans le bloc-notes : texte **identique à l'octet** au brouillon 1
   (`e0c90f39…`) ; empreinte intermédiaire après les 15 couples `9851ed9f…`, égale à celle du contre-lecteur du texte.
2. Chaque « ancien » des 18 couples du rédacteur est présent une fois dans la v3 scellée et dans aucun « nouveau » des 15 : les
   deux lots sont disjoints.
3. Blocs `plan-gele` et `empreintes-du-code` : identiques à l'octet v3 → v4 ; v2 → v4, seule la ligne `go:` change.
4. Différence v3 → v4 rattachée aux sections : tête, 0.5 bis, 0.7 (point d'insertion de 0.8), 0.8, 4, 8, 12, 13, 14, annexe B ;
   **rien** dans les sections 1, 2, 3, 5, 6, 7, 9, 10 et 11.
5. Recherche `<<[A-Z0-9_]+>>` : `['<<COMMIT_LANCEUR_DURABLE>>', '<<COMMIT_LANCEUR_DURABLE>>']`, rien d'autre (le seul autre `<<…>>`
   est le motif écrit en annexe B, hors motif).
6. Épreuve du lanceur gelé rejouée sur un `git archive 08ad8f35 orchestrator` neuf : marqueur rempli d'un hash factice → **accepté**
   (empreinte `54782fc5…`, GO-2026-11-04-06, 400 USD, 259 200 s, « aucun », Argon un fil, devis maximal 190,46 USD) ; marqueur
   laissé → refus « marqueur(s) non rempli(s) » ; sortie **identique à l'octet** à `epreuve-texte-v4-lanceur-gele-v1-sortie.txt`.
7. Différentiel du lanceur refait (v3 renommée par `sed`) : mêmes lignes que `diff-lanceur-v3-vers-v4-hors-renommage.txt`, à la
   ligne `VERSION` près (renommage).
8. `PYTHONPATH=src timeout 900 nice -n 10 .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_hote_durable_a1_v3_v4.py` :
   **127 passés en 183 s** (10:34:12 → 10:37:16 UTC) ; `-p no:cacheprovider` seulement pour ne rien écrire dans l'arbre.
9. Mes 4 couples appliqués au brouillon 1 (bloc-notes, `epreuve_clc.py` `fe19e8c2…`) : chaque « ancien » unique, deux marqueurs
   restants, texte `3696e9c3…` (2 240 lignes) **accepté** par le lanceur gelé marqueur rempli, refusé marqueur laissé.

## Points (gravité : bloquant / à corriger / note)

**Question 1 — couples et section 0.8**
1. Note (conforme) — les 15 couples des lecteurs sont appliqués tels quels (fichier lu par son empreinte, ordre gardé, empreinte intermédiaire égale).
2. Note (conforme) — les 18 couples du rédacteur correspondent un à un aux points 1, 2 et 18 à 28 de 0.8 (couples 7-8 → point 21 ; 10-12 → 23 ; 14-16 → 25) ; aucune ligne changée hors des couples (garde du script, rejouée).
3. Note (conforme) — hypothèses, prédictions, métriques, seuils, critères gelés, audits A1 à A9 : sections 2, 3, 5, 6, 7 non touchées depuis la v2 ; plan et code gelés inchangés.
4. Note — paragraphe de tête : « couverte … par le mot de Lazar de R-1553 … à confirmer » est exact ; R-1553 dit « A1-v3 complet, puis lancer » et c'est la mère qui ajoute « texte v4 et nouveau scellement s'il le faut » ; le texte le traite bien en nœud.
5. Note — la convention de tête (« la v3 », « texte v3 » décrivent la v3) laisse les titres « Troisième course (v3) » et « Hôte durable (v3 ; …) » nommer la course qui tournera sous la v4 : juste par la convention, comme la note 9 du lecteur du texte ; sans effet.
6. Note — notes 5 à 9 du lecteur du texte non reprises (offre écrite deux fois, « 80 h de vie », « la fille n'a plus de rôle », renvois du point 23 de 0.7, section 4 « GO ») : je les laisse en notes ; aucune ne change une garde ni une lecture.
7. À corriger (couple 3) — section 14 garde « Contre-lecture courte des ajouts de la v4, **à faire** » : même défaut que le n° 4 dans la v3 scellée (point 4 du lecteur du texte) ; le couple la dit faite, avec ce rapport et son verdict.

**Question 2 — marqueur et lanceur gelé**
8. Note (conforme) — épreuves 5 et 6 ; le remplissage doit nommer le commit de `main` qui porte le lanceur v4 **et** la v1, la sonde v1 et la sonde v10 (les quatre modules que `louer` copie de `COMMIT_PRIVE`), puis le contrôle de la section 13, point 4, sur le fichier final.

**Question 3 — lanceur v4**
9. Note (conforme) — `NOM_TEXTE` v4 dans la v4 seule ; v1 inchangée (`5b853fde…`) ; hors de `cmd_course` et du chemin vérifié (`preparer`, l. 693), la v1 n'emploie `NOM_TEXTE` nulle part (l. 56, 597, 685) ; `cmd_course` remplace l'unique occurrence ; essai : la v4 refuse un dépôt public sans texte v4.
10. Note (conforme) — corrections 1 à 8 faites comme proposées, chacune avec cas sain et artefact (ou artefact « de départ » sur la v3) : 1 (6 contre 2 ; étiquette autre : 2), 2 (Vast qui garde la machine : arrêt), 3 (journal en panne : versé, détruite), 5 (arbre sali après `--verifier-seulement`), 6 (ligne de 330 caractères), 7 (2.4.6 : refus, hôte et amorce), 8 (8 artefacts de la machine, client, cinq « no_such_ask », `controler` protégée et délai, minuterie sans `curl`, amorce qui installe numpy) ; la 4 n'est pas une garde (écriture au journal).
11. Note — correction 4 chez le pilote : `empreintes_du_code()` cherche l'amorce en `parents[1]/scripts/…` du module ; l'ordre copie les modules à plat dans `$D` : l'amorce y sera « absent de ce dossier » (l'essai tourne dans l'arborescence du dépôt) ; `COMMIT_PRIVE` et les quatre modules restent écrits ; sur la machine, l'amorce est trouvée.
12. Note — correction 2 jamais éprouvée sur Vast : un `DELETE` accepté dont l'inventaire tarde plus de ≈ 20 s (trois lectures à 10 s) fait demander l'arrêt d'une machine en cours de destruction ; l'arrêt arrête aussi la minuterie ; la sortie est déjà versée, le pire est du stockage facturé jusqu'au contrôle d'après échéance (code 7, la mère décide).
13. Note — versement : le « mesuré » est la somme des délais des appels réels (pire cas compté, 3 360 s), sous la réserve de 3 600 s ; marge 240 s.
14. **Conformité du relais à la commande d'Argon gelée (lue au commit `60656845`, `221df610…`)** — conforme : la v1 gelée lance `servir --port 8805 --plafond-usd 410 --max-appels 9000 --journal <sortie>` (`hote_durable_a1_v3.py:653-655`), les trois premiers strictement positifs ; `--modeles-permis` par défaut « gemini-4-argon » (modèle du plan) ; `--collisionneur` et `--sha-collisionneur` par défaut = `<racine>/donnees/espece-seule-v1/collisionneur_v7.py` (`:77`, relatif à la commande) et `c9725f02…`, que l'hôte extrait au même endroit et vérifie ; clé dans `GEMINI_API_KEY` (`env_relais` v4, l. 596-597) ; écoute et lecture sur `127.0.0.1` ; seul `GET /relais/etat` est lu (`etat_relais`, v1 l. 470-476) ; clés vérifiées `plafond_usd` (410.0 = 410), `max_appels`, `appels` = 0, `cle_presente` booléen (v1 l. 668-670), `depense_usd` lue par `.get` : toutes dans la réponse (`commande…:150-157`). Fait neuf : le relais **repart de zéro** à chaque lancement (`EtatRelais`, `:106-110`) — couple 2.

**Question 4 — ordre v2**
15. Note (conforme) — repris : préalable 2 au motif `troisieme-*` (4 branches) ; Argon seul (5) ; crédit (6) ; « no_such_ask » en dossier neuf, une fois ; conduite pour 0, 1, 2, 3, 5, 6, 7, égale aux codes de `controler` v4 ; récupération ; jeton par `JETON_VAR` ; commande d'Argon lue avant la location (3) ; destinataire ; `timeout 1800`.
16. Note (conforme) — commande de location : les 11 options requises de `louer`, puis `--verifier-seulement` ou rien ; `GO_ID=GO-2026-11-05-03` dans `env -i` ; `CLE_ARGON`, `GH_TOKEN`, `VAST_API_KEY` ; quatre modules copiés de `COMMIT_PRIVE` ; `offre` rend l'identifiant que `louer` convertit : exactement ce que le lanceur v4 attend.
17. À corriger (ordre) — étapes dans le mauvais ordre : les préalables s'écrivent dans `"$D/journal-location-…-v4.log"` et le préalable 1 lance `"$D/hote_durable_a1_v3_v4.py" inventaire`, alors que `$D` n'est créé (`mkdir "$D" || exit 2`) et les modules copiés que dans le bloc de location : suivi à la lettre, le préalable 1 ne tourne pas, ou le bloc sort en 2 au `mkdir` (sans dépense, mais hors des cas « si `louer` rend 2 »).
18. À corriger (ordre) — préalable 3 : désormais lu (R-1561 ; relu ici, point 14) ; (a), (b), (c) conformes ; écrire la lecture au journal suffit ; le `git show` sur la branche `donnees/recuperation-collisionneur-v8-v1` reste un contrôle d'empreinte (branche non vérifiée ici, aucun réseau).
19. Note — préalable 6 plus strict que le texte (qui admet aussi le mot de Lazar qui abandonne la précaution, écrit avec son prix) : sûr, mais à aligner ou à dire voulu.
20. Note — récupération : pour « secret trouvé », le redémarrage rejoue le même contrôle des secrets et s'arrête de nouveau ; pour un jeton échu ou révoqué, même jeton : la voie ne sert qu'à une poussée manquée en passant ; à écrire.

**Question 5 — autre point pour une course à 400 USD au plus**
21. Bloquant pour la course, non pour le scellement (nœuds déjà déclarés par le texte) — le mot de Lazar sur le périmètre de GO-2026-11-04-06 (« texte v3 neuf ») pour la v4, ou l'extension du GO, et son accord pour publier la v4 sur le dépôt public (R-1539 ne couvrait que la v3) : l'ordre v2 ne les exige pas au journal ; sans eux, la dépense sortirait du périmètre du GO.
22. Note — un relais relancé repart de zéro : ses plafonds (410 USD, 9 000 appels) valent par lancement ; la borne cumulée reste le registre de dépense du lanceur (400 USD), qui mord le premier ; le relevé final de l'hôte ne voit que le dernier lancement — couple 2 (déclaration, aucune règle neuve).
23. Note — chemin d'un 402 de l'interface lu : échec rendu en HTTP 200 par le relais, compté au pire cas, commande en code 3 (`:191-205`, `:358-360`) ; refus du relais seuls en code 4 (`:340-341`) : l'hypothèse du texte tient — couple 1.

## Couples (`couples-contre-lecture-courte-v4-v1.json`, 4, dans cet ordre, sur le brouillon 1, après les 33 déjà appliqués)

1. Section 8, risque déclaré (HTTP 402) : « non relue sur ce point » → lue (R-1561) et relue ici, avec les lignes (point 23).
2. Section 8, « Garde » : relais relancé, compteurs neufs, plafonds par lancement, borne cumulée du lanceur (points 14 et 22).
3. Section 14 : contre-lecture courte des ajouts de la v4 « à faire » → faite (point 7).
4. Section 0.8 : lignes 29 à 32 pour ces couples (règle « et seulement » du paragraphe de tête).

## Corrections de code (liste à part ; aucune exigée avant la location)

- C-a (note 11) : `empreintes_du_code()` chez le pilote — chercher l'amorce aussi à côté du module, ou que l'ordre la copie dans `$D`.
- C-b (note 12) : correction 2 — relire l'inventaire plus longtemps (60 à 120 s), ou ne pas arrêter une machine dont l'état lu est déjà « en destruction ».

## Corrections de l'ordre v2 (liste à part)

- O-1 (point 17) : une étape 0 avant les préalables — `D` neuf, modules copiés de `COMMIT_PRIVE`, empreintes au journal ; retirer le `mkdir "$D" || exit 2` du bloc de location (la garde `.identifiant` / `.creation-incertaine` de `louer` reste).
- O-2 (point 21) : un préalable — les deux mots de Lazar (périmètre de GO-2026-11-04-06 pour la v4 ou extension ; publication de la v4), écrits au journal avec heure et mots ; sans eux, aucune location.
- O-3 (point 18) : préalable 3 — citer la lecture de R-1561 et ce rapport (point 14), garder le contrôle d'empreinte.
- O-4 (point 19) : préalable 6 — admettre l'autre voie du texte, ou dire l'écart voulu.
- O-5 (point 20) : récupération — réservée à la poussée manquée en passant ; « secret trouvé » et jeton échu : la mère décide.

## Fichiers de ce contre-lecteur

- `contre-lecture-courte-v4-v1/couples-contre-lecture-courte-v4-v1.json`, sha256 `67cb27e65bed99e41d102e3a359f0839cbbf85549fb1da91cac9b9e861426570`.
- Bloc-notes (non versés) : `ecrire_couples_clc.py` `c318bfc7…`, `epreuve_clc.py` `fe19e8c2…`, `sections.py`, texte d'épreuve `v4-apres-couples-clc.md` `3696e9c3…`.
