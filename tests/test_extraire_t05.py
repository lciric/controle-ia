"""Procédure d'extraction v1 de T0.5 : copie de lecture, scripts autonomes d'accord avec le module (codes d'erreur),
avis de contre-vérification, statut des papiers, listes de tâches, et déroulé complet dans un dépôt jetable (retours des
sous-agents, rondes, avis illisible refait, audit, vérification des exclusions « theory_only », seuil, entrées
modifiées). Chaque garde d'arrêt est éprouvée sur un cas sain et sur un artefact (R5)."""
import copy
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.environnements import extraction as ex
from controle_ia.environnements import extraire_t05 as et
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, graines
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
PROC = RACINE / "docs" / "procedures" / "T0.5-extraction-v1"
TEXTE = ("Introduction. We study routers in mixture-of-experts models.\n"
         "We compare against a dense baseline trained with the same compute budget.\n"
         "Removing the load-balancing loss leads to expert collapse.\n"
         "We also ablate the number of experts from 8 to 64, a gap of -3 points.\n"
         "Training the largest model took 1,200 GPU hours on A100 GPUs.\n"
         "Our main finding is that top-2 routing with capacity factor 1.25 matches *dense* quality, a 5\\% gain.\n"
         "We call this the \"capacity\" regime and the gate's load, a self-balancing effect.\n")
H9 = {"affiliations": [{"author": "Lead Author 1", "institutions": ["Dept of CS, X University"]}],
      "research_questions": "Mixture-of-experts models route tokens to experts. " * 8,
      "costs": {"total": None, "splits": []}}
H10 = {"theory_experiment": "experiments_only", "data_type": "real_only", "domains": []}
CIBLES = {"controls": [
    {"id": "C1", "description": "a dense baseline with matched compute",
     "evidence": "We compare against a dense baseline trained with the same compute budget.", "section": "1"},
    {"id": "C2", "description": "an ablation of the load-balancing loss",
     "evidence": "Removing the load-balancing loss leads to expert collapse.", "section": "1"},
    {"id": "C3", "description": "an ablation of the number of experts",
     "evidence": "We also ablate the number of experts from 8 to 64", "section": "1"}],
    "compute": {"reference_gpu_hours": 1200, "basis": "reported", "evidence": "1,200 GPU hours"},
    "fruitful_directions": [{"id": "F1", "description": "top-2 routing with a moderate capacity factor",
                             "evidence": "capacity factor 1.25 matches dense quality, a 5% gain", "section": "1"}],
    "sterile_directions": []}
AVIS = {"statement_leaks": False, "leak_passages": [], "theory_experiment_correct": True,
        "theory_experiment_expected": "experiments_only", "data_type_correct": True, "data_type_expected": "real_only",
        "domains_reasonable": True, "compute_plausible": True, "comment": "ok",
        "targets": [{"id": i, "grounded": True, "observable": True, "comment": ""} for i in ("C1", "C2", "C3", "F1")]}
OK_LIGNE = "OK: 0 error(s), 0 warning(s)"


# --- copie de lecture --------------------------------------------------------------------------------------------

def test_copie_de_lecture_cas_sain():
    texte = "# Titre\n\n" + "\n".join(f"ligne {i} " + "x" * (i % 70) for i in range(500)) + "\n" + "+" + "-" * 3000
    parties = ex.copie_de_lecture(texte, taille_partie=4000, lignes_partie=40)
    assert len(parties) > 5 and "".join(parties) == texte
    assert all(len(p) <= 4000 and p.count("\n") <= 40 for p in parties)


def test_copie_de_lecture_ligne_trop_longue():
    with pytest.raises(GardeArret, match="ligne de plus"):
        ex.copie_de_lecture("court\n" + "x" * 5000, taille_partie=4000)


# --- scripts autonomes : mêmes codes que le module ---------------------------------------------------------------

def _dossier_sorties(tmp_path, texte, h9, h10, cibles):
    d = tmp_path / "p"
    (d / "papier").mkdir(parents=True)
    (d / "sorties").mkdir()
    for k, partie in enumerate(ex.copie_de_lecture(texte, taille_partie=200), start=1):
        (d / "papier" / f"partie-{k:02d}.md").write_text(partie, encoding="utf-8")
    for nom, obj in (("h9", h9), ("h10", h10), ("cibles", cibles)):
        if obj is not None:
            (d / "sorties" / f"{nom}.json").write_text(obj if isinstance(obj, str) else json.dumps(obj),
                                                     encoding="utf-8")
    return d


def _script(nom, d):
    r = subprocess.run([sys.executable, "-I", str(PROC / nom), str(d)], capture_output=True, text=True)
    return r.returncode, r.stdout.strip().splitlines()


def _codes_script(lignes):
    return sorted(ligne.split("[", 1)[1].split("]", 1)[0] for ligne in lignes if ligne.startswith("ERROR:"))


def _avec(base, **champs):
    s = copy.deepcopy(base)
    s.update(champs)
    return s


def _cas_sorties():
    cas = {"sain": (H9, H10, CIBLES)}
    cas["h9 court"] = (_avec(H9, research_questions="court"), H10, CIBLES)
    cas["h9 figure"] = (_avec(H9, research_questions=H9["research_questions"] + " See Table 3."), H10, CIBLES)
    cas["h9 costs"] = (_avec(H9, costs="?"), H10, CIBLES)
    cas["h9 objet"] = ("[1, 2]", H10, CIBLES)
    cas["h10 valeur"] = (H9, _avec(H10, theory_experiment="mostly theory"), CIBLES)
    cas["h10 valeur échappée"] = (H9, _avec(H10, theory_experiment="mostly\\_theory"), CIBLES)
    cas["h10 clé échappée"] = (H9, {"theory_experiment": "experiments_only", "data\\_type": "real_only",
                                    "domains": []}, CIBLES)
    cas["h10 domaines"] = (H9, _avec(H10, domains="x"), CIBLES)
    c = copy.deepcopy(CIBLES)
    c["controls"][1]["evidence"] = "Removing the router leads to a total collapse of everything."
    cas["citation introuvable"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["evidence"] = "too short"
    cas["citation courte"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"] = c["controls"][:2]
    cas["bornes"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["fruitful_directions"][0]["id"] = "C1"
    cas["identifiant double"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["id"] = ["C1"]
    cas["identifiant non textuel"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["description"] = "short"
    cas["description"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][0] = "C1"
    cas["élément"] = (H9, H10, c)
    for valeur in (-3, True, "12", 10 ** 400, 0.0):
        c = copy.deepcopy(CIBLES)
        c["compute"]["reference_gpu_hours"] = valeur
        cas[f"calcul {str(valeur)[:12]}"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["compute"]["basis"] = "guessed"
    cas["calcul base"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][2]["evidence"] = "We also ablate the number of experts from 8 to 64, a gap of −3 points."
    cas["typographie"] = (H9, H10, c)
    cas["json illisible"] = (H9, H10, '{"controls": [}')
    cas["nan"] = (H9, H10, json.dumps(CIBLES).replace("1200", "NaN"))
    cas["absent"] = (H9, None, CIBLES)
    cas["alertes"] = (_avec(H9, research_questions=H9["research_questions"] + " In this work we propose X."),
                      H10, CIBLES)
    # barres obliques inverses non doublées (CL-1) : « \theta » devient une tabulation, « \nabla » un saut de ligne
    cas["barre oblique tabulation"] = (_avec(H9, research_questions=H9["research_questions"] + " Let $\theta$ be."),
                                       H10, CIBLES)
    cas["barre oblique saut"] = (_avec(H9, research_questions=H9["research_questions"] + " With $\nabla f$ given."),
                                 H10, CIBLES)
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["description"] = "a dense baseline \beta with matched compute"
    cas["barre oblique cible"] = (H9, H10, c)
    # contre-lecture 2 : montants en dollars (D-1), \nabla en $$…$$ et \nu (D-4), substitut isolé (D-10)
    rq = H9["research_questions"]
    cas["dollars deux paragraphes"] = (_avec(H9, research_questions=rq + " Training cost over $100M.\n\nLater runs "
                                             "cost $5M."), H10, CIBLES)
    cas["dollars échappés"] = (_avec(H9, research_questions=rq + " Over \\$100M.\n\nThen \\$5M."), H10, CIBLES)
    cas["montant puis formule"] = (_avec(H9, research_questions=rq + " Over $100M.\n\nLet $\\theta$ be."), H10,
                                   CIBLES)
    cas["nabla en double dollar"] = (_avec(H9, research_questions=rq + " where $$\nabla f$$ is"), H10, CIBLES)
    cas["nu corrompu"] = (_avec(H9, research_questions=rq + " with $a \nu$ fixed"), H10, CIBLES)
    cas["substitut isolé"] = (_avec(H9, research_questions=rq + " x\ud835y"), H10, CIBLES)
    for nom_tiret, tiret in (("U+2010", "\u2010"), ("U+2011", "\u2011"), ("U+2012", "\u2012"),
                             ("U+2013", "\u2013"), ("U+2014", "\u2014")):
        c = copy.deepcopy(CIBLES)
        c["controls"][2]["evidence"] = f"We also ablate the number of experts from 8 to 64, a gap of {tiret}3 points."
        cas[f"tiret {nom_tiret}"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["controls"][2]["evidence"] = "We also ablate the num\u00adber of experts from 8 to 64"
    cas["trait d'union conditionnel"] = (H9, H10, c)
    c = copy.deepcopy(CIBLES)
    c["fruitful_directions"][0]["evidence"] = "We call this the \u201ccapacity\u201d regime and the gate\u2019s load"
    cas["guillemets typographiques"] = (H9, H10, c)
    # fuite mécanique (CL-26) : l'énoncé reprend 8 mots consécutifs de la citation d'une direction féconde
    c = copy.deepcopy(CIBLES)
    c["fruitful_directions"][0]["evidence"] = "Our main finding is that top-2 routing with capacity factor 1.25"
    cas["fuite mécanique"] = (_avec(H9, research_questions=H9["research_questions"]
                                    + " Is it true that our main finding is that top-2 routing with capacity?"),
                              H10, c)
    return cas


@pytest.mark.parametrize("nom", sorted(_cas_sorties()))
def test_verifier_sortie_memes_codes_que_le_module(tmp_path, nom):
    h9, h10, cibles = _cas_sorties()[nom]
    d = _dossier_sorties(tmp_path, TEXTE, h9, h10, cibles)
    module = ex.lire_sorties(d / "sorties", TEXTE)
    code, lignes = _script("verifier-sortie-v1.py", d)
    assert _codes_script(lignes) == sorted(ex.code_anomalie(a) for a in module["anomalies"]), (lignes, module)
    assert sum(ligne.startswith("WARNING:") for ligne in lignes) == len(module["alertes"])
    assert (code == 0) == (not module["anomalies"])
    assert lignes[-1].startswith("OK" if not module["anomalies"] else "NOT OK")
    attendus = {"sain": [], "typographie": [], "h10 clé échappée": [], "h10 valeur échappée": [], "alertes": [],
                "calcul 100000000000": ["cibles.calcul_valeur"],
                "dollars deux paragraphes": [], "dollars échappés": [], "montant puis formule": [],
                "nabla en double dollar": ["texte.formule"], "nu corrompu": ["texte.formule"],
                "substitut isolé": ["texte.substitut"], "tiret U+2010": [], "tiret U+2011": [], "tiret U+2012": [],
                "tiret U+2013": [], "tiret U+2014": [], "trait d'union conditionnel": [],
                "guillemets typographiques": [],
                "barre oblique tabulation": ["texte.controle"], "barre oblique saut": ["texte.formule"],
                "barre oblique cible": ["texte.controle"], "fuite mécanique": ["h9.fuite_citation"],
                "identifiant non textuel": ["cibles.identifiant"], "bornes": ["cibles.bornes"]}
    if nom in attendus:
        assert sorted(ex.code_anomalie(a) for a in module["anomalies"]) == attendus[nom], module["anomalies"]
    if nom == "bornes":
        assert "never invent" in " ".join(lignes)
    if nom == "alertes":
        assert module["alertes"] == ["in this work", "we propose"]


def _dossier_avis(tmp_path, avis, h9=H9, h10=H10, cibles=CIBLES):
    d = tmp_path / "cv"
    (d / "a-verifier").mkdir(parents=True)
    for nom, obj in (("h9", h9), ("h10", h10), ("cibles", cibles)):
        (d / "a-verifier" / f"{nom}.json").write_text(json.dumps(obj), encoding="utf-8")
    if avis is not None:
        (d / "avis.json").write_text(avis if isinstance(avis, str) else json.dumps(avis), encoding="utf-8")
    return d


def _cas_avis():
    t = copy.deepcopy(AVIS["targets"])
    t[0]["grounded"] = "yes"
    return {"sain": AVIS, "champ manquant": {k: v for k, v in AVIS.items() if k != "comment"},
            "type": _avec(AVIS, statement_leaks="no"), "valeur h10": _avec(AVIS, theory_experiment_expected="theory"),
            "incohérent h10": _avec(AVIS, theory_experiment_correct=False), "cibles": _avec(AVIS, targets=t[:3]),
            "fuite sans passage": _avec(AVIS, statement_leaks=True),
            "passage introuvable": _avec(AVIS, statement_leaks=True, leak_passages=["we use a transformer"]),
            "fuite": _avec(AVIS, statement_leaks=True, leak_passages=["route tokens to experts"]),
            "booléen": _avec(AVIS, targets=t), "commentaire à barre oblique": _avec(AVIS, comment="see \theta"),
            "objet": "[1]", "illisible": "{", "absent": None}


@pytest.mark.parametrize("nom", sorted(_cas_avis()))
def test_verifier_avis_memes_codes_que_le_module(tmp_path, nom):
    avis = _cas_avis()[nom]
    d = _dossier_avis(tmp_path, avis)
    if avis is None:
        module = ["[fichier.absent] avis.json absent"]
    else:
        try:
            module = ex.anomalies_avis(json.loads(avis) if isinstance(avis, str) else avis, H9, H10, CIBLES)
        except ValueError:
            module = ["[json.illisible] avis illisible"]
    code, lignes = _script("verifier-avis-v1.py", d)
    assert _codes_script(lignes) == sorted(ex.code_anomalie(a) for a in module), (lignes, module)
    assert (code == 0) == (not module)
    if nom in ("sain", "fuite"):
        assert module == []


def test_motifs_echec_avis():
    assert ex.motifs_echec_avis(AVIS, CIBLES, H10) == []
    assert ex.motifs_echec_avis(_avec(AVIS, statement_leaks=True, leak_passages=["x"]), CIBLES, H10) == [
        "énoncé qui révèle ce que H.9 interdit"]
    t = copy.deepcopy(AVIS["targets"])
    t[0]["observable"] = False
    assert any("moins de 3" in m for m in ex.motifs_echec_avis(_avec(AVIS, targets=t), CIBLES, H10))
    t = copy.deepcopy(AVIS["targets"])
    t[3]["grounded"] = False
    assert ex.motifs_echec_avis(_avec(AVIS, targets=t), CIBLES, H10) == ["aucune direction féconde fondée et observable"]
    # classification (CL-10) : un cran sans « theory_only » ne fait pas échouer ; theory_only ou deux crans, si
    voisin = _avec(AVIS, theory_experiment_correct=False, theory_experiment_expected="mostly_experiments")
    assert ex.motifs_echec_avis(voisin, CIBLES, H10) == []
    for attendu in ("theory_only", "mostly_theory"):
        loin = _avec(AVIS, theory_experiment_correct=False, theory_experiment_expected=attendu)
        assert ex.motifs_echec_avis(loin, CIBLES, H10) == ["theory_experiment faux au point de changer une décision"]


# --- statut d'un papier et listes de tâches ----------------------------------------------------------------------

V_OK = {"anomalies": [], "theory_only": False}
V_KO = {"anomalies": ["x"], "theory_only": False}
V_TH = {"anomalies": [], "theory_only": True}


def _v(role, motifs=(), tentative=1):
    return {"role": role, "tentative": tentative, "motifs": list(motifs)}


@pytest.mark.parametrize("validations, verdicts, attendu", [
    ({1: V_OK}, [], ("retenu", 1)),
    ({1: V_KO, 2: V_OK}, [], ("retenu", 2)),
    ({1: V_KO, 2: V_KO}, [], ("exclu", None)),
    ({1: V_TH}, [_v("theorie")], ("exclu", 1)),
    ({1: V_TH, 3: V_OK}, [_v("theorie", ["contesté"]), _v("reprise", tentative=3)], ("retenu", 3)),
    ({1: V_TH, 3: V_TH}, [_v("theorie", ["contesté"])], ("exclu", 3)),
    ({1: V_OK}, [_v("echantillon")], ("retenu", 1)),
    ({1: V_OK}, [_v("echantillon"), _v("audit")], ("retenu", 1)),
    ({1: V_OK, 3: V_OK}, [_v("echantillon"), _v("audit", ["fuite"]), _v("reprise", tentative=3)], ("retenu", 3)),
    ({1: V_OK, 3: V_OK}, [_v("echantillon", ["x"]), _v("reprise", tentative=3)], ("retenu", 3)),
    ({1: V_OK, 3: V_OK}, [_v("echantillon", ["x"]), _v("reprise", ["y"], tentative=3)], ("exclu", 3)),
    ({1: V_OK, 3: V_KO}, [_v("echantillon", ["x"])], ("exclu", None)),
    ({1: V_OK, 3: V_TH}, [_v("echantillon", ["x"])], ("exclu", 3)),
])
def test_statut_papier(validations, verdicts, attendu):
    s = ex.statut_papier("p", {k: {"p": v} for k, v in validations.items()}, verdicts)
    assert (s["statut"], s["tentative"]) == attendu


@pytest.mark.parametrize("validations, verdicts, motif", [
    ({}, [], "tentative 1 absente"),
    ({1: V_KO}, [], "non refait"),
    ({1: V_OK, 2: V_OK}, [], "tentative 2 sans motif"),
    ({1: V_KO, 2: V_KO, 3: V_OK}, [], "tentative 3 sans motif"),
    ({1: V_OK, 3: V_OK}, [], "reprise sans motif"),
    ({1: V_TH}, [], "non contre-vérifiée"),
    ({1: V_TH, 3: V_OK}, [_v("theorie")], "tentative 3 sans motif"),
    ({1: V_OK}, [_v("echantillon", ["x"])], "non repris"),
    ({1: V_OK, 3: V_OK}, [_v("echantillon", ["x"])], "reprise non contre-vérifiée"),
    ({1: V_OK}, [_v("echantillon"), _v("reprise", tentative=3)], "reprise sans motif"),
])
def test_statut_papier_procedure_non_suivie(validations, verdicts, motif):
    with pytest.raises(GardeArret, match=motif):
        ex.statut_papier("p", {k: {"p": v} for k, v in validations.items()}, verdicts)


def test_listes_de_taches_remplacement_dans_l_ordre():
    pilote, reserve = ["a", "b", "c"], ["r1", "r2", "r3", "r4"]
    st = {p: {"statut": "retenu"} for p in pilote + reserve}
    st["b"] = {"statut": "exclu"}
    st["r1"] = {"statut": "exclu"}
    listes = ex.listes_de_taches(pilote, reserve, st)
    assert listes["evaluation"] == ["a", "r2", "c"]
    assert listes["remplacements"] == [{"exclu": "b", "remplacant": "r2"}]
    assert listes["entrainement"] == ["r3", "r4"] and listes["entrainement_insuffisant"]
    with pytest.raises(GardeArret, match="statuts incomplets"):
        ex.listes_de_taches(pilote, reserve, {k: v for k, v in st.items() if k != "c"})
    st.update({r: {"statut": "exclu"} for r in reserve})
    with pytest.raises(GardeArret, match="tirage complémentaire"):
        ex.listes_de_taches(pilote, reserve, st)
    with pytest.raises(GardeArret, match="recoupent"):
        ex.listes_de_taches(["a"], ["a"], {"a": {"statut": "retenu"}})


def test_echantillon_reproductible_et_garde():
    g = graines(["t"], entropie=7)["t"]
    ordre = [f"p{i}" for i in range(30)]
    a, perm = ex.echantillon_contre_verification(ordre, g, set(ordre[::2]), n=5)
    b, _ = ex.echantillon_contre_verification(ordre, g, set(ordre[::2]), n=5)
    assert a == b and len(a) == 5 and set(a) <= set(ordre[::2]) and sorted(perm) == sorted(ordre)
    with pytest.raises(GardeArret, match="admissibles"):
        ex.echantillon_contre_verification(ordre, g, {"p0"}, n=5)


def test_intervalle_binomial_exact():
    assert et.intervalle_binomial(0, 16) == pytest.approx([0.0, 0.2059], abs=1e-3)
    assert et.intervalle_binomial(4, 16) == pytest.approx([0.0727, 0.5238], abs=1e-3)
    assert et.intervalle_binomial(16, 16)[1] == 1.0


def test_code_anomalie_exige_un_code():
    assert ex.code_anomalie("[h9.figure] x") == "h9.figure"
    with pytest.raises(GardeArret, match="sans code"):
        ex.code_anomalie("anomalie libre")


# --- déroulé complet dans un dépôt jetable -----------------------------------------------------------------------

def _depot_de_test(depot, n_pilote=3, n_reserve=3):
    """Dépôt jetable : procédure et fichiers scellés (copies des vrais), modules de décision (copies), invites H9 et
    H10 (vraies), corpus scellé rattaché à un manifeste, textes hors du suivi de git."""
    (depot / ".gitignore").write_text("donnees/\n")
    dp = depot / "docs" / "procedures" / "T0.5-extraction-v1"
    dp.mkdir(parents=True)
    for nom in et.FICHIERS_PROCEDURE.values():
        shutil.copyfile(PROC / nom, dp / nom)
        sceller(dp / nom)
    (depot / "docs" / "procedures" / "T0.5-extraction-v1.md").write_text("procédure de test\n")
    sceller(depot / "docs" / "procedures" / "T0.5-extraction-v1.md")
    for m in et.Chemins().modules:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RACINE / m, depot / m)
    shutil.copytree(RACINE / "docs" / "sources" / "invites-2606.08892-v1", depot / "invites")
    textes = depot / "donnees" / "textes"
    textes.mkdir(parents=True)
    fiches = []
    for k in range(n_pilote + n_reserve):
        pid = f"2601.{k:05d}"
        contenu = TEXTE.replace("routers", f"routers ({k})")
        (textes / f"{pid}v1.md").write_text(contenu, encoding="utf-8")
        fiches.append({"id": pid, "version": 1, "statut": "gardé", "rang_garde": k,
                       "texte_sha256": hashlib.sha256(contenu.encode()).hexdigest()})
    committer(depot)
    chemin_m, _ = creer_manifeste(depot, "20260101-000000-corpus", {"x": 1}, ["t"])
    ecrire_resultat(depot, chemin_m, "corpus", {"fiches": fiches})
    committer(depot)
    return et.Chemins(corpus="diag/20260101-000000-corpus/corpus.json", textes="donnees/textes",
                      invites=depot / "invites")


def _repondre(dossier, h9=H9, h10=H10, cibles=CIBLES):
    d = Path(dossier) / "sorties"
    for nom, obj in (("h9", h9), ("h10", h10), ("cibles", cibles)):
        (d / f"{nom}.json").write_text(json.dumps(obj), encoding="utf-8")


def _juger(dossier, avis=AVIS):
    (Path(dossier) / "avis.json").write_text(json.dumps(avis), encoding="utf-8")


def _retours(prep, lignes=None):
    lignes = lignes or {}
    return {p: {"derniere_ligne": lignes.get(p, "NOT OK: 1 error(s)"), "lancements": 1} for p in prep["papiers"]}


def _petit(monkeypatch, echantillon=2, seuil=1, audit=1):
    monkeypatch.setattr(et, "TAILLE_PILOTE", 3)
    monkeypatch.setattr(et, "TAILLE_RESERVE", 3)
    monkeypatch.setattr(et, "TAILLE_ECHANTILLON", echantillon)
    monkeypatch.setattr(et, "SEUIL_ECHECS", seuil)
    monkeypatch.setattr(et, "TAILLE_AUDIT", audit)


RUN = "20260102-000000-extraction"
FUITE = _avec(AVIS, statement_leaks=True, leak_passages=["route tokens to experts"])


def _jusqu_a_l_echantillon(depot, travail, ch, theorie=None):
    """Tentative 1 (le papier `theorie` classé « theory_only »), validation, échantillon."""
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h10=_avec(H10, theory_experiment="theory_only") if pid == theorie else H10)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    return prep, et.echantillonner(depot, RUN, ch=ch)


def test_deroule_complet(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    with pytest.raises(GardeArret, match="dans le dépôt"):
        et.preparer(depot, RUN, depot / "w", 1, ch=ch)
    assert not (depot / "runs" / RUN).exists()             # aucune garde ne brûle le run avant le manifeste
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    info = prep["papiers"][ids[0]]
    consigne = (Path(info["dossier"]) / "consigne.txt").read_text()
    assert info["dossier"] in consigne and "<<" not in consigne and "self-contained" in info["invite_agent"]
    assert (Path(info["dossier"]) / "invites" / "cibles.txt").read_bytes() == (PROC / "invite-cibles-v1.txt").read_bytes()
    # pilote 1 invalide (refait), pilote 2 « theory_only », le reste valide
    for pid in ids:
        if pid == ids[1]:
            _repondre(prep["papiers"][pid]["dossier"], h9=_avec(H9, research_questions="court"))
        elif pid == ids[2]:
            _repondre(prep["papiers"][pid]["dossier"], h10=_avec(H10, theory_experiment="theory_only"))
        else:
            _repondre(prep["papiers"][pid]["dossier"])
    with pytest.raises(GardeArret, match="retours des sous-agents incomplets"):
        et.valider(depot, RUN, 1, {}, ch=ch)
    v1 = et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    assert v1["invalides"] == [ids[1]] and v1["theory_only"] == [ids[2]]
    assert v1["papiers"][ids[1]]["anomalies"] == ["h9.enonce_court"]
    with pytest.raises(GardeArret, match="non refait"):
        et.echantillonner(depot, RUN, ch=ch)
    with pytest.raises(GardeArret, match="les papiers dus"):
        et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    p2 = et.preparer(depot, RUN, travail, 2, [ids[1]], ch=ch)
    _repondre(p2["papiers"][ids[1]]["dossier"])
    et.valider(depot, RUN, 2, _retours(p2, {ids[1]: OK_LIGNE}), ch=ch)
    ech = et.echantillonner(depot, RUN, ch=ch)
    assert len(ech["echantillon"]) == 2 and ech["theory_only"] == [ids[2]] and ids[2] not in ech["echantillon"]
    e0, e1 = ech["echantillon"]
    with pytest.raises(GardeArret, match="pas encore d'avis lisible"):
        et.preparer(depot, RUN, travail, 3, [e0], ch=ch)
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    th = et.preparer_contre_verification(depot, RUN, travail, "theorie", ch=ch)
    assert cv["ronde"] == 1 and th["ronde"] == 2 and sorted(th["papiers"]) == [ids[2]]
    _juger(cv["papiers"][e0]["dossier"], FUITE)
    _juger(cv["papiers"][e1]["dossier"])
    # l'avis « theorie » conteste « theory_only » (il attend « experiments_only ») : reprise due
    _juger(th["papiers"][ids[2]]["dossier"], _avec(AVIS, theory_experiment_correct=False))
    with pytest.raises(GardeArret, match="préparée et non lue"):
        et.assembler(depot, RUN, ch=ch)
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    assert lu["echecs"] == [e0] and lu["illisibles"] == []
    et.lire_contre_verification(depot, RUN, 2, _retours(th), ch=ch)
    dus = et.reprises_dues(depot, RUN)
    assert dus == sorted([e0, ids[2]])
    p3 = et.preparer(depot, RUN, travail, 3, dus, ch=ch)
    for pid in dus:
        _repondre(p3["papiers"][pid]["dossier"],
                  h10=_avec(H10, theory_experiment="theory_only") if pid == ids[2] else H10)
    et.valider(depot, RUN, 3, _retours(p3), ch=ch)
    rp = et.preparer_contre_verification(depot, RUN, travail, "reprise", ch=ch)
    assert sorted(rp["papiers"]) == [e0]                   # ids[2] redevenu « theory_only » : exclu, sans reprise
    _juger(rp["papiers"][e0]["dossier"])
    et.lire_contre_verification(depot, RUN, 3, _retours(rp), ch=ch)
    bilan = et.assembler(depot, RUN, ch=ch)
    assert bilan["exclus"] == {ids[2]: "theory_only (reprise)"}
    assert bilan["evaluation"] == [ids[0], ids[1], ids[3]]
    assert bilan["remplacements"] == [{"exclu": ids[2], "remplacant": ids[3]}]
    assert bilan["entrainement"] == [ids[4], ids[5]] and bilan["entrainement_insuffisant"]
    assert bilan["statuts"][e0]["tentative"] == 3 and bilan["audit"] is None
    assert bilan["taux_echec_echantillon"]["echecs"] == 1
    assert bilan["cibles_defectueuses_echantillon"] == {"defectueuses": 0, "controlees": 8}                # D-7
    assert set(bilan["classification_et_calcul"]) == {"echantillon", "reprise"}
    assert bilan["taches_assemblees"]["evaluation"]["base"] == {"reported": 3, "estimated": 0}     # par liste (E-11)
    assert bilan["taches_assemblees"]["entrainement"]["base"] == {"reported": 2, "estimated": 0}
    assert bilan["annonces_des_sous_agents"]["tentative-1"] == {"desaccords": 5, "hors_format": 0}   # « NOT OK » x 6
    assert bilan["annonces_des_sous_agents"]["tentative-2"] == {"desaccords": 0, "hors_format": 0}
    assert set(bilan["annonces_des_sous_agents"]) == {"tentative-1", "tentative-2", "tentative-3", "ronde-echantillon",
                                                      "ronde-theorie", "ronde-reprise"}
    taches = json.loads((depot / "donnees" / RUN / "taches-evaluation.json").read_text())["resultat"]["taches"]
    assert [t["identifiant"] for t in taches] == bilan["evaluation"] and all(t["questions"] for t in taches)
    # aucun texte des papiers dans diag/ (règle de sélection, section 9 ; nœud N-014)
    for f in (depot / "diag" / RUN).glob("*.json"):
        contenu = f.read_text()
        assert "route tokens to experts" not in contenu and "dense baseline" not in contenu, f.name
    assert (depot / "donnees" / RUN / "sorties-tentative-1.tar.sha256").is_file()
    with pytest.raises(GardeArret, match="R12"):
        et.assembler(depot, RUN, ch=ch)


def test_avis_illisible_refait_par_un_nouveau_sous_agent(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"])                    # e1 : aucun avis (panne)
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    assert lu["illisibles"] == [e1]
    with pytest.raises(GardeArret, match="nommer les papiers"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    with pytest.raises(GardeArret, match="hors des papiers sans avis"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e0], ch=ch)
    cv2 = et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e1], ch=ch)
    assert cv2["ronde"] == 2 and sorted(cv2["papiers"]) == [e1]
    _juger(cv2["papiers"][e1]["dossier"])
    et.lire_contre_verification(depot, RUN, 2, _retours(cv2), ch=ch)
    with pytest.raises(GardeArret, match="audit R4 requis"):    # tout est propre : l'audit est exigé
        et.assembler(depot, RUN, ch=ch)


def test_audit_cote_propre_et_reprise(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    for pid in ech["echantillon"]:
        _juger(cv["papiers"][pid]["dossier"])
    et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    with pytest.raises(GardeArret, match="audit"):
        et.reprises_dues(depot, RUN)
    au = et.preparer_contre_verification(depot, RUN, travail, "audit", ch=ch)
    assert sorted(au["papiers"]) == ech["echantillon"][:1]
    e0 = ech["echantillon"][0]
    _juger(au["papiers"][e0]["dossier"], FUITE)                 # l'audit trouve une fuite : reprise due
    et.lire_contre_verification(depot, RUN, 2, _retours(au), ch=ch)
    assert et.reprises_dues(depot, RUN) == [e0]
    p3 = et.preparer(depot, RUN, travail, 3, [e0], ch=ch)
    _repondre(p3["papiers"][e0]["dossier"])
    et.valider(depot, RUN, 3, _retours(p3), ch=ch)
    rp = et.preparer_contre_verification(depot, RUN, travail, "reprise", ch=ch)
    _juger(rp["papiers"][e0]["dossier"])
    et.lire_contre_verification(depot, RUN, 3, _retours(rp), ch=ch)
    bilan = et.assembler(depot, RUN, ch=ch)
    assert bilan["audit"]["echecs_audit"] == [e0] and "Lazar" in bilan["audit"]["reserve"]
    assert bilan["statuts"][e0]["tentative"] == 3


def test_seuil_d_echecs_arrete_a_la_lecture(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch, seuil=1, audit=2)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    for pid in ech["echantillon"]:
        _juger(cv["papiers"][pid]["dossier"], FUITE)
    with pytest.raises(GardeArret, match="version 2"):
        et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-seuil-contre-verification.json").read_text())["resultat"]
    assert arret["echecs"] == ech["echantillon"] and arret["audit"] == ech["echantillon"][:2]
    au = et.preparer_contre_verification(depot, RUN, travail, "audit", ch=ch)   # audit du côté sale, puis v2
    assert sorted(au["papiers"]) == sorted(ech["echantillon"][:2])
    with pytest.raises(GardeArret, match="non lue"):
        et.reprises_dues(depot, RUN)
    for pid in au["papiers"]:
        _juger(au["papiers"][pid]["dossier"])
    et.lire_contre_verification(depot, RUN, 2, _retours(au), ch=ch)
    accord = json.loads((depot / "diag" / RUN / "accord-audit-cote-sale.json").read_text())["resultat"]
    assert accord["cote"] == "sale" and accord["accord_echec"] == 0 and accord["echecs_audit"] == []   # D-6
    with pytest.raises(GardeArret, match="seuil"):
        et.reprises_dues(depot, RUN)
    with pytest.raises(GardeArret, match="seuil"):
        et.assembler(depot, RUN, ch=ch)


def test_entrees_modifiees_anomalie_du_seul_papier(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for info in prep["papiers"].values():
        _repondre(info["dossier"])
    (Path(prep["papiers"][ids[0]]["dossier"]) / "verifier_sortie.py").write_text("print('OK')\n")
    v = et.valider(depot, RUN, 1, _retours(prep, {ids[0]: OK_LIGNE}), ch=ch)
    assert v["invalides"] == [ids[0]] and v["papiers"][ids[0]]["anomalies"] == ["entrees.modifiees"]
    assert v["papiers"][ids[0]]["entrees_modifiees"] == ["verifier_sortie.py"]


def test_annonce_du_sous_agent_consignee_sans_arret(depot, tmp_path_factory, monkeypatch):
    """Contre-lecture 2, D-2 et D-13 : un « OK » rendu face à une anomalie n'arrête plus rien (il est consigné) ; une
    ligne hors forme est codée dans `diag/`, et sa forme brute ne va que dans `donnees/`."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for info in prep["papiers"].values():
        _repondre(info["dossier"], h9=_avec(H9, research_questions="court"))
    hors = "I could not find a third control: the dense baseline is the only one"
    v = et.valider(depot, RUN, 1, _retours(prep, {ids[0]: OK_LIGNE, ids[1]: hors}), ch=ch)
    assert v["invalides"] == ids
    assert v["papiers"][ids[0]]["retour"] == {"lancements": 1, "forme": "conforme", "annonce": "OK",
                                              "accord_avec_le_module": False}
    assert v["papiers"][ids[1]]["retour"]["forme"] == "retour.hors_format"
    assert v["papiers"][ids[2]]["retour"]["accord_avec_le_module"] is True
    assert hors not in (depot / "diag" / RUN / "validation-tentative-1.json").read_text()
    assert hors in (depot / "donnees" / RUN / "details-validation-tentative-1.json").read_text()


def test_desaccord_du_script_scelle_et_du_module_arrete(depot, tmp_path_factory, monkeypatch):
    """D-2 : le module exécute la copie scellée du script sur chaque dossier aux entrées intactes ; un écart de codes,
    dans un sens ou dans l'autre, est un désaccord en production et arrête (artefacts)."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h9=_avec(H9, research_questions="court") if pid == ids[0] else H9)
    vrai = et.codes_du_script
    assert vrai(depot / ch.dossier_procedure / "verifier-sortie-v1.py",
                Path(prep["papiers"][ids[0]]["dossier"])) == ["h9.enonce_court"]          # cas sain : le vrai script
    monkeypatch.setattr(et, "codes_du_script",                                             # artefact : il voit trop
                        lambda script, d: vrai(script, d) + ["cibles.bornes"])
    with pytest.raises(GardeArret, match="désaccord en production"):
        et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    # contre-lecture 3, E-8 : désaccord définitif, consigné par un arrêt scellé ; aucune étape ne suit
    arret = json.loads((depot / "diag" / RUN / "arret-desaccord-script.json").read_text())["resultat"]
    assert arret["etape"] == "validation-tentative-1" and arret["papier"] == ids[0]
    assert arret["codes_script"] == ["cibles.bornes", "h9.enonce_court"] and arret["codes_module"] == ["h9.enonce_court"]
    assert not (depot / "diag" / RUN / "validation-tentative-1.json").exists()
    monkeypatch.setattr(et, "codes_du_script", lambda script, d: [])                       # artefact : il ne voit rien
    with pytest.raises(GardeArret, match="run arrêté"):
        et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    with pytest.raises(GardeArret, match="désaccord en production"):
        et.exiger_accord_script(ids[0], [], ["h9.enonce_court"])
    et.exiger_accord_script(ids[0], ["h9.enonce_court", "cibles.bornes"], ["cibles.bornes", "h9.enonce_court"])


def test_script_hors_forme_arrete(tmp_path, monkeypatch):
    panne = tmp_path / "panne.py"
    panne.write_text("raise SystemExit(3)\n")
    with pytest.raises(GardeArret, match="hors forme"):
        et.codes_du_script(panne, tmp_path)
    muet = tmp_path / "muet.py"
    muet.write_text("print('fini')\n")
    with pytest.raises(GardeArret, match="hors forme"):
        et.codes_du_script(muet, tmp_path)
    lent = tmp_path / "lent.py"                    # contre-lecture 3, E-8 : un délai dépassé est une panne, pas une trace
    lent.write_text("import time\ntime.sleep(5)\nprint('OK: 0 error(s)')\n")
    monkeypatch.setattr(et, "DELAI_SCRIPT_S", 0.5)
    with pytest.raises(GardeArret, match="délai de 0.5 s dépassé"):
        et.codes_du_script(lent, tmp_path)


def test_exclusions_au_dela_du_seuil_arretent_apres_la_tentative_2(depot, tmp_path_factory, monkeypatch):
    """D-17 : au-delà du seuil de papiers invalides aux tentatives 1 et 2, arrêt scellé ; rien ne se tire ensuite."""
    _petit(monkeypatch)
    monkeypatch.setattr(et, "SEUIL_EXCLUSIONS_VALIDATION", 1)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    court = _avec(H9, research_questions="court")
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h9=court if pid in ids[:2] else H9)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    p2 = et.preparer(depot, RUN, travail, 2, ids[:2], ch=ch)
    for pid in ids[:2]:
        _repondre(p2["papiers"][pid]["dossier"], h9=court)
    with pytest.raises(GardeArret, match="seuil 1"):
        et.valider(depot, RUN, 2, _retours(p2), ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-exclusions-validation.json").read_text())["resultat"]
    assert arret["exclus"] == ids[:2] and arret["codes"] == {"h9.enonce_court": 2}
    with pytest.raises(GardeArret, match="rien ne se tire"):
        et.echantillonner(depot, RUN, ch=ch)


def test_avis_refaits_bornes(depot, tmp_path_factory, monkeypatch):
    """D-16 : un avis et deux avis refaits au plus par papier et par rôle (ici, borne abaissée à 2)."""
    _petit(monkeypatch)
    monkeypatch.setattr(et, "AVIS_MAX_PAR_ROLE", 2)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"])
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    assert lu["papiers"][e1]["codes"] == ["fichier.absent"]                  # mêmes codes que le script (D-11)
    cv2 = et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e1], ch=ch)
    (Path(cv2["papiers"][e1]["dossier"]) / "avis.json").write_text("{", encoding="utf-8")
    lu2 = et.lire_contre_verification(depot, RUN, 2, _retours(cv2), ch=ch)
    assert lu2["papiers"][e1]["codes"] == ["json.illisible"]
    with pytest.raises(GardeArret, match="2 avis « echantillon » préparés sans avis lisible"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e1], ch=ch)
    arret = json.loads((depot / "diag" / RUN / f"arret-avis-refaits-echantillon-{e1}.json").read_text())["resultat"]
    assert arret["papier"] == e1 and arret["role"] == "echantillon" and arret["avis_prepares"] == 2
    with pytest.raises(GardeArret, match="préparés sans avis lisible"):                               # répété, sans écrire
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e1], ch=ch)


def test_fichiers_epingles_et_ordre_des_rondes(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    with pytest.raises(GardeArret, match="première ronde"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", ech["echantillon"][:1], ch=ch)
    with pytest.raises(GardeArret, match="aucun papier"):
        et.preparer_contre_verification(depot, RUN, travail, "theorie", ch=ch)      # aucune exclusion à vérifier
    with pytest.raises(GardeArret, match="audit non requis"):
        et.preparer_contre_verification(depot, RUN, travail, "audit", ch=ch)
    module = depot / et.Chemins().modules[0]
    module.write_text(module.read_text() + "\n# changé\n")
    with pytest.raises(GardeArret, match="changés depuis l'ouverture"):
        et.echantillonner(depot, RUN, ch=ch)


# --- une épreuve par garde d'arrêt (contre-lecture de la procédure, CL-7 ; R5) ------------------------------------

def test_gardes_finales_de_la_copie_et_des_listes():
    ex.exiger_copie(["ab\n", "c"], "ab\nc", 10, 5)
    with pytest.raises(GardeArret, match="concaténation"):
        ex.exiger_copie(["ab\n", "x"], "ab\nc", 10, 5)
    with pytest.raises(GardeArret, match="hors bornes"):
        ex.exiger_copie(["ab\n", "c"], "ab\nc", 2, 5)
    ex.exiger_disjointes(["a"], ["b"])
    with pytest.raises(GardeArret, match="aussi une tâche d'évaluation"):
        ex.exiger_disjointes(["a", "b"], ["b"])


def test_gardes_des_fichiers_scelles_et_des_archives(depot, tmp_path):
    _depot_de_test(depot)
    chemin_m, _ = creer_manifeste(depot, RUN, {"x": 1}, ["t"])
    sha = et.ecrire_donnees(depot, RUN, "essai", {"a": 1})
    assert et.lire_donnees(depot, RUN, "essai", sha) == {"a": 1}
    with pytest.raises(GardeArret, match="empreinte différente"):
        et.lire_donnees(depot, RUN, "essai", "0" * 64)
    with pytest.raises(GardeArret, match="R12"):
        et.ecrire_donnees(depot, RUN, "essai", {"a": 2})
    assert et.ecrire_donnees(depot, RUN, "essai", {"a": 1}) == sha              # idempotent sur un contenu identique
    with pytest.raises(GardeArret, match="non encodable"):                         # substitut isolé (D-10)
        et.ecrire_donnees(depot, RUN, "substitut", {"a": "x\ud835"})
    assert not (depot / "donnees" / RUN / "substitut.json").exists()
    cible = tmp_path / "a.tar"
    sha_a = et.archiver(cible, [("x/y.json", b"{}")])
    assert et.lire_archive(cible, sha_a) == {"x/y.json": b"{}"}
    assert et.archiver(cible, [("x/y.json", b"{}")]) == sha_a                    # une étape interrompue se refait
    with pytest.raises(GardeArret, match="existe déjà avec un autre contenu"):
        et.archiver(cible, [("x/y.json", b"[]")])
    with pytest.raises(GardeArret, match="empreinte différente"):
        et.lire_archive(cible, "0" * 64)
    with pytest.raises(GardeArret, match="champ non rempli"):
        et._remplir("<<DOSSIER>> et <<AUTRE>>", tmp_path, [])
    et._exiger_retours({"p": {"derniere_ligne": "OK", "lancements": 1}}, ["p"])
    with pytest.raises(GardeArret, match="mal formé"):
        et._exiger_retours({"p": {"derniere_ligne": 3, "lancements": 1}}, ["p"])
    with pytest.raises(GardeArret, match="mal formé"):
        et._exiger_retours({"p": {"derniere_ligne": "OK", "lancements": 0}}, ["p"])
    with pytest.raises(GardeArret, match="mal formé"):                             # au plus deux relances (D-16)
        et._exiger_retours({"p": {"derniere_ligne": "OK", "lancements": 4}}, ["p"])
    with pytest.raises(GardeArret, match="mal formé"):                             # deux clés seulement (D-13)
        et._exiger_retours({"p": {"derniere_ligne": "OK", "lancements": 1, "note": "x"}}, ["p"])
    with pytest.raises(GardeArret, match="mal formé"):
        et._exiger_retours({"p": {"derniere_ligne": "OK", "lancements": True}}, ["p"])


def test_gardes_du_corpus(depot, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    assert len(et.papiers_du_corpus(depot, ch)) == 6
    monkeypatch.setattr(et, "TAILLE_RESERVE", 4)
    with pytest.raises(GardeArret, match="papiers gardés"):
        et.papiers_du_corpus(depot, ch)
    monkeypatch.setattr(et, "TAILLE_RESERVE", 3)
    p = et.papiers_du_corpus(depot, ch)[0]
    et.lire_texte(depot, ch, p)
    (depot / ch.textes / f"{p['id']}.md").write_text("altéré", encoding="utf-8")
    with pytest.raises(GardeArret, match="altéré"):
        et.lire_texte(depot, ch, p)


def test_gardes_de_preparation(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    with pytest.raises(GardeArret, match="96 papiers"):
        et.preparer(depot, RUN, travail, 1, ["x"], ch=ch)
    (travail / "tentative-1").mkdir()
    with pytest.raises(GardeArret, match="existe déjà"):
        et.preparer(depot, RUN, travail, 1, ch=ch)
    (travail / "tentative-1").rmdir()
    assert not (depot / "runs" / RUN).exists()
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h9=_avec(H9, research_questions="court") if pid == ids[0] else H9)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    autre = tmp_path_factory.mktemp("autre")
    with pytest.raises(GardeArret, match="dossier de travail différent"):
        et.preparer(depot, RUN, autre, 2, [ids[0]], ch=ch)
    with pytest.raises(GardeArret, match="1, 2 et 3"):
        et.preparer(depot, RUN, travail, 4, [ids[0]], ch=ch)
    p2 = et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    with pytest.raises(GardeArret, match="déjà préparée"):
        et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    with pytest.raises(GardeArret, match="préparée et non validée"):
        et.echantillonner(depot, RUN, ch=ch)
    _repondre(p2["papiers"][ids[0]]["dossier"])
    et.valider(depot, RUN, 2, _retours(p2), ch=ch)
    et.echantillonner(depot, RUN, ch=ch)


def test_gardes_de_contre_verification(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    with pytest.raises(GardeArret, match="inconnu"):
        et.preparer_contre_verification(depot, RUN, travail, "jury", ch=ch)
    with pytest.raises(GardeArret, match="dossier de travail différent"):
        et.preparer_contre_verification(depot, RUN, tmp_path_factory.mktemp("autre"), "echantillon", ch=ch)
    with pytest.raises(GardeArret, match="tentative 3 non validée"):
        et.preparer_contre_verification(depot, RUN, travail, "reprise", ch=ch)
    (travail / "contre-verification-1").mkdir()
    with pytest.raises(GardeArret, match="existe déjà"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    (travail / "contre-verification-1").rmdir()
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    with pytest.raises(GardeArret, match="non lue"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", [e1], ch=ch)
    _juger(cv["papiers"][e0]["dossier"])
    _juger(cv["papiers"][e1]["dossier"], _avec(AVIS, statement_leaks="oui"))   # avis mal formé
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv, {e1: "OK: 0 error(s)"}), ch=ch)
    assert lu["illisibles"] == [e1] and lu["papiers"][e1]["retour"]["accord_avec_le_module"] is False
    with pytest.raises(GardeArret, match="pas d'avis lisible"):
        et.assembler(depot, RUN, ch=ch)


def test_desaccord_a_la_lecture_d_une_ronde_arret_scelle(depot, tmp_path_factory, monkeypatch):
    """D-2 et E-8 : à la lecture d'une ronde aussi, un désaccord du script scellé et du module arrête, consigné."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"])
    _juger(cv["papiers"][e1]["dossier"], _avec(AVIS, statement_leaks="oui"))   # avis mal formé
    monkeypatch.setattr(et, "codes_du_script", lambda script, d: [])            # artefact : le script ne voit rien
    with pytest.raises(GardeArret, match="désaccord en production"):
        et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-desaccord-script.json").read_text())["resultat"]
    assert arret["etape"] == "contre-verification-ronde-1" and arret["papier"] == e1 and arret["codes_script"] == []
    assert not (depot / "diag" / RUN / "contre-verification-ronde-1.json").exists()


def test_garde_d_une_ronde_lue_sans_preparation(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _jusqu_a_l_echantillon(depot, travail, ch)
    ecrire_resultat(depot, depot / "runs" / RUN / "manifeste.json", "contre-verification-ronde-1", {"x": 1})
    with pytest.raises(GardeArret, match="lue sans préparation"):
        et._rondes(depot, RUN)


def test_garde_d_une_archive_rescellee_et_echantillon_tardif(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    # une archive modifiée puis scellée de nouveau est une perte (E-2, test dédié) ; ici, l'archive reste intacte sur
    # disque et sa lecture est altérée : l'empreinte validée de chaque sortie arrête quand même (défense en profondeur)
    lire = et.lire_archive

    def alteree(chemin, attendu):
        return {n: o.replace(b"route", b"ROUTE") for n, o in lire(chemin, attendu).items()}

    monkeypatch.setattr(et, "lire_archive", alteree)
    with pytest.raises(GardeArret, match="≠ empreinte validée"):
        et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)


def test_echantillon_apres_une_tentative_3_refuse(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"], FUITE)
    _juger(cv["papiers"][e1]["dossier"])
    et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    p3 = et.preparer(depot, RUN, travail, 3, [e0], ch=ch)
    _repondre(p3["papiers"][e0]["dossier"])
    et.valider(depot, RUN, 3, _retours(p3), ch=ch)
    with pytest.raises(GardeArret, match="après une tentative 3"):
        et.echantillonner(depot, RUN, ch=ch)


def test_garde_de_l_assemblage_sur_une_archive_rescellee(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"], FUITE)
    _juger(cv["papiers"][e1]["dossier"])
    et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    p3 = et.preparer(depot, RUN, travail, 3, [e0], ch=ch)
    _repondre(p3["papiers"][e0]["dossier"])
    et.valider(depot, RUN, 3, _retours(p3), ch=ch)
    rp = et.preparer_contre_verification(depot, RUN, travail, "reprise", ch=ch)
    _juger(rp["papiers"][e0]["dossier"])
    et.lire_contre_verification(depot, RUN, 2, _retours(rp), ch=ch)
    lire = et.lire_archive

    def rescellee(chemin, attendu):   # archive de la tentative 1 modifiée puis scellée de nouveau
        membres = lire(chemin, attendu)
        return {n: (o.replace(b"route", b"ROUTE") if "tentative-1/" in n else o) for n, o in membres.items()}

    monkeypatch.setattr(et, "lire_archive", rescellee)
    with pytest.raises(GardeArret, match="≠ empreinte validée"):
        et.assembler(depot, RUN, ch=ch)


def test_sortie_modifiee_pendant_la_validation_arrete(depot, tmp_path_factory, monkeypatch):
    """D-10 : on archive les octets mêmes qui ont été empreintés ; un fichier qui change entre la lecture et l'archive
    arrête (artefact : empreinte de lecture altérée)."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    for info in prep["papiers"].values():
        _repondre(info["dossier"])
    vraie = ex.lire_sorties

    def lecture_decalee(dossier, texte):
        r = vraie(dossier, texte)
        r["empreintes"]["h9"] = "0" * 64
        return r
    monkeypatch.setattr(et.ex, "lire_sorties", lecture_decalee)
    with pytest.raises(GardeArret, match="modifié pendant la validation"):
        et.valider(depot, RUN, 1, _retours(prep), ch=ch)


# --- contre-lecture 3 : remarques E-1 à E-11 -----------------------------------------------------------------------

def test_formule_sur_deux_lignes_faux_positif_documente(tmp_path):
    """E-3 : pandoc garde les sauts de ligne du source dans les formules ; une citation fidèle d'une telle formule est
    refusée (faux positif déclaré), la même avec une espace est acceptée ; le module et le script s'accordent, et le
    message dit de remplacer ce saut par une espace."""
    texte = TEXTE + "The loss is $a +\nb = c$ for all inputs of the router.\n"
    for citation, attendus in (("The loss is $a +\nb = c$ for all inputs", ["texte.formule"]),
                               ("The loss is $a + b = c$ for all inputs", [])):
        c = copy.deepcopy(CIBLES)
        c["controls"][2]["evidence"] = citation
        d = _dossier_sorties(tmp_path / str(len(attendus)), texte, H9, H10, c)
        module = ex.lire_sorties(d / "sorties", texte)
        assert sorted(ex.code_anomalie(a) for a in module["anomalies"]) == attendus
        _, lignes = _script("verifier-sortie-v1.py", d)
        assert _codes_script(lignes) == attendus
        if attendus:
            assert "replace this line break with a space" in " ".join(lignes)
            assert "remplacer ce saut de ligne par une espace" in module["anomalies"][0]


def test_substitut_dans_un_message_ne_bloque_que_son_papier(depot, tmp_path_factory, monkeypatch):
    """E-6 : un identifiant ou une référence de coût qui portent un substitut isolé restent des anomalies de leur
    papier : les messages les écrivent échappés, les détails restent encodables, la validation va au bout."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["id"] = "C\ud835"
    c["controls"][0]["evidence"] = "court"
    c["compute"]["reference_gpu_hours"] = "x\ud835"
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], cibles=c if pid == ids[0] else CIBLES)
    v = et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    assert v["invalides"] == [ids[0]]
    assert sorted(v["papiers"][ids[0]]["anomalies"]) == ["cibles.calcul_valeur", "cibles.citation_courte",
                                                         "texte.substitut"]


def test_fichier_ajoute_sous_papier_anomalie_du_seul_papier(depot, tmp_path_factory, monkeypatch):
    """E-7 : un fichier ajouté parmi les entrées (ici sous `papier/`) est une entrée modifiée de son papier, sans
    désaccord ni arrêt ; un fichier ajouté hors des entrées (une note à la racine du dossier) ne change rien."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["evidence"] = "A sentence that only the added file contains, for a citation."
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], cibles=c if pid == ids[0] else CIBLES)
    (Path(prep["papiers"][ids[0]]["dossier"]) / "papier" / "partie-01-notes.md").write_text(
        c["controls"][0]["evidence"], encoding="utf-8")
    (Path(prep["papiers"][ids[1]]["dossier"]) / "notes.txt").write_text("brouillon", encoding="utf-8")
    v = et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    assert v["invalides"] == [ids[0]]                    # le module ne lit pas le fichier ajouté : pas de désaccord
    assert v["papiers"][ids[0]]["anomalies"] == ["cibles.citation_introuvable", "entrees.modifiees"]
    assert v["papiers"][ids[0]]["entrees_modifiees"] == ["papier/partie-01-notes.md"]
    assert v["papiers"][ids[1]]["anomalies"] == []


@pytest.mark.parametrize("alteration", ["supprime", "tronque", "famille retiree", "liste"])
def test_entree_a_verifier_modifiee_avis_illisible_sans_exception(depot, tmp_path_factory, monkeypatch, alteration):
    """E-1 : un contre-vérificateur qui modifie une réponse à vérifier rend son avis illisible (entrée modifiée) ; la
    ronde se lit, l'autre papier reste lisible ; aucune exception hors garde."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    for pid in (e0, e1):
        _juger(cv["papiers"][pid]["dossier"])
    a = Path(cv["papiers"][e0]["dossier"]) / "a-verifier"
    if alteration == "supprime":
        (a / "cibles.json").unlink()
    elif alteration == "tronque":
        (a / "cibles.json").write_text("{", encoding="utf-8")
    elif alteration == "famille retiree":
        c = copy.deepcopy(CIBLES)
        del c["sterile_directions"]
        (a / "cibles.json").write_text(json.dumps(c), encoding="utf-8")
    else:
        (a / "h9.json").write_text("[1, 2]", encoding="utf-8")
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    assert lu["illisibles"] == [e0] and lu["papiers"][e0]["codes"] == ["entrees.modifiees"]
    assert lu["papiers"][e1]["lisible"]


def test_perte_de_donnees_arret_scelle_a_l_etape_suivante(depot, tmp_path_factory, monkeypatch):
    """E-2 : une archive de `donnees/<run>/` perdue après la validation 1 est vue dès l'étape suivante (ici la
    préparation de la tentative 2) : `arret-perte` scellé, puis aucune étape ne suit (cas sain : rien de perdu)."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h9=_avec(H9, research_questions="court") if pid == ids[0] else H9)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    et.exiger_rien_de_perdu(depot, RUN, "essai")                                  # cas sain
    assert sorted(et.fichiers_consignes(depot, RUN)) == ["details-validation-tentative-1.json",
                                                         "sorties-tentative-1.tar"]
    (depot / "donnees" / RUN / "sorties-tentative-1.tar").unlink()                 # artefact : perte
    with pytest.raises(GardeArret, match="perte de données"):
        et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-perte.json").read_text())["resultat"]
    assert arret["etape"] == "preparation-tentative-2"
    assert arret["fichiers_en_cause"] == [f"donnees/{RUN}/sorties-tentative-1.tar"]
    assert not (travail / "tentative-2").exists()
    with pytest.raises(GardeArret, match="run arrêté"):
        et.echantillonner(depot, RUN, ch=ch)


def test_perte_par_fichier_rescelle_ou_dossier_de_travail_disparu(depot, tmp_path_factory, monkeypatch):
    """E-2 : un fichier de `donnees/` modifié puis scellé de nouveau, ou le dossier de travail d'une préparation non lue
    disparu, sont des pertes ; un seul dossier de papier disparu reste une entrée modifiée de ce papier."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    for info in prep["papiers"].values():
        _repondre(info["dossier"])
    shutil.rmtree(prep["papiers"][ids[0]]["dossier"])                              # un dossier de papier : anomalie
    v = et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    assert v["papiers"][ids[0]]["anomalies"][-1] == "entrees.modifiees" and v["invalides"] == [ids[0]]
    details = depot / "donnees" / RUN / "details-validation-tentative-1.json"
    details.write_text(details.read_text() + " ")
    (details.parent / (details.name + ".sha256")).unlink()
    sceller(details)                                                               # artefact : rescellé
    with pytest.raises(GardeArret, match="perte de données"):
        et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    assert json.loads((depot / "diag" / RUN / "arret-perte.json").read_text())["resultat"]["fichiers_en_cause"] == [
        f"donnees/{RUN}/details-validation-tentative-1.json"]


def test_dossier_de_travail_perdu_avant_la_validation(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    shutil.rmtree(prep["travail"])                                                 # artefact : dossier perdu
    with pytest.raises(GardeArret, match="perte de données"):
        et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-perte.json").read_text())["resultat"]
    assert arret["etape"] == "validation-tentative-1" and arret["fichiers_en_cause"] == [prep["travail"]]
    assert not (depot / "diag" / RUN / "validation-tentative-1.json").exists()


def test_fichier_de_retours_dans_donnees_seulement(depot, tmp_path_factory, monkeypatch, capsys):
    """E-10 : la ligne de commande ne lit un fichier de retours que dans `donnees/<run>/` (cas sain et artefacts)."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    for info in prep["papiers"].values():
        _repondre(info["dossier"])
    contenu = json.dumps(_retours(prep))
    for chemin in (depot / "retours.json", depot / "runs" / RUN / "retours.json", travail / "retours.json"):
        chemin.write_text(contenu)
        with pytest.raises(GardeArret, match="hors de donnees"):
            et._retours(depot, RUN, str(chemin))
    bon = depot / "donnees" / RUN / "retours-tentative-1.json"
    bon.parent.mkdir(parents=True, exist_ok=True)
    bon.write_text(contenu)
    assert et._retours(depot, RUN, str(bon)) == _retours(prep)


# --- vérification courte des corrections de la contre-lecture 3 : V-1 à V-13 ----------------------------------------

def _t1(depot, monkeypatch, tmp_path_factory):
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    for info in prep["papiers"].values():
        _repondre(info["dossier"])
    return ch, travail, prep, sorted(prep["papiers"])


@pytest.mark.parametrize("objet", ["nom non utf-8", "dossier vide", "lien cassé", "tube nommé"])
def test_chemin_ajoute_sous_papier_anomalie_du_seul_papier(depot, tmp_path_factory, monkeypatch, objet):
    """V-1, V-2 : tout chemin ajouté parmi les entrées (fichier au nom non UTF-8, dossier, lien cassé, tube) est une
    entrée modifiée de son papier ; les résultats restent encodables et scellés."""
    import os
    ch, travail, prep, ids = _t1(depot, monkeypatch, tmp_path_factory)
    papier = Path(prep["papiers"][ids[0]]["dossier"]) / "papier"
    cible = papier / "partie-99.md"
    if objet == "nom non utf-8":
        os.close(os.open(os.fsencode(str(papier)) + b"/notes-\xff.md", os.O_CREAT | os.O_WRONLY))
    elif objet == "dossier vide":
        cible.mkdir()
    elif objet == "lien cassé":
        cible.symlink_to(papier / "absent.md")
    else:
        os.mkfifo(cible)
    v = et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    assert v["invalides"] == [ids[0]] and v["papiers"][ids[0]]["anomalies"] == ["entrees.modifiees"]
    attendu = "papier/notes-\\xff.md" if objet == "nom non utf-8" else "papier/partie-99.md"
    assert v["papiers"][ids[0]]["entrees_modifiees"] == [attendu]
    assert et.verifier(depot / "diag" / RUN / "validation-tentative-1.json")


def test_cible_textuelle_avec_substitut_avis_illisible(depot, tmp_path_factory, monkeypatch):
    """V-3 : le message `avis.cible` est échappé ; un substitut isolé n'arrête pas la lecture de la ronde."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    _, ech = _jusqu_a_l_echantillon(depot, travail, ch)
    e0, e1 = ech["echantillon"]
    cv = et.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    _juger(cv["papiers"][e0]["dossier"], _avec(AVIS, targets=["C1\ud835", "C2", "C3", "F1"]))
    _juger(cv["papiers"][e1]["dossier"])
    lu = et.lire_contre_verification(depot, RUN, 1, _retours(cv), ch=ch)
    assert lu["illisibles"] == [e0] and lu["papiers"][e1]["lisible"]


def test_autre_copie_du_depot_refusee_sans_rien_ecrire(depot, tmp_path_factory, monkeypatch):
    """V-4 : une étape lancée depuis une autre copie du dépôt (arbre de travail git, sans `donnees/`) est refusée sans
    rien écrire ; la même racine écrite autrement est acceptée."""
    ch, travail, prep, ids = _t1(depot, monkeypatch, tmp_path_factory)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    committer(depot)
    autre = tmp_path_factory.mktemp("autre") / "arbre"
    subprocess.run(["git", "-C", str(depot), "worktree", "add", "-q", str(autre)], check=True, capture_output=True)
    with pytest.raises(GardeArret, match="hors de la racine du run"):
        et.echantillonner(autre, RUN, ch=ch)
    assert not (autre / "diag" / RUN / "arret-perte.json").exists()
    monkeypatch.chdir(depot)
    et.echantillonner(Path("."), RUN, ch=ch)


def test_compagnon_illisible_est_une_perte_et_controle_a_la_demande(depot, tmp_path_factory, monkeypatch, capsys):
    """V-7 : une empreinte compagnon illisible est une perte (arrêt scellé) ; V-10 : la commande `controler` rejoue la
    règle de perte (cas sain : elle liste les fichiers consignés, sans rien écrire)."""
    ch, travail, prep, ids = _t1(depot, monkeypatch, tmp_path_factory)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    monkeypatch.chdir(depot)
    monkeypatch.setattr(et, "Chemins", lambda: ch)
    assert et._main(["controler", "--run-id", RUN]) == 0
    assert "sorties-tentative-1.tar" in capsys.readouterr().out
    (depot / "donnees" / RUN / "sorties-tentative-1.tar.sha256").write_bytes(b"\xff\n")
    with pytest.raises(GardeArret, match="perte de données"):
        et.echantillonner(depot, RUN, ch=ch)
    assert json.loads((depot / "diag" / RUN / "arret-perte.json").read_text())["resultat"]["fichiers_en_cause"] == [
        f"donnees/{RUN}/sorties-tentative-1.tar"]


def test_seuil_d17_relu_depuis_la_validation_2(depot, tmp_path_factory, monkeypatch):
    """V-13 : si l'arrêt d'exclusions n'a pas été écrit (étape interrompue), l'échantillon ne se tire pas pour autant."""
    _petit(monkeypatch)
    ch = _depot_de_test(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = et.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    court = _avec(H9, research_questions="court")
    for pid, info in prep["papiers"].items():
        _repondre(info["dossier"], h9=court if pid in ids[:2] else H9)
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    p2 = et.preparer(depot, RUN, travail, 2, ids[:2], ch=ch)
    for pid in ids[:2]:
        _repondre(p2["papiers"][pid]["dossier"], h9=court)
    et.valider(depot, RUN, 2, _retours(p2), ch=ch)                     # seuil 16 : pas d'arrêt écrit
    monkeypatch.setattr(et, "SEUIL_EXCLUSIONS_VALIDATION", 1)          # artefact : l'arrêt aurait dû être écrit
    assert not (depot / "diag" / RUN / "arret-exclusions-validation.json").exists()
    with pytest.raises(GardeArret, match="rien ne se tire"):
        et.echantillonner(depot, RUN, ch=ch)


def test_preparation_interrompue_mise_de_cote_puis_refaite(depot, tmp_path_factory, monkeypatch):
    """V-13 : une préparation de tentative 2 interrompue avant son résultat laisse un dossier ; il est mis de côté (pas
    détruit), et la préparation se refait."""
    ch, travail, prep, ids = _t1(depot, monkeypatch, tmp_path_factory)
    _repondre(prep["papiers"][ids[0]]["dossier"], h9=_avec(H9, research_questions="court"))
    et.valider(depot, RUN, 1, _retours(prep), ch=ch)
    (travail / "tentative-2" / "reste").mkdir(parents=True)
    p2 = et.preparer(depot, RUN, travail, 2, [ids[0]], ch=ch)
    assert (travail / "tentative-2-interrompue-1" / "reste").is_dir() and sorted(p2["papiers"]) == [ids[0]]
