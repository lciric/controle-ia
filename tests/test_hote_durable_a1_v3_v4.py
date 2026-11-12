"""Essais en mode jouet de l'hôte durable v4 d'A1-v3 (aucune location, aucun appel de modèle, aucun réseau).

Chaque garde neuve est éprouvée sur un cas sain et sur un artefact (R5). Monde jouet : celui des essais v1 (relais et lanceur
factices, dépôt public à deux commits), avec un dépôt privé nu qui admet les clones partiels (`file://`, comme GitHub), un clone
privé partiel comme celui du script de démarrage, Vast simulé par un fichier, et un `vastai` ou un `curl` factices. Toutes les
dates sont passées explicitement (JOUR = 2026-11-05).
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

import test_hote_durable_a1_v3 as t1  # monde jouet de la v1 (importé comme module : ses essais ne sont pas recollectés ici)
from controle_ia import hote_durable_a1_v3 as h
from controle_ia import hote_durable_a1_v3_v2 as v2  # artefacts de départ (la v2 inchangée)
from controle_ia import hote_durable_a1_v3_v3 as v3  # artefacts de départ (la v3 inchangée)
from controle_ia import hote_durable_a1_v3_v4 as v4
from controle_ia import sonde_hote_durable_a1_v3_v10 as s10

RACINE = t1.RACINE
GARDE = t1.GARDE_REELLE
JOUR = dt.date(2026, 11, 5)
CLE, JETON, CLE_VAST = t1.CLE, t1.JETON, t1.CLE_VAST
CLE_COMPTE = "vastjouet-cle-compte-v2-0002"
LIGNE_06 = t1.LIGNE_06
LIGNE_0503 = ("| GO-2026-11-05-03 | 2026-11-05 | calcul | machine de l'hôte durable d'A1-v3, une carte | 35 USD | 2026-11-18 | "
              "Lazar | mot de Lazar |\n")
GPU = {"id": 21, "resource_type": "gpu", "num_gpus": 1, "gpu_name": "GTX_1070", "dph_total": 0.055, "cpu_cores_effective": 14,
       "cpu_ram": 8007, "disk_space": 50, "reliability": 0.996, "geolocation": "FR", "machine_id": 7}
VOLUME = dict(GPU, id=31, resource_type="disk", num_gpus=0, cpu_ram=0, dph_total=0.01)
ENV_PILOTE = {"GO_ID": "GO-2026-11-05-03", "CLE_ARGON": CLE, "GH_TOKEN": JETON, "VAST_API_KEY": CLE_COMPTE,
              "PATH": os.environ["PATH"], "HOME": os.environ.get("HOME", "/root")}
CONTRAT = '{"success": true, "new_contract": 4242}'
PY_MACHINE = "/usr/bin/python3"  # v4 : Python 3.13 à numpy 2.5.3, comme l'image (le .venv des essais a numpy 2.4.6)
NSA = "{'success': False, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type is not available.'}"


def registre(tmp_path, *lignes, nom="go.md") -> Path:
    return t1.registre(tmp_path, *lignes, nom=nom)


# --- constantes, GO, clés, offre ---------------------------------------------------------------------------------------------


def test_borne_de_la_machine_et_versement_borne():
    assert v4.DUREE_MACHINE_S == 80 * 3600 and v4.MONTANT_GO_MACHINE_USD == 35 and v4.MONTANT_GO_COURSE_USD == 400
    assert abs(v4.cout_maximal_usd(0.40) - 0.40 * 293100 / 3600) < 1e-9 and v4.verifier_plafond(0.40) < 35  # 32,57 USD
    with pytest.raises(h.Refus, match="plafond 32 USD"):
        v4.verifier_plafond(0.40, 32)  # artefact : les 32 USD de la garde de l'hôte ne bornent pas la minuterie
    pire = 3 * v4.DELAI_GIT_S + v4.ESSAIS_POUSSEE * (2 * v4.DELAI_GIT_S + v4.ATTENTE_POUSSEE_S)
    assert pire < v4.RESERVE_VERSEMENT_S <= v4.MARGE_MINUTERIE_S


def test_go_de_la_machine_cas_sains_dont_le_registre_reel_de_main(tmp_path):
    g = v4.verifier_go_exact(registre(tmp_path, LIGNE_06, LIGNE_0503), GARDE, "GO-2026-11-05-03", v4.GO_MACHINE, 35, JOUR)
    assert g["plafond_usd"] == 35 and g["echeance"] == "2026-11-18"
    reel = RACINE / "registres" / "go.md"
    assert v4.verifier_go_exact(reel, GARDE, v4.GO_MACHINE, v4.GO_MACHINE, 35, JOUR)["lignes"] == 1
    assert h.verifier_go(reel, GARDE, v4.GO_COURSE, 400, JOUR)["echeance"] == "2026-11-18"


@pytest.mark.parametrize("lignes, go, jour, motif", [
    ([LIGNE_0503], "GO-2026-11-04-09", JOUR, "exigé ici"),
    ([], "GO-2026-11-05-03", JOUR, "absent"),
    ([LIGNE_0503.replace("35 USD", "34 USD")], "GO-2026-11-05-03", JOUR, "exactement 35"),
    ([LIGNE_0503.replace("35 USD", "≈ 35 USD")], "GO-2026-11-05-03", JOUR, "exactement 35"),
    ([LIGNE_0503], "GO-2026-11-05-03", dt.date(2026, 11, 19), "hors de sa période"),
    ([LIGNE_0503], "GO-2026-11-05-03", dt.date(2026, 11, 4), "hors de sa période"),
    ([LIGNE_0503.replace("| Lazar |", "| directeur |")], "GO-2026-11-05-03", JOUR, "pas accordé par Lazar"),
    ([LIGNE_0503, "| GO-2026-11-05-09 | 2026-11-05 | révocation | révoque GO-2026-11-05-03 | — | 2026-11-05 | Lazar | m |\n"],
     "GO-2026-11-05-03", JOUR, "révoqué"),
])
def test_go_de_la_machine_artefacts(tmp_path, lignes, go, jour, motif):
    with pytest.raises(h.Refus, match=motif):
        v4.verifier_go_exact(registre(tmp_path, *lignes), GARDE, go, v4.GO_MACHINE, 35, jour)


def test_cles_de_modele_seule_cle_argon_permise_et_liste_commune_a_l_amorce():
    assert v4.cles_interdites({"CLE_ARGON": CLE, "GH_TOKEN": JETON}) == []
    assert v4.cles_interdites({"GEMINI_API_KEY": "x", "RR_PROD_API_KEY_1": "y", "OPENAI_API_KEY": ""}) == [
        "GEMINI_API_KEY", "RR_PROD_API_KEY_1"]
    assert v4.MOTIF_AMORCE in (RACINE / v4.AMORCE).read_text()


def test_offre_a_une_carte_et_artefact_de_depart():
    assert s10.verifier_offre_sonde([GPU, VOLUME], 21)["num_gpus"] == 1
    with pytest.raises(h.Refus, match="volume de stockage"):
        s10.verifier_offre_sonde([GPU, VOLUME], 31)
    with pytest.raises(h.Refus, match="sans carte"):  # artefact de départ : la v1 refuse toute machine que Vast loue
        h.verifier_offre([GPU], 21)
    with pytest.raises(h.Refus, match="resource_type"):  # et la v2 refuse l'offre « sans carte » de la v1
        s10.verifier_offre_sonde([t1.OFFRE], 123)


def test_corps_porte_les_deux_go_et_l_echeance(tmp_path):
    o = s10.verifier_offre_sonde([GPU], 21)
    c = v4.corps("a" * 40, "b" * 40, "c" * 64, "d" * 40, o, {"CLE_ARGON": CLE, "GH_TOKEN": JETON}, 1_800_000_000)
    assert set(c["env"]) == {"COMMIT_PRIVE", "COMMIT_PUBLIC", "SHA_TEXTE", "COMMIT_REGISTRE", "GO_ID", "GO_MACHINE",
                             "PRIX_H_USD", "DEPOT_URL", "ECHEANCE_UTC_S", "CLE_ARGON", "GH_TOKEN"}
    assert (c["env"]["GO_ID"], c["env"]["GO_MACHINE"], c["label"]) == ("GO-2026-11-04-06", "GO-2026-11-05-03", v4.ETIQUETTE)
    assert c["env"]["DEPOT_URL"] == "https://github.com/lciric/controle-ia-travail.git"
    for kw, motif in (({"commit_public": "abc"}, "commit_public"), ({"secrets": {"GH_TOKEN": JETON}}, "CLE_ARGON"),
                      ({"echeance_utc_s": True}, "échéance")):
        a = dict(commit_prive="a" * 40, commit_public="b" * 40, sha_texte="c" * 64, commit_registre="d" * 40, offre=o,
                 secrets={"CLE_ARGON": CLE, "GH_TOKEN": JETON}, echeance_utc_s=1_800_000_000)
        a.update(kw)
        with pytest.raises(h.Refus, match=motif):
            v4.corps(**a)


# --- pilote : location ------------------------------------------------------------------------------------------------------


def vastai_factice(tmp_path, reponses):
    """`vastai` factice : n-ième appel → n-ième réponse (sortie standard, sortie d'erreur, code) ; compte ses appels."""
    d = tmp_path / "reponses-vastai"
    d.mkdir(exist_ok=True)
    for i, (o, e, c) in enumerate(reponses, 1):
        (d / f"{i}.out").write_text(o)
        (d / f"{i}.err").write_text(e)
        (d / f"{i}.code").write_text(str(c))
    outil = tmp_path / "vastai"
    outil.write_text(f'#!/bin/sh\nn=$(( $(cat "{d}/n" 2>/dev/null || echo 0) + 1 )); echo $n > "{d}/n"\n'
                     f'echo "$3" >> "{d}/offres"\ncat "{d}/$n.out" 2>/dev/null; cat "{d}/$n.err" >&2 2>/dev/null\n'
                     f'exit $(cat "{d}/$n.code" 2>/dev/null || echo 9)\n')
    outil.chmod(0o755)
    return str(outil), d


def appels(d) -> int:
    return int((d / "n").read_text()) if (d / "n").exists() else 0


def args_louer(tmp_path, reg=None, offres=None, **kw):
    f = tmp_path / "offres.json"
    f.write_text(json.dumps(offres if offres is not None else [GPU, dict(GPU, id=22, dph_total=0.06), VOLUME]))
    a = dict(go="GO-2026-11-04-06", go_machine="GO-2026-11-05-03",
             registre_main=str(reg or registre(tmp_path, LIGNE_06, LIGNE_0503)), garde_main=str(GARDE), offres=str(f),
             offre="21", commit_prive="a" * 40, commit_public="b" * 40, sha_texte="c" * 64, commit_registre="d" * 40,
             journal_local=str(tmp_path / "journal-location.log"), verifier_seulement=False)
    a.update(kw)
    return type("A", (), a)()


MAINTENANT = dt.datetime(2026, 11, 5, 9, 0, 0, tzinfo=dt.timezone.utc)


def louer(tmp_path, reponses=((CONTRAT, "", 0),), env=None, **kw):
    outil, d = vastai_factice(tmp_path, list(reponses))
    environ = dict(ENV_PILOTE) if env is None else env
    a = args_louer(tmp_path, **kw)
    code = v4.louer(a, v4.ClientPiloteV4(environ, outil), JOUR, environ, MAINTENANT)
    return code, a, d


def test_louer_cas_sain_etat_ligne_et_aucun_secret(tmp_path):
    code, a, d = louer(tmp_path)
    assert code == 0 and appels(d) == 1
    e = json.loads(Path(a.journal_local + ".etat.json").read_text())
    ech = int(MAINTENANT.timestamp()) + 600 + 288000 + 3600
    assert e["identifiant"] == 4242 and e["echeance_finale_utc"] == dt.datetime.fromtimestamp(ech, dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ") and e["borne_signe_de_vie_utc"] == "2026-11-05T09:30:00Z"
    assert e["controles_utc"][0] == "2026-11-05T09:40:00Z" and (e["go_machine"], e["go_course"]) == (v4.GO_MACHINE, v4.GO_COURSE)
    j = Path(a.journal_local).read_text()
    assert "LIGNE POUR registres/etat.md" in j and "controler" in j and "vastai destroy" not in j
    for s in (CLE, JETON, CLE_COMPTE):
        assert s not in j and s not in Path(a.journal_local + ".etat.json").read_text()


@pytest.mark.parametrize("modif, motif", [
    ({"env": {k: v for k, v in ENV_PILOTE.items() if k != "GO_ID"}}, "GO_ID=GO-2026-11-05-03 exigé"),
    ({"env": dict(ENV_PILOTE, GO_ID="GO-2026-11-04-09")}, "GO_ID=GO-2026-11-05-03 exigé"),
    ({"env": dict(ENV_PILOTE, GEMINI_API_KEY="autre")}, "autre que CLE_ARGON"),
    ({"env": {k: v for k, v in ENV_PILOTE.items() if k != "CLE_ARGON"}}, "secrets absents"),
    ({"reg": "sans-0503"}, "GO-2026-11-05-03 absent"),
    ({"reg": "0503-a-34"}, "exactement 35"),
    ({"reg": "sans-06"}, "GO-2026-11-04-06 absent"),
    ({"go_machine": "GO-2026-11-04-09"}, "exigé ici"),
    ({"offre": "31"}, "volume de stockage"),
    ({"offre": "22"}, "moins chère"),
    ({"commit_registre": "d" * 39}, "commit_registre"),
])
def test_louer_artefacts_rien_cree(tmp_path, modif, motif):
    regs = {"sans-0503": (LIGNE_06,), "0503-a-34": (LIGNE_06, LIGNE_0503.replace("35 USD", "34 USD")),
            "sans-06": (LIGNE_0503,)}
    if "reg" in modif:
        modif = dict(modif, reg=registre(tmp_path, *regs[modif["reg"]]))
    code, a, d = louer(tmp_path, **modif)
    j = Path(a.journal_local).read_text()
    assert code == 2 and appels(d) == 0 and "REFUS" in j and motif in j, j[-400:]
    assert not Path(a.journal_local + ".creation-incertaine").exists() and CLE not in j


def test_louer_verification_seule_rien_cree(tmp_path):
    code, a, d = louer(tmp_path, verifier_seulement=True)
    j = Path(a.journal_local).read_text()
    assert code == 0 and appels(d) == 0 and "vérification seulement : rien créé" in j and "GO_MACHINE" in j
    assert "coût de la machine au plus 4.4779 USD ≤ 35" in j and "longueurs : --args" in j


def test_seconde_location_et_creation_incertaine_refusees(tmp_path):
    assert louer(tmp_path)[0] == 0
    code, a, d = louer(tmp_path)
    assert code == 2 and "déjà eu lieu ou est incertaine" in Path(a.journal_local).read_text()
    t2 = tmp_path / "bis"
    t2.mkdir()
    code, a, d = louer(t2, reponses=(("texte libre", "", 0),))
    assert code == 2 and Path(a.journal_local + ".creation-incertaine").exists()
    assert v4.louer(args_louer(t2), v4.ClientPiloteV4(ENV_PILOTE, "/bin/false"), JOUR, dict(ENV_PILOTE), MAINTENANT) == 2


def test_no_such_ask_puis_contrat_au_deuxieme_essai(tmp_path):
    code, a, d = louer(tmp_path, reponses=(("", NSA, 0), (CONTRAT, "", 0)))
    assert code == 0 and appels(d) == 2 and (d / "offres").read_text().split() == ["21", "22"]
    assert json.loads(Path(a.journal_local + ".etat.json").read_text())["prix_h_usd"] == 0.06
    assert not Path(a.journal_local + ".creation-incertaine").exists()


@pytest.mark.parametrize("reponse, marqueur", [
    (("", "{'success': False, 'error': 'insufficient_credit', 'msg': 'pas de crédit'}", 0), False),
    (("réponse illisible", "", 0), True),
])
def test_autre_reponse_un_seul_appel(tmp_path, reponse, marqueur):
    code, a, d = louer(tmp_path, reponses=(reponse, (CONTRAT, "", 0)))
    assert code == 2 and appels(d) == 1 and Path(a.journal_local + ".creation-incertaine").exists() is marqueur


def test_client_v2_admet_la_cle_d_argon_et_la_masque(tmp_path):
    o = s10.verifier_offre_sonde([GPU], 21)
    c = v4.corps("a" * 40, "b" * 40, "c" * 64, "d" * 40, o, {"CLE_ARGON": CLE, "GH_TOKEN": JETON}, 1_800_000_000)
    outil, d = vastai_factice(tmp_path, [("", f"{{'success': False, 'error': 'x', 'msg': 'écho {CLE} {JETON}'}}", 1)])
    with pytest.raises(s10.RefusVastSansCreation) as e:
        v4.ClientPiloteV4(ENV_PILOTE, outil).creer(21, c)
    assert CLE not in str(e.value) and JETON not in str(e.value) and appels(d) == 1
    with pytest.raises(s10.RefusAvantAppel, match="clé de modèle"):  # artefact de départ : le client de la sonde la refuse
        s10.ClientPilote(ENV_PILOTE, outil).creer(21, c)
    c["env"]["GEMINI_API_KEY"] = "autre"
    with pytest.raises(s10.RefusAvantAppel, match="autre que CLE_ARGON"):
        v4.ClientPiloteV4(ENV_PILOTE, outil).creer(21, c)
    assert appels(d) == 1


# --- pilote : contrôle, facturation, inventaire, sous-commandes en fichier seul ----------------------------------------------


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
    f.write_text(json.dumps({"identifiant": 4242, "etiquette": v4.ETIQUETTE, "t0_utc": "2026-11-05T09:00:00Z",
                             "borne_signe_de_vie_utc": "2026-11-05T09:30:00Z", "echeance_finale_utc": "2026-11-08T18:10:00Z",
                             "controles_utc": ["2026-11-05T09:40:00Z", "2026-11-08T18:35:00Z"]}))
    return type("A", (), {"etat": str(f), "journal_local": str(tmp_path / "controle.log")})()


def heure(j, hh, mm):
    return dt.datetime(2026, 11, j, hh, mm, tzinfo=dt.timezone.utc)


INST = {"id": 4242, "label": "a1-v3-troisieme-v1", "actual_status": "running"}


@pytest.mark.parametrize("instances, vie, quand, code, gestes", [
    ([], False, heure(5, 9, 41), 0, []),
    ([INST], False, heure(5, 9, 20), 5, []),
    ([INST], True, heure(5, 9, 41), 5, []),
    ([INST], False, heure(5, 9, 41), 1, [("detruire", 4242)]),
    ([dict(INST, label="autre")], False, heure(5, 9, 41), 2, []),
    ([dict(INST, actual_status="stopped")], True, heure(8, 18, 35), 7, []),
    ([INST], False, heure(8, 18, 35), 7, []),  # après l'échéance : aucun geste, même sans signe de vie
])
def test_controler(tmp_path, instances, vie, quand, code, gestes):
    c = Inventaire(instances)
    assert v4.controler(etat_pilote(tmp_path), c, lambda: vie, quand, dict(ENV_PILOTE)) == code
    assert c.gestes == gestes


def test_controler_destruction_non_suivie_et_ls_remote_en_echec(tmp_path):
    c = Inventaire([INST], reste=True)
    assert v4.controler(etat_pilote(tmp_path), c, lambda: False, heure(5, 9, 41), dict(ENV_PILOTE)) == 3

    def echec():
        raise s10.RefusRecontroler("ls-remote : code 128")
    c = Inventaire([INST])
    assert v4.controler(etat_pilote(tmp_path), c, echec, heure(5, 9, 41), dict(ENV_PILOTE)) == 6 and c.gestes == []


def test_facturation_champs_filtres_et_etiquette_autre(tmp_path):
    a = etat_pilote(tmp_path)
    assert v4.relever_facturation(a, Inventaire([dict(INST, dph_total=0.055, storage_cost=0.1)]), dict(ENV_PILOTE)) == 0
    j = Path(a.journal_local).read_text()
    assert '"dph_total": 0.055' in j and CLE not in j and "extra_env" not in j and "onstart" not in j
    assert v4.relever_facturation(a, Inventaire([dict(INST, label="autre")]), dict(ENV_PILOTE)) == 2


def module_seul(*args, env=None):
    """Le module lancé comme fichier seul, comme sur la machine et chez la fille (`python3 -I -B …`)."""
    return subprocess.run([sys.executable, "-I", "-B", str(RACINE / v4.MODULE), *args], capture_output=True, text=True,
                          env=env or {"PATH": os.environ["PATH"]}, timeout=120)


def test_fichier_seul_une_seule_classe_refus_et_offre(tmp_path):
    r = module_seul("inventaire")  # sans VAST_API_KEY : le refus levé par la v10 est attrapé par la v2 (même classe)
    assert r.returncode == 2 and "REFUS : VAST_API_KEY absente" in r.stderr and "Traceback" not in r.stderr
    f = tmp_path / "offres.json"
    f.write_text(json.dumps([VOLUME, dict(GPU, id=22, dph_total=0.06), GPU]))
    r = module_seul("offre", "--offres", str(f))
    assert r.returncode == 0 and r.stdout.strip() == "21"
    f.write_text(json.dumps([VOLUME, t1.OFFRE]))
    assert module_seul("offre", "--offres", str(f)).returncode == 2


# --- script de démarrage et minuterie ---------------------------------------------------------------------------------------


def outil(d: Path, nom: str, corps: str) -> None:
    p = d / nom
    p.write_text("#!/bin/sh\n" + corps)
    p.chmod(0o755)


def depot_avec_amorce(tmp_path, amorce: str):
    nu = tmp_path / "prive-amorce.git"
    t1.run("git", "init", "-q", "--bare", "-b", "main", str(nu))
    t1.run("git", "-C", str(nu), "config", "uploadpack.allowFilter", "true")
    t1.run("git", "-C", str(nu), "config", "uploadpack.allowReachableSHA1InWant", "true")
    w = tmp_path / "w-amorce"
    t1.run("git", "init", "-q", "-b", "main", str(w))
    (w / "scripts").mkdir()
    (w / v4.AMORCE).write_text(amorce)
    t1.run("git", "add", "-A", cwd=w)
    t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "amorce", cwd=w)
    t1.run("git", "push", "-q", str(nu), "HEAD:refs/heads/main", cwd=w)
    return f"file://{nu}", t1.run("git", "rev-parse", "HEAD", cwd=w)


def demarrer(tmp_path, commit, depot, delete_code="200", label="a1-v3-troisieme-v1", ident="123", minuterie=None,
             detruire=False, **env_en_plus):
    racine = tmp_path / "racine"
    racine.mkdir(exist_ok=True)
    if minuterie:
        (racine / "a1v3-minuterie.txt").write_text(minuterie)
    if detruire:
        (racine / v4.DETRUIRE_MAINTENANT).write_text("")
    appels_ = tmp_path / "appels-curl.txt"
    b = tmp_path / "bin"
    b.mkdir(exist_ok=True)
    outil(b, "curl", f'echo "$@" >> "{appels_}"\ncase "$*" in *"-X DELETE"*) printf "{delete_code}";; *"-X PUT"*) printf 200;; '
                     f'*) printf \'{{"id": {ident}, "label": "{label}"}}\';; esac\n')
    env = {"PATH": f"{b}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_A1V3": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "A1V3_DUREE_S": "1", "A1V3_MARGE_S": "1", "A1V3_VIE_APRES_S": "1",
           "DEPOT_URL": str(depot), "GH_TOKEN": JETON, "CONTAINER_ID": ident, "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null", **env_en_plus}
    debut = time.time()
    r = subprocess.run(["bash", "-c", v4.script_de_demarrage(commit)], env=env, capture_output=True, text=True, timeout=240)
    log = racine / "a1v3-minuterie.log"
    fin = time.time() + 15
    while time.time() < fin and "HTTP" not in (log.read_text() if log.exists() else "") and "aucun geste" not in (
            log.read_text() if log.exists() else ""):
        time.sleep(0.2)
    return r, racine, (appels_.read_text() if appels_.exists() else ""), time.time() - debut


def test_demarrage_cas_sain_minuterie_clone_amorce_destruction(tmp_path):
    depot, commit = depot_avec_amorce(tmp_path, 'echo jouee > "$RACINE_A1V3/amorce-jouee.txt"\n')
    r, racine, appels_, _ = demarrer(tmp_path, commit, depot)
    assert r.returncode == 0, r.stderr
    temps = (racine / "a1v3-temps.txt").read_text()
    assert (racine / "amorce-jouee.txt").exists() and "clone 0 en" in temps and "amorce finie" in temps and "code 0" in temps
    log = (racine / "a1v3-minuterie.log").read_text()
    assert "DELETE instance 123 (essai 1) : HTTP 200" in log and "destruction demandée avant" not in log
    assert "-X PUT" not in appels_ and CLE_VAST not in log + temps and not (racine / v4.DETRUIRE_MAINTENANT).exists()


def test_demarrage_amorce_en_refus_destruction_immediate(tmp_path):
    """Échéance lointaine (1 h) : l'amorce refuse (code 2), la minuterie détruit tout de suite, le conteneur finit."""
    depot, commit = depot_avec_amorce(tmp_path, 'echo "AMORCE : refus jouet"; exit 2\n')
    r, racine, appels_, duree = demarrer(tmp_path, commit, depot, A1V3_DUREE_S="3600")
    temps = (racine / "a1v3-temps.txt").read_text()
    assert "code 2" in temps and "amorce en refus : destruction demandée" in temps and duree < 90
    log = (racine / "a1v3-minuterie.log").read_text()
    assert "destruction demandée avant l'échéance" in log and "DELETE instance 123 (essai 1) : HTTP 200" in log
    t0, ech = (racine / "a1v3-minuterie.txt").read_text().split()
    assert int(ech) - int(t0) == 3601  # l'échéance écrite reste celle d'origine


def test_demarrage_reprise_apres_refus_rien_n_est_lance(tmp_path):
    depot, commit = depot_avec_amorce(tmp_path, 'echo jouee > "$RACINE_A1V3/amorce-jouee.txt"\n')
    t = int(time.time())
    r, racine, appels_, duree = demarrer(tmp_path, commit, depot, minuterie=f"{t} {t + 3601}\n", detruire=True)
    assert not (racine / "amorce-jouee.txt").exists() and not (racine / "amorce-depot").exists()
    assert "rien n'est lancé" in (racine / "a1v3-temps.txt").read_text() and duree < 90
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "a1v3-minuterie.log").read_text()


def test_demarrage_clone_impossible_destruction_immediate(tmp_path):
    r, racine, appels_, duree = demarrer(tmp_path, "b" * 40, f"file://{tmp_path}/absent.git", A1V3_DUREE_S="3600")
    assert "amorce absente du clone" in (racine / "a1v3-temps.txt").read_text() and duree < 90
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "a1v3-minuterie.log").read_text()


@pytest.mark.parametrize("kw, attendu, interdit", [
    ({"delete_code": "403"}, "ALARME : destruction non obtenue avant la fin de vie", "-X PUT"),
    ({"label": "sonde-a1-v3-v10"}, "pas a1-v3-troisieme-v1 : aucun geste", "-X DELETE"),
    ({"ident": "58936100"}, "instance protégée : aucun geste", "-X DELETE"),
    ({"ident": "12a"}, "identifiant illisible : aucun geste", "-X DELETE"),
])
def test_demarrage_artefacts_de_la_minuterie(tmp_path, kw, attendu, interdit):
    r, racine, appels_, _ = demarrer(tmp_path, "b" * 40, f"file://{tmp_path}/absent.git", **kw)
    fin = time.time() + 20
    while time.time() < fin and attendu not in (racine / "a1v3-minuterie.log").read_text():
        time.sleep(0.2)
    assert attendu in (racine / "a1v3-minuterie.log").read_text()
    assert interdit not in appels_


def test_demarrage_echeance_absolue_passee_et_crochets_bornes(tmp_path):
    passe = int(time.time()) - 10
    r, racine, appels_, duree = demarrer(tmp_path, "b" * 40, f"file://{tmp_path}/absent.git", A1V3_DUREE_S="3600",
                                         ECHEANCE_UTC_S=str(passe))
    assert int((racine / "a1v3-minuterie.txt").read_text().split()[1]) == passe and duree < 90
    s = v4.script_de_demarrage("b" * 40)
    assert '[ "$D" -le 288000 ] || D=288000' in s and '[ "$MARGE" -le 3600 ] || MARGE=3600' in s
    with pytest.raises(h.Refus):
        v4.script_de_demarrage("main")


# --- amorce ------------------------------------------------------------------------------------------------------------------


def amorce(tmp_path, retirer=(), meminfo_kb=16_000_000, modules=v4.MODULES, **modif):
    racine = tmp_path / "racine-amorce"
    d = racine / "amorce-depot" / "src" / "controle_ia"
    d.mkdir(parents=True, exist_ok=True)
    for m in modules:
        (d / m).write_text(f'import pathlib\npathlib.Path({str(racine / "exec-atteint.txt")!r}).write_text("oui")\n')
    mem = tmp_path / "meminfo"
    mem.write_text(f"MemTotal:       {meminfo_kb} kB\n" if meminfo_kb is not None else "illisible\n")
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "COMMIT_PUBLIC": "b" * 40, "SHA_TEXTE": "c" * 64,
           "COMMIT_REGISTRE": "d" * 40, "GO_ID": "GO-2026-11-04-06", "GO_MACHINE": "GO-2026-11-05-03", "PRIX_H_USD": "0.055",
           "ECHEANCE_UTC_S": "1800000000", "CLE_ARGON": CLE, "GH_TOKEN": JETON, "RACINE_AMORCE": str(racine),
           "SAUTER_INSTALLATION": "1", "A1V3_MEMINFO": str(mem),
           "A1V3_PYTHON_IMAGE": str(faux_python(tmp_path, "image", "3.13")),
           "A1V3_PYTHON_CONFIGURATION": str(faux_python(tmp_path, "configuration", "3.11"))}
    for k in retirer:
        env.pop(k)
    env.update(modif)
    r = subprocess.run(["bash", str(RACINE / v4.AMORCE)], env=env, capture_output=True, text=True, timeout=60)
    return r, racine


def test_amorce_cas_sain_jusqu_a_exec(tmp_path):
    r, racine = amorce(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (racine / "exec-atteint.txt").exists() and "16000000 kB" in (racine / "a1v3-memoire.txt").read_text()
    assert CLE not in r.stdout + r.stderr and JETON not in r.stdout + r.stderr


@pytest.mark.parametrize("kw, motif", [
    ({"retirer": ("CLE_ARGON",)}, "variable CLE_ARGON absente"),
    ({"retirer": ("GO_MACHINE",)}, "variable GO_MACHINE absente"),
    ({"GO_ID": "GO-2026-11-03-01"}, "au lieu de GO-2026-11-04-06"),
    ({"GO_MACHINE": "GO-2026-11-04-09"}, "au lieu de GO-2026-11-05-03"),
    ({"GEMINI_API_KEY": "autre-cle"}, "GEMINI_API_KEY présente"),
    ({"RR_PROD_API_KEY_2": "autre-cle"}, "RR_PROD_API_KEY_2 présente"),
    ({"ECHEANCE_UTC_S": "demain"}, "ECHEANCE_UTC_S non entière"),
    ({"meminfo_kb": 1_000_000}, "< 2 Go"),
    ({"meminfo_kb": None}, "mémoire réelle illisible"),
    ({"modules": v4.MODULES[:3]}, "sonde_hote_durable_a1_v3_v10.py absent"),
])
def test_amorce_artefacts(tmp_path, kw, motif):
    r, racine = amorce(tmp_path, **kw)
    assert r.returncode == 2 and motif in r.stdout and not (racine / "exec-atteint.txt").exists(), r.stdout
    assert CLE not in r.stdout + r.stderr and "autre-cle" not in r.stdout


def test_amorce_curl_absent(tmp_path):
    d = tmp_path / "bin-sans-curl"
    d.mkdir()
    for o in ("bash", "date", "grep", "tr", "cut", "python3", "cat"):
        cible = subprocess.run(["bash", "-c", f"command -v {o}"], capture_output=True, text=True).stdout.strip()
        if cible:
            (d / o).symlink_to(cible)
    r, racine = amorce(tmp_path, PATH=str(d))
    assert r.returncode == 2 and "curl absent : rien ne part" in r.stdout


# --- machine -----------------------------------------------------------------------------------------------------------------


@pytest.fixture
def monde(tmp_path):
    def fabriquer(comportement=None, registre_source=None, registre_main=None, etiquette="a1-v3-troisieme-v1",
                  depuis_s=None, echeance_dans_s=4800):
        comp = tmp_path / "comportement.json"
        comp.write_text(json.dumps(comportement or {"code": 0}))
        nuit = h.NUIT
        relais = (t1.RELAIS % {"drapeau": str(tmp_path / "relais-mort-une-fois"), "comportement": str(comp)}).encode()
        piece = b"consigne factice\n"
        conf = json.dumps({"pieces": {"consigne": {"chemin": "pieces/a.md", "sha256": t1.sha(piece)}}}).encode()
        sources = {f"{nuit}/commande_argon_v56_nuit_v2.py": relais, f"{nuit}/registre_depense_cumulee_v1.py": b"# r\n",
                   f"{nuit}/pieces/a.md": piece, "donnees/espece-seule-v1/collisionneur_v7.py": b"# c\n"}
        reg_main = registre_main or ("# Registre\n\n" + t1.ENTETE + LIGNE_06 + LIGNE_0503).encode()
        nu = t1.depot_nu_avec_branches(tmp_path, {
            "main": {"registres/go.md": reg_main, ".claude/hooks/garde_calcul.py": GARDE.read_bytes(),
                     "LISEZMOI.md": b"racine de main\n"},
            h.SOURCE_REGISTRE: {"registres/go.md": registre_source or ("# R\n\n" + t1.ENTETE + LIGNE_06).encode()},
            h.REF_SOURCES: sources,
            h.REF_CONFIGURATION: {h.CHEMIN_CONF_DANS_REF: conf},
        })
        t1.run("git", "-C", str(nu), "config", "uploadpack.allowFilter", "true")
        t1.run("git", "-C", str(nu), "config", "uploadpack.allowReachableSHA1InWant", "true")
        clone = tmp_path / "amorce-depot"  # comme le script de démarrage : partiel, superficiel, clairsemé
        t1.run("git", "init", "-q", str(clone))
        t1.run("git", "-C", str(clone), "remote", "add", "origin", f"file://{nu}")
        t1.run("git", "-C", str(clone), "sparse-checkout", "set", "scripts", "src/controle_ia")
        t1.run("git", "-C", str(clone), "fetch", "-q", "--filter=blob:none", "--depth", "1", "origin", "main")
        t1.run("git", "-C", str(clone), "checkout", "-q", "--detach", "FETCH_HEAD")
        commit_registre = t1.run("git", "-C", str(nu), "rev-parse", f"refs/heads/{h.SOURCE_REGISTRE}")
        empreintes = {f"{nuit}/configuration-mini-course-kimi-argon-v3.json": t1.sha(conf),
                      f"{nuit}/commande_argon_v56_nuit_v2.py": t1.sha(relais),
                      f"{nuit}/registre_depense_cumulee_v1.py": t1.sha(b"# r\n"),
                      "donnees/espece-seule-v1/collisionneur_v7.py": t1.sha(b"# c\n")}
        pub = tmp_path / "public"
        t1.run("git", "init", "-q", "-b", "main", str(pub))
        lanceur = pub / "orchestrator/demonstrations/attaque_goodhart_v3.py"
        lanceur.parent.mkdir(parents=True)
        lanceur.write_text(t1.LANCEUR % {"comportement": str(comp), "compteur": str(tmp_path / "courses-lancees")})
        t1.run("git", "add", "-A", cwd=pub)
        t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "code gelé", cwd=pub)
        gele = t1.run("git", "rev-parse", "HEAD", cwd=pub)
        texte = pub / v4.NOM_TEXTE  # texte v4
        texte.parent.mkdir(parents=True, exist_ok=True)
        texte.write_text("texte scellé v3 (jouet)\n")
        Path(str(texte) + ".sha256").write_text(f"{t1.sha(texte.read_bytes())}  {texte.name}\n")
        t1.run("git", "add", "-A", cwd=pub)
        t1.run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "texte v3", cwd=pub)
        if depuis_s is not None:  # départ du conteneur écrit par le script de démarrage (m1)
            (tmp_path / "a1v3-minuterie.txt").write_text(f"{time.time() - depuis_s:.1f} 1800000000\n")
        for nom in ("a1v3-temps.txt", "amorce-a1v3-v4.log", "a1v3-memoire.txt"):
            (tmp_path / nom).write_text(f"{nom} : journal du démarrage (jouet)\n")
        r = h.Reglages(travail=tmp_path / "a1-v3-troisieme-v1", clone_prive=clone, clone_public=tmp_path / "pub-clone",
                       depot_public=str(pub), racine_sources=tmp_path / "sources", empreintes=empreintes,
                       commit_code_gele=gele, python_relais=PY_MACHINE, python_course=PY_MACHINE,
                       port=t1.port_libre(), periode_s=0.1, duree_max_s=600, attente_relais_s=10, essais_poussee=2,
                       attente_poussee_s=0, jouet=True, vast_jouet=tmp_path / "vast.json", aujourd_hui=JOUR)
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "etat": "running", "label": etiquette}],
                                                 "gestes": []})
        env = {"COMMIT_PUBLIC": t1.run("git", "rev-parse", "HEAD", cwd=pub), "SHA_TEXTE": t1.sha(texte.read_bytes()),
               "COMMIT_REGISTRE": commit_registre, "GO_ID": "GO-2026-11-04-06", "GO_MACHINE": "GO-2026-11-05-03",
               "PRIX_H_USD": "0.2", "ECHEANCE_UTC_S": str(int(time.time()) + echeance_dans_s), "CLE_ARGON": CLE,
               "GH_TOKEN": JETON, "CONTAINER_ID": "90000001", "CONTAINER_API_KEY": CLE_VAST}
        return r, env, nu
    return fabriquer


def gestes(r):
    return json.loads(r.vast_jouet.read_text())["gestes"]


def journal(f, b):
    return f[f"{b}/journal-hote-a1-v3-troisieme-v1.log"]


def test_machine_cas_sain_partie_de_main_signe_de_vie_et_destruction(monde, tmp_path):
    r, env, nu = monde()
    assert v4.MachineV4(r, env).principal() == 0
    b = h.BRANCHE_DONNEES
    f = t1.branche(nu, b)
    j = journal(f, b)
    for attendu in ("hote-durable-a1-v3-v4 ; machine GO-2026-11-05-03 ; course GO-2026-11-04-06",
                    "GO accepté par la garde de main", '"plafond_usd": 35.0', "aucun doublon",
                    f"signe de vie poussé : {v4.BRANCHE_VIE}", "pièces gelées : 4 empreintes égales",
                    "--verifier-seulement : code 0", "course lancée : PID", "fin du lanceur : code 0", "inchangé"):
        assert attendu in j, attendu
    assert f[f"{b}/code-sortie-lanceur.txt"].strip() == "0" and f"{b}/demarrage/amorce-a1v3-v4.log" in f
    for ligne in f[f"{b}/EMPREINTES-sortie-a1-v3-troisieme-v1.txt"].splitlines():
        e, nom = ligne.split("  ", 1)
        assert t1.sha(f[f"{b}/{nom}"].encode()) == e
    parent = t1.run("git", "-C", str(nu), "rev-parse", f"refs/heads/{b}^")
    assert parent == t1.run("git", "-C", str(nu), "rev-parse", "refs/heads/main")  # partie de main
    assert t1.run("git", "-C", str(nu), "show", f"refs/heads/{b}:LISEZMOI.md") == "racine de main"
    assert t1.branche(nu, v4.BRANCHE_VIE)  # signe de vie versé, sans donnée de la course
    t1.jamais_de_secret(f)
    t1.jamais_de_secret(t1.branche(nu, v4.BRANCHE_VIE))
    assert gestes(r) == [["detruire", 90000001]] and (r.travail / "ETAT").read_text().strip() == "verse"


def registre_canal_a_doublons():
    return ("# R\n\n" + t1.ENTETE + LIGNE_06 + LIGNE_06).encode()


@pytest.mark.parametrize("option, env_modif, motif", [
    ({"registre_source": registre_canal_a_doublons()}, {}, "identifiants en double"),
    ({}, {"COMMIT_REGISTRE": "e" * 40}, "absent de la branche canal/conv-audit-n04"),
    ({"registre_main": ("# R\n\n" + t1.ENTETE + LIGNE_06).encode()}, {}, "GO-2026-11-05-03 absent"),
    ({}, {"GO_MACHINE": "GO-2026-11-04-09"}, "exigé ici"),
    ({}, {"GO_MACHINE": None}, "variable GO_MACHINE absente"),
    ({"echeance_dans_s": 3600 + 30}, {}, "échéance absolue trop proche"),
    ({}, {"ECHEANCE_UTC_S": "demain"}, "ECHEANCE_UTC_S"),
    ({}, {"GEMINI_API_KEY": "autre"}, "autre que CLE_ARGON"),
    ({}, {"PRIX_H_USD": "0.5"}, "prix horaire"),
])
def test_machine_refus_rien_ne_part(monde, tmp_path, option, env_modif, motif):
    r, env, nu = monde(**option)
    for k, v in env_modif.items():
        env.pop(k) if v is None else env.__setitem__(k, v)
    assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    f = t1.branche(nu, h.BRANCHE_REFUS)
    j = journal(f, h.BRANCHE_REFUS)
    assert "REFUS" in j and motif in j, j[-500:]
    t1.jamais_de_secret(f)
    assert gestes(r) == [["detruire", 90000001]]


def test_machine_versement_impossible_machine_arretee(monde, tmp_path):
    r, env, nu = monde()
    t1.run("git", "-C", str(nu), "branch", h.BRANCHE_DONNEES, "main")  # branche déjà présente : R12
    assert v4.MachineV4(r, env).principal() == 3
    assert "déjà présente (R12)" in (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()
    assert gestes(r) == [["arreter", 90000001]]


def test_machine_fuite_d_un_secret_rien_verse(monde):
    r, env, nu = monde({"code": 0, "fuite": True})
    assert v4.MachineV4(r, env).principal() == 3
    assert t1.branche(nu, h.BRANCHE_DONNEES) == {} and gestes(r) == [["arreter", 90000001]]
    assert CLE not in (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()


def test_machine_exception_du_versement_attrapee(monde, monkeypatch):
    r, env, nu = monde()

    def casse(self, branche, liste):
        raise RuntimeError(f"panne jouet {JETON}")
    monkeypatch.setattr(v4.MachineV4, "verser", casse)
    assert v4.MachineV4(r, env).principal() == 3
    j = (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()
    assert "VERSEMENT IMPOSSIBLE : RuntimeError" in j and JETON not in j and gestes(r) == [["arreter", 90000001]]


class VastRefuse(h.ClientVastJouet):
    def __init__(self, chemin, refuse_arret=False):
        super().__init__(chemin)
        self.refuse_arret = refuse_arret

    def detruire(self, ident):
        raise h.Refus("Vast DELETE : HTTP 500")

    def arreter(self, ident):
        if self.refuse_arret:
            raise h.Refus("Vast PUT : HTTP 500")
        super().arreter(ident)


@pytest.mark.parametrize("refuse_arret, code, geste", [(False, 3, [["arreter", 90000001]]), (True, 4, [])])
def test_machine_destruction_refusee_puis_arret(monde, monkeypatch, refuse_arret, code, geste):
    r, env, nu = monde()
    monkeypatch.setattr(v4.MachineV4, "client_vast", lambda self: VastRefuse(self.r.vast_jouet, refuse_arret))
    assert v4.MachineV4(r, env).principal() == code
    assert t1.branche(nu, h.BRANCHE_DONNEES) and gestes(r) == geste


def test_machine_etiquette_autre_aucun_geste(monde):
    r, env, nu = monde(etiquette="sonde-a1-v3-v10")
    assert v4.MachineV4(r, env).principal() == 4 and gestes(r) == []


def test_machine_reprise_ne_relance_rien(monde, tmp_path):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    assert "REPRISE du conteneur" in journal(t1.branche(nu, h.BRANCHE_INTERROMPUE), h.BRANCHE_INTERROMPUE)
    assert gestes(r) == [["detruire", 90000001]]


def test_machine_cout_compte_depuis_le_depart_du_conteneur(monde, tmp_path):
    r, env, nu = monde(depuis_s=1800.0)
    m = v4.MachineV4(r, env)
    assert m.depart_conteneur is not None and abs(m.cout_machine() - 0.2 * 0.5) < 0.01  # 30 min à 0,2 USD/h
    (tmp_path / "a1v3-minuterie.txt").unlink()  # artefact : sans l'heure de départ, le compte part de l'hôte (v1)
    m2 = v4.MachineV4(r, env)
    assert m2.depart_conteneur is None and m2.cout_machine() < 0.001


@pytest.mark.parametrize("dans_s, borne_max", [(4800, 600), (3600 + 90, 90)])
def test_machine_echeance_absolue_borne_la_course(monde, dans_s, borne_max):
    r, env, nu = monde(echeance_dans_s=dans_s)
    assert v4.MachineV4(r, env).principal() == 0
    j = journal(t1.branche(nu, h.BRANCHE_DONNEES), h.BRANCHE_DONNEES)
    s = float(j.split("durée de la course bornée à ")[1].split(" s")[0])
    assert borne_max - 5 <= s <= borne_max and gestes(r) == [["detruire", 90000001]]


# --- v3 : C1 (interpréteur 3.13), C2 (signe de vie exigé), C3 (copie neuve à la reprise) -------------------------------------


def faux_python(tmp_path, nom, version, numpy="2.5.3"):
    """Interpréteur factice : répond sa version (`--version`, `-c`), sinon passe la main au vrai Python des essais."""
    d = tmp_path / f"faux-python-{nom}"
    d.mkdir(exist_ok=True)
    p = d / "python3"
    if not p.exists():
        p.write_text(f'#!/bin/sh\ncase "$1" in --version) echo "Python {version}.0 (jouet {nom})";; '
                     f'-c) case "$2" in *numpy*) echo "{numpy}";; *) echo "{version}";; esac;; '
                     f'*) exec {sys.executable} "$@";; esac\n')
        p.chmod(0o755)
    return p


def test_c1_reglages_et_path_du_relais_artefact_de_depart_v2():
    r = v4.reglages()
    assert (r.python_relais, r.python_course) == ("/usr/local/bin/python3", "/usr/local/bin/python3")
    assert v2.reglages().python_relais == "/usr/bin/python3"  # la v2 lançait le relais sous /usr/bin/python3 (3.11 sur l'image)
    m3 = v4.MachineV4(h.Reglages(travail=Path("/nulle/part/a1-v3-troisieme-v1")), {"CLE_ARGON": CLE})
    m2 = v2.MachineV2(h.Reglages(travail=Path("/nulle/part/a1-v3-troisieme-v1")), {"CLE_ARGON": CLE})
    assert m3.env_relais()["PATH"].startswith("/usr/local/bin:") and m2.env_relais()["PATH"].startswith("/usr/bin:")
    assert m3.python_configuration == "/usr/bin/python3"


def test_c1_cas_sain_versions_au_journal(monde):
    r, env, nu = monde()
    assert v4.MachineV4(r, env).principal() == 0
    j = journal(t1.branche(nu, h.BRANCHE_DONNEES), h.BRANCHE_DONNEES)
    assert "interpréteurs (C1) : relais" in j and "configuration gelée /usr/bin/python3 : Python 3.13" in j


@pytest.mark.parametrize("quoi", ["relais", "course", "configuration"])
def test_c1_interpreteur_autre_que_3_13_rien_ne_part(monde, tmp_path, quoi):
    r, env, nu = monde()
    faux = str(faux_python(tmp_path, "debian", "3.11"))
    if quoi == "relais":
        r.python_relais = faux
    elif quoi == "course":
        r.python_course = faux
    m = v4.MachineV4(r, env, python_configuration=faux) if quoi == "configuration" else v4.MachineV4(r, env)
    assert m.principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    j = journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)
    assert "interpréteur autre que Python 3.13 (C1)" in j and "Python 3.11.0 (jouet debian)" in j, j[-400:]
    assert gestes(r) == [["detruire", 90000001]]


def test_c1_amorce_lien_vers_l_interpreteur_de_l_image(tmp_path):
    r, racine = amorce(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    conf = tmp_path / "faux-python-configuration" / "python3"
    assert conf.is_symlink() and conf.resolve() == (tmp_path / "faux-python-image" / "python3").resolve()
    assert "interpréteurs avant (C1)" in r.stdout and "Python 3.11.0 (jouet configuration)" in r.stdout
    assert "interpréteurs après (C1)" in r.stdout and r.stdout.count("Python 3.13.0 (jouet image)") >= 3
    assert (racine / "exec-atteint.txt").exists()


@pytest.mark.parametrize("cas, motif", [("image-3.11", "n'est pas Python 3.13 (C1)"), ("lien-impossible", "impossible (C1)")])
def test_c1_amorce_artefacts(tmp_path, cas, motif):
    if cas == "image-3.11":
        r, racine = amorce(tmp_path, A1V3_PYTHON_IMAGE=str(faux_python(tmp_path, "vieille-image", "3.11")))
    else:
        r, racine = amorce(tmp_path, A1V3_PYTHON_CONFIGURATION="/proc/inexistant/python3")
    assert r.returncode == 2 and motif in r.stdout and not (racine / "exec-atteint.txt").exists(), r.stdout


def test_c2_signe_de_vie_deja_present_rien_ne_part(monde, tmp_path):
    r, env, nu = monde()
    t1.run("git", "-C", str(nu), "branch", v4.BRANCHE_VIE, "main")  # poussée du signe de vie refusée (R12)
    assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    j = journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)
    assert "signe de vie non poussé" in j and "signe de vie non vérifié par ls-remote (C2)" in j
    assert gestes(r) == [["detruire", 90000001]]


def test_c2_poussee_du_signe_de_vie_non_verifiee_rien_ne_part(monde, tmp_path, monkeypatch):
    r, env, nu = monde()
    original = v4.MachineV4._pousser
    monkeypatch.setattr(v4.MachineV4, "_pousser",
                        lambda self, v, b, url: None if b == v4.BRANCHE_VIE else original(self, v, b, url))
    assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    assert "(C2)" in journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)



@pytest.mark.parametrize("version, code, verse", [("v3", 0, True), ("v2", 3, False)])
def test_c3_reprise_apres_poussee_finale_manquee(monde, version, code, verse):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("scellement\n")
    (r.travail.parent / (r.travail.name + "-versement")).mkdir()  # copie laissée par une poussée finale manquée
    m = v4.MachineV4(r, env) if version == "v3" else v2.MachineV2(r, env)
    assert m.principal() == code
    f = t1.branche(nu, h.BRANCHE_INTERROMPUE)
    assert bool(f) is verse
    if verse:
        assert "REPRISE du conteneur" in journal(f, h.BRANCHE_INTERROMPUE) and gestes(r) == [["detruire", 90000001]]
    else:  # artefact de départ : la v2 bute sur la copie restée et arrête la machine sans verser
        assert "déjà présente (R12)" in (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()
        assert gestes(r) == [["arreter", 90000001]]


def test_c3_seconde_reprise_copie_neuve_deja_la_arret(monde):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("scellement\n")
    (r.travail.parent / (r.travail.name + "-versement-interrompue-v1")).mkdir()
    assert v4.MachineV4(r, env).principal() == 3 and gestes(r) == [["arreter", 90000001]]
    assert t1.branche(nu, h.BRANCHE_INTERROMPUE) == {}


# --- v4 : texte v4, corrections 1 à 7, artefacts de la correction 8 -----------------------------------------------------------


def test_v4_texte_v4_dans_la_commande_et_sur_la_machine(monde):
    r, env, nu = monde()
    m = v4.MachineV4(r, env)
    cmd = m.cmd_course(False)
    assert "prereg/preenregistrement-attaque-goodhart-v3-v4.md" in cmd and h.NOM_TEXTE.removeprefix("orchestrator/") not in cmd
    assert v3.MachineV3(r, env).cmd_course(False).count("prereg/preenregistrement-attaque-goodhart-v3-v3.md") == 1  # départ
    assert h.NOM_TEXTE.endswith("-v3-v3.md")  # la v1 gelée n'est pas touchée
    assert v4.MachineV4(r, env).principal() == 0
    j = journal(t1.branche(nu, h.BRANCHE_DONNEES), h.BRANCHE_DONNEES)
    assert "course lancée" in j and "git status --porcelain juste avant la course : vide" in j


def test_v4_texte_v3_seul_sur_le_depot_public_refuse(monde, tmp_path):
    r, env, nu = monde()
    pub = tmp_path / "public"  # le dépôt public ne porte que le nom de la v3 : le texte v4 est introuvable
    t1.run("git", "-C", str(pub), "mv", v4.NOM_TEXTE, h.NOM_TEXTE)
    t1.run("git", "-C", str(pub), "mv", v4.NOM_TEXTE + ".sha256", h.NOM_TEXTE + ".sha256")
    t1.run("git", "-C", str(pub), "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "v3 seule")
    env["COMMIT_PUBLIC"] = t1.run("git", "-C", str(pub), "rev-parse", "HEAD")
    assert v4.MachineV4(r, env).principal() == 0
    assert "texte v4 : empreinte None" in journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)
    assert not (tmp_path / "courses-lancees").exists()


class InventaireEchec:
    def __init__(self, x):
        self.x = x

    def instances(self):
        raise self.x


@pytest.mark.parametrize("x, code_v4, code_v3", [
    (h.Refus("vastai show instances : code 1"), 6, 2),
    (s10.RefusCertificat("vastai show instances : appel non parvenu à Vast (certificat) ; code 1"), 6, 2),
    (h.Refus("inventaire illisible"), 6, 2),
    (h.Refus("instance 4242 : étiquette 'autre', pas a1-v3-troisieme-v1 : aucun geste (f8)"), 2, 2),
])
def test_correction_1_controler_echec_de_vastai_recontroler(tmp_path, x, code_v4, code_v3):
    assert v4.controler(etat_pilote(tmp_path), InventaireEchec(x), lambda: False, heure(5, 9, 41), dict(ENV_PILOTE)) == code_v4
    assert v3.controler(etat_pilote(tmp_path), InventaireEchec(x), lambda: False, heure(5, 9, 41), dict(ENV_PILOTE)) == code_v3


class VastQuiGarde(h.ClientVastJouet):
    """Vast qui répond à la destruction sans détruire (refus rendu en HTTP 200)."""

    def detruire(self, ident):
        e = self._lire()
        e["gestes"].append(["detruire", ident])
        self._ecrire(e)


def test_correction_2_destruction_verifiee_par_l_inventaire(monde, monkeypatch):
    r, env, nu = monde()
    monkeypatch.setattr(v4.MachineV4, "client_vast", lambda self: VastQuiGarde(self.r.vast_jouet))
    monkeypatch.setattr(v4.MachineV4, "attente_inventaire_s", 0.0)
    assert v4.MachineV4(r, env).principal() == 3
    assert gestes(r) == [["detruire", 90000001], ["arreter", 90000001]]
    assert "encore listée après la destruction" in (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()


def test_correction_2_artefact_de_depart_la_v3_croit_la_machine_detruite(monde, monkeypatch):
    r, env, nu = monde()
    monkeypatch.setattr(v3.MachineV3, "client_vast", lambda self: VastQuiGarde(self.r.vast_jouet))
    assert v3.MachineV3(r, env).principal() == 0 and gestes(r) == [["detruire", 90000001]]


def test_correction_3_journal_en_panne_fin_quand_meme(monde, monkeypatch):
    r, env, nu = monde()
    original = h.Journal.ecrire

    def ecrire(self, texte):
        if texte.startswith("REFUS"):
            raise OSError("disque plein (jouet)")
        return original(self, texte)
    monkeypatch.setattr(h.Journal, "ecrire", ecrire)
    env["GO_MACHINE"] = "GO-2026-11-04-09"  # un refus avant la course
    assert v4.MachineV4(r, env).principal() == 0 and gestes(r) == [["detruire", 90000001]]
    assert t1.branche(nu, h.BRANCHE_REFUS)


def test_correction_3_artefact_de_depart_la_v3_meurt_sans_geste(monde, monkeypatch):
    r, env, nu = monde()
    original = h.Journal.ecrire

    def ecrire(self, texte):
        if texte.startswith("REFUS"):
            raise OSError("disque plein (jouet)")
        return original(self, texte)
    monkeypatch.setattr(h.Journal, "ecrire", ecrire)
    env["GO_MACHINE"] = "GO-2026-11-04-09"
    with pytest.raises(OSError):
        v3.MachineV3(r, env).principal()
    assert gestes(r) == []


def test_correction_4_code_ecrit_par_le_pilote_et_la_machine(monde, tmp_path):
    code, a, d = louer(tmp_path / "pilote" if (tmp_path / "pilote").mkdir() is None else tmp_path)
    j = Path(a.journal_local).read_text()
    assert code == 0 and "code (correction 4) : COMMIT_PRIVE " + "a" * 40 in j
    for m in v4.MODULES:
        assert f'"{m}": "{t1.sha((RACINE / "src/controle_ia" / m).read_bytes())}"' in j, m
    assert '"amorce_hote_durable_a1_v3_v4.sh": "' + t1.sha((RACINE / v4.AMORCE).read_bytes()) + '"' in j
    r, env, nu = monde()
    env["COMMIT_PRIVE"] = "c" * 40
    assert v4.MachineV4(r, env).principal() == 0
    assert "COMMIT_PRIVE " + "c" * 40 in journal(t1.branche(nu, h.BRANCHE_DONNEES), h.BRANCHE_DONNEES)


def test_correction_5_arbre_modifie_juste_avant_la_course(monde, tmp_path, monkeypatch):
    r, env, nu = monde()
    original = v4.MachineV4.verifier_seulement

    def salir(self):
        original(self)
        (self.r.clone_public / "orchestrator" / "intrus.txt").write_text("x")
    monkeypatch.setattr(v4.MachineV4, "verifier_seulement", salir)
    assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    assert "arbre du dépôt public modifié avant la course (correction 5)" in journal(t1.branche(nu, h.BRANCHE_REFUS),
                                                                                    h.BRANCHE_REFUS)


def test_correction_6_grep_ligne_entiere(tmp_path):
    longue = "| GO-2026-11-04-06 | " + "x" * 300 + " | fin de ligne |"
    f = tmp_path / "go.md"
    f.write_text("tête\n" + longue + "\n")
    assert v4.MachineV4._grep(f, "GO-2026-11-04-06") == ["2:" + longue]
    assert v3.MachineV3._grep(f, "GO-2026-11-04-06") == ["2:" + longue[:120]]  # départ : coupée à 120


@pytest.mark.parametrize("quoi", ["relais", "configuration"])
def test_correction_7_numpy_autre_que_2_5_3_rien_ne_part(monde, tmp_path, quoi):
    r, env, nu = monde()
    faux = str(faux_python(tmp_path, "numpy-vieux", "3.13", numpy="2.4.6"))
    if quoi == "relais":
        r.python_relais = faux
    m = v4.MachineV4(r, env, python_configuration=faux) if quoi == "configuration" else v4.MachineV4(r, env)
    assert m.principal() == 0 and not (tmp_path / "courses-lancees").exists()
    j = journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)
    assert "numpy autre que 2.5.3 (correction 7)" in j and "2.4.6" in j


def test_correction_7_amorce_numpy(tmp_path):
    r, racine = amorce(tmp_path, A1V3_PYTHON_IMAGE=str(faux_python(tmp_path, "image-numpy-vieux", "3.13", numpy="2.4.6")))
    assert r.returncode == 2 and "numpy 2.4.6 sous" in r.stdout and not (racine / "exec-atteint.txt").exists()
    r2, racine2 = amorce(tmp_path / "bis" if (tmp_path / "bis").mkdir() is None else tmp_path)
    assert r2.returncode == 0 and "numpy 2.5.3 sous" in r2.stdout


def faux_python_pip(tmp_path, pip_code):
    """Interpréteur 3.13 sans numpy, dont `-m pip install` réussit (code 0, numpy apparaît) ou échoue."""
    d = tmp_path / f"faux-python-pip-{pip_code}"
    d.mkdir()
    p = d / "python3"
    marque = d / "numpy-installe"
    p.write_text(f'#!/bin/sh\ncase "$1" in --version) echo "Python 3.13.0 (jouet pip)";; '
                 f'-c) case "$2" in *numpy*) [ -e "{marque}" ] && echo 2.5.3 || exit 1;; *) echo 3.13;; esac;; '
                 f'-m) [ {pip_code} = 0 ] && : > "{marque}"; exit {pip_code};; *) exec {sys.executable} "$@";; esac\n')
    p.chmod(0o755)
    return p


@pytest.mark.parametrize("pip_code, code, motif", [(0, 0, "numpy 2.5.3 sous"), (1, 2, "installation de numpy==2.5.3 impossible")])
def test_correction_8_amorce_installe_numpy(tmp_path, pip_code, code, motif):
    py = faux_python_pip(tmp_path, pip_code)
    r, racine = amorce(tmp_path, SAUTER_INSTALLATION="0", A1V3_PYTHON_IMAGE=str(py), A1V3_PYTHON_CONFIGURATION=str(py))
    assert r.returncode == code and motif in r.stdout, r.stdout


@pytest.mark.parametrize("cas, motif", [
    ("texte", "texte v4 : empreinte"),
    ("lignee", "ne descend pas du code gelé"),
    ("piece", "pièce donnees/espece-seule-v1/collisionneur_v7.py"),
    ("statut", "arbre du dépôt public modifié : "),
    ("port", "déjà pris"),
    ("verifier", "--verifier-seulement en code 2"),
    ("relais", "relais : réglages inattendus"),
    ("ls-remote", "signe de vie non vérifié par ls-remote (C2)"),
])
def test_correction_8_artefacts_des_gardes_de_la_machine(monde, tmp_path, monkeypatch, cas, motif):
    r, env, nu = monde({"code": 0, "verifier": 2} if cas == "verifier" else None)
    if cas == "texte":
        env["SHA_TEXTE"] = "e" * 64
    elif cas == "lignee":
        r.commit_code_gele = "0" * 40
    elif cas == "piece":
        r.empreintes["donnees/espece-seule-v1/collisionneur_v7.py"] = "0" * 64
    elif cas == "statut":
        original = h.git
        monkeypatch.setattr(h, "git", lambda *a, **k: " M intrus\n" if a[:1] == ("status",) else original(*a, **k))
    elif cas == "relais":
        original_etat = h.etat_relais
        monkeypatch.setattr(h, "etat_relais", lambda port: (lambda e: dict(e, plafond_usd=1) if e else e)(original_etat(port)))
    elif cas == "ls-remote":
        original, vus = h.git, []

        def faux(*a, **k):
            if a[:1] == ("ls-remote",) and a[-1] == f"refs/heads/{v4.BRANCHE_VIE}":
                vus.append(1)
                if len(vus) > 1:  # après la poussée : ls-remote contredit le commit local
                    return "f" * 40 + f"\trefs/heads/{v4.BRANCHE_VIE}\n"
            return original(*a, **k)
        monkeypatch.setattr(h, "git", faux)
    if cas == "port":
        import socket
        with socket.socket() as s:
            s.bind(("127.0.0.1", r.port))
            s.listen()
            assert v4.MachineV4(r, env).principal() == 0
    else:
        assert v4.MachineV4(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    j = journal(t1.branche(nu, h.BRANCHE_REFUS), h.BRANCHE_REFUS)
    assert motif in j, j[-500:]
    assert gestes(r) == [["detruire", 90000001]]


def test_correction_8_client_delai_certificat_espace(tmp_path, monkeypatch):
    lent = tmp_path / "vastai-lent"
    lent.write_text("#!/bin/sh\nsleep 5\n")
    lent.chmod(0o755)
    monkeypatch.setattr(s10, "DELAI_VASTAI_S", 1)
    a = args_louer(tmp_path)
    assert v4.louer(a, v4.ClientPiloteV4(ENV_PILOTE, str(lent)), JOUR, dict(ENV_PILOTE), MAINTENANT) == 2
    j = Path(a.journal_local).read_text()
    assert "délai dépassé (1 s)" in j and Path(a.journal_local + ".creation-incertaine").exists() and JETON not in j
    t2 = tmp_path / "certificat"
    t2.mkdir()
    outil_, d = vastai_factice(t2, [("", "ssl.SSLCertVerificationError: CERTIFICATE_VERIFY_FAILED", 1)])
    a2 = args_louer(t2)
    assert v4.louer(a2, v4.ClientPiloteV4(ENV_PILOTE, outil_), JOUR, dict(ENV_PILOTE), MAINTENANT) == 2
    assert "certificat" in Path(a2.journal_local).read_text() and not Path(a2.journal_local + ".creation-incertaine").exists()
    t3 = tmp_path / "espace"
    t3.mkdir()
    outil3, d3 = vastai_factice(t3, [(CONTRAT, "", 0)])
    env3 = dict(ENV_PILOTE, CLE_ARGON="cle avec espace")
    a3 = args_louer(t3)
    assert v4.louer(a3, v4.ClientPiloteV4(env3, outil3), JOUR, env3, MAINTENANT) == 2 and appels(d3) == 0
    assert "espace ou guillemet" in Path(a3.journal_local).read_text()


def test_correction_8_cinq_no_such_ask_refus_final_sans_marqueur(tmp_path):
    offres = [dict(GPU, id=21 + k, dph_total=0.055 + k / 1000) for k in range(6)]
    code, a, d = louer(tmp_path, reponses=[("", NSA, 0)] * 6, offres=offres)
    assert code == 2 and appels(d) == 5 and (d / "offres").read_text().split() == ["21", "22", "23", "24", "25"]
    assert "5 essai(s), tous « no_such_ask »" in Path(a.journal_local).read_text()
    assert not Path(a.journal_local + ".creation-incertaine").exists()


def test_correction_8_controler_protegee_et_delai(tmp_path):
    a = etat_pilote(tmp_path)
    e = json.loads(Path(a.etat).read_text())
    e["identifiant"] = 58936099
    Path(a.etat).write_text(json.dumps(e))
    c = Inventaire([dict(INST, id=58936099)])
    assert v4.controler(a, c, lambda: False, heure(5, 9, 41), dict(ENV_PILOTE)) == 2 and c.gestes == []

    class Lent:
        def instances(self):
            raise subprocess.TimeoutExpired(["vastai", "show"], 300)
    assert v4.controler(etat_pilote(tmp_path / "x" if (tmp_path / "x").mkdir() is None else tmp_path), Lent(), lambda: False,
                        heure(5, 9, 41), dict(ENV_PILOTE)) == 6


def test_correction_8_minuterie_sans_curl_repli_python(tmp_path):
    d = tmp_path / "bin-sans-curl"
    d.mkdir()
    for o in ("bash", "sh", "date", "sleep", "grep", "head", "base64", "setsid", "git", "timeout", "tee", "cat", "python3"):
        cible = subprocess.run(["bash", "-c", f"command -v {o}"], capture_output=True, text=True).stdout.strip()
        if cible:
            (d / o).symlink_to(cible)
    racine = tmp_path / "racine"
    racine.mkdir()
    env = {"PATH": str(d), "HOME": str(tmp_path), "RACINE_A1V3": str(racine), "API_VAST": "https://127.0.0.1:9/api/v0",
           "A1V3_DUREE_S": "1", "A1V3_MARGE_S": "1", "A1V3_VIE_APRES_S": "1", "DEPOT_URL": f"file://{tmp_path}/absent.git",
           "GH_TOKEN": JETON, "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST, "GIT_CONFIG_GLOBAL": "/dev/null"}
    subprocess.run(["bash", "-c", v4.script_de_demarrage("b" * 40)], env=env, capture_output=True, timeout=180)
    fin = time.time() + 20
    log = racine / "a1v3-minuterie.log"
    while time.time() < fin and "DELETE" not in (log.read_text() if log.exists() else ""):
        time.sleep(0.2)
    texte = log.read_text()
    assert "ALARME : curl absent au départ de la minuterie : repli par python3" in texte and "DELETE instance 123 (essai 1)" in texte
    assert CLE_VAST not in texte


@pytest.mark.parametrize("version, tient", [("v4", True), ("v3", False)])
def test_correction_8_versement_mesure_sous_la_reserve(monde, monkeypatch, version, tient):
    """Pire cas mesuré : chaque appel de `git` du versement (et de la poussée, échouée à chaque essai) va jusqu'à son délai."""
    r, env, nu = monde()
    r.essais_poussee = v4.ESSAIS_POUSSEE
    original, delais, ls = h.git, [], []

    def lent(*a, **k):  # la poussée répond, puis `ls-remote` la contredit : chaque essai fait ses deux appels réseau
        delais.append(k.get("delai", 900))
        time.sleep(0.01)
        if a[:1] == ("ls-remote",):
            ls.append(1)
            if len(ls) > 1:
                return "f" * 40 + "\trefs/heads/x\n"
        return original(*a, **k)
    m = (v4.MachineV4 if version == "v4" else v3.MachineV3)(r, env)
    m.j = h.Journal(r.travail.parent / "journal-mesure.log", {})
    r.travail.mkdir()
    (r.travail / "a.txt").write_text("x")
    liste = m.sceller()
    monkeypatch.setattr(h, "git", lent)
    assert m.verser(h.BRANCHE_DONNEES, liste) is False
    pire = sum(delais) + (v4.ESSAIS_POUSSEE - 1) * v4.ATTENTE_POUSSEE_S + 2 * (60 + 60)  # arrêts de la course et du relais
    assert len(ls) == 1 + v4.ESSAIS_POUSSEE and delais.count(v4.DELAI_GIT_S) >= 2 * v4.ESSAIS_POUSSEE
    assert (pire <= v4.RESERVE_VERSEMENT_S) is tient, pire
