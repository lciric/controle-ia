"""Pilote de l'environnement (a) (T0.5), sur modèle jouet : plan des épisodes, jeu par lots, notation, appariement."""
from __future__ import annotations

import json

import numpy as np
import pytest
import torch

from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.manifeste import generateur, graines
from controle_ia.scellement import sceller

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FMT = FormatChat(TOK, fins={TOK.convert_tokens_to_ids("<|im_end|>"), TOK.eos_token_id})
CONFIG = {"N": 1, "T": 2, "episodes_par_tache": 2, "lot": 3, "max_nouveaux": 6, "temperature": 1.0,
          "couches": [0, 1, 2], "fraction_equivalence": 0.5, "statistique_equivalence": "max",
          "tolerance_equivalence": 1e-4, "positions_min_controle_negatif": 4, "actions_min_controle_negatif": 10,
          "fraction_min_controle_negatif": 0.95}
TACHES = [{"identifiant": "2506.00001v1", "questions": "Why do routers matter?",
           "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": []}},
          {"identifiant": "2506.00002v1", "questions": "How to calibrate?", "classification": None}]

CIBLES_TEST = {"controls": [{"id": f"C{k}", "description": d} for k, d in
                            enumerate(("a dense baseline", "an ablation of the router", "a matched-compute run"), 1)],
               "fruitful_directions": [{"id": "F1", "description": "top-2 routing"}], "sterile_directions": []}


def _modele():
    return modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def _generateurs(plan, entropie=7):
    g = graines([e for e, _ in plan], entropie)
    return {e: generateur(g[e]) for e, _ in plan}


def test_config_incomplete_arrete():
    pa.exiger_config(CONFIG)
    with pytest.raises(GardeArret, match="incomplète"):
        pa.exiger_config({k: v for k, v in CONFIG.items() if k != "lot"})


def test_charger_taches(tmp_path):
    f = tmp_path / "taches.json"
    f.write_text(json.dumps({"taches": TACHES}), encoding="utf-8")
    with pytest.raises(GardeArret):
        pa.charger_taches(f)  # non scellé
    sceller(f)
    assert [t["identifiant"] for t in pa.charger_taches(f)] == ["2506.00001v1", "2506.00002v1"]
    for contenu, motif in [({"taches": TACHES + TACHES[:1]}, "double"),
                           ({"taches": [{"identifiant": "x", "questions": " "}]}, "sans énoncé")]:
        g = tmp_path / f"t-{motif[:4]}.json"
        g.write_text(json.dumps(contenu), encoding="utf-8")
        sceller(g)
        with pytest.raises(GardeArret, match=motif):
            pa.charger_taches(g)


def test_plan_et_graines_deterministes():
    plan = pa.plan_des_episodes(TACHES, 2)
    assert [e for e, _ in plan] == ["2506.00001v1/e0", "2506.00001v1/e1", "2506.00002v1/e0", "2506.00002v1/e1"]
    a = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    b = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    assert a == b and sorted(a) == [(i, t) for i in range(2) for t in range(3)]
    with pytest.raises(GardeArret):
        pa.plan_des_episodes(TACHES, 0)


def test_jouer_pilote_par_lots_et_rejeu():
    plan = pa.plan_des_episodes(TACHES, 2)
    m = _modele()
    fiches, vecteurs, cn = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["episode"] for f in fiches] == [e for e, _ in plan]
    assert cn["lecture"] in ("conforme", "non concluant") and cn["positions_min"] == 4
    a0 = fiches[0]["actions"][0]
    assert a0["texte"] and len(a0["ids"]) == fiches[0]["jetons_par_action"][0] and a0["fin"] - a0["debut"] == len(a0["ids"])
    eq = next(f["equivalence"] for f in fiches if f["equivalence"]["actions"])
    assert set(eq["controle_negatif_zone_generee"]) == set(eq["actions"]) == set(eq["longueurs_contexte"])
    assert all(f["bilan"]["actions"] == 2 for f in fiches) and sum(len(f["equivalence"]["actions"]) for f in fiches) > 0
    assert set(vecteurs) == {f"{e}|{c}" for e, _ in plan for c in CONFIG["couches"]}
    assert vecteurs["2506.00001v1/e0|1"].shape == (1, 2, 32) and vecteurs["2506.00001v1/e0|1"].dtype == np.float16
    rejeu, _, _ = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["empreintes"] for f in rejeu] == [f["empreintes"] for f in fiches]


def test_controle_negatif_du_pilote_cas_sain_et_artefacts():
    """R5, dans le chemin du pilote : cas sain (contrôle négatif vu) ; artefact 1 : tolérance aberrante, la garde est
    aveugle au décalage d'un jeton (arrêt de phase) ; artefact 2 : défaut D1 injecté (arrêt de la garde immédiate)."""
    plan = pa.plan_des_episodes(TACHES, 2)
    sain = {**CONFIG, "fraction_equivalence": 1.0, "positions_min_controle_negatif": 1, "actions_min_controle_negatif": 1}
    _, _, cn = pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), sain, garder_vecteurs=False)
    assert cn["lecture"] == "conforme" and cn["comparables"] >= 1 and cn["fraction"] >= 0.95
    with pytest.raises(GardeArret, match="aveugle au décalage"):
        pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), {**sain, "tolerance_equivalence": 1e9},
                        garder_vecteurs=False)
    with pytest.raises(GardeArret):
        pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), sain, garder_vecteurs=False, decalage_positions=1)


def test_jouer_pilote_generateur_manquant_arrete():
    plan = pa.plan_des_episodes(TACHES, 1)
    with pytest.raises(GardeArret, match="générateurs absents"):
        pa.jouer_pilote(_modele(), FMT, plan, {}, CONFIG)


def test_noter_ensembles_sans_imputation():
    demandes = [{"cle": f"j{k}", "questions": "Why?", "ensemble": "PROPOSAL 1: x", "classification": None,
                 "variante": v} for k, v in enumerate(["b0", "b*"])]
    sorties = pa.noter_ensembles(_modele(), FMT, demandes, {"j0": 1, "j1": 2}, lot=2, max_nouveaux=5, temperature=1.0)
    assert [s["cle"] for s in sorties] == ["j0", "j1"]
    assert all(s["score"] is None and s["anomalies"] and s["jetons_reponse"] <= 5 for s in sorties)
    with pytest.raises(GardeArret, match="limite de durée"):           # échéance à chaque lot (D-22 ; vérification 3, F-2)
        pa.noter_ensembles(_modele(), FMT, demandes, {"j0": 1, "j1": 2}, lot=2, max_nouveaux=5, temperature=1.0,
                           echeance=0.0)


def test_logits_independants_du_remplissage():
    m = _modele()
    contextes = [FMT.ouverture("s", "court"), FMT.ouverture("système plus long", "observation bien plus longue")]
    lot = pa.logits_derniere_position(m, contextes, TOK.pad_token_id)
    seuls = torch.cat([pa.logits_derniere_position(m, [c], TOK.pad_token_id) for c in contextes])
    assert torch.allclose(lot, seuls, atol=1e-5)
    with pytest.raises(GardeArret):
        pa.logits_derniere_position(m, [[]], TOK.pad_token_id)


def test_jetons_oui_non():
    with pytest.raises(GardeArret, match="un seul jeton"):
        pa.jetons_oui_non(TOK)  # tokeniseur par caractères : « Yes » fait trois jetons

    class Tok:
        def encode(self, s, add_special_tokens=False):
            return {"Yes": [7], "No": [9]}[s]

    assert pa.jetons_oui_non(Tok()) == (7, 9)


def test_apparier_probabilites(monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non", lambda tok: (TOK.convert_tokens_to_ids("Y"), TOK.convert_tokens_to_ids("N")))
    paires = [{"cle": f"p{k}", "proposition": "Train a dense baseline.", "cible": c, "famille": "controls"}
              for k, c in enumerate(["a dense baseline", "an ablation"])]
    s = pa.apparier(_modele(), FMT, paires, lot=2)
    assert [x["cle"] for x in s] == ["p0", "p1"] and all(0.0 <= x["p_oui"] <= 1.0 and x["masse_oui_non"] > 0 for x in s)
    with pytest.raises(GardeArret, match="sans famille"):              # aucune question par défaut (D-15)
        pa.apparier(_modele(), FMT, [{k: v for k, v in paires[0].items() if k != "famille"}], lot=2)
    with pytest.raises(GardeArret, match="limite de durée"):           # échéance contrôlée à chaque lot (D-6)
        pa.apparier(_modele(), FMT, paires, lot=2, echeance=0.0)


# --- analyse -----------------------------------------------------------------------------------------------

from controle_ia.environnements import analyse_pilote as ap  # noqa: E402


def _simuler(n, sb=2.0, sd=1.0, se=1.5, graine=3):
    r = np.random.default_rng(graine)
    beta, d1, d2 = r.normal(0, sb, n), r.normal(0, sd, n), r.normal(0, sd, n)
    e = r.normal(0, se, (3, n))
    return 50 + beta + d1 + e[0], 50 + beta + d1 + e[1], 50 + beta + d2 + e[2]


def test_decomposition_retrouve_les_composantes_simulees():
    d = ap.decomposition_variance(*_simuler(40000))
    vrai = {"tache": 4.0, "generation": 1.0, "juge": 2.25}
    for k, v in vrai.items():
        assert d["composantes"][k] == pytest.approx(v, rel=0.06), k
    assert d["parts"]["juge"] == pytest.approx(2.25 / 7.25, abs=0.02) and d["taches_incompletes"] == 0


def test_decomposition_sans_imputation_et_gardes():
    a, b, c = (x[:10].copy() for x in _simuler(10))
    a[0] = np.nan
    d = ap.decomposition_variance(a, b, c)
    assert d["taches"] == 9 and d["taches_incompletes"] == 1
    with pytest.raises(GardeArret, match="alignées"):
        ap.decomposition_variance(a, b[:5], c)
    with pytest.raises(GardeArret, match="impossible"):
        ap.decomposition_variance([1.0, np.nan], [1.0, 2.0], [1.0, 2.0])


def test_intervalles_contiennent_la_valeur_simulee():
    iv = ap.intervalles_parts_comptes(*_simuler(400, graine=8), tirages=300, rng=np.random.default_rng(1))
    assert iv["bornes"]["juge"][0] < 2.25 / 7.25 < iv["bornes"]["juge"][1] and iv["ecartes"] == 0


def test_somme_des_composantes_identite_et_juge_constant():
    """Contre-lecture 2 du pilote : la somme des composantes vaut (V̂[sA] + V̂[sB]) / 2 par construction (D-1) ; un juge
    aux notes constantes rend la différence appariée impossible, par une garde (D-13)."""
    a, b, c = _simuler(80, graine=5)
    d = ap.decomposition_complete(a, b, c)
    assert d["composantes"]["totale"] == pytest.approx((np.var(a, ddof=1) + np.var(b, ddof=1)) / 2, rel=1e-12)
    constant = np.full(80, 3.0)
    with pytest.raises(GardeArret, match="aucun tirage lisible"):
        ap.difference_appariee((a, b, c), (constant, constant, constant), 50, np.random.default_rng(2))
    with pytest.raises(GardeArret, match="aucun tirage lisible"):
        ap.intervalles_parts_comptes(constant, constant, constant, 50, np.random.default_rng(2))
    with pytest.raises(GardeArret, match="tâches complètes pour les deux juges"):
        ap.difference_appariee((a[:2], b[:2], c[:2]), (a[:2], b[:2], c[:2]), 50, np.random.default_rng(2))
    with pytest.raises(GardeArret, match="aucune cible"):
        ap.couverture({}, [1], [])


def test_kappa():
    x = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=bool)
    assert ap.kappa_cohen(x, x) == 1.0
    assert ap.kappa_cohen(x, ~x) == -1.0
    with pytest.raises(GardeArret, match="indéfini"):
        ap.kappa_cohen([1, 1], [1, 1])
    with pytest.raises(GardeArret):
        ap.kappa_cohen([1, 0], [1])


def test_couverture():
    p = {(1, "C1"): 0.9, (1, "C2"): 0.2, (2, "C1"): 0.1, (2, "C2"): 0.6}
    assert ap.couverture(p, [1, 2], ["C1", "C2"]) == {"part": 1.0, "couvertes": ["C1", "C2"]}
    assert ap.couverture(p, [1], ["C1", "C2"])["part"] == 0.5
    with pytest.raises(GardeArret, match="absentes"):
        ap.couverture(p, [1, 3], ["C1"])


# --- lanceur (mode jouet, dépôt jetable) -------------------------------------------------------------------

from controle_ia.environnements import lancer_pilote_a as lp  # noqa: E402
from conftest import committer  # noqa: E402


def _config_lanceur():
    return {**CONFIG, "episodes_par_tache": 2, "episodes_notes_deux_fois": [0], "episodes_decisifs": [0],
            "lot_juge": 2,
            "max_nouveaux_juge": 6, "temperature_juge": 1.0, "variante_juge": "b0", "lot_appariement": 4,
            "duree_max_s": 600, "mode": "jouet", "agent": {"nom": "agent-jouet"}, "noyau_attention": "math", "fils": 1,
            "juges": [{"nom": "jouet-8B", "meme_modele_que_agent": True, "sert_a_l_appariement": True},
                      {"nom": "jouet-3B", "meme_modele_que_agent": False, "sert_a_l_appariement": False}]}


def test_lanceur_de_bout_en_bout_en_mode_jouet(depot, monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non",
                        lambda tok: (tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")))
    taches = [dict(t, cibles=CIBLES_TEST) for t in TACHES]
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sceller(f)
    committer(depot)
    resume = lp.executer(_config_lanceur(), depot, "20261006-170000-pilote-jouet", None, str(f),
                         autoriser_depot_sale=True)
    assert resume["episodes"] == 4 and resume["actions"] == 8
    assert set(resume["notations"]) == {"jouet-8B", "jouet-3B"}
    d = depot / "diag" / "20261006-170000-pilote-jouet"
    assert {p.name for p in d.glob("*.json")} >= {"episodes.json", "notations-jouet-8B-decisives.json",
                                                  "notations-jouet-8B-descriptives.json",
                                                  "notations-jouet-3B-decisives.json",
                                                   "appariements.json", "resume.json"}
    assert (depot / "donnees" / "20261006-170000-pilote-jouet" / "vecteurs-par-action.npz.sha256").exists()
    with pytest.raises(GardeArret, match="R12"):
        lp.executer(_config_lanceur(), depot, "20261006-170000-pilote-jouet", None, str(f), autoriser_depot_sale=True)


def _taches_scellees(depot):
    taches = [dict(t, cibles=CIBLES_TEST) for t in TACHES]
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sha = sceller(f)
    return f, sha


def _prereg_pilote(depot, commit, config, sha_taches, entropie=4242, nom="prereg-pilote.md"):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    lignes = [f"- Commit du code d'analyse : `{commit}`",
              f"- Configuration du pilote (empreinte canonique) : `{lp.empreinte_config(config)}`",
              f"- Tâches du pilote : `{sha_taches}`", f"- Entropie : `{entropie}`"]
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _commit(depot):
    import subprocess
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def test_lanceur_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    """R1, R5 : un run avec préenregistrement ne part que si le commit, la configuration, les tâches et l'entropie
    sont ceux que cite le préenregistrement ; sinon arrêt avant tout manifeste."""
    monkeypatch.setattr(pa, "jetons_oui_non",
                        lambda tok: (tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")))
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)  # code importé du vrai dépôt (testé ailleurs)
    f, sha = _taches_scellees(depot)
    committer(depot)
    commit, config = _commit(depot), _config_lanceur()
    sain = _prereg_pilote(depot, commit, config, sha)
    autre_config = _prereg_pilote(depot, commit, dict(config, lot_juge=3), sha, nom="p-config.md")
    autres_taches = _prereg_pilote(depot, commit, config, "c" * 64, nom="p-taches.md")
    (depot / "prereg" / "p-sans.md").write_text(f"- Commit du code d'analyse : `{commit}`\n", encoding="utf-8")
    committer(depot)                                            # préenregistrements : hors de l'arbre gelé
    for p, motif in ((autre_config, "configuration .* citée"), (autres_taches, "tâches .* citées"),
                     (depot / "prereg" / "p-sans.md", "ne cite pas la configuration")):
        with pytest.raises(GardeArret, match=motif):
            lp.executer(config, depot, "20261006-170002-pilote-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261006-170002-pilote-jouet").exists()
    resume = lp.executer(config, depot, "20261006-170003-pilote-jouet", str(sain), str(f),
                         autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit and resume["taches_sha256"] == sha
    m = json.loads((depot / "runs" / "20261006-170003-pilote-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-pilote.md"
    assert {g["entropie"] for g in m["graines"].values()} == {"4242"}
    (depot / "nouveau_code.py").write_text("x = 1\n")         # artefact : arbre gelé modifié après le commit cité
    committer(depot)
    with pytest.raises(GardeArret, match="arbre gelé"):
        lp.executer(config, depot, "20261006-170004-pilote-jouet", str(sain), str(f),
                    autoriser_depot_sale=True)


def test_lanceur_reel_sans_preenregistrement_arrete(depot):
    c = dict(_config_lanceur(), mode="reel")
    with pytest.raises(GardeArret, match="R1"):
        lp.executer(c, depot, "20261006-170005-x", None, "inexistant.json")
    assert not (depot / "runs").exists()


def test_lanceur_arret_consigne_apres_le_manifeste(depot, monkeypatch):
    """Une panne après le manifeste laisse un arret.json scellé (étape, motif, partiel), puis se propage."""
    from controle_ia.manifeste import verifier_resultat

    def panne(*a, **k):
        raise GardeArret("panne simulée du juge")
    monkeypatch.setattr(lp, "noter_ensembles", panne)
    # le modèle jouet ne produit aucune proposition valide : une demande de notation factice fait appeler le juge
    monkeypatch.setattr(lp, "demandes_de_notation", lambda fiches, par_id, config, nom: [
        {"cle": f"juge-{nom}/{fiches[0]['episode']}/passe-0", "episode": fiches[0]["episode"], "questions": "q",
         "ensemble": "PROPOSAL 1: x", "classification": None, "variante": "b0"}])
    f, _ = _taches_scellees(depot)
    committer(depot)
    with pytest.raises(GardeArret, match="panne simulée"):
        lp.executer(_config_lanceur(), depot, "20261006-170006-pilote-jouet", None, str(f))
    arret = depot / "diag" / "20261006-170006-pilote-jouet" / "arret.json"
    corps = verifier_resultat(depot, arret)
    r = corps["resultat"]
    assert r["etape"] == "notations decisives par jouet-8B" and "panne simulée" in r["motif"]
    assert r["partiel"]["episodes_ecrits"] == 4
    assert (depot / "diag" / "20261006-170006-pilote-jouet" / "episodes.json").exists()


def test_jetons_jouet_et_lanceur_sans_substitution(depot, monkeypatch):
    """Le mode jouet apparie avec « Y » et « N » sans substituer `jetons_oui_non` (répétition de l'instance) ; le
    modèle jouet ne produit pas de proposition valide : deux paires sont fournies au lanceur."""
    assert pa.jetons_jouet(TOK) == (TOK.convert_tokens_to_ids("Y"), TOK.convert_tokens_to_ids("N"))
    with pytest.raises(GardeArret, match="un seul jeton"):
        pa.jetons_oui_non(TOK)                                  # artefact : sans la paire jouet, l'appariement arrête
    monkeypatch.setattr(lp, "paires_d_appariement", lambda fiches, par_id: [
        {"cle": "t/e0/1/C1", "proposition": "a dense baseline", "cible": "a dense baseline", "famille": "controls"},
        {"cle": "t/e0/1/C2", "proposition": "x", "cible": "y", "famille": "controls"}])
    f, _ = _taches_scellees(depot)
    committer(depot)
    resume = lp.executer(_config_lanceur(), depot, "20261006-170007-pilote-jouet", None, str(f))
    app = json.loads((depot / "diag" / "20261006-170007-pilote-jouet" / "appariements.json").read_text(encoding="utf-8"))
    assert resume["episodes"] == 4 and app["resultat"]["appariements"]
    assert all(0.0 <= a["p_oui"] <= 1.0 for a in app["resultat"]["appariements"])


def test_lanceur_ordre_des_etapes_arret_pendant_d(depot, monkeypatch):
    """D-6 (vérification 3, F-2 ; relectures des différentiels, Y-5 et V-4) : notations décisives des deux juges, puis
    appariement des propositions, puis base « énoncé seul », puis notations descriptives de D, dans cet ordre (chaque
    appariement est consigné à son appel). Un arrêt pendant les notations de D laisse écrits les épisodes, les notations
    décisives et l'appariement ; `arret.json` consigne l'étape."""
    from controle_ia.manifeste import verifier_resultat
    vrai_noter, appels = lp.noter_ensembles, []

    def noter(m, fmt, dem, graines_, *a, **k):
        descriptives = [d for d in dem if d["episode"].endswith("/e1")]
        appels.append("descriptives" if descriptives else "decisives")
        if descriptives:
            raise GardeArret("arrêt simulé pendant les notations de D")
        return vrai_noter(m, fmt, dem, graines_, *a, **k)

    # le modèle jouet ne forme pas d'ensemble : des demandes et une paire factices font appeler les juges et l'appariement
    monkeypatch.setattr(lp, "demandes_de_notation", lambda fiches, par_id, config, nom: [
        {"cle": f"juge-{nom}/{x['episode']}/passe-{p}", "episode": x["episode"], "questions": "q",
         "ensemble": "PROPOSAL 1: x", "classification": None, "variante": "b0"}
        for x in fiches for p in range(lp.passes_de(x["episode"], config))])
    monkeypatch.setattr(lp, "noter_ensembles", noter)
    def paires(fiches, par_id):
        appels.append("appariement")
        return [{"cle": "t/e0/1/C1", "proposition": "a dense baseline", "cible": "a dense baseline",
                 "famille": "controls"}]
    monkeypatch.setattr(lp, "paires_d_appariement", paires)
    vraie_enonce = lp.paires_enonce_seul

    def enonce_seul(taches):
        appels.append("enonce_seul")
        return vraie_enonce(taches)
    monkeypatch.setattr(lp, "paires_enonce_seul", enonce_seul)
    f, _ = _taches_scellees(depot)
    committer(depot)
    run = "20261006-170008-pilote-jouet"
    with pytest.raises(GardeArret, match="arrêt simulé pendant les notations de D"):
        lp.executer(_config_lanceur(), depot, run, None, str(f))
    d = depot / "diag" / run
    assert appels == ["decisives", "decisives", "appariement", "enonce_seul", "descriptives"]
    assert {x.name for x in d.glob("*.json")} == {"episodes.json", "notations-jouet-8B-decisives.json",
                                                  "notations-jouet-3B-decisives.json", "appariements.json",
                                                  "arret.json"}
    r = verifier_resultat(depot, d / "arret.json")["resultat"]
    assert r["etape"] == "notations descriptives par jouet-8B" and r["partiel"]["appariement_ecrit"] == "jouet-8B"


def test_signal_term_devient_un_arret_consigne():
    with pytest.raises(GardeArret, match="TERM"):
        lp._signal_term(15, None)


def test_lanceur_configuration_incomplete(depot):
    c = _config_lanceur()
    del c["lot_juge"]
    with pytest.raises(GardeArret, match="incomplète"):
        lp.executer(c, depot, "20261006-170001-x", None, "inexistant.json")


@pytest.mark.parametrize("cle, valeur, motif", [
    ("noyau_attention", "flash", "noyau d'attention"), ("noyau_attention", "À REMPLIR", "noyau d'attention"),
    ("duree_max_s", "À REMPLIR", "duree_max_s"), ("duree_max_s", 16_200, "duree_max_s"),
    ("duree_max_s", 15_001, "duree_max_s"), ("duree_max_s", 0, "duree_max_s"),
    ("duree_max_s", True, "duree_max_s"), ("mode", "essai", "mode")])
def test_lanceur_noyau_et_duree_valides_avant_le_manifeste(depot, cle, valeur, motif):
    """Contre-lecture 2 du pilote, D-14 et D-22, puis relecture du différentiel, Y-7 : noyau inconnu, durée non
    numérique ou hors de ]0 ; 15 000] : arrêt avant tout manifeste (cas sain : les autres tests du lanceur, et la borne
    de 15 000 s ci-dessous)."""
    c = dict(_config_lanceur(), **{cle: valeur})
    with pytest.raises(GardeArret, match=motif):
        lp.executer(c, depot, "20261006-170010-x", None, "inexistant.json")
    assert not (depot / "runs").exists()


def test_lanceur_duree_a_la_borne_acceptee(depot, monkeypatch):
    """Y-7, cas sain : 15 000 s, plafond de la formule, passe toutes les gardes d'avant le manifeste ; une sentinelle à
    la place de la création du manifeste le prouve, où que soit la garde de durée avant lui (V-3, Z-6 (d))."""
    class ManifesteAtteint(Exception):
        pass

    def sentinelle(*a, **k):
        raise ManifesteAtteint
    monkeypatch.setattr(lp, "creer_manifeste", sentinelle)
    f, _ = _taches_scellees(depot)
    with pytest.raises(ManifesteAtteint):
        lp.executer(dict(_config_lanceur(), duree_max_s=15_000), depot, "20261006-170011-x", None, str(f))


def test_passes_et_demandes():
    c = _config_lanceur()
    assert lp.passes_de("2506.00001v1/e0", c) == 2 and lp.passes_de("2506.00001v1/e1", c) == 1
    fiches = [{"episode": "t/e0", "tache": "t", "bilan": {"ensemble": "PROPOSAL 1: x", "propositions": []}},
              {"episode": "t/e1", "tache": "t", "bilan": {"ensemble": "  ", "propositions": []}}]
    d = lp.demandes_de_notation(fiches, {"t": {"questions": "Q?"}}, c, "j")
    assert [x["cle"] for x in d] == ["juge-j/t/e0/passe-0", "juge-j/t/e0/passe-1"]


def test_reponse_tronquee_sans_score_meme_si_les_notes_se_lisent(monkeypatch):
    from controle_ia.environnements.rubrique import CRITERES

    texte = "\n".join(f"{nom}: {hi}" for nom, lo, hi in CRITERES)
    complet = pa.lire_notes(texte, CRITERES)
    assert complet.complete  # le texte porte toutes les notes
    fin = sorted(FMT.fins)[0]
    sorties_generees = {"avec_fin": [5, 6, fin], "sans_fin": [5, 6, 7]}
    monkeypatch.setattr(pa, "generer_lot", lambda modele, ctx, mx, t, g, fins, pad: (
        [sorties_generees["avec_fin"], sorties_generees["sans_fin"]], None))
    monkeypatch.setattr(FMT.tok, "decode", lambda ids, skip_special_tokens=True: texte)
    demandes = [{"cle": f"j{k}", "questions": "Why?", "ensemble": "PROPOSAL 1: x", "classification": None,
                 "variante": "b0"} for k in range(2)]
    a, b = pa.noter_ensembles(_modele(), FMT, demandes, {"j0": 1, "j1": 2}, lot=2, max_nouveaux=5, temperature=1.0)
    assert a["score"] is not None and not a["tronquee"]
    assert b["score"] is None and b["tronquee"] and any("tronquée" in x for x in b["anomalies"])


def test_lanceur_refuse_cibles_incompletes_et_invite_alteree(depot, monkeypatch):
    from controle_ia.environnements import lancer_pilote_a as lp

    with pytest.raises(GardeArret, match="cibles semées complètes"):
        lp.exiger_cibles([{"identifiant": "x", "questions": "q"}])
    with pytest.raises(GardeArret, match="moins de 3 contrôles"):
        lp.exiger_cibles([{"identifiant": "x", "cibles": dict(CIBLES_TEST, controls=CIBLES_TEST["controls"][:2])}])
    with pytest.raises(GardeArret, match="sans description"):
        lp.exiger_cibles([{"identifiant": "x", "cibles": dict(CIBLES_TEST, sterile_directions=[{"id": "S1"}])}])
    lp.exiger_cibles([{"identifiant": "x", "cibles": CIBLES_TEST}])
    lp.exiger_invites({"variante_juge": "b0"})
    from controle_ia.environnements import invites

    def refuse(ident, racine=None):
        raise GardeArret(f"invite {ident} : empreinte non conforme")

    monkeypatch.setattr(invites, "charger_invite", refuse)
    with pytest.raises(GardeArret, match="H1-classification"):
        lp.exiger_invites({"variante_juge": "b0"})


def test_le_juge_voit_la_classification():
    from controle_ia.environnements import lancer_pilote_a as lp

    fiches = [{"episode": f"{TACHES[0]['identifiant']}/e0", "tache": TACHES[0]["identifiant"],
               "bilan": {"ensemble": "PROPOSAL 1: x"}},
              {"episode": f"{TACHES[1]['identifiant']}/e1", "tache": TACHES[1]["identifiant"],
               "bilan": {"ensemble": "PROPOSAL 1: y"}}]
    demandes = lp.demandes_de_notation(fiches, {t["identifiant"]: t for t in TACHES},
                                       {"episodes_notes_deux_fois": [0], "variante_juge": "b0"}, "j")
    assert len(demandes) == 3  # e0 noté deux fois, e1 une fois
    assert "Paper type: Mostly experimental" in demandes[0]["classification"]
    assert demandes[2]["classification"] is None  # tâche sans classification


# --- analyse, brouillon 2 du pilote (contre-lecture 1, CL-5 à CL-14) ---------------------------------------------

def test_parts_tronquees_et_composante_negative():
    p = ap.parts_tronquees({"tache": -1.0, "generation": 1.0, "juge": 3.0})
    assert p == {"tache": 0.0, "generation": 0.25, "juge": 0.75}
    assert ap.parts_tronquees({"tache": -1.0, "generation": -1.0, "juge": 0.0})["juge"] != \
        ap.parts_tronquees({"tache": -1.0, "generation": -1.0, "juge": 0.0})["juge"]   # total nul : NaN
    d = ap.decomposition_complete(*_simuler(4000))
    assert d["parts_tronquees"]["juge"] == pytest.approx(d["parts"]["juge"], abs=1e-9)   # rien de négatif
    assert d["variance_observee_A"] == pytest.approx(d["composantes"]["totale"], rel=0.1)
    assert d["composantes_negatives"] == []


def test_intervalles_comptes_et_difference_appariee():
    iv = ap.intervalles_parts_comptes(*_simuler(400, graine=8), tirages=300, rng=np.random.default_rng(1))
    assert iv["bornes"]["juge"][0] < 2.25 / 7.25 < iv["bornes"]["juge"][1]
    assert iv["ecartes"] == 0 and not iv["reserve"]
    huit = _simuler(400, se=1.0, graine=8)
    trois = _simuler(400, se=3.0, graine=9)       # juge plus bruité
    d = ap.difference_appariee(huit, trois, tirages=300, rng=np.random.default_rng(2))
    assert d["difference"] > 0 and d["borne"][0] > 0 and d["taches"] == 400
    with pytest.raises(GardeArret, match="alignées"):
        ap.difference_appariee(huit, tuple(x[:10] for x in trois), tirages=10, rng=np.random.default_rng(2))
    with pytest.raises(GardeArret, match="intervalles impossibles"):
        ap.intervalles_parts_comptes([1.0, 2.0], [1.0, 2.0], [1.0, 2.0], tirages=5, rng=np.random.default_rng(0))


def test_tirages_ecartes_comptes():
    # deux tâches seulement : beaucoup de tirages dégénérés (variance nulle), comptés et non sautés en silence
    a, b, c = np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])
    iv = ap.intervalles_parts_comptes(a, b, c, tirages=200, rng=np.random.default_rng(0))
    assert iv["ecartes"] > 0 and iv["reserve"]


@pytest.mark.parametrize("part, borne, incompletes, attendu", [
    (0.5, 0.3, 0.0, "rubrique gardée"),
    (0.85, 0.7, 0.0, "plan B"),
    (0.85, 0.5, 0.0, "nœud"),
    (0.5, 0.3, 0.25, "plan B"),
    (float("nan"), 0.0, 0.0, "nœud"),
])
def test_regle_plan_b(part, borne, incompletes, attendu):
    assert ap.regle_plan_b(part, borne, incompletes) == attendu


def test_tirage_stratifie_et_kappa_pondere():
    paires = [{"cle": f"p{i}", "tache": f"t{i % 10}", "famille": f, "oui_8b": i % 7 == 0}
              for i, f in enumerate(["controls"] * 70 + ["fruitful_directions"] * 70)]
    ech = ap.tirer_paires(paires, np.random.default_rng(3), par_strate=5)
    strates = {tuple(p["strate"]) for p in ech}
    assert len(ech) == 20 and len(strates) == 4
    for p in ech:   # poids = taille de la strate / nombre tiré
        n = sum(1 for q in paires if q["famille"] == p["famille"] and q["oui_8b"] == p["oui_8b"])
        assert p["poids"] == n / 5
    assert ech == ap.tirer_paires(paires, np.random.default_rng(3), par_strate=5)   # rejouable (R9)
    k = ap.kappa_pondere([True, True, False, False], [True, True, False, False], [1, 2, 3, 4])
    assert k["kappa"] == 1.0 and k["accord_positif"] == 1.0 and k["accord_negatif"] == 1.0
    assert ap.kappa_pondere([True, True], [True, True], [1, 1])["kappa"] is None   # une seule classe : indéfini
    with pytest.raises(GardeArret, match="non alignés"):
        ap.kappa_pondere([True], [True, False], [1, 1])
    with pytest.raises(GardeArret, match="non alignés"):
        ap.kappa_pondere([True], [True], [0])
    for p in ech:
        p["reference"] = p["oui_8b"]
    iv = ap.intervalle_kappa_par_tache(ech, tirages=100, rng=np.random.default_rng(4))
    assert iv["borne"] is not None and iv["borne"][0] <= 1.0


def test_masse_lisible():
    assert ap.masse_lisible([0.9] * 99 + [0.05])["lisible"]
    assert not ap.masse_lisible([0.9] * 90 + [0.05] * 10)["lisible"]
    assert not ap.masse_lisible([0.3] * 100)["lisible"]
    with pytest.raises(GardeArret, match="aucune paire"):
        ap.masse_lisible([])


def test_garde_du_format_au_debut_cas_sain_et_artefacts():
    """CL-25 : la transcription incrémentale coïncide avec le gabarit complet, pour l'agent et pour un juge ; en mode
    réel, le texte attendu dans l'ouverture est exigé et retrouvé ; un gabarit qui réécrit le passé arrête."""
    config = _config_lanceur()
    sain = lp.controler_format(FMT, {"nom": "agent-jouet"}, "agent", config)
    assert sain["verifie"] and sain["tours"] == 2 and sain["role"] == "agent"
    assert lp.controler_format(FMT, {"nom": "jouet-3B"}, "juge", config)["tours"] == 1
    with pytest.raises(GardeArret, match="texte attendu"):
        lp.controler_format(FMT, {"nom": "agent"}, "agent", dict(config, mode="reel"))
    with pytest.raises(GardeArret, match="ouverture sans"):
        lp.controler_format(FMT, {"nom": "agent", "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}, "agent",
                            config)

    class FormatFautif(FormatChat):
        def tour(self, debut, observation):            # artefact : un tour qui réécrit le début de la conversation
            return super().tour(debut, observation)[1:]

    with pytest.raises(GardeArret, match="format incrémental"):
        lp.controler_format(FormatFautif(TOK, fins=FMT.fins), {"nom": "agent"}, "agent", config)


def test_paires_enonce_seul():
    taches = [dict(t, cibles=CIBLES_TEST) for t in TACHES]
    paires = lp.paires_enonce_seul(taches)
    assert len(paires) == 2 * 4
    assert {p["famille"] for p in paires} == {"controls", "fruitful_directions"}
    assert paires[0]["cle"] == "2506.00001v1/enonce/C1" and paires[0]["proposition"] == TACHES[0]["questions"]


def test_lanceur_consigne_formats_et_enonce_seul(depot, monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non",
                        lambda tok: (tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")))
    f, _ = _taches_scellees(depot)
    committer(depot)
    lp.executer(_config_lanceur(), depot, "20261006-170010-pilote-jouet", None, str(f), autoriser_depot_sale=True)
    d = depot / "diag" / "20261006-170010-pilote-jouet"
    ep = json.loads((d / "episodes.json").read_text(encoding="utf-8"))["resultat"]
    assert set(ep["formats"]) == {"agent", "juge-jouet-8B", "juge-jouet-3B"}
    assert all(v["verifie"] for v in ep["formats"].values())
    assert ep["descriptifs"]["jetons_generes"] > 0
    app = json.loads((d / "appariements.json").read_text(encoding="utf-8"))["resultat"]
    assert len(app["enonce_seul"]) == 2 * 4 and app["descriptifs"]["paires"] == len(app["appariements"]) + 8
