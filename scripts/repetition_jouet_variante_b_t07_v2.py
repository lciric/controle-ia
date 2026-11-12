#!/usr/bin/env python3
"""Répétition jouet, sur une racine locale, du script remis à l'instance de la variante B, **v2**
(`scripts/etape_a_t07_variante_b_v2.sh`) — v2 de `repetition_jouet_variante_b_t07_v1.py` (laissé intact, R12).

Écrite à la reprise de l'option (c) des concepts (R-2166 ; consigne `consigne-module-t07-option-c-reprise-v1.md`, `fdb24706…`) :
sans réseau, sans carte, sans modèle descendu, sans Vast.

Ce qui change par rapport à la v1 :
- **arbre de T0.6 matérialisé par `git show`** depuis le commit `1609a4bf` (fichiers nommés : `src/`, `prereg/P3-consignes-v1.md`
  et son compagnon, `registres/go.md`, `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json`), au lieu d'un arbre extrait à ce
  commit (aucun `checkout`, aucun `worktree` : interdits communs, règle 4), plus `docs/sources/invites-2606.08892-v1/` que lit
  `environnements/invites.py` ; la liste et les empreintes des fichiers matérialisés
  sont écrites dans le résumé ;
- **neuf arguments** (argument `PERIMETRE`, C-1) ;
- **quatre passages** du script et un passage de mesure :
  1. `normal` : registre de `main` avec la ligne `SCELLEMENT-CONCEPTS-T07`, `PERIMETRE=JD,JA,JC,CONCEPTS` → code 0, phrases des
     concepts **lues** dans `sondes-t07.json` poussé ;
  2. `sans-concepts` (option (c), repli écrit) : même dépôt sans la ligne des concepts, `PERIMETRE=JD,JA,JC` → code 0, étape A
     menée au bout, phrases **non lues** (`ligne` : « absente »), aucune direction ;
  3. artefact `branche-deja-poussee` (dépôt 1) → code 2 avant tout repli (R12) ;
  4. artefact `perimetre-faux` (dépôt 2, `PERIMETRE` qui exige `CONCEPTS` absente) → code 2 avant tout repli (C-1) ;
  5. `mesure` (`ARRET_APRES_ESSAIS=1`, `ATTENDU` « - ») sur le dépôt 1, racine neuve : fin 0 après les essais, ligne mesurée égale
     à la ligne attendue des autres passages ;
  6. `decoupage` (O-2) : dépôt 1, branche neuve, seuil d'essai bas (`SEUIL_ESSAI`, `MORCEAU_ESSAI`, `LOT_ESSAI`) : les sorties de
     l'étape A au-dessus du seuil sont découpées en morceaux scellés, poussées par lots ; recomposition contrôlée contre le
     manifeste des morceaux, le compagnon et les lignes `SCORES-T07` et `SONDES-T07` ; aucun fichier ajouté au-dessus du seuil ;
  7. `minuterie_saine` et `minuterie_delete_en_echec` (O-3) : mesure, échéance à deux secondes, API locale (`API_ESSAI`, serveur
     sur 127.0.0.1) : DELETE journalisé avec son code HTTP (un essai sur 200 ; cinq sur 500, puis « destruction laissée à la
     session »), puis état « stopped » demandé par PUT ; aucune valeur de clé journalisée (présence de l'en-tête seulement).
- le fichier `lecture-sondes-t06.json` factice que la course jouet écrit n'est **jamais ouvert** : seule sa présence dans l'arbre
  de l'instance et son objet dans le clone partiel sont contrôlés (comme en v1).

    PYTHONPATH=src python scripts/repetition_jouet_variante_b_t07_v2.py --dossier <neuf> --sortie <résumé.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ICI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ICI / "src"))
sys.path.insert(0, str(ICI / "scripts"))

import repetition_jouet_t07_v1 as r1  # noqa: E402
import repetition_jouet_t07_v2 as r2  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from controle_ia.t07 import code_t07_v1 as ct  # noqa: E402
from controle_ia.t07 import registre_v1 as rg  # noqa: E402

SCRIPT = ICI / "scripts" / "etape_a_t07_variante_b_v2.sh"
BR, BR7B = "donnees/t07-etape-a-v1", "calcul/t06-confirmation-7b-v1"
CODE = ("src", "tests", "scripts", "requirements-cpu.txt", "requirements-gpu.txt", "pyproject.toml", "docs/sources/invites-2606.08892-v1",
        "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256")
ARBRE_T06 = ("src", "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256", "registres/go.md",
             "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json",
             "docs/sources/invites-2606.08892-v1")                # lu par environnements/invites.py (parents[3] du module)
ESSAIS = "tests/test_t07_journal_p3bis_d3_v1.py"
ATTENDU = "20 passed"
MOTIFS_7B = ("adaptateur-", "mesures-t06.npz", "textes-actions-t06.jsonl", "activations-sous-ensemble-t06-")
PERIMETRE_COMPLET, PERIMETRE_SANS = "JD,JA,JC,CONCEPTS", "JD,JA,JC"
BR_DECOUPAGE = "donnees/t07-etape-a-decoupage-v1"
DECOUPAGE = {"SEUIL_ESSAI": "100000", "MORCEAU_ESSAI": "40000", "LOT_ESSAI": "2"}     # sorties jouet de l'étape A ≈ 130 à 145 ko


class FausseApi:
    """Serveur local (127.0.0.1, port libre) qui tient lieu de l'API de Vast pour la minuterie et la fin (`API_ESSAI`) ; journalise
    méthode, chemin, présence d'un en-tête `Authorization: Bearer …` (jamais sa valeur) et corps ; `DELETE` rend `code_delete` ;
    `PUT` attend `attente_put` secondes avant de rendre 200 (la minuterie a le temps de tirer)."""

    def __init__(self, code_delete: int, attente_put: float):
        self.journal, api = [], self

        class Gestion(BaseHTTPRequestHandler):
            def _rendre(self, code: int, attente: float = 0.0) -> None:
                n = int(self.headers.get("Content-Length") or 0)
                corps = self.rfile.read(n).decode("utf-8", "replace") if n else ""
                aut = self.headers.get("Authorization", "")
                api.journal.append({"methode": self.command, "chemin": self.path, "bearer": aut.startswith("Bearer ") and len(aut) > 7,
                                    "corps": corps, "instant": round(time.time(), 2)})
                time.sleep(attente)
                self.send_response(code)
                self.end_headers()

            def do_DELETE(self):  # noqa: N802
                self._rendre(code_delete)

            def do_PUT(self):  # noqa: N802
                self._rendre(200, attente_put)

            def log_message(self, *a):
                pass
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}/api/v0"

    def fermer(self) -> None:
        self.serveur.shutdown()


def git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout.strip()


def montrer(commit: str, chemins: tuple, cible: Path) -> dict:
    """Fichiers suivis de `commit` sous `chemins`, écrits sous `cible` par `git show` (jamais d'extraction d'arbre) ; rend
    chemin → sha256."""
    empreintes = {}
    for f in git(ICI, "ls-tree", "-r", "--name-only", commit, "--", *chemins).splitlines():
        brut = subprocess.run(["git", "-C", str(ICI), "show", f"{commit}:{f}"], check=True, capture_output=True).stdout
        p = cible / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(brut)
        empreintes[f] = hashlib.sha256(brut).hexdigest()
    return empreintes


def construire_origine(base: Path, nom: str, t06: Path, run6: str, avec_concepts: bool) -> dict:
    """Dépôt distant local (nu) : `main` (C7, S7, H) et la branche de 7b ; sans la ligne des concepts si `avec_concepts` est faux."""
    origine = base / f"origin-{nom}.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(origine)], check=True)
    git(origine, "config", "uploadpack.allowFilter", "true")
    git(origine, "config", "uploadpack.allowAnySHA1InWant", "true")
    maison = base / f"maison-{nom}"
    r1.depot_neuf(maison)
    montrer(git(ICI, "rev-parse", "HEAD"), CODE, maison)
    r1.committer(maison)
    c7 = git(maison, "rev-parse", "HEAD")
    for x in ("runs", "diag"):
        shutil.copytree(t06 / x / run6, maison / x / run6)
    shutil.copytree(t06 / "donnees" / "t06-jouet", maison / "donnees" / "t06-jouet")
    (maison / "registres").mkdir(exist_ok=True)
    shutil.copy(t06 / "registres" / "go.md", maison / "registres" / "go.md")
    avant = rg.date_utc(int(time.time()) - 3600)
    config7 = r1.preparer_t07(maison, avant)
    for x in ("runs", "diag"):
        shutil.rmtree(maison / x / run6)
    cfg = json.loads(config7.read_text(encoding="utf-8"))
    cfg["code_t07_exige"] = True
    config7.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(config7)
    registre = (maison / "registres" / "scellements-v1.md").read_text(encoding="utf-8")
    (maison / "registres" / "scellements-v1.md").unlink()
    r1.committer(maison)
    s7 = git(maison, "rev-parse", "HEAD")
    reg = maison / "registres" / "scellements-v1.md"
    lignes = registre.replace("| GO-ETAPE-A-T07 |", "| GO-LECTURE-T07 |").splitlines(keepends=True)
    if not avec_concepts:
        lignes = [l for l in lignes if not l.startswith(f"| {rg.SCELLEMENT_CONCEPTS_T07} |")]
    reg.write_text("".join(lignes), encoding="utf-8")
    f = ct.ecrire_fichier_code(maison, c7, maison / "registres" / "code-t07" / "CODE-T07-v1.json")
    with open(reg, "a", encoding="utf-8") as h:
        h.write(rg.ecrire_ligne(rg.CODE_T07, avant, "registres/code-t07/CODE-T07-v1.json", sceller(f)) + "\n")
    concepts_a_main = sum(1 for l in reg.read_text(encoding="utf-8").splitlines() if l.startswith(f"| {rg.SCELLEMENT_CONCEPTS_T07} |"))
    r1.committer(maison)
    h_main = git(maison, "rev-parse", "HEAD")
    git(maison, "checkout", "-q", "-b", BR7B, c7)
    for x in ("runs", "diag"):
        shutil.copytree(t06 / x / run6, maison / x / run6)
    (maison / "donnees" / run6).mkdir(parents=True)
    poussees = []
    for p in sorted((t06 / "donnees" / run6).iterdir()):
        if p.is_file() and p.name.startswith(MOTIFS_7B):
            shutil.copy(p, maison / "donnees" / run6 / p.name)
            poussees.append(p.name)
    r1.committer(maison)
    git(maison, "push", "-q", str(origine), "main", BR7B)
    return {"origine": origine, "C7": c7, "S7": s7, "H": h_main, "config": config7.name, "branche_7b": git(maison, "rev-parse", BR7B),
            "donnees_7b": poussees, "ligne_concepts_a_main": concepts_a_main}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--entropie-t06", type=int, default=1)
    ap.add_argument("--commit-t06", default=r1.COMMIT_T06)
    ap.add_argument("--script", default=str(SCRIPT), help="script joué (défaut : la v2 de l'arbre) ; autre valeur : artefact déclaré")
    ap.add_argument("--normal-seulement", action="store_true", help="passage 1 seulement (artefact d'un script fautif)")
    a = ap.parse_args(argv)
    script = Path(a.script).resolve()
    base = Path(a.dossier).resolve()
    if base.exists():
        print(f"REFUS : {base} existe déjà (R12)", file=sys.stderr)
        return 2
    base.mkdir(parents=True)
    journal = base / "journal-repetition.txt"
    resume = {"debut": datetime.now(timezone.utc).isoformat(), "commit_t07": git(ICI, "rev-parse", "HEAD"),
              "script": {"chemin": str(script), "sha256": ct._sha(script.read_bytes())}}
    # 0. arbre de T0.6 matérialisé par git show (aucune extraction d'arbre)
    arbre = base / "arbre-t06"
    commit6 = git(ICI, "rev-parse", f"{a.commit_t06}^{{commit}}")
    emp = montrer(commit6, ARBRE_T06, arbre)
    resume["arbre_t06"] = {"commit": commit6, "fichiers": len(emp),
                           "empreinte_liste": hashlib.sha256(json.dumps(emp, sort_keys=True).encode()).hexdigest()}
    # 1. course 7b jouet
    t06 = base / "t06"
    r1.depot_neuf(t06)
    config6 = r1.preparer_t06(t06, arbre)
    r6 = r1.lancer([a.python, "-c", r2.ENVELOPPE, str(a.entropie_t06), "--config", config6.name, "--run-id", r1.RUN_T06], t06,
                   arbre / "src", journal)
    resume["t06"] = {k: r6[k] for k in ("code", "duree_s")}
    if r6["code"] != 0:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        return 1
    run6 = r1.RUN_T06
    # 2. deux dépôts distants locaux : avec et sans la ligne des concepts
    o1 = construire_origine(base, "avec-concepts", t06, run6, True)
    o2 = construire_origine(base, "sans-concepts", t06, run6, False)
    resume["depots"] = {n: {k: (str(v) if isinstance(v, Path) else v) for k, v in o.items()} for n, o in (("avec", o1), ("sans", o2))}

    # 3. le script de l'instance, tel quel, sous env -i
    def jouer(racine: Path, o: dict, perimetre: str, attendu: str = ATTENDU, extra: dict | None = None, branche: str = BR,
              echeance_s: int = 6 * 3600) -> dict:
        env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(base), "LANG": "C.UTF-8", "GH_TOKEN": "essai-local",
               "ESSAI_LOCAL": "1", "RACINE_INSTANCE": str(racine), "DEPOT_URL": f"file://{o['origine']}", "ESSAIS_LISTE": ESSAIS,
               "VENV_EXISTANT": str(Path(a.python).parents[1]), "GIT_CONFIG_NOSYSTEM": "1",
               **({"TMPDIR": os.environ["TMPDIR"]} if os.environ.get("TMPDIR") else {}), **(extra or {})}
        debut = time.perf_counter()
        p = subprocess.run(["bash", str(script), o["S7"], o["C7"], run6, o["config"], branche, BR7B, attendu,
                            str(int(time.time()) + echeance_s), perimetre], env=env, capture_output=True, text=True, timeout=1800)
        with open(journal, "a", encoding="utf-8") as h:
            h.write(f"$ bash {script.name} … (racine {racine.name}, PERIMETRE {perimetre})\ncode {p.returncode} en "
                    f"{round(time.perf_counter() - debut, 1)} s\n--- sortie\n{p.stdout[-8000:]}\n--- erreur\n{p.stderr[-4000:]}\n\n")
        fin = racine / "t07-etape-a-b-v1" / "fin-demandee"
        lignes = [l.split(" T07 ", 1)[1] for l in p.stdout.splitlines() if " T07 " in l]
        return {"code": p.returncode, "duree_s": round(time.perf_counter() - debut, 1),
                "fin": fin.read_text().strip() if fin.is_file() else None, "lignes": lignes,
                "repli_joue": any(l.startswith("repli, essai") for l in lignes), "derniere": lignes[-1] if lignes else None}

    def lire_pousse(org: Path, branche: str, chemin: str) -> bytes:
        """Fichier poussé, lu tel quel, ou recomposé depuis ses morceaux (manifeste `<chemin>.morceaux.json`)."""
        presents = set(git(org, "ls-tree", "-r", "--name-only", branche).splitlines())
        if chemin in presents:
            return subprocess.run(["git", "-C", str(org), "show", f"{branche}:{chemin}"], check=True, capture_output=True).stdout
        m = json.loads(git(org, "show", f"{branche}:{chemin}.morceaux.json"))
        d = os.path.dirname(chemin)
        return b"".join(subprocess.run(["git", "-C", str(org), "show", f"{branche}:{d}/{x['fichier']}"], check=True,
                                       capture_output=True).stdout for x in m["morceaux"])

    def controler(racine: Path, o: dict, branche: str = BR) -> dict:
        org, c = o["origine"], {}
        commits = git(org, "log", "--format=%s", f"{o['H']}..{branche}").splitlines()
        c["commits_pousses"] = commits[::-1]
        reg_pousse = git(org, "show", f"{branche}:registres/scellements-v1.md")
        c["lignes_scores_sondes"] = [l.split("|")[1].strip() for l in reg_pousse.splitlines() if l.startswith(("| SCORES-T07 |", "| SONDES-T07 |"))]
        c["src_tests_inchanges"] = subprocess.run(["git", "-C", str(org), "diff", "--quiet", o["C7"], branche, "--", "src", "tests"]).returncode == 0
        run7 = sorted(x for x in git(org, "ls-tree", "--name-only", f"{branche}:runs").splitlines() if "-t07-lecture-" in x)[-1]
        s = json.loads(lire_pousse(org, branche, f"diag/{run7}/sondes-t07.json"))["resultat"]
        m = json.loads(lire_pousse(org, branche, f"runs/{run7}/manifeste.json"))
        c["run_t07"] = run7
        c["phrases_concepts"] = s.get("phrases_concepts")
        c["directions"] = len(s["sondes_neuves"]["directions"])
        c["phrases_au_manifeste"] = m["config"].get("phrases_concepts_etape_a")
        c["taches_plancher_concept"] = sum(1 for t in m["graines"] if t.startswith("plancher-concept/"))
        depot_i = racine / "t07-etape-a-b-v1" / "depot"
        c["lecture_sondes_dans_l_arbre"] = (depot_i / "diag" / run6 / "lecture-sondes-t06.json").exists()
        oid = git(org, "rev-parse", f"{BR7B}:diag/{run6}/lecture-sondes-t06.json")
        manquants = subprocess.run(["git", "-C", str(depot_i), "rev-list", "--objects", "--missing=print", f"refs/remotes/origin/{BR7B}"],
                                   capture_output=True, text=True).stdout.split()
        c["lecture_sondes_descendu"] = oid in manquants
        c["lecture_sondes_objet_manquant_du_clone"] = f"?{oid}" in manquants
        return c

    passages = {}
    p1 = jouer(base / "instance-normal", o1, PERIMETRE_COMPLET)
    passages["normal"] = {**p1, "controles": controler(base / "instance-normal", o1) if p1["code"] == 0 else None}
    if a.normal_seulement:
        resume["passages"], resume["fin"] = passages, datetime.now(timezone.utc).isoformat()
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
        print(json.dumps({"normal": {k: p1[k] for k in ("code", "fin", "derniere")}}, ensure_ascii=False))
        return 0 if p1["code"] == 0 else 1
    p2 = jouer(base / "instance-sans-concepts", o2, PERIMETRE_SANS)
    passages["sans_concepts"] = {**p2, "controles": controler(base / "instance-sans-concepts", o2) if p2["code"] == 0 else None}
    passages["artefact_branche_deja_poussee"] = jouer(base / "instance-artefact-branche", o1, PERIMETRE_COMPLET)
    passages["artefact_perimetre_faux"] = jouer(base / "instance-artefact-perimetre", o2, PERIMETRE_COMPLET)
    pm = jouer(base / "instance-mesure", o1, PERIMETRE_COMPLET, "-", {"ARRET_APRES_ESSAIS": "1"})
    lm = base / "instance-mesure" / "t07-etape-a-b-v1" / "ligne-essais-mesuree.txt"
    passages["mesure"] = {**pm, "ligne_mesuree": lm.read_text(encoding="utf-8").strip() if lm.is_file() else None}
    # O-2 : découpage des fichiers de plus de SEUIL octets (seuil d'essai bas), sur une branche neuve du dépôt 1
    pd = jouer(base / "instance-decoupage", o1, PERIMETRE_COMPLET, extra=DECOUPAGE, branche=BR_DECOUPAGE)
    dec = {"controles": controler(base / "instance-decoupage", o1, BR_DECOUPAGE) if pd["code"] == 0 else None}
    if pd["code"] == 0:
        org = o1["origine"]
        ajoutes = git(org, "diff", "--name-only", "--diff-filter=A", o1["H"], BR_DECOUPAGE).splitlines()
        tailles = {l.split("\t", 1)[1]: int(l.split()[3]) for l in git(org, "ls-tree", "-r", "-l", BR_DECOUPAGE).splitlines()}
        seuil = int(DECOUPAGE["SEUIL_ESSAI"])
        manifs = sorted(x for x in ajoutes if x.endswith(".morceaux.json"))
        fichiers = []
        for mf in manifs:
            m = json.loads(git(org, "show", f"{BR_DECOUPAGE}:{mf}"))
            orig = mf[: -len(".morceaux.json")]
            brut = lire_pousse(org, BR_DECOUPAGE, orig)
            compagnon = git(org, "show", f"{BR_DECOUPAGE}:{orig}.sha256").split()[0]
            fichiers.append({"fichier": orig, "octets": m["octets"], "morceaux": len(m["morceaux"]),
                             "recomposition_egale": hashlib.sha256(brut).hexdigest() == m["sha256"] == compagnon,
                             "original_absent_de_la_branche": orig not in tailles,
                             "sceaux_des_morceaux": all(git(org, "show", f"{BR_DECOUPAGE}:{os.path.dirname(orig)}/{x['fichier']}.sha256").split()[0]
                                                        == x["sha256"] for x in m["morceaux"])})
        reg_d = git(org, "show", f"{BR_DECOUPAGE}:registres/scellements-v1.md")
        lignes_rs = {l.split("|")[1].strip(): (l.split("|")[3].strip(), l.split("|")[4].strip()) for l in reg_d.splitlines()
                     if l.startswith(("| SCORES-T07 |", "| SONDES-T07 |"))}
        dec.update({"fichiers_decoupes": fichiers,
                    "ajoutes_au_dessus_du_seuil": sorted(x for x in ajoutes if tailles.get(x, 0) > seuil),
                    "commits_de_morceaux": sum(1 for x in dec["controles"]["commits_pousses"] if ": morceaux " in x),
                    "scores_recomposes_egaux_au_registre": all(
                        hashlib.sha256(lire_pousse(org, BR_DECOUPAGE, ch)).hexdigest() == sha for ch, sha in lignes_rs.values())})
    passages["decoupage"] = {**pd, **dec}
    # O-3 : minuterie et fin contre une API locale (cas sain : DELETE rendu 200 ; artefact : DELETE en 500, cinq essais journalisés)
    for nom, code_delete in (("minuterie_saine", 200), ("minuterie_delete_en_echec", 500)):
        api = FausseApi(code_delete, 6.0)
        try:
            pmn = jouer(base / f"instance-{nom}", o1, PERIMETRE_COMPLET, "-",
                        {"ARRET_APRES_ESSAIS": "1", "API_ESSAI": api.url, "MINUTERIE_PAUSE_S": "0", "CONTAINER_ID": "4242",
                         "CONTAINER_API_KEY": "cle-factice-de-repetition"}, echeance_s=2)
        finally:
            api.fermer()
        passages[nom] = {**pmn, "api": api.journal}
    resume["passages"] = passages
    resume["fin"] = datetime.now(timezone.utc).isoformat()

    n, s = passages["normal"], passages["sans_concepts"]
    ab, ap_ = passages["artefact_branche_deja_poussee"], passages["artefact_perimetre_faux"]
    verdicts = {
        "normal_code_0": n["code"] == 0 and n["fin"] == "fin 0",
        "normal_phrases_lues": bool(n["controles"]) and (n["controles"]["phrases_concepts"] or {}).get("etat") == "lues"
                               and n["controles"]["directions"] > 0 and n["controles"]["taches_plancher_concept"] > 0,
        "sans_code_0": s["code"] == 0 and s["fin"] == "fin 0",
        "sans_phrases_non_lues": bool(s["controles"]) and (s["controles"]["phrases_concepts"] or {}).get("etat") == "non lues"
                                 and (s["controles"]["phrases_concepts"] or {}).get("ligne") == "absente"
                                 and s["controles"]["directions"] == 0 and s["controles"]["taches_plancher_concept"] == 0
                                 and (s["controles"]["phrases_au_manifeste"] or {}).get("etat") == "non lues",
        "sorties_poussees": all(x["controles"] and len(x["controles"]["lignes_scores_sondes"]) == 2 and x["controles"]["src_tests_inchanges"]
                                for x in (n, s)),
        "embargo_tenu": all(x["controles"] and not x["controles"]["lecture_sondes_dans_l_arbre"] and not x["controles"]["lecture_sondes_descendu"]
                            for x in (n, s)),
        "artefact_branche_code_2_sans_repli": ab["code"] == 2 and not ab["repli_joue"],
        "artefact_perimetre_code_2_sans_repli": ap_["code"] == 2 and not ap_["repli_joue"] and "périmètre (C-1)" in (ap_["derniere"] or "")
                                                 + " ".join(ap_["lignes"]),
        "mesure_egale_attendu": pm["code"] == 0 and pm["fin"] == "fin 0" and passages["mesure"]["ligne_mesuree"] == ATTENDU
                                and not pm["repli_joue"],
        "decoupage_conforme": (pd["code"] == 0 and pd["fin"] == "fin 0" and len(passages["decoupage"].get("fichiers_decoupes", [])) >= 2
                               and all(f["recomposition_egale"] and f["original_absent_de_la_branche"] and f["sceaux_des_morceaux"]
                                       and f["morceaux"] >= 2 for f in passages["decoupage"]["fichiers_decoupes"])
                               and passages["decoupage"]["ajoutes_au_dessus_du_seuil"] == []
                               and passages["decoupage"]["commits_de_morceaux"] >= 2
                               and passages["decoupage"]["scores_recomposes_egaux_au_registre"]
                               and len(passages["decoupage"]["controles"]["lignes_scores_sondes"]) == 2),
        "minuterie_saine": _minuterie(passages["minuterie_saine"], 1, "HTTP 200"),
        "minuterie_delete_en_echec_cinq_essais": _minuterie(passages["minuterie_delete_en_echec"], 5, "HTTP 500")
                                                 and any("cinq DELETE sans succès" in l for l in passages["minuterie_delete_en_echec"]["lignes"]),
    }
    resume["verdicts"] = verdicts
    ok = all(verdicts.values())
    resume["conforme"] = ok
    Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print(json.dumps({"verdicts": verdicts, "conforme": ok}, ensure_ascii=False))
    return 0 if ok else 1


def _minuterie(p: dict, n_delete: int, code: str) -> bool:
    """Minuterie et fin jouées contre l'API locale : `n_delete` DELETE journalisés avec leur code, en-tête Bearer présent, puis
    l'état « stopped » demandé par PUT ; code 0, fin 0 (mesure)."""
    deletes = [x for x in p["api"] if x["methode"] == "DELETE"]
    puts = [x for x in p["api"] if x["methode"] == "PUT"]
    lignes_delete = [l for l in p["lignes"] if l.startswith("MINUTERIE : DELETE, essai ")]
    return (p["code"] == 0 and p["fin"] == "fin 0" and len(deletes) == n_delete and len(lignes_delete) == n_delete
            and all(code in l for l in lignes_delete) and all(x["bearer"] and x["chemin"] == "/api/v0/instances/4242/" for x in deletes + puts)
            and len(puts) == 1 and json.loads(puts[0]["corps"] or "{}") == {"state": "stopped"}
            and any(l.startswith("fin, code 0 ; état « stopped » demandé : HTTP 200") for l in p["lignes"]))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
