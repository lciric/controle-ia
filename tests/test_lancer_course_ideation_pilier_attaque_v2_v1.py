"""Essais R5 de `scripts/lancer_course_ideation_pilier_attaque_v2_v1.py`.

Aucun modèle appelé, aucun réseau, l'orchestrateur réel jamais exécuté : un **faux orchestrateur** (dépôt git jetable, faux
`demonstrations/ideation_v8.py` qui consigne ses arguments et les **noms** de son environnement, faux `pole/adaptateurs.py`
dont la sonde rend l'état demandé) est servi au lanceur par `Reglages`, réglage que la ligne de commande n'expose pas.
Pour chaque garde : un cas sain et un artefact (drapeau interdit, plafonds au-dessus du total, bac à sable inactif, et les
gardes d'intégrité : GO, orchestrateur, pièces, arguments)."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_pilier_attaque_v2_v1.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_pilier_attaque_v2_v1", SCRIPT)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

FAUX_V8 = r'''
import json, os, sys
argv = sys.argv[1:]
if "--construire-liste-blanche" in argv:
    import hashlib
    i = argv.index("--construire-liste-blanche")
    sortie = argv[0]
    liste = {os.path.realpath(c): hashlib.sha256(open(c, "rb").read()).hexdigest() for c in argv[i + 1:]}
    open(sortie, "w").write(json.dumps(liste))
    sys.exit(0)
noms_cle = [n for n in os.environ if "KEY" in n or "TOKEN" in n or "SECRET" in n]
json.dump({"argv": argv, "cwd": os.getcwd(), "noms_cle": noms_cle, "go_id": os.environ.get("GO_ID")},
          open(os.environ["FAUX_JOURNAL"], "w"))
sys.exit(int(os.environ.get("FAUX_CODE", "0")))
'''

FAUX_ADAPTATEURS = r'''
import os
def etat_bac_a_sable_detaille():
    e = os.environ.get("FAUX_BAC", "actif")
    if e == "illisible":
        print("pas du JSON")
        raise SystemExit(0)
    if e == "erreur":
        raise RuntimeError("sonde en panne")
    return {"actif": e in ("actif", "sans_proc"), "proc_neuf": e == "actif", "motif": "faux : " + e}
'''

GO_LIGNE = ("| GO-2026-11-08-13 | 2026-11-08 | calcul | **Organisme d'idéation : course sur la question v2 scellée du pilier "
            "attaque** | 20 USD | 2026-11-15 | Lazar | R-1893 |")


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@pytest.fixture
def monde(tmp_path, monkeypatch):
    orch = tmp_path / "orch"
    (orch / "demonstrations").mkdir(parents=True)
    (orch / "pole").mkdir()
    (orch / "demonstrations" / "ideation_v8.py").write_text(FAUX_V8)
    (orch / "pole" / "__init__.py").write_text("")
    (orch / "pole" / "adaptateurs.py").write_text(FAUX_ADAPTATEURS)
    git(orch, "init", "-q", "-b", "main")
    git(orch, "config", "user.email", "t@example.invalid")
    git(orch, "config", "user.name", "t")
    git(orch, "add", "-A")
    git(orch, "commit", "-q", "-m", "faux")
    commit = subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    depot = tmp_path / "depot"
    pieces = {}
    for nom, (rel, _) in lc.PIECES.items():
        p = depot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"pièce factice {nom}\n")
        pieces[nom] = (rel, sha(p))
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n")
    journal = tmp_path / "journal.json"
    env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(journal), "FAUX_BAC": "actif",
           "ANTHROPIC_API_KEY": "valeur-factice-d-essai", "AUTRE_SECRET_X": "factice"}
    r = lc.Reglages(depot=depot, orchestrateur=orch, commit_orchestrateur=commit,
                    empreintes_orchestrateur={"demonstrations/ideation_v8.py": sha(orch / "demonstrations/ideation_v8.py"),
                                              "pole/adaptateurs.py": sha(orch / "pole/adaptateurs.py")},
                    pieces=pieces, registre_go=depot / "registres" / "go.md", dossier_runs=depot / "runs",
                    dossier_sorties=tmp_path / "sorties", depot_attendu_par_l_enveloppe=depot, python=sys.executable,
                    environnement=env, aujourd_hui=dt.date(2026, 11, 9), horodatage=lambda: "Mon Nov  9 07:00:00 UTC 2026")
    return {"r": r, "journal": journal, "env": env, "tmp": tmp_path}


def _refus(r, capsys):
    code = lc.principal([], r)
    err = capsys.readouterr().err
    return code, err


# --------------------------------------------------------------------------------------------------- cas sain de bout en bout

def test_sain_bout_en_bout(monde, capsys):
    r, journal = monde["r"], monde["journal"]
    assert lc.principal([], r) == 0
    j = json.loads(journal.read_text())
    argv = j["argv"]
    assert argv[1:3] == ["--liste-blanche", argv[2]] and Path(argv[2]).name == "liste-blanche.json"
    assert "--accepter-sans-bac-a-sable" not in argv and not any(a.startswith("--tolerer") for a in argv)
    i = argv.index("--budget-controle-externe-usd")
    assert argv[i + 1] == "1.25"
    assert j["noms_cle"] == [] and j["go_id"] == "GO-2026-11-08-13"
    assert Path(j["cwd"]).resolve() == r.orchestrateur.resolve()
    runs = list((r.dossier_runs).iterdir())
    assert len(runs) == 1
    dep = json.loads((runs[0] / "manifeste-lanceur-depart.json").read_text())
    assert dep["plafonds"]["sommes"]["somme_externe"] == 7.95
    assert dep["cles"]["noms_retires_de_l_environnement"] == ["ANTHROPIC_API_KEY", "AUTRE_SECRET_X"]
    assert "valeur-factice-d-essai" not in (runs[0] / "manifeste-lanceur-depart.json").read_text()
    assert dep["bac_a_sable"]["actif"] is True and dep["bac_a_sable"]["proc_neuf"] is True
    fin = json.loads((runs[0] / "manifeste-lanceur-fin.json").read_text())
    assert fin["code"] == 0
    for n in ("manifeste-lanceur-depart.json", "manifeste-lanceur-fin.json"):
        h, nom = (runs[0] / (n + ".sha256")).read_text().split()
        assert nom == n and h == sha(runs[0] / n)
    # la sortie de la course est hors du dépôt
    assert not str(dep["sortie"]).startswith(str(r.depot))


def test_code_de_l_orchestrateur_rendu(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"
    assert lc.principal([], monde["r"]) == 2
    fin = json.loads(next(monde["r"].dossier_runs.iterdir()).joinpath("manifeste-lanceur-fin.json").read_text())
    assert fin["code"] == 2


# --------------------------------------------------------------------------------------------------- garde : drapeaux interdits

def test_drapeaux_sain_commande_production():
    r = lc.Reglages.production()
    argv = lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h")
    lc.garde_drapeaux(argv)  # ne lève pas


@pytest.mark.parametrize("drapeau", ["--accepter-sans-bac-a-sable", "--accepter-sans", "--tolerer-somme-plafonds-externe",
                                     "--tolerer-somme-plafonds", "--tolerer", "--motif-sans-bac-a-sable=x",
                                     "--taille-max-consigne-externe=999999", "--prix-entree-usd-par-million-jetons"])
def test_drapeaux_artefact_direct(drapeau):
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h") + [drapeau]
    with pytest.raises(lc.Refus, match="interdit"):
        lc.garde_drapeaux(argv)


def test_drapeaux_artefact_bout_en_bout(monde, capsys):
    monde["r"].arguments_en_plus = ("--accepter-sans-bac-a-sable",)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "interdit" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


# --------------------------------------------------------------------------------------------------- garde : somme des plafonds

def test_sommes_sain_production():
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h")
    s = lc.garde_sommes(argv)
    assert s["somme_externe"] == 7.95 and s["somme_externe"] < 8.0
    assert s["somme_claude"] == 9.9


def test_sommes_artefact_valeur_du_devis():
    r = lc.Reglages.production()
    r.controle_externe_usd = lc.CONTROLE_EXTERNE_DEVIS_USD  # 1,35 : 8,05 > 8,0
    with pytest.raises(lc.Refus, match="pas sous le total externe"):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h"))


def test_sommes_artefact_egal_au_total():
    r = lc.Reglages.production()
    r.controle_externe_usd = 1.30  # 8,00 : égal, pas dessous
    with pytest.raises(lc.Refus, match="pas sous"):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h"))


def test_sommes_artefact_defauts_de_l_orchestrateur():
    argv = [a for a in lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h")]
    for cle in ("proposeur_ideation|gemini-4-argon=2.0", "juge_ideation|gemini-4-argon=2.5"):
        i = argv.index(cle)
        del argv[i - 1:i + 1]
    i = argv.index("--budget-controle-externe-usd")
    del argv[i:i + 2]
    s = lc.sommes_plafonds(argv)
    assert s["somme_externe"] == 11.2  # 2,5 + 2 × 2,5 + 3,5 + 0,2 : l'échec CL37-03 du rapport 12
    with pytest.raises(lc.Refus):
        lc.garde_sommes(argv)


def test_sommes_artefact_bout_en_bout(monde, capsys):
    monde["r"].plafonds = dict(lc.PLAFONDS_DEVIS, **{"juge_ideation|gemini-4-argon": 3.0})
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "pas sous le total externe" in err and not monde["journal"].exists()


# --------------------------------------------------------------------------------------------------- garde : bac à sable

@pytest.mark.parametrize("etat,motif", [("inactif", "inactif"), ("sans_proc", "/proc neuf"), ("illisible", "illisible"),
                                         ("erreur", "illisible")])
def test_bac_a_sable_artefact(monde, capsys, etat, motif):
    monde["env"]["FAUX_BAC"] = etat
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and motif in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_bac_a_sable_sain(monde):
    env, _ = lc.environnement_sans_cles(monde["env"])
    assert lc.sonder_bac_a_sable(monde["r"], env) == {"actif": True, "proc_neuf": True, "motif": "faux : actif"}


# --------------------------------------------------------------------------------------------------- gardes d'intégrité

def test_arguments_refuses(monde, capsys):
    assert lc.principal(["--accepter-sans-bac-a-sable"], monde["r"]) == 2
    assert "aucun argument" in capsys.readouterr().err and not monde["journal"].exists()


def test_go_sain_registre_reel():
    g = lc.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 9))
    assert g["id"] == "GO-2026-11-08-13" and g["echeance"] == "2026-11-15"


@pytest.mark.parametrize("jour", [dt.date(2026, 11, 7), dt.date(2026, 11, 16)])
def test_go_artefact_hors_periode(monde, capsys, jour):
    monde["r"].aujourd_hui = jour
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "période" in err


def test_go_artefact_revoque(monde, capsys):
    with open(monde["r"].registre_go, "a") as f:
        f.write("| GO-2026-11-09-01 | 2026-11-09 | révocation | révoque GO-2026-11-08-13 | — | — | Lazar | x |\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "révoqué" in err


def test_orchestrateur_artefact_modifie(monde, capsys):
    p = monde["r"].orchestrateur / "pole" / "adaptateurs.py"
    p.write_text(p.read_text() + "\n# remplacement\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "modifié" in err and not monde["journal"].exists()


def test_orchestrateur_artefact_empreinte(monde, capsys):
    monde["r"].empreintes_orchestrateur["pole/adaptateurs.py"] = "0" * 64
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "empreintes" in err


def test_orchestrateur_artefact_commit(monde, capsys):
    monde["r"].commit_orchestrateur = "f" * 40
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "commit" in err


def test_pieces_artefact(monde, capsys):
    rel = monde["r"].pieces["question"][0]
    (monde["r"].depot / rel).write_text("autre question\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


def test_cles_noms_seuls():
    env, retires = lc.environnement_sans_cles({"PATH": "/bin", "ANTHROPIC_API_KEY": "v", "GEMINI_API_KEY_2": "v",
                                               "GH_TOKEN": "v", "LANG": "C"})
    assert retires == ["ANTHROPIC_API_KEY", "GEMINI_API_KEY_2", "GH_TOKEN"]
    assert set(env) == {"PATH", "LANG", "GO_ID"}


def test_source_sans_remplacement_ni_drapeau():
    """Le lanceur n'importe pas l'orchestrateur dans son processus et ne cite les drapeaux interdits que dans sa liste."""
    texte = SCRIPT.read_text()
    assert "import pole" not in texte.replace("from pole.adaptateurs import etat_bac_a_sable_detaille", "")
    assert "setattr(" not in texte and "monkeypatch" not in texte
    assert texte.count('"--accepter-sans-bac-a-sable"') == 1
