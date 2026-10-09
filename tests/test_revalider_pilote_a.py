"""Revalidation courte de l'équivalence sur le domaine du pilote (T0.5), sur modèle jouet : gardes de configuration,
de tâches et de citations, lectures gelées (bras, chemin, audit, garde restreinte) et règle de choix, déroulé complet,
arrêt consigné qui garde un bras lu, panne de mémoire, rejeu ; cas sain et artefacts (R5 ; contre-lecture RV-1 à RV-23)."""
from __future__ import annotations

import json

import numpy as np
import pytest
import torch

from conftest import committer
from controle_ia.environnements import revalider_pilote_a as rv
from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import regler_determinisme
from controle_ia.manifeste import config_canonique
from controle_ia.scellement import sceller

regler_determinisme(1)

CONFIG = {"N": 1, "T": 2, "episodes_par_tache": 1, "lot": 2, "max_nouveaux": 6, "temperature": 1.0,
          "couches": [0, 1, 2], "fraction_equivalence": 1.0, "statistique_equivalence": "q99",
          "tolerance_equivalence": 0.2, "positions_min_controle_negatif": 4, "actions_min_controle_negatif": 1,
          "fraction_min_controle_negatif": 0.95, "agent": {"nom": "agent-jouet"}, "mode": "jouet", "fils": 1,
          "bras": ["defaut", "math"], "nombre_taches": 4, "transcriptions_repere": 2, "actions_min_comparees": 4,
          "part_min_contexte_couvert": 0.9, "memoire_carte_min_gio": 75, "memoire_pic_max_gio": 70,
          "marge_q99": 0.15, "rho_max": 3, "duree_max_s": 600, "duree_max_bras_s": 300,
          "duree_max_episodes_pilote_s": 1e9, "chemin": {"T": 2, "tolerance": 1e-5},
          "controle_positif": {"T": 2, "decalage_positions": 1, "positions_min": 4, "actions_min": 1,
                               "fraction_min": 0.95}}


def _taches(prefixe, n, longueur=lambda k: 1 + k):
    return [{"identifiant": f"{prefixe}.{k:05d}v1", "questions": f"Why do routers matter in setting {k}? " * longueur(k),
             "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": []}}
            for k in range(n)]


def _fichiers(depot, entrainement, evaluation, suffixe=""):
    chemins = []
    for nom, taches in (("entrainement", entrainement), ("evaluation", evaluation)):
        f = depot / f"taches-{nom}{suffixe}.json"
        f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
        sceller(f)
        chemins.append(str(f))
    committer(depot)
    return chemins


EVALUATION = _taches("2602", 64, longueur=lambda k: 1)


def test_configuration_gardee():
    rv.exiger_config_revalidation(CONFIG)
    for config, motif in [({k: v for k, v in CONFIG.items() if k != "part_min_contexte_couvert"}, "incomplète"),
                          (dict(CONFIG, bras=["math", "defaut"]), "dans cet ordre"),
                          (dict(CONFIG, statistique_equivalence="max"), "99e centile"),
                          (dict(CONFIG, fraction_equivalence=0.5), "fraction 1,0"),
                          (dict(CONFIG, marge_q99=0.3), "marge"),
                          (dict(CONFIG, transcriptions_repere=9), "repère"),
                          (dict(CONFIG, duree_max_bras_s=900), "durée d'un bras"),
                          (dict(CONFIG, chemin={"T": 2}), "chemin"),
                          (dict(CONFIG, controle_positif={"T": 2}), "controle_positif"),
                          (dict(CONFIG, mode="essai"), "inconnu")]:
        with pytest.raises(GardeArret, match=motif):
            rv.exiger_config_revalidation(config)


MESURES = {"actions_comparees": 80, "q99_max": 0.05, "ecart_max": 0.4, "contexte_max": 4000,
           "contexte_max_joue": 4200, "actions_remplies": 30}
REPERE = {"7": {"q99": 0.03}, "15": {"q99": 0.06}, "23": {"q99": 0.09}}
AUDIT = {"P9_zone_generee_non_nulle": True, "sondes_conformes": True, "rho_max_observe": 1.5}
CHEMIN = {"conforme": True}


def _lire(bras="math", **k):
    args = dict(mesures=MESURES, controle_negatif={"lecture": "conforme"}, repere=REPERE, rejeu_identique=True,
                config=dict(CONFIG, actions_min_comparees=40), audit=AUDIT, chemin=CHEMIN, bras=bras,
                memoire_pic_gio=40.0, duree_projetee_s=100.0)
    args.update(k)
    return rv.lire_bras(**args)


def test_lecture_d_un_bras_cas_sain_et_artefacts():
    for b in rv.BRAS:
        assert _lire(b)["conforme_avec_marge"]
    assert _lire(mesures=dict(MESURES, q99_max=0.18))["conforme"] and not _lire(
        mesures=dict(MESURES, q99_max=0.18))["conforme_avec_marge"]                      # conforme sans marge (RV-4)
    artefacts = [dict(mesures=dict(MESURES, q99_max=0.21)), dict(mesures=dict(MESURES, q99_max=float("nan"))),
                 dict(controle_negatif={"lecture": "contraire"}), dict(controle_negatif={"lecture": "non concluant"}),
                 dict(repere=dict(REPERE, **{"23": {"q99": 0.11}})), dict(rejeu_identique=False),
                 dict(mesures=dict(MESURES, contexte_max=3700)), dict(mesures=dict(MESURES, actions_remplies=0)),
                 dict(mesures=dict(MESURES, actions_comparees=39)), dict(memoire_pic_gio=71.0),
                 dict(duree_projetee_s=2e9), dict(audit=dict(AUDIT, P9_zone_generee_non_nulle=False)),
                 dict(audit=dict(AUDIT, sondes_conformes=False)), dict(audit=None)]
    for a in artefacts:
        assert not _lire(**a)["conforme"], a
    # chemin (RV-3) et rapport au repère : exigés au noyau par défaut seulement ; ρ au-dessus au « math » : réserve
    assert not _lire("defaut", chemin={"conforme": False})["conforme"] and _lire("math", chemin=None)["conforme"]
    assert not _lire("defaut", audit=dict(AUDIT, rho_max_observe=3.5))["conforme"]
    haut = _lire("math", audit=dict(AUDIT, rho_max_observe=3.5))
    assert haut["conforme"] and haut["reserve_rho"]
    assert not rv.lire_bras({}, {}, None, None, CONFIG, panne="mémoire")["conforme"]
    assert _lire(mesures=dict(MESURES, ecart_max=0.0, q99_max=0.0))["audit_R4_ecarts_tous_nuls"]


def test_regle_de_choix():
    oui = {"conforme": True, "conforme_avec_marge": True}
    sans_marge = {"conforme": True, "conforme_avec_marge": False}
    non = {"conforme": False, "conforme_avec_marge": False}
    assert rv.choisir_noyau({"defaut": oui, "math": oui}) == ("defaut", None)
    assert rv.choisir_noyau({"defaut": non, "math": oui}) == ("math", None)
    assert rv.choisir_noyau({"defaut": sans_marge, "math": oui}) == ("math", None)       # marge d'abord (RV-4)
    noyau, prop = rv.choisir_noyau({"defaut": sans_marge, "math": non})
    assert noyau is None and prop["noyau"] == "defaut" and "sans marge" in prop["motif"]
    noyau, prop = rv.choisir_noyau({"defaut": non, "math": dict(non, aveugle_action_entiere_seulement=True)})
    assert noyau is None and prop["garde"] == "zone générée"
    assert rv.choisir_noyau({"defaut": non, "math": non}) == (None, None)
    assert rv.choisir_noyau({"defaut": oui}) == ("defaut", None)                       # « math » non lu (RV-1)
    assert rv.choisir_noyau({}) == (None, None)


def test_taches_choisies_et_gardees(depot):
    longues = _taches("2601", 6, longueur=lambda k: [1, 9, 2, 9, 7, 3][k])
    e, v = _fichiers(depot, longues, EVALUATION)
    taches, domaine = rv.taches_d_entrainement(e, v, 3)
    assert [t["identifiant"] for t in taches] == ["2601.00001v1", "2601.00003v1", "2601.00004v1"]   # les plus longs
    assert domaine["couvre_le_pilote"] and domaine["longueur_max_choisies"] > domaine["longueur_max_evaluation"]
    for rang, (entrainement, evaluation, motif) in enumerate([
            (longues + [EVALUATION[0]], EVALUATION, "aussi tâches d'évaluation"),
            (longues + [dict(EVALUATION[1], identifiant="2602.00001v2")], EVALUATION, "aussi tâches d'évaluation"),
            (longues, EVALUATION[:63], "64 attendues"), (longues, [], "64 attendues"),
            (longues[:2], EVALUATION, "3 attendues")]):
        f_e, f_v = _fichiers(depot, entrainement, evaluation, suffixe=f"-{rang}")
        with pytest.raises(GardeArret, match=motif):
            rv.taches_d_entrainement(f_e, f_v, 3)


def test_citations_cas_sain_et_artefacts(tmp_path):
    sha_c = __import__("hashlib").sha256(config_canonique(CONFIG)).hexdigest()
    p = tmp_path / "prereg.md"

    from controle_ia.environnements.invites import RACINE_INVITES
    from controle_ia.scellement import verifier
    sha_index = verifier(RACINE_INVITES / "index.json")

    def ecrire(c=sha_c, t="a" * 64, v="b" * 64, entropie=7, i=sha_index):
        lignes = [f"- Configuration de la revalidation (empreinte canonique) : `{c}`", f"- Tâches d'entraînement : `{t}`",
                  f"- Tâches d'évaluation : `{v}`", f"- Index des invites : `{i}`", f"- Entropie : `{entropie}`"]
        p.write_text("\n".join(x for x in lignes if x), encoding="utf-8")
    ecrire()
    assert rv.exiger_citations(p, CONFIG, "a" * 64, "b" * 64) == 7
    ecrire(i="d" * 64)                                                   # RV-18 : index des invites autre que cité
    with pytest.raises(GardeArret, match="index des invites"):
        rv.exiger_citations(p, CONFIG, "a" * 64, "b" * 64)
    ecrire()
    for args, motif in [(dict(CONFIG, lot=3), "configuration"), ]:
        with pytest.raises(GardeArret, match=motif):
            rv.exiger_citations(p, args, "a" * 64, "b" * 64)
    with pytest.raises(GardeArret, match="entraînement"):
        rv.exiger_citations(p, CONFIG, "c" * 64, "b" * 64)
    with pytest.raises(GardeArret, match="évaluation"):
        rv.exiger_citations(p, CONFIG, "a" * 64, "c" * 64)
    p.write_text(p.read_text().replace("Tâches d'évaluation", "Tâches"), encoding="utf-8")
    with pytest.raises(GardeArret, match="ne cite pas"):
        rv.exiger_citations(p, CONFIG, "a" * 64, "b" * 64)


def test_reel_sans_preenregistrement_refuse(depot):
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    with pytest.raises(GardeArret, match="R1"):
        rv.executer(dict(CONFIG, mode="reel"), depot, "20261007-000000-revalidation", None, e, v)
    with pytest.raises(GardeArret, match="entropie d'essai"):
        rv.executer(CONFIG, depot, "20261007-000000-revalidation", "prereg.md", e, v, entropie_essai=3)


def test_q99_depasse_est_prudent():
    rng = np.random.default_rng(3)
    for _ in range(300):
        m = int(rng.integers(1, 400))
        e = rng.random(m) * rng.choice([0.1, 1.0, 3.0])
        tau = 0.2
        if rv.q99_depasse(int(np.sum(e > tau)), m):
            assert np.quantile(e, 0.99) > tau
    assert rv.q99_depasse(1, 1) and not rv.q99_depasse(0, 1) and not rv.q99_depasse(0, 0)


def _fiche_longue(q99_action, q99_generee, au_dessus, generes=20, contexte=4980, nuls=0, sonde=True):
    cle = "0,9"
    return {"equivalence": {
        "ecarts_q99": {cle: {7: q99_action}}, "ecarts": {cle: {7: max(q99_generee, q99_action)}},
        "positions_capturees": {cle: contexte + generes}, "longueurs_contexte": {cle: contexte},
        "lignes": {cle: {"remplissage": 3}}, "sondes": {cle: {"tableaux_distincts": True, "ulp_vu": sonde}},
        "profils": {cle: {7: {"generee": {"jetons": generes, "q99": q99_generee, "max": q99_generee, "nuls": nuls}}}},
        "controle_negatif_zone_generee": {cle: {7: {"positions": generes - 1, "au_dessus": au_dessus,
                                                    "max": 0.8, "q99": q99_action}}}},
        "actions": [{"debut": contexte}]}


def test_garde_zone_generee_et_proposition_au_noeud():
    # zone générée de 20 positions sur 5 000 : la garde de l'action entière est aveugle au décalage ; la garde
    # restreinte le voit si le 99e centile de la zone décalée dépasse le seuil (RV-11 : 19 positions sur 19 au-dessus)
    fiches = [_fiche_longue(0.03, 0.05, 19) for _ in range(12)]
    zg = rv.garde_zone_generee(fiches, 0.2, 4)
    assert zg["q99_generee_max"] == 0.05 and zg["comparables"] == 12 and zg["fraction"] == 1.0
    assert zg["part_zone_generee_sous_1pc"] == 1.0
    cfg = dict(CONFIG, actions_min_comparees=10, actions_min_controle_negatif=10)
    mesures = rv.domaine_et_garde(fiches)
    audit = rv.audit_symetrie(fiches, {"7": {"q99": 0.05}})
    lecture = rv.lire_bras(mesures, {"lecture": "contraire"}, {"7": {"q99": 0.05}}, True, cfg, zone_generee=zg,
                           audit=audit)
    assert not lecture["conforme"] and lecture["garde_zone_generee_conforme"]
    assert lecture["aveugle_action_entiere_seulement"]
    # une seule position décalée au-dessus du seuil : le maximum la verrait, pas le 99e centile (RV-11)
    zg_max = rv.garde_zone_generee([_fiche_longue(0.03, 0.05, 1) for _ in range(12)], 0.2, 4)
    assert zg_max["fraction"] == 0.0
    # un vrai défaut de la zone générée (99e centile 0,5) : pas de proposition
    zg_ko = rv.garde_zone_generee([_fiche_longue(0.03, 0.5, 19) for _ in range(12)], 0.2, 4)
    lecture_ko = rv.lire_bras(mesures, {"lecture": "contraire"}, {"7": {"q99": 0.05}}, True, cfg, zone_generee=zg_ko,
                              audit=audit)
    assert not lecture_ko["garde_zone_generee_conforme"] and not lecture_ko["aveugle_action_entiere_seulement"]


def test_audit_de_symetrie():
    sain = rv.audit_symetrie([_fiche_longue(0.03, 0.05, 19)], {"7": {"q99": 0.02}})
    assert sain["P9_zone_generee_non_nulle"] and sain["sondes_conformes"] and sain["rho_max_observe"] == pytest.approx(1.5)
    assert not rv.audit_symetrie([_fiche_longue(0.03, 0.05, 19, nuls=20)], None)["P9_zone_generee_non_nulle"]
    assert not rv.audit_symetrie([_fiche_longue(0.03, 0.05, 19, sonde=False)], None)["sondes_conformes"]
    assert rv.audit_symetrie([_fiche_longue(0.03, 0.05, 19)], {"7": {"q99": 0.0}})["rho_max_observe"] == float("inf")


def _fiche_chemin(maximum, generes=10, couches=(0, 1)):
    return {"equivalence": {"ecarts": {"0,0": {c: maximum for c in couches}},
                            "profils": {"0,0": {c: {"generee": {"jetons": generes, "max": maximum}} for c in couches}}}}


def test_lecture_du_chemin():
    cfg = dict(CONFIG, chemin={"T": 2, "tolerance": 3e-3})
    sain, d1 = [_fiche_chemin(1e-4)], [_fiche_chemin(0.06)]
    assert rv.lire_chemin(sain, {"lecture": "conforme"}, d1, cfg)["conforme"]
    assert not rv.lire_chemin([_fiche_chemin(5e-3)], {"lecture": "conforme"}, d1, cfg)["conforme"]          # C1
    assert rv.lire_chemin(sain, {"lecture": "conforme"}, [_fiche_chemin(1e-3)], cfg)["C2"] == "contraire"   # C2
    assert rv.lire_chemin(sain, {"lecture": "conforme"}, [_fiche_chemin(float("nan"))], cfg)["C2"] == "contraire"
    assert rv.lire_chemin(sain, {"lecture": "conforme"}, [_fiche_chemin(0.06, generes=2)], cfg)["C2"] == "non concluant"
    assert not rv.lire_chemin(sain, {"lecture": "contraire"}, d1, cfg)["conforme"]                          # C3


def test_deroule_complet_en_mode_jouet(depot):
    e, v = _fichiers(depot, _taches("2601", 5), EVALUATION)
    run = "20261007-000000-revalidation-jouet"
    resume = rv.executer(CONFIG, depot, run, None, e, v, entropie_essai=11)
    assert set(resume["lectures"]) == {"defaut", "math"}
    assert resume["domaine_enonces"]["couvre_le_pilote"]
    d = depot / "diag" / run
    for b in rv.BRAS:
        for nom in (f"episodes-{b}", f"mesures-{b}", f"lecture-{b}"):
            assert (d / f"{nom}.json.sha256").is_file(), nom
        r = resume["bras"][b]
        assert r["rejeu_identique"] is True
        assert r["mesures"]["actions_comparees"] == 8          # 4 épisodes × 2 actions, toutes comparées (RV-4)
        assert set(r["repere"]) == {"0", "1", "2"} and all(x["jetons"] > 0 for x in r["repere"].values())
        assert set(r["audit"]) >= {"P9_zone_generee_non_nulle", "sondes_conformes", "rho"}
        assert r["duree_projetee_episodes_pilote_s"] > 0
    chemin = resume["bras"]["defaut"]["chemin"]
    assert chemin["C2_comparables"] > 0 and chemin["C2"] in ("conforme", "contraire", "non concluant")
    assert resume["bras"]["math"]["chemin"] is None
    assert (d / "chemin-defaut.json.sha256").is_file()
    assert resume["noyau_retenu"] == rv.choisir_noyau(resume["lectures"])[0]
    mesures = json.loads((d / "mesures-defaut.json").read_text())["resultat"]
    assert len(mesures["repere_transcriptions"]) == 2                                   # plus longues (RV-12)
    episodes = json.loads((d / "episodes-defaut.json").read_text())["resultat"]["fiches"]
    longueurs = sorted(len(t["questions"]) for t in _taches("2601", 5))[-4:]
    assert sorted(len(t["questions"]) for t in _taches("2601", 5) if f"{t['identifiant']}/e0" in
                  {f["episode"] for f in episodes}) == longueurs                       # énoncés les plus longs (RV-5)


def test_arret_consigne_garde_le_bras_lu(depot, monkeypatch):
    """RV-1 : un arrêt pendant le bras « math » laisse le bras « defaut » écrit et lu ; l'arrêt applique la règle aux
    bras lus."""
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    vrai = rv._jouer_bras

    def panne(modele, fmt, bras, *a, **k):
        if bras == "math":
            raise GardeArret("limite de durée dépassée (simulée)")
        return vrai(modele, fmt, bras, *a, **k)
    monkeypatch.setattr(rv, "_jouer_bras", panne)
    run = "20261007-000003-revalidation-arret"
    with pytest.raises(GardeArret, match="simulée"):
        rv.executer(CONFIG, depot, run, None, e, v, entropie_essai=11)
    d = depot / "diag" / run
    arret = json.loads((d / "arret.json").read_text())["resultat"]
    assert arret["etape"] == "bras math" and arret["bras_lus"] == ["defaut"]
    lecture = json.loads((d / "lecture-defaut.json").read_text())["resultat"]["lecture"]
    assert arret["noyau_retenu_sur_les_bras_lus"] == rv.choisir_noyau({"defaut": lecture})[0]


def test_panne_de_memoire_dans_un_bras(depot, monkeypatch):
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    vrai = rv._jouer_bras

    def panne(modele, fmt, bras, *a, **k):
        if bras == "math":
            raise torch.cuda.OutOfMemoryError("mémoire simulée")
        return vrai(modele, fmt, bras, *a, **k)
    monkeypatch.setattr(rv, "_jouer_bras", panne)
    resume = rv.executer(CONFIG, depot, "20261007-000004-revalidation-panne", None, e, v, entropie_essai=11)
    assert resume["lectures"]["math"]["panne"].startswith("mémoire") and not resume["lectures"]["math"]["conforme"]


def test_rejeu_different_lu_non_conforme(depot, monkeypatch):
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    appels = []
    vrai = rv._empreintes_rejeu

    def decale(fiches):
        appels.append(1)
        r = vrai(fiches)
        return r if len(appels) % 2 else {k: dict(x, empreintes={"autre": 1}) for k, x in r.items()}
    monkeypatch.setattr(rv, "_empreintes_rejeu", decale)
    resume = rv.executer(CONFIG, depot, "20261007-000005-revalidation-rejeu", None, e, v, entropie_essai=11)
    assert all(not x["R4_rejeu"] and not x["conforme"] for x in resume["lectures"].values())


def test_signal_term_arrete():
    with pytest.raises(GardeArret, match="TERM"):
        rv._signal_term(15, None)


# --- vérification courte 2 (W-2, W-3, W-7, W-13, W-14) ------------------------------------------------------------

def test_carte_a100_gardee():
    """W-13 : le domaine revalidé est une A100 ; une autre carte arrête avant tout bras."""
    assert rv.exiger_carte_a100("NVIDIA A100-SXM4-80GB") == "NVIDIA A100-SXM4-80GB"
    assert rv.exiger_carte_a100("NVIDIA A100 80GB PCIe")
    for autre in ("NVIDIA H100 80GB HBM3", "NVIDIA RTX A1000"):          # X-9 : mot entier, pas une sous-chaîne
        with pytest.raises(GardeArret, match="A100"):
            rv.exiger_carte_a100(autre)


def test_mesures_exigees_en_mode_reel(depot, monkeypatch):
    """W-14 et X-5 : en mode réel, un pic de mémoire ou une durée projetée absents arrêtent (cas sain : mesures
    présentes, ou mode jouet) ; l'arrêt vient après l'écriture des épisodes et des mesures du bras, consigné à l'étape du
    bras."""
    rv.exiger_mesures_reelles(True, 40.0, 100.0, "defaut")
    rv.exiger_mesures_reelles(False, None, None, "defaut")
    for pic, projetee in ((None, 100.0), (40.0, None)):
        with pytest.raises(GardeArret, match="absents en mode réel"):
            rv.exiger_mesures_reelles(True, pic, projetee, "defaut")
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    vraie = rv.exiger_mesures_reelles

    def absentes(reel, pic, projetee, bras):
        return vraie(True, None, projetee, bras)                           # mode réel simulé, pic de mémoire absent
    monkeypatch.setattr(rv, "exiger_mesures_reelles", absentes)
    run = "20261007-000010-revalidation-mesures"
    with pytest.raises(GardeArret, match="absents en mode réel"):
        rv.executer(CONFIG, depot, run, None, e, v, entropie_essai=11)
    d = depot / "diag" / run
    arret = json.loads((d / "arret.json").read_text())["resultat"]
    assert arret["etape"] == "bras defaut" and arret["bras_lus"] == []
    for nom in ("episodes-defaut", "mesures-defaut"):
        assert (d / f"{nom}.json.sha256").is_file()


def test_echeance_du_bras_cas_sain_et_artefact(depot, monkeypatch):
    """W-3 et W-7 (b) : l'échéance du bras est contrôlée avant le repère (cas sain : à venir ; artefact : passée) ; la
    phase « chemin » reçoit l'échéance du bras, non celle du run ; un dépassement arrête, consigné à l'étape « repère et
    chemin »."""
    import time
    rv.exiger_echeance_bras(time.perf_counter() + 60, "defaut")
    with pytest.raises(GardeArret, match="limite de durée du bras defaut"):
        rv.exiger_echeance_bras(time.perf_counter() - 1, "defaut")
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    vrai, recues = rv._phase_chemin, []

    def phase(reference, fmt, plan, g, config, echeance):
        recues.append(echeance - time.perf_counter())
        return vrai(reference, fmt, plan, g, config, echeance)
    monkeypatch.setattr(rv, "_phase_chemin", phase)
    rv.executer(dict(CONFIG, duree_max_s=10 ** 6), depot, "20261007-000006-revalidation-echeance", None, e, v,
                entropie_essai=11)
    assert len(recues) == 1 and 0 < recues[0] <= CONFIG["duree_max_bras_s"]       # borne du bras, pas 10**6 s
    committer(depot)                                                               # le run suivant exige un arbre propre

    def depasse(echeance, bras):
        raise GardeArret(f"limite de durée du bras {bras} dépassée avant le repère (simulée)")
    monkeypatch.setattr(rv, "exiger_echeance_bras", depasse)
    run = "20261007-000007-revalidation-echeance"
    with pytest.raises(GardeArret, match="simulée"):
        rv.executer(CONFIG, depot, run, None, e, v, entropie_essai=11)
    arret = json.loads((depot / "diag" / run / "arret.json").read_text())["resultat"]
    assert arret["etape"] == "repère et chemin defaut" and arret["bras_lus"] == []
    assert (depot / "diag" / run / "mesures-defaut.json.sha256").is_file()           # le bras joué reste écrit


def test_panne_de_memoire_pendant_le_repere(depot, monkeypatch):
    """W-2 et W-7 (d) : une panne de mémoire pendant le repère ou la phase « chemin » est consignée comme pendant le
    bras : bras non conforme, l'autre bras se joue et se lit."""
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    vrai, appels = rv._modele_reference, []

    def reference(config, graine):
        appels.append(1)
        if len(appels) == 1:
            raise torch.cuda.OutOfMemoryError("mémoire simulée au repère")
        return vrai(config, graine)
    monkeypatch.setattr(rv, "_modele_reference", reference)
    resume = rv.executer(CONFIG, depot, "20261007-000008-revalidation-panne-repere", None, e, v, entropie_essai=11)
    d = resume["lectures"]["defaut"]
    assert d["panne"].startswith("mémoire pendant le repère") and not d["conforme"]
    assert "panne" not in resume["lectures"]["math"] and "R1_garde_saine" in resume["lectures"]["math"]
    assert resume["bras"]["math"]["longueur_remplie_max"] > 0                          # W-6 : au résumé


def test_signal_term_dans_un_sous_processus(depot):
    """W-7 (c) : un vrai signal TERM, envoyé par l'identifiant du processus (R10) au lanceur en mode jouet après son
    manifeste, devient un arrêt consigné (arret.json, motif « signal TERM »), code de sortie 1."""
    import os
    import signal
    import subprocess
    import sys
    import time
    from pathlib import Path
    (depot / "config.json").write_text(json.dumps(dict(CONFIG, T=4)), encoding="utf-8")
    sceller(depot / "config.json")
    e, v = _fichiers(depot, _taches("2601", 4), EVALUATION)
    run = "20261007-000009-revalidation-term"
    src = str(Path(rv.__file__).resolve().parents[2])
    env = dict(os.environ, PYTHONPATH=src, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.Popen([sys.executable, "-m", "controle_ia.environnements.revalider_pilote_a", "--config",
                          "config.json", "--entrainement", e, "--evaluation", v, "--run-id", run],
                         cwd=depot, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sceau = depot / "runs" / run / "manifeste.json.sha256"       # X-2 : le sceau, écrit après le manifeste, puis 0,5 s :
    limite = time.monotonic() + 300                               # le lanceur est alors dans le bloc qui consigne l'arrêt
    while not sceau.exists() and p.poll() is None and time.monotonic() < limite:
        time.sleep(0.05)
    time.sleep(0.5)
    assert sceau.exists() and p.poll() is None
    os.kill(p.pid, signal.SIGTERM)
    _, err = p.communicate(timeout=600)
    assert p.returncode == 1 and "signal TERM" in err
    arret = json.loads((depot / "diag" / run / "arret.json").read_text())["resultat"]
    assert "signal TERM" in arret["motif"]
