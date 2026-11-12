"""Essais R5 de `verifier_reception_r1_v4_v1.py` (fiche de réception v4 de R1) — v1.

Monde jouet (dossier temporaire de pytest, hors du dépôt de travail) : un dépôt git avec un commit « scellement »
(addendum, deux configurations, table v3, parent, code et scripts jouets, scellés), un commit « versement du témoin »
(seuls les quatre fichiers du témoin), une branche source `calcul/r1-v4-reparation-reel-v1` qui ajoute la réparation
(résultat, 3 épisodes consignés), la table v4, le rejeu (trois `.npz` jouets) et des traces d'instance porteuses de
sentinelles ; une branche de versement `calcul/r1-r2-reel-v1` dont le dernier commit ajoute exactement les fichiers
attendus ; un arbre de recalcul (commit du témoin versé plus les pièces versées) et la sortie jouet de
`chaine_table_v4_v1 --reception`. Les attendus jouets sont ceux du script, aux empreintes et comptes du monde jouet
(6 épisodes, T = 2, 3 cibles dont 2 retrouvées, 2 entrées v3), écrits dans une fiche jouet scellée.

Cas sain : « RÉCEPTION CONFORME », code 0. Puis un artefact par attente : code 2 et la garde nommée. Arrêts reçus :
code 3. Mode réel : le bloc d'une fiche doit égaler les attendus du script ; sur le dépôt de travail (si 5bd62a00 y
est), les textes scellés réels passent la garde `textes` (empreintes, compagnons, configurations canoniques, diff du
versement du témoin), et la suite s'arrête au versement (commit inexistant). Les clés interdites portent des
sentinelles qu'aucune sortie ne doit contenir. Variable `SCRIPT_RECEPTION_V4` : autre script à éprouver (banc)."""
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import numpy as np
import pytest

sys.dont_write_bytecode = True
ICI = Path(__file__).resolve().parent
SCRIPT = Path(os.environ.get("SCRIPT_RECEPTION_V4") or ICI / "verifier_reception_r1_v4_v1.py").resolve()
DEPOT_TRAVAIL = ICI.parents[3]
ENV = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_TERMINAL_PROMPT": "0",
       "GIT_AUTHOR_NAME": "essai", "GIT_AUTHOR_EMAIL": "essai@invalid", "GIT_COMMITTER_NAME": "essai",
       "GIT_COMMITTER_EMAIL": "essai@invalid", "PYTHONDONTWRITEBYTECODE": "1"}
os.environ.update({k: ENV[k] for k in ("GIT_CONFIG_NOSYSTEM", "GIT_CONFIG_GLOBAL", "GIT_TERMINAL_PROMPT")})
SENTINELLES = {"fideles": 713579246, "notees": 824680135, "part_fideles_parmi_notees": 0.86420975318642,
               "ecart_max": 0.0314159265358, "conformes_longueur": 935791357, "contextes_conformes": 146802468,
               "lecture_temoin": "sentinelle-lecture-temoin-5f3a", "lecture_rep": "sentinelle-lecture-rep-77b1",
               "traces": "sentinelle-traces-9c2e"}
T_RUN = "20261104-091009-r1-v4-temoin-reel"
R_RUN = "20261105-010000-r1-v4-reparation-reel"
J_RUN = "20261105-020000-r1-v4-rejeu-reel"


def module():
    spec = importlib.util.spec_from_file_location("verifier_reception_r1_v4_essai", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = module()


def git(d, *args):
    r = subprocess.run(["git", "-C", str(d), *args], capture_output=True, env=ENV)
    assert r.returncode == 0, f"git {args} : {r.stderr.decode()}"
    return r.stdout.decode("utf-8", "replace").strip()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def jb(x, indent=2):
    return (json.dumps(x, indent=indent, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def compagnon(chemin, b):
    return f"{sha(b)}  {Path(chemin).name}\n".encode()


def npz_octets(tableaux):
    f = io.BytesIO()
    np.savez_compressed(f, **tableaux)
    return f.getvalue()


def canon(c):
    return hashlib.sha256(json.dumps(c, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


class Monde:
    """Construit le monde jouet ; `h` : crochets {nom : fonction} qui altèrent un objet avant son écriture."""

    N_EP, T, LARGEUR = 6, 2, 4
    EPISODES = [f"ep{k}" for k in range(6)]
    CIBLES = ["ep2", "ep3", "ep4"]
    RETROUVEES = ["ep2", "ep4"]

    def __init__(self, base: Path, **h):
        self.base, self.h = base, h
        self.depot = base / "depot"
        self.depot.mkdir(parents=True)
        git(self.depot, "init", "-q", "--template=", "-b", "main")
        self.fichiers = {}

    def crochet(self, nom, x):
        f = self.h.get(nom)
        if f is not None:
            r = f(x)
            return r if r is not None and type(r) is type(x) else x
        return x

    def ecrire(self, chemin, b, sceau=True):
        p = self.depot / chemin
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
        self.fichiers[chemin] = b
        if sceau:
            c = self.crochet("compagnon:" + chemin, compagnon(chemin, b))
            (self.depot / (chemin + ".sha256")).write_bytes(c)
            self.fichiers[chemin + ".sha256"] = c

    def commit(self, message):
        git(self.depot, "add", "-A", "-f")
        git(self.depot, "commit", "-q", "-m", message)
        return git(self.depot, "rev-parse", "HEAD")

    # ------------------------------------------------------------ construction
    def construire(self):
        A = copy.deepcopy(M.ATTENDUS)
        A["jouet"] = True
        A["comptes"] = {"episodes": self.N_EP, "T": self.T, "actions": self.N_EP * self.T, "cibles": 3, "lots": 2,
                        "entrees_v3": 2, "identiques_base": 1, "seuil_non_conformes": 10}
        A["npz"]["largeur"] = self.LARGEUR
        # --- scellement
        pieces = {}
        addendum = b"# Addendum jouet v4\n"
        self.ecrire("prereg/R1-addendum-relance-v4.md", addendum)
        self.conf_r = {"mode": "jouet", "T": self.T, "voie_si_temoin_non_exact": "lot_fidele", "cibles_attendues": 3}
        self.conf_j = {"mode": "jouet", "chemin_table_tokenisation": A["table_v4"],
                       "table_tokenisation_sha256": "construite-en-session", "couches": [7, 15, 23]}
        self.table_v3 = {"version": 3, "T": self.T, "fiches_sha256": "f" * 64, "corrections_verifiees": 2,
                         "regle": "jouet", "episodes": [
                             {"episode": "ep0", "methode": "fins", "trajectoire_p3": "a0" * 32, "fins": {"0": 1},
                              "paires": []},
                             {"episode": "ep1", "methode": "une_paire", "trajectoire_p3": "a1" * 32, "fins": {},
                              "paires": [[1, 2]]}]}
        comptes3 = {m: 0 for m in M.METHODES_V3}
        comptes3.update(fins=1, une_paire=1, episodes=6, conformes_longueur=3, identiques_base=1, signales=2,
                        identiques_apres_table=3)
        self.table_v3["comptes"] = comptes3
        contenus = {
            "prereg/R1-reparation-v4-config-v2.json": jb(self.crochet("conf_r_fichier", self.conf_r), 1),
            "prereg/R1-rejeu-config-v6.json": jb(self.conf_j, 1),
            "prereg/R1-table-tokenisation-v3.json": jb(self.table_v3, 1),
            "prereg/R1-R2-rejeu-p3-v1.md": b"# parent jouet\n",
            "src/controle_ia/runs_nuit/chaine_table_v4_v1.py": b"# chaine jouet\n",
            "src/controle_ia/runs_nuit/rejeu_activations_v4.py": b"# rejeu jouet\n",
            "src/controle_ia/runs_nuit/resolution_graine_lot_v3.py": b"# lot v3 jouet\n",
            "src/controle_ia/runs_nuit/resolution_graine_lot_v2.py": b"# lot v2 jouet\n",
            "src/controle_ia/runs_nuit/resolution_graine_lot_v1.py": b"# lot v1 jouet\n",
            "src/controle_ia/runs_nuit/resolution_graine_v1.py": b"# graine v1 jouet\n",
            "src/controle_ia/manifeste.py": b"# manifeste jouet\n",
            "src/controle_ia/scellement.py": b"# scellement jouet\n",
            "scripts/r1_v4_instance_v2.sh": b"# script jouet\n",
            "scripts/amorce_instance_r1_v4_v2.sh": b"# amorce jouet\n",
        }
        for chemin, b in contenus.items():
            avec = chemin in A["pieces"] and A["pieces"][chemin]["compagnon"]
            self.ecrire(chemin, b, sceau=avec)
            pieces[chemin] = {"sha256": sha(b), "compagnon": avec}
        pieces["prereg/R1-addendum-relance-v4.md"] = {"sha256": sha(addendum), "compagnon": True}
        A["pieces"] = pieces
        A["preenregistrement"] = {"chemin": "prereg/R1-addendum-relance-v4.md", "sha256": sha(addendum)}
        A["config_reparation"]["sha256_canonique"] = canon(self.conf_r)
        A["config_rejeu"]["sha256_canonique"] = canon(self.conf_j)
        A["table_v3"]["sha256"] = sha(contenus["prereg/R1-table-tokenisation-v3.json"])
        self.crochet("apres_scellement", self)
        S = self.commit("scellement")
        # --- témoin
        mt = self.manifeste(T_RUN, A["commandes"]["temoin"], self.conf_r, S, "aucun-tirage-propre", A)
        mt = self.crochet("manifeste_temoin", mt)
        mtb = jb(mt)
        self.ecrire(f"runs/{T_RUN}/manifeste.json", mtb)
        rt = {"run_id": T_RUN, "manifeste_sha256": sha(mtb),
              "resultat": {"etape": "temoin", "version": "resolution_graine_lot_v3",
                           "lecture": SENTINELLES["lecture_temoin"], "voie_ecrite_d_avance": "lot_fidele"}}
        rt = self.crochet("resultat_temoin", rt)
        rtb = jb(rt)
        self.ecrire(f"diag/{T_RUN}/resolution-graine-lot-v3-temoin.json", rtb)
        self.crochet("avant_temoin_verse", self)
        TV = self.commit("versement du témoin")
        A["commits"] = {"scellement": S, "temoin_verse": TV}
        A["temoin"]["fichiers"] = {p: sha(self.fichiers[p]) for p in (
            f"diag/{T_RUN}/resolution-graine-lot-v3-temoin.json", f"diag/{T_RUN}/resolution-graine-lot-v3-temoin.json.sha256",
            f"runs/{T_RUN}/manifeste.json", f"runs/{T_RUN}/manifeste.json.sha256")}
        temoin = {"chemin": f"diag/{T_RUN}/resolution-graine-lot-v3-temoin.json", "sha256": sha(rtb), "voie": "lot_fidele",
                  "lecture": SENTINELLES["lecture_temoin"]}
        # --- branche source : réparation
        git(self.depot, "checkout", "-q", "-b", "calcul/r1-v4-reparation-reel-v1")
        mr = self.crochet("manifeste_reparation",
                          self.manifeste(R_RUN, A["commandes"]["reparation"], self.conf_r, TV, "aucun-tirage-propre", A))
        mrb = jb(mr)
        self.ecrire(f"runs/{R_RUN}/manifeste.json", mrb)
        consignes = []
        for k, e in enumerate(self.CIBLES):
            b = jb({"episode": e, "statut": "resolu" if e in self.RETROUVEES else "non_resolu"}, 1)
            self.ecrire(f"diag/{R_RUN}/episodes-reparation/{k:03d}.json", b)
            consignes.append({"episode": e, "statut": "x", "fichier": f"episodes-reparation/{k:03d}.json", "sha256": sha(b)})
        rep = {"run_id": R_RUN, "manifeste_sha256": sha(mrb), "resultat": {
            "etape": "reparation", "version": "resolution_graine_lot_v3", "voie": "lot_fidele",
            "run_source": A["run_source_p3"], "table_v3_sha256": A["table_v3"]["sha256"], "cibles": list(self.CIBLES),
            "lots_a_cible": [0, 1], "temoin": temoin, "lecture": SENTINELLES["lecture_rep"],
            "episodes": [{"episode": e, "empreinte_retrouvee": e in self.RETROUVEES, "ids": [[1, 2], [3]],
                          "statut": "resolu" if e in self.RETROUVEES else "non_resolu"} for e in self.CIBLES],
            "episodes_consignes": consignes, "lots_rapport": [{"independance_des_lignes": SENTINELLES["lecture_rep"]}]}}
        rep = self.crochet("resultat_reparation", rep)
        repb = jb(rep)
        self.ecrire(f"diag/{R_RUN}/resolution-graine-lot-v3-reparation.json", repb)
        self.commit("réparation")
        # --- table v4
        nouv = []
        for e in self.CIBLES:
            if e in self.RETROUVEES:
                nouv.append({"episode": e, "methode": "identifiants", "trajectoire_p3": "c" * 64, "fins": {}, "paires": [],
                             "actions": [{"pas": 0, "canonique": [9], "p3": [1, 2]}],
                             "resolution_graine": {"resultat_sha256": sha(repb), "voie": "lot_multi:directe"}})
            else:
                nouv.append({"episode": e, "methode": "non_resolu", "trajectoire_p3": "d" * 64, "fins": {}, "paires": [],
                             "cause_v4": "jouet"})
        episodes = self.table_v3["episodes"] + nouv
        comptes = {k: v for k, v in comptes3.items() if k not in M.METHODES_V3 and k != "identiques_apres_table"}
        for m in M.METHODES_V3:
            comptes[m] = sum(1 for x in episodes if x["methode"] == m)
        comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[m] for m in M.CORRIGEES_V3)
        comptes.update(non_conformes=3, cibles_v4=3, retrouvees_v4=len(self.RETROUVEES))
        meta = {k: v for k, v in self.table_v3.items() if k not in ("version", "comptes", "episodes")}
        table = {**meta, "version": 4, "regle_v4": "jouet", "table_v3_sha256": A["table_v3"]["sha256"],
                 "resultat_reparation_sha256": sha(repb), "voie": "lot_fidele", "temoin": temoin, "comptes": comptes,
                 "corrections_verifiees": comptes["identiques_apres_table"] - comptes["identiques_base"],
                 "non_resolus_v4": [x["episode"] for x in nouv if x["methode"] == "non_resolu"], "episodes": episodes}
        table = self.crochet("table", table)
        tb = self.crochet("table_octets", (json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode())
        self.ecrire(A["table_v4"], tb)
        B = self.commit("table v4")
        self.crochet("apres_table", self)
        Bc = git(self.depot, "rev-parse", "HEAD")
        # --- rejeu
        mj = self.crochet("manifeste_rejeu",
                          self.manifeste(J_RUN, A["commandes"]["rejeu"], self.conf_j, Bc, "fidelite", A))
        mjb = jb(mj)
        self.ecrire(f"runs/{J_RUN}/manifeste.json", mjb)
        n, d = self.N_EP * self.T, 3
        ident = self.identite()
        commun = {**ident, "jetons_empan": np.zeros(n, np.int64), "jetons_empan_rejeu": np.zeros(n, np.int64),
                  "couches": np.array([7, 15, 23], np.int64), "conforme_longueur": np.ones(n, bool),
                  "contexte_conforme": np.ones(n, bool), "ecart_fidelite": np.zeros(n), "fidele": np.ones(n, bool),
                  "trajectoire_identique": np.ones(n, bool), "activations_identiques": np.ones(n, bool)}
        fichiers = {}
        for nom, principal in A["npz"]["principaux"].items():
            tab = {principal: np.zeros((n, d, self.LARGEUR), np.float16), **commun}
            tab = self.crochet("npz:" + nom, tab)
            b = npz_octets(tab)
            self.ecrire(f"donnees/{J_RUN}/{nom}", b)
            fichiers[nom] = sha(b)
        par_t = {x["episode"]: x["methode"] for x in episodes}
        tok = {"addendum": A["addendum_tokenisation"], "version_table": 4, "table_sha256": sha(tb),
               "table_empreinte_citee": False, "non_conformes": 3, "signales": 2, "trajectoires_identiques_base": 1,
               "corrections_verifiees_au_chargement": table["corrections_verifiees"],
               "corrections_par_methode": {k: comptes[k] for k in M.CORRIGEES_V3},
               "par_methode_resolution": {"v1": 2, "v2": 0, "identifiants": 2, "aucune": 2},
               "methodes_resolution": {e: {"methode_table": par_t.get(e),
                                           "methode_resolution": M.methode_resolution(par_t.get(e))}
                                       for e in self.EPISODES},
               "episodes_non_resolus": [], "actions_non_resolues": 0, "fideles_parmi_non_resolues": 0,
               "seuil_non_conformes": 10, "episodes_non_retrouves_v4": ["ep3"], "actions_non_retrouvees_v4": 2,
               "part_fideles_parmi_notees": SENTINELLES["part_fideles_parmi_notees"],
               "p_r5_au_moins_90_pour_cent": False}
        rj = {"run_id": J_RUN, "manifeste_sha256": sha(mjb), "resultat": {
            "verdict_fidelite": "conforme", "fichiers": fichiers, "regle_repli_appliquee": False,
            "lecture": "principale", "empreintes_p3": {"episodes": 6, "trajectoires_identiques": comptes["identiques_apres_table"],
                                                        "activations_identiques_au_bit": 5},
            "fidelite_toutes": {"actions": n, "notees": SENTINELLES["notees"], "fideles": SENTINELLES["fideles"],
                                "conformes_longueur": SENTINELLES["conformes_longueur"],
                                "contextes_conformes": SENTINELLES["contextes_conformes"],
                                "ecart_max": SENTINELLES["ecart_max"]},
            "fidelite_echantillon": {"lecture": "conforme", "ecarts": [SENTINELLES["ecart_max"]]},
            "controle_negatif": {"lecture": "discriminant"}, "tokenisation": tok}}
        rj = self.crochet("resultat_rejeu", rj)
        if self.h.get("arret_rejeu"):
            arret = {"run_id": J_RUN, "manifeste_sha256": sha(mjb), "resultat": {
                "etape": "rejeu", "motif": "jouet", "verdict_fidelite": self.h["arret_rejeu"],
                "partiel": {"fidelite_echantillon": {"ecarts": [SENTINELLES["ecart_max"]]}}}}
            for nom in A["npz"]["principaux"]:
                (self.depot / "donnees" / J_RUN / nom).unlink()
                (self.depot / "donnees" / J_RUN / (nom + ".sha256")).unlink()
                del self.fichiers[f"donnees/{J_RUN}/{nom}"], self.fichiers[f"donnees/{J_RUN}/{nom}.sha256"]
            self.ecrire(f"diag/{J_RUN}/arret.json", jb(arret))
        else:
            self.ecrire(f"diag/{J_RUN}/rejeu-activations.json", jb(rj))
        self.commit("rejeu")
        self.ecrire(f"traces/r1-v4-reparation-x/r1-rejeu.json",
                    json.dumps({"fidelite": SENTINELLES["traces"]}).encode(), sceau=False)
        self.commit("traces")
        self.crochet("source_finale", self)
        # --- scores de P3 (hors du versement)
        scores = self.base / "scores-p3.npz"
        scores.write_bytes(npz_octets({**self.crochet("scores_identite", self.identite()),
                                       "scores": np.zeros((n, 2)), "jetons": np.zeros(n, np.int64)}))
        A["scores_p3"]["sha256"] = sha(scores.read_bytes())
        # --- versement
        verses = {p: b for p, b in self.fichiers.items()
                  if p.startswith((f"runs/{T_RUN}", f"diag/{T_RUN}", f"runs/{R_RUN}", f"diag/{R_RUN}", f"runs/{J_RUN}",
                                   f"diag/{J_RUN}", f"donnees/{J_RUN}", A["table_v4"]))}
        verses = self.crochet("verses", verses)
        git(self.depot, "checkout", "-q", "--orphan", "calcul/r1-r2-reel-v1")
        git(self.depot, "rm", "-q", "-rf", "--cached", ".")
        for x in list(self.depot.iterdir()):
            if x.name != ".git":
                shutil.rmtree(x) if x.is_dir() else x.unlink()
        (self.depot / "LISEZMOI").write_bytes(b"branche de versement jouet\n")
        self.commit("tête précédente")
        self.crochet("avant_versement", self)
        for p, b in verses.items():
            q = self.depot / p
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_bytes(b)
        V = self.commit("versement à l'octet")
        self.crochet("apres_versement", self)
        # --- recalcul
        rec = self.base / "recalcul"
        git(self.depot, "worktree", "add", "-q", "--detach", str(rec), TV)
        for p in (f"diag/{R_RUN}/resolution-graine-lot-v3-reparation.json", f"runs/{R_RUN}/manifeste.json", A["table_v4"]):
            if (self.depot / p).is_file():
                (rec / p).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(self.depot / p, rec / p)
        self.crochet("recalcul_arbre", rec)
        sortie = {"version": "chaine_table_v4_v1", "table": A["table_v4"], "table_sha256": sha(tb),
                  "reparation": f"diag/{R_RUN}/resolution-graine-lot-v3-reparation.json",
                  "resultat_reparation_sha256": sha(repb), "run_reparation": R_RUN,
                  "table_v3_sha256": A["table_v3"]["sha256"], "cibles": 3, "retrouvees": 2, "non_retrouvees": 1,
                  "entrees_v3": 2, "recalcul_egal_a_l_octet": True}
        sortie = self.crochet("sortie_recalcul", sortie)
        sr = self.base / "recalcul-sortie.json"
        sr.write_text(json.dumps(sortie, sort_keys=True) + "\n", encoding="utf-8")
        # --- fiche jouet scellée
        A = self.crochet("attendus", A)
        fiche = self.base / "fiche-jouet.md"
        fb = (f"# Fiche jouet\n\n{M.DEBUT_BLOC}\n```json\n{M.bloc(A)}\n```\n{M.FIN_BLOC}\n").encode()
        fiche.write_bytes(fb)
        (self.base / "fiche-jouet.md.sha256").write_bytes(self.crochet("fiche_sceau", compagnon(fiche, fb)))
        self.A = A
        return ["verifier", "--fiche", str(fiche), "--depot", str(self.depot), "--racine", str(self.depot),
                "--commit-versement", V, "--source", "refs/heads/calcul/r1-v4-reparation-reel-v1",
                "--run-reparation", R_RUN, "--run-rejeu", J_RUN, "--scores-p3", str(scores),
                "--sortie-recalcul", str(sr), "--racine-recalcul", str(rec), "--jouet"]

    def identite(self):
        n = self.N_EP * self.T
        return {"episode": np.array([f"ep{i // self.T}" for i in range(n)]), "pas": np.arange(n, dtype=np.int64) % self.T,
                "condition": np.array(["honnete"] * n), "tache": np.array(["t01"] * n)}

    @staticmethod
    def manifeste(run, commande, config, commit, tache, A):
        return {"run_id": run, "cree_le": "2026-11-05T00:00:00+00:00", "commit": commit, "depot_propre": True,
                "decisif": True, "preenregistrement": dict(A["preenregistrement"]), "config": config,
                "config_sha256": canon(config), "versions": {"python": "3.11"},
                "graines": {tache: {"entropie": A["entropie"], "spawn_key": ["1"], "etat_controle": [1, 2]}},
                "commande": commande, "reserves": []}


def lancer(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = M.main(argv)
    sortie = out.getvalue() + err.getvalue()
    for v in SENTINELLES.values():
        assert str(v) not in sortie, f"sentinelle {v} dans la sortie"
    return code, sortie


def monde(tmp_path, **h):
    return Monde(tmp_path, **h).construire()


def arret(tmp_path, garde, **h):
    code, sortie = lancer(monde(tmp_path, **h))
    assert code == 2, sortie
    assert f"ARRÊT [{garde}]" in sortie, sortie
    return sortie


# ------------------------------------------------------------------ cas sains
def test_cas_sain(tmp_path):
    code, sortie = lancer(monde(tmp_path))
    assert code == 0, sortie
    assert sortie.startswith("RÉCEPTION CONFORME")
    for g in ("fiche", "runs", "textes", "versement", "octets", "presence", "compagnon", "temoin", "reparation", "table",
              "chaine-locale", "rejeu", "commit-rejeu", "rattachement", "verdict", "table-comparee", "provenance",
              "comptes", "coherence-table", "fichiers", "npz", "recalcul"):
        assert g in sortie, g


def test_source_nommee_par_origin(tmp_path):
    argv = monde(tmp_path, apres_versement=lambda w: git(w.depot, "update-ref",
                                                          "refs/remotes/origin/calcul/r1-v4-reparation-reel-v1",
                                                          "refs/heads/calcul/r1-v4-reparation-reel-v1"))
    argv[argv.index("--source") + 1] = "refs/remotes/origin/calcul/r1-v4-reparation-reel-v1"
    assert lancer(argv)[0] == 0


def test_filtre_ne_garde_que_les_chemins_nommes():
    doc = {"run_id": "r", "resultat": {"verdict_fidelite": "conforme", "lecture": "x",
                                      "tokenisation": {"addendum": "a", "part_fideles_parmi_notees": 0.5}}}
    g = M.filtrer(doc, M.CHEMINS_LUS_REJEU)
    assert g == {"run_id": "r", "resultat": {"verdict_fidelite": "conforme", "tokenisation": {"addendum": "a"}}}
    assert not set(M.INTERDITS) & {k for ch in M.CHEMINS_LUS_REJEU for k in ch}


# ------------------------------------------------------------------ fiche
def test_fiche_non_scellee(tmp_path):
    argv = monde(tmp_path)
    Path(argv[2] + ".sha256").unlink()
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [fiche]" in sortie


def test_fiche_sceau_faux(tmp_path):
    arret(tmp_path, "fiche", fiche_sceau=lambda b: b"0" * 64 + b"  fiche-jouet.md\n")


def test_fiche_empreinte_annoncee_differente(tmp_path):
    argv = monde(tmp_path) + ["--fiche-sha256", "e" * 64]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [fiche]" in sortie


def test_fiche_jouet_en_mode_reel(tmp_path):
    argv = [x for x in monde(tmp_path) if x != "--jouet"]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [fiche]" in sortie


def test_fiche_marquee_reelle_en_mode_jouet(tmp_path):
    arret(tmp_path, "fiche", attendus=lambda A: A.update(jouet=False))


def test_fiche_reelle_au_bloc_altere(tmp_path):
    A = copy.deepcopy(M.ATTENDUS)
    A["comptes"]["cibles"] = 88
    f = tmp_path / "fiche.md"
    f.write_text(f"{M.DEBUT_BLOC}\n```json\n{M.bloc(A)}\n```\n{M.FIN_BLOC}\n", encoding="utf-8")
    Path(str(f) + ".sha256").write_bytes(compagnon(f, f.read_bytes()))
    code, sortie = lancer(["verifier", "--fiche", str(f), "--depot", str(tmp_path), "--racine", str(tmp_path),
                           "--commit-versement", "0" * 40, "--source", "x", "--run-reparation", R_RUN])
    assert code == 2 and "ARRÊT [fiche]" in sortie and "≠ attendus du script" in sortie


@pytest.mark.skipif(subprocess.run(["git", "-C", str(DEPOT_TRAVAIL), "cat-file", "-e",
                                    "5bd62a004279776c2718b3201c11001e16fa6527^{commit}"],
                                   capture_output=True).returncode != 0, reason="commit 5bd62a00 absent du dépôt")
def test_mode_reel_textes_scelles_reels(tmp_path):
    """Fiche réelle (bloc = attendus du script) sur le dépôt de travail : la garde `textes` passe sur les vraies pièces,
    puis la réception s'arrête au versement (commit inexistant)."""
    f = tmp_path / "fiche.md"
    f.write_text(f"{M.DEBUT_BLOC}\n```json\n{M.bloc()}\n```\n{M.FIN_BLOC}\n", encoding="utf-8")
    Path(str(f) + ".sha256").write_bytes(compagnon(f, f.read_bytes()))
    code, sortie = lancer(["verifier", "--fiche", str(f), "--depot", str(DEPOT_TRAVAIL), "--racine", str(tmp_path),
                           "--commit-versement", "0" * 40, "--source", "calcul/r1-v4-reparation-reel-v1",
                           "--run-reparation", R_RUN, "--run-rejeu", J_RUN])
    assert code == 2 and "ARRÊT [versement]" in sortie, sortie


def test_bloc_de_la_fiche_reelle_egal_au_script():
    fiche = ICI / "fiche-reception-r1-v4-v1.md"
    if not fiche.is_file():
        pytest.skip("fiche pas encore écrite")
    assert M.lire_bloc(fiche.read_text(encoding="utf-8")) == M.ATTENDUS


# ------------------------------------------------------------------ runs, textes
def test_nom_de_run_hors_forme(tmp_path):
    argv = monde(tmp_path)
    argv[argv.index("--run-rejeu") + 1] = "20261105-020000-r1-rejeu-reel"
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [runs]" in sortie


def test_piece_scellee_alteree(tmp_path):
    arret(tmp_path, "textes", attendus=lambda A: A["pieces"]["prereg/R1-R2-rejeu-p3-v1.md"].update(sha256="1" * 64))


def test_compagnon_de_piece_faux(tmp_path):
    arret(tmp_path, "textes", **{"compagnon:prereg/R1-rejeu-config-v6.json": lambda b: b"2" * 64 + b"  R1-rejeu-config-v6.json\n"})


def test_configuration_canonique_autre(tmp_path):
    arret(tmp_path, "textes", attendus=lambda A: A["config_rejeu"].update(sha256_canonique="3" * 64))


def test_versement_du_temoin_porte_autre_chose(tmp_path):
    arret(tmp_path, "textes", avant_temoin_verse=lambda w: w.ecrire("docs/autre.md", b"x\n"))


def test_table_v4_au_commit_du_temoin(tmp_path):
    arret(tmp_path, "textes", apres_scellement=lambda w: w.ecrire("prereg/R1-table-tokenisation-v4.json", b"{}\n"))


# ------------------------------------------------------------------ versement, octets, présence, compagnons
def test_versement_en_trop(tmp_path):
    arret(tmp_path, "versement", verses=lambda v: v.update({f"diag/{J_RUN}/autre.json": b"{}\n"}))


def test_versement_en_moins(tmp_path):
    arret(tmp_path, "versement", verses=lambda v: v.pop(f"diag/{R_RUN}/episodes-reparation/001.json.sha256"))


def test_versement_porte_les_traces(tmp_path):
    arret(tmp_path, "versement", verses=lambda v: v.update({"traces/x/r1-rejeu.json": b"{}\n"}))


def test_versement_modifie_un_existant(tmp_path):
    def f(w):
        (w.depot / "LISEZMOI").write_bytes(b"modifie\n")
    arret(tmp_path, "versement", avant_versement=f)


def test_versement_fusion(tmp_path):
    def f(w):
        git(w.depot, "checkout", "-q", "-b", "autre", "HEAD~1")
        (w.depot / "AUTRE").write_bytes(b"x\n")
        git(w.depot, "add", "AUTRE")
        git(w.depot, "commit", "-q", "-m", "autre")
        git(w.depot, "checkout", "-q", "calcul/r1-r2-reel-v1")
        git(w.depot, "merge", "-q", "--no-edit", "--no-ff", "autre")
    argv = monde(tmp_path, apres_versement=f)
    argv[argv.index("--commit-versement") + 1] = git(Path(argv[argv.index("--depot") + 1]), "rev-parse", "HEAD")
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [versement]" in sortie


def test_commit_de_versement_absent(tmp_path):
    argv = monde(tmp_path)
    argv[argv.index("--commit-versement") + 1] = "a" * 40
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [versement]" in sortie


def test_verse_different_de_la_source(tmp_path):
    p = f"diag/{R_RUN}/episodes-reparation/000.json"
    arret(tmp_path, "octets", verses=lambda v: v.update({p: v[p] + b" "}))


def test_temoin_verse_different_de_5bd62a00(tmp_path):
    p = f"runs/{T_RUN}/manifeste.json"
    arret(tmp_path, "octets", verses=lambda v: v.update({p: v[p] + b" "}))


def test_arbre_recu_different_du_commit(tmp_path):
    def f(w):
        q = w.depot / f"diag/{R_RUN}/episodes-reparation/002.json"
        q.write_bytes(q.read_bytes() + b" ")
    arret(tmp_path, "octets", apres_versement=f)


def test_branche_source_non_attendue(tmp_path):
    """Même contenu que la source, autre nom de branche."""
    argv = monde(tmp_path, apres_versement=lambda w: git(w.depot, "branch", "calcul/autre",
                                                          "calcul/r1-v4-reparation-reel-v1"))
    argv[argv.index("--source") + 1] = "refs/heads/calcul/autre"
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [octets]" in sortie


def test_empreinte_du_temoin_autre(tmp_path):
    arret(tmp_path, "octets", attendus=lambda A: A["temoin"]["fichiers"].update(
        {f"runs/{T_RUN}/manifeste.json": "4" * 64}))


def test_fichier_en_trop_dans_un_run_recu(tmp_path):
    def f(w):
        (w.depot / f"diag/{J_RUN}/en-trop.json").write_bytes(b"{}\n")
    arret(tmp_path, "presence", apres_versement=f)


def test_compagnon_faux_verse(tmp_path):
    arret(tmp_path, "compagnon", **{f"compagnon:diag/{R_RUN}/episodes-reparation/001.json":
                                    lambda b: b"5" * 64 + b"  001.json\n"})


# ------------------------------------------------------------------ témoin
def test_temoin_commit_autre(tmp_path):
    arret(tmp_path, "temoin", manifeste_temoin=lambda m: m.update(commit="6" * 40))


def test_temoin_commande_autre(tmp_path):
    arret(tmp_path, "temoin", manifeste_temoin=lambda m: m.update(commande="python -m x --etape temoin"))


def test_temoin_resultat_autre_etape(tmp_path):
    arret(tmp_path, "temoin", resultat_temoin=lambda r: r["resultat"].update(etape="reparation"))


def test_temoin_non_rattache(tmp_path):
    arret(tmp_path, "temoin", resultat_temoin=lambda r: r.update(manifeste_sha256="7" * 64))


# ------------------------------------------------------------------ réparation
def test_reparation_texte_autre(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m.update(
        preenregistrement={"chemin": "prereg/R1-addendum-relance-v3.md", "sha256": "8" * 64}))


def test_reparation_commit_autre(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m.update(commit="9" * 40))


def test_reparation_configuration_autre(tmp_path):
    def f(m):
        m["config"] = {**m["config"], "voie_si_temoin_non_exact": "passe_forcee"}
        m["config_sha256"] = canon(m["config"])
    arret(tmp_path, "reparation", manifeste_reparation=f)


def test_reparation_depot_sale(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m.update(
        depot_propre=False, reserves=["arbre de travail non propre"]))


def test_reparation_entropie_autre(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m["graines"]["aucun-tirage-propre"].update(entropie="1"))


def test_reparation_non_decisive(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m.update(decisif=False))


def test_reparation_voie_passe_forcee(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"].update(voie="passe_forcee"))


def test_reparation_cite_un_autre_temoin(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"]["temoin"].update(sha256="a" * 64))


def test_reparation_cibles_autres(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"].update(lots_a_cible=[0]))


def test_reparation_episodes_desordonnes(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"]["episodes"].reverse())


def test_reparation_consigne_empreinte_fausse(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"]["episodes_consignes"][1].update(sha256="b" * 64))


def test_reparation_table_v3_autre(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"].update(table_v3_sha256="c" * 64))


# ------------------------------------------------------------------ table v4
def test_table_serialisation_autre(tmp_path):
    arret(tmp_path, "table", table_octets=lambda b: json.dumps(json.loads(b), sort_keys=True, indent=2).encode() + b"\n")


def test_table_version_3(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(version=3))


def test_table_cite_une_autre_reparation(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(resultat_reparation_sha256="d" * 64))


def test_table_entree_v3_alteree(tmp_path):
    arret(tmp_path, "table", table=lambda t: t["episodes"][0].update(trajectoire_p3="e" * 64))


def test_table_cle_en_trop(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(autre=1))


def test_table_metadonnee_v3_alteree(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(fiches_sha256="0" * 64))


def test_table_non_resolus_v4_faux(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(non_resolus_v4=[]))


def test_table_comptes_faux(tmp_path):
    arret(tmp_path, "table", table=lambda t: t["comptes"].update(retrouvees_v4=3))


def test_table_retrouvee_retrogradee(tmp_path):
    """Artefact de V4-E5 : une retrouvée rétrogradée en `non_resolu`, table cohérente avec elle-même."""
    def f(t):
        e = t["episodes"][-1]
        e.clear()
        e.update(episode="ep4", methode="non_resolu", trajectoire_p3="c" * 64, fins={}, paires=[], cause_v4="x")
        t["non_resolus_v4"] = ["ep3", "ep4"]
        t["comptes"].update(identifiants=1, non_resolu=2, identiques_apres_table=4, retrouvees_v4=1)
        t["corrections_verifiees"] = 3
    arret(tmp_path, "chaine-locale", table=f)


def test_table_identifiants_sans_le_sceau(tmp_path):
    arret(tmp_path, "chaine-locale", table=lambda t: t["episodes"][2]["resolution_graine"].update(resultat_sha256="f" * 64))


# ------------------------------------------------------------------ rejeu
def test_rejeu_commande_v3(tmp_path):
    arret(tmp_path, "rejeu", manifeste_rejeu=lambda m: m.update(commande="python -m controle_ia.runs_nuit.rejeu_activations_v3"))


def test_rejeu_table_citee_d_avance(tmp_path):
    def f(m):
        m["config"] = {**m["config"], "table_tokenisation_sha256": "1" * 64}
        m["config_sha256"] = canon(m["config"])
    arret(tmp_path, "rejeu", manifeste_rejeu=f)


def test_rejeu_commit_hors_branche(tmp_path):
    arret(tmp_path, "commit-rejeu", manifeste_rejeu=lambda m: m.update(commit="2" * 40))


def test_rejeu_commit_au_temoin(tmp_path):
    """Commit lancé = 5bd62a00 jouet : la table v4 n'y est pas (diff ≠ réparation et table)."""
    def g(w):
        w.h["manifeste_rejeu"] = lambda m: m.update(commit=git(w.depot, "rev-parse", "HEAD~2"))
    arret(tmp_path, "commit-rejeu", apres_table=g)


def test_rejeu_non_rattache(tmp_path):
    arret(tmp_path, "rattachement", resultat_rejeu=lambda r: r.update(manifeste_sha256="3" * 64))


def test_rejeu_verdict_non_conforme(tmp_path):
    arret(tmp_path, "verdict", resultat_rejeu=lambda r: r["resultat"].update(verdict_fidelite="non conforme"))


def test_rejeu_table_comparee(tmp_path):
    arret(tmp_path, "table-comparee", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(table_sha256="4" * 64))


def test_rejeu_provenance_v3(tmp_path):
    arret(tmp_path, "provenance", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(
        addendum="prereg/R1-addendum-relance-v2.md"))


def test_rejeu_version_table(tmp_path):
    arret(tmp_path, "comptes", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(version_table=3))


def test_rejeu_empreinte_dite_citee(tmp_path):
    arret(tmp_path, "comptes", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(table_empreinte_citee=True))


def test_rejeu_non_conformes_autre(tmp_path):
    arret(tmp_path, "comptes", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(non_conformes=88))


def test_rejeu_actions_autres(tmp_path):
    arret(tmp_path, "comptes", resultat_rejeu=lambda r: r["resultat"]["fidelite_toutes"].update(actions=11))


def test_rejeu_regle_b(tmp_path):
    arret(tmp_path, "comptes", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(episodes_non_resolus=["ep1"]))


def test_rejeu_corrections_verifiees_autres(tmp_path):
    arret(tmp_path, "coherence-table", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(
        corrections_verifiees_au_chargement=3))


def test_rejeu_corrections_par_methode_autres(tmp_path):
    arret(tmp_path, "coherence-table", resultat_rejeu=lambda r: r["resultat"]["tokenisation"]["corrections_par_methode"].update(
        identifiants=1))


def test_rejeu_par_methode_resolution_autre(tmp_path):
    arret(tmp_path, "coherence-table", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(
        par_methode_resolution={"v1": 2, "v2": 0, "identifiants": 1, "aucune": 3}))


def test_rejeu_methodes_resolution_autres(tmp_path):
    arret(tmp_path, "coherence-table", resultat_rejeu=lambda r: r["resultat"]["tokenisation"]["methodes_resolution"][
        "ep4"].update(methode_table="non_resolu", methode_resolution="aucune"))


def test_rejeu_non_retrouves_autres(tmp_path):
    arret(tmp_path, "coherence-table", resultat_rejeu=lambda r: r["resultat"]["tokenisation"].update(
        episodes_non_retrouves_v4=[]))


def test_rejeu_fichiers_faux(tmp_path):
    arret(tmp_path, "fichiers", resultat_rejeu=lambda r: r["resultat"]["fichiers"].update(
        {"activations-p3-rejeu-v1.npz": "5" * 64}))


# ------------------------------------------------------------------ npz
def test_npz_tableau_en_trop(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1.npz": lambda t: t.update(autre=np.zeros(3))})


def test_npz_tableau_manquant(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1-maximum.npz": lambda t: t.pop("fidele")})


def test_npz_principal_en_float32(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1-maximum.npz":
                              lambda t: t.update(maximum=t["maximum"].astype(np.float32))})


def test_npz_principal_hors_forme(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1-complement-hors-cout.npz":
                              lambda t: t.update(maximum_hors_cout=np.zeros((12, 3, 5), np.float16))})


def test_npz_type_d_un_commun(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1.npz": lambda t: t.update(fidele=t["fidele"].astype(np.int8))})


def test_npz_identite_autre_type(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1.npz": lambda t: t.update(pas=t["pas"].astype(np.int32))})


def test_scores_p3_autre_empreinte(tmp_path):
    arret(tmp_path, "npz", attendus=lambda A: A["scores_p3"].update(sha256="6" * 64))


def test_scores_p3_absent(tmp_path):
    argv = monde(tmp_path)
    i = argv.index("--scores-p3")
    del argv[i:i + 2]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [npz]" in sortie


# ------------------------------------------------------------------ recalcul
def test_recalcul_absent(tmp_path):
    argv = monde(tmp_path)
    i = argv.index("--sortie-recalcul")
    del argv[i:i + 2]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [recalcul]" in sortie


def test_recalcul_inegal_a_l_octet(tmp_path):
    arret(tmp_path, "recalcul", sortie_recalcul=lambda s: s.update(recalcul_egal_a_l_octet=False))


def test_recalcul_sur_autres_pieces(tmp_path):
    arret(tmp_path, "recalcul", sortie_recalcul=lambda s: s.update(table_sha256="7" * 64))


def test_recalcul_comptes_autres(tmp_path):
    arret(tmp_path, "recalcul", sortie_recalcul=lambda s: s.update(retrouvees=3, non_retrouvees=0))


def test_recalcul_arbre_src_autre(tmp_path):
    def f(rec):
        q = rec / "src/controle_ia/runs_nuit/chaine_table_v4_v1.py"
        q.write_bytes(q.read_bytes() + b"# modifie\n")
    arret(tmp_path, "recalcul", recalcul_arbre=f)


def test_recalcul_arbre_table_autre(tmp_path):
    def f(rec):
        q = rec / "prereg/R1-table-tokenisation-v4.json"
        q.write_bytes(q.read_bytes() + b"\n")
    arret(tmp_path, "recalcul", recalcul_arbre=f)


def test_recalcul_arbre_absent(tmp_path):
    argv = monde(tmp_path)
    i = argv.index("--racine-recalcul")
    del argv[i:i + 2]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [recalcul]" in sortie


# ------------------------------------------------------------------ arrêts reçus
def test_rejeu_arrete_non_conforme(tmp_path):
    code, sortie = lancer(monde(tmp_path, arret_rejeu="non conforme"))
    assert code == 3 and sortie.startswith("COURSE ARRÊTÉE") and "non conforme" in sortie


def test_rejeu_arrete_motif_hors_liste(tmp_path):
    code, sortie = lancer(monde(tmp_path, arret_rejeu="autre"))
    assert code == 2 and "ARRÊT [arret-rejeu]" in sortie


def test_rejeu_absent(tmp_path):
    argv = monde(tmp_path, verses=lambda v: [v.pop(k) for k in list(v) if J_RUN in k])
    i = argv.index("--run-rejeu")
    del argv[i:i + 2]
    code, sortie = lancer(argv)
    assert code == 3 and "rejeu absent" in sortie


def test_reparation_arretee(tmp_path):
    def f(w):
        m = w.fichiers[f"runs/{R_RUN}/manifeste.json"]
        w.ecrire(f"diag/{R_RUN}/arret.json", jb({"run_id": R_RUN, "manifeste_sha256": sha(m),
                                                  "resultat": {"etape": "reparation", "motif": "jouet",
                                                               "partiel": {"x": SENTINELLES["lecture_rep"]}}}))
        w.commit("arrêt jouet")
    argv = monde(tmp_path, source_finale=f, verses=lambda v: [v.pop(k) for k in list(v)
                                                               if J_RUN in k or "tokenisation-v4" in k])
    code, sortie = lancer(argv)
    assert code == 3 and "réparation" in sortie and "arrêtée" in sortie, sortie


def test_rejeu_commit_au_scellement(tmp_path):
    def g(w):
        w.h["manifeste_rejeu"] = lambda m: m.update(commit=git(w.depot, "rev-parse", "HEAD~3"))
    arret(tmp_path, "commit-rejeu", apres_table=g)


def test_rejeu_lance_sur_une_autre_table(tmp_path):
    """La table versée (tête de la source) n'est pas celle du commit lancé du rejeu."""
    def f(w):
        p = "prereg/R1-table-tokenisation-v4.json"
        t = json.loads(w.fichiers[p])
        t["regle_v4"] = "jouet, réécrite après le rejeu"
        w.ecrire(p, (json.dumps(t, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode())
        w.commit("table réécrite")
    sortie = arret(tmp_path, "commit-rejeu", source_finale=f)
    assert "à l'octet" in sortie


def test_fiche_format_autre(tmp_path):
    arret(tmp_path, "fiche", attendus=lambda A: A.update(format="attendus-reception-r1-relance-v3-v1"))


def test_commit_du_temoin_absent(tmp_path):
    arret(tmp_path, "textes", attendus=lambda A: A["commits"].update(temoin_verse="f" * 40))


def test_scellement_non_parent_du_temoin(tmp_path):
    """Commit de même arbre que le scellement, mais qui n'est pas le parent du versement du témoin."""
    boite = {}
    def f(w):
        boite["s2"] = git(w.depot, "commit-tree", "main~1^{tree}", "-m", "autre scellement")
    arret(tmp_path, "textes", source_finale=f, attendus=lambda A: A["commits"].update(scellement=boite["s2"]))


def test_piece_alteree_compagnon_complice(tmp_path):
    p = "prereg/R1-R2-rejeu-p3-v1.md"
    arret(tmp_path, "textes", attendus=lambda A: A["pieces"][p].update(sha256="1" * 64),
          **{"compagnon:" + p: lambda b: b"1" * 64 + b"  R1-R2-rejeu-p3-v1.md\n"})


def test_versement_commit_a_deux_parents_meme_arbre(tmp_path):
    def f(w):
        v = git(w.depot, "rev-parse", "HEAD")
        m = git(w.depot, "commit-tree", v + "^{tree}", "-p", v + "~1", "-p", "main", "-m", "fusion")
        boite["m"] = m
    boite = {}
    argv = monde(tmp_path, apres_versement=f)
    argv[argv.index("--commit-versement") + 1] = boite["m"]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [versement]" in sortie and "parents" in sortie, sortie


def test_versement_modifie_un_chemin_attendu(tmp_path):
    def f(w):
        q = w.depot / f"diag/{R_RUN}/episodes-reparation/000.json"
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(b"ancien\n")
        w.commit("tête précédente bis")
    sortie = arret(tmp_path, "versement", avant_versement=f)
    assert "réécriture" in sortie


def test_course_arretee_versement_hors_des_runs(tmp_path):
    arret(tmp_path, "versement", arret_rejeu="non conforme",
          verses=lambda v: v.update({f"diag/{J_RUN}/autre.json": b"{}\n"}))


def test_reparation_autre_version(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"].update(version="resolution_graine_lot_v2"))


def test_reparation_consigne_mal_nommee(tmp_path):
    arret(tmp_path, "reparation", resultat_reparation=lambda r: r["resultat"]["episodes_consignes"][0].update(
        fichier="episodes-reparation/0.json"))


def test_rejeu_absent_sans_resultat_de_reparation(tmp_path):
    argv = monde(tmp_path, verses=lambda v: [v.pop(k) for k in list(v) if J_RUN in k or "lot-v3-reparation.json" in k])
    i = argv.index("--run-rejeu")
    del argv[i:i + 2]
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [reparation]" in sortie, sortie


def test_table_sur_une_autre_table_v3(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(table_v3_sha256="1" * 64))


def test_table_cite_un_autre_temoin(tmp_path):
    arret(tmp_path, "table", table=lambda t: t["temoin"].update(sha256="2" * 64))


def test_table_entrees_neuves_desordonnees(tmp_path):
    def f(t):
        t["episodes"][-1], t["episodes"][-3] = t["episodes"][-3], t["episodes"][-1]
    arret(tmp_path, "table", table=f)


def test_table_entree_neuve_d_autre_methode(tmp_path):
    def f(t):
        e = t["episodes"][-2]
        e["methode"] = "copie"
        t["non_resolus_v4"] = []
        t["comptes"].update(non_resolu=0, copie=1, identiques_apres_table=t["comptes"]["identiques_apres_table"] + 1)
        t["corrections_verifiees"] += 1
    arret(tmp_path, "table", table=f)


def test_table_corrections_verifiees_fausses(tmp_path):
    arret(tmp_path, "table", table=lambda t: t.update(corrections_verifiees=t["corrections_verifiees"] + 1))


def test_table_comptes_de_base_autres(tmp_path):
    arret(tmp_path, "table", attendus=lambda A: A["comptes"].update(identiques_base=2))


def test_rejeu_commit_hors_lignee_meme_arbre(tmp_path):
    """Commit de même arbre que la table v4, mais greffé sur le scellement : il ne descend pas du témoin versé."""
    def g(w):
        x = git(w.depot, "commit-tree", "HEAD^{tree}", "-p", "main~1", "-m", "greffe")
        w.h["manifeste_rejeu"] = lambda m: m.update(commit=x)
    arret(tmp_path, "commit-rejeu", apres_table=g)


def test_rejeu_commit_porte_un_chemin_de_plus(tmp_path):
    def g(w):
        w.ecrire("docs/en-plus.md", b"x\n", sceau=False)
        w.commit("chemin de plus avant le rejeu")
    sortie = arret(tmp_path, "commit-rejeu", apres_table=g)
    assert "d'autres chemins" in sortie


def test_npz_ordre_fortran(tmp_path):
    arret(tmp_path, "npz", **{"npz:activations-p3-rejeu-v1.npz":
                              lambda t: t.update(moyenne=np.asfortranarray(t["moyenne"]))})


def test_recalcul_deux_lignes(tmp_path):
    argv = monde(tmp_path)
    p = Path(argv[argv.index("--sortie-recalcul") + 1])
    p.write_text(p.read_text(encoding="utf-8") * 2, encoding="utf-8")
    code, sortie = lancer(argv)
    assert code == 2 and "ARRÊT [recalcul]" in sortie and "une seule ligne" in sortie


def test_recalcul_arbre_configuration_autre(tmp_path):
    def f(rec):
        q = rec / "prereg/R1-reparation-v4-config-v2.json"
        q.write_bytes(q.read_bytes() + b" ")
    arret(tmp_path, "recalcul", recalcul_arbre=f)


def test_manifeste_run_id_autre(tmp_path):
    arret(tmp_path, "reparation", manifeste_reparation=lambda m: m.update(run_id="20261105-010001-r1-v4-reparation-reel"))
