"""Lanceur de P3-bis sans échéance (`premier_test_ia.run_v2` ; texte de P3-bis, brouillon 6, « Ce que le code et la chaîne
doivent changer », point 2 (a)), mode jouet, dépôt jetable (R5) : `null` accepté pour les deux durées (cas sain), toute autre
valeur contrôlée par la garde de P3 avec son message (0, négatif, au-delà de 18 000, booléen, texte : artefacts) ; run de bout
en bout sans échéance malgré une horloge avancée d'un milliard de secondes (cas sain), et la même avance qui arrête encore un
run à borne numérique (artefact : une borne non nulle arrête encore) ; manifeste à `null`, commande de `run_v2`, aucun infini
écrit ; copie d'`executer` comparée ligne à ligne à celle de P3 ; garde de P3 inchangée (`null` toujours refusé par
`run.exiger_config_p3`) ; mode décisif et point d'entrée."""
import json
import math
import subprocess
import time
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import lire_manifeste
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia import run_v2 as rv
from controle_ia.scellement import sceller
from test_premier_test_ia_run import _config, _prereg, _taches

RACINE = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def entropie_fixe(monkeypatch):
    """Comme dans les essais de P3 : entropie fixée sans préenregistrement (deux classes en validation sur le jouet)."""
    vraie = rv.creer_manifeste

    def creer(*a, entropie=None, **k):
        return vraie(*a, entropie=20261017 if entropie is None else entropie, **k)

    monkeypatch.setattr(rv, "creer_manifeste", creer)


def _sans_echeance(c):
    return dict(c, duree_max_s=None, budget_entrainement_s=None)


def test_garde_de_configuration_null_accepte_autres_valeurs_refusees(tmp_path):
    c = _config(tmp_path)
    rv.exiger_config_p3bis(_sans_echeance(c))                       # les deux durées à null
    rv.exiger_config_p3bis(c)                                       # valeurs numériques de P3 : acceptées, comme dans P3
    for cle in rv.DUREES:
        rv.exiger_config_p3bis(dict(c, **{cle: None}))              # une seule à null
        rv.exiger_config_p3bis(dict(c, **{cle: rp.DUREE_MAX_S}))
        for v in (0, -5, rp.DUREE_MAX_S + 1, True, "900"):
            with pytest.raises(GardeArret, match=f"{cle} .* un nombre dans"):
                rv.exiger_config_p3bis(dict(_sans_echeance(c), **{cle: v}))
        x = _sans_echeance(c)
        del x[cle]
        with pytest.raises(GardeArret, match="configuration de P3 incomplète"):
            rv.exiger_config_p3bis(x)                               # absente n'est pas null
        with pytest.raises(GardeArret, match=f"{cle} None : un nombre dans"):
            rp.exiger_config_p3(dict(c, **{cle: None}))             # P3 inchangé : null y reste refusé
    with pytest.raises(GardeArret, match="mode 'autre' inconnu"):
        rv.exiger_config_p3bis(dict(_sans_echeance(c), mode="autre"))
    with pytest.raises(GardeArret, match="conditions"):
        rv.exiger_config_p3bis(dict(_sans_echeance(c), conditions=["honnete", "saboteur", "temoin"]))
    with pytest.raises(GardeArret, match="objet JSON"):
        rv.exiger_config_p3bis([])


def test_vue_sans_echeance_ne_change_que_les_durees_nulles():
    c = {"duree_max_s": None, "budget_entrainement_s": 600, "n_plancher": 4}
    v = rv.vue_sans_echeance(c)
    assert v == {"duree_max_s": math.inf, "budget_entrainement_s": 600, "n_plancher": 4} and c["duree_max_s"] is None
    assert rv.vue_sans_echeance(_sans_echeance({"x": 1}))["budget_entrainement_s"] == math.inf


def _avancer_l_horloge_apres_le_premier_plancher(monkeypatch):
    """Horloge avancée d'un milliard de secondes dès le premier plancher (après le manifeste et le début du run)."""
    vrai_plancher, vraie_horloge, avance = rp.plancher_de, time.perf_counter, {"s": 0.0}

    def plancher(*a, **k):
        r = vrai_plancher(*a, **k)
        avance["s"] = 1e9
        return r

    monkeypatch.setattr(rp, "plancher_de", plancher)
    monkeypatch.setattr(time, "perf_counter", lambda: vraie_horloge() + avance["s"])
    return avance


def test_bout_en_bout_sans_echeance_et_borne_numerique_qui_arrete(depot, tmp_path, monkeypatch):
    f = _taches(depot)
    committer(depot)
    avance = _avancer_l_horloge_apres_le_premier_plancher(monkeypatch)
    resume = rv.executer(_sans_echeance(_config(tmp_path)), depot, "20261109-120000-p3bis-jouet", None, str(f),
                         autoriser_depot_sale=True)
    assert resume["episodes"] == 8 and resume["actions"] == 16                     # au bout, malgré l'horloge (cas sain)
    m, _ = lire_manifeste(depot / "runs" / "20261109-120000-p3bis-jouet" / "manifeste.json")
    assert m["config"]["duree_max_s"] is None and m["config"]["budget_entrainement_s"] is None
    assert m["commande"] == rv.COMMANDE == "python -m controle_ia.premier_test_ia.run_v2"
    assert resume["config_sha256"] == m["config_sha256"]
    for p in list((depot / "runs").rglob("*.json")) + list((depot / "diag").rglob("*.json")):
        assert "Infinity" not in p.read_text(encoding="utf-8")                   # aucune durée infinie écrite
    # artefact : la même avance de l'horloge arrête un run dont la borne de l'entraînement est numérique
    avance["s"] = 0.0                                          # horloge remise à l'heure : le saut se refait au plancher
    c = dict(_config(tmp_path), duree_max_s=None, budget_entrainement_s=600)
    with pytest.raises(GardeArret, match="limite de durée dépassée pendant le plancher de tromperie"):
        rv.executer(c, depot, "20261109-120001-p3bis-jouet", None, str(f), autoriser_depot_sale=True)
    a = json.loads((depot / "diag" / "20261109-120001-p3bis-jouet" / "arret.json").read_text(encoding="utf-8"))["resultat"]
    assert a["etape"] == "entraînement" and "plancher de tromperie" in a["motif"]


def test_copie_d_executer_comparee_a_celle_de_p3():
    e = rv.ecart_a_p3()
    assert e["conforme"], e
    assert e["retirees"] == [x for x, _ in rv.ECART_ATTENDU] and e["ajoutees"] == [y for _, y in rv.ECART_ATTENDU]
    assert e["lignes_p3"] == e["lignes_p3bis"] and len(e["retirees"]) == 3
    assert rv._executer_apres_manifeste is rp._executer_apres_manifeste                  # importée, jamais recopiée


def test_mode_decisif_configuration_citee_a_null(depot, tmp_path, monkeypatch):
    """Le texte cite la configuration à null : le lanceur v2 la lance (cas sain), le lanceur de P3 la refuse (artefact :
    garde de P3 inchangée) ; une configuration à null mais d'une autre empreinte est refusée par la citation."""
    monkeypatch.setattr(rv, "exiger_code_importe_sous", lambda racine: None)
    c = _sans_echeance(_config(tmp_path))
    f = _taches(depot)
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    sha_t = subprocess.run(["sha256sum", str(f)], capture_output=True, text=True).stdout.split()[0]
    sain = _prereg(depot, commit, c, sha_t, nom="p3bis.md")
    autre = _prereg(depot, commit, dict(c, n_plancher=5), sha_t, nom="p3bis-autre.md")
    committer(depot)
    with pytest.raises(GardeArret, match="configuration .* citée"):
        rv.executer(c, depot, "20261109-120002-x", str(autre), str(f))
    with pytest.raises(GardeArret, match="duree_max_s None"):
        rp.executer(c, depot, "20261109-120003-x", str(sain), str(f))
    assert not (depot / "runs" / "20261109-120002-x").exists() and not (depot / "runs" / "20261109-120003-x").exists()
    m = rv.executer(c, depot, "20261109-120004-x", str(sain), str(f), autoriser_depot_sale=True)
    assert m["commit_cite"] == commit


def test_point_d_entree(depot, tmp_path, monkeypatch, capsys):
    """Le point d'entrée lit les données génériques sous `donnees/` du dossier courant (chemins relatifs de P3) : le dépôt
    jetable les reçoit par des liens vers celles du dépôt (fichiers suivis par git, présents dans tout clone neuf)."""
    (depot / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    (depot / "donnees").mkdir()
    for d in ("T0.7-faits-repe-v1", "T0.7-models-under-pressure-v1"):
        (depot / "donnees" / d).symlink_to(RACINE / "donnees" / d, target_is_directory=True)
    c = _sans_echeance(_config(tmp_path))
    cfg = depot / "config-p3bis.json"
    cfg.write_text(json.dumps(c), encoding="utf-8")
    sceller(cfg)
    f = _taches(depot)
    committer(depot)
    monkeypatch.chdir(depot)
    monkeypatch.setattr(rv.signal, "signal", lambda *a: None)                 # gestionnaire de TERM : pas dans pytest
    assert rv._main(["--config", str(cfg), "--taches", str(f), "--run-id", "20261109-120005-p3bis-jouet"]) == 0
    assert json.loads(capsys.readouterr().out)["episodes"] == 8
    with pytest.raises(SystemExit):
        rv._main(["--config", str(cfg), "--run-id", "20261109-120006-x"])          # --taches exigé, comme dans P3
