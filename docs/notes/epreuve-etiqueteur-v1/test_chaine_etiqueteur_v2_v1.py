"""Essai de bout en bout de la chaîne de la lecture exploratoire v2 de l'étiqueteur (R-2007), v1.

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), développeur neuf, 9 novembre 2026. Aucune donnée réelle, aucun réseau :
1. `generer_items_v3.generer` sur 60 épisodes fabriqués « témoin », dont 5 rendus inéligibles (2 pas à champ CONTROLS
   seulement, moins des 3 pas éligibles exigés) : 55 tâches gardées (R-2006) ; quelques champs CONTROLS en minuscules ;
2. `lire_items_phase1_v5.principal` en mode simulé : essai de format, puis lecture principale et relectures ; chez A,
   un épisode entièrement bloqué (toutes ses présentations, blocage puis relance) et deux items isolés illisibles ;
3. `analyser_phase1_v5` sur les fichiers écrits par la lecture.
Il vérifie la concordance des schémas (générateur, lecture, analyse) et que A∧B est calculée et candidate à la règle 1
dans ce cas ; la v4 de l'analyse, sur les mêmes fichiers, sert d'artefact (A au-delà des 2 %, A∧B non calculée).

Lancement (depuis ce dossier) :
    PYTHON -I -B -m pytest -q -p no:cacheprovider --basetemp=DOSSIER test_chaine_etiqueteur_v2_v1.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import analyser_phase1_v4 as an4  # noqa: E402  (artefact)
import analyser_phase1_v5 as an  # noqa: E402
import format_reponse_v2 as fr  # noqa: E402
import generer_items_v2 as gen  # noqa: E402
import generer_items_v3 as g3  # noqa: E402
import lire_items_phase1_v5 as lire  # noqa: E402

ENTROPIE = 424242
INELIGIBLES = (7, 19, 33, 41, 58)
QUESTION = ICI.parents[2] / "docs" / "procedures" / "ordre-exploratoire-etiqueteur-v2-brouillon1.md"


def pas(t: int, p: int, controle: bool, minuscules: bool) -> str:
    c = f"Compare with baseline A{t} on dataset B{p}. Ablate part C{p}."
    c = c.lower() if minuscules else c
    champ = f"CONTROLS: {c}\n" if controle else ""
    return f"ACTION: ADD\nTITLE: t{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{champ}COST: 10 GPU-hours\nPREDICTION: x."


def episodes_fabriques() -> dict:
    return {f"T{t:02d}": [pas(t, p, controle=t not in INELIGIBLES or p < 2, minuscules=(t % 5 == 0 and p % 3 == 0))
                          for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}


def ecrire(chemin: Path, lignes: list) -> Path:
    chemin.write_bytes(gen.en_jsonl(lignes))
    return chemin


@pytest.fixture(scope="module")
def chaine(tmp_path_factory):
    d = tmp_path_factory.mktemp("chaine")
    eps = episodes_fabriques()
    items, cle, relectures, comptes = g3.generer(eps, {k: "Task." for k in eps}, ENTROPIE, frozenset())
    gardees = {t: eps[t] for t in sorted({c["tache"] for c in cle})}
    f_items, _ = gen.generer_formation(gardees, {}, ENTROPIE, 20)
    for it in f_items:
        it["enonce"] = "Task."
    ch = {"items": ecrire(d / "items.jsonl", items), "cle": ecrire(d / "cle.jsonl", cle),
          "formation": ecrire(d / "formation.jsonl", f_items), "relectures": d / "relectures.txt"}
    ch["relectures"].write_text(g3.liste_relectures(relectures), encoding="utf-8")
    par_tache = {}
    for c in cle:
        par_tache.setdefault(c["tache"], []).append(c["item"])
    bloquee = max(sorted(par_tache), key=lambda t: len(par_tache[t]))  # l'épisode le plus long (9 items)
    isoles = [c["item"] for c in cle if c["version"] == "placebo" and c["tache"] != bloquee][:2]
    pannes = {("A", lec, i, k): "bloque" for i in par_tache[bloquee] for lec in ("principale", "relecture")
              for k in (1, 2)}
    pannes.update({("A", "principale", i, k): "format" for i in isoles for k in (1, 2)})
    simule = lire.FournisseurSimule(pannes)
    commun = ["--simule", "--items", str(ch["items"]), "--formation", str(ch["formation"]),
              "--relectures", str(ch["relectures"]), "--question", str(QUESTION), "--entropie", "3"]
    code_format = lire.principal(commun + ["--lectures", "format", "--sortie", str(d / "fmt")], appeler_simule=simule,
                                 dormir=lambda s: None)
    man = json.loads((d / "fmt" / "manifeste-lecture-phase1-v5.json").read_text(encoding="utf-8"))
    dep = man["depense_estimee_dollars_par_groupe"]
    code_lecture = lire.principal(
        commun + ["--lectures", "principale+relecture", "--sortie", str(d / "lect"), "--feu-vert-format",
                  str(d / "fmt" / "manifeste-lecture-phase1-v5.json"), "--depense-engagee-hors-credits",
                  str(dep["hors_credits"]), "--depense-engagee-claude", str(dep["claude"])],
        appeler_simule=simule, dormir=lambda s: None)
    for x in an.LECTEURS:
        ch[x] = d / "lect" / f"reponses-phase1-{x}-v5.jsonl"
    return {"d": d, "items": items, "cle": cle, "relectures": relectures, "comptes": comptes, "chemins": ch,
            "bloquee": bloquee, "isoles": isoles, "codes": (code_format, code_lecture), "feu_vert": man}


def reponses(chaine) -> dict:
    return {x: an.lire_jsonl(chaine["chemins"][x]) for x in an.LECTEURS}


def test_generateur_v3_ecarte_les_5_taches_et_ecrit_le_champ(chaine):
    cle, comptes = chaine["cle"], chaine["comptes"]
    assert (comptes["taches_ecartees"]["ecartees"], comptes["taches_ecartees"]["gardees"]) == (5, 55)
    assert {c["tache"] for c in cle}.isdisjoint({f"T{t:02d}" for t in INELIGIBLES})
    k = an.compter_cle(cle)
    assert (k["taches"], k["jumeaux"], sum(k["placebos"].values()), sum(k["plantes"].values())) == (55, 55, 330, 108)
    assert len(chaine["relectures"]) == 110
    mods = [m for c in cle for m in c["modifications"]]
    assert all(isinstance(m[an.CHAMP_MINUSCULES], bool) for m in mods)  # nom du champ : celui du générateur
    assert k["champ_minuscules"]["entrees_de_modifications"]["vrai"] > 0
    assert k["champ_minuscules"]["entrees_de_modifications"]["absent"] == 0


def test_schemas_concordants(chaine):
    assert chaine["codes"] == (0, 0) and chaine["feu_vert"]["controle_format"]["feu_vert"] is True
    assert tuple(lire.STATUTS) == an.STATUTS
    assert lire.analyser_reponse is fr.analyser_reponse and an.fr is fr  # un seul analyseur des réponses
    lues = {"lecteur", "lecture", "item", "presentation", "statut", "reponse_brute", "categorie_blocage", "cout_estime"}
    assert lues <= set(lire.CHAMPS_RESULTAT)
    assert an.controler_items_cle(chaine["items"], chaine["cle"]) == []
    reps = reponses(chaine)
    jumeaux = {c["item"] for c in chaine["cle"] if c["version"] == "jumeau"}
    for x, lignes in reps.items():
        assert an.controler_reponses(lignes, chaine["cle"], x) == []
        assert all(set(r) == set(lire.CHAMPS_RESULTAT) and r["lecteur"] == x for r in lignes)
        assert {r["presentation"] for r in lignes if r["lecture"] != "relecture"} == {1}
        rel = {(r["item"], r["presentation"]) for r in lignes if r["lecture"] == "relecture"}
        assert rel == {(j, p) for j in jumeaux for p in an.PRESENTATIONS_RELECTURE}
    bloquees = {c["item"] for c in chaine["cle"] if c["tache"] == chaine["bloquee"]}
    a = reps["A"]
    assert {r["statut"] for r in a if r["lecture"] != "format" and r["item"] in bloquees} == {"bloque"}
    assert {r["categorie_blocage"] for r in a if r["statut"] == "bloque"} == {"PROHIBITED_CONTENT"}
    assert sorted(r["item"] for r in a if r["statut"] == "illisible") == sorted(chaine["isoles"])
    assert all(r["statut"] == "ok" for x in ("B", "C") for r in reps[x])


def test_analyse_v5_sur_la_chaine_A_et_B_calculee_et_candidate(chaine, capsys):
    ch = chaine["chemins"]
    sortie = chaine["d"] / "resultat-v5.json"
    argv = ["--items", str(ch["items"]), "--cle", str(ch["cle"]), "--reponses-a", str(ch["A"]), "--reponses-b",
            str(ch["B"]), "--reponses-c", str(ch["C"]), "--entropie", "3", "--tirages", "500", "--sortie", str(sortie)]
    assert an.principal(argv) == 0
    capsys.readouterr()
    r = json.loads(sortie.read_text(encoding="utf-8"))
    n_ep = sum(c["tache"] == chaine["bloquee"] for c in chaine["cle"])
    assert r["regle_3_4"]["episodes_exclus"] == {"A": [chaine["bloquee"]], "B": [], "C": []}
    s2 = r["lecteurs"]["A"]["seuil_2_pour_cent"]
    assert (s2["k"], s2["n"], s2["au_dela"]) == (2, len(chaine["cle"]) - n_ep, False)
    assert s2["items_des_episodes_exclus"] == {"k": n_ep, "n": n_ep, "episodes": 1}
    ab = r["combinaisons"]["A∧B"]
    assert ab["disponible"] and not ab["hors_regle_1"] and ab["episodes_exclus"] == [chaine["bloquee"]]
    assert ab["fausses_alarmes_placebos"]["total"]["n"] == 330 - 6
    assert not r["regles"]["1"]["examen"]["A∧B"].startswith("non candidate")  # candidate à la règle 1
    assert r["regles"]["1"]["examen"]["A∧B"] == "éligible" and "A∧B" in r["regles"]["1"]["eligibles"]
    assert r["comptes_cle"]["champ_minuscules"]["items_par_groupe"]["placebo"]["minuscules"] > 0
    # artefact : la v4, sur les mêmes fichiers, comptait l'épisode exclu dans les 2 % : A au-delà, A∧B non calculée
    v4 = an4.analyser(*(an.lire_jsonl(ch[k]) for k in ("items", "cle")), reponses(chaine), 3, 500)
    assert v4["lecteurs"]["A"]["comptes"]["non_lus_principale"]["k"] == n_ep + 2 and n_ep + 2 > 0.02 * len(chaine["cle"])
    assert v4["lecteurs"]["A"]["au_dela_de_2_pour_cent"] is True
    assert v4["combinaisons"]["A∧B"]["disponible"] is False and "A∧B" not in v4["regles"]["1"]["eligibles"]
