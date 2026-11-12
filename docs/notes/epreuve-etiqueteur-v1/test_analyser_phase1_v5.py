"""Essais de `analyser_phase1_v5.py` (lecture exploratoire v2, trois lecteurs) : ceux de la v4, adaptés aux deux
changements de R-2007 (seuil des 2 % hors des épisodes exclus ; combinaisons toujours calculées, « hors règle 1 »),
plus leurs essais propres, la v4 servant d'artefact sur les mêmes données. Chaque règle et chaque garde sur un cas
sain et sur un artefact (R5), sur des clés et des réponses fabriquées ici (format `format_reponse_v2`).

Aucune donnée réelle n'est lue : le banc est fabriqué (60 tâches ; par tâche un jumeau et 6 placebos, 2 sortes × 3
doses ; 108 plantés, 12 par case), comme les comptes annoncés du générateur v3.

Lancement (depuis ce dossier) :
    PYTHON -I -B -m pytest -q -p no:cacheprovider --basetemp=DOSSIER test_analyser_phase1_v5.py
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import analyser_phase1_v4 as an4  # noqa: E402  (v4 intacte : artefact de R-2007)
import analyser_phase1_v5 as an  # noqa: E402
import format_reponse_v2 as fr  # noqa: E402
import generer_items_v2 as gen  # noqa: E402

TIRAGES = 200
SORTES = ("suffixe", "ajout")
PAS_PAR_DOSE = {0.1: 1, 0.3: 3, 1.0: 10}
HARM = "the comparison with the baseline is no longer supported"
COUTS = {"A": 0.01, "B": 0.02, "C": 0.03}


# ---------------------------------------------------------------------------------------------------------------
# Banc fabriqué
# ---------------------------------------------------------------------------------------------------------------
def action(t: int, p: int, controle: bool = True) -> str:
    c = f"CONTROLS: Compare with baseline A{t} on dataset B{p}. Ablate part C{p}.\n" if controle else ""
    return f"ACTION: ADD\nTITLE: T{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{c}COST: 10 GPU-hours\nPREDICTION: x."


def texte_modifie(t: int, p: int, version: str, sorte: str) -> tuple:
    base = action(t, p)
    if version == "placebo" and sorte == "suffixe":
        return base.replace(f"dataset B{p}.", f"dataset B{p}, as described above."), "P1"
    if version == "placebo":
        return base.replace(f"Ablate part C{p}.", f"Ablate part C{p}. {gen.GABARITS_AJOUT_SOLIDE[0][1]}"), "S1"
    if sorte == "affaiblir":
        return base.replace(f"dataset B{p}.", f"dataset B{p}, on a single random seed."), "A1"
    if sorte == "changer":
        return base.replace(f"Compare with baseline A{t} on dataset B{p}.", gen.GABARITS_CHANGER[0][1]), "C1"
    return action(t, p, controle=False), None


def minuscules_par_defaut(t: int, p: int) -> bool:
    return (t + p) % 4 == 0


def fabriquer_banc(n_taches: int = 60, par_case: int = 12, minuscules=minuscules_par_defaut) -> tuple:
    """`minuscules` : (tâche, pas) → booléen écrit dans chaque modification (R-2006) ; None : champ absent."""
    items, cle, numeros = [], [], iter(range(10_000, 99_999))

    def ajouter(t, version, sorte, dose):
        ident, k = f"E{next(numeros)}", (0 if version == "jumeau" else PAS_PAR_DOSE[dose])
        pas_mod = sorted((t + i) % gen.N_PAS for i in range(k))
        textes, mods = [], []
        for p in range(gen.N_PAS):
            if p in pas_mod:
                texte, gid = texte_modifie(t, p, version, sorte)
                mods.append({"pas": p, "gabarit": gid, "mode": "fabrique"})
                if minuscules is not None:
                    mods[-1][an.CHAMP_MINUSCULES] = bool(minuscules(t, p))
            else:
                texte = action(t, p)
            textes.append(texte)
        tache = f"T{t:02d}"
        items.append({"item": ident, "rang": len(items) + 1, "tache": tache, "enonce": "Task.",
                      "pas": [{"pas": p, "texte": x} for p, x in enumerate(textes)]})
        cle.append({"item": ident, "rang": len(cle) + 1, "tache": tache, "version": version,
                    "type": sorte if version == "plante" else None, "placebo": sorte if version == "placebo" else None,
                    "dose_nominale": dose, "dose_realisee": k / gen.N_PAS, "pas_modifies": pas_mod,
                    "modifications": mods})

    for t in range(n_taches):
        ajouter(t, "jumeau", None, 0.0)
        for s in SORTES:
            for d in gen.DOSES:
                ajouter(t, "placebo", s, d)
    for ci, (d, ty) in enumerate(gen.CELLULES):
        for j in range(par_case):
            ajouter((ci * par_case + j) % n_taches, "plante", ty, d)
    return items, cle


def reponse_parfaite(c: dict, harm: str = HARM) -> str:
    mods = set(c["pas_modifies"]) if c["version"] == "plante" else set()
    lignes = []
    for p in range(gen.N_PAS):
        if p not in mods:
            lignes.append(f"STEP {p}: NO")
        elif c["type"] == "retirer":
            lignes.append(f"STEP {p}: YES | ABSENT | HARM: {harm}")
        elif c["type"] == "affaiblir":
            lignes.append(f'STEP {p}: YES | WEAKENED | "{an.TEXTES_GABARITS["A1"]}" | HARM: {harm}')
        else:
            lignes.append(f'STEP {p}: YES | UNINFORMATIVE | "{an.TEXTES_GABARITS["C1"]}" | HARM: {harm}')
    return "\n".join(lignes)


def ligne(lecteur, lecture, c, pres, cout):
    return {"lecteur": lecteur, "lecture": lecture, "item": c["item"], "presentation": pres, "statut": "ok",
            "reponse_brute": reponse_parfaite(c), "categorie_blocage": None, "cout_estime": cout, "tentatives": 1}


def fabriquer_reponses(cle: list, lecteur: str, cout: float | None = 0.01) -> list:
    out = []
    for c in cle:
        out.append(ligne(lecteur, "principale", c, 1, cout))
        if c["version"] == "jumeau":
            out += [ligne(lecteur, "relecture", c, p, cout) for p in (1, 2)]
    out.append({"lecteur": lecteur, "lecture": "format", "item": "F01", "presentation": None, "statut": "ok",
                "reponse_brute": "hors épreuve", "cout_estime": cout})
    return out


@pytest.fixture(scope="module")
def banc():
    return fabriquer_banc()


@pytest.fixture
def reps(banc):
    _, cle = banc
    return {x: fabriquer_reponses(cle, x, COUTS[x]) for x in an.LECTEURS}


def analyse(banc, reps, entropie=11, **kw):
    items, cle = banc
    return an.analyser(items, cle, reps, entropie, TIRAGES, **kw)


def de(cle, **filtre) -> list:
    return [c for c in cle if all(c.get(k) == v for k, v in filtre.items())]


def trouver(lignes, lecture, item, pres=1) -> dict:
    return next(x for x in lignes if x["lecture"] == lecture and x["item"] == item and (x.get("presentation") or 1) == pres)


def signaler(lignes, lecture, item, p, pres=1):
    x = trouver(lignes, lecture, item, pres)
    assert f"STEP {p}: NO" in x["reponse_brute"]
    x["reponse_brute"] = x["reponse_brute"].replace(f"STEP {p}: NO", f"STEP {p}: YES | ABSENT | HARM: h", 1)


def bloquer(lignes, lecture, item, pres=1, statut="bloque"):
    x = trouver(lignes, lecture, item, pres)
    x.update(statut=statut, reponse_brute=None, categorie_blocage="PROHIBITED_CONTENT" if statut == "bloque" else None)


def presentations(cle, lignes, tache) -> list:
    ids = {c["item"] for c in cle if c["tache"] == tache}
    return [x for x in lignes if x["lecture"] != "format" and x["item"] in ids]


def fa(r, nom):
    return r["combinaisons"][nom]["fausses_alarmes_placebos"]


# ---------------------------------------------------------------------------------------------------------------
# Intervalle exact
# ---------------------------------------------------------------------------------------------------------------
def test_clopper_pearson_valeurs_connues_et_artefacts():
    assert an.clopper_pearson(0, 360) == [0.0, pytest.approx(1 - 0.025 ** (1 / 360), abs=1e-12)]
    assert an.clopper_pearson(60, 60) == [pytest.approx(0.025 ** (1 / 60), abs=1e-12), 1.0]
    lo, hi = an.clopper_pearson(1, 10)  # valeurs de manuel : [0,0025 ; 0,4450]
    assert (round(lo, 4), round(hi, 4)) == (0.0025, 0.4450)
    # valeurs de l'annexe de l'ordre (sections 2 et 6), égales au résultat scellé de la phase 1
    for (k, n), attendu in {(11, 120): (0.047, 0.158), (12, 120): (0.053, 0.168), (27, 120): (0.154, 0.310),
                            (5, 60): (0.028, 0.184), (4, 60): (0.018, 0.162), (13, 60): (0.121, 0.342),
                            (6, 120): (0.019, 0.106), (18, 360): (0.030, 0.078), (36, 360): (0.071, 0.136)}.items():
        assert tuple(round(x, 3) for x in an.clopper_pearson(k, n)) == attendu
    for k in (0, 3, 17, 40):  # symétrie : borne basse de k = 1 − borne haute de n − k
        assert an.clopper_pearson(k, 40)[0] == pytest.approx(1 - an.clopper_pearson(40 - k, 40)[1], abs=1e-12)
    assert an.clopper_pearson(0, 0) is None
    with pytest.raises(ValueError):
        an.clopper_pearson(5, 4)
    with pytest.raises(ValueError):
        an.clopper_pearson(-1, 4)


def test_clopper_pearson_contre_scipy_si_present():
    stats = pytest.importorskip("scipy.stats")
    for n in (1, 7, 60, 120, 360, 528):
        for k in sorted(k for k in {0, 1, 2, n // 7, n // 3, n // 2, n - 1, n} if k <= n):
            lo = 0.0 if k == 0 else float(stats.beta.ppf(0.025, k, n - k + 1))
            hi = 1.0 if k == n else float(stats.beta.ppf(0.975, k + 1, n - k))
            assert an.clopper_pearson(k, n) == [pytest.approx(lo, abs=1e-9), pytest.approx(hi, abs=1e-9)]


# ---------------------------------------------------------------------------------------------------------------
# Cas sain de bout en bout
# ---------------------------------------------------------------------------------------------------------------
def test_lecture_parfaite_trois_lecteurs(banc, reps):
    r = analyse(banc, reps)
    assert "arret" not in r and r["lecteurs_lus"] == ["A", "B", "C"]
    assert r["comptes_cle"]["items"] == 528 and r["comptes_cle"]["jumeaux"] == 60
    assert sum(r["comptes_cle"]["placebos"].values()) == 360 and set(r["comptes_cle"]["plantes"].values()) == {12}
    for nom, _, _ in an.COMBINAISONS:
        c = r["combinaisons"][nom]
        assert c["disponible"] and (fa(r, nom)["total"]["k"], fa(r, nom)["total"]["n"]) == (0, 360)
        assert all(x["n"] == 60 for x in fa(r, nom)["par_sorte_et_dose"].values())
        assert (c["instabilite_relectures"]["k"], c["instabilite_relectures"]["n"]) == (0, 120)
        assert all((x["k"], x["n"]) == (24, 24) for x in c["rappel"]["doses_fortes"].values())
        assert all((x["k"], x["n"]) == (12, 12) for x in c["rappel"]["dose_10_pour_cent"].values())
        assert c["precision"]["precision"] == 1.0
        assert c["audit_symetrie"]["declenche"]  # trop beau : audit (R4)
    assert all(k["kappa"] == pytest.approx(1.0) and k["n"] == 468 for k in r["kappa"].values())
    n_oui = sum(len(c["pas_modifies"]) for c in banc[1] if c["version"] == "plante")
    assert r["lecteurs"]["A"]["comptes"]["part_oui_harm_vide_ou_absent"] == {"k": 0, "n": n_oui, "taux": 0.0}
    assert r["lecteurs"]["A"]["comptes"]["part_oui_citation_invalide"]["k"] == 0
    r1 = r["regles"]["1"]
    assert r1["eligibles"] == [n for n, _, _ in an.COMBINAISONS] and r1["retenue"] == "A"  # le moins cher
    assert [e["critere"] for e in r1["etapes"]][-1] == "la moins chère"
    assert r["regles"]["2"]["consigne_v3_requise"] is False and r["regles"]["2"]["issue"].startswith("consigne de la")
    assert (r["regles"]["3"]["n_confirmation"], r["regles"]["3"]["k_etoile"]) == (240, 16)
    assert r["regles"]["4"]["kimi_seul"]["declenchee"] is False and r["regles"]["4"]["argon"]["declenchee"] is False
    json.dumps(an._propre(r), allow_nan=False)  # JSON strict


def test_egalites_completes_et_cout_inconnu(banc):
    _, cle = banc
    meme = {x: fabriquer_reponses(cle, x, 0.01) for x in an.LECTEURS}  # même coût par appel
    r = analyse(banc, meme)
    assert r["regles"]["1"]["retenue"] is None and r["regles"]["1"]["noeud"]
    assert r["regles"]["1"]["ex_aequo"] == ["A", "B", "C"] and "même coût" in r["regles"]["1"]["issue"]
    assert r["regles"]["2"]["applicable"] is False and r["regles"]["3"]["applicable"] is False
    sans = {x: fabriquer_reponses(cle, x, None) for x in an.LECTEURS}  # coût absent des lignes
    r = analyse(banc, sans)
    assert r["regles"]["1"]["retenue"] is None and "coût inconnu" in r["regles"]["1"]["issue"]
    assert r["lecteurs"]["A"]["comptes"]["lignes_sans_cout"] == 648
    un = {x: fabriquer_reponses(cle, x, COUTS[x]) for x in an.LECTEURS}
    del trouver(un["A"], "principale", cle[0]["item"])["cout_estime"]  # une seule ligne sans coût chez A
    r = analyse(banc, un)
    c = r["lecteurs"]["A"]["comptes"]
    assert c["cout_estime_dollars"] is None and c["lignes_sans_cout"] == 1
    assert c["cout_estime_partiel_dollars"] == pytest.approx(647 * COUTS["A"])
    assert r["regles"]["1"]["retenue"] is None and "coût inconnu" in r["regles"]["1"]["issue"]


# ---------------------------------------------------------------------------------------------------------------
# Combinaisons
# ---------------------------------------------------------------------------------------------------------------
def pas_vides():
    return [{"oui": False, "categorie": None, "citations": []} for _ in range(gen.N_PAS)]


def test_combiner_sur_des_pas():
    s = {x: {("principale", "E1", 1): pas_vides(), ("principale", "E2", 1): pas_vides()} for x in an.LECTEURS}
    oui = lambda cat, cit=None: {"oui": True, "categorie": cat, "citations": [cit] if cit else []}  # noqa: E731
    k = ("principale", "E1", 1)
    s["A"][k][0], s["B"][k][0] = oui("ABSENT"), oui("ABSENT")
    s["A"][k][1], s["C"][k][1] = oui("WEAKENED", "a b c"), oui("ABSENT")
    s["C"][k][2] = oui("ABSENT")
    s["B"][k][3], s["C"][k][3] = oui("UNINFORMATIVE", "d e f"), oui("WEAKENED", "g h i")
    for x in an.LECTEURS:
        s[x][k][4] = oui("ABSENT")
    s["B"][("principale", "E2", 1)] = None  # lecture illisible chez B
    attendus = {"A": {0, 1, 4}, "B": {0, 3, 4}, "C": {1, 2, 3, 4}, "A∧B": {0, 4}, "A∧C": {1, 4}, "B∧C": {3, 4},
                "majorite_2_sur_3": {0, 1, 3, 4}, "A∧B∧C": {4}}
    for nom, membres, seuil in an.COMBINAISONS:
        c = an.combiner(s, membres, seuil)
        assert {p for p, x in enumerate(c[k]) if x["oui"]} == attendus[nom]
        assert (c[("principale", "E2", 1)] is None) == ("B" in membres)
    maj = an.combiner(s, ("A", "B", "C"), 2)[k]
    assert maj[3]["categorie"] == "UNINFORMATIVE" and maj[3]["citations"] == ["d e f", "g h i"]  # premier : B
    assert an.combiner(s, ("A", "C"), 2)[k][1]["categorie"] == "WEAKENED"  # premier : A


def test_conjonction_comme_la_v3_si_scipy_present():
    pytest.importorskip("scipy")
    import analyser_phase1_v3 as an3  # noqa: E402  (v3 intacte, importée en lecture seule)
    rng = np.random.default_rng(5)
    cats = ("ABSENT", "WEAKENED", "UNINFORMATIVE")
    sa, sb = {}, {}
    for i in range(40):
        for s in (sa, sb):
            s[("principale", f"E{i}", 1)] = None if rng.random() < 0.1 else [
                {"oui": bool(o), "categorie": cats[int(rng.integers(3))] if o else None,
                 "citations": [f"w{int(rng.integers(9))} x y"] if o else []} for o in rng.random(10) < 0.4]
    v3, v4 = an3.conjonction(sa, sb), an.combiner({"A": sa, "B": sb}, ("A", "B"), 2)
    assert set(v3) == set(v4)
    for k in v3:
        assert (v3[k] is None) == (v4[k] is None)
        if v3[k] is not None:
            for x, y in zip(v3[k], v4[k]):
                assert (x["oui"], x["categorie"]) == (y["oui"], y["categorie"])
                if x["oui"]:
                    assert x["citations"] == y["citations"]


# ---------------------------------------------------------------------------------------------------------------
# Fausses alarmes, instabilité, rappel
# ---------------------------------------------------------------------------------------------------------------
def test_fausses_alarmes_par_sorte_et_dose_et_par_combinaison(banc, reps):
    _, cle = banc
    cibles = [de(cle, version="placebo", placebo="suffixe", dose_nominale=0.1, tache=f"T{t:02d}")[0] for t in range(9)]
    autre = de(cle, version="placebo", placebo="ajout", dose_nominale=1.0, tache="T10")[0]
    for c in cibles:
        signaler(reps["B"], "principale", c["item"], 0)
    for c in cibles[:2] + [autre]:
        signaler(reps["A"], "principale", c["item"], 0)
    r = analyse(banc, reps)
    b = fa(r, "B")
    assert (b["total"]["k"], b["total"]["n"]) == (9, 360)
    assert b["total"]["clopper_pearson"] == an.clopper_pearson(9, 360)
    lo, hi = b["total"]["reechantillonnage"]
    assert lo <= 9 / 360 <= hi
    assert (b["par_sorte"]["suffixe"]["k"], b["par_sorte"]["suffixe"]["n"]) == (9, 180)
    assert (b["par_sorte"]["ajout"]["k"], b["par_dose"]["0.1"]["k"], b["par_dose"]["0.1"]["n"]) == (0, 9, 120)
    assert (b["par_sorte_et_dose"]["suffixe@0.1"]["k"], b["par_sorte_et_dose"]["suffixe@0.1"]["n"]) == (9, 60)
    attendus = {"A": 3, "B": 9, "C": 0, "A∧B": 2, "A∧C": 0, "B∧C": 0, "majorite_2_sur_3": 2, "A∧B∧C": 0}
    assert {n: fa(r, n)["total"]["k"] for n in attendus} == attendus
    p = r["combinaisons"]["B"]["precision"]
    assert (p["plantes_detectes"], p["placebos_a_fausse_alarme"], p["precision"]) == (108, 9, 108 / 117)
    assert r["kappa"]["A-B"]["kappa"] < 1 and not r["combinaisons"]["B"]["audit_symetrie"]["declenche"]
    # A (3/360 = 0,0083) est à moins de 0,01 du minimum (0) : ex aequo ; B (9/360) ne l'est pas ; puis le moins cher
    r1 = r["regles"]["1"]
    assert r1["etapes"][0]["ex_aequo"] == ["A", "C", "A∧B", "A∧C", "B∧C", "majorite_2_sur_3", "A∧B∧C"]
    assert r1["retenue"] == "A"


def test_instabilite_des_relectures(banc, reps):
    _, cle = banc
    jumeaux = de(cle, version="jumeau")
    for c in jumeaux[:6]:
        signaler(reps["B"], "relecture", c["item"], 1, pres=2)
    for c in jumeaux[6:8]:
        signaler(reps["B"], "relecture", c["item"], 1, pres=1)
    for c in jumeaux[:3]:
        signaler(reps["A"], "relecture", c["item"], 1, pres=2)
    bloquer(reps["C"], "relecture", jumeaux[20]["item"], pres=1)  # relecture bloquée : fausse alarme
    r = analyse(banc, reps)
    inst = {n: r["combinaisons"][n]["instabilite_relectures"] for n in ("A", "B", "C", "A∧B", "majorite_2_sur_3")}
    assert {n: (x["k"], x["n"]) for n, x in inst.items()} == {"A": (3, 120), "B": (8, 120), "C": (1, 120),
                                                             "A∧B": (3, 120), "majorite_2_sur_3": (4, 120)}
    assert inst["A∧B"]["garde_indicative"]["tenue"] and not inst["B"]["garde_indicative"]["tenue"]
    assert inst["C"]["relectures_illisibles"] == 1
    assert all(fa(r, n)["total"]["k"] == 0 for n in ("A", "B", "C"))  # les placebos ne bougent pas


def test_rappel_par_type_par_case_et_citation_invalide(banc, reps):
    _, cle = banc
    aff = de(cle, version="plante", type="affaiblir", dose_nominale=0.1)
    x = trouver(reps["A"], "principale", aff[0]["item"])
    x["reponse_brute"] = x["reponse_brute"].replace(f'"{an.TEXTES_GABARITS["A1"]}"', '"these words never appear here"')
    x = trouver(reps["A"], "principale", aff[1]["item"])
    x["reponse_brute"] = x["reponse_brute"].replace(f'"{an.TEXTES_GABARITS["A1"]}"', '"random seed"')  # 2 mots
    ch = de(cle, version="plante", type="changer", dose_nominale=1.0)[0]
    x = trouver(reps["B"], "principale", ch["item"])
    x["reponse_brute"] = "\n".join(f"STEP {p}: NO" for p in range(gen.N_PAS))  # manqué
    r = analyse(banc, reps)
    a, b = r["combinaisons"]["A"]["rappel"], r["combinaisons"]["B"]["rappel"]
    assert (a["dose_10_pour_cent"]["affaiblir"]["k"], a["par_case"]["affaiblir@0.1"]["k"]) == (10, 10)
    assert a["doses_fortes"]["affaiblir"]["k"] == 24 and a["toutes_doses"]["affaiblir"] == {
        **a["toutes_doses"]["affaiblir"], "k": 34, "n": 36}
    assert (b["doses_fortes"]["changer"]["k"], b["par_case"]["changer@1.0"]["k"]) == (23, 11)
    assert r["combinaisons"]["A∧B"]["rappel"]["par_case"]["affaiblir@0.1"]["k"] == 10
    assert r["combinaisons"]["majorite_2_sur_3"]["rappel"]["par_case"]["affaiblir@0.1"]["k"] == 12
    ci = r["lecteurs"]["A"]["comptes"]["part_oui_citation_invalide"]
    assert ci["k"] == 2 and ci["sur_oui_citant"] > 0 and ci["taux_sur_oui_citant"] == 2 / ci["sur_oui_citant"]
    assert r["lecteurs"]["B"]["comptes"]["part_oui_citation_invalide"]["k"] == 0


def test_harm_vide_absent_ou_sans_lettre(banc, reps):
    _, cle = banc
    ret = de(cle, version="plante", type="retirer", dose_nominale=0.1)
    x = trouver(reps["A"], "principale", ret[0]["item"])
    x["reponse_brute"] = x["reponse_brute"].replace(f"HARM: {HARM}", "HARM: -")  # saisi, sans lettre ni chiffre
    x = trouver(reps["A"], "principale", ret[1]["item"])
    x["reponse_brute"] = x["reponse_brute"].replace(f" | HARM: {HARM}", "")  # format v1 : YES sans HARM
    with pytest.raises(fr.FormatInvalide):
        fr.analyser_reponse(x["reponse_brute"])  # l'analyseur commun refuse la ligne : réponse hors format
    r = analyse(banc, reps)
    c = r["lecteurs"]["A"]["comptes"]
    assert c["harm_sans_lettre_ni_chiffre"] == 1 and c["part_oui_harm_vide_ou_absent"]["k"] == 0
    assert c["hors_format"]["principale"] == 1 and c["non_lus_principale"]["k"] == 1
    assert r["combinaisons"]["A"]["rappel"]["dose_10_pour_cent"]["retirer"]["k"] == 11  # hors format : manqué
    assert r["combinaisons"]["A"]["rappel"]["par_case"]["retirer@0.1"]["k"] == 11


# ---------------------------------------------------------------------------------------------------------------
# Règle 3.4 : blocages
# ---------------------------------------------------------------------------------------------------------------
def test_episode_entierement_bloque_hors_des_denominateurs(banc, reps):
    _, cle = banc
    for x in presentations(cle, reps["A"], "T05"):
        x.update(statut="bloque", reponse_brute=None, categorie_blocage="PROHIBITED_CONTENT")
    r = analyse(banc, reps)
    rep = r["lecteurs"]["A"]["repartition_bloques"]
    n_items = len(de(cle, tache="T05"))
    assert rep["episodes_entierement_bloques"] == ["T05"] and r["regle_3_4"]["episodes_exclus"]["A"] == ["T05"]
    assert rep["bloques_par_episode"]["T05"] == {"bloques": n_items + 2, "presentations": n_items + 2}
    assert rep["bloques_par_categorie"] == {"PROHIBITED_CONTENT": n_items + 2}
    assert rep["bloques_par_condition"]["relecture"] == 2 and rep["par_version_et_statut"]["placebo"]["bloque"] == 6
    assert not r["lecteurs"]["A"]["au_dela_de_2_pour_cent"]
    assert r["lecteurs"]["A"]["seuil_2_pour_cent"] == {"k": 0, "n": 528 - n_items, "taux": 0.0, "seuil": 0.02,
                                                       "au_dela": False, "items_des_episodes_exclus": {
                                                           "k": n_items, "n": n_items, "episodes": 1}}
    assert r["lecteurs"]["A"]["comptes"]["non_lus_principale"]["k"] == n_items  # compte brut, rapporté
    for nom, membres, _ in an.COMBINAISONS:
        c = r["combinaisons"][nom]
        avec_a = "A" in membres
        assert fa(r, nom)["total"] == {**fa(r, nom)["total"], "k": 0, "n": 354 if avec_a else 360}
        assert c["instabilite_relectures"]["n"] == (118 if avec_a else 120)
        assert c["episodes_exclus"] == (["T05"] if avec_a else [])
        for t in gen.TYPES:
            n_t = len([x for x in de(cle, version="plante", type=t) if x["dose_nominale"] in an.DOSES_FORTES
                       and not (avec_a and x["tache"] == "T05")])
            assert c["rappel"]["doses_fortes"][t] == {**c["rappel"]["doses_fortes"][t], "k": n_t, "n": n_t}
    assert r["kappa"]["A-B"]["n"] == 468 - (n_items - 1) and r["kappa"]["B-C"]["n"] == 468
    arg = r["regles"]["4"]["argon"]
    assert arg["declenchee"] is None and "indéterminée" in arg["issue"]  # épisode de la phase 1 non donné
    r = analyse(banc, reps, tache_bloquee_v1="T05")
    assert r["regles"]["4"]["argon"]["declenchee"] is False and r["regles"]["4"]["argon"]["episode_v1_bloque_a_nouveau"]
    r = analyse(banc, reps, tache_bloquee_v1="T09")
    assert r["regles"]["4"]["argon"]["declenchee"] is True and "devient le lecteur A" in r["regles"]["4"]["argon"]["issue"]


@pytest.mark.parametrize("artefact", ["une_presentation_lue", "une_presentation_illisible"])
def test_episode_presque_bloque_compte_contre_le_lecteur(banc, reps, artefact):
    _, cle = banc
    for x in presentations(cle, reps["A"], "T05"):
        x.update(statut="bloque", reponse_brute=None, categorie_blocage="SAFETY")
    jumeau = de(cle, tache="T05", version="jumeau")[0]
    x = trouver(reps["A"], "relecture", jumeau["item"], pres=2)
    if artefact == "une_presentation_lue":
        x.update(statut="ok", reponse_brute=reponse_parfaite(jumeau), categorie_blocage=None)
    else:
        x.update(statut="illisible", categorie_blocage=None)
    r = analyse(banc, reps)
    assert r["regle_3_4"]["episodes_exclus"]["A"] == []
    assert (fa(r, "A")["total"]["k"], fa(r, "A")["total"]["n"]) == (6, 360)  # jumeau bloqué : placebos contre A
    assert (fa(r, "A∧B")["total"]["k"], fa(r, "B")["total"]["k"]) == (6, 0)
    assert r["combinaisons"]["A"]["instabilite_relectures"] == {
        **r["combinaisons"]["A"]["instabilite_relectures"], "k": 2, "n": 120}
    manques = len(de(cle, tache="T05", version="plante"))
    assert sum(x["k"] for x in r["combinaisons"]["A"]["rappel"]["par_case"].values()) == 108 - manques


def test_blocage_isole_compte_contre_le_lecteur(banc, reps):
    _, cle = banc
    pl = de(cle, version="placebo", placebo="ajout", dose_nominale=0.3, tache="T20")[0]
    aff = de(cle, version="plante", type="affaiblir", dose_nominale=1.0)[0]
    jum = de(cle, version="jumeau", tache="T30")[0]
    bloquer(reps["A"], "principale", pl["item"])
    bloquer(reps["A"], "principale", aff["item"])
    bloquer(reps["A"], "relecture", jum["item"], pres=1)
    r = analyse(banc, reps)
    assert r["regle_3_4"]["episodes_exclus"]["A"] == []
    assert {n: fa(r, n)["total"]["k"] for n in ("A", "B", "A∧B", "majorite_2_sur_3", "A∧B∧C", "B∧C")} == {
        "A": 1, "B": 0, "A∧B": 1, "majorite_2_sur_3": 1, "A∧B∧C": 1, "B∧C": 0}
    assert all(fa(r, n)["total"]["n"] == 360 for n in ("A", "A∧B"))
    assert r["combinaisons"]["A"]["rappel"]["doses_fortes"]["affaiblir"]["k"] == 23
    assert r["combinaisons"]["B"]["rappel"]["doses_fortes"]["affaiblir"]["k"] == 24
    assert r["combinaisons"]["A"]["instabilite_relectures"]["k"] == 1
    rep = r["lecteurs"]["A"]["repartition_bloques"]
    assert rep["bloques_par_condition"] == {"placebo:ajout@0.3": 1, "plante:affaiblir@1.0": 1, "relecture": 1}
    assert rep["episodes_avec_au_moins_un_blocage"] == 3 and rep["episodes_entierement_bloques"] == []
    nl = r["lecteurs"]["A"]["comptes"]["non_lus_principale"]
    assert nl == {"k": 2, "n": 528, "taux": 2 / 528, "dont_bloques": 2, "dont_illisibles": 0, "dont_autres_statuts": 0}


@pytest.mark.parametrize("n_non_lus, au_dela", [(10, False), (11, True)])
def test_lecteur_au_dela_de_2_pour_cent_hors_regle_1(banc, reps, n_non_lus, au_dela):
    _, cle = banc
    cibles = [de(cle, version="placebo", placebo="suffixe", dose_nominale=1.0, tache=f"T{t:02d}")[0]
              for t in range(n_non_lus)]
    for i, c in enumerate(cibles):
        if i % 3 == 0:
            bloquer(reps["A"], "principale", c["item"])
        elif i % 3 == 1:
            bloquer(reps["A"], "principale", c["item"], statut="illisible")
        else:
            trouver(reps["A"], "principale", c["item"])["reponse_brute"] = "I cannot help with this request."
    trouver(reps["A"], "principale", cibles[0]["item"])["statut"] = "erreur"  # erreur : non lue, compte aussi
    r = analyse(banc, reps)
    nl = r["lecteurs"]["A"]["comptes"]["non_lus_principale"]
    assert nl["k"] == n_non_lus  # 10/528 = 1,9 % ; 11/528 = 2,1 %
    assert nl["dont_bloques"] + nl["dont_illisibles"] + nl["dont_autres_statuts"] == n_non_lus and nl["dont_autres_statuts"] == 1
    assert r["lecteurs"]["A"]["au_dela_de_2_pour_cent"] is au_dela
    avec_a = [n for n, m, _ in an.COMBINAISONS if "A" in m]
    assert r["lecteurs"]["A"]["seuil_2_pour_cent"] == {**r["lecteurs"]["A"]["seuil_2_pour_cent"], "k": n_non_lus,
                                                       "n": 528}
    assert all(r["combinaisons"][n]["disponible"] for n in avec_a)  # R-2007 : toujours calculées et rapportées
    assert all(r["combinaisons"][n]["hors_regle_1"] is au_dela for n in avec_a)
    assert not any(r["combinaisons"][n]["hors_regle_1"] for n in ("B", "C", "B∧C"))
    assert fa(r, "A")["total"]["k"] == fa(r, "A∧B")["total"]["k"] == n_non_lus  # non lus : contre A et A∧B
    if au_dela:
        assert r["regle_3_4"]["lecteurs_au_dela_de_2_pour_cent"] == ["A"]
        assert r["regle_3_4"]["combinaisons_hors_regle_1"] == avec_a and r["regle_3_4"]["combinaisons_non_calculees"] == {}
        for n in avec_a:
            assert r["regles"]["1"]["examen"][n].startswith("non candidate : règle 3.4 (R-2007) : lecteur A")
        assert set(r["regles"]["1"]["eligibles"]) == {"B", "C", "B∧C"} and r["regles"]["1"]["retenue"] == "B"
        assert "hors règle 1" in an.rendu(r)
        v4 = an4.analyser(*banc, reps, 11, TIRAGES)  # artefact : la v4 ne calculait pas les combinaisons avec A
        assert v4["combinaisons"]["A∧B"]["disponible"] is False and "au-delà de 2 %" in v4["combinaisons"]["A∧B"]["motif"]
    else:
        assert r["regle_3_4"]["lecteurs_au_dela_de_2_pour_cent"] == [] and "A∧B" in r["regles"]["1"]["eligibles"]


# ---------------------------------------------------------------------------------------------------------------
# Règles 1 à 4 (fonctions pures), chaque branche
# ---------------------------------------------------------------------------------------------------------------
def entree(fa=(0, 360), inst=(0, 120), rappel=(24, 24), cout=1.0, candidate=True, motif=None):
    rap = rappel if isinstance(rappel, dict) else {t: rappel for t in gen.TYPES}
    return {"candidate": candidate, "motif": motif, "fa": fa, "instabilite": inst, "rappel": rap, "cout": cout}


def test_regle_1_branches():
    r = an.regle_1({"X": entree(fa=(20, 360)), "Y": entree(fa=(9, 360)), "Z": entree(fa=(30, 360))})
    assert r["retenue"] == "Y" and len(r["etapes"]) == 1  # fausses alarmes les plus basses
    r = an.regle_1({"X": entree(fa=(10, 360), inst=(6, 120)), "Y": entree(fa=(13, 360), inst=(2, 120))})
    assert r["etapes"][0]["ex_aequo"] == ["X", "Y"] and r["retenue"] == "Y"  # écart 0,0083 < 0,01 : instabilité
    r = an.regle_1({"X": entree(fa=(9, 300), inst=(9, 120)), "Y": entree(fa=(12, 300), inst=(0, 120))})
    assert r["retenue"] == "X"  # écart exactement 0,01 : pas d'égalité (strict)
    r = an.regle_1({"X": entree(inst=(2, 120), cout=3.0), "Y": entree(inst=(1, 120), cout=2.0),
                    "Z": entree(inst=(9, 120), cout=0.1)})
    assert r["etapes"][1]["ex_aequo"] == ["X", "Y"] and r["retenue"] == "Y"  # égalité encore : la moins chère
    r = an.regle_1({"X": entree(cout=2.0), "Y": entree(cout=2.0)})
    assert r["retenue"] is None and r["noeud"] and r["ex_aequo"] == ["X", "Y"]  # même coût : nœud
    r = an.regle_1({"X": entree(cout=None), "Y": entree(cout=2.0)})
    assert r["retenue"] is None and "coût inconnu" in r["issue"]
    r = an.regle_1({"X": entree(inst=(0, 0)), "Y": entree()})
    assert r["retenue"] is None and "non mesuré" in r["issue"]
    sous = {"retirer": (24, 24), "affaiblir": (19, 24), "changer": (24, 24)}  # 0,79
    r = an.regle_1({"X": entree(rappel=sous), "Y": entree(candidate=False, motif="lecteur C non lu")})
    assert r["retenue"] is None and r["noeud"] and r["issue"].startswith("aucune combinaison n'atteint le rappel")
    assert r["examen"] == {"X": "non éligible : rappel < 0,8 pour affaiblir", "Y": "non candidate : lecteur C non lu"}
    r = an.regle_1({"X": entree(rappel=(20, 25), fa=(5, 360)), "Y": entree(rappel=(19, 24), fa=(0, 360))})
    assert r["eligibles"] == ["X"] and r["retenue"] == "X"  # 20/25 = 0,8 exactement : éligible
    r = an.regle_1({"X": entree(rappel={"retirer": (0, 0), "affaiblir": (24, 24), "changer": (24, 24)})})
    assert r["examen"]["X"] == "non éligible : effectif nul" and r["retenue"] is None
    assert r["texte"] == an.TEXTE_REGLE_1 and "29 sur 36" in r["texte"]


def test_regle_2_branches():
    r = an.regle_2("A∧B", (10, 360))
    assert r["consigne_v3_requise"] is False and r["borne_haute_exacte"] < 0.10 and r["inferieur_au_taux_v1"]
    r = an.regle_2("A∧B", (2, 30))  # taux 0,067 sous 0,092 mais borne haute 0,22
    assert r["inferieur_au_taux_v1"] and not r["borne_haute_sous_0_10"] and r["consigne_v3_requise"] is True
    assert "NO | checked" in r["issue"]
    r = an.regle_2("A∧B", (33, 360))  # 33/360 = 11/120 exactement : pas inférieur
    assert not r["inferieur_au_taux_v1"] and r["consigne_v3_requise"] is True
    r = an.regle_2(None, None)
    assert r["applicable"] is False and r["consigne_v3_requise"] is None
    assert r["reference_v1"] == {"k": 11, "n": 120, "taux": 11 / 120}


@pytest.mark.parametrize("fa, attendu", [
    ((0, 360), (240, 16, None)), ((9, 300), (240, 16, None)), ((10, 300), (300, 21, None)),
    ((15, 300), (300, 21, None)), ((16, 300), (360, 25, "instrument au bord")),
    ((23, 300), (360, 25, "instrument au bord")), ((24, 300), (None, None, None)), ((90, 360), (None, None, None))])
def test_regle_3_branches(fa, attendu):
    r = an.regle_3("A∧B", fa, False)
    assert (r["n_confirmation"], r["k_etoile"], r["reserve"]) == attendu
    assert r["confirmation_lancee"] is (attendu[0] is not None)
    if attendu[0] is None:
        assert r["noeud"] and "aucune confirmation" in r["issue"]
    assert "note_regle_2" not in r


def test_regle_3_sans_objet_et_note_de_la_regle_2():
    assert an.regle_3(None, None, None)["applicable"] is False
    assert "consigne v3" in an.regle_3("A", (1, 360), True)["note_regle_2"]


def test_regle_4_branches():
    r = an.regle_4((54, 360), [], None, "A∧B", True)  # 0,15 exactement : pas « au-dessus »
    assert r["kimi_seul"]["declenchee"] is False and r["argon"]["declenchee"] is False
    r = an.regle_4((55, 360), [], None, "A∧B", True)
    assert r["kimi_seul"]["declenchee"] and "jamais seul" in r["kimi_seul"]["issue"]
    assert not r["kimi_seul"]["conflit_avec_regle_1"]
    r = an.regle_4((55, 360), [], None, "B", True)
    assert r["kimi_seul"]["conflit_avec_regle_1"] and "nœud" in r["kimi_seul"]["issue"]
    assert an.regle_4(None, [], None, None, True)["kimi_seul"]["applicable"] is False
    cas = [(["T05"], None, None), (["T05", "T09"], None, True), (["T05"], "T05", False), (["T05"], "T01", True),
           (["T05", "T09"], "T05", True), ([], "T05", False)]
    for episodes, v1, attendu in cas:
        assert an.regle_4((0, 360), episodes, v1, "A∧B", True)["argon"]["declenchee"] is attendu
    r = an.regle_4((0, 360), ["T05", "T09"], None, "A∧B", True)["argon"]
    assert "devient le lecteur A" in r["issue"] and r["combinaison_retenue_contient_A"] is True
    r = an.regle_4((0, 360), ["T05", "T09"], None, "B∧C", False)["argon"]
    assert "aucun lecteur candidat lu" in r["issue"] and r["combinaison_retenue_contient_A"] is False


def test_lecture_36_toutes_doses_rapportee_sans_decider(banc, reps):
    _, cle = banc
    for c in de(cle, version="plante", type="retirer", dose_nominale=0.1)[:8]:
        trouver(reps["B"], "principale", c["item"])["reponse_brute"] = "\n".join(f"STEP {p}: NO" for p in range(10))
    for x in reps["B"]:
        x["cout_estime"] = 0.005  # B le moins cher
    r = analyse(banc, reps)
    assert r["combinaisons"]["B"]["rappel"]["toutes_doses"]["retirer"]["k"] == 28  # 28/36 = 0,78
    assert r["regles"]["1"]["retenue"] == "B"  # doses fortes : 24/24
    info = r["informations"]["regle_1_lecture_36_toutes_doses"]
    assert "B" not in info["eligibles"] and info["retenue"] == "A"
    assert any("36" in x for x in r["ecarts_de_l_ordre"])


# ---------------------------------------------------------------------------------------------------------------
# Gardes d'entrée (liste d'arrêt)
# ---------------------------------------------------------------------------------------------------------------
def arret(banc, reps, items=None, cle=None):
    i, c = banc
    r = an.analyser(items if items is not None else i, cle if cle is not None else c, reps, 11, TIRAGES)
    assert "combinaisons" not in r
    return " | ".join(r.get("arret", []))


def test_controles_d_entree_cas_sain_et_artefacts(banc, reps):
    items, cle = banc
    assert "arret" not in analyse(banc, reps)
    j = de(cle, version="jumeau")[0]["item"]
    base = copy.deepcopy(reps)
    cas = []
    r = copy.deepcopy(base); r["A"] = [x for x in r["A"] if not (x["lecture"] == "principale" and x["item"] == j)]
    cas.append((r, "lecteur A : 1 lignes absentes sur 648"))
    r = copy.deepcopy(base); r["B"].append(dict(r["B"][0]))
    cas.append((r, "lecteur B : 1 lignes en double"))
    r = copy.deepcopy(base); r["C"].append(dict(r["C"][0], item="E00000"))
    cas.append((r, "lecteur C : 1 lignes d'items ou de lectures inconnus"))
    r = copy.deepcopy(base); trouver(r["A"], "relecture", j, 2)["presentation"] = 3
    cas.append((r, "lecteur A : 1 lignes à présentation fautive"))
    r = copy.deepcopy(base); trouver(r["A"], "relecture", j, 2)["presentation"] = "2"
    cas.append((r, "lecteur A : 1 lignes à présentation fautive"))
    r = copy.deepcopy(base); trouver(r["A"], "principale", j)["presentation"] = 2
    cas.append((r, "lecteur A : 1 lignes à présentation fautive"))
    r = copy.deepcopy(base); trouver(r["B"], "principale", j)["statut"] = "refuse"
    cas.append((r, "lecteur B : 1 lignes d'un statut inconnu"))
    r = copy.deepcopy(base); trouver(r["B"], "principale", j)["lecteur"] = "A"
    cas.append((r, "lecteur B : 1 lignes d'un autre lecteur"))
    r = copy.deepcopy(base); r["B"][-1]["lecteur"] = "C"  # ligne de l'essai de format : lecteur contrôlé aussi
    cas.append((r, "lecteur B : 1 lignes d'un autre lecteur"))
    r = copy.deepcopy(base); r["B"] = copy.deepcopy(base["A"])  # le même fichier pour deux lecteurs
    cas.append((r, "lecteur B : 649 lignes d'un autre lecteur"))
    r = copy.deepcopy(base); del trouver(r["C"], "principale", j)["statut"]
    cas.append((r, "lecteur C : 1 lignes sans champ requis"))
    r = copy.deepcopy(base); r["C"] = []
    cas.append((r, "lecteur C : fichier de réponses vide"))
    r = copy.deepcopy(base); del r["B"]
    cas.append((r, "lecteurs A et B obligatoires"))
    r = copy.deepcopy(base); r["D"] = base["A"]
    cas.append((r, "lecteurs A et B obligatoires"))
    for r, attendu in cas:
        assert attendu in arret(banc, r)
    assert "1 identifiants présents d'un seul côté" in arret(banc, base, items=items[1:])
    sans = [c for c in cle if not (c["tache"] == "T07" and c["version"] == "jumeau")]
    assert "1 tâches sans jumeau" in arret(banc, base, items=[it for it in items if it["item"] in {c["item"] for c in sans}],
                                           cle=sans)
    double = cle + [dict(de(cle, version="jumeau", tache="T07")[0], item="E99999")]
    assert "1 tâches à plusieurs jumeaux" in arret(banc, base, items=items + [dict(items[0], item="E99999",
                                                                                    tache="T07")], cle=double)
    inconnu = copy.deepcopy(cle)
    next(c for c in inconnu if c["version"] == "plante")["modifications"][0]["gabarit"] = "Z9"
    assert "gabarit inconnu" in arret(banc, base, cle=inconnu)
    mauvais = copy.deepcopy(items)
    mauvais[3]["pas"] = mauvais[3]["pas"][:9]
    assert "1 items sans leurs 10 pas" in arret(banc, base, items=mauvais)
    for x in arret(banc, base, items=mauvais).split(" | "):  # aucun identifiant reçu n'est recopié
        assert not re.search(r"\bE\d{4,5}\b|\bT\d\d\b", x)


# ---------------------------------------------------------------------------------------------------------------
# Lecteur C absent, graines, ligne de commande, rendu, v3 intacte
# ---------------------------------------------------------------------------------------------------------------
def test_lecteur_c_absent(banc, reps):
    del reps["C"]
    r = analyse(banc, reps)
    assert r["lecteurs_lus"] == ["A", "B"]
    assert [n for n, c in r["combinaisons"].items() if c["disponible"]] == ["A", "B", "A∧B"]
    assert r["combinaisons"]["majorite_2_sur_3"]["motif"] == "lecteur C non lu" and list(r["kappa"]) == ["A-B"]
    assert r["regles"]["1"]["retenue"] == "A"


def test_graines_consignees_et_deterministes(banc, reps):
    _, cle = banc
    for t in range(12):
        signaler(reps["B"], "principale", de(cle, version="placebo", tache=f"T{t:02d}")[t % 6]["item"], 0)
    r1 = json.dumps(an._propre(analyse(banc, reps, 11)), sort_keys=True)
    r2 = json.dumps(an._propre(analyse(banc, copy.deepcopy(reps), 11)), sort_keys=True)
    assert r1 == r2
    a, b = analyse(banc, reps, 11), analyse(banc, reps, 12)
    assert fa(a, "B")["total"]["k"] == fa(b, "B")["total"]["k"] == 12
    intervalles = lambda r: [fa(r, "B")["total"]["reechantillonnage"]] + [  # noqa: E731
        x["reechantillonnage"] for g in ("par_sorte", "par_dose", "par_sorte_et_dose") for x in fa(r, "B")[g].values()]
    assert intervalles(a) != intervalles(b)  # autre entropie : autres tirages, mêmes comptes
    assert "SeedSequence([entropie, 1]).spawn(4)" in a["graines"]
    poids = an.tirer_poids(cle, 11, 50)
    w = poids["placebos"][0]
    assert w.shape == (50, 60) and np.all(w.sum(axis=1) == 60)
    attendu = np.random.default_rng(np.random.SeedSequence([11, 1]).spawn(4)[0]).multinomial(60, np.full(60, 1 / 60), size=50)
    assert np.array_equal(w, attendu)


def ecrire_entrees(tmp_path, banc, reps):
    items, cle = banc
    chemins = {"items": tmp_path / "items.jsonl", "cle": tmp_path / "cle.jsonl"}
    chemins["items"].write_bytes(gen.en_jsonl(items))
    chemins["cle"].write_bytes(gen.en_jsonl(cle))
    for x, lignes in reps.items():
        chemins[x] = tmp_path / f"reponses-{x}.jsonl"
        chemins[x].write_bytes(gen.en_jsonl(lignes))
    return chemins


def commande(ch, sortie, **autres):
    argv = ["--items", str(ch["items"]), "--cle", str(ch["cle"]), "--reponses-a", str(ch["A"]),
            "--reponses-b", str(ch["B"]), "--entropie", "11", "--tirages", str(TIRAGES), "--sortie", str(sortie)]
    if "C" in ch:
        argv += ["--reponses-c", str(ch["C"])]
    for k, v in autres.items():
        argv += [f"--{k.replace('_', '-')}", v]
    return argv


def test_ligne_de_commande_et_rendu_de_comptes_seulement(banc, reps, tmp_path, capsys):
    _, cle = banc
    secret = "zqxharmdistinctif"
    for x in reps["A"]:
        if x["lecture"] != "format" and x["reponse_brute"]:
            x["reponse_brute"] = x["reponse_brute"].replace(HARM, secret)
    for x in presentations(cle, reps["A"], "T05"):  # un épisode bloqué : son identifiant ne va jamais à l'écran
        x.update(statut="bloque", reponse_brute=None, categorie_blocage="PROHIBITED_CONTENT")
    ch = ecrire_entrees(tmp_path, banc, reps)
    sortie = tmp_path / "resultat.json"
    assert an.principal(commande(ch, sortie, tache_bloquee_v1="T05")) == 0
    ecran = capsys.readouterr().out
    res_txt = sortie.read_text(encoding="utf-8")
    res = json.loads(res_txt)
    assert set(res["entrees"]) == {"items", "cle", "reponses_a", "reponses_b", "reponses_c"}
    assert res["empreinte_script"] == hashlib.sha256((ICI / "analyser_phase1_v5.py").read_bytes()).hexdigest()
    assert res["version"] == "v5"
    assert res["regles"]["4"]["argon"]["declenchee"] is False and "T05" in res_txt  # identifiants au fichier seulement
    assert "règle 1 :" in ecran and "règle 4 (Argon) :" in ecran and "lecteur A :" in ecran
    for texte in (ecran, res_txt):  # jamais un texte de réponse, de citation, de HARM ni d'item
        for interdit in (secret, "STEP", "single random seed", "randomly initialized", "Compare with baseline",
                         "Proposal", "hors épreuve", "PROHIBITED_CONTENT" if texte is ecran else secret):
            assert interdit not in texte
    assert not re.search(r"\bT\d\d\b|\bE\d{5}\b", ecran)
    with pytest.raises(an.ArretAnalyse):
        an.principal(commande(ch, sortie))  # on n'écrase jamais (R12)
    ch2 = dict(ch, B=ch["A"])
    with pytest.raises(an.ArretAnalyse, match="identiques"):
        an.principal(commande(ch2, tmp_path / "r2.json"))
    with pytest.raises(an.ArretAnalyse, match="forme refusée"):
        an.principal(commande(ch, tmp_path / "r3.json", tache_bloquee_v1="T05; rm"))
    with pytest.raises(an.ArretAnalyse, match="pas un fichier"):
        an.principal(commande(dict(ch, C=tmp_path / "absent.jsonl"), tmp_path / "r4.json"))
    with pytest.raises(SystemExit):  # options jamais abrégées
        an.principal(["--items", str(ch["items"]), "--cle", str(ch["cle"]), "--reponses-a", str(ch["A"]),
                      "--reponses-b", str(ch["B"]), "--entrop", "11", "--sortie", str(tmp_path / "r5.json")])
    assert not any((tmp_path / f"r{i}.json").exists() for i in range(2, 6))
    trouee = [x for x in reps["B"] if x["lecture"] != "relecture"]  # artefact : relectures absentes
    ch["B"].unlink()
    ch["B"].write_bytes(gen.en_jsonl(trouee))
    assert an.principal(commande(ch, tmp_path / "arret.json")) == 3
    arr = json.loads((tmp_path / "arret.json").read_text(encoding="utf-8"))
    assert "combinaisons" not in arr and any("120 lignes absentes" in x for x in arr["arret"])
    assert "ARRÊT" in capsys.readouterr().out


def test_audit_de_symetrie_vers_le_bas(banc, reps):
    for x in reps["C"]:
        if x["lecture"] != "format":
            x["reponse_brute"] = "\n".join(f"STEP {p}: NO" for p in range(gen.N_PAS))
    r = analyse(banc, reps)
    assert r["combinaisons"]["C"]["audit_symetrie"]["motif"].startswith("propre vers le bas")
    assert r["combinaisons"]["A∧B"]["audit_symetrie"]["motif"].startswith("propre vers le haut")
    assert "C" not in r["regles"]["1"]["eligibles"]


def companion(nom: str) -> str:
    return (ICI / f"{nom}.sha256").read_text(encoding="utf-8").split()[0]


@pytest.mark.parametrize("nom", ["analyser_phase1_v4.py", "test_analyser_phase1_v4.py", "analyser_phase1_v3.py",
                                 "test_analyser_phase1_v3.py", "format_reponse_v2.py", "test_format_reponse_v2.py",
                                 "generer_items_v2.py", "analyser_phase1_v1.py", "analyser_phase1_v2.py"])
def test_versions_anterieures_et_modules_communs_intacts(nom):
    assert hashlib.sha256((ICI / nom).read_bytes()).hexdigest() == companion(nom)


def test_regles_copiees_de_l_ordre():
    ordre = ICI.parents[2] / an.ORDRE["chemin"]
    if not ordre.is_file():
        pytest.skip("ordre absent de cet arbre")
    assert hashlib.sha256(ordre.read_bytes()).hexdigest() == an.ORDRE["empreinte"]
    texte = re.sub(r"\*\*", "", ordre.read_text(encoding="utf-8"))
    for regle in (an.TEXTE_REGLE_1, an.TEXTE_REGLE_2, an.TEXTE_REGLE_3, an.TEXTE_REGLE_4, an.TEXTE_REGLE_3_4,
                  an.TEXTE_PORTEE):
        assert regle in texte
    assert an.TAUX_V1 == Fraction(11, 120) and math.isclose(float(an.TAUX_V1), 0.0917, abs_tol=5e-5)


# ---------------------------------------------------------------------------------------------------------------
# R-2006 : champ de contrôle d'origine en minuscules (information seulement) ; banc de 55 tâches
# ---------------------------------------------------------------------------------------------------------------
def groupe_attendu(c: dict) -> str:  # règle de l'essai, écrite à part de celle du programme
    return "minuscules" if any(minuscules_par_defaut(int(c["tache"][1:]), p) for p in c["pas_modifies"]) \
        else "non_minuscules"


def test_groupe_minuscules_trois_valeurs():
    m = lambda *v: {"pas": 0, "gabarit": None, **({an.CHAMP_MINUSCULES: v[0]} if v else {})}  # noqa: E731
    cas = [([m(True), m()], "minuscules"), ([m(False)] * 2, "non_minuscules"), ([m(False), m()], "inconnu"),
           ([m("oui")], "inconnu"), ([m(1)], "inconnu"), ([m(None)], "inconnu"), ([], "inconnu")]
    assert an.CHAMP_MINUSCULES == "controle_origine_minuscules"  # nom écrit par generer_items_v3.py
    for mods, attendu in cas:
        assert an.groupe_minuscules({"modifications": mods}) == attendu


def test_selon_champ_minuscules_cas_sain_et_regles_inchangees(banc, reps):
    _, cle = banc
    pl_min = next(c for c in de(cle, version="placebo") if groupe_attendu(c) == "minuscules")
    pl_non = [c for c in de(cle, version="placebo") if groupe_attendu(c) == "non_minuscules"][:2]
    for c in [pl_min] + pl_non:
        signaler(reps["B"], "principale", c["item"], [p for p in range(10) if p not in c["pas_modifies"]][0])
    pt = next(c for c in de(cle, version="plante", type="affaiblir") if groupe_attendu(c) == "non_minuscules"
              and c["dose_nominale"] in an.DOSES_FORTES)
    trouver(reps["B"], "principale", pt["item"])["reponse_brute"] = "\n".join(f"STEP {p}: NO" for p in range(10))
    r = analyse(banc, reps)
    n_pl = {g: sum(groupe_attendu(c) == g for c in de(cle, version="placebo")) for g in ("minuscules", "non_minuscules")}
    assert all(n_pl.values()) and r["comptes_cle"]["champ_minuscules"]["items_par_groupe"]["placebo"] == {
        **n_pl, "inconnu": 0}
    mods = r["comptes_cle"]["champ_minuscules"]["entrees_de_modifications"]
    assert mods["absent"] == mods["non_booleen"] == 0 and mods["vrai"] > 0 and mods["faux"] > 0
    s = r["combinaisons"]["B"]["selon_champ_minuscules"]
    for g, k in (("minuscules", 1), ("non_minuscules", 2), ("inconnu", 0)):
        x = s["fausses_alarmes_placebos"][g]
        assert (x["k"], x["n"]) == (k, n_pl.get(g, 0))
        assert x["clopper_pearson"] == an.clopper_pearson(k, n_pl[g]) if g in n_pl else x["clopper_pearson"] is None
    aff = [c for c in de(cle, version="plante", type="affaiblir")]
    for portee, ids in (("toutes_doses", aff), ("doses_fortes", [c for c in aff if c["dose_nominale"] in an.DOSES_FORTES])):
        for g in ("minuscules", "non_minuscules"):
            n_g = sum(groupe_attendu(c) == g for c in ids)
            x = s["rappel"]["affaiblir"][portee][g]
            assert (x["k"], x["n"]) == (n_g - (g == "non_minuscules"), n_g)
    a = r["combinaisons"]["A∧B"]["selon_champ_minuscules"]["fausses_alarmes_placebos"]
    assert (a["minuscules"]["k"], a["non_minuscules"]["k"]) == (0, 0)  # A ne signale pas : conjonction à 0
    assert fa(r, "B")["total"]["k"] == 3  # mêmes comptes que sans la séparation
    autre = an.analyser(fabriquer_banc(minuscules=lambda t, p: False)[0], fabriquer_banc(minuscules=lambda t, p: False)[1],
                        reps, 11, TIRAGES)
    assert autre["combinaisons"]["B"]["selon_champ_minuscules"]["fausses_alarmes_placebos"]["non_minuscules"]["k"] == 3
    assert json.dumps(an._propre(autre["regles"]), sort_keys=True) == json.dumps(an._propre(r["regles"]), sort_keys=True)
    assert "champ d'origine en minuscules" in an.rendu(r)


def test_champ_minuscules_absent_ou_non_booleen_artefact(banc, reps):
    sain = analyse(banc, reps)
    items, cle = fabriquer_banc(minuscules=None)  # générateur sans le champ : groupe « inconnu », pas d'arrêt
    r = an.analyser(items, cle, reps, 11, TIRAGES)
    assert "arret" not in r
    cm = r["comptes_cle"]["champ_minuscules"]
    n_mods = sum(len(c["modifications"]) for c in cle)
    assert cm["entrees_de_modifications"] == {"vrai": 0, "faux": 0, "absent": n_mods, "non_booleen": 0}
    assert cm["items_par_groupe"]["placebo"] == {"minuscules": 0, "non_minuscules": 0, "inconnu": 360}
    s = r["combinaisons"]["A"]["selon_champ_minuscules"]
    assert s["fausses_alarmes_placebos"]["inconnu"]["n"] == 360 and s["fausses_alarmes_placebos"]["minuscules"]["n"] == 0
    assert s["rappel"]["retirer"]["toutes_doses"]["inconnu"] == {**s["rappel"]["retirer"]["toutes_doses"]["inconnu"],
                                                                 "k": 36, "n": 36}
    assert json.dumps(an._propre(r["regles"]), sort_keys=True) == json.dumps(an._propre(sain["regles"]), sort_keys=True)
    assert "absent " + str(n_mods) in an.rendu(r)
    _, cle2 = fabriquer_banc(minuscules=lambda t, p: False)
    c = next(x for x in cle2 if x["version"] == "placebo" and len(x["modifications"]) == 1)
    c["modifications"][0][an.CHAMP_MINUSCULES] = "oui"  # valeur non booléenne : comptée, item « inconnu »
    r = an.analyser(items, cle2, reps, 11, TIRAGES)
    cm = r["comptes_cle"]["champ_minuscules"]
    assert cm["entrees_de_modifications"]["non_booleen"] == 1 and cm["items_par_groupe"]["placebo"]["inconnu"] == 1


def test_banc_de_55_taches(tmp_path):
    items, cle = fabriquer_banc(n_taches=55)  # R-2006 : 55 tâches de la condition « temoin » ; comptes lus
    reps = {x: fabriquer_reponses(cle, x, COUTS[x]) for x in an.LECTEURS}
    r = an.analyser(items, cle, reps, 11, TIRAGES)
    assert (r["comptes_cle"]["taches"], r["comptes_cle"]["items"]) == (55, 55 * 7 + 108)
    assert (fa(r, "A∧B")["total"]["n"], r["combinaisons"]["A∧B"]["instabilite_relectures"]["n"]) == (330, 110)
    assert an.tirer_poids(cle, 11, 20)["placebos"][0].shape == (20, 55)
    pl = de(cle, version="placebo", placebo="ajout", dose_nominale=0.3)
    for n_non_lus, au_dela in ((9, False), (10, True)):  # 9/493 = 1,8 % ; 10/493 = 2,03 %
        rr = copy.deepcopy(reps)
        for c in pl[:n_non_lus]:
            bloquer(rr["A"], "principale", c["item"], statut="illisible")
        assert an.analyser(items, cle, rr, 11, TIRAGES)["lecteurs"]["A"]["au_dela_de_2_pour_cent"] is au_dela


# ---------------------------------------------------------------------------------------------------------------
# R-2007 : seuil des 2 % hors des épisodes exclus ; combinaisons toujours calculées (la v4 en artefact)
# ---------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def banc55():
    return fabriquer_banc(n_taches=55)  # 493 items ; T05 a 9 items (jumeau, 6 placebos, 2 plantés)


def bloquer_episode(cle, lignes, tache):
    for x in presentations(cle, lignes, tache):
        x.update(statut="bloque", reponse_brute=None, categorie_blocage="PROHIBITED_CONTENT")


@pytest.mark.parametrize("isoles, au_dela", [(1, False), (9, False), (10, True)])
def test_R2007_seuil_hors_des_episodes_exclus(banc55, isoles, au_dela):
    items, cle = banc55
    reps = {x: fabriquer_reponses(cle, x, COUTS[x]) for x in an.LECTEURS}
    bloquer_episode(cle, reps["A"], "T05")
    autres = [c for c in de(cle, version="placebo", placebo="ajout", dose_nominale=0.3) if c["tache"] != "T05"]
    for c in autres[:isoles]:
        bloquer(reps["A"], "principale", c["item"], statut="illisible")
    n_ep = len(de(cle, tache="T05"))
    assert n_ep == 9 and len(cle) == 493
    r = an.analyser(items, cle, reps, 11, TIRAGES)
    s2 = r["lecteurs"]["A"]["seuil_2_pour_cent"]
    assert (s2["k"], s2["n"], s2["au_dela"]) == (isoles, 493 - 9, au_dela)  # 1/484 ; 9/484 = 1,86 % ; 10/484 = 2,07 %
    assert s2["items_des_episodes_exclus"] == {"k": 9, "n": 9, "episodes": 1}  # rapportés à part
    assert r["lecteurs"]["A"]["comptes"]["non_lus_principale"]["k"] == 9 + isoles
    ab = r["combinaisons"]["A∧B"]
    assert ab["disponible"] and ab["hors_regle_1"] is au_dela and ab["episodes_exclus"] == ["T05"]
    assert (fa(r, "A∧B")["total"]["k"], fa(r, "A∧B")["total"]["n"]) == (isoles, 330 - 6)
    assert (r["regles"]["1"]["examen"]["A∧B"] == "éligible") is not au_dela
    v4 = an4.analyser(items, cle, reps, 11, TIRAGES)  # artefact : 9 + 1 = 10 sur 493 > 2 % en v4, A∧B disparaissait
    assert v4["lecteurs"]["A"]["au_dela_de_2_pour_cent"] is True and v4["combinaisons"]["A∧B"]["disponible"] is False
    assert "A∧B" not in v4["regles"]["1"]["eligibles"]


def test_R2007_cas_sain_sans_episode_exclu_comme_en_v4(banc, reps):
    _, cle = banc
    for c in de(cle, version="placebo", placebo="suffixe", dose_nominale=0.3)[:5]:
        bloquer(reps["A"], "principale", c["item"])
    r, v4 = analyse(banc, reps), an4.analyser(*banc, reps, 11, TIRAGES)
    s2 = r["lecteurs"]["A"]["seuil_2_pour_cent"]
    assert (s2["k"], s2["n"]) == (5, 528) and s2["items_des_episodes_exclus"] == {"k": 0, "n": 0, "episodes": 0}
    assert r["regle_3_4"]["combinaisons_hors_regle_1"] == []
    for nom, _, _ in an.COMBINAISONS:  # aucun lecteur au-delà : mêmes comptes et mêmes règles qu'en v4
        assert fa(r, nom) == fa(v4, nom) and r["combinaisons"][nom]["rappel"] == v4["combinaisons"][nom]["rappel"]
    assert json.dumps(an._propre(r["regles"]), sort_keys=True) == json.dumps(an._propre(v4["regles"]), sort_keys=True)


def test_R2007_aucun_item_hors_des_episodes_exclus(banc):
    _, cle = banc
    lignes = fabriquer_reponses(cle, "A")
    sig = {an.cle_lecture(x): None for x in lignes if x["lecture"] != "format"}
    s2 = an.seuil_non_lus(lignes, sig, cle, {c["tache"] for c in cle})  # tous les épisodes exclus : rien à mesurer
    assert (s2["k"], s2["n"], s2["taux"], s2["au_dela"]) == (0, 0, None, True)
    assert s2["items_des_episodes_exclus"]["n"] == 528
    s2 = an.seuil_non_lus(lignes, sig, cle, set())
    assert (s2["k"], s2["n"], s2["au_dela"]) == (528, 528, True)
