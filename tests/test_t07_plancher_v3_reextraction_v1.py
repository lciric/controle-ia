"""Essais de `reextraction_p3_v1.py` (plancher neuf des sondes figées de P3 à l'étape A de T0.7, remède (a')) — v1, fichier neuf
(consigne `consigne-code-plancher-v3-t07-v1.md`, `88879387…`, points 3 et 4).

Référence : **un vrai run jouet de P3** (`premier_test_ia.run.executer`, mode jouet, dépôt jetable, une fois par module), dont le
manifeste, `sondes-figees.json` et le fichier léger sont les entrées de la réextraction, comme le run réel de P3 l'est en mode
réel ; données génériques versées (faits, enjeux) à leur empreinte. Ses principales : `tromperie-lineaire-c2` (témoin
`tromperie-difference_moyennes-c2`) et `enjeux-difference_moyennes-c0` (la principale est le témoin).

- **Cas sain** : les deux bras établis, paliers « identique » (sondes refaites, témoin, 4 directions de P3 redonnées au bit
  près), n directions neuves sous la graine de T0.7 « plancher/<sonde> », reproductibles et autres sous une autre graine ;
  réglages de torch rétablis à la sortie ; fichier des planchers scellé, relu.
- **Artefacts (R5)**, chacun arrête le seul bras qu'il touche, motif écrit, aucune bascule vers les directions de P3 :
  bruit de « carte » (10⁻³ par jeton : palier « carte », réserve écrite ; principale linéaire : échec si « decisive »,
  réserve si « rapportee ») ; bruit fort (0,3) ; empan décalé d'un jeton ; autre couche ; graine des directions de P3 autre
  (seconde garde seule) ; seconde garde sans objet (graine absente) ; entrées fautives (données de P3 absentes, empreinte
  du manifeste fausse, faits exclus autres, effectifs autres, principale autre).
- Configuration `plancher_figees` (cas sain et refus) ; paliers ; écriture des planchers.
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import entrainement as en
from controle_ia.premier_test_ia.figees import lire_sondes
from controle_ia.scellement import verifier
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.t07 import reextraction_p3_v1 as rx

RACINE_DEPOT = Path(__file__).resolve().parents[1]
RUN_P3 = "20261017-120000-p3-jouet"
DONNEES = ("donnees/T0.7-faits-repe-v1/facts_true_false.csv", "donnees/T0.7-models-under-pressure-v1/training/train.jsonl")
N_NEUF = 40
GRAINE_T07 = 987654321


def _git(racine, *args):
    subprocess.run(["git", *args], cwd=racine, check=True, capture_output=True)


@pytest.fixture(scope="module")
def p3(tmp_path_factory):
    """Un run jouet de P3 (lanceur de P3 tel quel), données génériques liées sous la racine."""
    for rel in DONNEES:
        if not (RACINE_DEPOT / rel).is_file():
            pytest.skip(f"{rel} absent de l'extraction (données de P3)")
    from controle_ia.premier_test_ia import run as rp
    import test_premier_test_ia_run as tr
    d = tmp_path_factory.mktemp("p3jouet")
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@e.invalid")
    _git(d, "config", "user.name", "t")
    (d / "README").write_text("x\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "init")
    vraie = rp.creer_manifeste
    rp.creer_manifeste = lambda *a, entropie=None, **k: vraie(*a, entropie=20261017 if entropie is None else entropie, **k)
    try:
        f = tr._taches(d)
        _git(d, "add", "-A")
        _git(d, "commit", "-q", "-m", "taches")
        rp.executer(tr._config(d), d, RUN_P3, None, str(f), autoriser_depot_sale=True)
    finally:
        rp.creer_manifeste = vraie
    for rel in DONNEES:
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        for suf in ("", ".sha256"):
            os.symlink(RACINE_DEPOT / (rel + suf), d / (rel + suf))
    r = json.loads((d / f"diag/{RUN_P3}/sondes-figees.json").read_text())["resultat"]
    assert r["principales"] == {"tromperie": "tromperie-lineaire-c2", "enjeux": "enjeux-difference_moyennes-c0"}
    return d


def _cite(d, rel):
    return {"chemin": rel, "sha256": verifier(d / rel)}


def _config(d, garde="decisive", n_p3=4):
    leg = f"donnees/{RUN_P3}/sondes-figees-legeres.npz"
    return {"mode": "jouet", "sondes_par_concept": {"tromperie": "tromperie-lineaire-c2", "enjeux": "enjeux-difference_moyennes-c0",
                                                    "dissimulation": None, "domaine": None},
            "planchers_p3": _cite(d, leg), "fichiers_sondes": [_cite(d, leg)],
            "donnees_p3": {"faits": _cite(d, DONNEES[0]), "enjeux": _cite(d, DONNEES[1]), "manifeste_p3": _cite(d, f"runs/{RUN_P3}/manifeste.json"),
                           "sondes_figees_p3": _cite(d, f"diag/{RUN_P3}/sondes-figees.json")},
            rx.CLE_CONFIG: {"methode": rx.METHODE, "n_p3": n_p3, "tolerances": dict(rx.TOLERANCES), "garde_principale": garde}}


def _figees(d):
    s, _, _ = lire_sondes(d / f"donnees/{RUN_P3}/sondes-figees-legeres.npz")
    par = {x.nom: x for x in s}
    return {"tromperie": par["tromperie-lineaire-c2"], "enjeux": par["enjeux-difference_moyennes-c0"]}


def _lancer(d, config=None, graines=None, **kw):
    vus = []

    def graine_de(cle):
        vus.append(cle)
        return (graines or {}).get(cle, GRAINE_T07)
    r = rx.reextraire(d, config or _config(d), _figees(d), graine_de, N_NEUF, **kw)
    return r, vus


def _bruit(r: float, graine: int = 3):
    rng = np.random.default_rng(graine)

    def extraire(modele, exemples, couches, echeance=None):
        sortie = en.extraire(modele, exemples, couches, echeance)
        for c in sortie:
            for i, a in enumerate(sortie[c]):
                e = rng.standard_normal(a.shape)
                e *= r * np.linalg.norm(a, axis=1, keepdims=True) / np.maximum(np.linalg.norm(e, axis=1, keepdims=True), 1e-30)
                sortie[c][i] = (a.astype(np.float64) + e).astype(np.float32)
        return sortie
    return extraire


# ------------------------------------------------------------------------------------------------------------------ cas sain
def test_cas_sain_identique_et_directions_neuves(p3):
    import torch
    det, fils = torch.are_deterministic_algorithms_enabled(), torch.get_num_threads()
    r, vus = _lancer(p3)
    assert (torch.are_deterministic_algorithms_enabled(), torch.get_num_threads()) == (det, fils)       # réglages rétablis
    assert r["rapport"]["etat"] == "établi"
    assert sorted(vus) == ["plancher/enjeux-difference_moyennes-c0", "plancher/tromperie-lineaire-c2"]
    for nom, v in r["par_sonde"].items():
        assert v["etat"] == "établi" and v["palier"] == "identique" and v["reserve"] is None, (nom, v.get("motif"))
        assert v["garde_identite"]["palier"] == "identique" and v["garde_identite"]["ecart_max"] == 0.0
        assert v["garde_principale"]["palier"] == "identique"
        assert v["garde_directions_p3"]["palier"] == "identique" and v["garde_directions_p3"]["identiques"] == 4
        assert v["n"] == N_NEUF and [p.nom for p in v["directions"]] == [f"{nom}{rx.SUFFIXE_PLANCHER}-plancher-{k}" for k in range(N_NEUF)]
    t = r["par_sonde"]["tromperie-lineaire-c2"]
    assert t["garde_identite"]["sonde"] == "tromperie-difference_moyennes-c2" and t["garde_principale"]["sonde"] == "tromperie-lineaire-c2"
    assert r["par_sonde"]["enjeux-difference_moyennes-c0"]["garde_principale"]["role"] == "la principale est le témoin"
    assert r["rapport"]["donnees"]["tromperie"] == {"exemples": 20, "entrainement": 16, "validation": 4}
    assert r["rapport"]["reglages"]["reglages"]["deterministe"] is True
    json.dumps(rx.rapport_serialisable(r), ensure_ascii=False)


def test_directions_neuves_reproductibles_sous_la_graine_de_t07(p3):
    a, _ = _lancer(p3)
    b, _ = _lancer(p3)
    c, _ = _lancer(p3, graines={"plancher/tromperie-lineaire-c2": GRAINE_T07 + 1})
    for nom in a["par_sonde"]:
        wa = np.stack([p.w for p in a["par_sonde"][nom]["directions"]])
        assert np.array_equal(wa, np.stack([p.w for p in b["par_sonde"][nom]["directions"]]))
    wa = np.stack([p.w for p in a["par_sonde"]["tromperie-lineaire-c2"]["directions"]])
    wc = np.stack([p.w for p in c["par_sonde"]["tromperie-lineaire-c2"]["directions"]])
    assert not np.array_equal(wa, wc)
    # recette gardée : `plancher_apparie` sur les jetons réextraits, sous la graine de T0.7
    captes = {}

    def capter(modele, exemples, couches, echeance=None):
        sortie = en.extraire(modele, exemples, couches, echeance)
        captes[tuple(couches)] = sortie[couches[0]]
        return sortie
    d, _ = _lancer(p3, extraire=capter)
    for nom, couche in (("tromperie-lineaire-c2", 2), ("enjeux-difference_moyennes-c0", 0)):
        attendu = plancher_apparie(f"{nom}{rx.SUFFIXE_PLANCHER}", couche, captes[(couche,)], "max", N_NEUF, GRAINE_T07)
        assert [(p.nom, p.w.tobytes(), p.b) for p in d["par_sonde"][nom]["directions"]] == [(p.nom, p.w.tobytes(), p.b) for p in attendu]


def test_ecrire_planchers_scelle_et_relu(p3, tmp_path):
    r, _ = _lancer(p3)
    f = rx.ecrire_planchers(tmp_path, "20270101-000000-t07-lecture-jouet", r)
    assert f["directions"] == {n: N_NEUF for n in r["par_sonde"]}
    sondes, meta, sha = lire_sondes(tmp_path / f["chemin"], f["sha256"])
    assert len(sondes) == 2 * N_NEUF and meta["methode"] == rx.METHODE and set(meta["graines"].values()) == {
        "plancher/tromperie-lineaire-c2", "plancher/enjeux-difference_moyennes-c0"}
    with pytest.raises(GardeArret, match="R12"):
        rx.ecrire_planchers(tmp_path, "20270101-000000-t07-lecture-jouet", r)
    vide = {"par_sonde": {n: {**v, "etat": "échec"} for n, v in r["par_sonde"].items()}}
    assert rx.ecrire_planchers(tmp_path, "autre", vide) is None


# ------------------------------------------------------------------------------------------------------------------ artefacts
def test_bruit_de_carte_palier_carte_et_reserve(p3):
    """Bruit de 10⁻⁴ par jeton (seuils v8, R-2305 : sur le jouet, 16 exemples, le témoin y vaut ≈ 3 × 10⁻⁴) : témoin et
    directions au palier « carte » (réserve « cause non établie ») ; la principale linéaire, recette chaotique, s'écarte au-delà
    du processeur : réserve si « rapportee », échec si « decisive »."""
    r, _ = _lancer(p3, config=_config(p3, "rapportee"), extraire=_bruit(1e-4))
    assert "cause non établie" in rx.RESERVE_CARTE and "présumé" not in rx.RESERVE_CARTE          # CLP3-01 (R-2305)
    assert rx.TOLERANCES == {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}
    for nom, v in r["par_sonde"].items():
        assert v["etat"] == "établi" and v["palier"] == "carte" and v["reserve"] == rx.RESERVE_CARTE, nom
        assert 1e-6 < v["garde_identite"]["ecart_max"] <= rx.TOLERANCES["carte_sonde"]
        assert v["garde_identite"]["palier"] == v["garde_directions_p3"]["palier"] == "carte"
    t = r["par_sonde"]["tromperie-lineaire-c2"]
    assert t["garde_principale"]["palier"] == "échec" and t["garde_principale"]["ecart_max"] > 1e-3
    assert "rapportée, non décisive" in t["reserve_principale"]
    r2, _ = _lancer(p3, config=_config(p3, "decisive"), extraire=_bruit(1e-4))
    t2 = r2["par_sonde"]["tromperie-lineaire-c2"]
    assert t2["etat"] == "échec" and "R11" in t2["motif"] and t2["directions"] is None
    assert r2["par_sonde"]["enjeux-difference_moyennes-c0"]["etat"] == "établi" and r2["rapport"]["etat"] == "partiel"


def test_temoin_seul_decisif_sans_seconde_garde(p3, monkeypatch):
    """Seconde garde sans objet, principale rapportée : le témoin seul porte la garde ; bruit fort → échec."""
    vraie = rx.lire_p3

    def sans(racine, d):
        x = vraie(racine, d)
        x["graines"] = {k: v for k, v in x["graines"].items() if not k.startswith("plancher/")}
        return x
    monkeypatch.setattr(rx, "lire_p3", sans)
    r, _ = _lancer(p3, config=_config(p3, "rapportee"), extraire=_bruit(0.3))
    t = r["par_sonde"]["tromperie-lineaire-c2"]
    assert t["garde_directions_p3"]["palier"] == "sans objet" and t["garde_identite"]["palier"] == "échec" and t["etat"] == "échec"
    r, _ = _lancer(p3, config=_config(p3, "rapportee"))
    assert all(v["etat"] == "établi" and v["garde_directions_p3"]["palier"] == "sans objet" for v in r["par_sonde"].values())


def test_bruit_fort_echec_des_deux_bras(p3):
    r, _ = _lancer(p3, extraire=_bruit(0.3))
    assert r["rapport"]["etat"] == "échec"
    for v in r["par_sonde"].values():
        assert v["etat"] == "échec" and v["directions"] is None and "aucune bascule" in v["motif"]
        assert v["garde_identite"]["palier"] == "échec"


def test_empan_decale_d_un_jeton(p3):
    def decale(modele, exemples, couches, echeance=None):
        assert all(x["debut"] >= 1 for x in exemples)
        return en.extraire(modele, [{**x, "debut": x["debut"] - 1, "fin": x["fin"] - 1} for x in exemples], couches, echeance)
    r, _ = _lancer(p3, extraire=decale)
    assert all(v["etat"] == "échec" for v in r["par_sonde"].values())


def test_autre_couche(p3):
    def autre(modele, exemples, couches, echeance=None):
        sortie = en.extraire(modele, exemples, [1], echeance)
        return {c: sortie[1] for c in couches}
    r, _ = _lancer(p3, extraire=autre)
    assert all(v["etat"] == "échec" for v in r["par_sonde"].values())


def test_seconde_garde_seule_graine_autre(p3, monkeypatch):
    vraie = rx._graine_p3
    monkeypatch.setattr(rx, "_graine_p3", lambda p, cle: vraie(p, cle) + (1 if cle == "plancher/tromperie" else 0))
    r, _ = _lancer(p3)
    t = r["par_sonde"]["tromperie-lineaire-c2"]
    assert t["etat"] == "échec" and t["garde_identite"]["palier"] == "identique" and t["garde_directions_p3"]["palier"] == "échec"
    assert r["par_sonde"]["enjeux-difference_moyennes-c0"]["etat"] == "établi" and r["rapport"]["etat"] == "partiel"


def test_seconde_garde_sans_objet_si_graine_absente(p3, monkeypatch):
    vraie = rx.lire_p3

    def sans(racine, d):
        x = vraie(racine, d)
        x["graines"] = {k: v for k, v in x["graines"].items() if k != "plancher/enjeux"}
        return x
    monkeypatch.setattr(rx, "lire_p3", sans)
    r, _ = _lancer(p3)
    e = r["par_sonde"]["enjeux-difference_moyennes-c0"]
    assert e["etat"] == "établi" and e["garde_directions_p3"]["palier"] == "sans objet"


@pytest.mark.parametrize("faute", ["donnees_absentes", "manifeste_faux", "faits_exclus", "effectifs", "principale_autre"])
def test_fautes_d_entree_arretent_les_deux_bras(p3, monkeypatch, faute):
    config = _config(p3)
    figees = _figees(p3)
    if faute == "donnees_absentes":
        config["donnees_p3"] = None
    elif faute == "manifeste_faux":
        config["donnees_p3"]["manifeste_p3"]["sha256"] = "0" * 64
    elif faute == "faits_exclus":
        vraie = en.preparer_tromperie
        monkeypatch.setattr(en, "preparer_tromperie", lambda fmt, ex, rf: (lambda r: (r[0], r[1] + ["fait-0"]))(vraie(fmt, ex, rf)))
    elif faute == "effectifs":
        vraie = rx.lire_p3

        def autre(racine, d):
            x = vraie(racine, d)
            x["resultat"] = {**x["resultat"], "effectifs": {**x["resultat"]["effectifs"], "enjeux": {"entrainement": 18, "validation": 6}}}
            return x
        monkeypatch.setattr(rx, "lire_p3", autre)
    else:
        s, _, _ = lire_sondes(p3 / f"donnees/{RUN_P3}/sondes-figees-legeres.npz")
        figees["tromperie"] = next(x for x in s if x.nom == "tromperie-difference_moyennes-c2")
    r = rx.reextraire(p3, config, figees, lambda cle: GRAINE_T07, N_NEUF)
    assert r["rapport"]["etat"] == "échec"
    for v in r["par_sonde"].values():
        assert v["etat"] == "échec" and v["directions"] is None and v["motif"].startswith("réextraction impossible")


# --------------------------------------------------------------------------------------------------------------- configuration
def test_exiger_config_cas_sain_et_refus():
    bon = {"methode": rx.METHODE, "n_p3": 200, "tolerances": dict(rx.TOLERANCES), "garde_principale": "rapportee"}
    rx.exiger_config(bon, "reel")
    rx.exiger_config({**bon, "garde_principale": "decisive"}, "reel")
    rx.exiger_config({**bon, "n_p3": 24, "tolerances": {"processeur": 1e-5, "carte_sonde": 0.1, "carte_directions": 0.2}}, "jouet")
    for faux, motif in (({**bon, "methode": "directions_p3"}, "seule admise"), ({**bon, "n_p3": 24}, "200 en mode réel"),
                        ({**bon, "n_p3": True}, "200 en mode réel"), ({**bon, "garde_principale": "aucune"}, "attendu"),
                        ({**bon, "tolerances": {**rx.TOLERANCES, "carte_sonde": 0.05}}, "fixées d'avance"),
                        ({**bon, "tolerances": {"processeur": 1e-6}}, "clés"), ({k: v for k, v in bon.items() if k != "n_p3"}, "clés"),
                        ({**bon, "tolerances": {**rx.TOLERANCES, "processeur": 0.5}}, "processeur < carte"),
                        ({**bon, "tolerances": {**rx.TOLERANCES, "carte_directions": 1.0}}, r"\]0, 1\[")):
        with pytest.raises(GardeArret, match=motif):
            rx.exiger_config(faux, "reel")


def test_paliers():
    tol = dict(rx.TOLERANCES)
    i = {"identique": True, "ecart": 0.0, "motif": None}
    p = {"identique": False, "ecart": 1e-9, "motif": None}
    c = {"identique": False, "ecart": 5e-3, "motif": None}
    e = {"identique": False, "ecart": 5e-2, "motif": None}
    m = {"identique": False, "ecart": float("inf"), "motif": "famille"}
    assert rx.palier([i, i], 1e-2, tol) == ("identique", 0.0)
    assert rx.palier([i, p], 1e-2, tol)[0] == "processeur"
    assert rx.palier([p, c], 1e-2, tol)[0] == "carte"
    assert rx.palier([c, e], 1e-2, tol)[0] == "échec"
    assert rx.palier([c], tol["processeur"], tol)[0] == "échec"                 # principale chaotique : aucun palier « carte »
    assert rx.palier([i, m], 1e-2, tol)[0] == "échec"
    with pytest.raises(GardeArret):
        rx.palier([], 1e-2, tol)


@pytest.mark.parametrize("faute", ["lignes_enjeux", "exemples", "mode", "temoin_absent"])
def test_autres_fautes_d_entree(p3, monkeypatch, faute):
    """Autres gardes d'entrée, chacune sur son artefact (cas sain : `test_cas_sain_identique_et_directions_neuves`)."""
    config = _config(p3)
    if faute == "lignes_enjeux":
        from controle_ia.premier_test_ia import donnees as dn
        vraie = dn.tirer_enjeux
        monkeypatch.setattr(dn, "tirer_enjeux", lambda lignes, rng, n: list(reversed(vraie(lignes, rng, n))))
    elif faute == "exemples":
        vraie = rx.lire_p3

        def autre(racine, d):
            x = vraie(racine, d)
            x["resultat"] = {**x["resultat"], "donnees": {**x["resultat"]["donnees"], "exemples_tromperie": 21}}
            return x
        monkeypatch.setattr(rx, "lire_p3", autre)
    elif faute == "mode":
        vraie = rx.lire_p3

        def autre(racine, d):
            x = vraie(racine, d)
            x["config"] = {**x["config"], "mode": "reel"}
            return x
        monkeypatch.setattr(rx, "lire_p3", autre)
    else:
        vraie = rx._temoin
        monkeypatch.setattr(rx, "_temoin", lambda racine, cfg, c, s: vraie(racine, cfg, "absent" if c == "tromperie" else c, s))
    r = rx.reextraire(p3, config, _figees(p3), lambda cle: GRAINE_T07, N_NEUF)
    if faute == "temoin_absent":
        t = r["par_sonde"]["tromperie-lineaire-c2"]
        assert t["etat"] == "échec" and "témoin absent-difference_moyennes-c2 absent" in t["motif"]
        assert r["par_sonde"]["enjeux-difference_moyennes-c0"]["etat"] == "établi"     # la principale y est le témoin
    else:
        assert r["rapport"]["etat"] == "échec" and all(v["etat"] == "échec" for v in r["par_sonde"].values())


@pytest.mark.parametrize("deterministe", [False, True])
def test_reglages_de_torch_retablis_apres_la_reextraction(p3, deterministe):
    """`reglages_de_p3` pose les réglages de P3 (algorithmes déterministes) puis rétablit ceux du processus, quels qu'ils soient."""
    import torch
    avant = torch.are_deterministic_algorithms_enabled()
    try:
        torch.use_deterministic_algorithms(deterministe)
        with rx.reglages_de_p3(1, "cpu") as r:
            assert torch.are_deterministic_algorithms_enabled() is True and r["reglages"]["deterministe"] is True
        assert torch.are_deterministic_algorithms_enabled() is deterministe
        _lancer(p3)
        assert torch.are_deterministic_algorithms_enabled() is deterministe
    finally:
        torch.use_deterministic_algorithms(avant)


def test_bruit_de_1e3_arrete_sur_le_jouet_aux_seuils_v8(p3):
    """Seuils v8 (R-2305) : sur le jouet (16 et 19 exemples), un bruit de 10⁻³ par jeton porte le témoin au-delà de 10⁻³ :
    les deux bras s'arrêtent (aux effectifs réels, le calibrage v3 le fait passer : témoin ≤ 4,4 × 10⁻⁴)."""
    r, _ = _lancer(p3, config=_config(p3, "rapportee"), extraire=_bruit(1e-3))
    assert all(v["etat"] == "échec" and v["garde_identite"]["palier"] == "échec" for v in r["par_sonde"].values())


def test_palier_global_le_pire_des_gardes(p3, monkeypatch):
    """n25c (R-2305) : témoin « identique » et directions au palier « carte » → palier du bras « carte », réserve écrite."""
    vraie = rx.garde_directions

    def carte(redonnees, figees, h_max, tol):
        g = vraie(redonnees, figees, h_max, tol)
        assert g["palier"] == "identique"
        return {**g, "palier": "carte", "ecart_max": 5e-3}
    monkeypatch.setattr(rx, "garde_directions", carte)
    r, _ = _lancer(p3)
    for v in r["par_sonde"].values():
        assert v["garde_identite"]["palier"] == "identique" and v["garde_directions_p3"]["palier"] == "carte"
        assert v["etat"] == "établi" and v["palier"] == "carte" and v["reserve"] == rx.RESERVE_CARTE


@pytest.mark.parametrize("exc", [MemoryError, TypeError, AttributeError, IndexError])
def test_fautes_hors_garde_arretent_le_seul_bras(p3, monkeypatch, exc):
    """Note 07 (R-2305) : `MemoryError`, `TypeError`, `AttributeError`, `IndexError` arrêtent le seul bras (motif écrit, type
    compris), jamais l'étape A ; à l'extraction : les deux bras ; au tirage d'un bras : ce bras seul."""
    def casse(*a, **k):
        raise exc("artefact")
    r = rx.reextraire(p3, _config(p3), _figees(p3), lambda cle: GRAINE_T07, N_NEUF, extraire=casse)
    assert all(v["etat"] == "échec" and exc.__name__ in v["motif"] for v in r["par_sonde"].values())
    vraie = rx.plancher_apparie
    monkeypatch.setattr(rx, "plancher_apparie", lambda nom, *a, **k: (_ for _ in ()).throw(exc("tirage")) if nom.startswith("tromperie")
                        else vraie(nom, *a, **k))
    r, _ = _lancer(p3)
    t, e = r["par_sonde"]["tromperie-lineaire-c2"], r["par_sonde"]["enjeux-difference_moyennes-c0"]
    assert t["etat"] == "échec" and exc.__name__ in t["motif"] and e["etat"] == "établi"


def test_controle_avant_ouverture_cas_sain_et_artefacts(p3, tmp_path):
    """CLP3-03 (R-2305) : entrées de la réextraction contrôlées avant l'ouverture (jouet : cache sans objet)."""
    c = _config(p3)
    r = rx.controler_avant_ouverture(p3, c)
    assert set(r["figees"]) == {"tromperie-lineaire-c2", "enjeux-difference_moyennes-c0"}
    assert r["figees"]["tromperie-lineaire-c2"]["temoin"] == "tromperie-difference_moyennes-c2"
    assert all(x["directions_p3"] == 4 and x["graine_seconde_garde"] for x in r["figees"].values())
    assert r["modele_p3"]["etat"].startswith("sans objet")
    fautes = []
    x = _config(p3); x["donnees_p3"] = None; fautes.append((x, "donnees_p3"))
    x = _config(p3); x["donnees_p3"]["sondes_figees_p3"]["sha256"] = "0" * 64; fautes.append((x, "empreinte"))
    x = _config(p3); x["sondes_par_concept"]["tromperie"] = "tromperie-difference_moyennes-c2"; fautes.append((x, "principale de P3"))
    x = _config(p3, n_p3=5); fautes.append((x, "directions"))
    x = _config(p3); del x[rx.CLE_CONFIG]; fautes.append((x, "absente"))
    for cfg, motif in fautes:
        with pytest.raises(GardeArret, match=motif):
            rx.controler_avant_ouverture(p3, cfg)
    vrai = rx._temoin
    try:                                                        # témoin absent du fichier léger
        rx._temoin = lambda racine, cfg, c, s: vrai(racine, cfg, "absent" if c == "tromperie" else c, s)
        with pytest.raises(GardeArret, match="témoin absent-difference_moyennes"):
            rx.controler_avant_ouverture(p3, _config(p3))
    finally:
        rx._temoin = vrai


def _cache(base, modele, revision, fichiers):
    d = base / ("models--" + modele.replace("/", "--")) / "snapshots" / revision
    d.mkdir(parents=True)
    for nom, contenu in fichiers.items():
        (d / nom).write_text(contenu, encoding="utf-8")
    return base


REV = "0e9e39f249a16976918f6564b8830bc894c89659"
COMPLET = {"config.json": "{}", "tokenizer.json": "{}", "tokenizer_config.json": "{}",
           "model.safetensors.index.json": json.dumps({"weight_map": {"a": "model-00001-of-00002.safetensors",
                                                                       "b": "model-00002-of-00002.safetensors"}}),
           "model-00001-of-00002.safetensors": "x", "model-00002-of-00002.safetensors": "x"}


def test_revision_au_cache_cas_sain_et_artefacts(tmp_path, monkeypatch):
    """CLP3-03 : révision du modèle de P3 au cache local, lue hors ligne (cache factice ; aucun accès au réseau)."""
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    sain = _cache(tmp_path / "sain", "org/nom", REV, COMPLET)
    r = rx.revision_au_cache("org/nom", REV, str(sain))
    assert r["poids"] == 2 and r["dossier"].endswith(REV)
    with pytest.raises(GardeArret, match="absent du cache local"):
        rx.revision_au_cache("org/nom", "1" * 40, str(sain))
    with pytest.raises(GardeArret, match="absent du cache local"):
        rx.revision_au_cache("org/autre", REV, str(sain))
    partiel = _cache(tmp_path / "partiel", "org/nom", REV, {k: v for k, v in COMPLET.items() if k != "model-00002-of-00002.safetensors"})
    with pytest.raises(GardeArret, match="incomplet"):
        rx.revision_au_cache("org/nom", REV, str(partiel))
    sans_tok = _cache(tmp_path / "sans-tok", "org/nom", REV, {k: v for k, v in COMPLET.items() if k != "tokenizer.json"})
    with pytest.raises(GardeArret, match="tokenizer.json"):
        rx.revision_au_cache("org/nom", REV, str(sans_tok))
    sans_poids = _cache(tmp_path / "sans-poids", "org/nom", REV, {k: v for k, v in COMPLET.items() if "safetensors" not in k})
    with pytest.raises(GardeArret, match="safetensors"):
        rx.revision_au_cache("org/nom", REV, str(sans_poids))


def test_controle_avant_ouverture_en_mode_reel_lit_le_cache(p3, monkeypatch):
    """CLP3-03 : en mode réel, la révision de l'agent de P3 est cherchée au cache (ici : appel intercepté, cas sain et artefact)."""
    vus = []
    monkeypatch.setattr(rx, "revision_au_cache", lambda m, r, c=None: vus.append((m, r)) or {"modele": m, "revision": r})
    monkeypatch.setattr(rx, "exiger_config", lambda pf, mode: None)
    monkeypatch.setattr(rx.d3, "exiger_config", lambda d, mode: None)
    c = {**_config(p3), "mode": "reel"}
    r = rx.controler_avant_ouverture(p3, c)
    agent = json.loads((p3 / f"runs/{RUN_P3}/manifeste.json").read_text())["config"]["agent"]
    assert vus == [(str(agent.get("modele")), str(agent.get("revision")))] and r["modele_p3"]["modele"] == vus[0][0]
    monkeypatch.setattr(rx, "revision_au_cache", lambda m, r, c=None: (_ for _ in ()).throw(GardeArret("absent du cache local")))
    with pytest.raises(GardeArret, match="absent du cache local"):
        rx.controler_avant_ouverture(p3, c)
