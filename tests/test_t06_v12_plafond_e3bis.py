"""E3 bis sous GO-2026-11-07-08 (3 USD de plus sur GO-2026-11-06-01 : 8 USD pour E2, E3 et E3 bis ; échéance 12 novembre) — contre-lecture de la v11 (R-1746) : le total de 8 est LIÉ au GO
(les deux lignes du registre sont vérifiées, sans variable d'environnement) et la dépense antérieure est exigée (≥ 2,092 : E2 0,627 + E3 1,465), jamais acceptée à 0. Cas sain et artefact (R5)."""
from __future__ import annotations

import json
from datetime import timedelta

import pytest

from controle_ia.t06 import session_v11 as s11
from controle_ia.t06.session import GardeSession
import test_t06_v12_amorce as t
from test_t06_v12_amorce import (CONFIG_E2, CONFIG_E3, GO_E, _commit_source, _config_epreuve, _controles_epreuve, _dates_epreuve, _git, bac, depot_session,  # noqa: F401
                                 src_epreuve)

BIS = "GO-2026-11-07-08"


@pytest.mark.parametrize("plafond, ant, go, ok", [
    ("5.7", "2.092", BIS, True),           # le plafond proposé : 5,7 + 2,092 = 7,792 ≤ 7,9
    ("5.808", "2.092", BIS, True),         # borne exacte
    ("5.81", "2.092", BIS, False),
    ("5.7", "0", BIS, False),              # jamais acceptée à 0 : 5,7 serait permis sans dépense antérieure
    ("5.7", "2.091", BIS, False),          # sous 2,092
    ("5.7", "abc", BIS, False),
    ("5.7", "2.092", GO_E, False),         # le GO des 5 premiers USD ne permet pas 5,7 + 2,092
    ("4.27", "0.627", GO_E, True),         # E3 d'origine inchangé
    ("1", "0", GO_E, True),                # E2 : première épreuve, dépense antérieure 0
    ("1", "0", "GO-2026-11-02-28", False), # tout autre GO est refusé
])
def test_plafond_epreuve_borne_par_le_total_lie_au_go(plafond, ant, go, ok):
    if ok:
        assert "≤" in s11.verifier_plafond_epreuve(plafond, ant, go)
    else:
        with pytest.raises(GardeSession):
            s11.verifier_plafond_epreuve(plafond, ant, go)


def test_le_total_du_module_session_v8_n_est_pas_laisse_modifie():
    from controle_ia.t06 import session_v8 as s8
    s11.verifier_plafond_epreuve("5.7", "2.092", BIS)
    with pytest.raises(GardeSession):
        s11.verifier_plafond_epreuve("5.7", "2.092", GO_E)
    assert s8.GO_EPREUVES_USD == "5"


def _preparer_bis(src, *, ligne_bis=True, ligne_5=True, plafond=5.7, go=BIS):
    auj, ech, _ = _dates_epreuve()
    reg = src / "registres" / "go.md"
    lignes = [l for l in reg.read_text(encoding="utf-8").splitlines() if not l.startswith(f"| {GO_E} ") and not l.startswith(f"| {BIS} ")]
    if ligne_5:
        lignes.append(f"| {GO_E} | {auj} | calcul | épreuves à blanc E2 et E3 | 5 USD (E2 et E3 cumulés) | {ech} | Lazar | mot |")
    if ligne_bis:
        lignes.append(f"| {BIS} | {auj} | calcul | E3 bis | 3 USD | {ech + timedelta(days=2)} | Lazar | mot |")
    reg.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    c = _config_epreuve(CONFIG_E2, go_id=go, plafond_usd=plafond, mode="reel")        # carte modeste des offres factices du banc ; mode réel : HF_TOKEN exigé, T06_TESTS_ARGS refusé
    c["calendrier"] = {"dernier_jour_creation": str(ech + timedelta(days=1)), "fin_go_utc": (_dates_epreuve()[2] + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")}
    (src / "prereg" / "config-epreuve-e3bis.json").write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    _commit_source({"source": src}, "E3 bis : registre et configuration")
    _git(src, "push", "-q", "-f", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src, "fetch", "-q", "origin", "+refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")


def _controles(src, tmp_path, nom, ant):
    return _controles_epreuve(src, tmp_path, tmp_path / nom, config="prereg/config-epreuve-e3bis.json", T06_DEPENSE_EPREUVES_ANTERIEURES_USD=ant, T06_BRANCHE="essai/t06-e3bis-test")


def test_lanceur_cas_sain_e3_bis_verifie_les_deux_lignes_et_le_total_de_8(src_epreuve, tmp_path):
    _preparer_bis(src_epreuve)
    r = _controles(src_epreuve, tmp_path, "ok", "2.092")
    assert r.returncode == 0, r.stdout + r.stderr
    assert f"GO {BIS} (plafond de l'épreuve 5.7 USD sur 8" in r.stdout and "≤ 7.9" in r.stdout
    assert f"{GO_E}" in (tmp_path / "ok" / "lancement.txt").read_text(encoding="utf-8")


@pytest.mark.parametrize("cas, kw, ant, motif", [
    ("anterieure_0", {}, "0", "dépense antérieure"),
    ("anterieure_basse", {}, "2.0", "dépense antérieure"),
    ("sans_ligne_bis", {"ligne_bis": False}, "2.092", "absent"),
    ("sans_ligne_des_5_usd", {"ligne_5": False}, "2.092", "absent"),
    ("plafond_trop_haut", {"plafond": 5.82}, "2.092", "plafond"),
    ("autre_go", {"go": "GO-2026-11-02-28"}, "2.092", ""),
])
def test_lanceur_artefacts_e3_bis_refuses(src_epreuve, tmp_path, cas, kw, ant, motif):
    _preparer_bis(src_epreuve, **kw)
    r = _controles(src_epreuve, tmp_path, cas, ant)
    assert r.returncode != 0 and motif in r.stdout + r.stderr, (cas, r.stdout + r.stderr)
    assert "CONTRÔLES D'ÉPREUVE CONFORMES" not in r.stdout


def test_la_variable_t06_go_epreuves_total_usd_n_existe_plus_et_ne_permet_rien(src_epreuve, tmp_path):
    """Artefact de la v11 du rendu 3 : avec le GO des 5 premiers USD seul, un plafond de 5,7 ne passe plus, quelle que soit la variable."""
    auj, ech, _ = _dates_epreuve()
    c = _config_epreuve(CONFIG_E3, plafond_usd=5.7)
    (src_epreuve / "prereg" / "config-epreuve-e3.json").write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    _commit_source({"source": src_epreuve}, "plafond 5,7 sous le GO de 5 USD")
    _git(src_epreuve, "push", "-q", "-f", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src_epreuve, "fetch", "-q", "origin", "+refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    r = _controles_epreuve(src_epreuve, tmp_path, tmp_path / "v", config="prereg/config-epreuve-e3.json", T06_DEPENSE_EPREUVES_ANTERIEURES_USD="2.092", T06_GO_EPREUVES_TOTAL_USD="8")
    assert r.returncode != 0 and "CONTRÔLES D'ÉPREUVE CONFORMES" not in r.stdout


# --- création d'E3 bis, et refus de l'heure d'épuisement simulée hors épreuve (contre-lecture de la v11 : aucun essai ciblé de ce refus sur la v11) -----------------
from test_t06_v12_scripts import monde5, v5  # noqa: E402,F401


def _supp(m, ant="2.092"):
    return dict(T06_BRANCHE="essai/t06-e3bis-test", T06_REGISTRE_GO=str(m["src"] / "registres" / "go.md"), T06_DEPENSE_EPREUVES_ANTERIEURES_USD=ant, HF_TOKEN="jeton-hf-factice")


def _controles_bis(m, ant="2.092"):
    d = m["tmp"] / "bis"
    r = v5(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3bis.json", **_supp(m, ant))
    return d, r


def test_creation_e3_bis_commande_go_plafond_et_refus_de_tests_args_en_mode_reel(monde5):
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    r = v5(m, "creation", "auto", "course", "0", d, **_supp(m))
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith(f"GO_ID={BIS} timeout -k 10 300 ") and f"-e EPREUVE_GO_ID={BIS} " in cmd and "-e CONFIG=prereg/config-epreuve-e3bis.json" in cmd
    assert "TESTS_ARGS" not in cmd and "-e BRANCHE=essai/t06-e3bis-test" in cmd
    assert "plafond_creation 5.7" in (d / "lancement.txt").read_text(encoding="utf-8")
    # artefact : une sélection d'essais est refusée en mode réel (la suite ciblée figée de l'amorce est la seule jouée)
    r = v5(m, "creation", "auto", "course", "0", d, T06_TESTS_ARGS="tests/a.py,-x", **_supp(m))
    assert r.returncode == 2 and "T06_TESTS_ARGS refusé en mode reel" in r.stdout, r.stdout


def test_creation_e3_bis_la_depense_anterieure_du_lancement_ne_peut_pas_etre_descendue_a_0(monde5):
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    (d / "lancement.txt").write_text((d / "lancement.txt").read_text(encoding="utf-8").replace("epreuves_anterieures 2.092", "epreuves_anterieures 0"), encoding="utf-8")
    r = v5(m, "creation", "auto", "course", "0", d, **_supp(m, "0"))
    assert r.returncode == 2 and "plafond" in r.stdout and "dépense antérieure" in r.stdout, r.stdout


def test_heure_d_epuisement_simulee_admise_en_epreuve(monde5):
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    r = v5(m, "creation", "auto", "course", "0", d, T06_EPUISEMENT_SIMULE_S="600", **_supp(m))
    assert r.returncode == 0 and "DEPENSE_EPUISEE_UTC_S=" in r.stdout.splitlines()[-1], r.stdout


def test_heure_d_epuisement_simulee_refusee_hors_epreuve(monde5):
    """La course garde GO-2026-11-02-28 et 200 USD : `T06_EPUISEMENT_SIMULE_S` y est refusée (le seul essai ciblé de ce refus était dans test_t06_v4_scripts, exclu)."""
    m = monde5
    d = m["tmp"] / "course"
    r = v5(m, "controles", d, "2026-11-05", HF_TOKEN="jeton-hf-factice")
    assert r.returncode == 0, r.stdout + r.stderr
    r = v5(m, "creation", "auto", "course", "0", d, T06_EPUISEMENT_SIMULE_S="600", HF_TOKEN="jeton-hf-factice")
    assert r.returncode == 2 and "réservé aux épreuves à blanc" in r.stdout, r.stdout
    r = v5(m, "creation", "auto", "course", "0", d, HF_TOKEN="jeton-hf-factice")
    # cas sain : sans la variable, la création n'est plus refusée pour ce motif ; elle atteint le choix de l'offre (les offres factices du banc sont des cartes modestes : code 3, aucune offre conforme pour la carte de la course)
    assert r.returncode == 3 and "réservé aux épreuves à blanc" not in r.stdout and "aucune offre conforme" in r.stdout, r.stdout
