# [v2 : copie de test_t06_cibles_invisibles_v1.py avec le lanceur v5 en plus (E3 du 7 novembre). Ajout en place (chaîne v13, épreuve exploratoire du 8 novembre, branche prep/t06-explo-v2) : le lanceur v6 joué à marqueur comme le v5, et la preuve par l'arbre syntaxique que la seule lecture de la clé `cibles` des six lanceurs est celle de l'adaptateur ; fichier modifié en place parce que la liste figée v3 le nomme]
"""Cibles invisibles de T0.6 (N-060 ; R-1679 de la session mère) : essai à marqueur sur les chemins du lanceur de T0.6 (versions 1 à 4, répétition jouet
par la commande). Chaque tâche d'évaluation ET de distillation porte un marqueur unique dans tous les champs de ses cibles (`cibles`) et de ses coûts
rapportés (`couts_rapportes`) ; sont interceptés, avant tout modèle, tout ce qui part vers le modèle ou vers un moniteur (`FormatBrut.ouverture` et
`FormatChat.ouverture`, `charger_invite`, `conversation_de_controle`) ; sont lus ensuite tous les fichiers texte écrits par le run (résultats, données
légères, textes d'actions) et les sorties standard et d'erreur. Le marqueur ne doit figurer nulle part. Garde éprouvée (R5) : la même collecte sur des
tâches dont l'énoncé recopie les cibles doit trouver le marqueur (la collecte voit bien les invites).
La clé `cibles` de la configuration d'un adaptateur (`config["adaptateur"]["cibles"]`, modules de LoRA visés) n'a rien à voir avec les cibles cachées
des tâches : `test_cles_cibles_de_la_configuration_sont_des_modules_de_lora` le montre."""
from __future__ import annotations

import ast
import json
import re
import shutil
from pathlib import Path

import pytest
from conftest import committer

from controle_ia.harnais import formats
from controle_ia.scellement import sceller
from controle_ia.t06 import lanceur as la1
from controle_ia.t06 import lanceur_v2 as la2
from controle_ia.t06 import lanceur_v3 as la3
from controle_ia.t06 import lanceur_v4 as la4
from controle_ia.t06 import lanceur_v5 as la5
from controle_ia.t06 import lanceur_v6 as la6

RACINE = Path(__file__).resolve().parents[1]
NOTES = RACINE / "docs" / "notes" / "g0-deux-semaines-v1"
MARQUEUR = "qz7f3a9c"
NOMBRES_MARQUES = ("987654.321", "7654321")          # champs numériques marqués (R-1683) : heures de GPU de référence et coûts rapportés
ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?",
           "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?"]
VERSIONS = [("v1", la1, "config-t06-jouet-v2.json"), ("v2", la2, "config-t06-jouet-v3.json"), ("v3", la3, "config-t06-jouet-v4.json"),
            ("v4", la4, "config-t06-jouet-v5.json"), ("v5", la5, "config-t06-jouet-v5.json"),       # v2 : lanceur_v5, que joue l'amorce v9
            ("v6", la6, "config-t06-jouet-v5.json")]       # chaîne v13 : lanceur_v6, que joue l'amorce v11 (même configuration jouet que le v5 : le calcul ne change pas)


def _m(champ: str) -> str:
    return f"QZ7F3A9C-{champ}"


def _fuit(texte) -> bool:
    if not isinstance(texte, str):
        texte = json.dumps(texte, ensure_ascii=False, default=str)
    compact = re.sub(r"\s+", "", texte).casefold()
    return MARQUEUR in compact or any(n in compact for n in NOMBRES_MARQUES)


def _tache(ident: str, k: int, fuite: bool) -> dict:
    cibles = {"compute": {"reference_gpu_hours": 987654.321, "evidence": _m("compute-evidence")},
              "controls": [{"id": _m(f"ctl-id-{j}"), "description": _m(f"ctl-desc-{j}")} for j in range(3)],
              "fruitful_directions": [{"id": _m("fr-id"), "description": _m("fr-desc")}],
              "sterile_directions": [{"id": _m("st-id"), "description": _m("st-desc")}]}
    questions = ENONCES[k % len(ENONCES)] + f" ({ident})"
    if fuite:
        questions += "\n" + json.dumps(cibles)
    return {"identifiant": ident, "questions": questions, "cibles": cibles, "couts_rapportes": [{"item": _m("couts"), "gpu_hours": 7654321}]}


def _preparer(depot: Path, config_jouet: str, fuite: bool) -> dict:
    (depot / "prereg").mkdir(exist_ok=True)
    for nom in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
        shutil.copy(RACINE / "prereg" / nom, depot / "prereg" / nom)
    d = depot / "donnees" / "t06-jouet"
    d.mkdir(parents=True)
    # Six tâches d'évaluation (trois par pli), pas quatre : le modèle jouet par caractères, à température 1, tire un jeton de fin
    # en premier jeton d'une action avec une probabilité d'environ 1,6 % par (tâche, pas), le même dans toutes les conditions
    # et phases (générateur par tâche, mêmes graines) ; avec T = 2 et deux tâches par pli, une tâche sans aucune action notée
    # (probabilité d'environ 1/1000 par run, entropie neuve à chaque run jouet) laissait un pli à une seule tâche et la garde
    # du rééchantillonnage arrêtait le run (épreuve exploratoire du 8 novembre, [v1]). Avec trois tâches par pli, il en
    # faudrait deux mortes dans le même pli (probabilité de l'ordre de 1e-6). La garde est inchangée.
    for nom, ids in (("taches-evaluation.json", ["e1", "e2", "e3", "e4", "e5", "e6"]), ("taches-distillation.json", ["d1", "d2"])):
        (d / nom).write_text(json.dumps({"taches": [_tache(i, k, fuite) for k, i in enumerate(ids)]}, ensure_ascii=False), encoding="utf-8")
    config = json.loads((NOTES / config_jouet).read_text(encoding="utf-8"))
    config["taches_evaluation"]["sha256"] = sceller(d / "taches-evaluation.json")
    config["taches_distillation"]["sha256"] = sceller(d / "taches-distillation.json")
    if "egalite_jetons_reels" in config:
        config["egalite_jetons_reels"] = False
    (depot / "config.json").write_text(json.dumps(config, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    sceller(depot / "config.json")
    for x in ("runs", "diag"):
        (depot / x).mkdir(exist_ok=True)
    committer(depot)
    return config


def _fichiers_texte(depot: Path) -> list[tuple[str, str]]:
    """Tous les fichiers texte écrits par le run (résultats, données légères, textes d'actions), hors les tâches d'entrée."""
    fichiers = []
    for dossier in ("diag", "donnees", "runs"):
        for f in sorted((depot / dossier).rglob("*")):
            if f.is_file() and f.suffix in (".json", ".jsonl", ".txt", ".md", ".sha256") and not (dossier == "donnees" and f.name.startswith("taches-")):
                fichiers.append((str(f.relative_to(depot)), f.read_text(encoding="utf-8", errors="replace")))
    return fichiers


def _collecter(depot, capfd, monkeypatch, module, config_jouet: str, fuite: bool) -> dict:
    """Run jouet par la commande ; rend les textes envoyés au modèle (invites), les fichiers texte écrits et les sorties."""
    _preparer(depot, config_jouet, fuite)
    vus: list[str] = []

    def espion_ouverture(original):
        def f(self, consigne, observation):
            vus.extend([str(consigne), str(observation)])
            return original(self, consigne, observation)
        return f

    for classe in (formats.FormatBrut, formats.FormatChat):
        monkeypatch.setattr(classe, "ouverture", espion_ouverture(classe.ouverture))
    for nom in ("charger_invite", "conversation_de_controle"):
        original = getattr(module, nom)

        def espion(*a, _o=original, **k):
            r = _o(*a, **k)
            vus.append(json.dumps(r, ensure_ascii=False, default=str))
            return r
        monkeypatch.setattr(module, nom, espion)
    monkeypatch.chdir(depot)
    assert module._main(["--config", "config.json", "--run-id", "20261107-120000-t06-jouet"]) == 0
    sortie, erreur = capfd.readouterr()
    return {"invites": vus, "fichiers": _fichiers_texte(depot), "sortie": sortie + "\n" + erreur}


@pytest.mark.parametrize("version, module, config_jouet", VERSIONS, ids=[v[0] for v in VERSIONS])
def test_aucune_invite_ni_aucun_resultat_ne_porte_les_cibles(depot, capfd, monkeypatch, version, module, config_jouet):
    r = _collecter(depot, capfd, monkeypatch, module, config_jouet, fuite=False)
    assert len(r["invites"]) > 20 and all(x.strip() for x in r["invites"])
    assert not [k for k, x in enumerate(r["invites"]) if _fuit(x)], f"{version} : le marqueur des cibles figure dans une invite"
    assert r["fichiers"] and not [n for n, t in r["fichiers"] if _fuit(t)], f"{version} : le marqueur figure dans un fichier écrit"
    assert not _fuit(r["sortie"])


@pytest.mark.parametrize("version, module, config_jouet", VERSIONS, ids=[v[0] for v in VERSIONS])
def test_garde_la_collecte_voit_une_fuite_plantee(depot, capfd, monkeypatch, version, module, config_jouet):
    """Artefact (R5) : l'énoncé recopie les cibles ; la collecte trouve le marqueur dans les invites ET dans les fichiers écrits."""
    r = _collecter(depot, capfd, monkeypatch, module, config_jouet, fuite=True)
    assert any(_fuit(x) for x in r["invites"]), "la collecte ne voit pas les invites"
    assert any(_fuit(x) and MARQUEUR not in x.casefold() for x in r["invites"]) or any(n in re.sub(r"\s+", "", x) for x in r["invites"] for n in NOMBRES_MARQUES), "les champs numériques ne sont pas vus"


def test_garde_le_balayage_des_fichiers_voit_un_marqueur_plante(tmp_path):
    """Artefact (R5) : un fichier de résultat qui recopierait une cible est trouvé par le balayage des fichiers écrits."""
    (tmp_path / "diag" / "run").mkdir(parents=True)
    (tmp_path / "diag" / "run" / "resultat.json").write_text(json.dumps({"x": _m("ctl-id-0")}), encoding="utf-8")
    (tmp_path / "donnees").mkdir()
    (tmp_path / "runs").mkdir()
    assert [n for n, t in _fichiers_texte(tmp_path) if _fuit(t)] == ["diag/run/resultat.json"]
    (tmp_path / "diag" / "run" / "resultat.json").write_text(json.dumps({"x": "propre"}), encoding="utf-8")
    assert not [n for n, t in _fichiers_texte(tmp_path) if _fuit(t)]


def test_cles_cibles_de_la_configuration_sont_des_modules_de_lora():
    """Les six « lecteurs » de la clé `cibles` des modules de T0.6 lisent la configuration de l'adaptateur (modules de LoRA), jamais une tâche."""
    for _, _, config_jouet in VERSIONS:
        a = json.loads((NOTES / config_jouet).read_text(encoding="utf-8"))["adaptateur"]
        assert isinstance(a["cibles"], list) and a["cibles"] and all(isinstance(x, str) and "proj" in x for x in a["cibles"]), config_jouet
    assert la4.__doc__ is not None


def _lectures_de_cibles(source: str) -> list[tuple[str, int, bool]]:
    """(fonction, ligne, admise) de chaque constante « cibles » ou « couts_rapportes » d'un module ; admise seulement si
    c'est l'indice d'un nom `a` que la même fonction lie à `config["adaptateur"]` (configuration de l'adaptateur LoRA)."""
    sortie = []
    for f in [n for n in ast.walk(ast.parse(source)) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
        lies = {c.targets[0].id for c in ast.walk(f) if isinstance(c, ast.Assign) and len(c.targets) == 1
                and isinstance(c.targets[0], ast.Name) and isinstance(c.value, ast.Subscript)
                and isinstance(c.value.value, ast.Name) and c.value.value.id == "config"
                and isinstance(c.value.slice, ast.Constant) and c.value.slice.value == "adaptateur"}
        indices = {id(s.slice) for s in ast.walk(f) if isinstance(s, ast.Subscript) and isinstance(s.value, ast.Name)
                   and s.value.id in lies}
        for c in ast.walk(f):
            if isinstance(c, ast.Constant) and c.value in ("cibles", "couts_rapportes"):
                sortie.append((f.name, c.lineno, c.value == "cibles" and id(c) in indices))
    return sortie


def test_seule_lecture_de_cibles_des_lanceurs_est_l_adaptateur():
    """Preuve vérifiable des faux lecteurs admis par tests/test_cibles_invisibles_v2.py : dans chaque lanceur de T0.6, toute
    lecture de la clé `cibles` est `a["cibles"]` avec `a = config["adaptateur"]` dans la même fonction (une seule par lanceur)."""
    for _, module, _ in VERSIONS:
        lectures = _lectures_de_cibles(Path(module.__file__).read_text(encoding="utf-8"))
        assert lectures == [("_executer_apres_manifeste", lectures[0][1], True)], (module.__name__, lectures)


@pytest.mark.parametrize("plante", [
    'def f(config, tache):\n    a = config["adaptateur"]\n    return tache["cibles"]\n',
    'def f(config, taches):\n    a = config["adaptateur"]\n    return a["cibles"], [t["cibles"] for t in taches]\n',
    'def f(config, t):\n    a = t\n    return a["cibles"]\n',
    'def f(config):\n    a = config["adaptateur"]\n    return config["taches"][0]["couts_rapportes"]\n',
])
def test_garde_la_preuve_par_l_arbre_voit_une_lecture_de_tache_plantee(plante):
    """Artefact (R5) : une lecture de la clé `cibles` (ou des coûts rapportés) qui ne passe pas par la configuration de
    l'adaptateur n'est pas admise ; cas sain : la lecture des lanceurs l'est."""
    assert not all(admise for _, _, admise in _lectures_de_cibles(plante))
    assert _lectures_de_cibles('def f(config):\n    a = config["adaptateur"]\n    return tuple(a["cibles"])\n') == [("f", 3, True)]
