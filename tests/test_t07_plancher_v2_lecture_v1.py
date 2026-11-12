"""Essais de `lecture_v3.py` et `lectures_t07_v2.py` (remède (a) de T0.7 câblé dans l'étape B) — v1, fichier neuf (consigne
`consigne-code-plancher-v2-t07-v1.md`, `4efbdbf4…`, mandat, points 2 à 4).

- **Configuration** : `methode_plancher` exigée (absente → `CleAbsente` ; autre valeur → arrêt) ; configuration v6 (v5 du
  candidat 1, `4be50447…`, plus la seule clé neuve) admise par la v3 et par la v2 ; empreinte canonique de la v5 inchangée
  (`9d138bf3…`), celle de la v6 autre ; commande `empreinte-config` (code 0 sur la v6, 2 sur la v5).
- **Miroir** : `lecture_jeux_v3`, `etape_b`, `lire_avec_plancher` et `lectures` sont les fonctions de `lecture_v1`, `lecture_v2`
  et `lectures_t07_v1` à la lettre, aux seuls remplacements déclarés près.
- **`lecture_jeux_v3`** (R5) : cas sain → lectures complètes, `bas` = quantile + borne basse de la différence, `bas_sonde` =
  intervalle propre ; artefact (positifs d'une dose sur une seule tâche) → « échec » de cette seule lecture, motif de l'arrêt
  gelé tel quel ; artefact « sonde = une direction de son plancher » → « non au-dessus ».
- **Bout en bout** (faux run de 7b de `tests/test_t07_lecture_v1.py`, `lecture_v3.etape_a` puis `etape_b`) : issue de la grille,
  `methode_plancher` dans le résultat, toutes les lectures contre un plancher par la règle (a) sauf T4 (aire stratifiée, déclarée).
- **Grille** : `lecture_v3 grille` imprime exactement ce qu'imprime `lecture_v2 grille` (critères inchangés).
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07 import criteres_v1 as cr
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v2 as lv2
from controle_ia.t07 import lecture_v3 as lv3
from controle_ia.t07 import lectures_t07_v1 as lt1
from controle_ia.t07 import lectures_t07_v2 as lt2
from controle_ia.t07 import plancher_v2 as pl2
from test_t07_lecture_v1 import APRES_A
from test_t07_lecture_v2 import construire, lignes_audit, lignes_p3bis
from test_t07_lecture_v1 import INSTANT, INSTANT_B, RUN_T06
from test_t07_tirages_degeneres_v1 import _jeu_synthetique, _motif_gele

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_V5 = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-candidat1-pieces" / "configuration-t07-v5.json"
SHA_V5 = "4be50447d1063015aa8ad99970d7e803765d85964d2b58010f5731bcd8c4ff46"
CANONIQUE_V5 = "9d138bf3a635dbc0207a6bcf5cf7e436c34d3af8ce2866f96025a594cc04c681"
CANONIQUE_V6 = "7c61fcfbc8ed39d7f83832f11a79b1290d35f47f23e351e104f6dd632737b505"
METHODE = "difference_appariee_percentile"

# --------------------------------------------------------------------------------------- remplacements déclarés (miroir)
APPEL_V1 = ('                    resume = pl.comparer_scores_au_plancher(t[f"scores_{k}"][m], t[f"plancher_{k}"][:, m], y, t["tache"][m],\n'
            '                                                            int(config["tirages_aire"]), _graine(graines, f"{cle}/{nom}/{jeu}"),\n'
            '                                                            float(config["quantile_plancher"]), float(niveau))\n')
APPEL_V3 = ('                    resume = pl2.resume_pour_critere(pl2.comparer_difference_au_plancher(\n'
            '                        t[f"scores_{k}"][m], t[f"plancher_{k}"][:, m], y, t["tache"][m], int(config["tirages_aire"]),\n'
            '                        _graine(graines, f"{cle}/{nom}/{jeu}"), float(config["quantile_plancher"]), float(niveau)))\n')
JEUX = [
    ("def lecture_jeux(t: dict, index: dict, mesures: dict, config: dict, graines: dict, niveau: float, jeux_lus: list,\n"
     "                 cle:", "def lecture_jeux_v3(t: dict, index: dict, mesures: dict, config: dict, graines: dict, niveau: float,\n"
     "                    jeux_lus: list, cle:"),
    ("plancher (`comparer_scores_au_plancher`)", "plancher par la règle (a) (`plancher_v2.comparer_difference_au_plancher`,\n"
     "    `resume_pour_critere` : `bas` = quantile + borne basse de la différence)"),
    (APPEL_V1, APPEL_V3),
]
ETAPE_B = [
    ('"""Étape B, v2 (celle de `lecture_v1.etape_b`, plus G1, G3, G4, R14 et la lecture descriptive des couples figés)."""',
     '"""Étape B, v3 : celle de `lecture_v2.etape_b`, lectures au plancher par la règle (a) (`lecture_jeux_v3`, `lectures_t07_v2`) ;\n'
     '    `methode_plancher` écrite dans le résultat."""'),
    ("jeux = lv1.lecture_jeux(", "jeux = lecture_jeux_v3("),
    ("hors = lv1.lecture_jeux(", "hors = lecture_jeux_v3("),
    ("complementaires = lt.lectures(", "complementaires = lt2.lectures("),
    ("reserves_id = lt.reserves(", "reserves_id = lt2.reserves("),
    ('"couverture": cr.enumerer_couverture()}', '"couverture": cr.enumerer_couverture(), "methode_plancher": methode_plancher(config)}'),
]
APPEL_LT1 = ('        r = pl.comparer_scores_au_plancher(np.asarray(t[cle_scores])[m], np.asarray(t[cle_plancher])[:, m], y, np.asarray(t["tache"])[m],\n'
             '                                           int(config["tirages_aire"]), graine(graines, cle_graine, derivees),\n'
             '                                           float(config["quantile_plancher"]), NIVEAU)\n')
APPEL_LT2 = ('        r = pl2.resume_pour_critere(pl2.comparer_difference_au_plancher(\n'
             '            np.asarray(t[cle_scores])[m], np.asarray(t[cle_plancher])[:, m], y, np.asarray(t["tache"])[m],\n'
             '            int(config["tirages_aire"]), graine(graines, cle_graine, derivees), float(config["quantile_plancher"]), NIVEAU))\n')
LIRE = [
    ('"""Une sonde contre son plancher, à 95 %, sur `pos` contre `neg`."""',
     '"""Une sonde contre son plancher, à 95 %, sur `pos` contre `neg`, par la règle (a) (`plancher_v2`)."""'),
    (APPEL_LT1, APPEL_LT2),
    ('r["etat"] = AU_DESSUS if r["bas"] > r["plancher_quantile"] else NON_AU_DESSUS',
     'r["etat"] = AU_DESSUS if r["au_dessus_du_plancher"] else NON_AU_DESSUS'),
]
T1_V1 = ('                x = pl.comparer_scores_au_plancher(np.asarray(t[ks])[m1], np.asarray(t[kp])[:, m1], etiq[m1], np.asarray(t["tache"])[m1],\n'
         '                                                   int(config["tirages_aire"]), graine(graines, f"p15/{nom}/T1", derivees),\n'
         '                                                   float(config["quantile_plancher"]), NIVEAU)\n'
         '                x["etat"] = AU_DESSUS if x["bas"] > x["plancher_quantile"] else NON_AU_DESSUS\n')
T1_V2 = ('                x = pl2.resume_pour_critere(pl2.comparer_difference_au_plancher(\n'
         '                    np.asarray(t[ks])[m1], np.asarray(t[kp])[:, m1], etiq[m1], np.asarray(t["tache"])[m1],\n'
         '                    int(config["tirages_aire"]), graine(graines, f"p15/{nom}/T1", derivees), float(config["quantile_plancher"]),\n'
         '                    NIVEAU))\n'
         '                x["etat"] = AU_DESSUS if x["au_dessus_du_plancher"] else NON_AU_DESSUS\n')
LECTURES = [
    ("résultat de `lecture_v1.lecture_jeux` sur (i-a)", "résultat de `lecture_v3.lecture_jeux_v3` sur (i-a)"),
    (T1_V1, T1_V2),
]


def appliquer(source: str, remplacements) -> str:
    for avant, apres in remplacements:
        assert source.count(avant) == 1, avant[:80]
        source = source.replace(avant, apres)
    return source


# ---------------------------------------------------------------------------------------------------------- configuration
def config_v5() -> dict:
    brut = CONFIG_V5.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == SHA_V5
    return json.loads(brut)


def config_v6() -> dict:
    return {**config_v5(), "methode_plancher": METHODE}


def test_configuration_v6_admise_v5_refusee_empreintes():
    c5, c6 = config_v5(), config_v6()
    lv3.exiger_configuration(c6)
    lv2.exiger_configuration(c6)                 # la v2 (étape A, passe à blanc, repli) admet la clé neuve
    assert lv2.empreinte_canonique(c5) == CANONIQUE_V5 and lv2.empreinte_canonique(c6) == CANONIQUE_V6
    with pytest.raises(lv3.CleAbsente, match="methode_plancher absente"):
        lv3.exiger_configuration(c5)
    for autre in ("percentile", "bca_logit", None, ["difference_appariee_percentile"]):
        with pytest.raises(GardeArret, match="seule admise"):
            lv3.exiger_configuration({**c5, "methode_plancher": autre})
    with pytest.raises(GardeArret, match="niveau_decisif"):          # les contrôles de la v2 sont joués après
        lv3.exiger_configuration({**c6, "niveau_decisif": 0.95})
    assert lv3.CLES_CONFIG == tuple(lv2.CLES_CONFIG) + ("methode_plancher",)


def test_commande_empreinte_config_v6_et_v5(tmp_path):
    p6, p5 = tmp_path / "configuration-t07-v6.json", tmp_path / "configuration-t07-v5.json"
    p6.write_text(json.dumps(config_v6(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    p5.write_bytes(CONFIG_V5.read_bytes())
    src = Path(lv3.__file__).resolve().parents[2]                # le `src/` réellement importé (copie mutée comprise)
    env = {**{k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "HOME", "TMPDIR")},
           "PYTHONPATH": str(src), "PYTHONDONTWRITEBYTECODE": "1"}
    r6 = subprocess.run([sys.executable, "-m", "controle_ia.t07.lecture_v3", "empreinte-config", str(p6)], capture_output=True,
                        text=True, env=env)
    assert r6.returncode == 0 and r6.stdout.strip() == CANONIQUE_V6, r6.stderr
    r5 = subprocess.run([sys.executable, "-m", "controle_ia.t07.lecture_v3", "empreinte-config", str(p5)], capture_output=True,
                        text=True, env=env)
    assert r5.returncode == 2 and "methode_plancher absente" in r5.stderr


def test_grille_inchangee(capsys):
    assert lv2.main(["grille"]) == 0
    v2 = capsys.readouterr().out
    assert lv3.main(["grille"]) == 0
    assert capsys.readouterr().out == v2 and v2


# ---------------------------------------------------------------------------------------------------------------- miroir
def test_miroir_lecture_jeux_et_etape_b():
    assert inspect.getsource(lv3.lecture_jeux_v3) == appliquer(inspect.getsource(lv1.lecture_jeux), JEUX)
    assert inspect.getsource(lv3.etape_b) == appliquer(inspect.getsource(lv2.etape_b), ETAPE_B)
    assert lv3.ouvrir is lv2.ouvrir and lv3.completer_graines is lv2.completer_graines and lv3.lecture_couples is lv2.lecture_couples
    assert lv3._graine is lv1._graine and lv3.PHRASE_SUITE_FINALE == lv2.PHRASE_SUITE_FINALE


def test_miroir_lectures_t07():
    assert inspect.getsource(lt2.lire_avec_plancher) == appliquer(inspect.getsource(lt1.lire_avec_plancher), LIRE)
    assert inspect.getsource(lt2.lectures) == appliquer(inspect.getsource(lt1.lectures), LECTURES)
    for nom in ("difference", "placebo", "reserves", "_prediction_validite", "_absente", "_masque", "lectures_portant_aire"):
        assert getattr(lt2, nom) is getattr(lt1, nom), nom


def test_nouveaux_modules_sans_moyenne_ni_lecture_interdite():
    motifs = ("np.mean", ".mean(", "nanmean", "nanmedian", ".median(", "lecture-sondes-t06.json", "extraire_mesures_epreuve_t06_v1")
    for nom in ("plancher_v2.py", "lecture_v3.py", "lectures_t07_v2.py"):
        for ligne in (RACINE_DEPOT / "src" / "controle_ia" / "t07" / nom).read_text(encoding="utf-8").splitlines():
            code = ligne.split("#")[0].replace("np.median(aires)", "")
            assert not any(m in code for m in motifs), (nom, ligne)


# -------------------------------------------------------------------------------------------------------- lecture_jeux_v3
def test_lecture_jeux_v3_cas_sain_sens_de_bas():
    t, index, mesures, config, graines = _jeu_synthetique(False)
    jeux = lv3.lecture_jeux_v3(t, index, mesures, config, graines, 0.9875, [cr.JEU_I, "S75", "S100"])
    for s in jeux:
        for j, r in jeux[s].items():
            assert "echec" not in r and r["etat"] in cr.ETATS_SONDE
            d = r["difference"]
            assert d["methode"] == METHODE and r["bas"] == r["plancher"]["quantile"] + d["bas"] and r["sens_de_bas"] == pl2.SENS_DE_BAS
            assert (r["bas"] > r["plancher"]["quantile"]) is r["au_dessus_du_plancher"] is (d["bas"] > 0.0)
            v1 = lv1.lecture_jeux(t, index, mesures, config, graines, 0.9875, [j])[s][j]
            assert r["bas_sonde"] == v1["bas"] and r["haut_sonde"] == v1["haut"] and r["aire"] == v1["aire"]
            assert r["plancher"] == v1["plancher"] and r["triviaux"] == v1["triviaux"]


@pytest.mark.parametrize("cle, niveau", [("intervalle", 0.9875), ("descriptif", 0.95)])
def test_lecture_jeux_v3_artefact_degeneres_echec_motif_gele(cle, niveau):
    t, index, mesures, config, graines = _jeu_synthetique(True)
    jeux = lv3.lecture_jeux_v3(t, index, mesures, config, graines, niveau, [cr.JEU_I, "S75", "S100"], cle=cle)
    sain = lv3.lecture_jeux_v3(*_jeu_synthetique(False), niveau, [cr.JEU_I, "S100"], cle=cle)
    v1 = lv1.lecture_jeux(t, index, mesures, config, graines, niveau, ["S75"], cle=cle)
    for s in jeux:
        r = jeux[s]["S75"]
        assert r["etat"] == cr.ECHEC and _motif_gele(r["echec"]) > 2 and r["echec"] == v1[s]["S75"]["echec"]
        assert "triviaux" in r
        for j in (cr.JEU_I, "S100"):
            assert jeux[s][j]["etat"] == sain[s][j]["etat"] and jeux[s][j]["difference"] == sain[s][j]["difference"]


def test_lecture_jeux_v3_artefact_sonde_egale_a_une_direction_du_plancher():
    t, index, mesures, config, graines = _jeu_synthetique(False)
    t = dict(t)
    m = (t["condition"] == "saboteur") | (t["condition"] == "honnete")
    y = (t["condition"][m] == "saboteur").astype(int)
    from controle_ia.sondes.evaluation import aire_sous_courbe
    aires = np.array([aire_sous_courbe(t["plancher_0"][k][m], y) for k in range(t["plancher_0"].shape[0])])
    haute = int(np.argsort(aires, kind="stable")[-2])            # l'avant-dernière direction (au quantile 0,95 sur 24)
    t["scores_0"] = t["plancher_0"][haute].copy()
    r = lv3.lecture_jeux_v3(t, index, mesures, config, graines, 0.9875, [cr.JEU_I])["a"][cr.JEU_I]
    assert r["etat"] == cr.NON_AU_DESSUS and r["difference"]["bas"] <= 0.0


# ----------------------------------------------------------------------------------------------------------- bout en bout
def _plancher_lus(x, chemin=""):
    """Toutes les lectures (dictionnaires) portant `plancher_quantile`, avec leur chemin."""
    sortie = []
    if isinstance(x, dict):
        if "plancher_quantile" in x:
            sortie.append((chemin, x))
        for k, v in x.items():
            sortie += _plancher_lus(v, f"{chemin}/{k}")
    return sortie


def test_bout_en_bout_lecture_v3_jouet_par_la_commande(depot, capsys):
    """`lecture_v3 etape-a` puis `lecture_v3 etape-b` (points d'entrée, en processus) sur le faux run de 7b."""
    j = construire(depot)
    j.config["methode_plancher"] = METHODE
    cfg = j.racine / "config-t07-v6.json"
    cfg.write_text(json.dumps(j.config), encoding="utf-8")
    assert lv3.main(["etape-a", str(j.racine), RUN_T06, str(cfg), "--registre", str(j.registre), "--instant", str(INSTANT)]) == 0
    run_t07 = sorted(p.name for p in (j.racine / "runs").iterdir() if p.name != RUN_T06)[-1]
    m = json.loads((j.racine / "runs" / run_t07 / "manifeste.json").read_text())
    assert m["config"]["methode_plancher"] == METHODE
    lignes_audit(j, run_t07)
    lignes_p3bis(j, APRES_A)
    capsys.readouterr()
    assert lv3.main(["etape-b", str(j.racine), RUN_T06, run_t07, str(cfg), "--registre", str(j.registre),
                     "--instant", str(INSTANT_B)]) == 0
    assert capsys.readouterr().out.startswith("L2 : ")
    lec = json.loads((j.racine / "diag" / run_t07 / "lecture-t07.json").read_text())["resultat"]
    assert lec["issue_critere_3"] in {"L2", "L3", "L4", "L4b", "L5", "L6"}
    assert lec["methode_plancher"]["methode"] == METHODE and lec["methode_plancher"]["sens_de_bas"] == pl2.SENS_DE_BAS
    lus = _plancher_lus({"jeux": lec["jeux"], "hors": lec["jeux_hors_jugement"], "p": lec["predictions"]})
    assert len(lus) > 10
    for chemin, x in lus:
        if "/T4" in chemin:                                     # aire stratifiée (paquet gelé) : hors de la règle (a), déclaré
            assert "difference" not in x
            continue
        assert x["difference"]["methode"] == METHODE and "bas_sonde" in x, chemin
        if "etat" in x and x["etat"] in (cr.AU_DESSUS, cr.NON_AU_DESSUS, "non interprétable"):
            assert (x["etat"] != cr.NON_AU_DESSUS) is x["au_dessus_du_plancher"], chemin
    assert lec["issue_critere_3"] == "L2"                       # signal fort du jouet : même issue que la v2 (essai du chemin normal)


def test_etape_b_v3_refuse_une_configuration_sans_la_cle(depot):
    j = construire(depot)
    with pytest.raises(lv3.CleAbsente, match="methode_plancher"):
        lv3.etape_a(j.racine, j.registre, j.config, RUN_T06, instant=INSTANT)
    with pytest.raises(lv3.CleAbsente, match="methode_plancher"):
        lv3.etape_b(j.racine, j.registre, j.config, RUN_T06, "20261110-000000-t07-jouet", instant=INSTANT_B)
