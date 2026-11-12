"""Lecture des notations refaites du pilote de T0.5 (N-021) : équivalence avec `analyser` (mêmes notations, lues dans le
dossier du pilote ou dans un run distinct), gardes (cas sain et artefact, R5), juge échu."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.environnements import lire_notations_pilote as lnp
from controle_ia.environnements import lire_pilote as lp
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, verifier_resultat
from test_lire_pilote import ANALYSE, ENTROPIE, REEL, RUN, _etiqueter_selon_8b, _jusqu_a_l_analyse, construire

NOTATIONS = "20261012-200000-t05-notations-jouet"
LECTURE = "20261012-210000-t05-lecture-juges-jouet"


@pytest.fixture(autouse=True)
def _code_du_vrai_depot(monkeypatch):
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)


def _depot(tmp_path_factory, nom):
    d = tmp_path_factory.mktemp(nom)
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "t@example.invalid"),
                 ("config", "user.name", "t")):
        subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True)
    (d / "README").write_text("x\n")
    committer(d)
    return d


def _modules_notations(depot: Path) -> None:
    for m in lnp.MODULES_NOTATIONS:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REEL / m, depot / m)


def _notations_de(depot: Path, juge: str) -> list[dict]:
    return json.loads((depot / "diag" / RUN / f"notations-{juge}-decisives.json").read_text())["resultat"]["notations"]


def _prereg_notations(depot: Path, nom: str = "prereg-notations.md") -> str:
    """Préenregistrement de test conforme (sections exigées), scellé et committé ; chemin relatif."""
    from controle_ia.prereg import SECTIONS
    from controle_ia.scellement import sceller
    f = depot / "prereg" / nom
    f.parent.mkdir(exist_ok=True)
    corps = ["# Préenregistrement de test des notations", ""]
    for s in SECTIONS:
        corps += [f"## {s}", "", f"contenu {s} `{'a' * 64}` `{'b' * 64}`", ""]
    f.write_text("\n".join(corps), encoding="utf-8")
    sceller(f)
    committer(depot)
    return f"prereg/{nom}"


def _run_des_notations(depot: Path, notations: dict, run_pilote: str = RUN, prereg: str | None = None,
                       mode: str = "jouet", issue: str | None = "resume", statuts: dict | None = None) -> None:
    """Run des notations fabriqué à la main : manifeste (sous `prereg` s'il est donné), fichiers de notations, puis
    l'issue consignée (`resume`, `arret`, les deux, ou aucune) avec le statut de chaque juge (« écrit » pour un juge
    dont le fichier est écrit, « échu » sinon, sauf `statuts`)."""
    _modules_notations(depot)
    committer(depot)
    # chemin absolu : `creer_manifeste` résout le préenregistrement depuis le dossier courant (la racine, en vrai)
    chemin, _ = creer_manifeste(depot, NOTATIONS, {"run_pilote": run_pilote, "mode": mode}, ["x"], entropie=ENTROPIE,
                                decisif=prereg is not None, prereg=str(depot / prereg) if prereg else None)
    for j, n in notations.items():
        ecrire_resultat(depot, chemin, f"notations-{j}-decisives", {"notations": n})
    juges = {j: {"statut": "écrit" if j in notations else "échu"} for j in ("8B", "3B")}
    juges.update({j: {"statut": s} for j, s in (statuts or {}).items()})
    for nom in {"resume": ["resume"], "arret": ["arret"], "les-deux": ["resume", "arret"], None: []}[issue]:
        corps = {"juges": juges} if nom == "resume" else {"etape": "essai", "partiel": {"juges": juges}}
        ecrire_resultat(depot, chemin, nom, corps)
    committer(depot)


_GABARIT: dict = {}


def _pilote_complet_et_pilote_arrete(tmp_path_factory):
    """Les deux pilotes de `_construire_les_deux_pilotes`, construits une fois par processus, puis copiés pour chaque
    test (mêmes fichiers, même histoire git ; lectures rendues en copies profondes) : suite courte sur l'instance."""
    import copy
    if not _GABARIT:
        _GABARIT["a"], _GABARIT["lecture_a"], _GABARIT["b"], _GABARIT["lecture_b"] = \
            _construire_les_deux_pilotes(tmp_path_factory)
    copies = []
    for nom in ("a", "b"):
        d = tmp_path_factory.mktemp(f"copie-{nom}")
        shutil.copytree(_GABARIT[nom], d, dirs_exist_ok=True)
        copies.append(d)
    return copies[0], copy.deepcopy(_GABARIT["lecture_a"]), copies[1], copy.deepcopy(_GABARIT["lecture_b"])


def _construire_les_deux_pilotes(tmp_path_factory):
    """A : pilote arrêté pendant les notations de D (décisives écrites dans son dossier), lu par `analyser`. B : le même
    pilote arrêté pendant les notations décisives du 8B, première analyse faite (juges en nœud)."""
    a, ta = _depot(tmp_path_factory, "a"), tmp_path_factory.mktemp("travail-a")
    _jusqu_a_l_analyse(a, ta, etapes="descriptives")
    lecture_a = lp.analyser(a, RUN, ANALYSE, a / "taches.json")
    committer(a)
    b, tb = _depot(tmp_path_factory, "b"), tmp_path_factory.mktemp("travail-b")
    _jusqu_a_l_analyse(b, tb, etapes="decisives-8B")
    lecture_b = lp.analyser(b, RUN, ANALYSE, b / "taches.json")
    committer(b)
    assert all(lecture_b["juges"][j]["plan_b"] == "nœud" for j in ("8B", "3B"))
    return a, lecture_a, b, lecture_b


def test_equivalence_avec_analyser(tmp_path_factory):
    a, lecture_a, b, lecture_b = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")})
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    s = lp._serialisable
    assert s(lecture["juges"]) == s(lecture_a["juges"])
    assert s(lecture["difference_appariee"]) == s(lecture_a["difference_appariee"])
    assert all(lecture["predictions"][k] == lecture_a["predictions"][k] for k in ("P2", "P3"))
    assert lecture["relectures_audit"] == lecture_a["relectures_audit"]
    assert lecture_a["juges"]["8B"]["decomposition_concluante"]                       # cas non trivial
    assert all(lecture["predictions"][k] == lecture_b["predictions"][k] for k in lnp.PREDICTIONS_DE_LA_PREMIERE_LECTURE)
    r = verifier_resultat(b, b / "diag" / LECTURE / "lecture-juges.json")
    assert r["resultat"]["run_notations"] == NOTATIONS and r["resultat"]["arbre_propre"]
    assert not list((b / "diag" / RUN).glob("notations-*"))                          # dossier du pilote intact


def test_juge_echu_lu_en_noeud(tmp_path_factory):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {"8B": _notations_de(a, "8B")})
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert lecture["juges"]["8B"]["decomposition_concluante"] and lecture["juges"]["3B"]["plan_b"] == "nœud"
    assert lecture["predictions"]["P3"] == "non concluant"


def test_gardes_cas_sain_et_artefacts(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    n8, n3 = _notations_de(a, "8B"), _notations_de(a, "3B")
    # artefact : une notation désalignée (empreinte de l'ensemble noté)
    altere = [dict(n8[0], ensemble_sha256="0" * 64)] + n8[1:]
    _run_des_notations(b, {"8B": altere, "3B": n3})
    with pytest.raises(GardeArret, match="désalignement"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert not (b / "runs" / LECTURE).exists()
    # cas sain : les mêmes notations, alignées, dans un run des notations neuf (copie neuve du pilote arrêté)
    _, _, b2, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b2, {"8B": n8, "3B": n3})
    assert lnp.lire_notations(b2, RUN, NOTATIONS, ANALYSE, b2 / "taches.json", LECTURE)["juges"]["8B"]["plan_b"]


def test_gardes_de_rattachement_et_de_modules(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    # artefact : le dossier du pilote porte déjà des notations décisives (pilote A)
    _run_des_notations(a, {j: _notations_de(a, j) for j in ("8B", "3B")})
    with pytest.raises(GardeArret, match="porte des notations décisives"):
        lnp.lire_notations(a, RUN, NOTATIONS, ANALYSE, a / "taches.json", LECTURE)
    # artefact : run des notations rattaché à un autre pilote
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")}, run_pilote="20261010-120001-autre")
    with pytest.raises(GardeArret, match="rattaché au pilote"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)


def test_modules_modifies_et_predictions_divergentes(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")})
    # artefact : module des notations modifié après le commit du run des notations
    m = b / lnp.MODULES_NOTATIONS[1]
    texte = m.read_text()
    m.write_text(texte + "\n# modifié\n")
    with pytest.raises(GardeArret, match="modules des notations modifiés"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, autoriser_depot_sale=True)
    m.write_text(texte)
    # artefact : module de lecture gelé modifié (garde gelée d'`_ouvrir_analyse`)
    g = b / lp.MODULES_LECTURE[1]
    texte_g = g.read_text()
    g.write_text(texte_g + "\n# modifié\n")
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, autoriser_depot_sale=True)
    g.write_text(texte_g)
    # artefact : une prédiction de la première lecture qui ne se retrouve pas
    vraie = lnp.predictions
    monkeypatch.setattr(lnp, "predictions", lambda *x: {**vraie(*x), "P1": "inventée"})
    with pytest.raises(GardeArret, match="recalculées ≠ celles de la première lecture"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    monkeypatch.setattr(lnp, "predictions", vraie)
    assert not (b / "runs" / LECTURE).exists()
    lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)          # cas sain


def test_issue_du_run_des_notations_cas_sain_et_artefacts(tmp_path_factory):
    """Un run des notations sans résumé ni arrêt, ou avec les deux, n'est pas lu (ligne gelée du pilote) ; les statuts
    consignés doivent s'accorder avec les fichiers présents ; un arrêt consigné après un juge écrit se lit."""
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    n8 = _notations_de(a, "8B")
    for issue, statuts, motif in ((None, None, "ni resume.json ni arret.json"), ("les-deux", None, "un seul attendu"),
                                  ("resume", {"8B": "échu"}, "désaccord"), ("resume", {"3B": "écrit"}, "désaccord")):
        d = tmp_path_factory.mktemp("copie")
        shutil.copytree(b, d, dirs_exist_ok=True)
        _run_des_notations(d, {"8B": n8}, issue=issue, statuts=statuts)
        with pytest.raises(GardeArret, match=motif):
            lnp.lire_notations(d, RUN, NOTATIONS, ANALYSE, d / "taches.json", LECTURE)
        assert not (d / "runs" / LECTURE).exists()
    # issue sans sceau conforme : arrêt (garde gelée `verifier_resultat`, appelée par le lecteur)
    d = tmp_path_factory.mktemp("copie")
    shutil.copytree(b, d, dirs_exist_ok=True)
    _run_des_notations(d, {"8B": n8}, issue="resume")
    s = Path(str(d / "diag" / NOTATIONS / "resume.json") + ".sha256")
    s.write_text("0" * 64 + "  resume.json\n")
    with pytest.raises(GardeArret, match="empreinte"):
        lnp.lire_notations(d, RUN, NOTATIONS, ANALYSE, d / "taches.json", LECTURE, autoriser_depot_sale=True)
    assert not (d / "runs" / LECTURE).exists()
    _run_des_notations(b, {"8B": n8}, issue="arret")                                 # cas sain : arrêt pendant le 3B
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert lecture["issue_des_notations"] == {"fichier": "arret", "statuts": {"8B": "écrit", "3B": "échu"}}
    assert lecture["juges"]["3B"]["plan_b"] == "nœud" and lecture["predictions"]["P3"] == "non concluant"


@pytest.mark.parametrize("artefact, motif", [
    ("non-decisif", "non décisif"),
    ("mode-jouet", "hors mode réel"),
    ("autre-prereg", "autre préenregistrement"),
    ("prereg-modifie", "sceau|scellé|empreinte"),
    ("prereg-rescelle", "autre préenregistrement"),
    ("prereg-hors-du-depot", "hors du dépôt$"),          # garde du lecteur, non celle de creer_manifeste
])
def test_lecture_decisive_exige_le_run_sous_le_preenregistrement(tmp_path_factory, artefact, motif):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    p = _prereg_notations(b)
    autre = _prereg_notations(b, "autre.md")
    notes = {j: _notations_de(a, j) for j in ("8B", "3B")}
    if artefact == "non-decisif":
        _run_des_notations(b, notes, mode="reel")
    elif artefact == "mode-jouet":
        _run_des_notations(b, notes, prereg=p, mode="jouet")
    elif artefact == "autre-prereg":
        _run_des_notations(b, notes, prereg=autre, mode="reel")
    elif artefact == "prereg-modifie":
        _run_des_notations(b, notes, prereg=p, mode="reel")
        (b / p).write_text((b / p).read_text() + "\nmodifié\n")
    elif artefact == "prereg-rescelle":
        # même chemin, texte changé puis rescellé : sceau conforme, empreinte ≠ celle du manifeste du run
        from controle_ia.scellement import sceller
        _run_des_notations(b, notes, prereg=p, mode="reel")
        (b / p).write_text((b / p).read_text() + "\nmodifié\n")
        Path(str(b / p) + ".sha256").unlink()
        sceller(b / p)
    else:
        _run_des_notations(b, notes, prereg=p, mode="reel")
    passe = str(tmp_path_factory.mktemp("ailleurs") / "prereg.md") if artefact == "prereg-hors-du-depot" else str(b / p)
    with pytest.raises(GardeArret, match=motif):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, prereg=passe,
                           autoriser_depot_sale=True)
    assert not (b / "runs" / LECTURE).exists()


def test_lecture_decisive_cas_sain(tmp_path_factory):
    a, lecture_a, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    p = _prereg_notations(b)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")}, prereg=p, mode="reel")
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, prereg=str(b / p))
    assert lp._serialisable(lecture["juges"]) == lp._serialisable(lecture_a["juges"])
    m = json.loads((b / "runs" / LECTURE / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == p
    # graines tirées par la lecture, consignées dans son manifeste (R9), égales à celles de la première analyse
    m_a = json.loads((b / "runs" / ANALYSE / "manifeste.json").read_text())
    cles = ["analyse/bootstrap-parts-8B", "analyse/bootstrap-parts-3B", "analyse/bootstrap-difference", "analyse/audit"]
    assert sorted(m["graines"]) == sorted(cles) and all(m["graines"][k] == m_a["graines"][k] for k in cles)


def test_graines_de_la_lecture_gardes(tmp_path_factory, monkeypatch):
    """Graines de la lecture : égales à celles du manifeste de la première analyse, d'une seule entropie ; sinon arrêt
    avant toute écriture (R5 ; cas sain : test_lecture_decisive_cas_sain)."""
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")})
    vraies = lnp.graines
    monkeypatch.setattr(lnp, "graines", lambda c, e: {k: dict(v, etat_controle=[0, 0]) for k, v in vraies(c, e).items()})
    with pytest.raises(GardeArret, match="graines de la lecture ≠ celles du manifeste de la première analyse"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    monkeypatch.setattr(lnp, "graines", vraies)
    vraie_ouverture = lnp._ouvrir_analyse

    def ouverture(racine, run):
        chemin, m, etat = vraie_ouverture(racine, run)
        g = dict(m["graines"])
        g["analyse/audit"] = vraies(["analyse/audit"], 1)["analyse/audit"]       # graine valide, autre entropie
        return chemin, {**m, "graines": g}, etat

    monkeypatch.setattr(lnp, "_ouvrir_analyse", ouverture)
    with pytest.raises(GardeArret, match="d'entropies différentes"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert not (b / "runs" / LECTURE).exists()


def _temoin_meme_pilote(tmp_path_factory, notes: dict):
    """Témoin « même pilote » (contre-lecture R2) : C construit comme B (même graine : mêmes épisodes, même appariement,
    même étiquetage), puis les notations données écrites dans le dossier du pilote, lu par `analyser`."""
    c, tc = _depot(tmp_path_factory, "c"), tmp_path_factory.mktemp("travail-c")
    d = construire(c, etapes="decisives-8B")
    chemin_m = c / "runs" / RUN / "manifeste.json"
    for j, n in notes.items():
        ecrire_resultat(c, chemin_m, f"notations-{j}-decisives", {"notations": n})
    committer(c)
    lp.preparer_etiquetage(c, RUN, ANALYSE, d["prereg"], d["taches"], tc)
    committer(c)
    _etiqueter_selon_8b(c, d, tc, inverser=0.1)
    lp.lire_etiquetage(c, RUN, ANALYSE, d["taches"], tc)
    committer(c)
    return lp.analyser(c, RUN, ANALYSE, c / "taches.json")


def test_equivalence_avec_analyser_sur_le_meme_pilote(tmp_path_factory):
    a, _, b, lecture_b = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    notes = {j: _notations_de(a, j) for j in ("8B", "3B")}
    temoin = _temoin_meme_pilote(tmp_path_factory, notes)
    _run_des_notations(b, notes)
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    s = lp._serialisable
    assert s(lecture["juges"]) == s(temoin["juges"])
    assert s(lecture["difference_appariee"]) == s(temoin["difference_appariee"])
    assert all(lecture["predictions"][k] == temoin["predictions"][k] for k in ("P1", "P2", "P3", "P4", "P5", "P6", "P7"))
    assert lecture["relectures_audit"] == temoin["relectures_audit"]
    sans_familles = lambda x: {k: v for k, v in x.items() if k != "familles"}
    assert sans_familles(lecture["audit_r4_juges"]) == sans_familles(temoin["audit_r4"])
    # cas non trivial : deux juges concluants, différence sur au moins 48 tâches, P3 tranchée, 10 réponses tirées
    assert lecture["difference_appariee"]["taches"] >= 48 and lecture["predictions"]["P3"] != "non concluant"
    assert all(lecture["juges"][j]["decomposition_concluante"] for j in ("8B", "3B"))
    assert not lecture["audit_r4_juges"]["declenche"] and not lecture["lecture_suspendue"]
    assert len(lecture["relectures_audit"]["reponses_de_juge"]) == 10
    # les actions tirées diffèrent de celles de la première lecture (réponses tirées d'abord, même graine) : déclaré
    assert lecture["relectures_audit"]["actions"] != lecture_b["relectures_audit"]["actions"]


def test_8b_echu_3b_seul_lu(tmp_path_factory):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {"3B": _notations_de(a, "3B")})
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert lecture["juges"]["8B"]["plan_b"] == "nœud" and lecture["juges"]["3B"]["decomposition_concluante"]
    assert lecture["predictions"]["P2"] == "non concluant" and lecture["predictions"]["P3"] == "non concluant"
    assert lecture["difference_appariee"] is None
    assert {x.split("/")[0] for x in lecture["relectures_audit"]["reponses_de_juge"]} == {"juge-3B"}
    # lecture retenue (R-164 ; R-155, (3)) : un juge sans fichier est en nœud, sans déclencher « décomposition
    # impossible » ; le déclencheur ne joue que pour un juge écrit dont la décomposition est impossible (artefact)
    assert not lecture["audit_r4_juges"]["declenche"] and not lecture["lecture_suspendue"]
    _, _, c, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    constant = [dict(x, notes={k: 1 for k in x["notes"]}) if x["score"] is not None else x
                for x in _notations_de(a, "3B")]                                   # notes constantes
    _run_des_notations(c, {"3B": constant})
    lecture = lnp.lire_notations(c, RUN, NOTATIONS, ANALYSE, c / "taches.json", LECTURE)
    assert lecture["juges"]["3B"].get("decomposition_impossible")
    assert lecture["audit_r4_juges"]["declenche"] and lecture["lecture_suspendue"]
    assert [x for x in lecture["audit_r4_juges"]["trop_sale"] if "décomposition impossible" in x] == \
        [x for x in lecture["audit_r4_juges"]["trop_sale"] if x.startswith("juge 3B : décomposition impossible")] != []


def test_declencheur_propre_aux_juges_suspend_la_lecture(tmp_path_factory):
    """Plus de 10 % de réponses A et B identiques pour le 8B : déclencheur « trop propre » propre aux juges, lecture
    suspendue (cas sain : test d'équivalence, aucun déclencheur). Second témoin « même pilote » (contre-lecture R2,
    angle « lecture ») : `analyser`, sur les mêmes notations écrites dans le dossier du pilote, déclenche le même audit
    (mêmes listes « trop propre » et « trop sale », sans famille) et suspend aussi la lecture."""
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    n8 = _notations_de(a, "8B")
    par_cle = {x["cle"]: x for x in n8}
    copie = [dict(x, reponse=par_cle[x["cle"].replace("/passe-1", "/passe-0")]["reponse"])
             if x["cle"].endswith("/passe-1") else x for x in n8]
    notes = {"8B": copie, "3B": _notations_de(a, "3B")}
    _run_des_notations(b, notes)
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert lecture["audit_r4_juges"]["declenche"] and lecture["lecture_suspendue"]
    assert any("8B" in x and "identiques" in x for x in lecture["audit_r4_juges"]["trop_propre"])
    temoin = _temoin_meme_pilote(tmp_path_factory, notes)
    assert temoin["audit_r4"]["familles"] == []
    assert lecture["audit_r4_juges"]["trop_propre"] == temoin["audit_r4"]["trop_propre"] != []
    assert lecture["audit_r4_juges"]["trop_sale"] == temoin["audit_r4"]["trop_sale"]
    assert temoin["lecture_suspendue"] is True


def test_autres_gardes_du_lecteur_cas_sain_et_artefacts(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    notes = {j: _notations_de(a, j) for j in ("8B", "3B")}
    _run_des_notations(b, notes)
    lire = lambda **k: lnp.lire_notations(b, k.get("run_pilote", RUN), k.get("run_notations", NOTATIONS), ANALYSE,
                                          b / "taches.json", LECTURE, autoriser_depot_sale=k.get("sale", False))
    # manifeste du pilote différent de celui de l'analyse
    vrai_cp = lnp.charger_pilote
    monkeypatch.setattr(lnp, "charger_pilote", lambda *x: {**vrai_cp(*x), "manifeste_sha256": "0" * 64})
    with pytest.raises(GardeArret, match="manifeste du pilote différent de celui de l'analyse"):
        lire()
    monkeypatch.setattr(lnp, "charger_pilote", vrai_cp)
    # run du pilote différent de celui du manifeste d'analyse
    with pytest.raises(GardeArret, match="≠ run du manifeste d'analyse"):
        lire(run_pilote="20261010-120001-autre")
    # manifeste du run des notations absent
    with pytest.raises(GardeArret, match="manifeste du run des notations absent"):
        lire(run_notations="20261012-200009-absent")
    # format recalculé différent de la première lecture
    vrai_format = lnp.mesures_format
    monkeypatch.setattr(lnp, "mesures_format", lambda *x: {**vrai_format(*x), "part_valides": -1.0})
    with pytest.raises(GardeArret, match="format recalculé ≠ format de la première lecture"):
        lire()
    monkeypatch.setattr(lnp, "mesures_format", vrai_format)
    # première lecture d'un autre pilote
    vrai_vr = lnp.verifier_resultat

    def vr(racine, chemin):
        c = vrai_vr(racine, chemin)
        if Path(chemin).name == "lecture.json":
            c = {**c, "resultat": {**c["resultat"], "run_pilote": "20261010-120001-autre"}}
        return c

    monkeypatch.setattr(lnp, "verifier_resultat", vr)
    with pytest.raises(GardeArret, match="première lecture d'un autre pilote"):
        lire()
    monkeypatch.setattr(lnp, "verifier_resultat", vrai_vr)
    # modules des notations absents
    m = b / lnp.MODULES_NOTATIONS[0]
    texte = m.read_text()
    m.unlink()
    with pytest.raises(GardeArret, match="modules des notations absents"):
        lire(sale=True)
    m.write_text(texte)
    # fichier de notations rattaché à un autre run (copié avec son sceau)
    autre = "20261012-200008-autre-notations"
    chemin_autre, _ = creer_manifeste(b, autre, {"run_pilote": RUN, "mode": "jouet"}, ["x"], entropie=ENTROPIE,
                                      autoriser_depot_sale=True)
    f_autre = ecrire_resultat(b, chemin_autre, "notations-8B-decisives", {"notations": notes["8B"]})
    cible = b / "diag" / NOTATIONS / "notations-8B-decisives.json"
    sauve = (cible.read_bytes(), Path(str(cible) + ".sha256").read_bytes())
    cible.write_bytes(f_autre.read_bytes())
    Path(str(cible) + ".sha256").write_bytes(Path(str(f_autre) + ".sha256").read_bytes())
    with pytest.raises(GardeArret, match=f"rattaché au run {autre}"):
        lire(sale=True)
    cible.write_bytes(sauve[0])
    Path(str(cible) + ".sha256").write_bytes(sauve[1])
    # résumé du run des notations rattaché à un autre run (copié avec son sceau)
    r_autre = ecrire_resultat(b, chemin_autre, "resume", {"juges": {"8B": {"statut": "écrit"}, "3B": {"statut": "écrit"}}})
    cible = b / "diag" / NOTATIONS / "resume.json"
    sauve = (cible.read_bytes(), Path(str(cible) + ".sha256").read_bytes())
    cible.write_bytes(r_autre.read_bytes())
    Path(str(cible) + ".sha256").write_bytes(Path(str(r_autre) + ".sha256").read_bytes())
    with pytest.raises(GardeArret, match=rf"resume\.json rattaché au run {autre}"):
        lire(sale=True)
    cible.write_bytes(sauve[0])
    Path(str(cible) + ".sha256").write_bytes(sauve[1])
    # comparaison des modules des notations à un commit introuvable ; cas sain : le commit du run des notations
    with pytest.raises(GardeArret, match="comparaison au commit"):
        lnp.exiger_modules_notations(b, "0" * 40)
    lnp.exiger_modules_notations(b, json.loads((b / "runs" / NOTATIONS / "manifeste.json").read_text())["commit"])
    assert not (b / "runs" / LECTURE).exists()
    lire(sale=True)                                                                   # cas sain
