"""Écrit `couples-texte-v4-v1.json` : les couples du rédacteur de la v4, appliqués après les 15 de la contre-lecture complète."""
import json
import sys
from pathlib import Path

N4, TOTAL = int(sys.argv[1]), int(sys.argv[2])  # essais de la v4, et de v1 à v4 ensemble
LANCEUR_V3 = ("`src/controle_ia/hote_durable_a1_v3_v3.py`, `scripts/amorce_hote_durable_a1_v3_v3.sh` et "
              "`tests/test_hote_durable_a1_v3_v3.py`")
LANCEUR_V4 = ("`src/controle_ia/hote_durable_a1_v3_v4.py`, `scripts/amorce_hote_durable_a1_v3_v4.sh` et "
              "`tests/test_hote_durable_a1_v3_v4.py`")
BB = "`bb35e87f0e7825b2225f2ade1177da428f78352e`"
MQ = "<<COMMIT_LANCEUR_DURABLE>>"

TETE = (
    "**Version 4, brouillon 1 — troisième course d'A1-v3, sur hôte durable** (5 novembre 2026 ; rédacteur-développeur des couples "
    "des brouillons 2 et 3 de la v3 et des lanceurs durables v2 à v4, qui n'a écrit ni les textes v1 et v2, ni le texte v3 hors de ces "
    "couples, ni le code v3 ou v3.1, ni les contre-lectures, ni les audits ; heures relevées par `date -u` au rapport "
    "`rapport-redaction-v4-v1.md`). Ce fichier est la v3 scellée (`prereg/preenregistrement-attaque-goodhart-v3-v3.md`, sha256 "
    "`c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa`, commit public `08ad8f35`) avec, et seulement, les "
    "changements de la section 0.8 (une ligne chacun : avant → après ; raison) : les 15 couples de la contre-lecture complète du "
    "texte v3 (`docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/contre-lecture-complete-v1/contre-lecture-complete-texte-v3-v1.md`, "
    "`06d6283d…`, « lançable après couples, version v4 » ; couples `couples-contre-lecture-complete-texte-v3-v1.json`, `16803c05…`), "
    "puis les couples du rédacteur (`couples-texte-v4-v1.json`), appliqués dans l'ordre par script (`appliquer-couples-texte-v4-v1.py`, "
    "sortie `sortie-appliquer-couples-texte-v4-v1.txt`, même dossier du dépôt privé). **Raison** : la v3 scellée garde le marqueur "
    "de l'audit A9 de la seconde course, que le lanceur gelé refuse (« marqueur(s) non rempli(s) » ; contre-lecture complète, B1) ; il "
    "est ici rempli par l'audit rendu (`audit-A9-a1-v3-seconde-course-v1.md`, `a0577b8b…`, section 0.5 bis), avec sa réserve : la "
    "dépense de la seconde course n'est établie que sur le journal du relais, non appariée au registre de dépense de la sortie. "
    "**Aucune course n'a tourné sous la v3** : rien n'a été loué ni lancé (R-1545, R-1553), et le lanceur gelé l'aurait refusée ; la "
    "course de ce texte reste donc la **troisième** (non une quatrième, qui demanderait un GO neuf, section 8) ; **aucune relance de "
    "la v3**. **GO** inchangés : GO-2026-11-04-06 (course, 400 USD) et GO-2026-11-05-03 (machine, 35 USD) ; la lettre du périmètre de "
    "GO-2026-11-04-06 (« texte v3 neuf, contre-lu par un lecteur neuf, scellé, committé et poussé avant la course ») est couverte, pour "
    "la v4, par le mot de Lazar de R-1553 (« A1-v3 complet, puis lancer », relevé avec « texte v4 et nouveau scellement s'il le faut ») "
    "— à confirmer par Lazar avant la course, ou extension du GO (nœud ; contre-lecture complète, point 15) ; la poussée de la v4 sur "
    "le dépôt public de l'organisme est une publication (nœud de Lazar ; R-1539 accordait la v3). **Lanceur durable v4** ("
    + LANCEUR_V4 + ") : il lit ce texte (`NOM_TEXTE` = `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md`) et porte "
    "les corrections 1 à 8 de la contre-lecture complète du lanceur v3 (`contre-lecture-complete-lanceur-v3-v1.md`, `ed4dc27e…`). "
    "**Statut : brouillon 1 de la v4, non scellé ; ses ajouts hors des 15 couples (ce paragraphe, la section 0.8, les couples du "
    "rédacteur) sont à contre-lire, court (section 14) ; un marqueur (annexe B) : le commit du lanceur durable v4, deux fois.** "
    "**Nom de la version scellée : `prereg/preenregistrement-attaque-goodhart-v3-v4.md`** (nom suivant libre, R12). **Scellement** : "
    "après la contre-lecture courte et ses couples, le remplissage du marqueur et le contrôle de la section 13, point 4 (motif du "
    "lanceur cherché par programme ; fichier lu sous son nom scellé par `lire_preenregistrement` du lanceur gelé), par l'écriture, par "
    "le directeur, du compagnon `preenregistrement-attaque-goodhart-v3-v4.md.sha256`, committé et poussé avec ce fichier avant la "
    "course ; **la graine est l'empreinte de ce fichier** : texte neuf, graine neuve, cartes neuves (section 4) ; un scellement, une "
    "course. Dans tout ce qui suit, hors de ce paragraphe, de la section 0.8 et des passages qu'elle nomme, « ce fichier », « ce "
    "texte », « la v3 » et « texte v3 » décrivent la v3 et ses versions antérieures.\n\n")

SECTION_08 = (
    "### 0.8 Changements de la v3 à la v4 (une ligne chacun : avant → après ; raison)\n\n"
    "1. Titre : « …, troisième course sur hôte durable : version 3, brouillon 1 » → « … : version 4, brouillon 1 » ; texte neuf.\n"
    "2. Paragraphe de tête : + paragraphe de la v4 (ce qu'elle est, raison, aucune course sous la v3, aucune relance de la v3, GO et mot de Lazar à confirmer, lanceur v4, statut, un marqueur, nom scellé `…-v4.md`, scellement, graine), placé avant le paragraphe de scellement de la v3, gardé tel quel ; consigne.\n"
    "3. Section 0.5 bis : marqueur AUDIT_A9_SECONDE → l'audit A9 de la seconde rendu (chemin, commits, empreinte `a0577b8b…`, conclusion, cinq points, dépense établie sur le seul journal du relais, non appariée au registre ; réserves) ; contre-lecture complète, couple 1 (B1).\n"
    "4. Section 0.5 bis : coupure « vers 03:46 » par la limite d'usage → session bloquée dès 03:04:53 UTC, processus de travail redémarré à 03:46:39–40, garde arrêtée « worker_restart » ; couple 2 (audit A9, réserves).\n"
    "5. Section 0.5 bis : durée ≈ 1 h 43 → ≈ 1 h 42 ; couple 3.\n"
    "6. Section 12 : même durée ; couple 4.\n"
    "7. Section 0.5 bis : dépense → bornée par un appel en vol, ≈ 50,30 USD au plus ; couple 5.\n"
    "8. Section 0.5 bis : cause « par la limite d'usage de la session » → sous la limite du compte, lien vraisemblable non prouvé ; couple 6.\n"
    "9. Section 0.5 bis : ce que l'audit A9 de la seconde a lu → aucun fichier de l'état scellé (noms et empreintes) ; couple 7.\n"
    "10. Section 13, point 4 : marqueurs de la v1 et de la v2 seuls → + ceux de la v3 (celui resté) et de la v4, contrôle par programme et lecture par le lanceur gelé du fichier final avant le compagnon ; couple 8.\n"
    "11. Section 14 : titre ; couple 9.\n"
    "12. Section 14 : n° 4 « à faire » → rendue (ce qu'elle a lu ; couples du brouillon 3 non contre-lus avant le scellement de la v3, puis par la contre-lecture complète) ; couple 10.\n"
    "13. Section 14 : liste des pièces du n° 4 → le lanceur durable v2, qu'il a lu ; couple 11.\n"
    "14. Section 8 : précaution du crédit d'Argon → + son abandon (R-1543) et son prix ; couple 12.\n"
    "15. Section 8 : + disparition de la machine (rien versé ; ce qui reste à l'audit) ; couple 13.\n"
    "16. Section 8 : poussée finale manquée ou secret trouvé → + perte possible de la sortie et de la dépense, aucune récupération éprouvée ; couple 14.\n"
    "17. Section 13, point 7 quater : + échéance du jeton GitHub postérieure à T0 + 82 h, contrôlée avant la location ; couple 15.\n"
    "18. Section 0.5 bis, « Aucune relance » : v1 et v2 → + la v3 (aucune course sous la v3) ; contre-lecture complète, point 14.\n"
    "19. Section 0.5 bis : « lanceur durable v3, `GO_MACHINE` » → « lanceur durable v4 » ; nom du lanceur (NOM_TEXTE).\n"
    "20. Section 4, « Graines » : empreinte de « ce texte v3 » → de ce texte (v4) ; texte neuf, graine neuve.\n"
    "21. Section 4, commande exacte : « texte scellé v3 » → « texte scellé v4 », `--preenregistrement …-v3.md` → `…-v4.md` ; nom de la version scellée.\n"
    "22. Section 8, « Troisième course (v3) » : lanceur durable v3 au commit `bb35e87f…` → lanceur durable v4 au marqueur COMMIT_LANCEUR_DURABLE, essais rejoués ; raison : B1 (NOM_TEXTE), corrections 1 à 8.\n"
    "23. Section 8, « Préparation » : clone public au commit du texte v3 → v4 ; + `git status --porcelain` relevé de nouveau juste avant la course (correction 5) ; + numpy 2.5.3 vérifié (correction 7) ; contre-lecture complète du lanceur.\n"
    "24. Section 8, « Destruction par identifiant » : + destruction vérifiée par l'inventaire, encore listée → arrêt (correction 2).\n"
    "25. Section 13, point 7 quater : lanceur durable v3 et son commit → v4 et le marqueur ; « texte v3 scellé » → « texte v4 scellé » ; `controler` du lanceur v4 (qui rend 6 sur tout échec de `vastai`, correction 1).\n"
    "26. Section 14 : + contre-lecture courte des ajouts de la v4, à faire ; contre-lecture complète, point 4.\n"
    "27. Annexe B : + version 4 : un marqueur ; marqueurs.\n"
    "28. Section 0.8, neuve : cette liste ; consigne.\n\n")

C = [
    ("titre", "# Préenregistrement — attaque de Goodhart contre le juge statistique, reprise propre d'A1 (course « A1-v3 »), troisième course sur hôte durable : version 3, brouillon 1",
     "# Préenregistrement — attaque de Goodhart contre le juge statistique, reprise propre d'A1 (course « A1-v3 »), troisième course sur hôte durable : version 4, brouillon 1"),
    ("paragraphe de tête de la v4", "**Scellement (5 novembre 2026, 07:35 UTC, heure relevée par `date -u`).**",
     TETE + "**Scellement (5 novembre 2026, 07:35 UTC, heure relevée par `date -u`).**"),
    ("section 0.5 bis, « Aucune relance »", "**Aucune relance de la v1 ni de la\nv2** : chacune a eu sa course",
     "**Aucune relance de la v1, de la v2 ni de la v3** (v4 : aucune course n'a tourné sous la v3, refusée par le lanceur gelé ; rien "
     "loué ni lancé, R-1545, R-1553) ; v1 et\nv2 : chacune a eu sa course"),
    ("section 0.5 bis : nom du lanceur durable", "(lanceur durable v3, `GO_MACHINE`)", "(lanceur durable v4, `GO_MACHINE`)"),
    ("section 0.8, neuve", "## 1. Question et motivation", SECTION_08 + "## 1. Question et motivation"),
    ("section 4, « Graines »", "l'entier de l'empreinte de ce texte v3 :",
     "l'entier de l'empreinte de ce texte (v4 : texte neuf, graine neuve ; la v3, refusée par le lanceur, n'a calculé aucune carte) :"),
    ("section 4, commande exacte : texte", "au commit qui porte le texte scellé v3, descendant du commit de la v3.1",
     "au commit qui porte le texte scellé v4, descendant du commit de la v3.1"),
    ("section 4, commande exacte : nom", "--preenregistrement prereg/preenregistrement-attaque-goodhart-v3-v3.md",
     "--preenregistrement prereg/preenregistrement-attaque-goodhart-v3-v4.md"),
    ("section 8, « Troisième course (v3) » : lanceur durable",
     "Le lanceur durable v3 (" + LANCEUR_V3 + " du dépôt privé, au commit " + BB + ", qui porte aussi la v1, "
     "`src/controle_ia/hote_durable_a1_v3.py`, et la sonde v10, `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` et "
     "`src/controle_ia/sonde_hote_durable_a1_v3.py`, dont la v3 reprend le code ; essais en mode jouet : les 96 de la v3, les 82 de la "
     "v2 et les 49 de la v1 rejoués, 227 passés, additif 1 au rapport `rapport-redaction-v3-v2.md` ; brouillon 2 : la v2 ; brouillon 1 : "
     "la v1 seule, section 9, L18)",
     "Le lanceur durable v4 (" + LANCEUR_V4 + " du dépôt privé, au commit " + MQ + ", qui porte aussi la v1, "
     "`src/controle_ia/hote_durable_a1_v3.py`, et la sonde v10, `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` et "
     "`src/controle_ia/sonde_hote_durable_a1_v3.py`, dont la v4 reprend le code ; il lit ce texte v4 (`NOM_TEXTE`) et porte les "
     "corrections 1 à 8 de la contre-lecture complète du lanceur v3 ; essais en mode jouet : les " + str(N4) + " de la v4, les 96 de la "
     "v3, les 82 de la v2 et les 49 de la v1 rejoués, " + str(TOTAL) + " passés, rapport `rapport-redaction-v4-v1.md` ; v3 : la v3, au "
     "commit `bb35e87f…` ; brouillons 2 et 3 de la v3 : la v2, puis la v3 ; brouillon 1 : la v1 seule, section 9, L18)"),
    ("section 8, « Préparation » : texte v4", "clone public au commit du texte v3, qui doit descendre de `9776ed0`",
     "clone public au commit du texte v4, qui doit descendre de `9776ed0`"),
    ("section 8, « Préparation » : correction 5", "l'empreinte attendue et à son compagnon, `git status --porcelain` vide ; port 8805 libre",
     "l'empreinte attendue et à son compagnon, `git status --porcelain` vide (v4, correction 5 : relevé de nouveau juste avant la "
     "course, écrit au journal, sinon refus) ; port 8805 libre"),
    ("section 8, « Préparation » : correction 7", "sinon rien ne part et la machine est détruite ;",
     "sinon rien ne part et la machine est détruite ; (v4, correction 7) numpy 2.5.3 vérifié de même sous ces chemins, versions au "
     "journal, sinon rien ne part ;"),
    ("section 8, « Destruction par identifiant » : correction 2", "destruction refusée par Vast → arrêt.",
     "destruction refusée par Vast → arrêt (v4, correction 2 : destruction vérifiée par l'inventaire, relu jusqu'à trois fois ; "
     "machine encore listée → arrêt)."),
    ("section 13, point 7 quater : lanceur durable",
     "tenus par le lanceur durable v3 (" + LANCEUR_V3 + " du dépôt privé, avec la v1 et la sonde v10 dont il reprend le code, commit "
     + BB + ",",
     "tenus par le lanceur durable v4 (" + LANCEUR_V4 + " du dépôt privé, avec la v1 et la sonde v10 dont il reprend le code, commit "
     + MQ + ","),
    ("section 13, point 7 quater : texte v4", "Avant la location : texte v3 scellé, committé et poussé",
     "Avant la location : texte v4 scellé, committé et poussé"),
    ("section 13, point 7 quater : `controler`", "(`controler` du lanceur durable v3,",
     "(`controler` du lanceur durable v4, qui rend 6, « recontrôler », sur tout échec de `vastai`,"),
    ("section 14 : contre-lecture courte de la v4", "ceux du rapport de rédaction, section 4.",
     "ceux du rapport de rédaction, section 4.\n\n**Contre-lecture courte des ajouts de la v4, à faire** (R2 ; contre-lecture "
     "complète du texte, point 4) : par un sous-agent neuf qui n'a écrit ni ce brouillon, ni le lanceur durable, ni les "
     "contre-lectures complètes. Objet : les ajouts du rédacteur hors des 15 couples (paragraphe de tête de la v4, section 0.8, couples "
     "`couples-texte-v4-v1.json`) et leur accord avec le lanceur durable v4. Fichiers à lui donner : ce brouillon "
     "(`docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/preenregistrement-attaque-goodhart-v3-v4-brouillon1.md` du dépôt "
     "privé) ; la v3 scellée (`c697d0df…`) et son compagnon ; les deux contre-lectures complètes et les 15 couples ; les couples du "
     "rédacteur, son script et sa sortie ; le rapport `rapport-redaction-v4-v1.md` ; le lanceur durable v4 (trois fichiers) et le "
     "différentiel `diff-lanceur-v3-vers-v4-hors-renommage.txt`. Puis, sur le fichier final, le contrôle de la section 13, point 4."),
    ("annexe B : version 4", "**Version 3, brouillon 1 : deux marqueurs**",
     "**Version 4, brouillon 1 : un marqueur**, COMMIT_LANCEUR_DURABLE, deux fois (section 8, « Troisième course (v3) » ; section 13, "
     "point 7 quater) : rempli par le hash complet du commit de `main` du dépôt privé qui porte le lanceur durable v4 (et la v1, la sonde "
     "v10 et la sonde v1), avec leurs empreintes, après la contre-lecture courte des ajouts de la v4 (section 14) et ses couples ; "
     "AUDIT_A9_SECONDE est rempli (section 0.5 bis) ; vérifié par programme (motif `<<[A-Z0-9_]+>>`, chiffres compris) : il ne "
     "reste que ces deux occurrences ; puis le contrôle de la section 13, point 4, sur le fichier final, avant le compagnon.\n\n"
     "**Version 3, brouillon 1 : deux marqueurs**"),
]
couples = [{"n": i, "lieu": lieu, "ancien": a, "nouveau": b} for i, (lieu, a, b) in enumerate(C, 1)]
doc = {"source": "prereg/preenregistrement-attaque-goodhart-v3-v3.md (dépôt public de l'organisme, commit 08ad8f35)",
       "source_sha256": "c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa",
       "couples_contre_lecture": "contre-lecture-complete-v1/couples-contre-lecture-complete-texte-v3-v1.json",
       "couples_contre_lecture_sha256": "16803c0508830e31eb8bd794c6993e8b924f070a176ea6cf84250479dac710a9",
       "cible": "preenregistrement-attaque-goodhart-v3-v4-brouillon1.md",
       "regle": "les 15 couples de la contre-lecture complète d'abord, dans leur ordre, puis ceux-ci, dans l'ordre ; chaque « ancien » "
                "présent une seule fois au moment de son application ; rien d'autre ne change ; citation du périmètre de "
                "GO-2026-11-04-06 intacte ; seul marqueur restant : COMMIT_LANCEUR_DURABLE, deux fois",
       "couples": couples}
Path(sys.argv[3]).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
print(len(couples), "couples écrits")
