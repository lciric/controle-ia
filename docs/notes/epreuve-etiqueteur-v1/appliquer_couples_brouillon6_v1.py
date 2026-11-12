#!/usr/bin/env python3
"""Brouillon 6 de l'épreuve de l'étiqueteur : brouillon 5, plus les 11 couples de la contre-lecture bornée du delta du
brouillon 5, plus les compléments qu'exige `lire_items_phase1_v4.py` ; appliqués, comptés et journalisés (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 et 8 novembre 2026. Fonctions d'application reprises
de `appliquer_couples_brouillon4_v1.py` (import, inchangé) ; mêmes règles.

Usage :
    python -I -B appliquer_couples_brouillon6_v1.py --heure-fin HH:MM:SS
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import appliquer_couples_brouillon4_v1 as b4  # noqa: E402
import appliquer_couples_brouillon5_v1 as b5  # noqa: E402  (texte des pièces du brouillon 5)

BROUILLON5 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon5.md"
COUPLES = ICI / "couples-contre-lecture-delta-brouillon5-v1.json"
BROUILLON6 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon6.md"
JOURNAL = ICI / "journal-couples-brouillon6-v1.json"
EMPREINTE_BROUILLON5 = "f66a3e9d5a64e021b20db747dd8bd02e905523a2d0c9981c2a6fa4a649af3ea7"
EMPREINTE_COUPLES = "bc3f2926829db0dafca48cd2a6ed70a9d9504e6ef555ed5ec3ae0ba82f6c1e82"
Arret, h = b4.Arret, b4.h


def pieces_b5() -> str:
    for c in b5.complements("00:00:00", "## Annexe C — empreintes au rendu (sans contenu de clé)\n## Annexe D", ""):
        if c["id"] == "C5-07":
            return c["nouveau"]
    raise Arret("pièces du brouillon 5 introuvables")


def annexe_c(heure_fin: str, texte: str) -> str:
    q = texte.split("<!-- debut-question-fermee -->", 1)[1].split("<!-- fin-question-fermee -->", 1)[0]
    lignes = [f"Pièces, le 8 novembre 2026 à {heure_fin} (temps universel) ; ce texte-ci et le journal des couples ne "
              "peuvent contenir leur propre empreinte : le journal donne celle de ce texte, la session mère calcule celle "
              "du journal.", "", "| fichier | empreinte | statut |", "|---|---|---|"]
    for f, statut in (("generer_items_v2.py", "en vigueur"), ("test_generer_items_v2.py", "en vigueur, 24 essais"),
                      ("lire_items_phase1_v4.py", "en vigueur"), ("test_lire_items_phase1_v4.py", "en vigueur, 79 essais"),
                      ("analyser_phase1_v3.py", "en vigueur"), ("test_analyser_phase1_v3.py", "en vigueur, 12 essais"),
                      ("epreuve_phases_v1.py", "en vigueur"), ("test_epreuve_phases_v1.py", "en vigueur, 6 essais"),
                      ("test_demonstrations_contre_lecture_v2.py", "6 démonstrations, contre les versions 2"),
                      ("devis-epreuve-etiqueteur-v4.md", "en vigueur"), ("devis_phase1_v3.py", "script du devis"),
                      ("appliquer_couples_brouillon6_v1.py", "ce script"),
                      ("appliquer_couples_brouillon5_v1.py", "repris par ce script"),
                      ("appliquer_couples_brouillon4_v1.py", "fonctions reprises par ce script"),
                      ("lire_items_phase1_v3.py", "remplacée, intacte"),
                      ("preenregistrement-epreuve-etiqueteur-v1-brouillon5.md", "brouillon relu par la contre-lecture bornée"),
                      ("contre-lecture-delta-brouillon5-v1.md", "rapport de la contre-lecture bornée du delta du brouillon 5"),
                      ("couples-contre-lecture-delta-brouillon5-v1.json", "11 couples appliqués"),
                      ("guide-annotation-v1.md", "inchangé")):
        lignes.append(f"| `{f}` | `{h(ICI / f)}` | {statut} |")
    lignes.append(f"| bloc de la question fermée (entre les marqueurs ; identique aux brouillons 1 à 5) | "
                  f"`{hashlib.sha256(q.encode('utf-8')).hexdigest()}` | inchangé |")
    lignes.append("| texte de la question rendu par `extraire_question`, sans la clôture de code (champ `question` du "
                  "manifeste de lecture) | `eea2687531fccdb903092f2fa7511db86debdbea5977b6fdacd86d89723220b4` | inchangé |")
    lignes += ["",
               f"**Essais** : 127 passés à {heure_fin} en environnement vidé (`env -i`) : les 121 des versions en vigueur "
               "(dont 57 scénarios à fausse clé) et les 6 démonstrations de la contre-lecture 1 ; les jeux des versions "
               "remplacées passent toujours contre leurs versions intactes.", "",
               "**Prix d'Argon** : toujours à vérifier (`ai.google.dev` hors du réseau permis de cette session) ; contrôle "
               "en deux temps, dont la facture de l'essai de format, à l'ordre des opérations.", "",
               "**Interdits tenus** : aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni "
               "`docs/notes/bras-attaque/` ; aucune clé lue (seules des valeurs factices posées par les essais) ; aucun "
               "appel payant ; aucun contact, aucune publication ; aucun module du programme importé ; aucun commit, "
               "aucune poussée, aucun fichier d'empreinte compagnon ; versions antérieures, brouillons 1 à 5, "
               "contre-lectures et leurs pièces non modifiés."]
    return "\n".join(lignes)


def complements(heure_fin: str, texte: str, couples: dict) -> list:
    debut_c = texte.index("## Annexe C — empreintes au rendu (sans contenu de clé)")
    fin_c = texte.index("## Annexe D")
    cd503, cd511, cd510 = couples["CD5-03"]["nouveau"], couples["CD5-11"]["nouveau"], couples["CD5-10"]["nouveau"]
    assert cd511.endswith(" |")
    return [
        {"id": "C6-01", "motif": "titre", "ancien": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 5",
         "nouveau": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 6"},
        {"id": "C6-02", "motif": "rédacteur",
         "ancien": "j'ai écrit les brouillons 1 à 4 de ce texte et les scripts qu'il cite ; je n'ai écrit ni les deux contre-lectures, ni leurs couples, ni leurs essais.",
         "nouveau": "j'ai écrit les brouillons 1 à 5 de ce texte et les scripts qu'il cite ; je n'ai écrit aucune des trois contre-lectures, ni leurs couples, ni leurs essais."},
        {"id": "C6-03", "motif": "heures", "ancien": "7 novembre 2026, de 23:33:23 à 23:40:51 (brouillon 5).",
         "nouveau": f"du 7 novembre 2026 à 23:56:57 au 8 novembre 2026 à {heure_fin} (brouillon 6)."},
        {"id": "C6-04", "motif": "statut du brouillon 6", "ancien": "- **Statut** : brouillon 5 = brouillon 4,",
         "nouveau": "- **Statut** : brouillon 6 = brouillon 5, plus les 11 couples de la contre-lecture bornée du delta du brouillon 5 (appliqués par `appliquer_couples_brouillon6_v1.py`, journal `journal-couples-brouillon6-v1.json`), plus les compléments qu'exige `lire_items_phase1_v4.py` (six chemins résiduels du masquage fermés ; dépense d'une tentative interrompue comptée) ; ces compléments et la version 4 **ne sont pas contre-lus** ; **non scellé**. Historique : brouillon 5 = brouillon 4,"},
        {"id": "C6-05", "motif": "demande de la session mère", "ancien": "ajouter les remarques R1 à R4 ; écrire ce brouillon 5 et un devis v4.",
         "nouveau": "ajouter les remarques R1 à R4 ; écrire ce brouillon 5 et un devis v4.\n- **Demande de la session mère** (7 novembre 2026, vers 23:56, temps universel) : fermer les six chemins résiduels du masquage en `lire_items_phase1_v4.py` (options jamais abrégées, aucune valeur reçue recopiée par l'analyseur d'arguments, chemin invalide refusé sans recopie), avec des essais pour ces six scénarios et pour les autres ; corriger la dépense sous-comptée (CD5-11) ; écrire le contrôle sur la facture de l'essai de format (CD5-05, CD5-06) ; appliquer les 11 couples dans ce brouillon 6."},
        {"id": "C6-06", "motif": "base",
         "ancien": "- **Base** : commit `bcb73441e` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 à 4, les deux contre-lectures, leurs couples et leurs essais sont versés ; aucun n'est touché.",
         "nouveau": "- **Base** : commit `01cd248e5` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 à 5, les trois contre-lectures, leurs couples et leurs essais sont versés ; aucun n'est touché."},
        {"id": "C6-07", "motif": "pièces", "ancien": pieces_b5(),
         "nouveau": "- **Pièces** (dossier `docs/notes/epreuve-etiqueteur-v1/`) : ce texte ; **versions en vigueur** : `generer_items_v2.py` et `test_generer_items_v2.py` (24 essais), `lire_items_phase1_v4.py` et `test_lire_items_phase1_v4.py` (79 essais, dont 57 scénarios à fausse clé), `analyser_phase1_v3.py` et `test_analyser_phase1_v3.py` (12 essais), `epreuve_phases_v1.py` et `test_epreuve_phases_v1.py` (6 essais) : **121 essais**, plus les 6 démonstrations de la contre-lecture 1 (`test_demonstrations_contre_lecture_v2.py`) : **127 passés** sur processeur, en environnement vidé ; `devis-epreuve-etiqueteur-v4.md` ; `appliquer_couples_brouillon6_v1.py` et son journal `journal-couples-brouillon6-v1.json` ; **versions remplacées, intactes** (R12) : `generer_items_v1.py`, `lire_items_phase1_v1.py` à `lire_items_phase1_v3.py`, `analyser_phase1_v1.py` et `analyser_phase1_v2.py`, leurs essais, devis v1 à v3 ; inchangés : `guide-annotation-v1.md`, `consigne-recrutement-annotateurs-v1.md` (à mettre au volume de la phase 2 avant son départ). Empreintes : annexe C."},
        {"id": "C6-08", "motif": "table des changements depuis le brouillon 5", "ancien": "## Ce qui change depuis le brouillon 4\n",
         "nouveau": """## Ce qui change depuis le brouillon 5

| point | brouillon 5 | brouillon 6 (contre-lecture bornée du delta du brouillon 5) |
|---|---|---|
| masquage : options abrégées | `--re=<clé>`, `--relais=<clé>` recopiés en entier sur la sortie d'erreur | options jamais abrégées ; tout message d'arguments réécrit, ne nommant que des options connues, sans aucune valeur reçue (`lire_items_phase1_v4.py`) |
| masquage : clé passée comme chemin | recopiée par le message d'erreur du système (`--registre-go` en mode réel, `--items` en mode simulé sans variable) | chaque chemin d'entrée contrôlé avant lecture et refusé sans recopie ; erreurs du système et exceptions écrites sans leur message |
| essais à fausse clé | 46 scénarios de la contre-lecture, hors du dépôt ; 6 fuites | 57 scénarios au dépôt (les 6, rejoués aussi contre la v3, et 51 autres) : aucun fragment de 6 caractères |
| dépense d'une tentative interrompue (CD5-11) | réserve jamais réglée : dépense sous-comptée au manifeste | réglée au pire cas et comptée ; nombre et réserve restante au manifeste |
| contrôle des prix (CD5-05, CD5-06) | — | entre l'essai de format et la lecture principale : facture de l'essai de format, montant au plus égal à la dépense estimée, jetons égaux |
| texte | — | 11 couples appliqués par script, comptés et journalisés ; compléments au même journal |

## Ce qui change depuis le brouillon 4
"""},
        {"id": "C6-09", "motif": "masquage : chemins résiduels fermés en v4", "n": 3,
         "ancien": "valeur refusée jamais recopiée, hors des deux chemins résiduels de la limite 14",
         "nouveau": "valeur refusée jamais recopiée (les deux chemins résiduels de la version 3 sont fermés en version 4 : limite 14)"},
        {"id": "C6-10", "motif": "limite 14 : fermés en v4", "ancien": cd503,
         "nouveau": cd503 + " **Fermés dans `lire_items_phase1_v4.py`** : options jamais abrégées (`allow_abbrev=False`) et messages d'arguments réécrits, qui ne nomment que des options connues et ne recopient aucune valeur reçue ; chaque chemin d'entrée contrôlé avant lecture et refusé sans recopie ; erreurs du système et exceptions écrites sans leur message. Les six chemins et 51 autres scénarios à fausse clé sont rejoués par `test_lire_items_phase1_v4.py` (aucun fragment de 6 caractères ; la version 3 sert d'artefact pour les six). Reste hors de portée du script la clé de Kimi, qui vit dans le relais."},
        {"id": "C6-11", "motif": "CD5-11 corrigé au code", "ancien": cd511,
         "nouveau": cd511[:-2] + " ; **corrigé dans `lire_items_phase1_v4.py`** : la réserve d'une tentative interrompue est réglée au pire cas et comptée dans la dépense, leur nombre et la réserve restante sont écrits au manifeste (essai `test_CD5_11_reserve_d_une_tentative_interrompue_comptee`) |"},
        {"id": "C6-12", "motif": "lecture v4 (réglages)", "ancien": "  - Code : constantes `LECTEURS` de `lire_items_phase1_v3.py` (inchangées depuis la v2),",
         "nouveau": "  - Code : constantes `LECTEURS` de `lire_items_phase1_v4.py` (inchangées depuis la v2),"},
        {"id": "C6-13", "motif": "lecture v4", "ancien": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v3.py` (les versions 1 et 2 restent intactes ; essais",
         "nouveau": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v4.py` (les versions 1 à 3 restent intactes ; essais `test_six_chemins_fermes_en_v4_et_ouverts_en_v3`, `test_arguments_jamais_recopies`, `test_chemins_du_fournisseur_en_mode_reel`, `test_CD5_11_reserve_d_une_tentative_interrompue_comptee`, et, repris de la v3,"},
        {"id": "C6-14", "motif": "ordre des opérations : script v4", "ancien": "2. Scripts de lecture (`lire_items_phase1_v3.py`)",
         "nouveau": "2. Scripts de lecture (`lire_items_phase1_v4.py`)"},
        {"id": "C6-15", "motif": "points ouverts : code v4", "ancien": "et au code (`lire_items_phase1_v3.py`)", "nouveau": "et au code (`lire_items_phase1_v4.py`)"},
        {"id": "C6-16", "motif": "R1 : code v4", "ancien": "(vérifié par `lire_items_phase1_v3.py`, remarque R1", "nouveau": "(vérifié par `lire_items_phase1_v4.py`, remarque R1"},
        {"id": "C6-17", "motif": "relais : code v4", "ancien": "arrête le lecteur Kimi (`lire_items_phase1_v3.py`)", "nouveau": "arrête le lecteur Kimi (`lire_items_phase1_v4.py`)"},
        {"id": "C6-18", "motif": "R4 : code v4", "ancien": "`lire_items_phase1_v3.py` en fait un arrêt général", "nouveau": "`lire_items_phase1_v4.py` en fait un arrêt général"},
        {"id": "C6-19", "motif": "liste d'arrêt : chemins et options abrégées",
         "ancien": "| argument de forme refusée (nom de la variable de la clé, commit, empreinte du relais, GO, adresse du relais), argument inconnu,",
         "nouveau": "| argument de forme refusée (nom de la variable de la clé, commit, empreinte du relais, GO, adresse du relais), chemin d'entrée qui n'est pas un fichier, option abrégée, argument inconnu,"},
        {"id": "C6-20", "motif": "contrôle sur la facture de l'essai de format (CD5-05, CD5-06), explicite à l'ordre d'exécution",
         "ancien": "**après le contrôle des prix** sur le relevé du fournisseur",
         "nouveau": "**après le contrôle des prix** sur la facture ou le relevé d'usage de chaque fournisseur pour les seuls appels de l'essai de format (montant facturé, hors taxes, au plus égal à la dépense estimée de ce lecteur au journal de l'essai de format ; jetons facturés égaux, à l'arrondi près, aux jetons écrits ; pour Argon comme pour Kimi ; sinon arrêt avant la lecture principale et nœud du directeur)"},
        {"id": "C6-21", "motif": "traitement de la contre-lecture bornée du delta du brouillon 5", "ancien": cd510,
         "nouveau": cd510 + "\n- **Traitement de la contre-lecture bornée du delta du brouillon 5** (brouillon 6) : 11 couples appliqués par script, comptés et journalisés ; les deux chemins résiduels du masquage (six scénarios) fermés dans `lire_items_phase1_v4.py`, avec 57 scénarios à fausse clé au dépôt ; la dépense d'une tentative interrompue (CD5-11) comptée au code ; le contrôle sur la facture de l'essai de format (CD5-05, CD5-06) écrit à l'ordre des opérations. La version 4 et ces compléments ne sont pas contre-lus."},
        {"id": "C6-22", "motif": "annexe C refaite", "ancien": texte[debut_c:fin_c],
         "nouveau": "## Annexe C — empreintes au rendu (sans contenu de clé)\n\nANNEXE_C_6\n\n"},
    ]


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--heure-fin", required=True)
    a = p.parse_args(argv)
    for chemin, attendue in ((BROUILLON5, EMPREINTE_BROUILLON5), (COUPLES, EMPREINTE_COUPLES)):
        if h(chemin) != attendue:
            raise Arret(f"empreinte de {chemin.name} différente de l'attendue")
    for chemin in (BROUILLON6, JOURNAL):
        if chemin.exists():
            raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
    texte = BROUILLON5.read_text(encoding="utf-8")
    liste = json.loads(COUPLES.read_text(encoding="utf-8"))
    if len(liste) != 11:
        raise Arret(f"{len(liste)} couples au lieu de 11")
    par_id = {c["id"][:6]: c for c in liste}
    texte, j1 = b4.appliquer_couples(texte, liste)
    texte, j2 = b4.appliquer_complements(texte, complements(a.heure_fin, texte, par_id))
    if texte.count("ANNEXE_C_6") != 1:
        raise Arret("emplacement de l'annexe C introuvable")
    texte = texte.replace("ANNEXE_C_6", annexe_c(a.heure_fin, texte))
    octets = texte.encode("utf-8")
    BROUILLON6.write_bytes(octets)
    journal = {"script": Path(__file__).name, "empreinte_script": h(Path(__file__)),
               "scripts_repris": {n: h(ICI / n) for n in ("appliquer_couples_brouillon4_v1.py", "appliquer_couples_brouillon5_v1.py")},
               "entrees": {BROUILLON5.name: EMPREINTE_BROUILLON5, COUPLES.name: EMPREINTE_COUPLES},
               "sortie": {BROUILLON6.name: hashlib.sha256(octets).hexdigest()},
               "comptes": {"couples_appliques": len(j1), "occurrences_des_couples": sum(x["n_trouve"] for x in j1),
                           "complements_appliques": len(j2), "occurrences_des_complements": sum(x["n_trouve"] for x in j2)},
               "couples": [dict(x, source="couple de la contre-lecture bornée du delta du brouillon 5") for x in j1],
               "complements": j2}
    JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"comptes": journal["comptes"], "brouillon6": journal["sortie"][BROUILLON6.name]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
