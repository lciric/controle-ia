"""Essais R5 de `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py` (voie (a), R-1981 ; corrections de la
contre-lecture `4591fe97…`, R-1984 : M1, m1 à m6).

Aucun modèle appelé, aucun réseau, l'orchestrateur réel jamais exécuté : un **faux orchestrateur** (dépôt git jetable, faux
`demonstrations/ideation_v8.py` qui consigne ses arguments et les **noms** de son environnement, faux `pole/adaptateurs.py`
dont la sonde rend l'état demandé) est servi au lanceur par `Reglages`, réglage que la ligne de commande n'expose pas.
Pour chaque garde : un cas sain et un artefact (drapeau interdit, plafonds au-dessus du total, bac à sable inactif, et les
gardes d'intégrité : GO, orchestrateur, pièces, arguments), plus les gardes de taille par calcul (passe 1 trop basse,
passe 2 trop basse, mesure illisible). Ajouts de la version 3 : cache d'octets planté (`.pyc` et `__pycache__`, fichier
ignoré), préfixe du cache transmis et effectif sous `-I`, interpréteur, plafond du GO, seuil de la passe 2, juge comparé
à sa consigne, environnement sans copie, et les artefacts manquants de m6."""
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
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_pilier_attaque_v2_v3.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_pilier_attaque_v2_v3", SCRIPT)
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
json.dump({"argv": argv, "cwd": os.getcwd(), "noms_cle": noms_cle, "go_id": os.environ.get("GO_ID"),
           "pycache_prefix": sys.pycache_prefix, "pycache_env": os.environ.get("PYTHONPYCACHEPREFIX"),
           "orig_argv": sys.orig_argv}, open(os.environ["FAUX_JOURNAL"], "w"))
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

# tailles de `mesurer-consignes-pilier-attaque-v2-v1.json` (`db44b41e…`), seules clés lues par le lanceur
MESURE = {"prix_entree_usd_par_million_jetons": 10.0,
          "consignes": {"consigne_de_controle_externe": 415253, "consigne_passe_1": 60637, "consigne_passe_2_maximale": 414778,
                        "nombre_par_proposeur": 8, "fiches_au_juge_au_maximum": 52, "consigne_du_juge_maximale": 2194842}}

PFX = Path("/x/sortie/pycache")

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
    (orch / ".gitignore").write_text("__pycache__/\n*.pyc\n*.log\n")
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
        p.write_text(json.dumps(MESURE) if nom == "mesure_consignes" else f"pièce factice {nom}\n")
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
    assert argv[argv.index("--budget-passe-2-externe-usd") + 1] == "2.3"
    assert "proposeur_ideation|gemini-4-argon=1.7" in argv
    assert j["noms_cle"] == [] and j["go_id"] == "GO-2026-11-08-13"
    assert Path(j["cwd"]).resolve() == r.orchestrateur.resolve()
    runs = list((r.dossier_runs).iterdir())
    assert len(runs) == 1
    dep = json.loads((runs[0] / "manifeste-lanceur-depart.json").read_text())
    assert dep["plafonds"]["sommes"]["somme_externe"] == 7.95
    assert dep["cles"]["noms_retires_de_l_environnement"] == ["ANTHROPIC_API_KEY", "AUTRE_SECRET_X"]
    assert "valeur-factice-d-essai" not in (runs[0] / "manifeste-lanceur-depart.json").read_text()
    assert dep["bac_a_sable"]["actif"] is True and dep["bac_a_sable"]["proc_neuf"] is True
    assert dep["plafonds"]["gardes_de_taille"]["course"]["marge"] == 24747
    # M1 : préfixe du cache neuf, hors du clone, effectif sous -I (option -X), variable aussi transmise
    pfx = Path(dep["cache_d_octets"]["prefixe"])
    assert pfx.is_dir() and pfx.parent == Path(dep["sortie"]).parent
    assert r.orchestrateur.resolve() not in pfx.resolve().parents
    assert j["pycache_prefix"] == str(pfx) and j["pycache_env"] == str(pfx)
    assert j["orig_argv"][1:5] == ["-I", "-B", "-X", f"pycache_prefix={pfx}"]
    assert dep["go"]["plafond_usd"] == 20.0
    assert dep["python"]["chemin"] == r.python
    assert "jamais lues" not in json.dumps(dep, ensure_ascii=False)
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
    argv = lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h", PFX)
    lc.garde_drapeaux(argv)  # ne lève pas


@pytest.mark.parametrize("drapeau", ["--accepter-sans-bac-a-sable", "--accepter-sans", "--tolerer-somme-plafonds-externe",
                                     "--tolerer-somme-plafonds", "--tolerer", "--motif-sans-bac-a-sable=x",
                                     "--taille-max-consigne-externe=999999", "--prix-entree-usd-par-million-jetons"])
def test_drapeaux_artefact_direct(drapeau):
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX) + [drapeau]
    with pytest.raises(lc.Refus, match="interdit"):
        lc.garde_drapeaux(argv)


def test_drapeaux_artefact_bout_en_bout(monde, capsys):
    monde["r"].arguments_en_plus = ("--accepter-sans-bac-a-sable",)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "interdit" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


# --------------------------------------------------------------------------------------------------- garde : somme des plafonds

def test_sommes_sain_production():
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX)
    s = lc.garde_sommes(argv)
    assert s["somme_externe"] == 7.95 and s["somme_externe"] < 8.0
    assert s["somme_claude"] == 9.9


def test_sommes_artefact_valeur_du_devis():
    r = lc.Reglages.production()
    r.controle_externe_usd = lc.CONTROLE_EXTERNE_DEVIS_USD  # 1,35 : 8,05 > 8,0
    with pytest.raises(lc.Refus, match="pas sous le total externe"):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


def test_sommes_artefact_egal_au_total():
    r = lc.Reglages.production()
    r.controle_externe_usd = 1.30  # 8,00 : égal, pas dessous
    with pytest.raises(lc.Refus, match="pas sous"):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


def test_sommes_artefact_defauts_de_l_orchestrateur():
    argv = [a for a in lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX)]
    for cle in ("proposeur_ideation|gemini-4-argon=1.7", "juge_ideation|gemini-4-argon=2.5"):
        i = argv.index(cle)
        del argv[i - 1:i + 1]
    for opt in ("--budget-controle-externe-usd", "--budget-passe-2-externe-usd"):
        i = argv.index(opt)
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
    pfx = monde["tmp"] / "pfx-absent" / "pycache"
    env, _ = lc.environnement_sans_cles(monde["env"], pfx)
    assert lc.sonder_bac_a_sable(monde["r"], env, pfx) == {"actif": True, "proc_neuf": True, "motif": "faux : actif"}


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


# --------------------------------------------------------------------------------------------------- gardes de taille (calcul)

def test_tailles_sain_production():
    r = lc.Reglages.production()
    g = lc.garde_tailles(r, lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))
    assert (g["course"]["taille_max"], g["course"]["marge"]) == (440000, 24747)
    assert (g["passe_1"]["taille_max"], g["passe_1"]["marge"]) == (360000, 299363)
    # m1 : consigne de passe 2 aux fiches de 8 000 (≈ 60 637 + 8 × 8 009), plus la « marge » fictive contre 414 778
    assert (g["passe_2_fiches_8000"]["taille_max"], g["passe_2_fiches_8000"]["consigne"]) == (600000, 124709)
    assert g["passe_2_fiches_8000"]["marge"] == 475291
    s2 = g["passe_2_seuil_de_fiche"]
    assert s2["fiche_de_passe_1_la_plus_longue_admise"] == 17901
    assert s2["depense_au_plus_si_refus_usd"] == 3.35
    assert s2["consigne_passe_2_maximale_mesuree"] == 414778
    assert "185222" not in json.dumps(g) and "marge_contre_415253" not in json.dumps(g)
    # m3 : juge contre sa propre consigne maximale, rapporté sans garde
    j = g["juge_argon_rapporte"]
    assert (j["taille_max"], j["consigne_du_juge_maximale"], j["marge_au_maximum_theorique"]) == (480000, 2194842, -1714842)
    assert j["lecture"].startswith("ne passerait pas au maximum théorique")


def test_tailles_sain_borne_basse_passe_2(monde):
    r = monde["r"]
    r.passe_2_externe_usd = 2.25  # 900 000 − 480 000 = 420 000 ≥ 415 253
    g = lc.garde_tailles(r, lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))
    assert g["course"]["marge"] == 4747


@pytest.mark.parametrize("p2", [2.0, 2.2])
def test_tailles_artefact_passe_2_trop_basse(monde, p2):
    r = monde["r"]
    r.passe_2_externe_usd = p2  # 2,0 : 320 000 < 415 253 (l'arrêt de la version 1)
    with pytest.raises(lc.Refus, match="course"):
        lc.garde_tailles(r, lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


def test_tailles_artefact_passe_1_trop_basse(monde):
    r = monde["r"]
    r.plafonds = dict(lc.PLAFONDS_REGLES, **{"proposeur_ideation|gemini-4-argon": 0.9})  # 360 000 − 320 000 < 60 637
    with pytest.raises(lc.Refus, match="passe_1"):
        lc.garde_tailles(r, lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


def test_tailles_artefact_bout_en_bout(monde, capsys):
    monde["r"].passe_2_externe_usd = 2.0
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "garde(s) de taille" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_tailles_artefact_mesure_illisible(monde, capsys):
    rel = monde["r"].pieces["mesure_consignes"][0]
    p = monde["r"].depot / rel
    p.write_text(json.dumps({"prix_entree_usd_par_million_jetons": 10.0, "consignes": {}}))
    monde["r"].pieces["mesure_consignes"] = (rel, sha(p))
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "illisible" in err and not monde["journal"].exists()


def test_pieces_sain_sur_main():
    """Les pièces copiées sur `main` sont trouvées, empreintes conformes."""
    assert set(lc.verifier_pieces(lc.Reglages.production())) == set(lc.PIECES)


# =================================================================================================== ajouts de la version 3

# --------------------------------------------------------------------------------------------------- M1 : cache d'octets

def _committer_tout(orch):
    git(orch, "add", "-A")
    git(orch, "commit", "-q", "-m", "faux 2")
    return subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()


def test_cache_sain_clone_sans_cache(monde):
    assert lc.caches_d_octets(monde["r"].orchestrateur) == []
    o = lc.verifier_orchestrateur(monde["r"])
    assert o["fichiers_ignores"] == [] and o["caches_d_octets"] == []


def test_cache_artefact_pyc_plante_bout_en_bout(monde, capsys):
    """Un `.pyc` valide planté à côté d'une source (ignoré par le `.gitignore` : `git status --porcelain` le tait)."""
    orch = monde["r"].orchestrateur
    pyc = orch / "pole" / "__pycache__" / f"adaptateurs.{sys.implementation.cache_tag}.pyc"
    import py_compile
    py_compile.compile(str(orch / "pole" / "adaptateurs.py"), cfile=str(pyc), doraise=True)
    assert subprocess.run(["git", "-C", str(orch), "status", "--porcelain"], capture_output=True, text=True).stdout == ""
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "ignorés" in err and "__pycache__" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_cache_artefact_autre_fichier_ignore(monde, capsys):
    (monde["r"].orchestrateur / "trace.log").write_text("x")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "--ignored" in err and "trace.log" in err


def test_cache_artefact_pyc_suivi_par_git(monde, capsys):
    """Un `.pyc` versionné (hors `git status`, hors `--ignored`) : la recherche sous l'orchestrateur le trouve."""
    orch = monde["r"].orchestrateur
    (orch / ".gitignore").write_text("*.log\n")
    (orch / "pole" / "relais.pyc").write_bytes(b"\x00faux")
    monde["r"].commit_orchestrateur = _committer_tout(orch)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "cache d'octets sous l'orchestrateur" in err and "relais.pyc" in err


def test_cache_artefact_dossier_pycache_vide(tmp_path):
    (tmp_path / "pole" / "__pycache__").mkdir(parents=True)
    assert lc.caches_d_octets(tmp_path) == [str(tmp_path / "pole" / "__pycache__")]


def test_prefixe_effectif_sous_I_et_variable_ignoree(tmp_path):
    """Constat de la version 3 : sous `-I`, Python ignore `PYTHONPYCACHEPREFIX` mais suit `-X pycache_prefix` ; un `.pyc`
    planté (valide, d'une autre source) n'est plus lu avec le préfixe."""
    import os
    import py_compile
    mod = tmp_path / "m"
    mod.mkdir()
    src = mod / "cible.py"
    src.write_text("VALEUR = 'source'\n")
    st = src.stat()
    leurre = tmp_path / "leurre.py"
    leurre.write_text("VALEUR = 'leurre'\n")
    os.utime(leurre, ns=(st.st_atime_ns, st.st_mtime_ns))
    # même taille de source (horodatage et taille sont vérifiés par l'en-tête du .pyc)
    assert len(leurre.read_bytes()) == len(src.read_bytes())
    pyc = mod / "__pycache__" / f"cible.{sys.implementation.cache_tag}.pyc"
    py_compile.compile(str(leurre), cfile=str(pyc), doraise=True)
    code = "import sys; sys.path.insert(0, sys.argv[1]); import cible; print(cible.VALEUR, sys.pycache_prefix)"
    base = {"PATH": "/usr/bin:/bin"}
    sans = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(mod)], env=base, capture_output=True, text=True)
    assert sans.stdout.split()[0] == "leurre"     # le trou de M1 : -B n'empêche pas la lecture
    var = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(mod)], capture_output=True, text=True,
                         env=dict(base, PYTHONPYCACHEPREFIX=str(tmp_path / "pfx1")))
    assert var.stdout.split() == ["leurre", "None"]   # la variable seule ne tient pas sous -I
    opt = subprocess.run([sys.executable, *lc.options_interprete(tmp_path / "pfx2"), "-c", code, str(mod)],
                         env=base, capture_output=True, text=True)
    assert opt.stdout.split() == ["source", str(tmp_path / "pfx2")]
    assert not (tmp_path / "pfx2").exists()           # -B : rien écrit


def test_prefixe_sain_et_artefacts(tmp_path):
    clone = tmp_path / "clone"
    clone.mkdir()
    lc.verifier_prefixe_pycache(tmp_path / "sorties" / "id" / "pycache", clone)
    with pytest.raises(lc.Refus, match="dans le clone"):
        lc.verifier_prefixe_pycache(clone / "orchestrator" / "pycache", clone)
    (tmp_path / "deja").mkdir()
    with pytest.raises(lc.Refus, match="déjà présent"):
        lc.verifier_prefixe_pycache(tmp_path / "deja", clone)
    with pytest.raises(lc.Refus, match="non absolu"):
        lc.verifier_prefixe_pycache(Path("relatif/pycache"), clone)


def test_prefixe_artefact_sortie_dans_le_clone_bout_en_bout(monde, capsys):
    monde["r"].dossier_sorties = monde["r"].orchestrateur / "sorties"
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "dans le clone" in err and not monde["journal"].exists()


def test_orchestrateur_sain_clone_reel():
    """Le vrai clone : commit, arbre propre fichiers ignorés compris, aucun cache, empreintes (git et sha256 seulement ;
    rien de l'orchestrateur importé ni exécuté)."""
    r = lc.Reglages.production()
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    o = lc.verifier_orchestrateur(r)
    assert o["commit"] == lc.COMMIT_ORCHESTRATEUR and o["racine_clone"] == "/home/user/ideation-organism"


# --------------------------------------------------------------------------------------------------- m5 : interpréteur

def test_interprete_sain(monde):
    assert lc.verifier_interprete(monde["r"])["chemin"] == sys.executable


def test_interprete_production_absolu():
    r = lc.Reglages.production()
    assert r.python == "/usr/local/bin/python3" == lc.PYTHON_COURSE
    assert Path(r.python).is_file()
    argv = lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX)
    assert argv[0] == "/usr/local/bin/python3"


@pytest.mark.parametrize("python,motif", [("python3", "non absolu"), ("/nulle/part/python3", "absent"),
                                          ("/bin/sh", "un seul interpréteur")])
def test_interprete_artefacts(monde, capsys, python, motif):
    monde["r"].python = python
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


# --------------------------------------------------------------------------------------------------- m2 : plafond du GO

def test_go_plafond_sain_registre_reel():
    g = lc.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 9))
    assert g["plafond_usd"] == 20.0


@pytest.mark.parametrize("plafond,motif", [("19 USD", "sous les totaux"), ("19,99 USD", "sous les totaux"),
                                           ("vingt", "illisible"), ("", "illisible")])
def test_go_plafond_artefacts(monde, capsys, plafond, motif):
    reg = monde["r"].registre_go
    reg.write_text(reg.read_text().replace("| 20 USD |", f"| {plafond} |"))
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and motif in err


# --------------------------------------------------------------------------------------------------- m4 : environnement

def test_environnement_sans_copie_integrale():
    """Le filtrage ne lit la valeur d'aucune variable de clé : une correspondance qui lève à la lecture d'une clé passe."""
    class Env(dict):
        def __getitem__(self, n):
            if "KEY" in n or "TOKEN" in n:
                raise AssertionError(f"valeur de {n} lue")
            return dict.__getitem__(self, n)
    env, retires = lc.environnement_sans_cles(Env(PATH="/bin", ANTHROPIC_API_KEY="v", GH_TOKEN="v"), Path("/p/pycache"))
    assert retires == ["ANTHROPIC_API_KEY", "GH_TOKEN"]
    assert env == {"PATH": "/bin", "GO_ID": "GO-2026-11-08-13", "PYTHONPYCACHEPREFIX": "/p/pycache"}


def test_environnement_source_sans_dict_os_environ():
    assert "dict(os.environ)" not in SCRIPT.read_text()


# --------------------------------------------------------------------------------------------------- m6 : artefacts manquants

@pytest.mark.parametrize("avant,apres,motif", [
    ("| calcul |", "| publication |", "type"),
    ("| Lazar |", "| Claude |", "Lazar exigé"),
    ("**Organisme d'idéation : course sur la question v2 scellée du pilier attaque**", "phase 0 : T0.6", "périmètre"),
])
def test_go_artefacts_ligne(monde, capsys, avant, apres, motif):
    reg = monde["r"].registre_go
    reg.write_text(reg.read_text().replace(avant, apres))
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and motif in err


def test_go_artefact_identifiant_en_double(monde, capsys):
    with open(monde["r"].registre_go, "a") as f:
        f.write(GO_LIGNE + "\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "2 ligne(s) principale(s)" in err


@pytest.mark.parametrize("option,valeur", [("--budget-total-usd", "13.0"), ("--budget-externe-usd", "7.0")])
def test_sommes_artefact_totaux_differents(option, valeur):
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX)
    argv[argv.index(option) + 1] = valeur
    with pytest.raises(lc.Refus, match="du GO"):
        lc.garde_sommes(argv)


def _mesure(monde, **modif):
    rel = monde["r"].pieces["mesure_consignes"][0]
    p = monde["r"].depot / rel
    m = json.loads(json.dumps(MESURE))
    for k, v in modif.items():
        if k == "prix":
            m["prix_entree_usd_par_million_jetons"] = v
        else:
            m["consignes"][k] = v
    p.write_text(json.dumps(m))
    monde["r"].pieces["mesure_consignes"] = (rel, sha(p))


def test_tailles_artefact_autre_prix(monde, capsys):
    _mesure(monde, prix=8.3)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "autre prix" in err


def test_tailles_artefact_nombre_different(monde, capsys):
    _mesure(monde, nombre_par_proposeur=7)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "--nombre" in err


def test_tailles_artefact_passe_2_fiches_8000(monde):
    """La consigne de passe 1 grossie au point que la passe 2 aux fiches de 8 000 ne tienne plus (600 000)."""
    _mesure(monde, consigne_passe_1=600000 - 8 * 8009 + 1)   # 535 929
    r = monde["r"]
    # passe 1 à 2,2 : 880 000 − 320 000 = 560 000 ≥ 535 929, elle tient ; seule la passe 2 (600 000 < 600 001) tombe
    r.plafonds = dict(lc.PLAFONDS_REGLES, **{"proposeur_ideation|gemini-4-argon": 2.2})
    with pytest.raises(lc.Refus, match="passe_2_fiches_8000") as e:
        lc.garde_tailles(r, lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))
    assert '"passe_1"' not in str(e.value) and '"course"' not in str(e.value)


def test_seuil_passe_2_formule():
    assert lc.seuil_fiche_passe_2(920000, 60637, 8) == 17901
    # à la borne : la consigne estimée au seuil tient, un caractère de plus non
    f = 17901
    assert 60637 + 8 * (f + 9) <= 920000 - 8 * f * 5
    assert 60637 + 8 * (f + 1 + 9) > 920000 - 8 * (f + 1) * 5


def test_ecrire_scelle_artefact_existant(tmp_path):
    p = tmp_path / "m.json"
    lc.ecrire_scelle(p, {"a": 1})
    with pytest.raises(lc.Refus, match="existe déjà"):
        lc.ecrire_scelle(p, {"a": 2})
    assert json.loads(p.read_text()) == {"a": 1}


def test_dossier_de_run_deja_present(monde, capsys, monkeypatch):
    class Fige(dt.datetime):
        @classmethod
        def now(cls, tz=None):
            return dt.datetime(2026, 11, 9, 7, 0, 0, tzinfo=dt.timezone.utc)
    monkeypatch.setattr(lc._dt, "datetime", Fige)
    (monde["r"].dossier_runs / "20261109-070000-course-ideation-pilier-attaque-v2-v3").mkdir(parents=True)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "existe déjà" in err and not monde["journal"].exists()


def test_orchestrateur_absent(monde, capsys):
    monde["r"].orchestrateur = monde["tmp"] / "nulle-part"
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "orchestrateur absent" in err


def test_chemin_avec_espace():
    r = lc.Reglages.production()
    r.depot = Path("/un dossier/depot")
    with pytest.raises(lc.Refus, match="espace"):
        lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX)


def test_date_u_illisible(monkeypatch):
    monkeypatch.setattr(lc.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 1, stdout="", stderr="panne"))
    with pytest.raises(lc.Refus, match="date -u"):
        lc.date_u()


def test_date_u_saine():
    assert "UTC" in lc.date_u()
