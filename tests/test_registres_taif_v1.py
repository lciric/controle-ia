"""Tables de l'entretien avec le Transformative AI Fund (`scripts/registres_taif_v1.py`) sur un petit dépôt factice.

Cas sain : trois tables et `sources-v1.json` écrits, cellules reliées (critère de G0 prouvé → verdict et empreinte ;
prédiction → issue lue dans la table de lecture du verdict ; run → montant du registre des dépenses), idempotence.
Artefacts (R5) : verdict sans compagnon → refusé ; verdict dont l'empreinte diffère du compagnon → refusé ; dépense
sans GO → signalée ; cellule sans source → vide, jamais inventée (aucune source enregistrée pour elle)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("registres_taif_v1", RACINE / "scripts" / "registres_taif_v1.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

RUN = "20261005-102042-validation-reelle"
PREREG = "prereg/T0.4-validation-modele-reel-v1.md"
VERDICT = "docs/verdicts/verdict-T0.4-critere-1-G0-v1.md"


def _ecrire(racine: Path, rel: str, texte: str, scelle: bool = False) -> Path:
    p = racine / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    if scelle:
        sceller(p)
    return p


def _depot_factice(racine: Path) -> Path:
    """Dépôt minimal : programme, candidature, registres, un préenregistrement, un verdict, un manifeste."""
    _ecrire(racine, "docs/programme-controle-ia-v2.md", "\n".join([
        "# Programme", "", "## 10. Plan expérimental", "", "### Phase 0 — instruments",
        "Tâches : socle ; harnais.",
        "**Porte G0 (prêt pour G1)** : harnais validé ; organismes avec dose-réponse ; "
        "préenregistrements de G1 et du papier C scellés et contre-lus ; état de l'art vérifié.", "",
        "### Phase 1", "- E1.1 organismes.", "", "| Période | Contenu |", "|---|---|",
        "| M0 (5 oct. → 1er nov. 2026) | Phase 0, porte G0 |", ""]), scelle=True)
    _ecrire(racine, "livrables/candidature-ea-funds-v1/proposal-v1.md", "\n".join([
        "# Proposal", "", "## 6. Progress to date (phase 0, since 5 October 2026)", "",
        "- **Activation harness validated** on the real model (criterion 1 of gate G0).",
        "- **Compute spent:** about $20.", "",
        "Gate G0 (1 November 2026) still requires organisms with a dose–response.", "",
        "## 7. Timeline (12 months from 1 November 2026)", "", "| Months | Period | Work | Gates and outputs |",
        "|-----|--------|------|------|", "| 1–2 | Nov–Dec 2026 | Paper A | G1 and GC |",
        "| 3 | Jan 2027 | Write Paper A | Paper A on arXiv |", "",
        "## 8. Deliverables and success criteria", "", "**Deliverables.**", "", "- Three papers.", "",
        "**Success.**", "", "1. The lemma is proven.", "", "## 9. Risks", "- none", ""]), scelle=True)
    _ecrire(racine, "registres/etat.md", "\n".join([
        "# État", "", "## Phase en cours",
        "Phase 0. Porte de sortie : G0, au plus tard fin novembre 2026, critères inchangés (N-027, tranché (a)).", "",
        "## Tâches de la phase 0", "", "| tâche | état | matériel | note |", "|---|---|---|---|",
        f"| T0.4 harnais et activations | **fait** : critère 1 de G0 **prouvé** | GPU | run `{RUN}` ; "
        f"verdict `{VERDICT}`. Reste : rien |",
        "| T0.6 organismes v0 | conception proposée | GPU | Paquet fait. Reste : contre-lecture et scellement |", "",
        "## Derniers verdicts de porte",
        "Aucune porte franchie. Critères de G0 prouvés : **1** (harnais validé). Restent les critères 2 (organismes), "
        "3 (G1), 4 (papier C) et 5 (état de l'art).", "", "## Dépenses", "rien", ""]))
    _ecrire(racine, "registres/decisions.md", "\n".join([
        "# Décisions", "", "| id | date (UTC) | décision | raison |", "|---|---|---|---|",
        "| R-041 | 2026-10-05 | Verdict R13 du critère 1 : **non concluant**. | R13 |",
        "| N-027 | 2026-10-20 | Porte G0 : calendrier décalé à fin novembre. | nœud |", ""]))
    _ecrire(racine, "registres/go.md", "\n".join([
        "# GO", "", "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |",
        "|---|---|---|---|---|---|---|---|",
        "| GO-2026-10-04-08 | 2026-10-04 | calcul | phase 0 | 150 USD | 2026-11-01 | Lazar | message |",
        "| GO-2026-10-04-02 | 2026-10-04 | revendication | N-003 | — | 2026-10-04 | Lazar | message |", ""]))
    _ecrire(racine, "registres/depenses.md", "\n".join([
        "# Dépenses", "", "| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |",
        "|---|---|---|---|---|---|---|---|---|",
        "| 2026-10-05 | GO-2026-10-04-08 | phase 0 (T0.4) | 54298522 | carte A100 (1,093 USD/h) | 0,22 | ≈ 0,24 | ≈ 0,8 sur 150 | run A |",
        "", "## Engagements",
        "- 2026-10-05 10:31 UTC — instance 54298522 arrêtée après 0,22 heure, ≈ 0,24 USD de marche (1,093 USD/h) ; "
        "cumul ≈ 0,8 USD sur 150 (GO-2026-10-04-08).",
        "- 2026-10-26 00:55 UTC — appel isolé, une cellule valide, **0,62 USD** ; aucune référence.",
        "- 2026-10-20 06:07 UTC — crédit rechargé : crédit relu 11,79 USD.", ""]))
    _ecrire(racine, "registres/arrets.md", "\n".join([
        "# Arrêts", "", "| date (UTC) | cible | raison | vérification |", "|---|---|---|---|",
        f"| 2026-10-05 10:31 | instance Vast.ai **54298522** | run A `{RUN}` arrêté par la garde | état exited |", ""]))
    _ecrire(racine, PREREG, "\n".join([
        "# Préenregistrement — T0.4 — v1", "", "## Hypothèse", "Le harnais est exact.", "",
        "## Prédiction chiffrée et signe attendu", "", "| id | prédiction | ordre de grandeur attendu | réfutation |",
        "|---|---|---|---|", "| P1 | garde de format conforme | identité | arrêt d'une garde |",
        "| P2 | écart relatif ≤ 1e-4 | 1e-16 à 1e-6 | un écart > 1e-4 : contraire |",
        "| P9 | au moins un écart non nul | écarts non nuls | aucun : audit de symétrie |", "",
        "## Métrique", "écart relatif.", "", "## Seuil", "", "- P2 : τ_logique = 1e-4.", "- P1 : identité exacte.", "",
        "## Plan d'analyse", "lecture.", "", "## Critères de lecture gelés", "table.", "", "## Liste d'arrêt", "gardes.", "",
        "## Contre-lecture", "", "- **Contre-lecture 1** (sous-agent neuf, 2026-10-05) : scellable après corrections.",
        "- **Contre-lecture 2** (sous-agent neuf, 2026-10-05) : scellable.", ""]), scelle=True)
    _ecrire(racine, "prereg/brouillon-G0-grille-v1.md", "# brouillon\n\n## Prédiction chiffrée et signe attendu\n| id | p |\n|---|---|\n| B1 | x |\n", scelle=True)
    _ecrire(racine, VERDICT, "\n".join([
        f"# Verdict R13 — T0.4, run A `{RUN}` — critère 1 de la porte G0 — v1", "",
        "**Verdict.** Le critère 1 de G0 est **non concluant**. P1 est conforme ; P2 non concluant.", "",
        f"Préenregistrement appliqué : `{PREREG}`.", "", "## 3. Lectures", "",
        "| id | valeur | lecture gelée |", "|---|---|---|", "| P1 | identité | conforme |",
        "| P2 | 1,27e-4 | non concluant : précision probable |", ""]), scelle=True)
    _ecrire(racine, f"runs/{RUN}/manifeste.json", json.dumps({
        "run_id": RUN, "cree_le": "2026-10-05T10:20:44+00:00", "decisif": True, "commit": "6cf7f20",
        "preenregistrement": {"chemin": PREREG, "sha256": "x" * 64}}, ensure_ascii=False, indent=1) + "\n", scelle=True)
    _ecrire(racine, "runs/20261004-034500-factice/manifeste.json", json.dumps({
        "run_id": "20261004-034500-factice", "cree_le": "2026-10-04T03:27:10+00:00", "decisif": False,
        "preenregistrement": None}) + "\n", scelle=True)
    return racine


@pytest.fixture
def depot_taif(tmp_path):
    return _depot_factice(tmp_path / "depot")


def _lire(sortie: Path):
    return {n: (sortie / n).read_text(encoding="utf-8") for n in
            ("promis-livre-v1.md", "calibration-v1.md", "cout-par-resultat-v1.md")}, \
        json.loads((sortie / "sources-v1.json").read_text(encoding="utf-8"))


def _ligne(texte: str, debut: str) -> list[str]:
    for l in texte.splitlines():
        if l.startswith(debut):
            return [c.strip() for c in l.strip().strip("|").split("|")]
    raise AssertionError(f"ligne {debut!r} absente")


# --------------------------------------------------------------------------- cas sain
def test_cas_sain_trois_tables_et_sources(depot_taif):
    sortie = depot_taif / "livrables" / "registres-taif-v1"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    assert resume["comptes"] == {"promis-livre-v1": 12, "calibration-v1": 3, "cout-par-resultat-v1": 3,
                                 "preregs_lus": 1, "verdicts_lus": 1, "manifestes_lus": 2}

    # G0 : cinq critères (G1 et papier C séparés) ; critère 1 prouvé, pièce = verdict et son empreinte compagnon.
    g0_1 = _ligne(tables["promis-livre-v1.md"], "| G0-1 ")
    assert g0_1[2] == "harnais validé" and g0_1[3] == "M0 (5 oct. → 1er nov. 2026)"
    assert g0_1[4].startswith("prouvé") and g0_1[5] == f"`{VERDICT}`"
    assert g0_1[6] == rt.empreinte(depot_taif / VERDICT) and g0_1[7] == ""
    g0_2 = _ligne(tables["promis-livre-v1.md"], "| G0-2 ")
    assert g0_2[4] == "reste (organismes)" and g0_2[5] == "" and "fin novembre 2026" in g0_2[7] and "Reste :" in g0_2[7]
    assert _ligne(tables["promis-livre-v1.md"], "| G0-3 ")[2].startswith("préenregistrement de G1")
    assert _ligne(tables["promis-livre-v1.md"], "| G0-4 ")[2].startswith("préenregistrement du papier C")
    assert sources["cellules"]["promis-livre-v1"]["G0-1"]["piece"]["chemin"] == VERDICT
    assert sources["cellules"]["promis-livre-v1"]["G0-1"]["etat"]["chemin"] == "registres/etat.md"
    # Candidature : promesse reliée à T0.4 ; période à venir lue sur le jour du script.
    c6_1 = _ligne(tables["promis-livre-v1.md"], "| C6-1 ")
    assert c6_1[5] == f"`{VERDICT}`" and "fait" in c6_1[4]
    assert _ligne(tables["promis-livre-v1.md"], "| C7-1 ")[4] == "période en cours au jour du script"
    assert _ligne(tables["promis-livre-v1.md"], "| C7-2 ")[4] == "à venir (période non commencée au jour du script)"

    # Calibration : P1 confirmée et P2 non concluante, lues dans la table de lecture du verdict ; P9 non citée.
    cal = tables["calibration-v1.md"]
    p1 = _ligne(cal, f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P1 ")
    assert p1[4] == "P1 : identité exacte." and p1[5] == f"`{VERDICT}`" and p1[7] == "confirmée"
    assert p1[8].startswith("2 : n° 1 (sous-agent neuf, 2026-10-05)") and p1[9] == RUN
    p2 = _ligne(cal, f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P2 ")
    assert p2[4] == "P2 : τ_logique = 1e-4." and p2[7] == "non concluante"
    assert sources["cellules"]["calibration-v1"][f"T0.4-validation-modele-reel-v1.md#P2"]["issue"]["lignes"] == [12]
    assert "brouillon-G0-grille-v1.md" not in cal

    # Coût : montant du run lu dans la table des dépenses (0,24), instance par le registre des arrêts, un verdict.
    run = _ligne(tables["cout-par-resultat-v1.md"], f"| {RUN} ")
    assert run[3] == "54298522" and run[4] == "GO-2026-10-04-08" and run[5] == "0,24" and run[8] == "1" and run[9] == "0,24"
    assert sources["cellules"]["cout-par-resultat-v1"][RUN]["montant"]["lignes"] == [5]
    go = _ligne(tables["cout-par-resultat-v1.md"], "| GO-2026-10-04-08 ")
    assert go[1] == "GO calcul" and go[5] == "0,48"      # table et puce citent le GO : deux lignes constatées sommées
    assert "GO-2026-10-04-02" not in tables["cout-par-resultat-v1.md"]
    assert sources["fichiers_lus"][VERDICT] == rt.empreinte(depot_taif / VERDICT)


def test_idempotent(depot_taif):
    sortie = depot_taif / "sortie"
    rt.construire(depot_taif, sortie, "2026-11-05")
    premiere = {p.name: p.read_bytes() for p in sortie.iterdir()}
    rt.construire(depot_taif, sortie, "2026-11-05")
    assert {p.name: p.read_bytes() for p in sortie.iterdir()} == premiere


# --------------------------------------------------------------------------- artefacts
def test_verdict_sans_compagnon_refuse(depot_taif):
    (depot_taif / (VERDICT + ".sha256")).unlink()
    with pytest.raises(rt.GardeArret, match="compagnon absente"):
        rt.construire(depot_taif, depot_taif / "sortie", "2026-11-05")
    assert not (depot_taif / "sortie").exists()


def test_verdict_altere_refuse(depot_taif):
    p = depot_taif / VERDICT
    p.write_text(p.read_text(encoding="utf-8") + "ligne ajoutée après scellement\n", encoding="utf-8")
    with pytest.raises(rt.GardeArret, match="différente du compagnon"):
        rt.construire(depot_taif, depot_taif / "sortie", "2026-11-05")


def test_preregistrement_sans_compagnon_refuse(depot_taif):
    (depot_taif / (PREREG + ".sha256")).unlink()
    with pytest.raises(rt.GardeArret, match="compagnon absente"):
        rt.construire(depot_taif, depot_taif / "sortie", "2026-11-05")


def test_depense_sans_go_signalee(depot_taif):
    sortie = depot_taif / "sortie"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    signales = [s for s in resume["signalements"] if s["quoi"] == "dépense sans GO cité sur la ligne"]
    assert [s["ligne"] for s in signales] == [9] and signales[0]["chemin"] == "registres/depenses.md"
    sans_go = _ligne(_lire(sortie)[0]["cout-par-resultat-v1.md"], "| (sans GO) l. 9 ")
    assert sans_go[1] == "dépense sans GO (signalée)" and sans_go[5] == "0,62"
    # Le relevé de crédit (ligne 10) n'est pas une dépense : ni signalé, ni compté.
    assert all(s["ligne"] != 10 for s in resume["signalements"])
    assert "11,79" not in _lire(sortie)[0]["cout-par-resultat-v1.md"]


def test_cellule_sans_source_reste_vide(depot_taif):
    sortie = depot_taif / "sortie"
    rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    # P9 n'est citée ni par le verdict ni par la section « Seuil » : issue dite « non citée », seuil vide.
    p9 = _ligne(tables["calibration-v1.md"], f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P9 ")
    assert p9[7] == "non citée par le verdict" and p9[4] == ""
    assert "seuil" not in sources["cellules"]["calibration-v1"]["T0.4-validation-modele-reel-v1.md#P9"]
    # « Compute spent » ne se relie à aucune tâche : état, pièce, empreinte et glissement vides, aucune source.
    c6_2 = _ligne(tables["promis-livre-v1.md"], "| C6-2 ")
    assert c6_2[4:8] == ["", "", "", ""]
    assert set(sources["cellules"]["promis-livre-v1"]["C6-2"]) == {"promesse", "date_promise"}
    # Livrables de la section 8 : aucune pièce reliée, cellules vides.
    assert _ligne(tables["promis-livre-v1.md"], "| C8-1 ")[4:8] == ["", "", "", ""]
    # Le montant d'une ligne à plusieurs montants n'est pas tranché : cellule vide, montants listés.
    assert "montants_retenus" in rt.lire_depenses(rt.Fichier(depot_taif, "registres/depenses.md"))[1]


def test_montants_depense_filtres():
    texte = ("instance 1 arrêtée après 0,5 heure, ≈ 2,67 USD de marche (1,093 USD/h), plafond 24 USD, "
             "cumul ≈ 5 USD sur 150 ; crédit relu 11,79 USD ; enveloppe commune 5 USD ; **4,30 / 12 USD** ; "
             "GO-2026-11-04-06, 400 USD")
    assert rt.montants_depense(texte) == ["2,67", "4,30"]
