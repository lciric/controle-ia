"""Harnais de T0.4 : instrument seulement, sur modèle jouet à poids aléatoires (aucune mesure).

Couvre : tokeniseur hors ligne, initialisation déterministe, couches par défaut, crochets et passe
unique, garde d'équivalence (cas sain + artefact), vecteur d'action par maximum (dernier jeton, moyenne
et médiane refusés), scores de sondes par maximum ou attention (autres agrégations refusées), garde
« en ligne = hors ligne » (cas sain + artefact), indexation (agent, pas) et empans exacts, rejeu au bit
près (cas sain + artefact de graine), liste blanche des modèles, estimation du stockage, run factice de
bout en bout avec la politique de stockage par défaut.
"""
import dataclasses

import numpy as np
import pytest
import torch

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import (Crochets, agreger, couches_par_defaut, ecart_equivalence,
                                             exiger_equivalence, passe_unique)
from controle_ia.harnais.episode import (EnvironnementJouet, empreinte_episode, generer, jouer_episode,
                                         vecteurs_par_action)
from controle_ia.harnais.modeles import (empreinte_poids, exiger_modele_autorise, modele_jouet,
                                         regler_determinisme, tokeniseur_caracteres)
from controle_ia.harnais.sondes import exiger_identite, score_action, scores_en_ligne, sonde_lineaire_aleatoire
from controle_ia.harnais.stockage import estimer

regler_determinisme(1)
TOK = tokeniseur_caracteres()


def _modele(graine=7):
    return modele_jouet(graine, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def test_tokeniseur_aller_retour():
    texte = "Pas 2. Agent 1 : élève « très » prudent…"
    ids = TOK(texte, add_special_tokens=False)["input_ids"]
    assert TOK.decode(ids) == texte and TOK.unk_token_id not in ids


def test_modele_jouet_deterministe():
    assert empreinte_poids(_modele(7)) == empreinte_poids(_modele(7))
    assert empreinte_poids(_modele(7)) != empreinte_poids(_modele(8))


def test_couches_par_defaut():
    assert couches_par_defaut(4) == [0, 1, 2]
    assert couches_par_defaut(32) == [7, 15, 23]
    assert couches_par_defaut(1) == [0]
    with pytest.raises(GardeArret):
        couches_par_defaut(0)


def test_equivalence_saine_et_artefact():
    m = _modele()
    ctx = [TOK.bos_token_id] + TOK("Tu es l'agent 0.", add_special_tokens=False)["input_ids"]
    with Crochets(m, [0, 2]) as c:
        nouveaux = generer(m, ctx, 12, 1.0, 1234, TOK.eos_token_id)
        acts_gen = c.vider()
    ids = ctx + nouveaux
    acts = passe_unique(m, ids, [0, 2])
    assert acts[0].shape == (len(ids), 32)
    assert acts_gen[0].shape[0] in (len(ids), len(ids) - 1)
    ecarts = ecart_equivalence(acts_gen, acts)
    exiger_equivalence(ecarts, 1e-4, "cas sain")
    assert max(ecarts.values()) < 1e-5
    # artefact : un poids modifié entre la génération et la passe unique
    with torch.no_grad():
        m.model.layers[0].mlp.down_proj.weight.add_(0.05)
    acts_faux = passe_unique(m, ids, [0, 2])
    with pytest.raises(GardeArret, match="génération ≠ passe unique"):
        exiger_equivalence(ecart_equivalence(acts_gen, acts_faux), 1e-4, "artefact")


def test_vecteur_d_action_max_seulement():
    a = np.arange(20, dtype=np.float32).reshape(5, 4)
    assert np.array_equal(agreger(a, 1, 4, "max"), a[3])
    b = np.array([[0, 5], [3, 1], [2, 2]], dtype=np.float32)
    assert np.array_equal(agreger(b, 0, 3, "max"), [3, 5])
    for interdite in ("dernier", "moyenne", "mediane", "mean", "attention"):
        with pytest.raises(GardeArret, match="seul le maximum.*jamais la moyenne"):
            agreger(a, 0, 2, interdite)
    with pytest.raises(GardeArret, match="empan"):
        agreger(a, 3, 3, "max")


def test_sonde_max_et_attention():
    rng = np.random.default_rng(3)
    acts = rng.standard_normal((9, 8)).astype(np.float32)
    acts[4, 0] = 10.0                                   # le jeton 4 domine la coordonnée 0
    s_max = sonde_lineaire_aleatoire("m", 1, 8, "max", np.random.default_rng(1))
    brut = acts[2:7].astype(np.float64) @ s_max.w + s_max.b
    assert score_action(s_max, acts, 2, 7) == pytest.approx(brut.max(), abs=1e-12)
    s_att = sonde_lineaire_aleatoire("a", 1, 8, "attention", np.random.default_rng(2))
    brut_att = acts[2:7].astype(np.float64) @ s_att.w + s_att.b
    assert brut_att.min() <= score_action(s_att, acts, 2, 7) <= brut_att.max()
    q = np.zeros(8)
    q[0] = 50.0                                         # attention concentrée sur le jeton 4
    concentree = dataclasses.replace(s_att, q=q)
    assert score_action(concentree, acts, 2, 7) == pytest.approx(brut_att[2], abs=1e-9)
    for interdite in ("moyenne", "mediane", "dernier"):
        with pytest.raises(GardeArret, match="maximum ou l'attention"):
            score_action(dataclasses.replace(s_max, agregation=interdite), acts, 0, 3)
    with pytest.raises(GardeArret, match="sans requête"):
        score_action(dataclasses.replace(s_att, q=None), acts, 0, 3)

    class Fausse:                                       # artefact : un scalaire au lieu d'un score par jeton
        nom, couche, agregation = "f", 1, "max"

        def scores_par_jeton(self, a):
            return np.float64(a.sum())
    with pytest.raises(GardeArret, match="forme"):
        score_action(Fausse(), acts, 0, 3)


def _jouer(m, graines, N=2, T=2, echantillon=()):
    return jouer_episode(m, TOK, EnvironnementJouet(), "ep", N, T, graines, [0, 1, 2], max_nouveaux=10,
                         echantillon_equivalence=echantillon)


def test_episode_indexation_et_empans():
    m = _modele()
    graines = {(i, t): 100 + 10 * i + t for t in range(2) for i in range(2)}
    ep, acts, eq = _jouer(m, graines, echantillon=set(graines))
    ordre = [(a.agent, a.pas) for a in ep.actions_dans_l_ordre()]
    assert ordre == [(0, 0), (1, 0), (0, 1), (1, 1)]
    for tr in ep.transcriptions:
        assert all(a.agent == tr.agent for a in tr.actions)
        for a in tr.actions:
            assert tr.ids[a.debut:a.fin] == a.ids and a.fin - a.debut == len(a.ids) >= 1
    v = vecteurs_par_action(ep, acts, 1, "max")
    assert v.shape == (2, 2, 32)
    a = ep.transcriptions[1].actions[0]
    assert np.array_equal(v[1, 0], acts[1][1][a.debut:a.fin].max(axis=0))
    assert len(eq["ecarts"]) == 4 and max(max(e.values()) for e in eq["ecarts"].values()) < 1e-5


def test_scores_en_ligne_et_garde_hors_ligne():
    m = _modele()
    graines = {(i, t): 900 + i + 3 * t for t in range(2) for i in range(2)}
    ep, acts, _ = _jouer(m, graines)
    sondes = [sonde_lineaire_aleatoire("m", 1, 32, "max", np.random.default_rng(1)),
              sonde_lineaire_aleatoire("a", 1, 32, "attention", np.random.default_rng(2))]
    sc = scores_en_ligne(ep, acts, sondes)
    assert set(sc) == {"m", "a"} and sc["m"].shape == (2, 2) and np.all(np.isfinite(sc["a"]))
    a10 = ep.transcriptions[1].actions[0]
    assert sc["m"][1, 0] == score_action(sondes[0], acts[1][1], a10.debut, a10.fin)
    copie = {a: {c: v.copy() for c, v in pc.items()} for a, pc in acts.items()}
    exiger_identite(sc, scores_en_ligne(ep, copie, sondes), "cas sain")
    copie[1][1][a10.debut:a10.fin] += 1e-3              # artefact : activations altérées entre mémoire et disque
    with pytest.raises(GardeArret, match="en ligne ≠ recalcul hors ligne"):
        exiger_identite(sc, scores_en_ligne(ep, copie, sondes), "artefact")
    with pytest.raises(GardeArret, match="non capturée"):
        scores_en_ligne(ep, acts, [sonde_lineaire_aleatoire("x", 3, 32, "max", np.random.default_rng(4))])
    with pytest.raises(GardeArret, match="double"):
        scores_en_ligne(ep, acts, [sondes[0], sondes[0]])


def test_relecture_du_disque_saine_et_artefacts(tmp_path):
    from controle_ia.harnais import run_harnais_factice as R
    m = _modele()
    ep, acts, _ = _jouer(m, {(i, t): 300 + i + 5 * t for t in range(2) for i in range(2)})
    sondes = [sonde_lineaire_aleatoire("m", 1, 32, "max", np.random.default_rng(1)),
              sonde_lineaire_aleatoire("a", 2, 32, "attention", np.random.default_rng(2))]
    vecteurs, scores = R.calculer_en_ligne(R.CONFIG, ep, acts, [0, 1, 2], sondes)
    sain = R.ecrire_tableaux(tmp_path / "sain.npz", acts, vecteurs, scores)
    R.relire_et_controler(sain, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, True, acts)
    evaluation = R.ecrire_tableaux(tmp_path / "evaluation.npz", None, vecteurs, scores)
    R.relire_et_controler(evaluation, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, False)
    with pytest.raises(GardeArret, match="hors entraînement"):     # artefact : par jeton gardé en évaluation
        R.relire_et_controler(sain, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, False)
    faux = {a: {c: v.copy() for c, v in pc.items()} for a, pc in acts.items()}
    faux[0][2] += 1e-3                                              # artefact : activations écrites ≠ mémoire
    altere = R.ecrire_tableaux(tmp_path / "altere.npz", faux, vecteurs, scores)
    with pytest.raises(GardeArret, match="recalcul hors ligne"):
        R.relire_et_controler(altere, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, True, acts)
    scores_faux = {k: v + 1.0 for k, v in scores.items()}           # artefact : scores écrits ≠ mémoire
    with pytest.raises(GardeArret, match="scores relus"):
        R.relire_et_controler(sain, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores_faux, True, acts)
    with pytest.raises(GardeArret, match="sans la référence"):       # la relecture par jeton exige la mémoire
        R.relire_et_controler(sain, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, True)
    # artefact (contre-lecture 1, Rem-2) : positions hors des empans d'action altérées sur le disque ;
    # vecteurs et scores inchangés, mais les activations par jeton relues diffèrent de la mémoire
    hors = {a: {c: v.copy() for c, v in pc.items()} for a, pc in acts.items()}
    for tr in ep.transcriptions:
        dans = np.zeros(len(tr.ids), dtype=bool)
        for x in tr.actions:
            dans[x.debut:x.fin] = True
        for c in hors[tr.agent]:
            hors[tr.agent][c][~dans] = 0.0
    hors_empans = R.ecrire_tableaux(tmp_path / "hors-empans.npz", hors, vecteurs, scores)
    with pytest.raises(GardeArret, match="activations par jeton relues"):
        R.relire_et_controler(hors_empans, R.CONFIG, ep, [0, 1, 2], sondes, vecteurs, scores, True, acts)
    with pytest.raises(GardeArret, match="R12"):
        R.ecrire_tableaux(tmp_path / "sain.npz", acts, vecteurs, scores)


def test_politique_de_stockage_gardes():
    from controle_ia.harnais import run_harnais_factice as R
    R.valider_config(R.CONFIG)
    pol = R.CONFIG["politique"]
    for politique, motif in (
            (dict(pol, episodes_par_jeton=[5]), "hors de"),
            (dict(pol, vecteurs_par_action=["dernier"]), "refusé"),
            (dict(pol, sondes=[dict(pol["sondes"][0], agregation="moyenne")]), "refusée"),
            (dict(pol, sondes=[dict(pol["sondes"][0], couche="quatrieme")]), "indisponible"),
            (dict(pol, sondes=[pol["sondes"][0], pol["sondes"][0]]), "double")):
        with pytest.raises(GardeArret, match=motif):
            R.valider_config(dict(R.CONFIG, politique=politique))


def test_rejeu_identique_et_artefact_de_graine():
    m = _modele()
    graines = {(i, t): 500 + i + 7 * t for t in range(2) for i in range(2)}
    e1 = empreinte_episode(*_jouer(m, graines)[:2])
    e2 = empreinte_episode(*_jouer(m, graines)[:2])
    assert e1 == e2
    autres = dict(graines)
    autres[(1, 1)] += 1
    e3 = empreinte_episode(*_jouer(m, autres)[:2])
    assert e3["trajectoire"] != e1["trajectoire"]
    with pytest.raises(GardeArret, match="graine absente"):
        _jouer(m, {(0, 0): 1})


def test_liste_blanche_des_modeles():
    exiger_modele_autorise("meta-llama/Llama-3.1-8B-Instruct", "0e9e39f249a16976918f6564b8830bc894c89659")
    with pytest.raises(GardeArret, match="GO de Lazar"):
        exiger_modele_autorise("meta-llama/Llama-3.3-70B-Instruct", "0e9e39f")
    with pytest.raises(GardeArret, match="révision"):
        exiger_modele_autorise("Qwen/Qwen2.5-7B-Instruct", None)
    for mobile in ("main", "0e9e39f", "0E9E39F249A16976918F6564B8830BC894C89659"):
        with pytest.raises(GardeArret, match="révision figée"):
            exiger_modele_autorise("meta-llama/Llama-3.1-8B-Instruct", mobile)


def test_estimation_du_stockage():
    e = estimer(2000, 6000, 20, 3, 4096, 2, 0.1)
    assert e["tout_par_jeton_octets"] == 2000 * 6000 * 3 * 4096 * 2
    assert e["politique_defaut_octets"] == round(0.1 * e["tout_par_jeton_octets"]) + 2000 * 20 * 3 * 4096 * 2
    with pytest.raises(GardeArret):
        estimer(0, 1, 1, 1, 1)
    with pytest.raises(GardeArret):
        estimer(1, 1, 1, 1, 1, fraction_par_jeton=1.5)


def test_run_harnais_factice_de_bout_en_bout(depot):
    from controle_ia.harnais import run_harnais_factice as R
    from controle_ia.manifeste import verifier_resultat
    from controle_ia.scellement import verifier

    config = dict(R.CONFIG, episodes=2, N=2, T=2, max_nouveaux=8,
                  modele={"couches": 4, "largeur": 32, "tetes": 4, "tetes_cle_valeur": 2, "intermediaire": 64})
    s1 = R.executer(depot, "20261004-150000-harnais-factice", entropie=4242, config=config)
    assert s1["rejeu_identique"] and s1["reserves"] == []
    corps = verifier_resultat(depot, s1["resume"])
    r = corps["resultat"]
    e0, e1 = r["episodes"]
    assert r["couches"] == [0, 1, 2] and e0["actions"][0][:2] == [0, 0]
    assert e0["par_jeton_conserve"] and not e1["par_jeton_conserve"]
    assert [s["couche"] for s in r["sondes"]] == [1, 1]
    for e in (e0, e1):
        verifier(depot / e["tableaux"])
    with np.load(depot / e0["tableaux"]) as z:
        assert z["par_action/couche1/max"].shape == (2, 2, 32) and z["scores/lineaire-attention"].shape == (2, 2)
        assert {f"par_jeton/agent{a}/couche{c}" for a in (0, 1) for c in (0, 1, 2)} <= set(z.files)
        assert not any(k.endswith("/dernier") for k in z.files)
    with np.load(depot / e1["tableaux"]) as z:            # épisode d'évaluation : rien par jeton
        assert not any(k.startswith("par_jeton/") for k in z.files) and "scores/lineaire-max" in z.files
    assert r["stockage_modele_reel"]["politique_defaut_go"] < r["stockage_modele_reel"]["tout_par_jeton_go"]
    # même entropie, autre run sur la même machine : mêmes empreintes au bit près
    committer(depot)
    s2 = R.executer(depot, "20261004-150001-harnais-factice", entropie=4242, config=config)
    r2 = verifier_resultat(depot, s2["resume"])["resultat"]
    assert [e["empreintes"] for e in r2["episodes"]] == [e0["empreintes"], e1["empreintes"]]
    assert r2["empreinte_poids"] == r["empreinte_poids"] and r2["sondes"] == r["sondes"]
    with pytest.raises(GardeArret):        # R12 : jamais deux fois le même run
        R.executer(depot, "20261004-150001-harnais-factice", entropie=4242, config=config)
