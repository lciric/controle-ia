#!/usr/bin/env python3
"""Sonde de l'hôte durable d'A1-v3 (GO-2026-11-04-09, GO de la machine), v1 : une course factice sur une vraie machine Vast sans carte.

But : éprouver, avant la troisième course et pour quelques centimes, ce que les essais jouets ne peuvent pas éprouver — la
recherche et la création d'une machine sans carte par l'outil `vastai`, l'image (`python:3.13-bookworm` : git, Python,
`/usr/bin/python3`, installation de numpy au numéro exact), une commande détachée suivie par l'hôte, le versement d'une sortie
factice scellée sur la branche `donnees/sonde-hote-durable-a1-v3-v1`, la lecture de la clé d'instance (`CONTAINER_API_KEY`),
l'arrêt au plafond de durée et la destruction de la machine par son propre identifiant.

**Aucune clé d'Argon, aucun relais, aucun appel de modèle** : la sonde refuse de partir si une variable de clé de modèle est
dans son environnement (`CLE_ARGON`, `GEMINI*`, `ANTHROPIC*`, `OPENAI*`, `MOONSHOT*`, `KIMI*`). Seul secret : le jeton GitHub
limité au dépôt privé de travail, qui sert au versement.

Plafonds écrits : prix horaire au plus 0,40 USD (offre **la moins chère** des offres conformes de la réponse) ; durée de la
course factice bornée par le plafond de durée de la sonde, 20 min par défaut, 30 au plus ; dépense de machine au plus 0,50 USD,
marge de démarrage et de versement comprise (15 min). La course factice dure plus longtemps que le plafond : la sonde doit
finir **par son plafond de durée**, qui est ce qu'elle éprouve.

Réutilise les gardes, le scellement, le contrôle des secrets, le versement et la destruction du lanceur durable
(`hote_durable_a1_v3.py`, `Machine`), sans les modifier.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:  # paquet (essais) ou fichier seul (machine : `python3 -I -B …/sonde_hote_durable_a1_v3.py`)
    from . import hote_durable_a1_v3 as h
except ImportError:
    _spec = importlib.util.spec_from_file_location("hote_durable_a1_v3", Path(__file__).resolve().parent / "hote_durable_a1_v3.py")
    h = importlib.util.module_from_spec(_spec)
    sys.modules["hote_durable_a1_v3"] = h
    _spec.loader.exec_module(h)

VERSION = "sonde-hote-durable-a1-v3-v1"
GO_SONDE = "GO-2026-11-04-09"      # GO de la machine (mot de Lazar, 4 novembre 08:41 UTC) ; GO-2026-11-04-06 : Argon seul
MONTANT_GO_SONDE_USD = 35.0
BRANCHE_SONDE = "donnees/sonde-hote-durable-a1-v3-v1"
BRANCHE_SONDE_INTERROMPUE = "donnees/sonde-hote-durable-a1-v3-interrompue-v1"
DUREE_DEFAUT_MIN, DUREE_MAX_MIN = 20, 30
MARGE_MIN = 15                 # démarrage de la machine, installation, versement, destruction
PLAFOND_SONDE_USD = 0.50
COURSE_FACTICE_S = 3600        # plus long que tout plafond de la sonde : la fin doit venir du plafond de durée
CLES_INTERDITES = re.compile(r"^(CLE_ARGON|GEMINI.*|ANTHROPIC.*|OPENAI.*|MOONSHOT.*|KIMI.*|RR_.*API_KEY.*)$")
AMORCE = "scripts/amorce_sonde_hote_durable_a1_v3_v1.sh"
COURSE_FACTICE = r'''
import json, os, sys, time
d = sys.argv[1]; duree = float(sys.argv[2]); os.makedirs(d)
cles = sorted(k for k in os.environ if any(m in k.upper() for m in ("KEY", "TOKEN", "CLE")))
with open(os.path.join(d, "manifeste-factice.json"), "w") as f:
    json.dump({"pid": os.getpid(), "debut": time.time(), "variables_de_cle": cles}, f)
fin = time.time() + duree
while time.time() < fin:
    with open(os.path.join(d, "battements.txt"), "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
    time.sleep(min(10.0, max(0.05, fin - time.time())))
with open(os.path.join(d, "resultat-factice.json"), "w") as f:
    json.dump({"fin": "normale"}, f)
'''


def verifier_go_sonde(chemin_registre: Path, chemin_garde: Path, go_id: str, aujourd_hui: dt.date) -> dict:
    """GO de la machine : la garde de `main` telle quelle (type, Lazar, validité, révocation, extensions), puis montant
    exactement 35 USD sur la ligne et sur chaque extension ; tout autre GO (GO-2026-11-04-06 compris) est refusé."""
    if go_id != GO_SONDE:
        raise h.Refus(f"GO {go_id} : la sonde ne part que sous {GO_SONDE} (GO de la machine ; aucun autre GO)")
    garde = h.charger_garde(chemin_garde, chemin_registre)
    tampon = h.io.StringIO()
    try:
        with h.redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise h.Refus(f"garde de main : {tampon.getvalue().strip()}") from None
    lignes = h.lignes_du_go(chemin_registre, go_id)
    if not lignes:
        raise h.Refus(f"{go_id} absent du registre")
    for cellules in lignes:
        m = h.MONTANT.match(cellules[4])
        if not m or abs(float(m.group(1).replace(",", ".")) - MONTANT_GO_SONDE_USD) > 1e-9:
            raise h.Refus(f"{go_id} : plafond « {cellules[4]} » au lieu de exactement {MONTANT_GO_SONDE_USD:g} USD")
    return {"go": go_id, "lignes": len(lignes), "plafond_usd": MONTANT_GO_SONDE_USD,
            "registre_sha256": h.sha256_fichier(chemin_registre), "echeance": lignes[0][5]}


def cles_de_modele(environ: dict) -> list[str]:
    return sorted(k for k, v in environ.items() if v and CLES_INTERDITES.match(k))


def verifier_plafond_sonde(dph: float, duree_min: float, plafond_usd: float = PLAFOND_SONDE_USD) -> float:
    if not (0 < duree_min <= DUREE_MAX_MIN):
        raise h.Refus(f"durée de la sonde {duree_min} min hors de ]0 ; {DUREE_MAX_MIN}]")
    cout = dph * (duree_min + MARGE_MIN) / 60
    if cout > plafond_usd:
        raise h.Refus(f"dépense de la sonde au plus {cout:.4f} USD > plafond {plafond_usd} USD")
    return cout


def offre_la_moins_chere(offres: list[dict], offre_id: int) -> dict:
    """L'offre choisie doit être conforme (garde du lanceur durable) et la moins chère des offres conformes de la réponse."""
    choisie = h.verifier_offre(offres, offre_id)
    conformes = []
    for o in offres:
        try:
            conformes.append(h.verifier_offre([o], o.get("id")))
        except h.Refus:
            continue
    moins = min(c["dph_total"] for c in conformes)
    if choisie["dph_total"] > moins + 1e-12:
        raise h.Refus(f"offre {offre_id} à {choisie['dph_total']} USD/h : une offre conforme est moins chère ({moins})")
    return choisie


def script_de_demarrage_sonde(commit_prive: str) -> str:
    base = h.script_de_demarrage(commit_prive)
    ancien = "bash /root/amorce-depot/scripts/amorce_hote_durable_a1_v3_v1.sh 2>&1 | tee -a /root/amorce-a1v3.log"
    assert base.count(ancien) == 1
    return base.replace(ancien, f"bash /root/amorce-depot/{AMORCE} 2>&1 | tee -a /root/amorce-sonde-a1v3.log")


def corps_sonde(commit_prive: str, offre: dict, duree_min: float, gh_token: str) -> dict:
    if not gh_token:
        raise h.Refus("GH_TOKEN absent : la sonde ne pourrait pas verser")
    env = {"COMMIT_PRIVE": commit_prive, "GO_ID": GO_SONDE, "PRIX_H_USD": f"{offre['dph_total']:.6f}",
           "DUREE_MAX_S": str(int(duree_min * 60)), "DEPOT_URL": h.DEPOT_PRIVE, "GH_TOKEN": gh_token}
    interdites = cles_de_modele(env)
    if interdites:  # garde redondante : le corps ne doit porter aucune clé de modèle
        raise h.Refus(f"clé de modèle dans le corps de la sonde : {interdites}")
    b64 = __import__("base64").b64encode(script_de_demarrage_sonde(commit_prive).encode()).decode("ascii")
    return {"image": h.IMAGE, "disk": 30, "label": "sonde-a1-v3-v1", "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-sonde-a1v3.sh && bash /root/demarrage-sonde-a1v3.sh"}


class ClientSondeCli(h.ClientVastCli):
    """Création de la sonde : même outil, mêmes options ; seul secret masqué, le jeton GitHub."""

    def creer(self, offre_id: int, corps: dict) -> int:
        if cles_de_modele(corps["env"]):
            raise h.Refus("clé de modèle dans le corps de la sonde : rien créé")
        if any(c.isspace() or c in "\"'" for v in corps["env"].values() for c in v):
            raise h.Refus("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        env = " ".join(f"-e {k}={v}" for k, v in corps["env"].items())
        args = ["create", "instance", str(offre_id), "--raw", "--image", corps["image"], "--disk", str(corps["disk"]),
                "--cancel-unavail", "--label", corps["label"], "--env", env, "--entrypoint", "bash", "--args", "-c",
                corps["script"]]
        texte = self._lancer(args, {"GH_TOKEN": corps["env"]["GH_TOKEN"]})
        for ligne in reversed(texte.strip().splitlines()):
            try:
                rep = json.loads(ligne)
            except ValueError:
                continue
            if rep.get("success") and isinstance(rep.get("new_contract"), int):
                return rep["new_contract"]
            break
        raise h.Refus("création de la sonde refusée ou réponse illisible : vérifier par l'inventaire")


def louer_sonde(a, client=None, aujourd_hui=None, environ=None) -> int:
    environ = dict(os.environ) if environ is None else environ
    j = h.Journal(Path(a.journal_local), {k: environ.get(k, "") for k in ("GH_TOKEN", "VAST_API_KEY", "CLE_ARGON")})
    try:
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        g = verifier_go_sonde(Path(a.registre_main), Path(a.garde_main), a.go, aujourd_hui)
        j.ecrire(f"sonde : GO {g['go']} accepté par la garde de main (registre {g['registre_sha256']})")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = offre_la_moins_chere(offres, int(a.offre))
        cout = verifier_plafond_sonde(o["dph_total"], float(a.duree_min))
        j.ecrire(f"sonde : offre {o['id']} à {o['dph_total']} USD/h, la moins chère des conformes ; plafond de durée "
                 f"{a.duree_min} min ; dépense au plus {cout:.4f} USD ≤ {PLAFOND_SONDE_USD} USD")
        corps = corps_sonde(a.commit_prive, o, float(a.duree_min), environ.get("GH_TOKEN", ""))
        if a.verifier_seulement:
            j.ecrire("sonde, vérification seulement : rien créé (variables : " + ", ".join(sorted(corps["env"])) + ")")
            return 0
        ident = (client or ClientSondeCli()).creer(o["id"], corps)
        j.ecrire(f"sonde créée : identifiant {ident}")
        Path(a.journal_local + ".identifiant").write_text(f"{ident}\n")
        return 0
    except (h.Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


class MachineSonde(h.Machine):
    """La séquence de la sonde ; scellement, contrôle des secrets, versement et destruction hérités du lanceur durable."""

    def __init__(self, r: h.Reglages, environ: dict[str, str], course_factice_s: float = COURSE_FACTICE_S):
        super().__init__(r, environ)
        self.course_factice_s = course_factice_s

    def principal(self) -> int:
        journal = self.t / "journal-sonde-a1-v3-v1.log"
        if self.etat_fichier.exists():
            self.j = h.Journal(journal, self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur de la sonde : état « {avant} » ; rien n'est relancé")
            if avant == "verse":
                return self.se_detruire(True)
            self.nature_fin = "reprise_du_conteneur"
            return self.fin(BRANCHE_SONDE_INTERROMPUE)
        self.t.mkdir(parents=True, exist_ok=False)
        self.j = h.Journal(journal, self.secrets)
        self.j.ecrire(f"{VERSION} ; machine {self.env.get('CONTAINER_ID', '?')} ; prix {self.prix_h} USD/h ; "
                      f"plafond de durée {self.r.duree_max_s:g} s")
        self.etat("demarrage")
        try:
            self.preparer_sonde()
            self.etat("course")
            self.garder_sonde()
        except h.Refus as e:
            self.j.ecrire(f"REFUS : {e}")
            self.nature_fin = "refus_avant_course" if self.course is None else "refus_pendant_la_course"
        except Exception as e:  # jamais un repli silencieux
            self.j.ecrire(f"EXCEPTION {type(e).__name__} : {self.j.masquer(str(e))[:500]}")
            self.nature_fin = "exception_de_l_hote"
        return self.fin(BRANCHE_SONDE)

    def preparer_sonde(self) -> None:
        e, r = self.env, self.r
        interdites = cles_de_modele(e)
        if interdites:
            raise h.Refus(f"clé de modèle dans l'environnement de la sonde : {interdites} (aucune clé d'Argon)")
        for k in ("GH_TOKEN", "GO_ID", "PRIX_H_USD", "DUREE_MAX_S"):
            if not e.get(k):
                raise h.Refus(f"variable {k} absente")
        if not (0 < self.prix_h <= h.PRIX_MAX_H_USD):
            raise h.Refus(f"prix horaire {self.prix_h} hors de ]0 ; {h.PRIX_MAX_H_USD}]")
        verifier_plafond_sonde(self.prix_h, r.duree_max_s / 60)
        h.git("fetch", "-q", "origin", "+refs/heads/main:refs/remotes/origin/main", cwd=r.clone_prive,
              gh_token=self.secrets["GH_TOKEN"])
        tete = h.git("rev-parse", "refs/remotes/origin/main", cwd=r.clone_prive).strip()
        reg, garde = self.t / "registre-go-main.md", self.t / "garde_calcul_main.py"
        reg.write_bytes(h.lancer(["git", "show", f"{tete}:registres/go.md"], cwd=r.clone_prive).stdout)
        garde.write_bytes(h.lancer(["git", "show", f"{tete}:.claude/hooks/garde_calcul.py"], cwd=r.clone_prive).stdout)
        g = verifier_go_sonde(reg, garde, e["GO_ID"], r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        self.j.ecrire(f"GO accepté par la garde de main {tete} : {g['go']}, {g['plafond_usd']:g} USD")
        self.relever_l_hote()
        self.lire_cle_d_instance()
        sortie = self.t / "sortie-factice"
        out = open(self.t / "course-factice-stdout.log", "ab")
        self.course = subprocess.Popen([sys.executable, "-I", "-B", "-c", COURSE_FACTICE, str(sortie),
                                        str(self.course_factice_s)], env={"PATH": "/usr/local/bin:/usr/bin:/bin",
                                                                          "LANG": "C.UTF-8"},
                                       stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                       start_new_session=True)
        self.j.ecrire(f"course factice détachée : PID {self.course.pid} (durée prévue {self.course_factice_s:g} s, "
                      f"au-delà du plafond de {r.duree_max_s:g} s)")

    def sceller(self) -> Path:
        liste = self.t / "EMPREINTES-sonde-hote-durable-a1-v3-v1.txt"
        lignes = [f"{h.sha256_fichier(p)}  {p.relative_to(self.t)}" for p in self.fichiers_a_verser() if p != liste]
        liste.write_text("\n".join(lignes) + "\n")
        return liste

    def relever_l_hote(self) -> None:
        """Faits de l'image et de la machine, écrits au journal : ce que la vraie course trouvera."""
        def sortie(cmd):
            try:
                rr = h.lancer(cmd, delai=60)
                return (rr.stdout + rr.stderr).decode("utf-8", "replace").strip()[:200]
            except Exception as x:  # absent : c'est un fait à écrire, pas une erreur
                return f"absent ({type(x).__name__})"
        faits = {"python_sonde": sys.version.split()[0], "plateforme": platform.platform(),
                 "usr_bin_python3": sortie(["/usr/bin/python3", "--version"]),
                 "numpy": sortie(["python3", "-c", "import numpy; print(numpy.__version__)"]),
                 "git": sortie(["git", "--version"]), "coeurs": os.cpu_count(),
                 "disque_libre_go": round(shutil.disk_usage("/").free / 1e9, 1),
                 "container_id_present": bool(self.env.get("CONTAINER_ID")),
                 "container_api_key_presente": bool(self.env.get("CONTAINER_API_KEY"))}
        (self.t / "faits-hote.json").write_text(json.dumps(faits, ensure_ascii=False, indent=1))
        self.j.ecrire("faits de l'hôte : " + json.dumps(faits, ensure_ascii=False))

    def lire_cle_d_instance(self) -> None:
        """Mesure, pas une garde : la clé d'instance lit-elle la machine ? (la destruction finale dira si elle détruit)."""
        ident = self.env.get("CONTAINER_ID", "")
        try:
            client = h.ClientVastJouet(self.r.vast_jouet) if self.r.jouet else h.ClientVast(self.secrets["CONTAINER_API_KEY"])
            vues = [i.get("id") for i in client.instances()]
            self.j.ecrire(f"clé d'instance : lecture faite, {len(vues)} instance(s), la machine {ident} "
                          f"{'vue' if ident.isdigit() and int(ident) in vues else 'NON vue'}")
        except h.Refus as x:
            self.j.ecrire(f"clé d'instance : lecture refusée ({x})")

    def garder_sonde(self) -> None:
        r = self.r
        releves = self.t / "garde-sonde-a1-v3.jsonl"
        while True:
            code = self.course.poll()
            ecoule = time.monotonic() - self.debut
            with open(releves, "a", encoding="utf-8") as f:
                f.write(json.dumps({"utc": h.maintenant(), "course_vivante": code is None, "ecoule_s": round(ecoule, 1),
                                    "cout_machine_usd": round(self.cout_machine(), 5)}) + "\n")
            if code is not None:
                self.code_course = code
                (self.t / "code-sortie-course-factice.txt").write_text(f"{code}\n")
                self.j.ecrire(f"fin de la course factice avant le plafond : code {code}")
                self.nature_fin = "fin_de_la_course_factice"
                return
            if ecoule >= r.duree_max_s or self.cout_machine() >= r.plafond_machine_usd:
                self.nature_fin = "plafond_de_duree_de_la_sonde"
                self.j.ecrire(f"PLAFOND DE DURÉE DE LA SONDE atteint ({ecoule:.1f} s, {self.cout_machine():.4f} USD) : "
                              "course factice arrêtée par son identifiant (attendu)")
                self.code_course = h.arreter_par_pid(self.course, self.j, "course factice")
                (self.t / "code-sortie-course-factice.txt").write_text(f"{self.code_course} (plafond de durée)\n")
                return
            time.sleep(r.periode_s)


def reglages_sonde(environ: dict) -> h.Reglages:
    duree = float(environ.get("DUREE_MAX_S", DUREE_DEFAUT_MIN * 60))
    return h.Reglages(travail=Path("/root/sonde-a1-v3-v1"), duree_max_s=duree, periode_s=30,
                      plafond_machine_usd=PLAFOND_SONDE_USD)


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer")
    for nom in ("--go", "--registre-main", "--garde-main", "--offres", "--offre", "--commit-prive", "--journal-local"):
        l.add_argument(nom, required=True)
    l.add_argument("--duree-min", default=str(DUREE_DEFAUT_MIN))
    l.add_argument("--verifier-seulement", action="store_true")
    sous.add_parser("hote")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer_sonde(args)
    env = dict(os.environ)
    return MachineSonde(reglages_sonde(env), env).principal()


if __name__ == "__main__":
    sys.exit(principal())
