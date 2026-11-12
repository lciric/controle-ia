# Contre-lecture complète du texte — préenregistrement A1-v3, version 3 scellée (R2, lecteur neuf)

Contre-lecteur neuf : je n'ai écrit ni le texte (v1, v2, v3 et leurs brouillons), ni le code v3 ou v3.1, ni le lanceur durable, ni
les sondes, ni aucune contre-lecture ou audit précédent. 5 novembre 2026, de 09:36:59 UTC à la remise (heures relevées par `date -u`).
Consigne : `consigne-contre-lecture-complete-texte-v3-v1.md`, sha256 `f03f78df69b7abbb4b99d0d45aff1de179b7e5ea8aa5276290e51f9a8758b983`
(compagnon égal). Interdits tenus : aucun commit, aucun `.sha256` rendu, aucun fichier existant modifié, rien sous `donnees/` ni
`/home/claude/coffre-*`, aucun réseau, aucune location, aucune clé lue, aucune dépense ; commandes sous `timeout 600 nice -n 10`,
épreuves en `python3 -I -B` sur des copies du bloc-notes, hors de tout dépôt.

**Verdict : lançable après couples, version v4 du texte.**
La v3 scellée (`c697d0df…`) n'est pas lançable : elle garde le marqueur `<<AUDIT_A9_SECONDE>>`, que le lanceur gelé refuse (B1, éprouvé).
La v4 = la v3 + les 15 couples joints (éprouvée : acceptée par le lanceur gelé), plus un lanceur durable v4 qui nomme `…-v4.md` et le mot de Lazar sur « texte v3 » du périmètre de GO-2026-11-04-06 ; aucun autre bloquant.

## Pièces lues et empreintes vérifiées

- Texte scellé v3 : `/home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md`, sha256
  `c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa` (recalculé ; égal au compagnon et à la consigne ; 2 153 lignes,
  296 390 octets ; commit public `08ad8f35`) — **lu en entier** : tête, sections 0 à 14, annexes A et B, empreintes.
- v2 scellée, même dossier : `2a29f59353ce776f92d17799de25f8b75741f1c60dcc5edfbc427bf0ae3a8bb1` (compagnon égal) ; différence complète
  v2 → v3 relue bloc par bloc.
- Brouillons 1 à 3 de la v3 (`6e65136a…`, `86ad379b…`, `a92166b8…`), couples `couples-brouillon2-v3-v1.json` (`e1be43e2…`),
  `contre-lecture-n4-v1/couples-contre-lecture-n4-v1.json` (`462a8ea2…`), `couples-brouillon3-v3-v1.json` (`2e0f742a…`) : compagnons
  égaux ; contre-lecture n° 4 (`b524b41c…`) et sa consigne (`d1322529…`) ; rapports `rapport-redaction-v3-v2.md` (sections 2 à 8) et
  son additif 1 ; audit A9 de la seconde course `audit-A9-a1-v3-seconde-course-v1.md` (`a0577b8b…`, compagnon égal), en entier.
- Registres du dépôt privé (lecture seule) : `registres/go.md` (lignes 242 à 253) ; `registres/decisions.md` (R-1463, R-1471, R-1478,
  R-1511, R-1527, R-1533, R-1534, R-1538 à R-1554) ; `registres/depenses.md` (rien sous GO-2026-11-04-06, -04-09 ni -05-03).
- Lanceur durable v3 au commit `bb35e87f` : `src/controle_ia/hote_durable_a1_v3_v3.py` `916a3c85…`, `scripts/amorce_hote_durable_a1_v3_v3.sh`
  `e37bfde5…`, `tests/test_hote_durable_a1_v3_v3.py` `2f7e9291…` (égaux au commit, à l'arbre et aux compagnons) ; lu aux seuls passages
  que le texte décrit (ordre des contrôles sur la machine, `louer`, `NOM_TEXTE`, chemins, numpy) — la confrontation complète est celle
  du second lecteur. Ordre `docs/procedures/ordre-fille-a1-v3-troisieme-course-v1.md` : recherche de mots seulement.

## Épreuves (bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl/`, hors dépôt)

- Arbre `git archive 08ad8f35 orchestrator` ; les 73 fichiers du bloc `empreintes-du-code` y sont ceux de `9776ed0` (`git diff --stat
  9776ed0 08ad8f35` vide sur ces 73 chemins ; `9776ed0` ancêtre de `08ad8f35`).
- `scripts/epreuve_marqueur.py` (`940cab64…`) : texte v3 et son compagnon réel → `verifier_scelle` vrai, puis **« REFUS
  PreenregistrementRefuse marqueur(s) non rempli(s) : ['<<AUDIT_A9_SECONDE>>'] »**.
- `scripts/epreuve_v4_simulee.py` (`d0b6c387…`) : même texte, marqueur remplacé par un texte quelconque, renommé `…-v4.md`, compagnon
  factice → **accepté** (73 empreintes ; plan : GO-2026-11-04-06, 400 USD, 259 200 s, « aucun », Argon un fil, configuration
  `e5306c47…`, devis maximum 190,46 USD).
- `scripts/epreuve_go.py` (`819678d0…`) : `verifier_go_v55` gelé, GO-2026-11-04-06 à 400 USD : registre du canal à `740f49e2` accepté
  le 5 et le 18 novembre, refusé le 19 (validité) ; registre de `main` à `a364e947` refusé (« identifiant GO-2026-10-24-07 en
  double ») ; ligne 244 de `main` = ligne 82 du canal à `740f49e2` et à `0aa04b5c`, à l'octet ; canal : 74 identifiants, aucun
  doublon ; `main` : 17 doublons (les seize de la v2 et GO-2026-11-04-04) — comme le texte l'écrit (section 4).
- `scripts/rejouer_couples.py` (`eeb43c21…`) : brouillon 1 + 10 couples = brouillon 2 (`86ad379b…`) ; brouillon 2 + 9 + 10 couples =
  brouillon 3 (`a92166b8…`), à l'octet ; brouillon 3 → v3 : le paragraphe de scellement et deux `<<COMMIT_LANCEUR_DURABLE>>` remplacés,
  rien d'autre (`diff`).
- `scripts/hunks_sections.py` (`a1a94969…`) : les 24 blocs du diff v2 → v3 rattachés à leur section (question 4).
- `scripts/ecrire_couples.py` (`7d8837d4…`) et `scripts/epreuve_couples.py` (`629dd448…`) : les 15 couples, chacun présent une fois
  dans la v3 et au moment de son application, appliqués dans l'ordre → texte de sha256
  `9851ed9f3b579358885b630ef947333e7973c906de6a84e9adeba9ceba67b738` (2 200 lignes) : aucun jeton au motif du lanceur ; blocs
  `plan-gele` et `empreintes-du-code` inchangés à l'octet ; renommé `…-v4.md` dans l'arbre extrait, compagnon factice :
  **accepté** par `lire_preenregistrement` (GO-2026-11-04-06, 400 USD, 259 200 s, « aucun », entropie ≥ 2⁶⁴) ; copie retirée ensuite.

## Points (gravité : bloquant / à corriger / note)

### Bloquant

- **B1 — bloquant (questions 1, 2 et 6) : le texte scellé garde le marqueur `<<AUDIT_A9_SECONDE>>` (ligne 533, section 0.5 bis) ; le lanceur gelé refuse donc ce texte.** Le paragraphe de scellement (ligne 3) dit « brouillon 3 … avec, et seulement : le marqueur du commit du lanceur durable remplacé (deux fois) » ; or la règle de scellement du texte lui-même (lignes 25 et 26) exige « le remplissage des deux marqueurs », l'annexe B (lignes 2061 à 2066) en annonce deux, et R-1543 décrit le texte comme « brouillon 3 + commit du lanceur rempli + paragraphe de scellement ». Le motif gelé `<<[A-Z0-9_]+>>` (`demonstrations/attaque_goodhart_v3.py:97`) le voit et `lire_preenregistrement` refuse (`:271-273`) : épreuve ci-dessus. Sur l'hôte durable v3 l'ordre est : GO, registre, signe de vie poussé, sources, clone public, relais lancé, puis `--verifier-seulement` exigé en code 0 (`hote_durable_a1_v3.py:689-694`, hérité ; appelé `hote_durable_a1_v3_v3.py:647`) : la machine aurait été louée, la branche du signe de vie prise (R12), et rien ne serait parti (aucune dépense d'Argon). La section 0.5 bis le dit (ligne 536 : « Tant que ce marqueur reste, le lanceur refuse ce texte »). Aucune étape ne l'a arrêté : le n° 4 ne recevait pas l'audit A9 de la seconde course (sa consigne, `d1322529…`) et laissait les marqueurs au scellement, et le scellement n'a pas fait lire le fichier final par le lanceur gelé (point 1). **Levée** : version v4 (nom neuf, R12 ; texte neuf, graine neuve), marqueur rempli par l'audit A9 de la seconde course, rendu (R-1478) : `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/audit-A9-a1-v3-seconde-course-v1.md`, sha256 `a0577b8b0c6e0487b090d064f0872034f66024357ece95d2b14152b130e90a41` (compagnon égal), fichier entré par l'instantané `c0243d37`, compagnon par `cbaf76a9496aa90bf23a57e5926be08878fb95bd` (« R-1478 : audit A9 de la seconde course d'A1-v3 »), qui porte les deux et descend dans `main` (vérifié par `git show`) ; conclusion « cause d'infrastructure établie » — couple 1. **Conséquence hors du texte** : le lanceur durable fige le nom du texte (`NOM_TEXTE = "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md"`, `src/controle_ia/hote_durable_a1_v3.py:56`, repris par la v3) : une v4 (`…-v4.md`, nom suivant libre) demande un lanceur durable v4 (noms neufs, R12, essais rejoués), que la v4 du texte doit nommer (tête, 0.5 bis l. 572, section 8 « Troisième course (v3) », 13 point 7 quater, 14) — couples à écrire quand ce commit existera, non joints.

### Question 1 — cohérence interne du texte entier

1. À corriger (couple 8) — section 13, point 4, « **Marqueurs (aucun ne reste)** », n'a pas été mis à jour pour la v3 : il ne nomme que les marqueurs de la v1 et de la v2, alors que l'annexe B en annonce deux pour la v3 ; aucune étape de la section 13 n'exige, sur le fichier final, la recherche des marqueurs au motif du lanceur et sa lecture par `lire_preenregistrement` avant l'écriture du compagnon — l'étape qui aurait arrêté B1.
2. À corriger (couples 2 à 7) — section 0.5 bis, faits de la seconde course non alignés sur l'audit A9 rendu (ses réserves R3, R4, R7 ; R-1478 : « à reporter dans la section 0.5 bis ») : limite d'usage bloquante dès 03:04:53 UTC (texte : « vers 03:46 ») ; 03:46:39–40 = redémarrage du processus de travail, garde arrêtée « worker_restart » (absent) ; ≈ 1 h 42 (texte : 1 h 43, aussi en section 12) ; lien limite → redémarrage vraisemblable, non prouvé (le texte l'affirme) ; dépense 48,49583 à ≈ 50,30 USD avec un appel en vol (texte : 48,49583) ; « son audit A9 ne lit que ce que l'audit A9 de la première a lu (journaux, registre de dépense, manifeste de départ) » : l'audit n'a lu aucun fichier de l'état scellé (noms et empreintes seulement).
3. À corriger (couple 1) — les cinq points que le texte assigne à l'audit comprennent « dépense appariée au registre » ; l'audit l'établit sur le journal du relais seulement, non appariée au registre de dépense de la sortie (lecture interdite par sa consigne ; audit, section 6, point 3) : la v4 l'écrit en remplissant le marqueur ; ce n'est pas une condition d'admission (la règle de la section 8 demande la cause), c'est une réserve (R4).
4. À corriger (couples 9 à 11) — section 14 : le n° 4 y est encore « à faire » ; sa liste de pièces dit « ce brouillon (`…-brouillon1.md`) » et « le lanceur durable v3 … et son additif 1 », alors que le n° 4 a lu le brouillon 2 et le lanceur durable v2 (son titre, sa consigne ; le couple 9 du brouillon 3 a réécrit la liste après coup) ; les 10 couples du rédacteur appliqués au brouillon 3 (C1 à C3 du code, noms v2 → v3) n'ont été contre-lus par personne avant le scellement (R2 non tenue pour eux ; R-1543 dit « R2 tenue ») — ils le sont par cette lecture et par la lecture parallèle du lanceur ; pour la v4, ce que le rédacteur ajoutera hors de ces couples (tête, section 0.8, lanceur v4) demande une contre-lecture courte avant le scellement.
5. Note — section 8, « Création » : la puce garde « **aucune carte** (`num_gpus` = 0) » et le préambule dit « ces critères remplacent “aucune carte (`num_gpus` = 0)” dans la liste ci-dessous » : juste par la phrase de remplacement, contradictoire à la lecture ; « 8 Go de mémoire » (liste) et « au moins 8 000 Mo de mémoire » (préambule) sont le même critère, la mémoire vive (`cpu_ram ≥ 8 000 Mo` dans `louer`) ; la v4 gagnerait à écrire l'offre une fois.
6. Note — section 8, « Plafonds de la machine » : « 80 h de vie et 32 USD (0,40 USD × 80 h) » ; sections 12 et 13 : « au plus 32,57 USD (minuterie : création + 10 min + 80 h + 1 h, plus 15 min) » : les deux sont vrais (80 h et 32 USD = garde de l'hôte qui arrête la course ; 32,57 USD = borne de la minuterie de destruction ; rapport `rapport-redaction-v3-v2.md`, section 2, (C)), mais le texte ne relie jamais les deux, et « 80 h de vie » est inexact (la machine vit jusqu'à ≈ 81 h 25).
7. Note — section 0.5 bis : « la session qui lance (la fille) ne fait que louer, puis n'a plus de rôle » contredit le point 7 quater (contrôles du pilote à T0 + 40 min et après l'échéance finale ; inventaire R14) ; le couple 9 du n° 4 n'a corrigé que le point 7 quater.
8. Note — renvois faux : section 0.7, point 23, « sections 4, 8, 13 point 7 quater et 14 » : le renommage dit « section 4 » est en section 0.5 bis (ligne 572 ; le couple 3 du brouillon 3 le dit « section 4 (ligne 570) ») ; la phrase « Brouillon 3 » de la tête omet 0.5 bis. Les autres renvois neufs que j'ai suivis (0.5 bis, 0.7, 4 « GO » et « Registre », 8 « Troisième course (v3) », 9 L18, 11, 12, 13 points 3, 7, 7 quater et 9, 14, annexe B, rapport v3-v2 section 2 (C) et section 5 conduite (b), audit A9 de la première sections 2 et 8, R-1463, R-1471, R-1511, R-1527, R-1533, R-1534, R-1538 à R-1541) existent et disent ce qui est cité.
9. Note — section 4, « GO » : sous la convention de la tête, la puce commence par « **GO-2026-11-03-01** (bloc `plan-gele`) » alors que le bloc porte GO-2026-11-04-06 (dit plus bas, « Troisième course (v3) ») ; de même pour le registre hors du clone et le dossier de sortie (chemins de la v2 d'abord) : juste par la convention, trompeur pour un lecteur. Titre « version 3, brouillon 1 » d'un texte scellé : convention de la v2 (n° 4, point 6), sans effet.
10. Note (conforme) — hypothèses, prédictions, métriques, seuils, plan d'analyse, critères gelés (ordre 2, 6, 1, 3, 4, 5), audits A1 à A9 et liste d'arrêt : chacun défini une fois (sections 2, 3, 5, 6, 7, 8), sans contradiction entre sections ; table des comptes à u unités jouées recoupée par sondage de Wilson (0/11 → 0,2588 ; 0/12 → 0,2425 ; 1/19 → 0,2464 ; 1/18 → 0,2576 ; 3/20 → 0,0524 ; 3/21 → 0,0498 ; 2/11 → 0,0514 ; 1/4 → 0,0456 ; 1/3 → 0,0615), cohérente avec « sous 19 », « sous 21 », « de 4 à 11 », « de 1 à 3 ».

### Question 2 — prédictions et critères

11. Note (conforme) — P1 à P6 reconduites de T sans changement, avec signe attendu, seuils en comptes à u unités jouées et valeurs d'A1 « pour information » ; « réplication à valeurs antérieures connues » déclarée ; issues ouvertes dans les deux sens (brèche, bras perdu, sans dents, résiste, instrument, précision) ; aucune course ne vise un signe (R3).
12. Note (conforme, R7) — aucun chiffre de l'état de l'art ; chiffres d'A1 renvoyés à A, V et AD par section et empreinte ; ceux de la seconde course au rapport de la fille et à l'audit ; le chemin du 402 est dit « non relu » sur la commande.
13. À corriger (couple 1) — la règle de lecture des trois courses est écrite d'avance (0.5 bis ; 13, point 9), mais la règle qui **admet** la troisième (« cause d'infrastructure établie par l'audit A9 ») n'est pas écrite dans le texte scellé : sa citation est le marqueur (B1).
14. À corriger (tête de la v4, non jointe) — la v4 doit dire qu'aucune course n'a tourné sous la v3 (rien loué ni lancé : R-1545, R-1553 ; la v3 est refusée par le lanceur), donc que sa course est encore la troisième (non une quatrième, qui demanderait un GO neuf, section 8), et ajouter « aucune relance de la v3 ».
15. À corriger (procédure, nœud de Lazar) — GO-2026-11-04-06 (ligne 244) et GO-2026-11-05-04 (ligne 252) disent « texte v3 neuf, contre-lu …, scellé, committé et poussé avant la course » : une v4 sort de la lettre du périmètre ; ni le lanceur gelé ni le lanceur durable ne lisent le périmètre ; la v4 cite le mot de Lazar qui la couvre (R-1553, « A1-v3 complet, puis lancer », relayé avec « texte v4 … s'il le faut ») ou une extension du GO. De même, la poussée de la v4 sur le dépôt public de l'organisme est une publication (nœud de Lazar) : R-1539 accordait « push v3 ». Les trois GO échoient le 2026-11-18 (vérifiés une fois, au départ).
16. Note — section 12, « pour information » : ≈ 0,078 USD par appel de la seconde course (48,49583 / 620) compte les 5 échecs (au pire cas réservé, ≈ 1,6 USD chacun, si la table de la section 4 vaut pour eux) et se compare au 0,062 USD d'A1, calculé sans l'échec ((34,35943 − 1,61417)/526) : pas à périmètre égal ; sans effet sur le plan.

### Question 3 — ce qui peut fausser la course ou sa lecture

17. Note (conforme) — instrument : Argon seul, relais 8805 à un fil (410 USD, 9 000 appels, aucune reprise), code `9776ed0` (73 empreintes égales sur `08ad8f35`), configuration `e5306c47…` (absente de ce conteneur, vérifié par empreinte sur tout le disque, R11), plan gelé accepté par le lanceur gelé ; interpréteur 3.13 (C1) ; numpy installé en 2.5.3 par l'amorce s'il manque, version écrite au journal et au manifeste ; graine neuve à la v4 (celle de la v3, publique depuis 07:35 UTC, n'a servi à rien : aucune carte calculée, L18).
18. Note (conforme) — plafonds : 400 USD (la garde du registre mord la première, ≈ 398,39 USD réglés) ; relais 410 USD et 9 000 appels (≥ 400 et ≥ 8 000 exigés, section 13, point 7 (a) : 6 144 + 247 + 1 584 = 7 975) ; 72 h (≥ 35,78 h) ; garde de l'hôte 80 h et 32 USD ; minuterie 32,57 USD sous GO-2026-11-05-03 (35 USD : il reste 2,43 USD pour tout autre usage de ce GO, sonde ou location manquée, ce que le texte ne dit pas). Chiffres des sections 4, 8 et 12 recalculés, exacts : 17,76 USD par tentative perdue et ≈ 33,9 USD par heure de panne de l'interface ; marges de 22,4 / 18,8 / 15,1 / 11,7 tentatives, soit 11,8 / 9,8 / 7,9 / 6,1 h ; ≈ 12 h de 402 au plus, ≈ 5 USD de machine ; 206 / 166 / 129 appels en échec intermittent ; 223 / 186 / 150 / 117 appels muets ; 144 et 148 appels au délai ; devis 65,35 USD, 2,23 + 1,65 = 3,88 h, 380,93 USD et 2 151 appels aux taux doublé et triplé ; marges de durée 68,12 / 46,88 / 36,22 h.
19. Note (conforme) — codes 2 à 6, commande muette, 402 et 429 : table de la section 4, règles, choix (e), section 8 et section 12 concordent ; 402 de l'interface → code 3 au pire cas (déduit de n° 294, déclaré non relu) ; si le relais rendait ce 402 comme son propre HTTP 402, la commande sortirait en code 4 et la course s'arrêterait aussitôt (« refus_de_budget ») : deux arrêts d'infrastructure sans résultat, sous la même règle.
20. À corriger (couple 13) — **disparition de la machine** (hôte de Vast perdu, instance détruite par un tiers) : rien n'est versé, car manifeste, registre de dépense, journaux et relevés de la garde ne vivent que sur la machine ; le texte dit seulement « une mort brutale perd les réponses en mémoire, comme en v2 », alors qu'en v2 le disque survivait : la dépense d'Argon n'est alors connue que par la facturation du fournisseur (≤ 400 USD), la machine par celle de Vast (≤ 32,57 USD), et l'audit A9 n'a que la branche du signe de vie, le journal de la location et l'inventaire de Vast — à écrire.
21. À corriger (couple 14) — **poussée finale manquée ou secret trouvé** : « la machine s'arrête … données gardées sur son disque, et la session qui reprend décide » ; aucune voie de récupération n'est éprouvée (point d'entrée = amorce, sans coquille ; `vastai copy` non éprouvé, R-1549 ; jeton non remplaçable sur la machine, R-1551) ; C3 ne sauve qu'une panne passagère suivie d'une relance : une telle fin peut perdre la sortie et sa dépense — à déclarer (R4).
22. À corriger (couple 15) — **échéance du jeton GitHub** absente du texte, alors qu'elle a arrêté le départ (R-1545) et qu'un jeton échu rend le versement final impossible : contrôle à écrire avant la location (7 quater : échéance après T0 + 82 h, lue sans l'afficher ; sinon rien n'est loué) ; R-1554 à R-1558 : les sessions neuves voient encore l'ancien jeton (échéance 10:00:36 UTC).
23. Note — plus aucune alerte en direct : l'« alerte écrite d'avance » du point 7 devient une lecture d'après coup par l'audit A9 (7 quater) ; une cause durable (402, clé révoquée, quota quotidien) va jusqu'à l'arrêt au plafond (≤ ≈ 12 h, sans résultat) sans décision de Lazar ; dit par morceaux (section 8, 402 ; 7 quater), cohérent avec « l'hôte n'envoie aucun message ».
24. Note — reprise et versement : C3 (copie de nom neuf), signe de vie exigé (C2), destruction par identifiant, branches neuves (R12) et « sortie scellée avant lecture » sont écrits et cohérents ; ce qui est rapporté si la course meurt est écrit pour la reprise du conteneur (état versé sur `…-troisieme-interrompue-v1`), non pour la disparition (point 20).

### Question 4 — écart à la v2 scellée

25. Note (conforme) — différence complète v2 → v3 : 24 blocs, tous dans des sections que la section 0.7 et le paragraphe de scellement nomment (tête, 0.4, 0.5 bis, 0.7, section 4 dont la ligne `go:` du bloc `plan-gele` et ses notes, sections 8, 9 L18, 11, 12, 13, 14, annexe B, empreintes) ; aucun dans les sections 1, 2, 3, 5, 6, 7 et 10 ; blocs `empreintes-du-code` et `plan-gele` (hors `go:`) inchangés ; chaîne des brouillons et passage brouillon 3 → v3 rejoués à l'octet.
26. Note — seuls écarts de déclaration : les renvois du point 8 ; et le paragraphe de scellement, juste dans ce qu'il dit, tait le second marqueur (B1).

### Question 5 — risques déclarés

27. Note (conforme) — clé d'Argon : métadonnées de la machine chez Vast, clé d'instance qui voit tout le compte (R-1533), exploitant de la machine, transcription d'une session (R-1540), usure du crédit commun ; conduite écrite (nom de variable, jamais affichée, rotation après la course, risque au rapport de la course).
28. Note (conforme) — jeton GitHub : exposition à l'exploitant et écriture possible sur `main` (dont `registres/go.md`, lu par les gardes) déclarées, rotation après la course ; manque l'échéance (point 22).
29. À corriger (couple 12) — crédit d'Argon : le texte écrit une précaution (Lazar confirme au moins 400 USD ou une recharge automatique, la fille l'écrit au journal), absente de l'ordre de la fille (recherche de « crédit », « solde », « 402 » : rien) et abandonnée par R-1543 (« risque accepté pour aller vite ») ; texte, ordre et registre doivent dire la même chose, avec le prix : un solde épuisé en cours de course perd, sans résultat, tout ce qui a été dépensé avant le premier 402 (jusqu'à ≈ 131 USD à l'attendu haut du code).
30. Note (recommandation) — la seconde course avait fait un appel d'Argon de contrôle sur un relais temporaire distinct (port 8815, code 0, 0,00064 USD, hors course) ; la v3 n'en fait aucun sur la machine (« réglages relevés … aucune dépense ») : un tel appel, avant la course, arrêterait pour quelques centimes un solde nul, une clé révoquée ou un interpréteur défaillant (il ne prouve pas un crédit de 400 USD) ; à porter, si le directeur le retient, par le lanceur durable v4, qui est de toute façon à écrire.
31. Note — interpréteur Python : C1 écrit et cohérent (3.13 par chemin absolu, lien de `/usr/bin/python3`, versions au journal, sinon rien ne part) ; le texte affirme que la configuration gelée écrit `/usr/bin/python3` pour la commande d'Argon, ce que le rédacteur n'a pas relu (additif 1, section 6, point 2) et que je ne peux pas relire (configuration absente) : les deux cas sont couverts par C1.
32. Note — versement : épreuve « partie de `main` » contre GitHub déclarée réussie (07:31:40 UTC, `19d2b119`) — non vérifiable ici (branche et objet absents des références locales, aucun réseau) ; échecs : points 21 et 22.

### Question 6 — autre point pour une course à 400 USD au plus

33. Bloquant — B1 (ci-dessus), avec ses deux suites hors du texte : lanceur durable v4 (`NOM_TEXTE`) et mot de Lazar sur le périmètre (point 15).
34. Note — intégrité des sorties sur une machine tierce : l'exploitant, déclaré maître du disque et de la mémoire pour les secrets, l'est aussi des sorties avant leur scellement sur la machine ; non exclu, non déclaré ; réserve à écrire au rapport de la course (R4).

## Couples (`couples-contre-lecture-complete-texte-v3-v1.json`, 15, dans cet ordre ; chaque « ancien » présent une fois dans la v3 scellée et au moment de son application ; épreuve ci-dessus)

1. Section 0.5 bis : marqueur `<<AUDIT_A9_SECONDE>>` et ses quatre lignes → chemin, commits, empreinte, conclusion de l'audit A9 rendu, ses cinq points (dont la dépense non appariée au registre) et ses réserves (B1 ; points 3 et 13).
2. Section 0.5 bis : « coupée par la limite d'usage … vers 03:46 » → bloquée dès 03:04:53, redémarrage du processus de travail à 03:46:39–40, garde arrêtée « worker_restart » (point 2).
3. Section 0.5 bis : durée « ≈ 1 h 43 » → « ≈ 1 h 42 » (point 2).
4. Section 12 : même chiffre (point 2).
5. Section 0.5 bis : dépense bornée par un appel en vol, ≈ 50,30 USD au plus (point 2).
6. Section 0.5 bis : cause « par la limite d'usage de la session » → sous la limite du compte, lien vraisemblable non prouvé (point 2).
7. Section 0.5 bis : ce que l'audit A9 de la seconde a lu (point 2).
8. Section 13, point 4 : marqueurs de la v3, celui resté, contrôle par programme et lecture par le lanceur gelé du fichier final avant le compagnon (point 1).
9. Section 14 : titre (point 4).
10. Section 14 : n° 4 rendu, ce qu'il a lu, couples du brouillon 3 non contre-lus, contre-lecture complète (point 4).
11. Section 14 : liste de pièces du n° 4, lanceur durable v2 (point 4).
12. Section 8 : précaution du crédit d'Argon, son abandon (R-1543) et son prix (point 29).
13. Section 8 : disparition de la machine (point 20).
14. Section 8 : poussée finale manquée ou secret trouvé (point 21).
15. Section 13, point 7 quater : échéance du jeton GitHub (point 22).

Restent au rédacteur de la v4, hors de ces couples (ils dépendent du commit du lanceur durable v4, ou sont l'en-tête d'une version) :
paragraphe de tête de la v4 et section 0.8 (avant → après ; raison : B1 et cette contre-lecture) ; nom `…-v4.md` dans la commande
exacte (section 4) ; « texte v3 » là où il désigne le texte de la course (section 4, commande exacte ; section 8, « Préparation » ;
section 13, point 7 quater) ; noms, essais et commit du lanceur durable v4 (tête, 0.5 bis l. 572, section 8, 13 point 7 quater, 14) ;
les points 14 et 15 ; à sa discrétion, les notes 5 à 9 et la recommandation 30. Ce qu'il ajoute ainsi demande une contre-lecture
courte avant le scellement (point 4), puis le contrôle du couple 8 sur le fichier final.

## Non vérifié

La configuration gelée (`e5306c47…`), la commande d'Argon (`221df610…`), le registre de dépense (`8ba92066…`) et le collisionneur
(`c9725f02…`) sont absents de ce conteneur (recherche par empreinte sur tout le disque : seules des copies factices d'essais) ; la
branche et le commit de l'épreuve du versement, le rapport de la sonde v10 et les états scellés des deux premières courses ne sont pas
dans les références locales ; aucun réseau. Le chemin d'un 402 et la forme exacte de la commande d'Argon viennent donc du texte et de
n° 294.
