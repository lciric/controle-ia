"""Lanceur « notations seules » du pilote de T0.5 (N-021) : sur un pilote jouet arrêté pendant ses notations décisives,
notations refaites dans un run distinct, aux mêmes graines ; gardes d'avant le manifeste (cas sain et artefact, R5) ;
échéances par juge et globale ; signal TERM ; lignes de progression sans texte."""
from __future__ import annotations

import atexit
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

from conftest import committer
from controle_ia import gardes
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_pilote_a import CIBLES_TEST, TACHES, _config_lanceur

PILOTE = "20261012-100000-pilote-jouet"


def _taches(depot):
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES]}), encoding="utf-8")
    return f, sceller(f)


_GABARITS: dict = {}


def _pilote_arrete(depot, monkeypatch, etape_arret="decisives"):
    """Pilote jouet arrêté (voir `_construire_pilote_arrete`), construit une fois par processus dans un gabarit, puis
    copié dans le dépôt du test (mêmes fichiers, même histoire git) : la suite reste courte sur l'instance (mise en
    place sous 1 500 s ; contre-lecture R2, angle « chaîne »)."""
    if etape_arret not in _GABARITS:
        gabarit = Path(tempfile.mkdtemp(prefix=f"pilote-jouet-{etape_arret}-"))
        atexit.register(shutil.rmtree, gabarit, True)
        for args in (("init", "-q", "-b", "main"), ("config", "user.email", "test@example.invalid"),
                     ("config", "user.name", "test")):
            subprocess.run(["git", "-C", str(gabarit), *args], check=True, capture_output=True)
        (gabarit / "README").write_text("x\n")
        committer(gabarit)
        _construire_pilote_arrete(gabarit, monkeypatch, etape_arret)
        _GABARITS[etape_arret] = gabarit
    shutil.rmtree(depot / ".git")
    shutil.copytree(_GABARITS[etape_arret], depot, dirs_exist_ok=True)
    f = depot / "taches.json"
    return f, empreinte(f)


def _construire_pilote_arrete(depot, monkeypatch, etape_arret="decisives"):
    """Pilote jouet complet jusqu'à l'appariement, ensembles non vides, arrêté à l'échéance pendant les notations
    décisives du 8B, comme le vrai pilote."""
    vrai_jouer = lp.jouer_pilote

    def jouer(*a, **k):
        fiches, vecteurs, cn = vrai_jouer(*a, **k)
        for f in fiches:
            f["bilan"]["ensemble"] = f"PROPOSAL 1: idée {f['episode']}"
        return fiches, vecteurs, cn

    def noter(*a, **k):
        raise GardeArret("limite de durée dépassée pendant les notations")

    def apparier_en_panne(*a, **k):
        raise GardeArret("panne simulée de l'appariement")

    monkeypatch.setattr(lp, "jouer_pilote", jouer)
    monkeypatch.setattr(lp, "noter_ensembles", noter)
    if etape_arret == "appariement":
        monkeypatch.setattr(lp, "apparier", apparier_en_panne)
    f, sha = _taches(depot)
    committer(depot)
    with pytest.raises(GardeArret):
        lp.executer(_config_lanceur(), depot, PILOTE, None, str(f))
    monkeypatch.undo()
    committer(depot)
    return f, sha


def _config(**changes):
    c = _config_lanceur()
    base = {k: c[k] for k in npa.CLES_EGALES_AU_PILOTE}
    return {**base, "mode": "jouet", "run_pilote": PILOTE,
            "duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 600}, "duree_globale_s": 1200,
            "notations_attendues_par_juge": 4, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


def test_bout_en_bout_notations_dans_un_run_distinct(depot, monkeypatch, capsys):
    f, _ = _pilote_arrete(depot, monkeypatch)
    avant = _fichiers(depot, PILOTE)
    assert avant == ["appariements.json", "arret.json", "episodes.json"]
    run = "20261012-110000-notations-jouet"
    resume = npa.executer(_config(), depot, run, None, str(f))
    assert _fichiers(depot, PILOTE) == avant                       # rien d'écrit dans le dossier du pilote
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "notations-jouet-8B-decisives.json",
                                     "resume.json"]
    assert {n: j["statut"] for n, j in resume["juges"].items()} == {"jouet-8B": "écrit", "jouet-3B": "écrit"}
    fiches = json.loads((depot / "diag" / PILOTE / "episodes.json").read_text())["resultat"]["fiches"]
    import hashlib
    ensembles = {x["episode"]: hashlib.sha256(x["bilan"]["ensemble"].encode()).hexdigest() for x in fiches}
    for juge in ("jouet-8B", "jouet-3B"):
        r = verifier_resultat(depot, depot / "diag" / run / f"notations-{juge}-decisives.json")
        assert r["run_id"] == run
        cles = [n["cle"] for n in r["resultat"]["notations"]]
        assert cles == [f"juge-{juge}/{t['identifiant']}/e0/passe-{p}" for t in TACHES for p in (0, 1)]
        assert all(n["ensemble_sha256"] == ensembles[n["cle"].split("/", 1)[1].rsplit("/", 1)[0]]
                   for n in r["resultat"]["notations"])
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    mn = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert all(mn["graines"][k] == mp["graines"][k] for k in mn["graines"])
    err = capsys.readouterr().err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ")]
    assert len(lignes) == 2 + 1 + 2 + 1 and "PROPOSAL" not in err and "idée" not in err
    assert "juge=jouet-8B lot=1/2" in lignes[0]


def test_rejeu_identique_et_r12(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    a = "20261012-110001-notations-jouet"
    b = "20261012-110002-notations-jouet"
    npa.executer(_config(), depot, a, None, str(f), autoriser_depot_sale=True)
    npa.executer(_config(), depot, b, None, str(f), autoriser_depot_sale=True)
    for juge in ("jouet-8B", "jouet-3B"):
        na, nb = (json.loads((depot / "diag" / r / f"notations-{juge}-decisives.json").read_text())["resultat"]
                  ["notations"] for r in (a, b))
        assert [(x["reponse"], x["score"]) for x in na] == [(x["reponse"], x["score"]) for x in nb]
    with pytest.raises(GardeArret, match="R12"):
        npa.executer(_config(), depot, a, None, str(f), autoriser_depot_sale=True)


def _gardes_saines(depot, f, config=None):
    """Cas sain des gardes d'avant le manifeste, rejouées dans l'ordre d'`executer` sans lancer de notation (le run
    complet est éprouvé par le test de bout en bout) : suite courte sur l'instance."""
    c = config or _config()
    npa.exiger_config_notations(c)
    pil = npa.charger_pilote_note(depot, c["run_pilote"])
    assert pil["arret"]["partiel"]["taches_sha256"] == empreinte(f)
    npa.exiger_egal_au_pilote(c, pil, c["mode"])
    par_id = {x["identifiant"]: x for x in pa.charger_taches(str(f))}
    dem = {j["nom"]: npa.demandes_decisives(pil, par_id, c, j["nom"]) for j in c["juges"]}
    assert all(len(v) == c["notations_attendues_par_juge"] for v in dem.values())
    entropie = int(next(iter(pil["manifeste"]["graines"].values()))["entropie"])
    npa.exiger_graines_du_pilote(npa.cles_des_graines(dem), entropie, pil)


@pytest.mark.parametrize("changement, motif", [
    ({"lot_juge": 3}, "lot_juge ≠ celui du pilote"),
    ({"notations_attendues_par_juge": 5}, "4 notations à faire, 5 attendues"),
    ({"duree_globale_s": 0}, "durée globale"),
    ({"duree_max_juges_s": {"jouet-8B": 600}}, "une durée par juge"),
    ({"run_pilote": "20261012-100001-autre"}, "manifeste du pilote absent"),
])
def test_gardes_de_configuration_cas_sain_et_artefacts(depot, monkeypatch, changement, motif):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110003-notations-jouet"
    with pytest.raises(GardeArret, match=motif):
        npa.executer(_config(**changement), depot, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / run).exists()
    _gardes_saines(depot, f)                                                            # cas sain


def test_config_incomplete_et_reel_sans_preenregistrement(depot):
    with pytest.raises(GardeArret, match="incomplète"):
        npa.executer({k: v for k, v in _config().items() if k != "fils"}, depot, "20261012-110004-x", None, "t.json")
    with pytest.raises(GardeArret, match="R1"):
        npa.executer(_config(mode="reel"), depot, "20261012-110005-x", None, "t.json")
    assert not (depot / "runs").exists()


def test_etat_du_pilote_artefacts(depot, monkeypatch):
    """Notations ou résumé déjà présents, épisodes altérés, tâches différentes : arrêt avant le manifeste."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110006-notations-jouet"
    d = depot / "diag" / PILOTE
    # tâches différentes de celles du pilote
    g = depot / "taches-autres.json"
    g.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES[:1]]}), encoding="utf-8")
    sceller(g)
    with pytest.raises(GardeArret, match="tâches ≠ celles du pilote"):
        npa.executer(_config(), depot, run, None, str(g), autoriser_depot_sale=True)
    # épisodes altérés : le sceau ne tient plus
    texte = (d / "episodes.json").read_text()
    (d / "episodes.json").write_text(texte.replace("idée", "idee"))
    with pytest.raises(GardeArret):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    (d / "episodes.json").write_text(texte)
    # notation déjà présente dans le dossier du pilote
    (d / "notations-jouet-8B-decisives.json").write_text("{}")
    with pytest.raises(GardeArret, match="déjà présents"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    (d / "notations-jouet-8B-decisives.json").unlink()
    assert not (depot / "runs" / run).exists()
    _gardes_saines(depot, f)                                                            # cas sain


def test_pilote_arrete_pendant_l_appariement_sans_appariements(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch, etape_arret="appariement")
    with pytest.raises(GardeArret, match="appariements.json absent"):
        npa.executer(_config(), depot, "20261012-110007-notations-jouet", None, str(f), autoriser_depot_sale=True)


def _prereg(depot, config, pilote_d, sha_taches, entropie, commit, nom="prereg-notations.md", lignes_en_plus=(),
            remplacements=None):
    """Préenregistrement de test ; `remplacements` : intitulé → valeur citée à la place (None : ligne retirée)."""
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    valeurs = {"Commit du code d'analyse": commit,
               "Configuration des notations (empreinte canonique)": lp.empreinte_config(config),
               "Run du pilote noté": PILOTE,
               "Manifeste du pilote noté": empreinte(depot / "runs" / PILOTE / "manifeste.json"),
               "Épisodes du pilote noté": empreinte(pilote_d / "episodes.json"),
               "Arrêt du pilote noté": empreinte(pilote_d / "arret.json"),
               "Tâches du pilote": sha_taches, "Entropie": entropie, **(remplacements or {})}
    lignes = [f"- {k} : `{v}`" for k, v in valeurs.items() if v is not None] + list(lignes_en_plus)
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def test_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    f, sha = _pilote_arrete(depot, monkeypatch)
    monkeypatch.setattr(npa, "exiger_code_importe_sous", lambda racine: None)
    import subprocess
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    d = depot / "diag" / PILOTE
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    entropie = int(next(iter(mp["graines"].values()))["entropie"])
    c = _config()
    sain = _prereg(depot, c, d, sha, entropie, commit)
    cas = [(_prereg(depot, _config(duree_globale_s=1100), d, sha, entropie, commit, "p-config.md"), "configuration"),
           (_prereg(depot, c, d, sha, entropie + 1, commit, "p-entropie.md"), "entropie ≠ celle du pilote"),
           (_prereg(depot, c, d, "c" * 64, entropie, commit, "p-taches.md"), "tâches"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-double.md",
                    (f"- Run du pilote noté : `20261012-100009-autre`",)), "plusieurs fois"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-manifeste.md",
                    remplacements={"Manifeste du pilote noté": "1" * 64}), "manifeste"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-episodes.md",
                    remplacements={"Épisodes du pilote noté": "2" * 64}), "épisodes"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-arret.md",
                    remplacements={"Arrêt du pilote noté": "3" * 64}), "arrêt"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-arret-absent.md",
                    remplacements={"Arrêt du pilote noté": None}), "arrêt citée nulle part"),
           (_prereg(depot, c, d, sha, entropie, commit, "p-run.md",
                    remplacements={"Run du pilote noté": "20261012-100009-autre"}), "run du pilote")]
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            npa.executer(c, depot, "20261012-110008-notations-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261012-110008-notations-jouet").exists()
    resume = npa.executer(c, depot, "20261012-110009-notations-jouet", str(sain), str(f), autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit
    m = json.loads((depot / "runs" / "20261012-110009-notations-jouet" / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-notations.md"


def test_echeance_du_8b_le_3b_continue(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110010-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 1e-9, "jouet-3B": 600}), depot, run, None, str(f),
                          autoriser_depot_sale=True)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 0
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "resume.json"]


def test_echeance_globale_arrete_et_consigne(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110011-notations-jouet"
    with pytest.raises(GardeArret, match="limite de durée"):
        npa.executer(_config(duree_globale_s=1e-9), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations decisives par jouet-8B" and r["partiel"]["juges"]["jouet-8B"]["lots_faits"] == 0


def test_signal_term_pendant_le_8b_n_ouvre_jamais_le_3b(depot, monkeypatch):
    """Un TERM reçu pendant le 8B arrête le run (jamais avalé pour continuer) : aucun fichier de notation, le 3B
    n'est pas commencé, `arret.json` consigne l'étape."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    vrai = npa.noter_ensembles

    def noter(*a, **k):
        sortie = vrai(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)          # signal avalé par une bibliothèque : drapeau seul
        return sortie

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110012-notations-jouet"
    with pytest.raises(GardeArret):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "notations decisives par jouet-8B" and set(r["partiel"]["juges"]) == {"jouet-8B"}
    assert r["partiel"]["juges"]["jouet-8B"]["lots_faits"] == 1


def test_format_different_du_pilote_arrete(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    vrai = npa.controler_format

    def controle(fmt, spec, role, config):
        r = vrai(fmt, spec, role, config)
        return {**r, "altere": True} if spec["nom"] == "jouet-3B" else r

    monkeypatch.setattr(npa, "controler_format", controle)
    run = "20261012-110013-notations-jouet"
    with pytest.raises(GardeArret, match="format ≠ celui du début du pilote"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]["etape"] == "contrôle du format"


def test_graines_differentes_du_pilote_arretent():
    pilote = {"manifeste": {"graines": {"a": {"entropie": "7", "spawn_key": ["1"]}}}}
    with pytest.raises(GardeArret, match="entropie ≠ celle du pilote"):
        npa.exiger_graines_du_pilote(["a"], 8, pilote)
    from controle_ia.manifeste import graines
    pilote = {"manifeste": {"graines": graines(["a", "b"], 7)}}
    npa.exiger_graines_du_pilote(["a", "b"], 7, pilote)                                # cas sain
    pilote["manifeste"]["graines"]["b"] = {"entropie": "7", "spawn_key": ["0"]}
    with pytest.raises(GardeArret, match="graines ≠ celles du pilote"):
        npa.exiger_graines_du_pilote(["a", "b"], 7, pilote)


def test_noter_ensembles_inchange():
    """Le lanceur importe `noter_ensembles` du code cité, sans copie ni enveloppe."""
    assert npa.noter_ensembles is pa.noter_ensembles and npa.demandes_de_notation is lp.demandes_de_notation


def _reecrire(chemin, changer):
    """Résultat scellé réécrit (contenu changé par `changer`), puis rescellé : seule la garde visée peut l'arrêter."""
    corps = json.loads(chemin.read_text())
    changer(corps)
    chemin.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    Path(str(chemin) + ".sha256").unlink()             # artefact de test : l'ancien sceau retiré, puis rescellé
    sceller(chemin)


def test_etat_du_pilote_etape_appariement_rattachement_resume(depot, monkeypatch):
    """Gardes de `charger_pilote_note` (R5) : arrêt à une autre étape (appariement présent), appariement non consigné
    comme écrit, résultat rattaché à un autre run, résumé déjà présent ; puis cas sain."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    d = depot / "diag" / PILOTE
    sauve = {n: (d / n).read_bytes() for n in ("arret.json", "arret.json.sha256", "appariements.json",
                                                "appariements.json.sha256")}

    def remettre():
        for n, b in sauve.items():
            (d / n).write_bytes(b)

    _reecrire(d / "arret.json", lambda c: c["resultat"].update(etape="appariement par jouet-8B"))
    with pytest.raises(GardeArret, match="arrêté à l'étape 'appariement par jouet-8B'"):
        npa.charger_pilote_note(depot, PILOTE)
    remettre()
    _reecrire(d / "arret.json", lambda c: c["resultat"]["partiel"].pop("appariement_ecrit"))
    with pytest.raises(GardeArret, match="appariement non consigné comme écrit"):
        npa.charger_pilote_note(depot, PILOTE)
    remettre()
    from controle_ia.manifeste import creer_manifeste, lire_manifeste
    autre = "20261012-100002-autre-run"
    chemin_autre, _ = creer_manifeste(depot, autre, {"essai": 1}, ["x"], autoriser_depot_sale=True)
    _, sha_autre = lire_manifeste(chemin_autre)
    _reecrire(d / "appariements.json", lambda c: c.update(run_id=autre, manifeste_sha256=sha_autre))
    with pytest.raises(GardeArret, match="rattaché à un autre run ou à un autre manifeste"):
        npa.charger_pilote_note(depot, PILOTE)
    remettre()
    (d / "resume.json").write_text("{}")
    with pytest.raises(GardeArret, match=r"\['resume.json'\] déjà présents"):
        npa.charger_pilote_note(depot, PILOTE)
    (d / "resume.json").unlink()
    assert npa.charger_pilote_note(depot, PILOTE)["arret"]["etape"] == "notations decisives par jouet-8B"   # cas sain


def test_garde_des_versions_en_mode_reel(depot, monkeypatch):
    """Versions de torch, transformers, tokenizers et numpy égales à celles du pilote, en mode réel seulement (R5)."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    pil = npa.charger_pilote_note(depot, PILOTE)
    vp = pil["manifeste"]["versions"]
    monkeypatch.setattr(npa, "versions", lambda: dict(vp))
    npa.exiger_egal_au_pilote(_config(), pil, "reel")                                   # cas sain
    for b in npa.VERSIONS_EGALES:
        monkeypatch.setattr(npa, "versions", lambda b=b: {**vp, b: "0.0.essai"})
        with pytest.raises(GardeArret, match=rf"versions ≠ celles du pilote : \['{b}'\]"):
            npa.exiger_egal_au_pilote(_config(), pil, "reel")
    npa.exiger_egal_au_pilote(_config(), pil, "jouet")                                  # jouet : versions non lues


@pytest.mark.parametrize("changement, accepte", [
    ({"duree_globale_s": 23100}, True), ({"duree_globale_s": 23101}, False),
    ({"duree_max_juges_s": {"jouet-8B": 0, "jouet-3B": 600}}, False),
    ({"duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 23101}}, False),
    ({"duree_max_juges_s": {"jouet-8B": True, "jouet-3B": 600}}, False),
    ({"notations_attendues_par_juge": 0}, False), ({"mode": "autre"}, False),
])
def test_bornes_de_la_configuration(changement, accepte):
    if accepte:
        npa.exiger_config_notations(_config(**changement))
    else:
        with pytest.raises(GardeArret):
            npa.exiger_config_notations(_config(**changement))


def test_format_du_3b_recharge_hors_ligne_different(depot, monkeypatch):
    """Le 3B rechargé hors ligne doit garder le format contrôlé au début du run : sinon arrêt consigné à son
    chargement, le fichier du 8B restant écrit (R5)."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    vrai, appels = npa.controler_format, []

    def controle(fmt, spec, role, config):
        r = vrai(fmt, spec, role, config)
        appels.append(spec["nom"])
        return {**r, "altere": True} if spec["nom"] == "jouet-3B" and appels.count("jouet-3B") == 2 else r

    monkeypatch.setattr(npa, "controler_format", controle)
    run = "20261012-110014-notations-jouet"
    with pytest.raises(GardeArret, match="format chargé hors ligne ≠ format contrôlé au début du run"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json", "notations-jouet-8B-decisives.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "chargement du juge jouet-3B" and r["partiel"]["juges"]["jouet-8B"]["statut"] == "écrit"


def test_echeance_du_3b_le_8b_reste_ecrit(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)
    run = "20261012-110015-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 600, "jouet-3B": 1e-9}), depot, run, None, str(f),
                          autoriser_depot_sale=True)
    assert {n: j["statut"] for n, j in resume["juges"].items()} == {"jouet-8B": "écrit", "jouet-3B": "échu"}
    assert resume["juges"]["jouet-3B"]["lots_faits"] == 0
    assert _fichiers(depot, run) == ["notations-jouet-8B-decisives.json", "resume.json"]


def test_8b_echu_apres_un_lot_sans_fichier_partiel(depot, monkeypatch, capsys):
    """Horloge du lanceur avancée de 2 000 s à chaque lot : le 8B (échéance 1 500 s) fait un lot, puis échoit ; sa
    sortie partielle n'est jamais écrite ; le 3B note ; la ligne de fin consigne « échu » et « 1/2 »."""
    import time as vrai_temps
    from types import SimpleNamespace
    f, _ = _pilote_arrete(depot, monkeypatch)
    decalage = [0.0]
    monkeypatch.setattr(npa, "time", SimpleNamespace(perf_counter=lambda: vrai_temps.perf_counter() + decalage[0]))
    vrai = npa.noter_ensembles

    def noter(*a, **k):
        sortie = vrai(*a, **k)
        decalage[0] += 2000.0
        return sortie

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110016-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 1500, "jouet-3B": 23000}, duree_globale_s=23000),
                          depot, run, None, str(f), autoriser_depot_sale=True)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 1
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"
    # aucun compte de jetons ni de réponses consigné pour le juge échu ; le juge écrit garde ses descriptifs
    assert set(resume["juges"]["jouet-8B"]) == {"lots", "lots_faits", "statut", "duree_s", "memoire_pic_gio"}
    assert resume["juges"]["jouet-3B"]["jetons_generes"] > 0
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "resume.json"]
    err = capsys.readouterr().err
    assert "juge=jouet-8B fin=échu lots_faits=1/2" in err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ") and " lot=" in x]
    assert lignes and all(set(k.split("=")[0] for k in x.split()[2:]) == {"juge", "lot", "duree_s"} for x in lignes)


def test_panne_autre_que_garde_consignee_puis_propagee(depot, monkeypatch):
    """Une panne de la bibliothèque (mémoire de la carte, par exemple) est consignée dans `arret.json`, avec son
    motif, puis propagée (R5)."""
    f, _ = _pilote_arrete(depot, monkeypatch)

    def noter(*a, **k):
        raise RuntimeError("CUDA out of memory (essai)")

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110017-notations-jouet"
    with pytest.raises(RuntimeError, match="CUDA out of memory"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["motif"] == "RuntimeError: CUDA out of memory (essai)" and r["etape"] == "notations decisives par jouet-8B"


def test_term_puis_autre_exception_le_term_fait_foi(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)

    def noter(*a, **k):
        gardes.SIGNAL_TERM_RECU.append(15)
        raise RuntimeError("exception d'une bibliothèque après le signal (essai)")

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110018-notations-jouet"
    with pytest.raises(GardeArret, match="signal TERM reçu"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["motif"].startswith(gardes.MOTIF_TERM) and "RuntimeError" in r["motif"]


def test_panne_du_prechargement_du_3b(depot, monkeypatch):
    f, _ = _pilote_arrete(depot, monkeypatch)

    def precharger(config):
        raise GardeArret("préchargement du juge jouet-3B : fichier essentiel absent (essai)")

    monkeypatch.setattr(npa, "precharger_juges", precharger)
    run = "20261012-110019-notations-jouet"
    with pytest.raises(GardeArret, match="préchargement"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    assert verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]["etape"] == "préchargement des juges"


def _horloge_avancee(monkeypatch):
    """Horloge du lanceur simulée : le temps réel plus un décalage que le test avance à volonté."""
    import time as vrai_temps
    from types import SimpleNamespace
    decalage = [0.0]
    monkeypatch.setattr(npa, "time", SimpleNamespace(perf_counter=lambda: vrai_temps.perf_counter() + decalage[0]))
    return decalage


def test_echeance_du_3b_ancree_a_son_premier_lot(depot, monkeypatch):
    """L'échéance du 3B court depuis son premier lot, non depuis le début du run (contre-lecture R2, angle « code du
    lanceur ») : 2 000 s passent pendant chaque lot du 8B ; le 3B (1 500 s) note quand même. Un 3B ancré au début du
    run échoirait sans aucun lot."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    decalage = _horloge_avancee(monkeypatch)
    vrai = npa.noter_ensembles

    def noter(*a, **k):
        sortie = vrai(*a, **k)
        if all(x["cle"].startswith("juge-jouet-8B/") for x in sortie):
            decalage[0] += 2000.0
        return sortie

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    run = "20261012-110020-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 23000, "jouet-3B": 1500}, duree_globale_s=23000),
                          depot, run, None, str(f), autoriser_depot_sale=True)
    assert decalage[0] >= 4000.0
    assert {n: j["statut"] for n, j in resume["juges"].items()} == {"jouet-8B": "écrit", "jouet-3B": "écrit"}


def test_echeance_du_8b_ancree_au_debut_du_run(depot, monkeypatch):
    """L'échéance du 8B court depuis le début du run, chargement compris : 2 000 s passent pendant le chargement de
    l'agent ; le 8B (1 500 s) échoit sans aucun lot, le 3B note. Un 8B ancré à son premier lot noterait."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    decalage = _horloge_avancee(monkeypatch)
    vrai = npa.charger_modele_et_format
    appels = []

    def charger(*a, **k):
        appels.append(1)
        sortie = vrai(*a, **k)
        if len(appels) == 1:                                     # chargement de l'agent (le 8B)
            decalage[0] += 2000.0
        return sortie

    monkeypatch.setattr(npa, "charger_modele_et_format", charger)
    run = "20261012-110021-notations-jouet"
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 1500, "jouet-3B": 23000}, duree_globale_s=23000),
                          depot, run, None, str(f), autoriser_depot_sale=True)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 0
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"
    assert _fichiers(depot, run) == ["notations-jouet-3B-decisives.json", "resume.json"]


def test_etat_et_debut_du_run_avant_le_manifeste(depot, monkeypatch):
    """L'état du run et son début sont calculés avant le manifeste (vérification courte du code, second tour, constat
    1) : l'empreinte de la configuration n'est jamais calculée une fois le dossier du run créé ; 2 000 s qui passent
    pendant la création du manifeste comptent dans l'échéance du 8B (1 500 s), qui échoit sans aucun lot."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    decalage = _horloge_avancee(monkeypatch)
    run = "20261012-110023-notations-jouet"
    vu, vraie_empreinte, vrai_creer = [], npa.empreinte_config, npa.creer_manifeste

    def empreinte(*a, **k):
        vu.append((depot / "runs" / run).exists())
        return vraie_empreinte(*a, **k)

    def creer(*a, **k):
        sortie = vrai_creer(*a, **k)
        decalage[0] += 2000.0
        return sortie

    monkeypatch.setattr(npa, "empreinte_config", empreinte)
    monkeypatch.setattr(npa, "creer_manifeste", creer)
    resume = npa.executer(_config(duree_max_juges_s={"jouet-8B": 1500, "jouet-3B": 23000}, duree_globale_s=23000),
                          depot, run, None, str(f), autoriser_depot_sale=True)
    assert vu and not any(vu)
    assert resume["juges"]["jouet-8B"]["statut"] == "échu" and resume["juges"]["jouet-8B"]["lots_faits"] == 0
    assert resume["juges"]["jouet-3B"]["statut"] == "écrit"


def test_panne_au_chargement_du_8b_consignee_sous_son_etape(depot, monkeypatch):
    """Une panne au chargement de l'agent (le 8B : téléchargement compris) est consignée sous l'étape « chargement du
    juge jouet-8B », avec le type et le message de l'exception ; aucun fichier de notations (cas sain de l'étape « contrôle
    du format » : test_format_different_du_pilote_arrete)."""
    f, _ = _pilote_arrete(depot, monkeypatch)

    def charger(*a, **k):
        raise OSError("panne simulée du téléchargement (essai)")

    monkeypatch.setattr(npa, "charger_modele_et_format", charger)
    run = "20261012-110022-notations-jouet"
    with pytest.raises(OSError, match="téléchargement"):
        npa.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "chargement du juge jouet-8B" and r["motif"] == "OSError: panne simulée du téléchargement (essai)"


def test_memes_notations_que_le_lanceur_du_pilote(depot, monkeypatch):
    """Équivalence de bout en bout (contre-lecture R2) : à la même entropie, un pilote jouet complet (lanceur du pilote)
    et les notations refaites sur le même pilote arrêté pendant ses notations décisives rendent, clé à clé, les mêmes
    réponses, scores, jetons et ensembles notés ; épisodes A, B et C (e0 noté deux fois, e1), dernier lot partiel."""
    from controle_ia.manifeste import creer_manifeste as vrai_creer
    entropie = 20261012
    monkeypatch.setattr(lp, "creer_manifeste", lambda *a, **k: vrai_creer(*a, **{**k, "entropie": entropie}))
    vrai_jouer = lp.jouer_pilote

    def jouer(*a, **k):
        fiches, vecteurs, cn = vrai_jouer(*a, **k)
        for x in fiches:
            x["bilan"]["ensemble"] = f"PROPOSAL 1: idée {x['episode']}"
        return fiches, vecteurs, cn

    monkeypatch.setattr(lp, "jouer_pilote", jouer)
    # une tâche, lots de 2 : trois notations par juge (A, B et C), dernier lot d'une seule (lots de 4 : coûteux en jouet)
    cfg = {**_config_lanceur(), "episodes_par_tache": 2, "episodes_decisifs": [0, 1], "episodes_notes_deux_fois": [0],
           "lot_juge": 2}
    f = depot / "taches-une.json"
    f.write_text(json.dumps({"taches": [dict(TACHES[0], cibles=CIBLES_TEST)]}), encoding="utf-8")
    sceller(f)
    committer(depot)
    complet = "20261012-100003-pilote-complet"
    lp.executer(cfg, depot, complet, None, str(f), autoriser_depot_sale=True)
    vrai_noter = lp.noter_ensembles

    def noter_en_panne(*a, **k):
        raise GardeArret("limite de durée dépassée pendant les notations")

    monkeypatch.setattr(lp, "noter_ensembles", noter_en_panne)
    arrete = "20261012-100004-pilote-arrete"
    with pytest.raises(GardeArret):
        lp.executer(cfg, depot, arrete, None, str(f), autoriser_depot_sale=True)
    monkeypatch.setattr(lp, "noter_ensembles", vrai_noter)
    run = "20261012-110020-notations-jouet"
    c = {**{k: cfg[k] for k in npa.CLES_EGALES_AU_PILOTE}, "mode": "jouet", "run_pilote": arrete,
         "duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 600}, "duree_globale_s": 1200,
         "notations_attendues_par_juge": 3}
    resume = npa.executer(c, depot, run, None, str(f), autoriser_depot_sale=True)
    assert {n: (j["statut"], j["lots"]) for n, j in resume["juges"].items()} == {"jouet-8B": ("écrit", 2),
                                                                                  "jouet-3B": ("écrit", 2)}
    champs = ("cle", "reponse", "score", "jetons_reponse", "tronquee", "ensemble_sha256")
    for juge in ("jouet-8B", "jouet-3B"):
        a, b = (verifier_resultat(depot, depot / "diag" / r / f"notations-{juge}-decisives.json")["resultat"]
                ["notations"] for r in (complet, run))
        assert len(a) == len(b) == 3
        assert [{k: x[k] for k in champs} for x in a] == [{k: x[k] for k in champs} for x in b]
        assert sorted({x["cle"].split("/")[2] for x in b}) == ["e0", "e1"]
