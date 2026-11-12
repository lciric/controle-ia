"""Tables de l'entretien avec le Transformative AI Fund, version 3 (`scripts/registres_taif_v3.py`) sur un petit dépôt factice.

Les 19 essais de la v2 sont repris, adaptés aux noms v3 et à la source neuve des promesses : la candidature factice est
un texte extrait à la mise en page de `pdftotext -layout` (titres « N. Titre » à la colonne 0, puces sans glyphe, table du
calendrier à colonnes alignées, sauts de page « \\x0c »), comme la candidature envoyée au fonds le 7 octobre 2026.
Repris de la v1 (cas sain : tables et `sources-v3.json` écrits, cellules reliées, idempotence ; artefacts : verdict sans
compagnon → refusé ; verdict altéré → refusé ; préenregistrement sans compagnon → refusé ; dépense sans GO → signalée ;
cellule sans source → vide) et de la v2, un essai sain et un essai artefact par changement de règle (R5) :
  1. comptes par issue recalculés depuis le texte de la table rendue (une ligne ajoutée au texte change le compte) ;
  2. table de lecture du verdict lue avant les mots-clés (verdict factice dont la prose contredit la table ; « oui » /
     « non » sous « conforme » ; identifiant de bras « Rd-6 » lu « R6 » ; table recopiée du préenregistrement ignorée ;
     colonne « réfutation atteinte ? » lue à l'envers ; plusieurs identifiants sur une ligne) ;
  3. issue « sans objet » distincte de « non atteinte », hors du taux ;
  4. analyseur strict des dépenses (registre factice aux totaux connus ; ligne ambiguë → journal ; « ≈ » → colonne estimé ;
     estimation remplacée par un relevé → comptée une fois ; deux montants → journal ; prix, cumul, plafond, crédit → jamais
     sommés ; clé `total_depenses_phase0`).
Nouveaux dans la v3, un cas sain et un artefact par règle de lecture de la mise en page extraite (section « v3 » en fin de
fichier) : numéros de ligne exacts malgré les sauts de page ; puces de la section 6 recollées (une majuscule après une fin
de phrase ouvre une puce, sinon la ligne continue la puce) ; paragraphe « Gate G0 » sur deux lignes ; ligne du calendrier
de la section 7 coupée sur plusieurs lignes physiques recollée ; en-tête du calendrier absent → aucune ligne C7 et un
signalement ; section absente → aucune ligne et un signalement, jamais une exception ; livrables et critères numérotés de
la section 8, critère coupé sur deux lignes recollé."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("registres_taif_v3", RACINE / "scripts" / "registres_taif_v3.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

RUN = "20261005-102042-validation-reelle"
PREREG = "prereg/T0.4-validation-modele-reel-v1.md"
VERDICT = "docs/verdicts/verdict-T0.4-critere-1-G0-v1.md"
TABLES = ("promis-livre-v3.md", "calibration-v3.md", "cout-par-resultat-v3.md", "total-depenses-v3.md")
CANDIDATURE = "docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt"


def _rang(mois: str, periode: str, travail: str, portes: str) -> str:
    """Une ligne physique de la table du calendrier à la mise en page `-layout` : colonnes aux positions 1, 12, 31, 90."""
    return ((" " + mois).ljust(12) + periode.ljust(19) + travail.ljust(59) + portes).rstrip()


def _candidature_texte(sections: tuple[int, ...] = (6, 7, 8), entete7: bool = True, gate_g0: bool = True) -> str:
    """Candidature factice à la mise en page du texte extrait du PDF envoyé (titres à la colonne 0, puces sans glyphe,
    table alignée, sauts de page « \\x0c »). `sections` : sections 6, 7, 8 présentes ; `entete7` : ligne « Months … » de
    la table ; `gate_g0` : paragraphe « Gate G0 » de la section 6."""
    L = ["White-Box Control of Diffuse Threats", " Applicant              Lazar",
         " Period                 1 December 2026 – 30 June 2027 (7 months)", "",
         "1. Summary", "Most monitoring in AI control scores one action at a time.",
         "\x0c2. Problem", "Diffuse sabotage defeats per-action monitoring.", ""]
    if 6 in sections:
        L += ["6. Progress to date (phase 0, since 5 October 2026)",
              "     Activation harness validated on the real model, on a rented",
              "     H200 (criterion 1 of gate G0), after an inconclusive first version. The validation covered",
              "     bit-identical replay.",
              "     Compute spent: about $20."]
        if gate_g0:
            L += ["Gate G0 (at the start of the grant, December 2026) still requires organisms with a dose–response, probes",
                  "above the random floor."]
        L += [""]
    if 7 in sections:
        L += ["7. Timeline (seven months from 1 December 2026)"]
        L += [_rang("Months", "Period", "Work", "Gates and outputs") if entete7 else "A seven-month plan, month by month."]
        L += [_rang("1", "Nov 2026", "Close G0. Paper C: deference of judges under the five", "G0"),
              _rang("", "", "attack families (HC1). Paper A: organisms and", ""),
              _rang("", "", "dose–response", ""),
              _rang("2", "Jan 2027", "Paper C: impersonation (HC3)", "Paper C on arXiv and at a"),
              _rang("", "", "", "workshop; GC"),
              "", "The minimal scenario stops after month 4.", ""]
    if 8 in sections:
        L += ["8. Deliverables and success criteria", "Deliverables.",
              "     Two papers: C (arXiv and a workshop by month 4) and A (arXiv and a conference submission",
              "     by month 7). Paper B in the ambitious scenario.",
              "\x0c    Model organisms and probes.",
              "Success.",
              " 1. The deference law and the displacement tax are measured (Paper C).",
              " 2. The lemma and the negative theorem are proven and tested on real activations within the 2 × 2",
              "    design (Paper A).", ""]
    L += ["9. Risks and pre-committed pivots", " Risk                       Pre-committed response",
          " No internal signal         Publish the negative result", ""]
    return "\n".join(L)


def _ecrire(racine: Path, rel: str, texte: str, scelle: bool = False) -> Path:
    p = racine / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    if scelle:
        compagnon = Path(str(p) + ".sha256")
        if compagnon.exists():                 # dépôt factice réécrit par un essai : l'ancienne empreinte est retirée d'abord
            compagnon.unlink()
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
    _ecrire(racine, CANDIDATURE, _candidature_texte(), scelle=True)
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
        "| GO-2026-10-04-08 | 2026-10-04 | calcul | phase 0 (T0.4) | 150 USD | 2026-11-01 | Lazar | message |",
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
    return {n: (sortie / n).read_text(encoding="utf-8") for n in TABLES}, \
        json.loads((sortie / "sources-v3.json").read_text(encoding="utf-8"))


def _ligne(texte: str, debut: str) -> list[str]:
    for l in texte.splitlines():
        if l.startswith(debut):
            return [c.strip() for c in l.strip().strip("|").split("|")]
    raise AssertionError(f"ligne {debut!r} absente")


def _verdict_factice(racine: Path, corps: list[str]) -> None:
    """Réécrit (et rescelle) le verdict factice avec le corps donné après l'en-tête commun."""
    _ecrire(racine, VERDICT, "\n".join([f"# Verdict R13 — T0.4, run A `{RUN}` — v1", "",
                                        f"Préenregistrement appliqué : `{PREREG}`.", ""] + corps + [""]), scelle=True)


def _issue(racine: Path, prediction_id: str) -> tuple[str, dict]:
    sortie = racine / "sortie"
    rt.construire(racine, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    ligne = _ligne(tables["calibration-v3.md"], f"| `{PREREG}` | {rt.empreinte(racine / PREREG)} | {prediction_id} ")
    return ligne[7], sources["cellules"]["calibration-v3"][f"T0.4-validation-modele-reel-v1.md#{prediction_id.split(',')[0]}"].get("issue", {})


# --------------------------------------------------------------------------- cas sain (repris de la v1, adapté)
def test_cas_sain_quatre_tables_et_sources(depot_taif):
    sortie = depot_taif / "livrables" / "registres-taif-v3"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    assert resume["version"] == "registres-taif-v3"
    # 5 critères de G0 + 2 puces de la section 6 + C6-G0 + 2 lignes du calendrier + 2 livrables + 2 critères de succès.
    assert {k: v for k, v in resume["comptes"].items() if k != "calibration"} == {
        "promis-livre-v3": 14, "calibration-v3": 3, "cout-par-resultat-v3": 3, "total-depenses-v3": {"par_go": 2, "par_tache": 2},
        "preregs_lus": 1, "verdicts_lus": 1, "manifestes_lus": 2}
    assert sources["fichiers_lus"][CANDIDATURE] == rt.empreinte(depot_taif / CANDIDATURE)
    assert not [s for s in resume["signalements"] if s["chemin"] == CANDIDATURE]
    assert (sortie / "journal-depenses-v3.txt").is_file()

    # G0 : cinq critères (G1 et papier C séparés) ; critère 1 prouvé, pièce = verdict et son empreinte compagnon.
    g0_1 = _ligne(tables["promis-livre-v3.md"], "| G0-1 ")
    assert g0_1[2] == "harnais validé" and g0_1[3] == "M0 (5 oct. → 1er nov. 2026)"
    assert g0_1[4].startswith("prouvé") and g0_1[5] == f"`{VERDICT}`"
    assert g0_1[6] == rt.empreinte(depot_taif / VERDICT) and g0_1[7] == ""
    g0_2 = _ligne(tables["promis-livre-v3.md"], "| G0-2 ")
    assert g0_2[4] == "reste (organismes)" and g0_2[5] == "" and "fin novembre 2026" in g0_2[7] and "Reste :" in g0_2[7]
    assert _ligne(tables["promis-livre-v3.md"], "| G0-3 ")[2].startswith("préenregistrement de G1")
    assert _ligne(tables["promis-livre-v3.md"], "| G0-4 ")[2].startswith("préenregistrement du papier C")
    assert sources["cellules"]["promis-livre-v3"]["G0-1"]["piece"]["chemin"] == VERDICT
    c6_1 = _ligne(tables["promis-livre-v3.md"], "| C6-1 ")
    assert c6_1[5] == f"`{VERDICT}`" and "fait" in c6_1[4]
    assert c6_1[2].startswith("Activation harness validated on the real model, on a rented H200 (criterion 1 of gate G0)")
    assert c6_1[3] == "déclaré fait à la candidature (phase 0, since 5 October 2026)"
    assert _ligne(tables["promis-livre-v3.md"], "| C6-2 ")[2] == "Compute spent: about $20."
    c6_g0 = _ligne(tables["promis-livre-v3.md"], "| C6-G0 ")
    assert c6_g0[3] == "at the start of the grant, December 2026" and c6_g0[4] == "prouvés : 1 ; restent : 2, 3, 4, 5"
    assert c6_g0[2].endswith("probes above the random floor.")        # paragraphe de deux lignes recollé
    c7_1 = _ligne(tables["promis-livre-v3.md"], "| C7-1 ")
    assert c7_1[3] == "mois 1 (Nov 2026)" and c7_1[4] == "période en cours au jour du script"
    assert _ligne(tables["promis-livre-v3.md"], "| C7-2 ")[4] == "à venir (période non commencée au jour du script)"
    assert _ligne(tables["promis-livre-v3.md"], "| C8-1 ")[3] == "fin de la période (section 7 : seven months from 1 December 2026)"

    # Calibration : P1 confirmée et P2 non concluante, lues dans la table de lecture du verdict (changement 2) ; P9 non citée.
    cal = tables["calibration-v3.md"]
    p1 = _ligne(cal, f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P1 ")
    assert p1[4] == "P1 : identité exacte." and p1[5] == f"`{VERDICT}`" and p1[7] == "confirmée"
    assert p1[8].startswith("2 : n° 1 (sous-agent neuf, 2026-10-05)") and p1[9] == RUN
    p2 = _ligne(cal, f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P2 ")
    assert p2[4] == "P2 : τ_logique = 1e-4." and p2[7] == "non concluante"
    src_p2 = sources["cellules"]["calibration-v3"]["T0.4-validation-modele-reel-v1.md#P2"]["issue"]
    assert src_p2["lignes"] == [12] and src_p2["note"].startswith("table de lecture du verdict")
    assert "brouillon-G0-grille-v1.md" not in cal

    # Coût (table 3, règles de la v1) : montant du run lu dans la table des dépenses, instance par le registre des arrêts.
    run = _ligne(tables["cout-par-resultat-v3.md"], f"| {RUN} ")
    assert run[3] == "54298522" and run[4] == "GO-2026-10-04-08" and run[5] == "0,24" and run[8] == "1" and run[9] == "0,24"
    go = _ligne(tables["cout-par-resultat-v3.md"], "| GO-2026-10-04-08 ")
    assert go[1] == "GO calcul" and go[5] == "0,48"
    assert "GO-2026-10-04-02" not in tables["cout-par-resultat-v3.md"]
    assert sources["fichiers_lus"][VERDICT] == rt.empreinte(depot_taif / VERDICT)

    # Total strict (changement 4) : seul le montant en gras de la ligne 9 est relevé ; ≈ 0,24 (table et puce) estimé ;
    # le crédit relu (ligne 10) n'est ni sommé ni estimé.
    assert resume["total_depenses_phase0"] == "0,62"
    assert resume["total_depenses_phase0_detail"] == {"releve_usd": "0,62", "lignes_sommees": 1, "estime_usd_a_part": "0,48",
                                                      "lignes_estimees": 2, "lignes_non_sommees": 1}
    assert _ligne(tables["total-depenses-v3.md"], "| **relevé (phase 0)** ")[1:4] == ["**0,62**", "1", "1"]
    go_total = _ligne(tables["total-depenses-v3.md"], "| GO-2026-10-04-08 ")
    assert go_total[3] == "" and go_total[6] == "0,48" and go_total[8] == "5, 8"
    assert sources["cellules"]["total-depenses-v3"]["global"]["releve"]["lignes"] == [9]
    assert "11,79" not in tables["total-depenses-v3.md"]


def test_idempotent(depot_taif):
    sortie = depot_taif / "sortie"
    rt.construire(depot_taif, sortie, "2026-11-05")
    premiere = {p.name: p.read_bytes() for p in sortie.iterdir()}
    assert set(premiere) == set(TABLES) | {"sources-v3.json", "journal-depenses-v3.txt"}
    rt.construire(depot_taif, sortie, "2026-11-05")
    assert {p.name: p.read_bytes() for p in sortie.iterdir()} == premiere


# --------------------------------------------------------------------------- artefacts repris de la v1
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
    sans_go = _ligne(_lire(sortie)[0]["cout-par-resultat-v3.md"], "| (sans GO) l. 9 ")
    assert sans_go[1] == "dépense sans GO (signalée)" and sans_go[5] == "0,62"
    # Le relevé de crédit (ligne 10) n'est pas une dépense pour la table 3 ; pour la table 4 il va au journal, sans somme.
    assert all(s["ligne"] != 10 or s["quoi"].startswith("dépense non sommée") for s in resume["signalements"])
    assert "11,79" not in _lire(sortie)[0]["cout-par-resultat-v3.md"]


def test_cellule_sans_source_reste_vide(depot_taif):
    sortie = depot_taif / "sortie"
    rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    p9 = _ligne(tables["calibration-v3.md"], f"| `{PREREG}` | {rt.empreinte(depot_taif / PREREG)} | P9 ")
    assert p9[7] == "non citée par le verdict" and p9[4] == ""
    assert "seuil" not in sources["cellules"]["calibration-v3"]["T0.4-validation-modele-reel-v1.md#P9"]
    c6_2 = _ligne(tables["promis-livre-v3.md"], "| C6-2 ")
    assert c6_2[4:8] == ["", "", "", ""]
    assert set(sources["cellules"]["promis-livre-v3"]["C6-2"]) == {"promesse", "date_promise"}
    assert _ligne(tables["promis-livre-v3.md"], "| C8-1 ")[4:8] == ["", "", "", ""]
    assert set(sources["cellules"]["promis-livre-v3"]["C8-1"]) == {"promesse", "date_promise"}


def test_montants_depense_filtres():
    texte = ("instance 1 arrêtée après 0,5 heure, ≈ 2,67 USD de marche (1,093 USD/h), plafond 24 USD, "
             "cumul ≈ 5 USD sur 150 ; crédit relu 11,79 USD ; enveloppe commune 5 USD ; **4,30 / 12 USD** ; "
             "GO-2026-11-04-06, 400 USD")
    assert rt.montants_depense(texte) == ["2,67", "4,30"]


# --------------------------------------------------------------------------- changement 1 : comptes alignés sur la table
def test_comptes_recalcules_depuis_la_table_rendue(depot_taif):
    sortie = depot_taif / "sortie"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    cal = tables["calibration-v3.md"]
    # Cas sain : les comptes de `sources-v3.json` sont ceux que l'on recalcule depuis le texte de la table rendue.
    attendu = {"total": 3, "par_issue": {"confirmée": 1, "non citée par le verdict": 1, "non concluante": 1},
               "tranchees": 2, "confirmees": 1, "refutees": 0, "non_concluantes": 1, "sans_objet": 0,
               "taux_confirmation": "1 / 2 = 0,500", "taux_confirmation_valeur": 0.5}
    assert resume["comptes"]["calibration"] == attendu == sources["comptes"]["calibration"]
    assert rt.compter_issues_table_md(cal.split("## Comptes par issue")[0]) == attendu
    bloc = cal.split("## Comptes par issue")[1]
    assert "| **total** | **3** |" in bloc and "| confirmée | 1 |" in bloc and "**1 / 2 = 0,500**" in bloc
    # Artefact : une ligne ajoutée au texte de la table change le compte recalculé (le compte vient de la table, pas d'ailleurs).
    table_seule = cal.split("## Comptes par issue")[0]
    lignes = table_seule.splitlines()
    k = max(i for i, l in enumerate(lignes) if l.startswith("| `prereg/"))
    ajoutee = lignes[k].replace("| non citée par le verdict |", "| non déclenchée |")
    assert ajoutee != lignes[k]
    modifie = rt.compter_issues_table_md("\n".join(lignes[: k + 1] + [ajoutee] + lignes[k + 1:]))
    assert modifie["total"] == 4 and modifie["par_issue"]["non déclenchée"] == 1 and modifie["tranchees"] == 2
    # Artefact : table sans colonne « issue » → garde d'arrêt, jamais un compte silencieux.
    with pytest.raises(rt.GardeArret, match="colonne « issue » absente"):
        rt.compter_issues_table_md("| a | b |\n|---|---|\n| x | y |\n")


def test_categories_de_compte():
    assert rt.categorie_issue("réfutée (non conforme)") == "réfutée"
    assert rt.categorie_issue("contradictoire (confirmée l. 3 / sans objet l. 9)") == "contradictoire"
    assert rt.categorie_issue("registre des décisions, R-025 (pas de verdict scellé) : …") == "registre des décisions (sans verdict scellé)"
    assert rt.categorie_issue("mixte (Rk-7 : confirmée l. 62 ; Rk-8 : réfutée (non conforme) l. 63)").startswith("mixte")
    assert rt.categorie_issue("sans objet") == "sans objet" and rt.categorie_issue("") == "(vide)"


# --------------------------------------------------------------------------- changement 2 : table de lecture d'abord
def test_table_de_lecture_prime_sur_les_mots_cles(depot_taif):
    # Cas de référence (Rk-5 de la revalidation T0.5 v2) : la prose de tête dit « P2 non concluant : ne s'applique pas ;
    # les deux sont conformes », la table de lecture dit « oui » sous « conforme » → confirmée, par la ligne de table.
    _verdict_factice(depot_taif, [
        "## 1. Verdict", "", "- **P1 ou P2 non concluant** : ne s'applique pas ; les deux sont conformes pour « defaut ».", "",
        "## 3. Tableau", "", "| critère | grandeur | valeur | seuil gelé | conforme |", "|---|---|---|---|---|",
        "| P1, garde saine | q99 | 0,13 | ≤ 0,2 | oui |", "| P2, domaine | actions | 160 | ≥ 40 | oui |", "",
        "## 7. Comparaison", "", "- P2 : 160 actions comparées attendues ; 160 observées."])
    issue, src = _issue(depot_taif, "P2")
    assert issue == "confirmée" and src["lignes"] == [14] and src["note"].startswith("table de lecture du verdict")
    # Artefact : sans ligne de table, la même prose donne « non concluante » par mots-clés (lecture de la v1).
    _verdict_factice(depot_taif, [
        "## 1. Verdict", "", "- **P1 ou P2 non concluant** : ne s'applique pas ; les deux sont conformes pour « defaut ».", "",
        "## 7. Comparaison", "", "- P2 : 160 actions comparées attendues ; 160 observées."])
    issue, src = _issue(depot_taif, "P2")
    assert issue == "non concluante" and src["lignes"] == [7] and src["note"].startswith("mots-clés")


def test_oui_non_bras_et_non_atteint(depot_taif):
    # « non » sous « conforme » → réfutée (non conforme) ; « non atteint » n'est pas « non » ; « Rd-6 » se lit « R6 ».
    _ecrire(depot_taif, PREREG, "\n".join([
        "# Préenregistrement", "", "## Prédiction chiffrée et signe attendu", "", "| id | prédiction | réfutation |", "|---|---|---|",
        "| Rk-1 | q99 ≤ 0,2 | > 0,2 |", "| Rd-6 | chemin | écart |", "| P9 | audit | aucun écart |", "", "## Seuil", "", "- Rk-1 : 0,2.", ""]),
        scelle=True)
    _verdict_factice(depot_taif, [
        "| critère | valeur | seuil gelé | conforme |", "|---|---|---|---|",
        "| **R1, durée** | 8 089 s | ≤ 7 800 s | **non** (dépassement) |", "| R6, chemin | 3e-4 | ≤ 3e-3 | oui |",
        "", "| id | issue observée | lecture |", "|---|---|---|", "| P9 | production non jouée | **non atteint** |"])
    assert _issue(depot_taif, "Rk-1")[0] == "réfutée (non conforme)"
    assert _issue(depot_taif, "Rd-6")[0] == "confirmée" and _issue(depot_taif, "Rd-6")[1]["lignes"] == [8]
    assert _issue(depot_taif, "P9")[0] == "non atteinte"
    assert rt.motif_id("Rd-6").search("| R6, chemin |") and not rt.motif_id("Rd-6").search("R66")


def test_table_recopiee_du_prereg_ignoree(depot_taif):
    # Artefact : une table recopiée du préenregistrement (en-tête « réfutation », sans colonne d'issue) cite P2 avec le mot
    # « réfutation » ; elle n'est pas une table de lecture : l'issue vient de la prose.
    _verdict_factice(depot_taif, [
        "| id | prédiction | réfutation |", "|---|---|---|", "| P2 | écart ≤ 1e-4 | un écart > 1e-4 : réfutation |", "",
        "**Verdict.** P2 conforme (écart 3e-5)."])
    issue, src = _issue(depot_taif, "P2")
    assert issue == "confirmée" and src["lignes"] == [9]


def test_colonne_refutation_atteinte_lue_a_l_envers(depot_taif):
    _verdict_factice(depot_taif, [
        "| grandeur | prédiction | observé | réfutation écrite atteinte ? |", "|---|---|---|---|",
        "| P1, `E` | > 0,47 | 1,32 | non |", "| P2, `D` | aucune prédiction de signe | −0,06 | **non tranchée** : la réfutation ne peut pas être lue |",
        "| P9, `A` | ≈ 0,63 | 0,63 | oui |"])
    assert _issue(depot_taif, "P1")[0] == "confirmée"
    assert _issue(depot_taif, "P2")[0] == "non concluante"
    assert _issue(depot_taif, "P9")[0] == "réfutée"


def test_plusieurs_identifiants_sur_une_ligne(depot_taif):
    _ecrire(depot_taif, PREREG, "\n".join([
        "# Préenregistrement", "", "## Prédiction chiffrée et signe attendu", "", "| id | prédiction | réfutation |", "|---|---|---|",
        "| Rk-7, Rk-8 | mémoire ≤ 70 Gio ; durée ≤ 7 800 s | au-dessus |", "| A1, jeux « au-dessus » (T1, T4) | borne > 0 | ≤ 0 |", ""]),
        scelle=True)
    _verdict_factice(depot_taif, [
        "| critère | valeur | seuil gelé | conforme |", "|---|---|---|---|",
        "| R7, mémoire | 24 Gio | ≤ 70 Gio | oui |", "| **R8, durée** | 8 089 s | ≤ 7 800 s | **non** |", "", "A1 : conforme."])
    issue, src = _issue(depot_taif, "Rk-7, Rk-8")
    assert issue == "mixte (Rk-7 : confirmée l. 7 ; Rk-8 : réfutée (non conforme) l. 8)" and src["lignes"] == [7, 8]
    # « A1, jeux … » n'est pas une liste d'identifiants : un seul identifiant, lu dans la prose.
    assert _issue(depot_taif, "A1")[0] == "confirmée"
    assert rt.identifiants_cellule("Rk-7, Rk-8") == ["Rk-7", "Rk-8"]
    assert rt.identifiants_cellule("A1, jeux qui demandent « au-dessus » (T1, T4)") == ["A1"]
    assert rt.identifiants_cellule("P3-P4 (validité, niveau 1 de H-P3c)") == ["P3-P4"]
    # Sain : même issue pour les deux identifiants → une seule issue.
    _verdict_factice(depot_taif, ["| critère | valeur | seuil | conforme |", "|---|---|---|---|",
                                  "| R7, mémoire | 24 | ≤ 70 | oui |", "| R8, durée | 7 000 | ≤ 7 800 | oui |"])
    assert _issue(depot_taif, "Rk-7, Rk-8")[0] == "confirmée"


# --------------------------------------------------------------------------- changement 3 : « sans objet »
def test_sans_objet_distinct_de_non_atteinte(depot_taif):
    _ecrire(depot_taif, PREREG, "\n".join([
        "# Préenregistrement", "", "## Prédiction chiffrée et signe attendu", "", "| id | prédiction | réfutation |", "|---|---|---|",
        "| P1 | x | y |", "| P7 | contrôle de T1 | non établi |", "| P8 | contrôle de T2 | non établi |", "| A7 | forme du coût | — |", ""]),
        scelle=True)
    _verdict_factice(depot_taif, [
        "**Verdict.** P1 conforme ; P7 : sans objet (cible non établie) ; P8 : non atteint (production non jouée).", "",
        "| ce que rend l'addendum | ici |", "|---|---|", "| `reserve_A7_forme` | sans objet (A7 ne vise que des conclusions de sonde) |"])
    sortie = depot_taif / "sortie"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    tables, _ = _lire(sortie)
    assert _issue(depot_taif, "P7")[0] == "sans objet"
    assert _issue(depot_taif, "P8")[0] == "non atteinte"                       # artefact : « non atteint » reste « non atteinte »
    issue_a7, src_a7 = _issue(depot_taif, "A7")
    assert issue_a7 == "sans objet" and src_a7["lignes"] == [9] and "cellule de table" in src_a7["note"]
    c = resume["comptes"]["calibration"]
    assert c["par_issue"] == {"confirmée": 1, "non atteinte": 1, "sans objet": 2} and c["sans_objet"] == 2
    assert c["tranchees"] == 1 and c["taux_confirmation"] == "1 / 1 = 1,000"   # ni au numérateur ni au dénominateur
    assert "| sans objet | 2 |" in tables["calibration-v3.md"]


# --------------------------------------------------------------------------- changement 4 : analyseur strict des dépenses
REGISTRE_SAIN = "\n".join([
    "# Dépenses", "", "| date | GO | devis | type | appels | — | coût (USD) | cumul | note |", "|---|---|---|---|---|---|---|---|---|",
    "| 2026-10-31 | GO-2026-10-31-05 | poste (50 USD) | API | appels | — | 18.52 | 18.52 / 50 | tour 1 (T0.5) |",
    "| 2026-10-04 | GO-2026-10-04-08 | phase 0 (T0.4) | carte (3,124 USD/h) | 0,15 | — | ≈ 0,47 | ≈ 0,5 sur 150 | premier lancement |",
    "", "## Journal",
    "- 2026-10-24 19:16 UTC — brainstorm (GO-2026-10-24-06) : run v1, 0,00 USD (HTTP 400) ; run v2, **1,01 USD** (Fable 0,95, "
    "Opus 0,06) selon le journal. **Cumul sous GO-2026-10-24-06 : 1,01 USD sur 25.**",
    "- 2026-10-29 10:26 UTC — **fin : tour du collisionneur (GO-2026-10-29-10, plafond 11,8 USD)** : 9 cellules, **6,83 USD** "
    "(journal). Total des deux runs : 3,19 + 6,83 = **10,02 USD** (plafond cumulé 15).",
    "- 2026-10-06 12:11 UTC — instance 54476244 arrêtée après 0,572 heure, ≈ 2,67 USD de marche (4,669 USD/h), plus le "
    "téléchargement ; cumul de la phase 0 ≈ 5,1 USD (GO-2026-10-04-08).",
    "- 2026-10-20 06:07 UTC — crédit rechargé (GO-2026-10-04-08) : crédit relu 11,79 USD, contre 5,31 USD à 02:10 UTC.",
    "- 2026-10-24 12:10 UTC — dépense sans GO : débits visibles 6,01 USD au relevé ; instance 56799469 : 6,42 USD au même relevé.",
    "- 2026-11-03 06:17 UTC — départ d'A1-v3 (GO-2026-11-02-21, plafond 400 USD ; devis au plus ≈ 190 USD) : premier relevé du "
    "relais à 06:18 UTC : 6 appels, 0,35 USD.",
    "- 2026-11-03 07:24 UTC — A1-v3 arrêtée par l'infrastructure (GO-2026-11-02-21) : **41 appels, 4,25 USD au compte du relais**, "
    "dont 1,61 USD au pire cas pour l'appel 41.",
    "- 2026-10-15 11:29 UTC — engagement (GO-2026-10-12-02, au plus 10,5 USD) : offre à 1,08 USD de l'heure ; attendu ≈ 4,9 USD ; "
    "pire cas ≈ 8,1 USD ; cumul engagé au plafond : au plus ≈ 59,2 USD sur 150.",
    "- 2026-10-31 13:06 UTC — arrêt (GO-06) : 6,36 USD comptés (Fable 2,40, Argon 1,61).",
    "- 2026-11-03 10:23 UTC — départ (GO-2026-11-03-04) : contrôles conformes (0,00279 USD) ; attendu ≈ 12,3 USD.",
    ""])

GO_SAIN = "\n".join([
    "# GO", "", "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |", "|---|---|---|---|---|---|---|---|",
    "| GO-2026-10-31-05 | 2026-10-31 | calcul | poste collisionneur protocelles | 50 USD | 2026-11-05 | Lazar | m |",
    "| GO-2026-10-04-08 | 2026-10-04 | calcul | devis de calcul de la phase 0 (T0.4 à T0.8) | 150 USD | 2026-11-01 | Lazar | m |",
    "| GO-2026-11-02-21 | 2026-11-02 | calcul | attaque A1-v3, Argon seul | 400 USD | 2026-11-05 | Lazar | m |", ""])


def _analyse(tmp_path: Path, registre: str, go: str = GO_SAIN) -> dict:
    racine = tmp_path / "r"
    _ecrire(racine, "registres/depenses.md", registre)
    _ecrire(racine, "registres/go.md", go)
    dep = rt.Fichier(racine, "registres/depenses.md")
    return rt.analyser_depenses_strict(dep, rt.lire_go(rt.Fichier(racine, "registres/go.md")))


def test_depenses_strict_registre_sain_totaux_connus(tmp_path):
    A = _analyse(tmp_path, REGISTRE_SAIN)
    sommees = {e["ligne"]: e["montant"] for e in A["sommees"]}
    # Relevés : table (18.52), montant unique en gras (1,01 ; 6,83 ; 4,25), montant unique (6,36 ; 0,00279) → 36,97279.
    assert sommees == {5: "18.52", 9: "1,01", 10: "6,83", 15: "4,25", 17: "6,36", 18: "0,00279"}
    assert round(A["global"]["releve"], 5) == 36.97279 and A["global"]["lignes_sommees"] == 6
    # Estimations : « ≈ 0,47 » (table) et « ≈ 2,67 USD de marche » ; jamais dans le relevé.
    assert {e["ligne"]: e["montant"] for e in A["estimees"]} == {6: "0,47", 11: "2,67"}
    assert round(A["global"]["estime"], 2) == 3.14
    # Journal : crédit (12), deux montants (13), premier relevé partiel (14), engagement de contexte seulement (16).
    journal = {e["ligne"]: e["raison"] for e in A["journal"]}
    assert set(journal) == {12, 13, 14, 16}
    assert journal[12].startswith("montants de contexte seulement") and journal[13].startswith("plusieurs montants")
    assert journal[14].startswith("relevé partiel") and journal[16].startswith("montants de contexte seulement")
    # Par GO : relevé, lignes sommées, estimé à part, lignes non sommées ; GO abrégé à part ; périmètre lu dans le registre des GO.
    g = A["par_go"]
    assert g["GO-2026-10-31-05"]["releve"] == 18.52 and g["GO-2026-10-31-05"]["lignes_sommees"] == [5]
    assert g["GO-2026-11-02-21"]["releve"] == 4.25 and g["GO-2026-11-02-21"]["lignes_non_sommees"] == [14]
    assert g["GO-2026-10-04-08"]["releve"] == 0.0 and round(g["GO-2026-10-04-08"]["estime"], 2) == 3.14 and g["GO-2026-10-04-08"]["lignes_non_sommees"] == [12]
    assert g["(GO abrégé, non résolu : GO-06)"]["releve"] == 6.36 and g["(sans GO cité)"]["lignes_non_sommees"] == [13]
    # Par tâche : T0.5 nommée sur la ligne 5 ; T0.4 nommée sur la ligne 6 ; sinon le périmètre du GO (« T0.4 à T0.8 »).
    t = A["par_tache"]
    assert t["T0.5"]["releve"] == 18.52 and round(t["T0.4"]["estime"], 2) == 0.47
    assert round(t["T0.4 + T0.8"]["estime"], 2) == 2.67 and t["T0.4 + T0.8"]["lignes_non_sommees"] == [12]
    assert t["(aucune tâche de la phase 0 nommée)"]["lignes_sommees"] == [9, 10, 15, 17, 18]


def test_depenses_strict_artefacts_par_regle(tmp_path):
    base = ["# Dépenses", "", "## Journal"]
    # (a) Ligne ambiguë, deux montants nus → journal, rien sommé.
    A = _analyse(tmp_path / "a", "\n".join(base + ["- 2026-11-01 10:00 UTC — deux lots (GO-2026-10-04-08) : lot A 3,10 USD, lot B 2,20 USD.", ""]))
    assert not A["sommees"] and not A["estimees"] and A["journal"][0]["raison"] == "plusieurs montants (3,10 USD, 2,20 USD)"
    assert A["par_go"]["GO-2026-10-04-08"]["lignes_non_sommees"] == [4] and A["global"]["releve"] == 0.0
    # (b) Estimation « ≈ » → colonne estimé, jamais dans le relevé ; « ≤ », « environ », « au plus » aussi.
    A = _analyse(tmp_path / "b", "\n".join(base + [
        "- 2026-11-01 10:00 UTC — fin (GO-2026-10-04-08) : dépense ≈ 2,67 USD de marche.",
        "- 2026-11-01 11:00 UTC — fin (GO-2026-10-04-08) : dépense **≤ 0,037 USD**.",
        "- 2026-11-01 12:00 UTC — fin (GO-2026-10-04-08) : environ 1,5 USD.",
        "- 2026-11-01 13:00 UTC — fin (GO-2026-10-04-08) : coût de la machine au plus 5,02 USD.", ""]))
    assert [e["montant"] for e in A["estimees"]] == ["2,67", "0,037", "1,5", "5,02"] and not A["sommees"]
    assert A["global"]["releve"] == 0.0 and round(A["global"]["estime"], 3) == 9.227
    # (c) Estimation remplacée par un relevé → comptée une fois : sur la même ligne, et d'une ligne à l'autre (même GO).
    A = _analyse(tmp_path / "c", "\n".join(base + [
        "- 2026-11-04 10:25 UTC — session 1 finie (GO-2026-11-03-03) : dépense estimée ≈ 0,96 USD ; relevé exact sur la facture à faire.",
        "- 2026-11-05 02:24 UTC — facture relue (GO-2026-11-03-03) : relevé exact : **1,02 USD** (remplace l'estimation de la ligne du 4 novembre).",
        "- 2026-11-05 03:00 UTC — sonde finie (GO-2026-11-05-01) : dépense estimée ≈ 0,03 USD, relevé 0,02 USD sur la facture.", ""]))
    assert {e["ligne"]: e["montant"] for e in A["sommees"]} == {5: "1,02", 6: "0,02"}
    assert A["sommees"][1]["raison"].startswith("relevé qui remplace les estimations de la même ligne")
    assert not A["estimees"] and round(A["global"]["releve"], 2) == 1.04 and A["global"]["estime"] == 0.0
    assert [e["raison"] for e in A["journal"] if e["ligne"] == 4] == ["estimation remplacée par le relevé de la l. 5 (comptée une fois)"]
    assert A["par_go"]["GO-2026-11-03-03"] == {"releve": 1.02, "lignes_sommees": [5], "estime": 0.0, "lignes_estimees": [], "lignes_non_sommees": [4]}
    # (c') Sans la mention de remplacement, l'estimation antérieure reste en colonne estimé (le relevé ne la compte pas deux fois).
    A = _analyse(tmp_path / "c2", "\n".join(base + [
        "- 2026-11-04 10:25 UTC — session 1 finie (GO-2026-11-03-03) : dépense estimée ≈ 0,96 USD.",
        "- 2026-11-05 02:24 UTC — session 2 finie (GO-2026-11-03-03) : **1,02 USD**.", ""]))
    assert round(A["global"]["releve"], 2) == 1.02 and round(A["global"]["estime"], 2) == 0.96
    # (d) Deux montants en gras → journal ; une fourchette → journal ; un relevé partiel → journal.
    A = _analyse(tmp_path / "d", "\n".join(base + [
        "- 2026-11-03 08:30 UTC — appels (GO-2026-10-04-08) : Astra **0,508 USD** ; Argon **0,4597 USD** ; total ≈ 0,97 USD.",
        "- 2026-10-05 14:44 UTC — lancement (GO-2026-10-04-08) : dépense de carte de 4,4 à 6,7 USD selon l'offre.",
        "- 2026-11-03 06:17 UTC — départ (GO-2026-10-04-08) : premier relevé du relais : 0,35 USD.",
        "- 2026-11-03 09:00 UTC — tour inscrit à la clôture (GO-2026-10-04-08) : total 20,84 USD.", ""]))
    assert not A["sommees"] and not A["estimees"]
    raisons = [e["raison"] for e in A["journal"]]
    assert raisons[0] == "plusieurs montants en gras" and raisons[1].startswith("fourchette 4,4 à 6,7 USD")
    assert raisons[2].startswith("relevé partiel") and raisons[3].startswith("reprise ou bilan")
    # (e) Prix unitaire, cumul, plafond, crédit, devis, montant collé à un GO, « x / plafond », formule « = » : jamais sommés.
    A = _analyse(tmp_path / "e", "\n".join(base + [
        "- 2026-10-04 18:02 UTC — engagement (GO-2026-10-04-08) : prix 3,124 USD de l'heure ; plafond 19,6 USD ; cumul 0,5 USD "
        "sur 150 ; crédit relu 9,99 USD ; devis 7,2 USD ; GO-2026-11-04-06, 400 USD ; **4,30 / 12 USD** ; 6 × 1,08 + 0,9 = 7,38 USD.", ""]))
    assert not A["sommees"] and not A["estimees"] and A["journal"][0]["raison"].startswith("montants de contexte seulement")
    assert [j["classe"] for j in rt.jetons_montants(A["journal"][0]["texte"].split("— ", 1)[1])] == ["prix"] + ["hors_depense"] * 7
    # (f) Montant unique en gras parmi des composantes → total de la ligne ; sans gras, plusieurs montants → journal.
    A = _analyse(tmp_path / "f", "\n".join(base + [
        "- 2026-10-25 08:16 UTC — tour (GO-2026-10-04-08) : Fable OK (0,87 USD), Opus OK (0,55 USD) ; **1,42 USD**.",
        "- 2026-10-25 08:20 UTC — tour (GO-2026-10-04-08) : Fable OK (0,87 USD), Opus OK (0,55 USD) ; 1,42 USD.", ""]))
    assert [(e["ligne"], e["montant"]) for e in A["sommees"]] == [(4, "1,42")]
    assert [e["ligne"] for e in A["journal"]] == [5] and A["journal"][0]["raison"].startswith("plusieurs montants")


def test_total_depenses_cle_sources_et_journal(depot_taif):
    sortie = depot_taif / "sortie"
    resume = rt.construire(depot_taif, sortie, "2026-11-05")
    tables, sources = _lire(sortie)
    assert sources["total_depenses_phase0"] == resume["total_depenses_phase0"] == "0,62"
    assert "`total_depenses_phase0`" in tables["total-depenses-v3.md"] and "<<TOTAL_DEPENSES_PHASE0>>" in tables["total-depenses-v3.md"]
    journal = (sortie / "journal-depenses-v3.txt").read_text(encoding="utf-8")
    assert "l. 10 [montants de contexte seulement" in journal and "11,79" in journal
    non_sommees = [s for s in sources["signalements"] if s["quoi"].startswith("dépense non sommée")]
    assert [s["ligne"] for s in non_sommees] == [10]
    assert sources["cellules"]["total-depenses-v3"]["global"]["non_sommees"]["lignes"] == [10]


# --------------------------------------------------------------------------- v3 : mise en page du texte extrait du PDF envoyé
def _promis(racine: Path, jour: str = "2026-11-05") -> tuple[dict, str, dict]:
    sortie = racine / "sortie"
    resume = rt.construire(racine, sortie, jour)
    tables, sources = _lire(sortie)
    return resume, tables["promis-livre-v3.md"], sources


def _ids(table: str, prefixe: str) -> list[str]:
    return [l.split("|")[1].strip() for l in table.splitlines() if l.startswith(f"| {prefixe}")]


def test_fichier_texte_numeros_de_ligne_malgre_les_sauts_de_page(depot_taif):
    # Sain : la ligne « 6. Progress to date » est la 10e du fichier, après un saut de page (« \x0c2. Problem », l. 7) ;
    # `FichierTexte` cite 10. Artefact : `Fichier` (coupe `splitlines`) la citerait 11, un numéro qui n'existe pas dans le fichier.
    texte = rt.FichierTexte(depot_taif, CANDIDATURE, scelle=True)
    assert texte.lignes[9] == "6. Progress to date (phase 0, since 5 October 2026)"
    assert len(texte.lignes) == len(texte.chemin.read_text(encoding="utf-8").split("\n")) - 1
    assert rt.Fichier(depot_taif, CANDIDATURE).lignes[10] == "6. Progress to date (phase 0, since 5 October 2026)"
    titre, lignes = rt.section_texte(texte, 6)
    assert titre == (10, "6. Progress to date (phase 0, since 5 October 2026)") and lignes[0][0] == 11 and lignes[-1][0] == 17
    assert rt.section_texte(texte, 2)[0] == (7, "\x0c2. Problem")             # saut de page devant un titre : titre quand même
    assert rt.section_texte(texte, 4) == (None, [])
    _, table, sources = _promis(depot_taif)
    src = sources["cellules"]["promis-livre-v3"]
    assert src["C6-1"]["promesse"]["lignes"] == [11, 12, 13] and src["C6-1"]["promesse"]["chemin"] == CANDIDATURE
    assert src["C6-2"]["promesse"]["lignes"] == [14] and src["C6-G0"]["promesse"]["lignes"] == [15, 16]
    assert src["C7-1"]["promesse"]["lignes"] == [20, 21, 22] and src["C7-2"]["promesse"]["lignes"] == [23, 24]
    assert src["C8-1"]["promesse"]["lignes"] == [30, 31] and src["C8-2"]["promesse"]["lignes"] == [32]
    assert src["C8-3"]["promesse"]["lignes"] == [34] and src["C8-4"]["promesse"]["lignes"] == [35, 36]
    assert src["C8-1"]["date_promise"]["lignes"] == [18, 30, 31]              # titre de la section 7 cité pour la date


def test_section6_puces_recollees(depot_taif):
    # Sain : une puce sur trois lignes (« on a rented » / « H200 … The validation covered » / « bit-identical replay. ») est
    # une seule promesse ; la ligne « H200 … » commence par une majuscule mais la puce courante ne finit pas par un point :
    # elle continue la puce. « Compute spent » ouvre une puce (majuscule après « replay. »).
    _, table, _ = _promis(depot_taif)
    assert _ids(table, "C6-") == ["C6-1", "C6-2", "C6-G0"]
    c6_1 = _ligne(table, "| C6-1 ")[2]
    assert "on a rented H200 (criterion 1 of gate G0), after an inconclusive first version. The validation covered bit-identical replay." in c6_1
    # Unitaire : la même règle sur des lignes données.
    items = rt.items_indentes([(1, "     Alpha one"), (2, "     Beta two."), (3, "     gamma three."), (4, "     Delta four"),
                               (5, "Colonne zéro"), (6, "     Epsilon five."), (7, ""), (8, " 1. Un critère sur"), (9, "    deux lignes."),
                               (10, " 2. Deux.")])
    # Règle : « Beta two. » continue « Alpha one » (majuscule, mais la puce ne finit pas par un point) ; « gamma three. »
    # continue (minuscule) ; « Delta four » ouvre une puce (majuscule après un point) ; la ligne à la colonne 0 clôt la puce ;
    # « Epsilon » ouvre une puce ; les numérotées ouvrent chacune une puce et la ligne indentée suivante les continue.
    assert [(i["lignes"], i["texte"]) for i in items] == [
        ([1, 2, 3], "Alpha one Beta two. gamma three."), ([4], "Delta four"), ([6], "Epsilon five."),
        ([8, 9], "Un critère sur deux lignes."), ([10], "Deux.")]
    # Artefact : aucune ligne indentée → aucune puce, pas d'exception.
    assert rt.items_indentes([(1, "Colonne zéro."), (2, "")]) == []


def test_section6_sans_paragraphe_gate_g0_signale(depot_taif):
    _ecrire(depot_taif, CANDIDATURE, _candidature_texte(gate_g0=False), scelle=True)
    resume, table, _ = _promis(depot_taif)
    assert _ids(table, "C6-") == ["C6-1", "C6-2"] and "| C6-G0 " not in table
    assert [s["quoi"] for s in resume["signalements"] if s["chemin"] == CANDIDATURE] == \
        ["paragraphe « Gate G0 » absent de la section 6 : aucune ligne C6-G0"]


def test_section7_ligne_du_calendrier_coupee_recollee(depot_taif):
    # Sain : la ligne « 1 » court sur trois lignes physiques (cellule « Work » coupée deux fois), la ligne « 2 » sur deux
    # (cellule « Gates » coupée) ; chacune donne une seule ligne C7, cellules recollées par un espace, période telle que le texte.
    _, table, sources = _promis(depot_taif)
    assert _ids(table, "C7-") == ["C7-1", "C7-2"]
    c7_1 = _ligne(table, "| C7-1 ")
    assert c7_1[2] == ("Close G0. Paper C: deference of judges under the five attack families (HC1). Paper A: organisms and "
                       "dose–response → G0")
    assert c7_1[3] == "mois 1 (Nov 2026)"
    c7_2 = _ligne(table, "| C7-2 ")
    assert c7_2[2] == "Paper C: impersonation (HC3) → Paper C on arXiv and at a workshop; GC" and c7_2[3] == "mois 2 (Jan 2027)"
    assert sources["cellules"]["promis-livre-v3"]["C7-2"]["etat"]["lignes"] == [23, 24]
    # Unitaire : une cellule décalée de deux colonnes au plus va à la bonne colonne (tolérance) ; une ligne vide finit la table.
    rangs, erreur = rt.table_alignee([(1, _rang("Months", "Period", "Work", "Gates and outputs")),
                                      (2, _rang("5–6", "Apr–May 2027", "Paper A: adaptive attacks", "Paper A on arXiv;")),
                                      (3, "  " + _rang("", "", "learning against the probe", "submission")[2:]),
                                      (4, ""), (5, _rang("7", "Jun 2027", "Après la table : ignoré", "Final report"))])
    assert erreur == "" and len(rangs) == 1
    assert rangs[0] == {"lignes": [2, 3], "cellules": ["5–6", "Apr–May 2027", "Paper A: adaptive attacks learning against the probe",
                                                       "Paper A on arXiv; submission"]}


def test_section7_sans_entete_signalee_sans_exception(depot_taif):
    # Artefact : la ligne « Months … Period … Work … » manque → aucune ligne C7, un signalement, le reste de la table est rendu.
    _ecrire(depot_taif, CANDIDATURE, _candidature_texte(entete7=False), scelle=True)
    resume, table, _ = _promis(depot_taif)
    assert _ids(table, "C7-") == [] and _ids(table, "C8-") == ["C8-1", "C8-2", "C8-3", "C8-4"]
    assert resume["comptes"]["promis-livre-v3"] == 12
    signales = [s for s in resume["signalements"] if s["chemin"] == CANDIDATURE]
    assert [s["quoi"] for s in signales] == ["table de la section 7 illisible (en-tête « Months … Period … Work … » absent) : aucune ligne C7"]
    assert signales[0]["ligne"] == 18 and signales[0]["texte"].startswith("7. Timeline")
    # Unitaire : sans en-tête, ([], raison) ; en-tête sans ligne de calendrier : ([], raison), jamais une exception.
    assert rt.table_alignee([(1, " 1          Dec 2026           Close G0      G0")]) == ([], "en-tête « Months … Period … Work … » absent")
    assert rt.table_alignee([(1, _rang("Months", "Period", "Work", "Gates and outputs")), (2, "")]) == ([], "aucune ligne de calendrier sous l'en-tête")


@pytest.mark.parametrize("absente, restantes, quoi", [
    (6, ["C7-1", "C7-2", "C8-1", "C8-2", "C8-3", "C8-4"], "section 6 « Progress to date » absente de la candidature : aucune ligne C6"),
    (7, ["C6-1", "C6-2", "C6-G0", "C8-1", "C8-2", "C8-3", "C8-4"], "section 7 « Timeline » absente de la candidature : aucune ligne C7"),
    (8, ["C6-1", "C6-2", "C6-G0", "C7-1", "C7-2"], "section 8 « Deliverables and success criteria » absente de la candidature : aucune ligne C8"),
])
def test_section_absente_aucune_ligne_et_signalement(depot_taif, absente, restantes, quoi):
    # Artefact : une section manque → aucune ligne pour elle, un signalement (`signalements` de `sources-v3.json`), pas d'exception ;
    # les autres sections et les critères de G0 sont rendus. Sans section 7, la date promise des lignes C8 reste vide (sans source).
    _ecrire(depot_taif, CANDIDATURE, _candidature_texte(sections=tuple(s for s in (6, 7, 8) if s != absente)), scelle=True)
    resume, table, sources = _promis(depot_taif)
    assert _ids(table, "C") == restantes and _ids(table, "G0-") == ["G0-1", "G0-2", "G0-3", "G0-4", "G0-5"]
    signales = [s for s in sources["signalements"] if s["chemin"] == CANDIDATURE]
    assert [s["quoi"] for s in signales] == [quoi] and signales[0]["ligne"] == 0 and signales[0]["sha256"] == rt.empreinte(depot_taif / CANDIDATURE)
    if absente == 7:
        assert _ligne(table, "| C8-1 ")[3] == "" and "date_promise" not in sources["cellules"]["promis-livre-v3"]["C8-1"]


def test_section8_livrables_puis_criteres_numerotes(depot_taif):
    # Sain : deux livrables (puces sans glyphe, la première sur deux lignes, la seconde derrière un saut de page) puis deux
    # critères numérotés « 1. », « 2. » (le second coupé sur deux lignes) ; les étiquettes « Deliverables. » et « Success. » ne
    # sont pas des puces ; identifiants C8-1 à C8-4 dans l'ordre du texte.
    _, table, _ = _promis(depot_taif)
    assert _ids(table, "C8-") == ["C8-1", "C8-2", "C8-3", "C8-4"]
    assert _ligne(table, "| C8-1 ")[2] == ("Two papers: C (arXiv and a workshop by month 4) and A (arXiv and a conference submission "
                                            "by month 7). Paper B in the ambitious scenario.")
    assert _ligne(table, "| C8-2 ")[2] == "Model organisms and probes."
    assert _ligne(table, "| C8-3 ")[2] == "The deference law and the displacement tax are measured (Paper C)."
    assert _ligne(table, "| C8-4 ")[2] == ("The lemma and the negative theorem are proven and tested on real activations within the 2 × 2 "
                                            "design (Paper A).")
    assert "Deliverables." not in [l.split("|")[3].strip() for l in table.splitlines() if l.startswith("| C8-")]
    # Artefact : un critère numéroté suivi d'une ligne indentée en majuscule après un point ouvre une puce nouvelle (règle écrite) :
    # un lecteur qui coupe une phrase après un point et reprend par une majuscule verrait deux puces ; la règle le dit.
    items = rt.items_indentes([(1, " 1. Un critère fini."), (2, "    Suite en majuscule après un point.")])
    assert [i["texte"] for i in items] == ["Un critère fini.", "Suite en majuscule après un point."]
