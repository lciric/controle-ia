"""Validation du harnais sur modèle réel (T0.4) : répétition complète sur modèle jouet, comparaison de deux
runs (rejeu entre processus), codage bfloat16 sans perte, gardes de lancement et de fin de phase (cas sain +
artefacts), lecture gelée, empreintes des fichiers du modèle.
"""
import contextlib
import json
import subprocess
import time
from pathlib import Path

import numpy as np
import pytest
import torch

import controle_ia
from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.harnais import politique as P
from controle_ia.harnais import validation_reelle as V
from controle_ia.harnais.episode import EnvironnementJouet, jouer_episodes
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import (comparer_fichiers, empreinte_poids, exiger_type_des_poids, modele_jouet,
                                         sha1_git, tokeniseur_caracteres_chat)

PETITE = dict(V.CONFIG_REPETITION,          # logique telle quelle : remplissage et fins anticipées sur les lignes comparées
              production=dict(V.CONFIG_REPETITION["production"], episodes=4, T=2, max_nouveaux=8),
              debit={"tailles_lot": [1, 4], "longueur_contexte": 32, "max_nouveaux": 4})
LECTURE_SAINE = {"format": "conforme", "tests_instance": "sans objet", "logique_equivalence": "conforme",
                 "logique_controle_negatif": "conforme", "controle_positif": "conforme",
                 "chemin_equivalence": "conforme", "chemin_controle_negatif": "conforme",
                 "controle_positif_chemin": "conforme", "production_equivalence": "conforme",
                 "production_controle_negatif": "conforme", "rejeu_en_processus": "conforme",
                 "audit_symetrie": "non déclenché"}


def test_repetition_complete_puis_rejeu_entre_runs(depot):
    s1 = V.executer(depot, "20261004-160000-repetition-jouet", entropie=77, config=PETITE, verifier_import=False)
    assert s1["lecture"] == LECTURE_SAINE
    r = json.loads((depot / s1["resume"]).read_text(encoding="utf-8"))["resultat"]
    prod, lo = r["production"], r["logique"]
    assert prod["stockage"]["codage"] == "bfloat16-bits" and prod["stockage"]["octets_par_valeur_construction"] == 2
    assert prod["plan_lots"] == [[0, 1], [2, 3]] and [e["par_jeton_conserve"] for e in prod["episodes"]] == [
        False, True, True, False]
    assert lo["equivalence"]["ecart_max"] <= 1e-4 < lo["equivalence"]["controle_negatif"]["min_des_maxima"]
    assert lo["equivalence"]["couverture"]["lignes_echantillon"] == [1, 2] and lo["noyau_attention"] == "math"
    assert set(prod["repere_precision"]) == {"0", "1", "2"} and r["chargement"]["type_des_poids"] == "torch.float64"
    pc = r["controle_positif"]                                         # version 2 : défaut D1 vu au seuil de logique
    assert pc["bilan"]["comparables"] >= 4 and pc["bilan"]["vus"] == pc["bilan"]["comparables"]
    assert pc["bilan"]["min_des_maxima"] > lo["equivalence"]["tolerance"] > lo["equivalence"]["ecart_max"]
    assert lo["noyaux_permis"]["math"] is True and r["reglages"]["relus"]["algorithmes_deterministes"] is True
    assert [m["taille_lot"] for m in r["debit"]["mesures"]] == [1, 4]
    assert all(m["jetons_generes"] == 4 * m["taille_lot"] for m in r["debit"]["mesures"])
    assert (depot / "diag" / "20261004-160000-repetition-jouet" / "logique-episode-3-trajectoire.json").is_file()
    for e in prod["episodes"]:                       # gros tableaux hors git, scellés sur place, empreinte au résumé
        npz = depot / e["tableaux"]
        assert e["tableaux"].startswith("donnees/") and npz.is_file()
        assert npz.with_name(npz.name + ".sha256").read_text().split()[0] == e["tableaux_sha256"]
        assert set(e["empreintes"]) == {"trajectoire", "activations", "logits", "vecteurs", "scores"}
    committer(depot)
    s2 = V.executer(depot, "20261004-160100-repetition-jouet", config=PETITE, rejeu_de="20261004-160000-repetition-jouet",
                    verifier_import=False)
    assert s2["comparaison"]["identique"] and s2["comparaison"]["lecture"] == "conforme"
    committer(depot)
    with pytest.raises(GardeArret, match="entropie"):
        V.executer(depot, "20261004-160200-repetition-jouet", entropie=78, config=PETITE,
                   rejeu_de="20261004-160000-repetition-jouet", verifier_import=False)
    # rejeu incompatible : refusé avant tout calcul (aucun run créé)
    autre = dict(PETITE, production=dict(PETITE["production"], temperature=0.7))
    with pytest.raises(GardeArret, match="configuration"):
        V.executer(depot, "20261004-160300-repetition-jouet", config=autre, rejeu_de="20261004-160000-repetition-jouet",
                   verifier_import=False)
    assert not (depot / "runs" / "20261004-160300-repetition-jouet").exists()


def test_comparaison_saine_et_artefacts(depot, monkeypatch):
    V.executer(depot, "20261004-170000-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261004-170100-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    sain = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    assert sain["identique"] and sain["differences"] == []
    committer(depot)
    with pytest.raises(GardeArret, match="R12"):      # une comparaison ne se réécrit pas
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    V.executer(depot, "20261004-170200-repetition-jouet", entropie=6, config=PETITE, verifier_import=False)
    committer(depot)
    with pytest.raises(GardeArret, match="graines différentes"):
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170200-repetition-jouet")
    # artefacts : relectures qui diffèrent (logits, capture, fichier npz, lecture) → différences nommées, « contraire »
    V.executer(depot, "20261004-170400-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def altere(racine, chemin):
        corps = vrai(racine, chemin)
        if "170400" in str(chemin):
            e = corps["resultat"]["production"]["episodes"][1]
            e["empreintes"]["logits"] = "0" * 64
            e["tableaux_sha256"] = "1" * 64
            e["equivalence"]["empreintes_capture"]["0,0"] = "2" * 64
            corps["resultat"]["lecture"]["format"] = "contraire"
        return corps
    monkeypatch.setattr(V, "verifier_resultat", altere)
    c = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170400-repetition-jouet")
    assert not c["identique"] and c["lecture"] == "contraire"
    attendues = [{"phase": "production", "episode": "episode-1", "empreinte": "logits"},
                 {"phase": "production", "episode": "episode-1", "equivalence": "empreintes_capture"},
                 {"phase": "production", "episode": "episode-1", "motif": "fichier npz différent"}]
    assert c["differences"][:3] == attendues and c["differences"][3]["motif"] == "lectures différentes"


def test_gardes_de_lancement(depot, tmp_path_factory):
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        V.executer(depot, "20261004-180000-validation-reelle", revision="0" * 40, verifier_import=False)
    with pytest.raises(GardeArret, match="révision figée"):
        V.valider_config(V.CONFIG_REELLE, "main")
    V.valider_config(V.CONFIG_REELLE, "0e9e39f249a16976918f6564b8830bc894c89659")
    for mauvaise, motif in ((dict(PETITE, logique=dict(PETITE["logique"], dtype="float32")), "double précision"),
                            (dict(PETITE, controle_positif=dict(PETITE["controle_positif"], decalage_positions=0)),
                             "contrôle positif"),
                            (dict(PETITE, controle_positif=dict(PETITE["controle_positif"], T=99)), "contrôle positif"),
                            (dict(PETITE, production=dict(PETITE["production"], episodes_equivalence=[9])), "hors de la phase"),
                            (dict(PETITE, production=dict(PETITE["production"], lots_rejeu_en_processus=[5])), "lots de rejeu"),
                            (dict(PETITE, debit=dict(PETITE["debit"], tailles_lot=[64])), "plus de lignes"),
                            (dict(PETITE, logique=dict(PETITE["logique"], noyau_attention="flash")), "noyau"),
                            (dict(PETITE, logique=dict(PETITE["logique"], tolerance=0)), "tolérance")):
        with pytest.raises(GardeArret, match=motif):
            V.valider_config(mauvaise, None)
    # limite de durée entre phases : l'arrêt est consigné (arret.json scellé, lecture partielle), puis propagé
    with pytest.raises(GardeArret, match="limite de durée"):
        V.executer(depot, "20261004-180100-repetition-jouet", entropie=1, config=dict(PETITE, limite_s=-1),
                   verifier_import=False)
    arret = json.loads((depot / "diag" / "20261004-180100-repetition-jouet" / "arret.json").read_text(encoding="utf-8"))
    assert arret["resultat"]["phase"] == "logique" and "limite de durée" in arret["resultat"]["motif"]
    assert arret["resultat"]["partiel"]["lecture_partielle"]["logique_equivalence"] == "non atteint"
    # mémoire vive (Rem-5) : cas sain, artefact, fichier illisible
    dehors = tmp_path_factory.mktemp("meminfo")
    meminfo = dehors / "meminfo"
    meminfo.write_text("MemTotal:       131072000 kB\n")
    sans_cgroup = (str(dehors / "absent1"), str(dehors / "absent2"))
    assert V.exiger_memoire_vive(64, meminfo, sans_cgroup)["effective_go"] == 134.2
    cgroup = dehors / "memory.max"
    cgroup.write_text("max\n")                                     # pas de plafond
    assert V.exiger_memoire_vive(64, meminfo, (str(cgroup),))["plafond_conteneur_go"] is None
    cgroup.write_text("34359738368\n")                             # artefact (N-12) : hôte riche, conteneur plafonné à 32 Gio
    with pytest.raises(GardeArret, match="plafond du conteneur 34.4"):
        V.exiger_memoire_vive(64, meminfo, (str(cgroup),))
    meminfo.write_text("MemTotal:       33554432 kB\n")
    with pytest.raises(GardeArret, match="< 64 Go"):
        V.exiger_memoire_vive(64, meminfo, sans_cgroup)
    with pytest.raises(GardeArret, match="illisible"):
        V.exiger_memoire_vive(64, dehors / "absent")
    assert V.exiger_memoire_vive(0) is None
    # mémoire de la carte (N-4)
    assert V.exiger_memoire_carte(75, total_octets=80 * 2 ** 30) == 80.0
    with pytest.raises(GardeArret, match="40.0 Gio < 75"):
        V.exiger_memoire_carte(75, total_octets=40 * 2 ** 30)
    assert V.exiger_memoire_carte(0) is None
    with pytest.raises(GardeArret, match="signal TERM"):        # délai externe (Rem-7)
        V._signal_term(15, None)


def test_garde_de_duree_dans_une_phase():
    """Rem-7 : la durée se vérifie à chaque pas (t, i), pas seulement entre les phases."""
    tok = tokeniseur_caracteres_chat()
    fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    m = modele_jouet(3, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    graines = [{(0, 0): 1, (0, 1): 2}]
    jouer_episodes(m, fmt, EnvironnementJouet(), ["e"], 1, 2, graines, [0, 1, 2], 4, echeance=time.perf_counter() + 600)
    with pytest.raises(GardeArret, match="limite de durée dépassée au pas 0"):
        jouer_episodes(m, fmt, EnvironnementJouet(), ["e"], 1, 2, graines, [0, 1, 2], 4, echeance=time.perf_counter() - 1)


def _preregistrement(depot, commit, revision="0e9e39f249a16976918f6564b8830bc894c89659", entropie=12345):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / "prereg.md"
    p.write_text(f"- Commit du code d'analyse : `{commit}`\n- Révision du modèle : `{revision}`\n"
                 f"- Entropie : `{entropie}`\n", encoding="utf-8")
    return p


def test_gardes_code_cite_citations_et_import(depot):
    """Rem-8 : gardes de lancement testées (cas sain + artefacts)."""
    (depot / "src").mkdir()
    (depot / "src" / "module.py").write_text("x = 1\n")
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    p = _preregistrement(depot, commit)
    assert V.exiger_code_cite(depot, p) == commit
    assert V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", None) == 12345
    assert V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", 12345) == 12345
    with pytest.raises(GardeArret, match="révision"):
        V.exiger_citations(p, "1" * 40, None)
    with pytest.raises(GardeArret, match="entropie"):
        V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", 999)
    (depot / "prereg" / "sans.md").write_text(f"- Commit du code d'analyse : `{commit}`\n")
    with pytest.raises(GardeArret, match="ne cite pas la révision"):
        V.exiger_citations(depot / "prereg" / "sans.md", "0e9e39f249a16976918f6564b8830bc894c89659", None)
    committer(depot)                                            # préenregistrements : hors de l'arbre gelé
    assert V.exiger_code_cite(depot, p) == commit
    (depot / "src" / "module.py").write_text("x = 2\n")       # artefact : code modifié puis committé
    committer(depot)
    with pytest.raises(GardeArret, match="arbre gelé .* modifié depuis le commit cité"):
        V.exiger_code_cite(depot, p)
    with pytest.raises(GardeArret, match="ne cite pas le commit"):
        V.exiger_code_cite(depot, depot / "README")
    racine = Path(controle_ia.__file__).resolve().parents[2]
    V.exiger_code_importe_sous(racine)                          # cas sain : le code vient de src/ du dépôt
    with pytest.raises(GardeArret, match="hors de la racine"):
        V.exiger_code_importe_sous(depot)


def test_sortie_des_tests_scellee_et_lue(depot, tmp_path_factory):
    """Rem-8 : la sortie de pytest sur l'instance devient un résultat scellé, rattaché au manifeste, et se lit."""
    dehors = tmp_path_factory.mktemp("sorties")                 # hors du dépôt, comme sur l'instance
    ok = dehors / "tests-ok.txt"
    ok.write_text("....\n170 passed in 50.12s\n")
    gelee = dict(PETITE, tests_attendus=170)
    s = V.executer(depot, "20261004-190000-repetition-jouet", entropie=3, config=gelee, sortie_tests=ok,
                   verifier_import=False)
    assert s["lecture"]["tests_instance"] == "conforme"
    corps = json.loads((depot / "diag" / "20261004-190000-repetition-jouet" / "tests-instance.json").read_text())
    assert corps["resultat"]["derniere_ligne"] == "170 passed in 50.12s"
    reussis = lambda run: json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"][
        "tests_instance"]["reussis"]
    assert reussis("20261004-190000-repetition-jouet") is True
    committer(depot)
    ko = dehors / "tests-ko.txt"
    ko.write_text("..s.\n169 passed, 1 skipped in 50.12s\n")       # contre-lecture 4, Q-2 : champ aligné sur P0
    s = V.executer(depot, "20261004-190100-repetition-jouet", entropie=3, config=gelee, sortie_tests=ko,
                   verifier_import=False)
    assert s["lecture"]["tests_instance"] == "contraire" and reussis("20261004-190100-repetition-jouet") is False
    for derniere in ("168 passed, 2 skipped in 5.0s", "169 passed in 5.0s", "170 passed, 1 xfailed in 5.0s",
                     "170 passed, 1 error in 5.0s"):
        assert V.lire({"tests_instance": {"derniere_ligne": derniere}}, gelee)["tests_instance"] == "contraire"
    for derniere in ("170 passed in 66.88s (0:01:06)", "170 passed, 3 warnings in 5.0s"):
        assert V.lire({"tests_instance": {"derniere_ligne": derniere}}, gelee)["tests_instance"] == "conforme"


def test_lecture_couverture_controle_negatif_audit_et_nan():
    def bilan(ecart=1e-6, ctx=1e-7, gen=1e-6, comparables=12, passent=12, remplies=3, finies=2, positions=40,
              lignes=(1, 6), zeros_gen=(1, 40)):
        return {"tolerance": 1e-4, "ecart_max": ecart, "max_contexte": ctx, "max_zone_generee": gen,
                "controle_negatif": {"comparables": comparables, "passent": passent,
                                     "fraction": passent / comparables if comparables else None},
                "couverture": {"actions_remplies": remplies, "actions_finies_avant": finies,
                               "positions_generees_comparees": positions, "lignes_echantillon": list(lignes)},
                "zeros": {"7": {"contexte": [5, 10], "generee": list(zeros_gen)},
                          "15": {"contexte": [5, 10], "generee": list(zeros_gen)}},
                "sondes_audit": {"tableaux_distincts": True, "ulp_vu": True}}

    def resume(**kw):
        return {"format": {"verifie": True}, "logique": {"equivalence": bilan(**kw)},
                "production": {"equivalence": dict(bilan(), tolerance=0.1), "rejeu_en_processus": [{"identique": True}]}}
    lire = lambda **kw: V.lire(resume(**kw), V.CONFIG_REELLE)
    assert lire()["logique_equivalence"] == "conforme"
    # N-2 : un écart concentré dans la zone générée (défaut de décodage, exp10 : 6e-4) reste « contraire »
    assert lire(ecart=6e-4, ctx=1.4e-7, gen=6e-4)["logique_equivalence"] == "contraire"
    assert lire(ecart=6e-4, ctx=4e-4, gen=6e-4)["logique_equivalence"] == "non concluant : précision probable"
    # contre-lecture 4, Q-2 : rapport des maxima ≤ 3 (M-2), dans les deux sens
    assert lire(ecart=2.9e-4, ctx=1e-4, gen=2.9e-4)["logique_equivalence"] == "non concluant : précision probable"
    assert lire(ecart=3.1e-4, ctx=1e-4, gen=3.1e-4)["logique_equivalence"] == "contraire"
    assert lire(ecart=3.1e-4, ctx=3.1e-4, gen=1e-4)["logique_equivalence"] == "contraire"
    assert lire(ecart=5e-2, ctx=4e-2, gen=5e-2)["logique_equivalence"] == "contraire"
    for manque in ({"remplies": 0}, {"finies": 0}, {"positions": 0}, {"lignes": (0,)}):
        assert lire(**manque)["logique_equivalence"] == "non concluant"
    # N-14 : contrôle négatif de phase
    assert lire(passent=11)["logique_controle_negatif"] == "contraire"           # 11/12 = 0,917 < 0,95
    assert lire(comparables=40, passent=39)["logique_controle_negatif"] == "conforme"
    assert lire(comparables=40, passent=37)["logique_controle_negatif"] == "contraire"
    assert lire(comparables=5, passent=5)["logique_controle_negatif"] == "non concluant"
    # N-9 : une valeur illisible n'est jamais conforme
    assert lire(ecart=float("inf"))["logique_equivalence"] == "contraire"
    assert lire(ecart=float("nan"))["logique_equivalence"] == "contraire"
    # N-1 : un audit déclenché maintient toujours la réserve
    assert lire()["audit_symetrie"] == "non déclenché"
    assert "réserve maintenue" in lire(zeros_gen=(40, 40))["audit_symetrie"]
    partiel = V.lire({"format": {"verifie": True}}, V.CONFIG_REELLE)
    assert partiel["production_equivalence"] == "non atteint" and partiel["rejeu_en_processus"] == "non atteint"


def test_codage_bfloat16_sans_perte_et_refus():
    x = torch.randn(5, 7).to(torch.bfloat16).to(torch.float32).numpy()
    c = P.coder(x, "bfloat16-bits")
    assert c.dtype == np.uint16 and c.nbytes == x.nbytes // 2
    assert np.array_equal(P.decoder(c, "bfloat16-bits"), x)
    with pytest.raises(GardeArret, match="non représentables"):
        P.coder(np.array([1.0 + 2 ** -20], dtype=np.float32), "bfloat16-bits")
    with pytest.raises(GardeArret, match="inconnu"):
        P.coder(x, "float16")


def test_empreinte_et_type_des_poids_en_demi_precision():
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    e32 = empreinte_poids(m)
    e16 = empreinte_poids(m.to(torch.bfloat16))
    assert e32 != e16 and e16 == empreinte_poids(modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4,
                                                              tetes_cle_valeur=2, intermediaire=64).to(torch.bfloat16))
    exiger_type_des_poids(m, "bfloat16")
    m.lm_head.weight.data = m.lm_head.weight.data.float()       # artefact : un tenseur resté en simple précision
    with pytest.raises(GardeArret, match="float32"):
        exiger_type_des_poids(m, "bfloat16")


def test_empreintes_des_fichiers_du_modele(tmp_path):
    """Rem-6 : fichiers du modèle contre les empreintes publiées (sha256 des gros fichiers, identifiant git sinon)."""
    import hashlib
    (tmp_path / "config.json").write_bytes(b'{"a": 1}\n')
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 1000)
    git = subprocess.run(["git", "hash-object", str(tmp_path / "config.json")], capture_output=True, text=True).stdout.strip()
    assert sha1_git(b'{"a": 1}\n') == git
    publies = {"config.json": {"git_sha1": git},
               "poids.safetensors": {"sha256": hashlib.sha256(b"\x00" * 1000).hexdigest()}}
    r = comparer_fichiers(tmp_path, publies)
    assert all(x["conforme"] for x in r.values()) and r["poids.safetensors"]["octets"] == 1000
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 999 + b"\x01")      # artefact : poids altérés
    with pytest.raises(GardeArret, match="poids.safetensors"):
        comparer_fichiers(tmp_path, publies)
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 1000)
    (tmp_path / "intrus.json").write_bytes(b"{}")                              # artefact : fichier inconnu du dépôt
    with pytest.raises(GardeArret, match="absent de la révision"):
        comparer_fichiers(tmp_path, publies)


def test_fichiers_du_modele_depuis_un_cache(tmp_path):
    """Le dossier de la révision se retrouve dans un cache au format de huggingface_hub, hors ligne."""
    from controle_ia.harnais.modeles import empreintes_fichiers_modele
    rev = "0e9e39f249a16976918f6564b8830bc894c89659"
    snap = tmp_path / "models--org--modele" / "snapshots" / rev
    snap.mkdir(parents=True)
    contenus = {n: f"{{\"{n}\": 1}}".encode() for n in ("config.json", "generation_config.json", "tokenizer.json",
                                                         "tokenizer_config.json")}
    contenus["model-00001-of-00001.safetensors"] = b"\x01" * 64
    publies = {}
    for n, c in contenus.items():
        (snap / n).write_bytes(c)
        publies[n] = ({"sha256": __import__("hashlib").sha256(c).hexdigest()} if n.endswith(".safetensors")
                      else {"git_sha1": sha1_git(c)})
    r = empreintes_fichiers_modele("org/modele", rev, publies=publies, cache_dir=str(tmp_path))
    assert set(r) == set(contenus) and all(x["conforme"] for x in r.values())
    with pytest.raises(GardeArret, match="absente du cache"):
        empreintes_fichiers_modele("org/modele", "1" * 40, publies=publies, cache_dir=str(tmp_path))
    (snap / "tokenizer.json").unlink()                                          # artefact : fichier essentiel manquant
    with pytest.raises(GardeArret, match="manquants"):
        empreintes_fichiers_modele("org/modele", rev, publies=publies, cache_dir=str(tmp_path))


# ---------------------------------------------------------------- contre-lecture 2 : gardes sans test (N-3) et suites

GABARIT_DATE = ("{% for m in messages %}<|im_start|>{{ m['role'] }}\n{% if loop.first %}Today Date: "
                "{{ date_string | default('04 Oct 2026') }}\n{% endif %}{{ m['content'] }}<|im_end|>\n{% endfor %}"
                "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")


def test_garde_de_date_d_en_tete():
    tok = tokeniseur_caracteres_chat()
    tok.chat_template = GABARIT_DATE
    m = modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    config = dict(PETITE, format=dict(PETITE["format"], texte_attendu_ouverture="Today Date: 26 Jul 2024"))
    fmt, f = V.format_du_modele(m, tok, config)                       # cas sain : la variable figée est lue
    assert "Today Date: 26 Jul 2024" in f["ouverture"] and f["verifie"]
    tok.chat_template = GABARIT_DATE.replace("{{ date_string | default('04 Oct 2026') }}", "04 Oct 2026")
    with pytest.raises(GardeArret, match="ne lit pas les variables figées"):   # artefact : date du jour imposée
        V.format_du_modele(m, tok, config)


def _point_de_controle(dossier, dtype):
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(5, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64).to(dtype)
    m.save_pretrained(dossier)
    tok.save_pretrained(dossier)


def _rediriger(monkeypatch, dossier):
    import transformers
    for classe in (transformers.AutoConfig, transformers.AutoTokenizer, transformers.AutoModelForCausalLM):
        vraie = classe.from_pretrained
        monkeypatch.setattr(classe, "from_pretrained",
                            lambda nom, revision=None, _v=vraie, **kw: _v(str(dossier), **kw))


def test_charger_modele_conversion_exacte_et_type_natif(tmp_path, monkeypatch):
    """Chargement bfloat16 puis conversion sur l'appareil : identique au chargement direct en simple précision ; un
    point de contrôle qui n'est pas en bfloat16 est refusé (la conversion ne serait pas exacte)."""
    from transformers import AutoModelForCausalLM
    from controle_ia.harnais.modeles import charger_modele
    rev = "0e9e39f249a16976918f6564b8830bc894c89659"
    bf16 = tmp_path / "bf16"
    _point_de_controle(bf16, torch.bfloat16)
    direct = AutoModelForCausalLM.from_pretrained(str(bf16), dtype=torch.float32)
    _rediriger(monkeypatch, bf16)
    m32, tok = charger_modele("meta-llama/Llama-3.1-8B-Instruct", rev, "float32", "cpu")
    a, b = m32.state_dict(), direct.state_dict()
    assert a.keys() == b.keys() and all(torch.equal(a[k], b[k]) for k in a)
    assert all(p.dtype == torch.float32 for p in m32.parameters()) and len(tok) == len(tokeniseur_caracteres_chat())
    m16, _ = charger_modele("meta-llama/Llama-3.1-8B-Instruct", rev, "bfloat16", "cpu")
    assert all(p.dtype == torch.bfloat16 for p in m16.parameters())
    m64, _ = charger_modele("meta-llama/Llama-3.1-8B-Instruct", rev, "float64", "cpu")   # version 2 : logique
    direct64 = AutoModelForCausalLM.from_pretrained(str(bf16), dtype=torch.float64)
    a, b = m64.state_dict(), direct64.state_dict()
    assert all(p.dtype == torch.float64 for p in m64.parameters()) and all(torch.equal(a[k], b[k]) for k in a)
    assert m64.normalisations_en_double == 2 * 2 + 1 and not hasattr(m32, "normalisations_en_double")
    fp32 = tmp_path / "fp32"                                              # artefact : point de contrôle en simple précision
    _point_de_controle(fp32, torch.float32)
    monkeypatch.undo()
    _rediriger(monkeypatch, fp32)
    with pytest.raises(GardeArret, match="pas en bfloat16"):
        charger_modele("meta-llama/Llama-3.1-8B-Instruct", rev, "float32", "cpu")


def test_gardes_differees_de_bout_en_bout(depot, monkeypatch):
    """Défaut de logique injecté (relecture des captures décalée) : la phase de logique va à son terme, les gardes de
    fin de phase arrêtent, `arret.json` porte les profils complets et la lecture partielle « contraire »."""
    import controle_ia.harnais.episode as E
    vraie = E.relire_crochets_lot
    monkeypatch.setattr(E, "relire_crochets_lot", lambda brut, k, lc, plan, n: vraie(brut, k, lc + 1, plan, n))
    with pytest.raises(GardeArret, match="logique : .* faute"):
        V.executer(depot, "20261004-200000-repetition-jouet", entropie=9, config=PETITE, verifier_import=False)
    arret = json.loads((depot / "diag" / "20261004-200000-repetition-jouet" / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "logique" and arret["partiel"]["logique"]["equivalence"]["actions_comparees"] == 12
    assert arret["partiel"]["lecture_partielle"]["logique_equivalence"] == "contraire"
    assert arret["partiel"]["lecture_partielle"]["production_equivalence"] == "non atteint"


def test_rejeu_refuse_avant_calcul_et_arret_de_comparaison(depot, monkeypatch):
    (depot / "src").mkdir()
    (depot / "src" / "module.py").write_text("x = 1\n")
    committer(depot)
    V.executer(depot, "20261004-210000-repetition-jouet", entropie=4, config=PETITE, verifier_import=False)
    committer(depot)
    # arrêt de comparaison consigné, puis propagé
    def comparaison_en_echec(racine, a, b):
        raise GardeArret("comparaison impossible (artefact)")
    monkeypatch.setattr(V, "comparer_runs", comparaison_en_echec)
    with pytest.raises(GardeArret, match="artefact"):
        V.executer(depot, "20261004-210100-repetition-jouet", config=PETITE, rejeu_de="20261004-210000-repetition-jouet",
                   verifier_import=False)
    assert (depot / "diag" / "20261004-210100-repetition-jouet" / "arret-comparaison-20261004-210000-repetition-jouet.json").is_file()
    monkeypatch.undo()
    committer(depot)
    # code différent de celui du run A : refusé avant tout calcul
    (depot / "src" / "module.py").write_text("x = 2\n")
    committer(depot)
    with pytest.raises(GardeArret, match="arbre gelé .* différent de celui du run A"):
        V.executer(depot, "20261004-210200-repetition-jouet", config=PETITE, rejeu_de="20261004-210000-repetition-jouet",
                   verifier_import=False)
    assert not (depot / "runs" / "20261004-210200-repetition-jouet").exists()


def test_rejeu_d_un_run_a_incomplet(depot):
    """N-16 : un run A arrêté (sans résumé) ne se rejoue pas : refus avant tout calcul."""
    incomplet = dict(PETITE, limite_s=-1)
    with pytest.raises(GardeArret, match="limite de durée"):
        V.executer(depot, "20261004-220000-repetition-jouet", entropie=2, config=incomplet, verifier_import=False)
    committer(depot)
    with pytest.raises(GardeArret, match="résumé du run A absent"):
        V.executer(depot, "20261004-220100-repetition-jouet", config=incomplet, rejeu_de="20261004-220000-repetition-jouet",
                   verifier_import=False)
    assert not (depot / "runs" / "20261004-220100-repetition-jouet").exists()


def test_comparaison_voit_la_machine_et_le_chargement(depot, monkeypatch):
    """N-11 : un changement de carte, de pilote, de chargement, de gabarit ou de repère est une différence nommée."""
    V.executer(depot, "20261004-230000-repetition-jouet", entropie=8, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261004-230100-repetition-jouet", entropie=8, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def altere(racine, chemin):
        corps = vrai(racine, chemin)
        if "230100" in str(chemin):
            r = corps["resultat"]
            r["reglages"]["pilote"] = "999.0"
            r["chargement"]["attention"] = "eager"
            r["format"]["gabarit_sha256"] = "0" * 64
            r["production"]["repere_precision"]["0"]["max"] = 1.0
        return corps
    monkeypatch.setattr(V, "verifier_resultat", altere)
    c = V.comparer_runs(depot, "20261004-230000-repetition-jouet", "20261004-230100-repetition-jouet")
    motifs = {d.get("motif") for d in c["differences"]}
    assert {"reglages différents", "chargement différents", "format différents",
            "repère de précision différent"} <= motifs and c["lecture"] == "contraire"


# ---------------------------------------------------------------- contre-lecture 3

def test_p4_contraire_se_lit_au_vu_du_repere(depot):
    """M-1 : un écart de production au-dessus du seuil arrête le run après le repère, le rejeu et le stockage."""
    stricte = dict(PETITE, production=dict(PETITE["production"], tolerance=1e-9))
    with pytest.raises(GardeArret, match="production : .* faute"):
        V.executer(depot, "20261004-240000-repetition-jouet", entropie=11, config=stricte, verifier_import=False)
    arret = json.loads((depot / "diag" / "20261004-240000-repetition-jouet" / "arret.json").read_text())["resultat"]
    prod = arret["partiel"]["production"]
    assert arret["phase"] == "production" and {"repere_precision", "rejeu_en_processus", "stockage"} <= set(prod)
    assert "empreintes_logits" in prod["rejeu_en_processus"][0]                          # M-8
    assert arret["partiel"]["lecture_partielle"]["production_equivalence"] == "contraire"


def test_p0_tests_conformes():
    """M-4 : exactement N tests réussis, rien d'autre."""
    assert V.tests_conformes("....\n170 passed in 66.88s (0:01:06)\n", 170)
    assert V.tests_conformes("170 passed, 2 warnings in 5.0s", 170)
    for mauvaise in ("169 passed in 5.0s", "170 passed, 1 skipped in 5.0s", "170 passed, 1 xpassed in 5.0s",
                     "170 passed, 2 deselected in 5.0s", "1 failed, 169 passed in 5.0s", "", "170 passed in 5.0s\nfin"):
        assert not V.tests_conformes(mauvaise, 170)
    assert not V.tests_conformes("170 passed in 5.0s", None)


def test_gardes_de_la_carte_dans_regler_determinisme(monkeypatch):
    """M-4 : branche « carte » de `regler_determinisme`, testable sans carte : indisponible, réglage cuBLAS refusé."""
    from controle_ia.harnais.modeles import regler_determinisme
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    with pytest.raises(GardeArret, match="indisponible"):
        regler_determinisme(1, "cuda")
    monkeypatch.setattr(torch.cuda, "is_available", lambda: True)
    monkeypatch.setenv("CUBLAS_WORKSPACE_CONFIG", ":0:0")
    with pytest.raises(GardeArret, match="déterminisme non garanti"):
        regler_determinisme(1, "cuda")
    regler_determinisme(1, "cpu")                                     # rétablit le réglage sur processeur


def test_plafonds_du_groupe_de_controle(tmp_path_factory):
    """M-11 : plafonds du groupe du processus et de ses ancêtres, en v1 comme en v2 ; le plus petit l'emporte."""
    d = tmp_path_factory.mktemp("cgroup")
    proc = d / "cgroup"
    proc.write_text("12:memory:/process_api/claude/bash\n0::/ignore\n")
    v1 = d / "fs" / "memory" / "process_api" / "claude" / "bash"
    v1.mkdir(parents=True)
    (v1 / "memory.limit_in_bytes").write_text("14345035776\n")
    (d / "fs" / "memory" / "memory.limit_in_bytes").write_text("9223372036854771712\n")
    (d / "fs" / "memory.max").write_text("max\n")
    fichiers = V.plafonds_cgroup(str(proc), str(d / "fs"))
    assert str(v1 / "memory.limit_in_bytes") in fichiers and str(d / "fs" / "memory" / "memory.limit_in_bytes") in fichiers
    meminfo = d / "meminfo"
    meminfo.write_text("MemTotal:       16500000 kB\n")
    r = V.exiger_memoire_vive(10, meminfo, fichiers)
    assert r["plafond_conteneur_go"] == 14.3 and r["effective_go"] == 14.3
    with pytest.raises(GardeArret, match="effective 14.3"):
        V.exiger_memoire_vive(15, meminfo, fichiers)


def test_arbre_gele_hors_dossiers_documentaires(depot):
    """M-5 : tout l'arbre est gelé par le commit cité, sauf les dossiers documentaires et les sorties."""
    (depot / ".gitignore").write_text("donnees/\n")
    (depot / "docs").mkdir()
    (depot / "docs" / "note.md").write_text("a\n")
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    p = _preregistrement(depot, commit)
    (depot / "docs" / "note.md").write_text("b\n")                 # documentaire : permis
    (depot / "registres").mkdir()
    (depot / "registres" / "etat.md").write_text("x\n")
    committer(depot)
    assert V.exiger_code_cite(depot, p) == commit
    (depot / ".gitignore").write_text("\n")                        # artefact : configuration de git modifiée
    committer(depot)
    with pytest.raises(GardeArret, match="arbre gelé"):
        V.exiger_code_cite(depot, p)


# ---------------------------------------------------------------- contre-lecture 4

def test_p0_refus_avant_le_manifeste_en_mode_decisif(depot, tmp_path_factory, monkeypatch):
    """Q-2 : en mode décisif, une sortie des tests non conforme arrête avant le manifeste (aucun run) ; une sortie
    conforme laisse aller jusqu'au manifeste."""
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    p = _preregistrement(depot, commit)
    committer(depot)                                            # préenregistrement hors de l'arbre gelé
    decisive = dict(V.CONFIG_REELLE, memoire_vive_min_go=0)
    sortie = tmp_path_factory.mktemp("sorties") / "tests.txt"
    run = "20261004-250000-validation-reelle"
    for mauvaise in (f"{V.CONFIG_REELLE['tests_attendus'] - 1} passed, 1 skipped in 5.0s\n", "",
                     f"{V.CONFIG_REELLE['tests_attendus']} passed in 5.0s\nfin\n"):
        sortie.write_text(mauvaise)
        with pytest.raises(GardeArret, match="P0 : .* aucun run"):
            V.executer(depot, run, revision="0e9e39f249a16976918f6564b8830bc894c89659", config=decisive, prereg=p,
                       sortie_tests=sortie, verifier_import=False)
        assert not (depot / "runs" / run).exists() and not (depot / "diag" / run).exists()
    sortie.write_text(f"....\n{V.CONFIG_REELLE['tests_attendus']} passed in 5.0s (0:00:05)\n")

    def manifeste(*a, **k):
        raise GardeArret("manifeste atteint")
    monkeypatch.setattr(V, "creer_manifeste", manifeste)
    with pytest.raises(GardeArret, match="manifeste atteint"):
        V.executer(depot, run, revision="0e9e39f249a16976918f6564b8830bc894c89659", config=decisive, prereg=p,
                   sortie_tests=sortie, verifier_import=False)


def test_plafonds_v2_et_minimum_des_ancetres(tmp_path_factory):
    """Q-2 : groupe de contrôle v2 (ligne « 0:: », memory.max) ; le plus petit plafond du groupe et de ses
    ancêtres l'emporte, même porté par un ancêtre ; « max » ne compte pas."""
    d = tmp_path_factory.mktemp("cgroup2")
    proc = d / "cgroup"
    proc.write_text("0::/user.slice/session-1.scope\n")
    feuille = d / "fs" / "user.slice" / "session-1.scope"
    feuille.mkdir(parents=True)
    (feuille / "memory.max").write_text("12000000000\n")
    (d / "fs" / "user.slice" / "memory.max").write_text("8000000000\n")
    (d / "fs" / "memory.max").write_text("max\n")
    fichiers = V.plafonds_cgroup(str(proc), str(d / "fs"))
    assert fichiers[0] == str(feuille / "memory.max") and fichiers[-1] == str(d / "fs" / "memory.max")
    meminfo = d / "meminfo"
    meminfo.write_text("MemTotal:       16500000 kB\n")
    r = V.exiger_memoire_vive(5, meminfo, fichiers)
    assert r["plafond_conteneur_go"] == 8.0 and r["effective_go"] == 8.0
    with pytest.raises(GardeArret, match="effective 8.0"):
        V.exiger_memoire_vive(10, meminfo, fichiers)


# ---------------------------------------------------------------- version 2 (N-010, option a)

def test_capture_en_double_precision_et_sonde_d_un_ulp():
    """La capture garde la double précision ; la simple et la demi-précision passent en simple précision (exact) ;
    la sonde d'audit perturbe d'un ulp dans le type capturé."""
    from controle_ia.harnais.activations import Crochets, sonde_de_comparaison
    for type_modele, attendu in ((torch.float64, np.float64), (torch.float32, np.float32), (torch.bfloat16, np.float32)):
        m = modele_jouet(3, 40, couches=2, largeur=16, tetes=2, tetes_cle_valeur=1, intermediaire=32).to(type_modele).eval()
        with torch.no_grad(), Crochets(m, [0, 1]) as c:
            m(torch.tensor([[1, 2, 3, 4]]), use_cache=False)
            acts = c.vider()
        assert all(a.dtype == attendu for a in acts.values())
    g = {0: np.random.default_rng(0).standard_normal((5, 8))}
    p = {0: g[0].copy()}
    assert sonde_de_comparaison(g, p) == {"tableaux_distincts": True, "ulp_vu": True}
    assert np.nextafter(np.float64(1.0), np.inf) - 1.0 < np.finfo(np.float32).eps      # un ulp double ≪ un ulp simple


def _sorties_controle_positif(maxima, jetons=9):
    """Sorties factices : une action par entrée, maxima de la zone générée par couche."""
    class Ep:
        identifiant = "episode-1"
    rapport = {"ecarts": {}, "profils": {}}
    for k, mx in enumerate(maxima):
        cle = f"0,{k}"
        rapport["ecarts"][cle] = {c: 0.0 for c in mx}
        rapport["profils"][cle] = {c: {"generee": {"jetons": jetons, "max": v}, "contexte": {"jetons": 5, "max": 2e-16}}
                                   for c, v in mx.items()}
    return [(Ep(), None, rapport)]


def test_bilan_et_garde_du_controle_positif():
    """Le défaut D1 est vu si, à chaque couche, le maximum de la zone générée dépasse le seuil de logique ; une
    action courte est comptée à part ; un NaN n'est jamais vu ; sous le nombre minimal d'actions, rien ne se juge."""
    c, cp = {"tolerance": 1e-4}, dict(V.CONFIG_REELLE["controle_positif"])
    vus = [{7: 3e-3, 15: 5e-3, 23: 8e-3}] * 12
    b = V.bilan_controle_positif(_sorties_controle_positif(vus), c, cp)
    assert (b["comparables"], b["vus"], b["fraction"]) == (12, 12, 1.0) and b["min_des_maxima"] == 3e-3
    assert b["max_contexte"] == 2e-16                                 # descriptif (R4) : D1 ne touche pas le contexte
    V.exiger_controle_positif(b, cp, "sain")
    aveugle = vus[:10] + [{7: 3e-3, 15: 5e-5, 23: 8e-3}, {7: float("nan"), 15: 5e-3, 23: 8e-3}]
    b2 = V.bilan_controle_positif(_sorties_controle_positif(aveugle), c, cp)
    assert b2["vus"] == 10 and b2["manques"] == ["episode-1:0,10", "episode-1:0,11"] and b2["min_des_maxima"] == float("-inf")
    with pytest.raises(GardeArret, match="défaut D1 injecté non vu"):
        V.exiger_controle_positif(b2, cp, "artefact")
    courtes = V.bilan_controle_positif(_sorties_controle_positif(vus, jetons=3), c, cp)
    assert courtes["comparables"] == 0 and courtes["courtes"] == 12
    V.exiger_controle_positif(courtes, cp, "trop peu d'actions : rien ne se juge")


def test_lecture_du_controle_positif():
    def resume(bilan=None):
        r = {"format": {"verifie": True}}
        if bilan is not None:
            r["controle_positif"] = {"bilan": bilan}
        return r
    lire = lambda r: V.lire(r, V.CONFIG_REELLE)["controle_positif"]           # noqa: E731
    assert lire(resume()) == "non atteint"
    assert lire(resume({"comparables": 9, "fraction": 1.0})) == "non concluant"
    assert lire(resume({"comparables": 20, "fraction": 0.95})) == "conforme"
    assert lire(resume({"comparables": 20, "fraction": 0.9})) == "contraire"


def test_controle_positif_aveugle_de_bout_en_bout(depot):
    """Artefact : seuil de logique trop lâche (1e-2) ; P2 passe, mais le défaut D1 (environ 5e-4 sur le jouet) n'est
    plus vu ; le run s'arrête en phase de contrôle positif, bilan et lecture consignés dans arret.json."""
    lache = dict(PETITE, logique=dict(PETITE["logique"], tolerance=1e-2))
    with pytest.raises(GardeArret, match="défaut D1 injecté non vu"):
        V.executer(depot, "20261005-120000-repetition-jouet", entropie=21, config=lache, verifier_import=False)
    arret = json.loads((depot / "diag" / "20261005-120000-repetition-jouet" / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "controle_positif"
    lp = arret["partiel"]["lecture_partielle"]
    assert lp["logique_equivalence"] == "conforme" and lp["controle_positif"] == "contraire"
    assert lp["production_equivalence"] == "non atteint"


def test_reglages_relus_et_noyaux_permis():
    from controle_ia.harnais.modeles import noyaux_attention_permis, regler_determinisme
    r = regler_determinisme(1, "cpu")
    assert r["relus"]["algorithmes_deterministes"] is True and r["relus"]["fils"] == 1
    with V.noyau("math"):
        permis = noyaux_attention_permis()
    assert permis["math"] is True and permis["flash"] is False and permis["memoire_efficace"] is False
    hors = noyaux_attention_permis()
    assert hors["flash"] is True                                       # le contexte rétablit les noyaux à sa sortie


def test_comparaison_voit_le_controle_positif_mais_pas_sa_duree(depot, monkeypatch):
    V.executer(depot, "20261005-130000-repetition-jouet", entropie=9, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261005-130100-repetition-jouet", entropie=9, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261005-130200-repetition-jouet", entropie=9, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def duree(racine, chemin):
        corps = vrai(racine, chemin)
        if "130100" in str(chemin):
            corps["resultat"]["controle_positif"]["debit"]["generation_s"] += 1.0
            corps["resultat"]["controle_positif"]["memoire_max_go"] = 99.0          # descriptif, hors comparaison
        return corps
    monkeypatch.setattr(V, "verifier_resultat", duree)
    assert V.comparer_runs(depot, "20261005-130000-repetition-jouet", "20261005-130100-repetition-jouet")["identique"]

    def bilan(racine, chemin):                                       # chaque comparaison s'écrit une fois (R12)
        corps = vrai(racine, chemin)
        if "130200" in str(chemin):
            corps["resultat"]["controle_positif"]["bilan"]["min_des_maxima"] += 1e-9
        return corps
    monkeypatch.setattr(V, "verifier_resultat", bilan)
    c = V.comparer_runs(depot, "20261005-130000-repetition-jouet", "20261005-130200-repetition-jouet")
    assert {"phase": "controle_positif", "motif": "contrôle positif différent"} in c["differences"]


def test_sonde_de_memoire_sans_lecture():
    """La sonde de mémoire (non décisive) tourne la charge de la phase de logique et ne rend que mémoire et durées :
    aucune équivalence, aucun écart (R1)."""
    from controle_ia.harnais.sonde_memoire import mesurer_charge
    m = modele_jouet(5, 200, couches=4, largeur=16, tetes=2, tetes_cle_valeur=1, intermediaire=32).to(torch.float64).eval()
    etapes = mesurer_charge(m, pad_id=0, lot=8, longueur=60, nouveaux=5, longueur_passe=70,
                            noyau=lambda: V.noyau("math"))
    assert set(etapes) == {"generation", "passe_unique"}
    assert etapes["generation"]["jetons_generes"] == 8 * 5 and etapes["generation"]["longueur_remplie"] == 60
    cles = {k for e in etapes.values() for k in e}
    assert not any(mot in k for k in cles for mot in ("ecart", "equivalence", "lecture"))


# ---------------------------------------------------------------- contre-lecture 1 de la v2

def test_normalisations_en_double():
    """V-1 : dans la phase de logique, chaque normalisation RMS calcule en double précision (la bibliothèque passe par
    la simple précision) ; le changement vaut pour ce modèle seulement ; garde : poids en double précision, au moins
    une normalisation."""
    from transformers.models.llama.modeling_llama import LlamaRMSNorm
    from controle_ia.harnais.modeles import _rms_en_double, normalisations_en_double
    m = modele_jouet(3, 40, couches=2, largeur=16, tetes=2, tetes_cle_valeur=1, intermediaire=32).to(torch.float64).eval()
    x = torch.randn(3, 5, 16, dtype=torch.float64, generator=torch.Generator().manual_seed(0)) * 3
    norme = m.model.norm
    with torch.no_grad():
        bibliotheque = norme(x)                                   # chemin de la bibliothèque : simple précision
        assert normalisations_en_double(m) == 2 * 2 + 1 and m.normalisations_en_double == 5
        double = norme(x)
        attendu = norme.weight * (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + norme.variance_epsilon))
    assert double.dtype == torch.float64 and torch.equal(double, attendu)
    assert not torch.equal(double, bibliotheque)                  # la simple précision arrondissait vraiment
    assert (double - bibliotheque).abs().max() < 1e-5             # même formule, à l'arrondi de simple précision près
    assert all(n.forward.__func__ is _rms_en_double for n in m.modules() if type(n).__name__.endswith("RMSNorm"))
    assert LlamaRMSNorm(16).to(torch.float64).forward.__func__ is LlamaRMSNorm.forward     # la classe n'est pas touchée
    with pytest.raises(GardeArret, match="poids en torch.float32"):
        normalisations_en_double(modele_jouet(3, 40, couches=2, largeur=16, tetes=2, tetes_cle_valeur=1,
                                              intermediaire=32))
    with pytest.raises(GardeArret, match="aucune normalisation"):
        normalisations_en_double(torch.nn.Linear(2, 2).double())


def test_arret_de_logique_garde_le_bilan_du_controle_positif(depot, monkeypatch):
    """V-2 : le contrôle positif est joué avant les gardes ; la garde de la logique passe avant la sienne. Artefact :
    P2 contraire (seuil de logique de 1e-30) et contrôle positif rendu aveugle : l'arrêt est en phase de logique, et
    arret.json garde le bilan du contrôle positif et sa lecture."""
    stricte = dict(PETITE, logique=dict(PETITE["logique"], tolerance=1e-30))
    vrai = V.bilan_controle_positif

    def aveugle(sorties, c, cp):
        return dict(vrai(sorties, c, cp), vus=0, fraction=0.0, manques=["artefact"])
    monkeypatch.setattr(V, "bilan_controle_positif", aveugle)
    with pytest.raises(GardeArret, match="logique : .*faute"):
        V.executer(depot, "20261005-140000-repetition-jouet", entropie=21, config=stricte, verifier_import=False)
    arret = json.loads((depot / "diag" / "20261005-140000-repetition-jouet" / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "logique"
    pc = arret["partiel"]["controle_positif"]
    assert pc["bilan"]["fraction"] == 0.0 and pc["T"] == PETITE["controle_positif"]["T"]
    lp = arret["partiel"]["lecture_partielle"]
    assert lp["logique_equivalence"] == "contraire" and lp["controle_positif"] == "contraire"


def test_controle_positif_graines_propres_T_et_trajectoires(depot, monkeypatch):
    """V-2, V-9 : le contrôle positif tire ses graines de ses propres tâches (« controle-positif/… »), joue T pas du
    contrôle positif (pas ceux de la logique), seul injecte D1, écrit ses trajectoires dans diag/ ; son contexte, que
    D1 ne touche pas, reste au niveau de l'arrondi de la double précision."""
    appels = []
    vrai = V.jouer_phase

    def espion(modele, fmt, c, graines, phase, couches, **kw):
        appels.append((phase, c["T"], kw.get("decalage_positions", 0)))
        return vrai(modele, fmt, c, graines, phase, couches, **kw)
    monkeypatch.setattr(V, "jouer_phase", espion)
    run = "20261005-140100-repetition-jouet"
    V.executer(depot, run, entropie=5, config=PETITE, verifier_import=False)
    cp = PETITE["controle_positif"]
    assert cp["T"] != PETITE["logique"]["T"]
    assert ("controle-positif", cp["T"], cp["decalage_positions"]) in appels
    assert ("controle-positif-chemin", cp["T"], cp["decalage_positions"]) in appels      # version 3
    assert all(d == 0 for phase, _, d in appels if not phase.startswith("controle-positif"))
    resume = json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"]
    trajectoires = sorted((depot / "diag" / run).glob("controle-positif-episode-*-trajectoire.json"))
    assert len(trajectoires) == PETITE["logique"]["episodes"]
    t0 = json.loads(trajectoires[0].read_text())["resultat"]
    assert t0["T"] == cp["T"] and all(len(tr["actions"]) == cp["T"] for tr in t0["transcriptions"])
    assert resume["controle_positif"]["bilan"]["max_contexte"] < 1e-12
    assert resume["chargement"]["normalisations_en_double"] == 2 * PETITE["modele_jouet"]["couches"] + 1


def test_sonde_d_un_ulp_dans_le_type_capture(monkeypatch):
    """V-10 : la sonde d'audit perturbe d'un ulp du type capturé (double précision : bien moins qu'un ulp de simple
    précision)."""
    import controle_ia.harnais.activations as A
    vus = []
    vrai = A.ecarts_par_jeton
    monkeypatch.setattr(A, "ecarts_par_jeton", lambda g, p: (vus.append(np.array(p, copy=True)), vrai(g, p))[1])
    for dtype in (np.float64, np.float32):
        vus.clear()
        g = {0: np.random.default_rng(1).standard_normal((4, 8)).astype(dtype)}
        assert A.sonde_de_comparaison(g, {0: g[0].copy()})["ulp_vu"]
        avant, apres = vus
        delta = float(apres[0, 0]) - float(avant[0, 0])
        assert apres.dtype == dtype and 0 < delta <= np.finfo(dtype).eps * abs(float(avant[0, 0]))
        if dtype == np.float64:
            assert delta < np.finfo(np.float32).eps * abs(float(avant[0, 0])) / 2


def test_configuration_decisive_v3():
    """V-2 ; version 3 (N-011, option a) : valeurs gelées qu'aucune garde ne vérifie par ailleurs."""
    c, r = V.CONFIG_REELLE, V.CONFIG_REPETITION
    assert c["logique"]["dtype"] == "float64" and c["logique"]["noyau_attention"] == "math"
    assert c["logique"]["tolerance"] == 1e-4 and c["logique"]["statistique"] == "max"
    assert (c["chemin"]["dtype"], c["chemin"]["noyau_attention"], c["chemin"]["tolerance"],
            c["chemin"]["statistique"]) == ("float32", "math", 3e-3, "max")
    assert (c["production"]["noyau_attention"], c["production"]["tolerance"], c["production"]["statistique"]) == (
        "math", 0.2, "q99")
    assert {k: c["chemin"][k] for k in ("episodes", "N", "T", "max_nouveaux", "taille_lot", "episodes_equivalence")} == \
        {k: c["logique"][k] for k in ("episodes", "N", "T", "max_nouveaux", "taille_lot", "episodes_equivalence")}
    assert c["controle_positif"] == {"T": 5, "decalage_positions": 1, "positions_min": 4, "actions_min": 10,
                                     "fraction_min": 0.95}
    assert c["memoire_carte_min_gio"] == 130 and c["memoire_vive_min_go"] == 96
    assert c["controle_positif"]["T"] != c["logique"]["T"] and r["controle_positif"]["T"] != r["logique"]["T"]


# ---------------------------------------------------------------- version 3 (N-011, option a)

def test_statistique_q99_garde_et_controle_negatif():
    """La garde de production lit le 99e centile des écarts par jeton (par action et par couche) : quelques jetons de
    la queue d'arrondi de la demi-précision ne l'arrêtent pas ; un désalignement, qui touche presque tous les jetons,
    l'arrête. Le contrôle négatif lit la même grandeur."""
    from controle_ia.harnais.activations import ecart_decale_zone_generee, ecart_equivalence
    from controle_ia.harnais.episode import bilan_controle_negatif, exiger_gardes
    rng = np.random.default_rng(0)
    p = {7: rng.standard_normal((300, 16))}
    g = {7: p[7] * (1 + 0.01 * rng.standard_normal((300, 1)))}            # arrondi : ≈ 1 % par jeton
    g[7][5] = p[7][5] * 1.5                                                # un jeton de queue : 50 %
    mx, q99 = ecart_equivalence(g, p)[7], ecart_equivalence(g, p, quantile=0.99)[7]
    assert mx > 0.4 and q99 < 0.05
    rapport = {"tolerance": 0.2, "statistique": "q99", "ecarts": {"0,0": {7: mx}}, "ecarts_q99": {"0,0": {7: q99}}}
    exiger_gardes(rapport, "0,0", "q99")                                   # passe : la queue ne l'arrête pas
    with pytest.raises(GardeArret, match="99|écarts"):
        exiger_gardes(dict(rapport, statistique="max"), "0,0", "max")      # sur le maximum, il s'arrêterait
    decale = {7: np.roll(p[7], 1, axis=0)}                                 # désalignement d'un jeton
    assert ecart_equivalence(decale, p, quantile=0.99)[7] > 0.5
    zone = ecart_decale_zone_generee(g, p, 100, 0.2)[7]
    assert {"max", "q99", "au_dessus", "positions"} <= set(zone) and zone["q99"] > 0.5
    sain = {"tolerance": 0.2, "statistique": "q99", "episode": "e",
            "controle_negatif_zone_generee": {"0,0": {7: {"max": 1.4, "q99": 1.3, "positions": 50}}}}
    aveugle = {"tolerance": 0.2, "statistique": "q99", "episode": "e",
               "controle_negatif_zone_generee": {"0,0": {7: {"max": 1.4, "q99": 0.1, "positions": 50}}}}
    assert bilan_controle_negatif([sain])["passent"] == 1 and bilan_controle_negatif([sain])["statistique"] == "q99"
    assert bilan_controle_negatif([aveugle])["passent"] == 0                # le maximum seul ne suffit plus
    with pytest.raises(GardeArret, match="mêlées"):
        bilan_controle_negatif([sain, dict(aveugle, statistique="max")])


def test_lecture_de_la_production_sur_le_99e_centile():
    """La lecture de l'équivalence de production suit la grandeur de sa garde : le 99e centile par action ; le
    maximum reste rapporté, sans seuil."""
    bilan = {"tolerance": 0.2, "statistique": "q99", "ecart_max": 0.52, "ecart_q99_max": 0.1,
             "max_contexte": 0.52, "max_zone_generee": 0.08,
             "couverture": {"actions_remplies": 1, "actions_finies_avant": 1, "positions_generees_comparees": 9,
                            "lignes_echantillon": [1]},
             "controle_negatif": {"comparables": 40, "fraction": 1.0}, "zeros": {}}
    lire = lambda b: V.lire({"format": {"verifie": True}, "production": {"equivalence": b}},  # noqa: E731
                            V.CONFIG_REELLE)["production_equivalence"]
    assert lire(bilan) == "conforme"
    assert lire(dict(bilan, ecart_q99_max=0.3)) == "contraire"
    assert lire(dict(bilan, ecart_q99_max=float("nan"))) == "contraire"
    assert lire(dict(bilan, statistique="max")) == "contraire"             # sur le maximum : 0,52 > 0,2


def test_phase_chemin_de_bout_en_bout(depot):
    """La phase de chemin (simple précision, noyau et régime de production) et son contrôle positif sont joués,
    consignés et lus ; la production lit le 99e centile ; le débit consigne le noyau de production (qu'il y tourne
    est vérifié par `test_debit_au_noyau_de_production`)."""
    run = "20261006-100000-repetition-jouet"
    s = V.executer(depot, run, entropie=31, config=PETITE, verifier_import=False)
    assert s["lecture"] == LECTURE_SAINE
    r = json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"]
    ch, pcc, prod = r["chemin"], r["controle_positif_chemin"], r["production"]
    assert ch["dtype"] == "float32" and ch["chargement"]["type_des_poids"] == "torch.float32"
    assert ch["chargement"]["normalisations_en_double"] == 0 and ch["equivalence"]["statistique"] == "max"
    assert ch["equivalence"]["ecart_max"] <= PETITE["chemin"]["tolerance"] < pcc["bilan"]["min_des_maxima"]
    assert pcc["bilan"]["comparables"] >= 4 and pcc["bilan"]["vus"] == pcc["bilan"]["comparables"]
    assert pcc["T"] == PETITE["controle_positif"]["T"]
    assert prod["equivalence"]["statistique"] == "q99"
    assert prod["equivalence"]["ecart_q99_max"] <= prod["equivalence"]["ecart_max"]
    assert prod["equivalence"]["controle_negatif"]["statistique"] == "q99"
    assert r["debit"]["noyau_attention"] == PETITE["production"]["noyau_attention"]
    d = depot / "diag" / run
    assert len(list(d.glob("chemin-episode-*-trajectoire.json"))) == PETITE["chemin"]["episodes"]
    assert len(list(d.glob("controle-positif-chemin-episode-*-trajectoire.json"))) == PETITE["chemin"]["episodes"]


def test_chemin_aveugle_de_bout_en_bout(depot):
    """Artefact : seuil du chemin trop lâche (1e-2 sur le jouet, où D1 vaut environ 2e-4) : la logique est conforme,
    le chemin aussi, mais son contrôle positif ne voit pas D1 ; le run s'arrête en phase de contrôle positif du
    chemin, bilans et lecture consignés."""
    lache = dict(PETITE, chemin=dict(PETITE["chemin"], tolerance=1e-2))
    with pytest.raises(GardeArret, match="contrôle positif du chemin : défaut D1 injecté non vu"):
        V.executer(depot, "20261006-100100-repetition-jouet", entropie=21, config=lache, verifier_import=False)
    arret = json.loads((depot / "diag" / "20261006-100100-repetition-jouet" / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "controle_positif_chemin"
    lp = arret["partiel"]["lecture_partielle"]
    assert lp["logique_equivalence"] == lp["controle_positif"] == lp["chemin_equivalence"] == "conforme"
    assert lp["controle_positif_chemin"] == "contraire" and lp["production_equivalence"] == "non atteint"


def test_configuration_v3_refusee():
    """Gardes de configuration de la version 3 : chemin en simple précision sur le maximum ; production sur le
    99e centile ; noyau de production fixé (hors jouet) et emprunté par le chemin."""
    reelle = V.CONFIG_REELLE
    rev = "0e9e39f249a16976918f6564b8830bc894c89659"
    V.valider_config(reelle, rev)
    for mauvaise, motif in (
            (dict(reelle, chemin=dict(reelle["chemin"], dtype="bfloat16")), "chemin"),
            (dict(reelle, chemin=dict(reelle["chemin"], statistique="q99")), "chemin"),
            (dict(reelle, production=dict(reelle["production"], statistique="max")), "99e centile"),
            (dict(reelle, production=dict(reelle["production"], noyau_attention="defaut"),
                  chemin=dict(reelle["chemin"], noyau_attention="defaut")), "noyau"),
            (dict(reelle, chemin=dict(reelle["chemin"], noyau_attention="defaut")), "noyau"),
            (dict(reelle, production=dict(reelle["production"], statistique="moyenne")), "statistique")):
        with pytest.raises(GardeArret, match=motif):
            V.valider_config(mauvaise, rev)


def test_comparaison_voit_le_chemin(depot, monkeypatch):
    """La comparaison des runs A et B porte aussi sur la phase de chemin (empreintes, profils, chargement) et sur
    son contrôle positif (sans sa durée ni son pic de mémoire)."""
    V.executer(depot, "20261006-100200-repetition-jouet", entropie=8, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261006-100300-repetition-jouet", entropie=8, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def altere(racine, chemin):
        corps = vrai(racine, chemin)
        if "100300" in str(chemin):
            r = corps["resultat"]
            r["chemin"]["episodes"][1]["empreintes"]["activations"] = "0" * 64
            r["chemin"]["chargement"]["type_des_poids"] = "torch.float16"
            r["controle_positif_chemin"]["bilan"]["min_des_maxima"] += 1e-9
        return corps
    monkeypatch.setattr(V, "verifier_resultat", altere)
    c = V.comparer_runs(depot, "20261006-100200-repetition-jouet", "20261006-100300-repetition-jouet")
    assert {"phase": "chemin", "episode": "episode-1", "empreinte": "activations"} in c["differences"]
    assert any(d.get("phase") == "chemin" and d.get("motif") == "chargement différent" for d in c["differences"])
    assert {"phase": "controle_positif_chemin", "motif": "contrôle positif différent"} in c["differences"]


def test_repere_au_noyau_de_production(depot, monkeypatch):
    """Version 3 : le repère de précision se calcule au noyau d'attention de la production, comme la génération et la
    passe unique qu'il situe (« math » sur le modèle réel) ; hors de ce contexte, il tournerait aux noyaux par défaut,
    non consignés."""
    actifs, vus = [], []
    vrai_noyau, vrai_repere = V.noyau, V.repere_precision

    @contextlib.contextmanager
    def espion_noyau(nom):
        actifs.append(nom)
        try:
            with vrai_noyau(nom):
                yield
        finally:
            actifs.pop()

    def espion_repere(*a, **kw):
        vus.append(list(actifs))
        return vrai_repere(*a, **kw)
    monkeypatch.setattr(V, "noyau", espion_noyau)
    monkeypatch.setattr(V, "repere_precision", espion_repere)
    run = "20261006-110000-repetition-jouet"
    V.executer(depot, run, entropie=8, config=PETITE, verifier_import=False)
    assert vus == [[PETITE["production"]["noyau_attention"]]]
    r = json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"]
    assert set(r["production"]["repere_precision"]) == {str(c) for c in r["production"]["couches"]}


# ---------------------------------------------------------------- contre-lecture 1 de la v3 (X-2, X-4, X-10)

def test_chaine_du_99e_centile_de_bout_en_bout(depot):
    """X-4 : dans un run de bout en bout, pour chaque action comparée de chaque phase, la grandeur de la garde de
    production (`ecarts_q99`) est le 99e centile des écarts par jeton sur toutes les positions capturées (champ
    `q99` du profil, calculé à part) ; le bilan lit le maximum de ces 99e centiles, pas celui des maxima."""
    run = "20261006-120000-repetition-jouet"
    V.executer(depot, run, entropie=13, config=PETITE, verifier_import=False)
    r = json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"]
    differents = 0
    for phase in V.PHASES_COMPAREES:
        q99s = []
        for e in r[phase]["episodes"]:
            eq = e["equivalence"]
            for cle, par_couche in eq["ecarts_q99"].items():
                for c, v in par_couche.items():
                    assert v == eq["profils"][cle][c]["q99"]
                    q99s.append(v)
                    differents += v != eq["ecarts"][cle][c]
        assert q99s and r[phase]["equivalence"]["ecart_q99_max"] == max(q99s)
    assert differents > 0                                                  # le 99e centile n'est pas le maximum


def test_controle_negatif_q99_lit_la_grandeur_de_la_garde():
    """X-2, X-4 : en production, le contrôle négatif lit le 99e centile sur les positions que lit la garde (contexte
    non décalé, zone générée décalée), ni sur la zone générée seule, ni à la médiane. Un décalage confiné à une zone
    générée de moins de 1 % des positions échappe à la garde : le contrôle négatif le montre."""
    from controle_ia.harnais.activations import ecart_decale_zone_generee, ecart_equivalence, ecarts_par_jeton
    from controle_ia.harnais.episode import bilan_controle_negatif
    rng = np.random.default_rng(3)

    def cas(lc, m):
        p = {7: rng.standard_normal((lc + m, 16))}
        return {7: p[7] * (1 + 0.01 * rng.standard_normal((lc + m, 1)))}, p
    g, p = cas(80, 20)                                     # zone générée de 20 % des positions : décalage vu
    z = ecart_decale_zone_generee(g, p, 80, 0.2)[7]
    attendu = np.quantile(np.concatenate([ecarts_par_jeton(g[7][:80], p[7][:80]),
                                          ecarts_par_jeton(g[7][81:], p[7][80:99])]), 0.99)
    assert z["q99"] == attendu and z["q99"] > 0.2
    g, p = cas(2000, 15)                                   # 15 positions générées sur 2 015 : moins de 1 %
    z = ecart_decale_zone_generee(g, p, 2000, 0.2)[7]
    seule = np.quantile(ecarts_par_jeton(g[7][2001:], p[7][2000:2014]), 0.99)
    decale = {7: np.concatenate([g[7][:2000], p[7][1999:2014]])}           # zone générée décalée d'un jeton
    assert seule > 0.2 and z["q99"] < 0.2
    assert ecart_equivalence(decale, p, quantile=0.99)[7] < 0.2            # la garde ne verrait pas le décalage
    rapport = {"tolerance": 0.2, "statistique": "q99", "episode": "e", "controle_negatif_zone_generee": {"0,0": {7: z}}}
    assert bilan_controle_negatif([rapport])["passent"] == 0


def test_lecture_du_chemin_couverture_audit_et_maximum():
    """X-4 : la lecture du chemin exige la couverture et se fait sur le maximum (pas sur le 99e centile) ; l'audit
    de symétrie couvre le chemin."""
    def bilan(ecart=1e-6, q99=1e-7, remplies=3, finies=2, zeros_gen=(1, 40), tol=3e-3, stat="max"):
        return {"tolerance": tol, "statistique": stat, "ecart_max": ecart, "ecart_q99_max": q99,
                "max_contexte": ecart, "max_zone_generee": ecart,
                "controle_negatif": {"comparables": 12, "passent": 12, "fraction": 1.0},
                "couverture": {"actions_remplies": remplies, "actions_finies_avant": finies,
                               "positions_generees_comparees": 40, "lignes_echantillon": [1, 6]},
                "zeros": {"7": {"contexte": [5, 10], "generee": list(zeros_gen)}},
                "sondes_audit": {"tableaux_distincts": True, "ulp_vu": True}}

    def lire(**kw):
        return V.lire({"format": {"verifie": True}, "logique": {"equivalence": bilan(tol=1e-4)},
                       "chemin": {"equivalence": bilan(**kw)},
                       "production": {"equivalence": bilan(tol=0.2, stat="q99"),
                                      "rejeu_en_processus": [{"identique": True}]}}, V.CONFIG_REELLE)
    assert lire()["chemin_equivalence"] == "conforme"
    assert lire(remplies=0)["chemin_equivalence"] == "non concluant"
    assert lire(finies=0)["chemin_equivalence"] == "non concluant"
    assert lire(ecart=5e-3, q99=1e-3)["chemin_equivalence"] == "contraire"   # le maximum, pas le 99e centile
    assert lire()["audit_symetrie"] == "non déclenché"
    assert "chemin" in lire(zeros_gen=(40, 40))["audit_symetrie"]


def test_arret_du_chemin_garde_le_bilan_de_son_controle_positif(depot):
    """X-4 : le contrôle positif du chemin est joué et consigné avant les gardes du chemin ; si C1 arrête le run
    (artefact : seuil du chemin de 1e-12), `arret.json` contient son bilan."""
    stricte = dict(PETITE, chemin=dict(PETITE["chemin"], tolerance=1e-12))
    run = "20261006-120100-repetition-jouet"
    with pytest.raises(GardeArret, match="chemin"):
        V.executer(depot, run, entropie=17, config=stricte, verifier_import=False)
    arret = json.loads((depot / "diag" / run / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "chemin"
    assert arret["partiel"]["controle_positif_chemin"]["bilan"]["comparables"] > 0
    assert arret["partiel"]["lecture_partielle"]["chemin_equivalence"] == "contraire"


def test_debit_au_noyau_de_production(depot, monkeypatch):
    """X-4 : chaque génération du débit tourne dans le contexte du noyau d'attention de la production."""
    actifs, vus = [], []
    vrai_noyau, vrai_generer = V.noyau, V.generer_lot

    @contextlib.contextmanager
    def espion_noyau(nom):
        actifs.append(nom)
        try:
            with vrai_noyau(nom):
                yield
        finally:
            actifs.pop()

    def espion_generer(*a, **kw):
        vus.append(list(actifs))
        return vrai_generer(*a, **kw)
    monkeypatch.setattr(V, "noyau", espion_noyau)
    monkeypatch.setattr(V, "generer_lot", espion_generer)
    V.executer(depot, "20261006-120200-repetition-jouet", entropie=19, config=PETITE, verifier_import=False)
    assert vus == [[PETITE["production"]["noyau_attention"]]] * len(PETITE["debit"]["tailles_lot"])


def test_panne_de_memoire_du_debit_consignee(depot, monkeypatch):
    """X-10 : le débit est descriptif ; un manque de mémoire de la carte y est consigné sans arrêter le run (résumé
    écrit, lectures inchangées) ; les lots plus grands ne sont pas tentés."""
    appels = []
    vrai = V.generer_lot

    def panne(modele, transcriptions, *a, **kw):
        appels.append(len(transcriptions))
        if len(transcriptions) >= PETITE["debit"]["tailles_lot"][1]:
            raise torch.cuda.OutOfMemoryError("CUDA out of memory (essai)")
        return vrai(modele, transcriptions, *a, **kw)
    monkeypatch.setattr(V, "generer_lot", panne)
    run = "20261006-120300-repetition-jouet"
    s = V.executer(depot, run, entropie=31, config=PETITE, verifier_import=False)
    assert s["lecture"] == LECTURE_SAINE
    d = json.loads((depot / "diag" / run / "resume.json").read_text())["resultat"]["debit"]
    assert d["panne_memoire"] is True and appels == PETITE["debit"]["tailles_lot"][:2]
    assert "jetons_par_s" in d["mesures"][0] and "OutOfMemoryError" in d["mesures"][1]["erreur"]


def test_autre_panne_du_debit_arrete_le_run(depot, monkeypatch):
    """X-10, artefact : seule la panne de mémoire du débit se consigne sans arrêt ; une autre exception (ici une
    garde) arrête le run en phase de débit, `arret.json` à l'appui, sans résumé."""
    def garde(*a, **kw):
        raise GardeArret("essai : garde pendant le débit")
    monkeypatch.setattr(V, "generer_lot", garde)
    run = "20261006-120400-repetition-jouet"
    with pytest.raises(GardeArret, match="pendant le débit"):
        V.executer(depot, run, entropie=29, config=PETITE, verifier_import=False)
    arret = json.loads((depot / "diag" / run / "arret.json").read_text())["resultat"]
    assert arret["phase"] == "debit" and not (depot / "diag" / run / "resume.json").exists()
