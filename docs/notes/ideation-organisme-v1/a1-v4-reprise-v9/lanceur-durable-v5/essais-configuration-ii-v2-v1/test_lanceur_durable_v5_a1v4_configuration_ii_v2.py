"""Essais en mode jouet du lanceur durable v5 d'A1-v4 (aucune location, aucun appel de modèle, aucun réseau, aucune clé réelle).

Chaque garde neuve est éprouvée sur un cas sain et sur un artefact (R5). Monde jouet : faux `vastai` (réponses en fichiers), faux
registre des GO (lignes de la course à 200 USD et de la machine à 35 USD, plus la ligne de dose-réponse à 100 USD), dépôt privé nu
qui admet les clones partiels (configuration des mondes et compagnon sur `main`), dépôt public jouet (lanceur gelé v4 factice,
fichiers gelés factices, texte v4-v1 scellé avec ses blocs), relais factice, Vast simulé par un fichier. Dates passées explicitement.

Lancement (depuis la racine du dépôt privé, `.venv` actif) :
    python -m pytest -q docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/test_lanceur_durable_v5_a1v4.py
"""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

import test_hote_durable_a1_v3 as t1  # monde jouet de la v1 (relais et lanceur factices, dépôt nu à branches)
from controle_ia import hote_durable_a1_v3 as h
from controle_ia import hote_durable_a1_v3_v4 as v4
from controle_ia import sonde_hote_durable_a1_v3_v10 as s10

ICI = Path('/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5')
_spec = importlib.util.spec_from_file_location("hote_durable_a1_v4_v5", ICI / "hote_durable_a1_v4_v5.py")
v5 = importlib.util.module_from_spec(_spec)
sys.modules["hote_durable_a1_v4_v5"] = v5
_spec.loader.exec_module(v5)

RACINE = t1.RACINE
GARDE = t1.GARDE_REELLE
JOUR = dt.date(2026, 11, 8)
CLE, JETON, CLE_VAST = t1.CLE, t1.JETON, t1.CLE_VAST
CLE_COMPTE = "vastjouet-cle-compte-v5-0005"
GO_M = "GO-2026-11-08-12"
LIGNE_22 = ("| GO-2026-11-02-22 | 2026-11-02 | calcul | Attaque de Goodhart contre le nul v9 (« A1-v4 »), Argon seul | 200 USD | "
            "2026-11-16 | Lazar | mots de Lazar |\n")
LIGNE_12 = ("| GO-2026-11-08-12 | 2026-11-08 | calcul | **Machine (hôte durable Vast.ai) pour la course A1-v4** : reprise "
            "préenregistrée de l'attaque contre le nul v9 | 35 USD | 2026-11-16 | Lazar | R-1890 |\n")
LIGNE_11 = ("| GO-2026-11-08-11 | 2026-11-08 | calcul | Course de dose-réponse des organismes (T0.6), mode exploratoire ; instance "
            "A100 ou H200 chez Vast.ai | 100 USD | 2026-11-16 | Lazar | mots |\n")
LIGNE_0503 = ("| GO-2026-11-05-03 | 2026-11-05 | calcul | Machine de l'hôte durable d'A1-v3, ce que Vast loue | 35 USD | 2026-11-18 | "
              "Lazar | mot |\n")
GPU = {"id": 21, "resource_type": "gpu", "num_gpus": 1, "gpu_name": "GTX_1070", "dph_total": 0.055, "cpu_cores_effective": 14,
       "cpu_ram": 8007, "disk_space": 50, "reliability": 0.996, "geolocation": "FR", "machine_id": 7}
VOLUME = dict(GPU, id=31, resource_type="disk", num_gpus=0, cpu_ram=0, dph_total=0.01)
CONTRAT = '{"success": true, "new_contract": 4242}'
PY_MACHINE = "/usr/bin/python3"  # Python 3.13 à numpy 2.5.3 sur l'hôte des essais (comme l'image)
MAINTENANT = dt.datetime(2026, 11, 8, 18, 0, 0, tzinfo=dt.timezone.utc)
_CONF_II = json.loads((ICI / "configuration-mondes-variante-ii-v2.json").read_text(encoding="utf-8"))  # adaptation : monde jouet aux noms de la (ii) v2
LANCEUR_GELE = _CONF_II["lanceur_gele"]
FICHIERS_PUBLICS = tuple(sorted(set(_CONF_II["fichiers_geles_publics"]) - {LANCEUR_GELE}))
PREFIXE_II = _CONF_II["prefixe_texte"]
N_GELES_II = len(_CONF_II["fichiers_geles_publics"])
LANCEUR_GELE_I = "demonstrations/attaque_goodhart_v4.py"  # variante (i), configuration v1 inchangée
PUB_II = Path('/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/commit-v5/public')  # clone public au commit préparé b8c1db3a (patchs v5 et lecteur)
def nom_texte_ii(n):
    return v5.nom_texte(n, PREFIXE_II)
VERSION_CONF = {"i": "v1", "ii": "v2"}  # adaptation : la variante (ii) lue est la v2


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def registre(tmp_path, *lignes, nom="go.md") -> Path:
    return t1.registre(tmp_path, *lignes, nom=nom)


def sceller(p: Path) -> str:
    e = sha(p.read_bytes())
    Path(str(p) + ".sha256").write_text(f"{e}  {p.name}\n")
    return e


def env_pilote(**modif) -> dict:
    e = {"GO_ID": GO_M, v5.NOM_GO_MACHINE_ENV: GO_M, v5.NOM_CLE_ARGON_PILOTE: CLE, "GH_TOKEN": JETON, "VAST_API_KEY": CLE_COMPTE,
         "PATH": os.environ["PATH"], "HOME": os.environ.get("HOME", "/root")}
    for k, v in modif.items():
        e.pop(k) if v is None else e.__setitem__(k, v)
    return e


# --- monde jouet : dépôt public (code gelé factice, texte v4-v1 scellé), configuration des mondes ------------------------------


def configuration(dossier: Path, racine_publique: Path | None, variante_fichier="ii", sceller_aussi=True, **modif) -> Path:
    """La configuration livrée de la variante, fichiers gelés remplacés par ceux du dépôt public jouet, puis `modif`."""
    variante = variante_fichier
    c = json.loads((ICI / f"configuration-mondes-variante-{variante}-{VERSION_CONF[variante]}.json").read_text(encoding="utf-8"))
    if racine_publique is not None:
        c["fichiers_geles_publics"] = {r: sha((racine_publique / "orchestrator" / r).read_bytes()) for r in FICHIERS_PUBLICS + (LANCEUR_GELE,)}
    for k, v in modif.items():
        c.pop(k) if v is None else c.__setitem__(k, v)
    dossier.mkdir(parents=True, exist_ok=True)
    p = dossier / f"configuration-mondes-variante-{variante}-{VERSION_CONF[variante]}.json"
    p.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if sceller_aussi:
        sceller(p)
    return p


def texte_jouet(racine_publique: Path, conf_chemin: Path, version=1, nom=None, marqueur=False, **plan) -> tuple[Path, str]:
    """Texte v4-v<N> jouet : blocs `plan-gele` et `empreintes-du-code` (ceux de la configuration), compagnon ; rend (chemin, sha)."""
    c = json.loads(conf_chemin.read_text(encoding="utf-8"))
    lignes = {"mode": "course", "grille": "24 cartes par monde, 24 unités par case", "mondes": c["mondes_texte"], "fournisseurs": "argon",
              "fournisseur_argon": "type=commande_externe, port=8805, modele=gemini-4-argon, fils=1, taux_usd=0.062, secondes=7.6-40",
              "essais_avant_repli": "3", "relais_perdu_h": "aucun", "plafond_usd": "200", "duree_max_h": "72",
              "decision_ecart": "décisions de Lazar", "configuration_sha256": "f" * 64, "go": "GO-2026-11-02-22", "go_machine": GO_M}
    lignes.update(plan)
    gelees = dict(c["fichiers_geles_publics"])
    gelees.update(plan.pop("gelees", {}) if "gelees" in plan else {})
    bloc_plan = "\n".join(f"{k}: {v}" for k, v in lignes.items() if v is not None)
    bloc_e = "\n".join(f"{e}  {r}" for r, e in sorted(gelees.items()))
    corps = (f"# Préenregistrement A1-v4 (jouet)\n\n{'<<CASE_CONFIGURATION>>' if marqueur else ''}\n{v5.DEBUT_PLAN}\n```\n{bloc_plan}\n```\n"
             f"{v5.FIN_PLAN}\n\n{v5.DEBUT_EMPREINTES}\n```\n{bloc_e}\n```\n{v5.FIN_EMPREINTES}\n")
    p = racine_publique / (nom or nom_texte_ii(version))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(corps, encoding="utf-8")
    return p, sceller(p)


def depot_public(tmp_path, comportement: Path, variante="ii", conf_modif=None, texte_modif=None, git_aussi=True):
    """Dépôt public jouet : commit « code gelé » (lanceur v4 factice et fichiers gelés factices), configuration des mondes dans
    `tmp_path/conf`, puis commit « texte v4-v1 » (texte et compagnon). Rend un dict de ses pièces."""
    pub = tmp_path / "public"
    (pub / "orchestrator").mkdir(parents=True)
    lanceur = pub / "orchestrator" / LANCEUR_GELE
    lanceur.parent.mkdir(parents=True, exist_ok=True)
    lanceur.write_text(t1.LANCEUR % {"comportement": str(comportement), "compteur": str(tmp_path / "courses-lancees")})
    for r in FICHIERS_PUBLICS:
        f = pub / "orchestrator" / r
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"# {r} (code gelé jouet)\n")
    gele = commit_public = None
    if git_aussi:
        t1.run("git", "init", "-q", "-b", "main", str(pub))
        t1.run("git", "add", "-A", cwd=pub)
        t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "code gelé", cwd=pub)
        gele = t1.run("git", "rev-parse", "HEAD", cwd=pub)
    conf = configuration(tmp_path / "conf", pub, variante, **({"commit_code_gele": gele} if gele else {}), **(conf_modif or {}))
    texte, sha_texte = texte_jouet(pub, conf, **(texte_modif or {}))
    if git_aussi:
        t1.run("git", "add", "-A", cwd=pub)
        t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "texte v4-v1", cwd=pub)
        commit_public = t1.run("git", "rev-parse", "HEAD", cwd=pub)
    return {"pub": pub, "gele": gele, "commit_public": commit_public, "conf": conf, "texte": texte, "sha_texte": sha_texte}


# --- constantes, GO, configuration, texte -------------------------------------------------------------------------------------


def test_constantes_de_la_v5_et_noms_neufs():
    assert (v5.GO_COURSE, v5.MONTANT_GO_COURSE_USD, v5.ETIQUETTE) == ("GO-2026-11-02-22", 200.0, "a1-v4-v9")
    assert v5.NOM_GO_MACHINE_ENV == "GO_ID_MACHINE" and v5.NOM_CLE_ARGON_PILOTE == "GEMINI_API_KEY_2"
    for b in (v5.BRANCHE_DONNEES, v5.BRANCHE_INTERROMPUE, v5.BRANCHE_REFUS, v5.BRANCHE_VIE):
        assert "a1v4" in b and b not in (h.BRANCHE_DONNEES, h.BRANCHE_INTERROMPUE, h.BRANCHE_REFUS, v4.BRANCHE_VIE)
    assert v5.MODULES[-1] == "hote_durable_a1_v4_v5.py" and v5.AMORCE.endswith("_v5.sh") and v5.TRAVAIL == "a1-v4-reprise-v9-v1"
    src = (ICI / "hote_durable_a1_v4_v5.py").read_text(encoding="utf-8")
    assert "GO-2026-11-05-03" not in src and "GO-2026-11-08-12" not in src  # aucun identifiant de machine en dur
    assert v5.MOTS_PERIMETRE_MACHINE == ("machine", "a1-v4")


def test_nom_du_texte_parametre_et_artefacts():
    assert v5.nom_texte(3) == "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v3.md"
    assert v5.version_du_texte(Path("/x/orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v12.md")) == 12
    for mauvais in ("orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md", "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon3.md",
                    "orchestrator/autre/preenregistrement-attaque-goodhart-v4-v1.md", "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v0.md"):
        with pytest.raises(h.Refus, match="nom du texte"):
            v5.version_du_texte(Path(mauvais))
    # préfixe configurable (un code d'attaque v5 pourrait exiger `…-v5-v<N>.md`) ; préfixe illisible refusé
    assert v5.version_du_texte(Path("orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v2.md"), "preenregistrement-attaque-goodhart-v5-v") == 2
    assert v5.nom_texte(1, "preenregistrement-attaque-goodhart-v5-v").endswith("-v5-v1.md")
    with pytest.raises(h.Refus, match="nom du texte"):
        v5.version_du_texte(Path("orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v1.md"), "preenregistrement-attaque-goodhart-v5-v")
    with pytest.raises(h.Refus, match="préfixe"):
        v5.version_du_texte(Path("orchestrator/prereg/x-v1.md"), "x-v")


def test_go_des_appels_exact_200_sain_et_registre_reel(tmp_path):
    g = v5.verifier_go_course(registre(tmp_path, LIGNE_22, LIGNE_12), GARDE, "GO-2026-11-02-22", JOUR)
    assert g["plafond_usd"] == 200 and g["echeance"] == "2026-11-16"
    reel = RACINE / "registres" / "go.md"
    assert v5.verifier_go_course(reel, GARDE, v5.GO_COURSE, JOUR)["lignes"] == 1


@pytest.mark.parametrize("lignes, go, motif", [
    ([LIGNE_22.replace("200 USD", "199 USD"), LIGNE_12], "GO-2026-11-02-22", "exactement 200"),
    ([LIGNE_22.replace("200 USD", "≈ 200 USD"), LIGNE_12], "GO-2026-11-02-22", "exactement 200"),
    ([LIGNE_12], "GO-2026-11-02-22", "absent"),
    ([LIGNE_22, LIGNE_12], "GO-2026-11-08-12", "exigé ici"),
    ([t1.LIGNE_06, LIGNE_12], "GO-2026-11-04-06", "exigé ici"),
])
def test_go_des_appels_artefacts(tmp_path, lignes, go, motif):
    with pytest.raises(h.Refus, match=motif):
        v5.verifier_go_course(registre(tmp_path, *lignes), GARDE, go, JOUR)


def test_go_de_la_machine_lu_sur_la_ligne_sain_et_registre_reel(tmp_path):
    g = v5.verifier_go_machine(registre(tmp_path, LIGNE_22, LIGNE_12), GARDE, GO_M, JOUR)
    assert g["plafond_usd"] == 35.0 and g["echeance"] == "2026-11-16" and g["lignes"] == 1
    reel = RACINE / "registres" / "go.md"  # la ligne réelle GO-2026-11-08-12, sans identifiant en dur dans le module
    g = v5.verifier_go_machine(reel, GARDE, GO_M, JOUR)
    assert g["plafond_usd"] == 35.0 and g["echeance"] == "2026-11-16"
    ext = LIGNE_12.replace("**Machine (hôte durable Vast.ai)", "extension : précision").replace("2026-11-16", "2026-11-15")
    assert v5.verifier_go_machine(registre(tmp_path, LIGNE_22, LIGNE_12, ext), GARDE, GO_M, JOUR)["lignes"] == 2


@pytest.mark.parametrize("lignes, go, jour, motif", [
    ([LIGNE_22], GO_M, JOUR, "GO-2026-11-08-12 absent"),
    ([LIGNE_22, LIGNE_12.replace("| calcul |", "| décision |")], GO_M, JOUR, "pas « calcul »"),
    ([LIGNE_22, LIGNE_12], GO_M, dt.date(2026, 11, 17), "hors de sa période"),
    ([LIGNE_22, LIGNE_12], GO_M, dt.date(2026, 11, 7), "hors de sa période"),
    ([LIGNE_22, LIGNE_12.replace("| Lazar |", "| directeur |")], GO_M, JOUR, "pas accordé par Lazar"),
    ([LIGNE_22, LIGNE_12.replace("35 USD", "—")], GO_M, JOUR, "plafond « — » illisible"),
    ([LIGNE_22, LIGNE_12.replace("35 USD", "≈ 35 USD")], GO_M, JOUR, "illisible"),
    ([LIGNE_22, LIGNE_12, LIGNE_12.replace("**Machine (hôte durable Vast.ai)", "extension : plafond").replace("35 USD", "40 USD")],
     GO_M, JOUR, "plafonds différents"),
    ([LIGNE_22, LIGNE_12, "| GO-2026-11-08-13 | 2026-11-08 | révocation | révoque GO-2026-11-08-12 | — | 2026-11-08 | Lazar | m |\n"],
     GO_M, JOUR, "révoqué"),
    ([LIGNE_22, LIGNE_12], "GO-2026-11-02-22", JOUR, "est la ligne des appels"),
    ([LIGNE_22, LIGNE_12], "", JOUR, "absent ou illisible"),
    ([LIGNE_22, LIGNE_12], "GO_2026_11_08_12", JOUR, "absent ou illisible"),
    ([LIGNE_22, LIGNE_12, LIGNE_11], "GO-2026-11-08-11", JOUR, "périmètre sans"),  # course de dose-réponse : pas la machine
    ([LIGNE_22, LIGNE_12, LIGNE_0503], "GO-2026-11-05-03", JOUR, "périmètre sans"),  # machine d'A1-v3 : pas A1-v4
])
def test_go_de_la_machine_artefacts(tmp_path, lignes, go, jour, motif):
    with pytest.raises(h.Refus, match=motif):
        v5.verifier_go_machine(registre(tmp_path, *lignes), GARDE, go, jour)


def test_go_de_la_machine_registre_reel_refuse_dose_reponse_et_a1_v3():
    reel = RACINE / "registres" / "go.md"
    with pytest.raises(h.Refus, match="périmètre sans"):
        v5.verifier_go_machine(reel, GARDE, "GO-2026-11-08-11", JOUR)  # 100 USD, course de dose-réponse : refusée comme machine
    with pytest.raises(h.Refus, match="périmètre sans"):
        v5.verifier_go_machine(reel, GARDE, "GO-2026-11-05-03", JOUR)  # machine d'A1-v3


def test_garde_de_depense_plafond_lu_sain_et_artefacts():
    assert abs(v5.cout_maximal_usd(0.40) - 0.40 * 293100 / 3600) < 1e-9
    assert v5.verifier_plafond(0.40, 35.0, GO_M) < 35
    with pytest.raises(h.Refus, match="plafond 32 USD lu sur la ligne GO-2026-11-08-12"):
        v5.verifier_plafond(0.40, 32.0, GO_M)
    with pytest.raises(h.Refus, match="plafond 1 USD"):
        v5.verifier_plafond(0.055, 1.0, GO_M)  # ligne à 1 USD : insuffisante
    for mauvais in (0, -1, None, True, "35"):
        with pytest.raises(h.Refus, match="plafond de la machine illisible"):
            v5.verifier_plafond(0.055, mauvais, GO_M)


def test_cles_pilote_source_argon_par_son_nom_et_machine_cle_argon_seule():
    assert v5.cles_interdites_pilote({"GEMINI_API_KEY_2": CLE, "GH_TOKEN": JETON}) == []
    assert v5.cles_interdites_pilote({"GEMINI_API_KEY_2": CLE, "GEMINI_API_KEY": "x", "KIMI_KEY": "y"}) == ["GEMINI_API_KEY", "KIMI_KEY"]
    assert v5.cles_interdites({"GEMINI_API_KEY_2": CLE}) == ["GEMINI_API_KEY_2"]  # sur la machine et dans le corps : refusée
    assert v5.cles_interdites({"CLE_ARGON": CLE}) == []
    assert v5.nom_du_jeton_github({"CONTROLE_IA_GITHUB_TOKEN_2": JETON}) == "CONTROLE_IA_GITHUB_TOKEN_2"
    assert v5.nom_du_jeton_github({"GH_TOKEN": JETON, "CONTROLE_IA_GITHUB_TOKEN_2": "x"}) == "GH_TOKEN"
    assert v5.nom_du_jeton_github({"GH_TOKEN": ""}) is None


@pytest.mark.parametrize("variante", ["i", "ii"])
def test_configuration_des_mondes_sain(tmp_path, variante):
    p = configuration(tmp_path / "c", None, variante)
    c = v5.lire_configuration_mondes(p)
    assert c["variante"] == variante and c["mondes"] == v5.VARIANTES_MONDES[variante] and c["sha256"] == sha(p.read_bytes())
    assert c["mondes_texte"] == {"i": "W1 et W2", "ii": "W2 et W2g"}[variante] and c["etiquette"] == "a1-v4-v9"


@pytest.mark.parametrize("kw, motif", [
    ({"variante": "iii"}, "variante de mondes inconnue"),
    ({"variante": "i"}, "variante i : mondes"),  # variante (i) déclarée, mondes de la (ii)
    ({"mondes": ["W2"]}, "variante ii : mondes"),
    ({"mondes_texte": ""}, "mondes_texte"),
    ({"etiquette": "a1-v3-troisieme-v1"}, "étiquette"),
    ({"go_course": "GO-2026-11-04-06"}, "go_course"),
    ({"plafond_course_usd": 400}, "go_course"),
    ({"commit_code_gele": "516feca"}, "commit_code_gele"),
    ({"prefixe_texte": "preenregistrement-attaque-goodhart-v4-brouillon"}, "prefixe_texte"),
    ({"prefixe_texte": None}, "clés attendues"),
    ({"fichiers_geles_publics": {}}, "fichiers_geles_publics"),
    ({"fichiers_geles_publics": {"pole/nul_v9.py": "abc"}}, "fichiers_geles_publics"),
    ({"fichiers_geles_publics": {"pole/nul_v9.py": "a" * 64}}, "lanceur gelé"),
    ({"lanceur_gele": None}, "clés attendues"),
    ({"inconnue": 1}, "clés attendues"),
])
def test_configuration_des_mondes_artefacts(tmp_path, kw, motif):
    p = configuration(tmp_path / "c", None, "ii", **kw)
    with pytest.raises(h.Refus, match=motif):
        v5.lire_configuration_mondes(p)


def test_configuration_compagnon_absent_faux_ou_json_illisible(tmp_path):
    p = configuration(tmp_path / "c", None, "ii", sceller_aussi=False)
    with pytest.raises(h.Refus, match="compagnon .sha256 absent"):
        v5.lire_configuration_mondes(p)
    Path(str(p) + ".sha256").write_text("0" * 64 + f"  {p.name}\n")
    with pytest.raises(h.Refus, match="différente du compagnon"):
        v5.lire_configuration_mondes(p)
    p.write_text("{pas du json", encoding="utf-8")
    sceller(p)
    with pytest.raises(h.Refus, match="JSON"):
        v5.lire_configuration_mondes(p)
    with pytest.raises(h.Refus, match="introuvable"):
        v5.lire_configuration_mondes(tmp_path / "absente.json")


def test_configurations_livrees_lisibles_et_egales_au_depot_public(tmp_path):
    """Les deux fichiers livrés, lus avec un compagnon calculé ici (le dossier n'en porte pas : la mère scelle) ; variante (ii)
    livrée ; empreintes égales aux fichiers du clone public local s'il est présent."""
    pub = Path("/home/user/ideation-organism")
    for variante in ("i", "ii"):
        src = ICI / f"configuration-mondes-variante-{variante}-{VERSION_CONF[variante]}.json"
        with pytest.raises(h.Refus, match="compagnon .sha256 absent"):
            v5.lire_configuration_mondes(src)
        copie = tmp_path / src.name
        copie.write_bytes(src.read_bytes())
        sceller(copie)
        c = v5.lire_configuration_mondes(copie)
        assert c["variante"] == variante and c["lanceur_gele"] == (LANCEUR_GELE if variante == "ii" else LANCEUR_GELE_I) and len(c["fichiers_geles_publics"]) == (N_GELES_II if variante == "ii" else 11)
        assert {"pole/attaque_goodhart_v4.py", "pole/nul_v9.py", "demonstrations/banc_tricheurs_v9.py", (LANCEUR_GELE if variante == "ii" else LANCEUR_GELE_I)} <= set(c["fichiers_geles_publics"])
        if (pub / "orchestrator" / "pole" / "nul_v9.py").is_file():
            assert v5.verifier_fichiers_geles(PUB_II if variante == "ii" else pub, c) == (N_GELES_II if variante == "ii" else 11)
    assert json.loads((ICI / "configuration-mondes-variante-ii-v2.json").read_text())["mondes_texte"] == "W2 et W2g"


def test_texte_sain(tmp_path):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    conf = v5.lire_configuration_mondes(d["conf"])
    t = v5.verifier_texte(d["texte"], d["sha_texte"], conf)
    assert (t["version"], t["mondes"], t["plafond_usd"], t["go"], t["go_machine"]) == (1, "W2 et W2g", 200.0, "GO-2026-11-02-22", GO_M)
    assert t["nom"] == nom_texte_ii(1) and t["lignes_gelees"] == N_GELES_II and t["sha256"] == d["sha_texte"]
    assert v5.verifier_texte(d["texte"], d["sha_texte"], conf, GO_M)["go_machine"] == GO_M  # ligne go_machine égale à la ligne vérifiée
    with pytest.raises(h.Refus, match="go_machine = 'GO-2026-11-08-12', la ligne vérifiée"):
        v5.verifier_texte(d["texte"], d["sha_texte"], conf, "GO-2026-11-08-11")
    assert v5.verifier_fichiers_geles(d["pub"], conf) == N_GELES_II


@pytest.mark.parametrize("texte_modif, sha_faux, motif", [
    ({"nom": "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md"}, False, "nom du texte"),
    ({"nom": "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon3.md"}, False, "nom du texte"),
    ({}, True, "différente de celle attendue"),
    ({"marqueur": True}, False, "marqueur"),
    ({"mondes": "W1 et W2"}, False, "mondes = 'W1 et W2'"),
    ({"plafond_usd": "400"}, False, "plafond_usd"),
    ({"plafond_usd": "deux cents"}, False, "plafond_usd"),
    ({"go": "GO-2026-11-04-06"}, False, "go = 'GO-2026-11-04-06'"),
    ({"mode": "essai"}, False, "mode = 'essai'"),
    ({"go_machine": "GO-2026-11-02-22"}, False, "go_machine = 'GO-2026-11-02-22' illisible ou égal"),
    ({"nom": "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v1.md"}, False, "nom du texte"),  # adaptation : nom v4 sous le préfixe v5 de la (ii) v2
    ({"fournisseurs": "argon, kimi"}, False, "fournisseurs"),
    ({"gelees": {"pole/nul_v9.py": "0" * 64}}, False, "autre empreinte"),
    ({"gelees": {"pole/nul_v9.py": None}}, False, "absents du bloc"),
])
def test_texte_artefacts(tmp_path, texte_modif, sha_faux, motif):
    g = texte_modif.pop("gelees", None)
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False, texte_modif=texte_modif)
    conf = v5.lire_configuration_mondes(d["conf"])
    texte, sha_texte = d["texte"], d["sha_texte"]
    if g is not None:  # bloc des empreintes retouché : une ligne changée ou retirée
        contenu = texte.read_text(encoding="utf-8")
        for r, e in g.items():
            ligne = [l for l in contenu.splitlines() if l.endswith(f"  {r}")][0]
            contenu = contenu.replace(ligne + "\n", "" if e is None else f"{e}  {r}\n")
        texte.write_text(contenu, encoding="utf-8")
        sha_texte = sceller(texte)
    with pytest.raises(h.Refus, match=motif):
        v5.verifier_texte(texte, "e" * 64 if sha_faux else sha_texte, conf)


def test_texte_non_scelle_ou_compagnon_faux(tmp_path):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    conf = v5.lire_configuration_mondes(d["conf"])
    comp = Path(str(d["texte"]) + ".sha256")
    comp.unlink()
    with pytest.raises(h.Refus, match="compagnon .sha256 absent"):
        v5.verifier_texte(d["texte"], d["sha_texte"], conf)
    comp.write_text("1" * 64 + "  x\n")
    with pytest.raises(h.Refus, match="différente du compagnon"):
        v5.verifier_texte(d["texte"], d["sha_texte"], conf)
    with pytest.raises(h.Refus, match="64 caractères"):
        v5.verifier_texte(d["texte"], "abc", conf)


def test_fichier_gele_modifie_sur_le_clone_public(tmp_path):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    conf = v5.lire_configuration_mondes(d["conf"])
    (d["pub"] / "orchestrator" / "pole" / "nul_v9.py").write_text("# modifié\n")
    with pytest.raises(h.Refus, match="fichier gelé modifié ou absent du clone public : pole/nul_v9.py"):
        v5.verifier_fichiers_geles(d["pub"], conf)
    (d["pub"] / "orchestrator" / "pole" / "attaque_goodhart_v4.py").unlink()
    with pytest.raises(h.Refus, match="attaque_goodhart_v4.py : gelé .*présent absent"):
        v5.verifier_fichiers_geles(d["pub"], conf)


def test_corps_v5_variables_et_artefacts(tmp_path):
    o = s10.verifier_offre_sonde([GPU], 21)
    conf = {"sha256": "f" * 64, "chemin_depot": "docs/notes/x/configuration-mondes-variante-ii-v1.json"}
    c = v5.corps("a" * 40, "b" * 40, "c" * 64, v5.nom_texte(1), "d" * 40, GO_M, conf, o, {"CLE_ARGON": CLE, "GH_TOKEN": JETON}, 1_800_000_000)
    assert set(c["env"]) == {"COMMIT_PRIVE", "COMMIT_PUBLIC", "SHA_TEXTE", "NOM_TEXTE", "COMMIT_REGISTRE", "GO_ID", "GO_MACHINE",
                             "CHEMIN_CONFIGURATION_MONDES", "SHA_CONFIGURATION_MONDES", "PRIX_H_USD", "DEPOT_URL", "ECHEANCE_UTC_S",
                             "CLE_ARGON", "GH_TOKEN"}
    assert (c["env"]["GO_ID"], c["env"]["GO_MACHINE"], c["label"]) == ("GO-2026-11-02-22", GO_M, "a1-v4-v9")
    assert c["env"]["DEPOT_URL"] == "https://github.com/lciric/controle-ia-travail.git" and "demarrage-a1v4-v5.sh" in c["script"]
    assert "GEMINI_API_KEY_2" not in c["env"] and v5.cles_interdites(c["env"]) == []
    base = dict(commit_prive="a" * 40, commit_public="b" * 40, sha_texte="c" * 64, nom_texte_relatif=v5.nom_texte(1), commit_registre="d" * 40,
                go_machine=GO_M, conf=conf, offre=o, secrets={"CLE_ARGON": CLE, "GH_TOKEN": JETON}, echeance_utc_s=1_800_000_000)
    for kw, motif in (({"go_machine": "GO-2026-11-02-22"}, "égal au GO des appels"), ({"go_machine": "35"}, "go_machine"),
                      ({"nom_texte_relatif": "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md"}, "nom du texte"),
                      ({"secrets": {"GH_TOKEN": JETON}}, "CLE_ARGON"), ({"echeance_utc_s": True}, "échéance"),
                      ({"conf": {"sha256": "f" * 64, "chemin_depot": "/abs/conf.json"}}, "relatif")):
        a = dict(base)
        a.update(kw)
        with pytest.raises(h.Refus, match=motif):
            v5.corps(**a)


def test_script_de_demarrage_et_minuterie_noms_de_la_v5():
    s = v5.script_de_demarrage("b" * 40)
    assert "a1v3" not in s and "a1-v3" not in s and v5.AMORCE in s and "amorce-a1v4-v5.log" in s and "RACINE_A1V4" in s
    assert "a1-v4-v9" in v5.MINUTERIE and "58936096 58936099 58936100" in v5.MINUTERIE and "pas a1-v4-v9 : aucun geste" in v5.MINUTERIE
    assert '[ "$D" -le 288000 ] || D=288000' in s
    with pytest.raises(h.Refus):
        v5.script_de_demarrage("main")


# --- pilote : location ------------------------------------------------------------------------------------------------------


def vastai_factice(tmp_path, reponses):
    d = tmp_path / "reponses-vastai"
    d.mkdir(exist_ok=True)
    for i, (o, e, c) in enumerate(reponses, 1):
        (d / f"{i}.out").write_text(o)
        (d / f"{i}.err").write_text(e)
        (d / f"{i}.code").write_text(str(c))
    outil = tmp_path / "vastai"
    outil.write_text(f'#!/bin/sh\nn=$(( $(cat "{d}/n" 2>/dev/null || echo 0) + 1 )); echo $n > "{d}/n"\n'
                     f'echo "$3" >> "{d}/offres"\nprintf "%s\\n" "$@" >> "{d}/arguments"\ncat "{d}/$n.out" 2>/dev/null; cat "{d}/$n.err" >&2 2>/dev/null\n'
                     f'exit $(cat "{d}/$n.code" 2>/dev/null || echo 9)\n')
    outil.chmod(0o755)
    return str(outil), d


def appels(d) -> int:
    return int((d / "n").read_text()) if (d / "n").exists() else 0


def args_louer(tmp_path, d, reg=None, offres=None, **kw):
    f = tmp_path / "offres.json"
    f.write_text(json.dumps(offres if offres is not None else [GPU, dict(GPU, id=22, dph_total=0.06), VOLUME]))
    a = dict(registre_main=str(reg or registre(tmp_path, LIGNE_22, LIGNE_12, LIGNE_11)), garde_main=str(GARDE), offres=str(f), offre="21",
             commit_prive="a" * 40, commit_public="b" * 40, texte=str(d["texte"]), sha_texte=d["sha_texte"], configuration_mondes=str(d["conf"]),
             racine_privee=str(tmp_path), commit_registre="d" * 40, journal_local=str(tmp_path / "journal-location.log"), verifier_seulement=False)
    a.update(kw)
    return type("A", (), a)()


def louer(tmp_path, reponses=((CONTRAT, "", 0),), env=None, depot=None, **kw):
    outil, dv = vastai_factice(tmp_path, list(reponses))
    environ = env_pilote() if env is None else env
    d = depot or depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    a = args_louer(tmp_path, d, **kw)
    code = v5.louer(a, v5.ClientPiloteV5(environ, outil), JOUR, environ, MAINTENANT)
    return code, a, dv


def test_louer_cas_sain_etat_ligne_et_aucun_secret(tmp_path):
    code, a, dv = louer(tmp_path)
    assert code == 0 and appels(dv) == 1
    e = json.loads(Path(a.journal_local + ".etat.json").read_text())
    ech = int(MAINTENANT.timestamp()) + 600 + 288000 + 3600
    assert e["identifiant"] == 4242 and e["etiquette"] == "a1-v4-v9" and e["borne_signe_de_vie_utc"] == "2026-11-08T18:30:00Z"
    assert e["echeance_finale_utc"] == dt.datetime.fromtimestamp(ech, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert (e["go_machine"], e["go_course"], e["plafond_machine_usd"], e["variante_mondes"]) == (GO_M, "GO-2026-11-02-22", 35.0, "ii")
    assert e["texte"] == nom_texte_ii(1) and e["mondes"] == ["W2", "W2g"]
    j = Path(a.journal_local).read_text()
    assert "LIGNE POUR registres/etat.md" in j and "garde de dépense (1/2)" in j and "garde de dépense (2/2)" in j
    assert "plafond lu 35 USD" in j and f"{N_GELES_II} fichiers gelés publics égaux" in j and "W2 et W2g" in j
    args_vastai = (dv / "arguments").read_text()
    assert "CLE_ARGON=" in args_vastai and "GEMINI_API_KEY_2" not in args_vastai and "GO_MACHINE=GO-2026-11-08-12" in args_vastai
    for s in (CLE, JETON, CLE_COMPTE):
        assert s not in j and s not in Path(a.journal_local + ".etat.json").read_text()


@pytest.mark.parametrize("modif, motif", [
    ({"env": env_pilote(GO_ID_MACHINE=None)}, "GO_ID_MACHINE absent ou illisible"),
    ({"env": env_pilote(GO_ID_MACHINE="GO-2026-11-8-12")}, "GO_ID_MACHINE absent ou illisible"),
    ({"env": env_pilote(GO_ID=None)}, "GO_ID=GO-2026-11-08-12 exigé"),
    ({"env": env_pilote(GO_ID="GO-2026-11-02-22")}, "GO_ID=GO-2026-11-08-12 exigé"),
    ({"env": env_pilote(GO_ID_MACHINE="GO-2026-11-02-22", GO_ID="GO-2026-11-02-22")}, "est la ligne des appels"),
    ({"env": env_pilote(GO_ID_MACHINE="GO-2026-11-08-11", GO_ID="GO-2026-11-08-11")}, "périmètre sans"),  # dose-réponse, 100 USD
    ({"env": env_pilote(GO_ID_MACHINE="GO-2026-11-08-09", GO_ID="GO-2026-11-08-09")}, "GO-2026-11-08-09 absent"),
    ({"reg": "machine-decision"}, "pas « calcul »"),
    ({"reg": "machine-echue"}, "hors de sa période"),
    ({"reg": "machine-1-usd"}, "plafond 1 USD lu sur la ligne"),
    ({"reg": "appels-199"}, "exactement 200"),
    ({"reg": "sans-appels"}, "GO-2026-11-02-22 absent"),
    ({"env": env_pilote(GEMINI_API_KEY_2=None)}, "clé d'Argon absente par son nom \\(GEMINI_API_KEY_2\\)"),
    ({"env": env_pilote(GEMINI_API_KEY="autre")}, "autre que GEMINI_API_KEY_2"),
    ({"env": env_pilote(GH_TOKEN=None)}, "jeton GitHub absent"),
    ({"sha_texte": "e" * 64}, "différente de celle attendue"),
    ({"offre": "31"}, "volume de stockage"),
    ({"offre": "22"}, "moins chère"),
    ({"commit_registre": "d" * 39}, "commit_registre"),
])
def test_louer_artefacts_rien_cree(tmp_path, modif, motif):
    regs = {"machine-decision": (LIGNE_22, LIGNE_12.replace("| calcul |", "| décision |")),
            "machine-echue": (LIGNE_22, LIGNE_12.replace("2026-11-16", "2026-11-07")),
            "machine-1-usd": (LIGNE_22, LIGNE_12.replace("35 USD", "1 USD")),
            "appels-199": (LIGNE_22.replace("200 USD", "199 USD"), LIGNE_12), "sans-appels": (LIGNE_12,)}
    if "reg" in modif:
        modif = dict(modif, reg=registre(tmp_path, *regs[modif["reg"]]))
    code, a, dv = louer(tmp_path, **modif)
    j = Path(a.journal_local).read_text()
    assert code == 2 and appels(dv) == 0 and "REFUS" in j and __import__("re").search(motif, j), j[-400:]
    assert not Path(a.journal_local + ".creation-incertaine").exists() and not Path(a.journal_local + ".etat.json").exists()
    assert CLE not in j and JETON not in j


@pytest.mark.parametrize("conf_modif, texte_modif, motif", [
    ({"variante": "iv"}, {}, "variante de mondes inconnue"),
    ({"sceller_aussi": False}, {}, "compagnon .sha256 absent"),
    ({}, {"mondes": "W1 et W2"}, "mondes = 'W1 et W2'"),
    ({}, {"marqueur": True}, "marqueur"),
    ({}, {"nom": "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon3.md"}, "nom du texte"),
    ({}, {"go_machine": "GO-2026-11-08-11"}, "go_machine = 'GO-2026-11-08-11', la ligne vérifiée"),
])
def test_louer_configuration_et_texte_artefacts(tmp_path, conf_modif, texte_modif, motif):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False, conf_modif=conf_modif, texte_modif=texte_modif)
    code, a, dv = louer(tmp_path, depot=d)
    j = Path(a.journal_local).read_text()
    assert code == 2 and appels(dv) == 0 and motif in j, j[-400:]


def test_louer_fichier_gele_modifie_rien_cree(tmp_path):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    (d["pub"] / "orchestrator" / LANCEUR_GELE).write_text("# lanceur modifié\n")
    code, a, dv = louer(tmp_path, depot=d)
    j = Path(a.journal_local).read_text()
    assert code == 2 and appels(dv) == 0 and f"fichier gelé modifié ou absent du clone public : {LANCEUR_GELE}" in j


def test_louer_verification_seule_rien_cree_deux_calculs(tmp_path):
    code, a, dv = louer(tmp_path, verifier_seulement=True)
    j = Path(a.journal_local).read_text()
    assert code == 0 and appels(dv) == 0 and "vérification seulement : rien créé" in j and "GO_MACHINE" in j and "NOM_TEXTE" in j
    assert "garde de dépense (1/2) : offre 21 à 0.055 USD/h, coût au plus 4.4779 USD ≤ 35" in j and "garde de dépense (2/2, sur le corps) : 4.4779" in j
    assert not Path(a.journal_local + ".identifiant").exists() and not Path(a.journal_local + ".etat.json").exists()


def test_louer_aucune_valeur_de_cle_dans_la_sortie_ni_le_journal(tmp_path, capsys):
    """La sortie standard (journal imprimé) et le journal, après un refus de Vast qui recopie les secrets : masqués."""
    echo = f"{{'success': False, 'error': 'x', 'msg': 'écho {CLE} {JETON} {CLE_COMPTE}'}}"
    code, a, dv = louer(tmp_path, reponses=(("", echo, 1),))
    sortie = capsys.readouterr().out + Path(a.journal_local).read_text()
    assert code == 2 and appels(dv) == 1
    for s in (CLE, JETON, CLE_COMPTE):
        assert s not in sortie
    assert "REFUS" in sortie


def test_seconde_location_et_creation_incertaine_refusees(tmp_path):
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    assert louer(tmp_path, depot=d)[0] == 0
    code, a, dv = louer(tmp_path, depot=d)
    assert code == 2 and "déjà eu lieu ou est incertaine" in Path(a.journal_local).read_text()
    t2 = tmp_path / "bis"
    t2.mkdir()
    code, a, dv = louer(t2, reponses=(("texte libre", "", 0),))
    assert code == 2 and Path(a.journal_local + ".creation-incertaine").exists()


def test_no_such_ask_puis_contrat_au_deuxieme_essai(tmp_path):
    nsa = "{'success': False, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type is not available.'}"
    code, a, dv = louer(tmp_path, reponses=(("", nsa, 0), (CONTRAT, "", 0)))
    assert code == 0 and appels(dv) == 2 and (dv / "offres").read_text().split() == ["21", "22"]
    assert json.loads(Path(a.journal_local + ".etat.json").read_text())["prix_h_usd"] == 0.06


# --- pilote : contrôle par identifiant --------------------------------------------------------------------------------------------


class Inventaire:
    def __init__(self, instances, reste=False):
        self._i, self.reste, self.gestes = instances, reste, []

    def instances(self):
        return list(self._i)

    def detruire(self, n):
        self.gestes.append(("detruire", n))
        if not self.reste:
            self._i = [i for i in self._i if i["id"] != n]

    def facturation(self, n):
        return dict(self._i[0], extra_env=[["CLE_ARGON", CLE]], onstart="x")


def etat_pilote(tmp_path):
    f = tmp_path / "etat.json"
    f.write_text(json.dumps({"identifiant": 4242, "etiquette": v5.ETIQUETTE, "t0_utc": "2026-11-08T18:00:00Z",
                             "borne_signe_de_vie_utc": "2026-11-08T18:30:00Z", "echeance_finale_utc": "2026-11-12T03:10:00Z",
                             "controles_utc": ["2026-11-08T18:40:00Z", "2026-11-12T03:35:00Z"]}))
    return type("A", (), {"etat": str(f), "journal_local": str(tmp_path / "controle.log")})()


def heure(j, hh, mm):
    return dt.datetime(2026, 11, j, hh, mm, tzinfo=dt.timezone.utc)


INST = {"id": 4242, "label": "a1-v4-v9", "actual_status": "running"}


@pytest.mark.parametrize("instances, vie, quand, code, gestes", [
    ([], False, heure(8, 18, 41), 0, []),
    ([INST], False, heure(8, 18, 20), 5, []),
    ([INST], True, heure(8, 18, 41), 5, []),
    ([INST], False, heure(8, 18, 41), 1, [("detruire", 4242)]),
    ([dict(INST, label="a1-v3-troisieme-v1")], False, heure(8, 18, 41), 2, []),
    ([INST], False, heure(12, 3, 35), 7, []),
])
def test_controler_par_identifiant(tmp_path, instances, vie, quand, code, gestes):
    c = Inventaire(instances)
    assert v5.controler(etat_pilote(tmp_path), c, lambda: vie, quand, env_pilote()) == code
    assert c.gestes == gestes
    j = Path(tmp_path / "controle.log").read_text()
    assert CLE not in j and JETON not in j


def test_controler_protegee_destruction_non_suivie_et_facturation(tmp_path):
    c = Inventaire([INST], reste=True)
    assert v5.controler(etat_pilote(tmp_path), c, lambda: False, heure(8, 18, 41), env_pilote()) == 3
    a = etat_pilote(tmp_path)
    Path(a.etat).write_text(json.dumps(dict(json.loads(Path(a.etat).read_text()), identifiant=58936099)))
    c = Inventaire([dict(INST, id=58936099)])
    assert v5.controler(a, c, lambda: False, heure(8, 18, 41), env_pilote()) == 2 and c.gestes == []
    a = etat_pilote(tmp_path)
    assert v5.relever_facturation(a, Inventaire([dict(INST, dph_total=0.055)]), env_pilote()) == 0
    j = Path(a.journal_local).read_text()
    assert '"dph_total": 0.055' in j and CLE not in j and "extra_env" not in j
    assert v5.relever_facturation(a, Inventaire([dict(INST, label="autre")]), env_pilote()) == 2


# --- module en fichier seul (import de repli), sous-commandes sans création ------------------------------------------------------


def module_seul(*args, env=None):
    return subprocess.run([sys.executable, "-I", "-B", str(ICI / "hote_durable_a1_v4_v5.py"), *args], capture_output=True, text=True,
                          env=env or {"PATH": os.environ["PATH"]}, timeout=120)


def test_fichier_seul_offre_inventaire_et_verifier_texte(tmp_path):
    r = module_seul("inventaire")
    assert r.returncode == 2 and "REFUS : VAST_API_KEY absente" in r.stderr and "Traceback" not in r.stderr
    f = tmp_path / "offres.json"
    f.write_text(json.dumps([VOLUME, dict(GPU, id=22, dph_total=0.06), GPU]))
    r = module_seul("offre", "--offres", str(f))
    assert r.returncode == 0 and r.stdout.strip() == "21"
    d = depot_public(tmp_path, tmp_path / "comp.json", git_aussi=False)
    r = module_seul("verifier-texte", "--texte", str(d["texte"]), "--sha-texte", d["sha_texte"], "--configuration-mondes", str(d["conf"]))
    assert r.returncode == 0 and json.loads(r.stdout)["fichiers_geles_publics_egaux"] == N_GELES_II and not (tmp_path / "journal-location.log").exists()
    r = module_seul("verifier-texte", "--texte", str(d["texte"]), "--sha-texte", "e" * 64, "--configuration-mondes", str(d["conf"]))
    assert r.returncode == 2 and "REFUS" in r.stderr


# --- amorce ------------------------------------------------------------------------------------------------------------------------


def faux_python(tmp_path, nom, version, numpy="2.5.3"):
    d = tmp_path / f"faux-python-{nom}"
    d.mkdir(exist_ok=True)
    p = d / "python3"
    if not p.exists():
        p.write_text(f'#!/bin/sh\ncase "$1" in --version) echo "Python {version}.0 (jouet {nom})";; '
                     f'-c) case "$2" in *numpy*) echo "{numpy}";; *) echo "{version}";; esac;; '
                     f'*) exec {sys.executable} "$@";; esac\n')
        p.chmod(0o755)
    return p


def amorce(tmp_path, retirer=(), meminfo_kb=16_000_000, modules=None, **modif):
    racine = tmp_path / "racine-amorce"
    d = racine / "amorce-depot" / "src" / "controle_ia"
    d.mkdir(parents=True, exist_ok=True)
    for m in (v5.MODULES if modules is None else modules):
        (d / m).write_text(f'import pathlib\npathlib.Path({str(racine / "exec-atteint.txt")!r}).write_text("oui")\n')
    mem = tmp_path / "meminfo"
    mem.write_text(f"MemTotal:       {meminfo_kb} kB\n" if meminfo_kb is not None else "illisible\n")
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "COMMIT_PUBLIC": "b" * 40, "SHA_TEXTE": "c" * 64, "NOM_TEXTE": nom_texte_ii(1),
           "COMMIT_REGISTRE": "d" * 40, "GO_ID": "GO-2026-11-02-22", "GO_MACHINE": GO_M, "CHEMIN_CONFIGURATION_MONDES": "docs/x/conf.json",
           "SHA_CONFIGURATION_MONDES": "f" * 64, "PRIX_H_USD": "0.055", "ECHEANCE_UTC_S": "1800000000", "CLE_ARGON": CLE, "GH_TOKEN": JETON,
           "RACINE_AMORCE": str(racine), "SAUTER_INSTALLATION": "1", "A1V4_MEMINFO": str(mem),
           "A1V4_PYTHON_IMAGE": str(faux_python(tmp_path, "image", "3.13")), "A1V4_PYTHON_CONFIGURATION": str(faux_python(tmp_path, "configuration", "3.11"))}
    for k in retirer:
        env.pop(k)
    env.update(modif)
    r = subprocess.run(["bash", str(ICI / "amorce_hote_durable_a1_v4_v5.sh")], env=env, capture_output=True, text=True, timeout=60)
    return r, racine


def test_amorce_cas_sain_jusqu_a_exec(tmp_path):
    r, racine = amorce(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (racine / "exec-atteint.txt").exists() and "16000000 kB" in (racine / "a1v4-memoire.txt").read_text()
    assert "GO des appels GO-2026-11-02-22 ; GO de la machine GO-2026-11-08-12" in r.stdout
    assert CLE not in r.stdout + r.stderr and JETON not in r.stdout + r.stderr


@pytest.mark.parametrize("kw, motif", [
    ({"retirer": ("CLE_ARGON",)}, "variable CLE_ARGON absente"),
    ({"retirer": ("NOM_TEXTE",)}, "variable NOM_TEXTE absente"),
    ({"retirer": ("SHA_CONFIGURATION_MONDES",)}, "variable SHA_CONFIGURATION_MONDES absente"),
    ({"GO_ID": "GO-2026-11-04-06"}, "au lieu de GO-2026-11-02-22"),
    ({"GO_MACHINE": "GO-2026-11-02-22"}, "égal à la ligne des appels"),
    ({"GO_MACHINE": "35"}, "illisible"),
    ({"NOM_TEXTE": "orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon3.md"}, "hors de orchestrator/prereg"),
    ({"NOM_TEXTE": "orchestrator/autre/preenregistrement-attaque-goodhart-v4-v1.md"}, "hors de orchestrator/prereg"),
    ({"GEMINI_API_KEY_2": "autre-cle"}, "GEMINI_API_KEY_2 présente"),  # sur la machine, même la source du pilote est refusée
    ({"KIMI_API_KEY": "autre-cle"}, "KIMI_API_KEY présente"),
    ({"ECHEANCE_UTC_S": "demain"}, "ECHEANCE_UTC_S non entière"),
    ({"meminfo_kb": 1_000_000}, "< 2 Go"),
    ({"modules": v5.MODULES[:-1]}, "hote_durable_a1_v4_v5.py absent"),
])
def test_amorce_artefacts(tmp_path, kw, motif):
    r, racine = amorce(tmp_path, **kw)
    assert r.returncode == 2 and motif in r.stdout and not (racine / "exec-atteint.txt").exists(), r.stdout
    assert CLE not in r.stdout + r.stderr and "autre-cle" not in r.stdout


# --- machine -----------------------------------------------------------------------------------------------------------------------

CHEMIN_CONF_DEPOT = "docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json"


@pytest.fixture
def monde(tmp_path):
    def fabriquer(comportement=None, registre_main=None, etiquette="a1-v4-v9", echeance_dans_s=4800, conf_modif=None, texte_modif=None,
                  casser_public=None):
        comp = tmp_path / "comportement.json"
        comp.write_text(json.dumps(comportement or {"code": 0}))
        d = depot_public(tmp_path, comp, conf_modif=conf_modif, texte_modif=texte_modif)
        if casser_public:
            casser_public(d["pub"])
            t1.run("git", "add", "-A", cwd=d["pub"])
            t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "cassé", cwd=d["pub"])
            d["commit_public"] = t1.run("git", "rev-parse", "HEAD", cwd=d["pub"])
        nuit = h.NUIT
        relais = (t1.RELAIS % {"drapeau": str(tmp_path / "relais-mort-une-fois"), "comportement": str(comp)}).encode()
        piece = b"consigne factice\n"
        conf_argon = json.dumps({"pieces": {"consigne": {"chemin": "pieces/a.md", "sha256": sha(piece)}}}).encode()
        sources = {f"{nuit}/commande_argon_v56_nuit_v2.py": relais, f"{nuit}/registre_depense_cumulee_v1.py": b"# r\n",
                   f"{nuit}/pieces/a.md": piece, "donnees/espece-seule-v1/collisionneur_v7.py": b"# c\n"}
        reg_main = registre_main or ("# Registre\n\n" + t1.ENTETE + LIGNE_22 + LIGNE_12 + LIGNE_11).encode()
        conf_octets = d["conf"].read_bytes()
        nu = t1.depot_nu_avec_branches(tmp_path, {
            "main": {"registres/go.md": reg_main, ".claude/hooks/garde_calcul.py": GARDE.read_bytes(), "LISEZMOI.md": b"racine de main\n",
                     CHEMIN_CONF_DEPOT: conf_octets, CHEMIN_CONF_DEPOT + ".sha256": Path(str(d["conf"]) + ".sha256").read_bytes()},
            h.SOURCE_REGISTRE: {"registres/go.md": ("# R\n\n" + t1.ENTETE + LIGNE_22).encode()},
            h.REF_SOURCES: sources,
            h.REF_CONFIGURATION: {h.CHEMIN_CONF_DANS_REF: conf_argon},
        })
        t1.run("git", "-C", str(nu), "config", "uploadpack.allowFilter", "true")
        t1.run("git", "-C", str(nu), "config", "uploadpack.allowReachableSHA1InWant", "true")
        clone = tmp_path / "amorce-depot"
        t1.run("git", "init", "-q", str(clone))
        t1.run("git", "-C", str(clone), "remote", "add", "origin", f"file://{nu}")
        t1.run("git", "-C", str(clone), "sparse-checkout", "set", "scripts", "src/controle_ia")
        t1.run("git", "-C", str(clone), "fetch", "-q", "--filter=blob:none", "--depth", "1", "origin", "main")
        t1.run("git", "-C", str(clone), "checkout", "-q", "--detach", "FETCH_HEAD")
        commit_prive = t1.run("git", "-C", str(nu), "rev-parse", "refs/heads/main")
        commit_registre = t1.run("git", "-C", str(nu), "rev-parse", f"refs/heads/{h.SOURCE_REGISTRE}")
        empreintes = {f"{nuit}/configuration-mini-course-kimi-argon-v3.json": sha(conf_argon), f"{nuit}/commande_argon_v56_nuit_v2.py": sha(relais),
                      f"{nuit}/registre_depense_cumulee_v1.py": sha(b"# r\n"), "donnees/espece-seule-v1/collisionneur_v7.py": sha(b"# c\n")}
        (tmp_path / "a1v4-minuterie.txt").write_text(f"{time.time() - 30:.1f} 1800000000\n")
        for nom in ("a1v4-temps.txt", "amorce-a1v4-v5.log", "a1v4-memoire.txt"):
            (tmp_path / nom).write_text(f"{nom} : journal du démarrage (jouet)\n")
        r = h.Reglages(travail=tmp_path / v5.TRAVAIL, clone_prive=clone, clone_public=tmp_path / "pub-clone", depot_public=str(d["pub"]),
                       racine_sources=tmp_path / "sources", empreintes=empreintes, commit_code_gele="0" * 40, python_relais=PY_MACHINE,
                       python_course=PY_MACHINE, port=t1.port_libre(), periode_s=0.1, duree_max_s=600, attente_relais_s=10, essais_poussee=2,
                       attente_poussee_s=0, jouet=True, vast_jouet=tmp_path / "vast.json", aujourd_hui=JOUR)
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "etat": "running", "label": etiquette}], "gestes": []})
        env = {"COMMIT_PRIVE": commit_prive, "COMMIT_PUBLIC": d["commit_public"], "SHA_TEXTE": d["sha_texte"], "NOM_TEXTE": nom_texte_ii(1),
               "COMMIT_REGISTRE": commit_registre, "GO_ID": "GO-2026-11-02-22", "GO_MACHINE": GO_M, "CHEMIN_CONFIGURATION_MONDES": CHEMIN_CONF_DEPOT,
               "SHA_CONFIGURATION_MONDES": sha(conf_octets), "PRIX_H_USD": "0.2", "ECHEANCE_UTC_S": str(int(time.time()) + echeance_dans_s),
               "CLE_ARGON": CLE, "GH_TOKEN": JETON, "CONTAINER_ID": "90000001", "CONTAINER_API_KEY": CLE_VAST}
        return r, env, nu, d
    return fabriquer


def gestes(r):
    return json.loads(r.vast_jouet.read_text())["gestes"]


def journal(f, b):
    return f[f"{b}/{v5.JOURNAL_HOTE}"]


def test_machine_cas_sain_lanceur_v4_texte_v4_v1_signe_de_vie_et_destruction(monde, tmp_path):
    r, env, nu, d = monde()
    assert v5.MachineV5(r, env).principal() == 0
    b = v5.BRANCHE_DONNEES
    f = t1.branche(nu, b)
    j = journal(f, b)
    for attendu in ("hote-durable-a1-v4-v5 ; machine GO-2026-11-08-12 ; appels GO-2026-11-02-22", '"plafond_usd": 35.0', '"plafond_usd": 200.0',
                    "garde de dépense (machine) : coût au plus", "variante (ii) ['W2', 'W2g']", "aucun doublon",
                    f"signe de vie poussé : {v5.BRANCHE_VIE}", "pièces gelées : 4 empreintes égales", f"{N_GELES_II} fichiers gelés publics égaux",
                    f"texte {nom_texte_ii(1)} {d['sha_texte']} = compagnon = SHA_TEXTE ; mondes « W2 et W2g »",
                    "--verifier-seulement : code 0", "course lancée : PID", "fin du lanceur : code 0", "inchangé", "nature de la fin : fin_du_lanceur"):
        assert attendu in j, attendu
    assert f[f"{b}/code-sortie-lanceur.txt"].strip() == "0" and f"{b}/demarrage/amorce-a1v4-v5.log" in f
    assert f"{b}/sortie-attaque-goodhart-v5/manifeste.json" in f and f"{b}/configuration-mondes/configuration-mondes-variante-ii-v2.json" in f
    assert f"{b}/garde-a1-v4.jsonl" in f and f"{b}/course-stdout-a1-v4.log" in f and f"{b}/relais-argon-journal-a1-v4.jsonl" in f
    for ligne in f[f"{b}/{v5.LISTE_EMPREINTES}"].splitlines():
        e, nom = ligne.split("  ", 1)
        assert sha(f[f"{b}/{nom}"].encode()) == e
    parent = t1.run("git", "-C", str(nu), "rev-parse", f"refs/heads/{b}^")
    assert parent == t1.run("git", "-C", str(nu), "rev-parse", "refs/heads/main")
    assert t1.branche(nu, v5.BRANCHE_VIE) and not t1.branche(nu, h.BRANCHE_DONNEES)
    t1.jamais_de_secret(f)
    t1.jamais_de_secret(t1.branche(nu, v5.BRANCHE_VIE))
    assert gestes(r) == [["detruire", 90000001]] and (r.travail / "ETAT").read_text().strip() == "verse"


def test_machine_cmd_course_lanceur_v4_texte_et_go(monde):
    r, env, nu, d = monde()
    m = v5.MachineV5(r, env)
    m.conf = v5.lire_configuration_mondes(d["conf"])
    cmd = m.cmd_course(True)
    assert cmd[3:7] == [PY_MACHINE, "-I", "-B", "demonstrations/attaque_goodhart_v5.py"] and cmd[-1] == "--verifier-seulement"
    assert cmd[cmd.index("--preenregistrement") + 1] == "prereg/preenregistrement-attaque-goodhart-v5-v1.md"
    assert cmd[cmd.index("--go") + 1] == "GO-2026-11-02-22" and cmd[7].endswith("a1-v4-reprise-v9-v1/sortie-attaque-goodhart-v5")
    assert "--verifier-seulement" not in m.cmd_course(False)


def casser_nul_v9(pub):
    (pub / "orchestrator" / "pole" / "nul_v9.py").write_text("# nul v9 modifié après le scellement\n")


@pytest.mark.parametrize("option, env_modif, motif", [
    ({"casser_public": casser_nul_v9}, {}, "fichier gelé modifié ou absent du clone public : pole/nul_v9.py"),
    ({"registre_main": ("# R\n\n" + t1.ENTETE + LIGNE_22 + LIGNE_12.replace("| calcul |", "| décision |")).encode()}, {}, "pas « calcul »"),
    ({"registre_main": ("# R\n\n" + t1.ENTETE + LIGNE_22 + LIGNE_12.replace("35 USD", "1 USD")).encode()}, {}, "plafond 1 USD lu sur la ligne"),
    ({"registre_main": ("# R\n\n" + t1.ENTETE + LIGNE_22.replace("200 USD", "199 USD") + LIGNE_12).encode()}, {}, "exactement 200"),
    ({"registre_main": ("# R\n\n" + t1.ENTETE + LIGNE_22 + LIGNE_12 + LIGNE_11).encode()}, {"GO_MACHINE": "GO-2026-11-08-11"}, "périmètre sans"),
    ({}, {"GO_MACHINE": "GO-2026-11-02-22"}, "égal à la ligne des appels"),
    ({}, {"GO_ID": "GO-2026-11-04-06"}, "la ligne des appels est GO-2026-11-02-22"),
    ({}, {"SHA_CONFIGURATION_MONDES": "0" * 64}, "le pilote a vérifié"),
    ({}, {"SHA_TEXTE": "e" * 64}, "différente de celle attendue"),
    ({}, {"NOM_TEXTE": "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md"}, "nom du texte"),
    ({}, {"NOM_TEXTE": "orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v2.md"}, "texte introuvable"),
    ({}, {"CHEMIN_CONFIGURATION_MONDES": None}, "variable CHEMIN_CONFIGURATION_MONDES absente"),
    ({}, {"GEMINI_API_KEY_2": "autre"}, "autre que CLE_ARGON"),
    ({"echeance_dans_s": 3600 + 30}, {}, "échéance absolue trop proche"),
    ({"conf_modif": {"variante": "v"}}, {}, "variante de mondes inconnue"),
    ({"texte_modif": {"mondes": "W1 et W2"}}, {}, "mondes = 'W1 et W2'"),
    ({"texte_modif": {"go_machine": "GO-2026-11-05-03"}}, {}, "go_machine = 'GO-2026-11-05-03', la ligne vérifiée"),
])
def test_machine_refus_rien_ne_part(monde, tmp_path, option, env_modif, motif):
    r, env, nu, d = monde(**option)
    for k, v in env_modif.items():
        env.pop(k) if v is None else env.__setitem__(k, v)
    assert v5.MachineV5(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    f = t1.branche(nu, v5.BRANCHE_REFUS)
    j = journal(f, v5.BRANCHE_REFUS)
    assert "REFUS" in j and motif in j, j[-600:]
    t1.jamais_de_secret(f)
    assert gestes(r) == [["detruire", 90000001]]


def test_machine_etiquette_autre_aucun_geste(monde):
    r, env, nu, d = monde(etiquette="a1-v3-troisieme-v1")
    assert v5.MachineV5(r, env).principal() == 4 and gestes(r) == []


def test_machine_reprise_du_conteneur_ne_relance_rien(monde):
    r, env, nu, d = monde()
    r.travail.mkdir(parents=True)
    (r.travail / "ETAT").write_text("course\n")
    assert v5.MachineV5(r, env).principal() == 0
    f = t1.branche(nu, v5.BRANCHE_INTERROMPUE)
    assert "REPRISE du conteneur" in journal(f, v5.BRANCHE_INTERROMPUE) and gestes(r) == [["detruire", 90000001]]
