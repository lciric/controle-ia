"""Essais de comportement des notes 05 et 10 (contre-lecture courte des corrections, CLC-P3-06, R-2311) — v1, fichier neuf.

Ces deux corrections n'étaient tenues que par le miroir (mutations c14 et c17 survivantes sans lui). Ici, sans le miroir :

- **note 05** : l'étape B, jouée par la commande sur le faux run de 7b après une vraie étape A, s'arrête quand un plancher
  décisif n'a pas `n_plancher` directions — tableau ouvert tronqué d'une direction, ou configuration de l'étape B qui annonce
  un autre `n_plancher` que celui de l'étape A — motif écrit, aucune lecture écrite ; cas sain : la même étape B, sans
  artefact, va au bout (code 0, lecture écrite) ;
- **note 10** : `etape-a-apres-repli` (et `etape-a`) affichent l'état des planchers des sondes figées sur leur ligne de sortie,
  rapport du repli transmis à l'étape A.
"""
from __future__ import annotations

import json

from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v4 as lv4
from controle_ia.t07 import repli_etapes_v2 as rt2
from test_t07_lecture_v1 import APRES_A, INSTANT, INSTANT_B, RUN_T06
from test_t07_lecture_v2 import construire, lignes_audit, lignes_p3bis
from test_t07_plancher_v3_lecture_v1 import _config_jouet, v8


def _etape_a(j, cfg, capsys):
    assert lv4.main(["etape-a", str(j.racine), RUN_T06, str(cfg), "--registre", str(j.registre), "--instant", str(INSTANT)]) == 0
    run_t07 = sorted(p.name for p in (j.racine / "runs").iterdir() if p.name != RUN_T06)[-1]
    lignes_audit(j, run_t07)
    lignes_p3bis(j, APRES_A)
    capsys.readouterr()
    return run_t07


def _etape_b(j, cfg, run_t07, capsys):
    code = lv4.main(["etape-b", str(j.racine), RUN_T06, run_t07, str(cfg), "--registre", str(j.registre), "--instant", str(INSTANT_B)])
    s = capsys.readouterr()
    return code, s.out, s.err, (j.racine / "diag" / run_t07 / "lecture-t07.json").exists()


def test_note_05_cas_sain_etape_b_au_bout(depot, capsys):
    j = construire(depot)
    cfg = _config_jouet(j)
    run_t07 = _etape_a(j, cfg, capsys)
    code, out, err, lu = _etape_b(j, cfg, run_t07, capsys)
    assert code == lv4.CODE_OK and lu, err


def test_note_05_plancher_tronque_arrete_l_etape_b(depot, capsys, monkeypatch):
    """Tableau `plancher_<k>` d'une sonde notée ouvert avec 29 directions au lieu de 30 → arrêt de l'étape B, motif écrit."""
    j = construire(depot)
    cfg = _config_jouet(j)
    run_t07 = _etape_a(j, cfg, capsys)
    vraie, vus = lv1.ouvrir_scores, []

    def tronque(*a, **k):
        t, index = vraie(*a, **k)
        e = next(e for e in index["sondes"] if e.get("etat") == "notée")
        vus.append(e["nom"])
        t = dict(t)
        t[f"plancher_{e['rang']}"] = t[f"plancher_{e['rang']}"][:-1]
        return t, index
    monkeypatch.setattr(lv1, "ouvrir_scores", tronque)
    code, out, err, lu = _etape_b(j, cfg, run_t07, capsys)
    assert vus and code == lv4.CODE_ARRET and not lu
    assert f"plancher décisif de {vus[0]} : 29 directions, 30 attendues : arrêt" in err, err


def test_note_05_n_plancher_autre_a_l_etape_b(depot, capsys):
    """Configuration de l'étape B qui annonce 31 directions, étape A jouée à 30 → arrêt de l'étape B, motif écrit."""
    j = construire(depot)
    cfg = _config_jouet(j)
    run_t07 = _etape_a(j, cfg, capsys)
    c = json.loads(cfg.read_text(encoding="utf-8"))
    c["n_plancher"] = 31
    cfg31 = j.racine / "config-t07-n31.json"
    cfg31.write_text(json.dumps(c), encoding="utf-8")
    code, out, err, lu = _etape_b(j, cfg31, run_t07, capsys)
    assert code == lv4.CODE_ARRET and not lu
    assert "n_plancher 30 à l'étape A ≠ 31 (configuration) : arrêt" in err, err


ETAT = {"tromperie-x": "échec", "enjeux-y": "établi"}


def _faux_etape_a(vus):
    def faux(racine, registre, config, run_t06, *a, repli=None, **k):
        vus.append(repli)
        return {"scores": {"chemin": "donnees/r/scores-actions-t07.npz"}, "index": {"sondes_lues": ["s"]},
                "planchers_figees": {"etats": dict(ETAT)}}
    return faux


def test_note_10_etat_des_figees_affiche(tmp_path, capsys, monkeypatch):
    """`etape-a-apres-repli` (repli_etapes_v2) et `etape-a` (lecture_v4) écrivent « plancher des figées : {…} » ; le rapport
    du repli est transmis à l'étape A."""
    c = v8()
    c["mode"] = "jouet"
    cfg = tmp_path / "config.json"
    cfg.write_text(json.dumps(c), encoding="utf-8")
    vus = []
    monkeypatch.setattr(rt2, "lire_rapport", lambda racine, run: {"rapport": "repli"})
    monkeypatch.setattr(lv4, "etape_a", _faux_etape_a(vus))
    capsys.readouterr()
    assert lv4.main(["etape-a-apres-repli", str(tmp_path), "run", str(cfg)]) == lv4.CODE_OK
    out = capsys.readouterr().out
    assert vus == [{"rapport": "repli"}]
    assert out.strip().endswith(f"plancher des figées : {ETAT}"), out
    assert lv4.main(["etape-a", str(tmp_path), "run", str(cfg)]) == lv4.CODE_OK
    out = capsys.readouterr().out
    assert out.strip().endswith(f"plancher des figées : {ETAT}") and vus[-1] is None, out
