"""Lecture d'intégrité et de conformité, étape F, relance v4 de R1 (lecteur R13, lecture seule).

Usage : python -I lecture_integrite_v1.py <arbre de lecture> <dépôt main>
N'écrit rien dans les arbres lus ; imprime sur la sortie standard.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ARBRE = Path(sys.argv[1])
MAIN = Path(sys.argv[2])
COMMIT_MAIN = "759d0103"
COMMIT_CITE = "b478ea39ccfb1b897ebcf1016ab6e0aae17344fb"

V4 = {
    "principale": ("20261106-121351-analyse-principale-r1-r2-v1", "analyse-principale-r1-r2-v1", "c0b3875d", "2a192479",
                   "python -m controle_ia.analyse_principale_r1_r2.lecture_v8", "prereg/analyse-principale-r1-r2-v1.md",
                   "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537",
                   "prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json",
                   "### Liste fermée du code — analyse principale (code v8)"),
    "par_episode": ("20261106-121448-analyse-par-episode-v1", "analyse-par-episode-v1", "fbf4b71f", "a1f04ce8",
                    "python -m controle_ia.analyse_principale_r1_r2.lecture_v9", "prereg/analyse-par-episode-v1.md",
                    "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4",
                    "prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json",
                    "### Liste fermée du code — analyse par épisode (code v9)"),
    "secondaire": ("20261106-121459-analyse-blanche-noire-v3", "analyse-blanche-noire-v3", "23e98831", "6f2bd078",
                   "python -m controle_ia.analyse_blanche_noire.lecture_v5", "prereg/analyse-blanche-noire-v3.md",
                   "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9",
                   "prereg/fiche-reception-blanche-noire-v3-relance-v4.json",
                   "### Liste fermée du code — analyse secondaire (code v5)"),
}
V3 = {
    "principale": ("20261103-072723-analyse-principale-r1-r2-v1", "analyse-principale-r1-r2-v1", "0587c398"),
    "par_episode": ("20261103-072805-analyse-par-episode-v1", "analyse-par-episode-v1", "79f2a758"),
    "secondaire": ("20261103-072840-analyse-blanche-noire-v3", "analyse-blanche-noire-v3", "91f711c6"),
}
ADDENDUM = "prereg/addendum-1-gardes-analyses-r1-v4-v1.md"
ADDENDUM_SHA = "a5ac6632691a0d12f777b14fa31ca432da35a57a1145fd3b00e147fd3d12fa0a"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(repo, *args, binaire=False):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=True)
    return r.stdout if binaire else r.stdout.decode()


def compagnon(p):
    c = Path(str(p) + ".sha256")
    if not c.exists():
        return None
    return c.read_text().split()[0]


ok_global = True


def constat(nom, vrai, detail=""):
    global ok_global
    ok_global &= bool(vrai)
    print(f"[{'OK' if vrai else 'ÉCART'}] {nom}" + (f" — {detail}" if detail else ""))


print("# 1. Empreintes des fichiers de sortie contre leurs compagnons (arbre e13e5e28)")
for d in ("runs", "diag", "journaux"):
    for p in sorted((ARBRE / d).rglob("*")):
        if p.is_file() and not p.name.endswith(".sha256"):
            h = sha(p)
            constat(f"{p.relative_to(ARBRE)} {h}", compagnon(p) == h)

print("\n# 2. Empreintes attendues (consigne) et rattachement résultat → manifeste")
for nom, t in V4.items():
    run, sortie, pref_res, pref_man, *_ = t
    hr = sha(ARBRE / "diag" / run / f"{sortie}.json")
    hm = sha(ARBRE / "runs" / run / "manifeste.json")
    constat(f"v4 {nom} résultat {hr[:8]}… = {pref_res}…", hr.startswith(pref_res))
    constat(f"v4 {nom} manifeste {hm[:8]}… = {pref_man}…", hm.startswith(pref_man))
    res = json.loads((ARBRE / "diag" / run / f"{sortie}.json").read_text())
    constat(f"v4 {nom} résultat.manifeste_sha256 = sha du manifeste", res.get("manifeste_sha256") == hm)
for nom, (run, sortie, pref_man) in V3.items():
    hm = sha(ARBRE / "runs" / run / "manifeste.json")
    hr = sha(ARBRE / "diag" / run / f"{sortie}.json")
    res = json.loads((ARBRE / "diag" / run / f"{sortie}.json").read_text())
    constat(f"v3 {nom} manifeste {hm[:8]}… = {pref_man}… (liste close K2)", hm.startswith(pref_man))
    constat(f"v3 {nom} résultat {hr} rattaché", res.get("manifeste_sha256") == hm)
    # identité avec la branche de la course v3
    blob = git(ARBRE, "show", f"adc1be82:runs/{run}/manifeste.json", binaire=True)
    constat(f"v3 {nom} manifeste identique à canal/conv-audit-n04 (adc1be82)", hashlib.sha256(blob).hexdigest() == hm)

print("\n# 3. Textes qui gouvernent : main 759d0103 = arbre de lecture = compagnons")
for chemin in [t[5] for t in V4.values()] + [ADDENDUM, "prereg/R1-addendum-relance-v4.md",
                                             "docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/fiche-reception-r1-v4-v2.md",
                                             V4["principale"][7], V4["secondaire"][7]]:
    hmain = hashlib.sha256(git(MAIN, "show", f"{COMMIT_MAIN}:{chemin}", binaire=True)).hexdigest() if chemin.startswith(("prereg/analyse", "prereg/addendum", "prereg/R1-add", "docs/")) else None
    if (ARBRE / chemin).exists():
        harb, comp = sha(ARBRE / chemin), compagnon(ARBRE / chemin)
    else:  # absent de la branche des analyses : lu sur main seulement
        harb = hmain
        comp = git(MAIN, "show", f"{COMMIT_MAIN}:{chemin}.sha256").split()[0]
        print(f"    ({chemin} absent de l'arbre e13e5e28 : lu sur main {COMMIT_MAIN})")
    constat(f"{chemin} arbre {harb} compagnon={'égal' if comp == harb else comp} main={'égal' if hmain in (None, harb) else hmain}",
            harb is not None and comp == harb and (hmain is None or hmain == harb))

print("\n# 4. Manifestes v4 : commande gelée, texte, décisif, arbre propre, addendum, commit")
for nom, t in V4.items():
    run, sortie, _, _, cmd, texte, texte_sha, fiche, titre = t
    m = json.loads((ARBRE / "runs" / run / "manifeste.json").read_text())
    constat(f"{nom} commande = {cmd}", m["commande"] == cmd)
    constat(f"{nom} preenregistrement = {texte} {texte_sha[:8]}…", m["preenregistrement"] == {"chemin": texte, "sha256": texte_sha})
    constat(f"{nom} decisif, depot_propre", m["decisif"] is True and m["depot_propre"] is True)
    constat(f"{nom} config.addendum = addendum scellé", m["config"]["addendum"] == {"chemin": ADDENDUM, "sha256": ADDENDUM_SHA})
    constat(f"{nom} config.fiche = {fiche}", m["config"]["fiche"] == fiche if isinstance(m["config"]["fiche"], str) else m["config"]["fiche"].get("chemin") == fiche, json.dumps(m["config"]["fiche"])[:120])
    hfiche = sha(ARBRE / fiche)
    constat(f"{nom} config.fiche_sha256 = sha de la fiche sur disque {hfiche[:8]}…", m["config"].get("fiche_sha256") == hfiche)
    c = m["commit"]
    constat(f"{nom} commit {c[:8]} descend du commit cité {COMMIT_CITE[:8]}",
            subprocess.run(["git", "-C", str(ARBRE), "merge-base", "--is-ancestor", COMMIT_CITE, c]).returncode == 0)
    diff = subprocess.run(["git", "-C", str(ARBRE), "diff", "--quiet", COMMIT_CITE, c, "--", "src", "tests"]).returncode
    constat(f"{nom} src et tests identiques entre commit cité et {c[:8]}", diff == 0)
    # liste fermée du bloc de l'addendum, recalculée sur le commit du manifeste
    add = git(MAIN, "show", f"{COMMIT_MAIN}:{ADDENDUM}")
    i = add.index("\n" + titre + "\n") + 1
    j = add.find("\n### ", i + 1)
    j2 = add.find("\nEmpreinte des constantes", i + 1)
    fin = min(x for x in (j, j2, len(add)) if x > 0)
    bloc = add[i:fin]
    paires = re.findall(r"`([^`]+\.py)` : `([0-9a-f]{64})`", bloc)
    ecarts = []
    for chemin, attendu in paires:
        h = hashlib.sha256(git(ARBRE, "show", f"{c}:{chemin}", binaire=True)).hexdigest()
        if h != attendu:
            ecarts.append(chemin)
    constat(f"{nom} liste fermée du bloc ({len(paires)} fichiers) égale au commit {c[:8]}", paires and not ecarts, ", ".join(ecarts))
    print(f"    graines : {sorted(m['graines'])}")
    print(f"    créé le : {m['cree_le']}")

print("\n# 5. Graines v4 = graines v3 (Plan, point 4 de l'addendum)")
for nom in V4:
    g4 = json.loads((ARBRE / "runs" / V4[nom][0] / "manifeste.json").read_text())["graines"]
    g3 = json.loads((ARBRE / "runs" / V3[nom][0] / "manifeste.json").read_text())["graines"]
    constat(f"{nom} graines identiques v3/v4", g4 == g3)

print("\n# 6. Tentative de 12:11:25Z : aucun manifeste ni sortie, dans aucun commit")
noms = git(ARBRE, "log", "--all", "--name-only", "--format=", "--", "runs", "diag").split()
suspects = sorted({n for n in noms if "20261106-1211" in n or "20261106-1212" in n})
constat("aucun chemin runs/ ou diag/ 20261106-1211*/1212* dans l'historique", not suspects, ", ".join(suspects))
print("    journal de la tentative :", repr((ARBRE / "journaux/20261106-121125-analyse-principale-r1-r2-v1.log").read_text()))
runs_cit = []
for p in sorted((ARBRE / "runs").glob("*/manifeste.json")):
    b = p.read_bytes()
    if any(x.encode() in b for x in (ADDENDUM, ADDENDUM_SHA, "analyse-principale-r1-r2-v1.md", "analyse-par-episode-v1.md",
                                     "analyse-blanche-noire-v3.md", "8e2679526b27", "26a3ff72e3a3", "1f6a6da2c551")):
        runs_cit.append(p.parent.name)
print("    manifestes de l'arbre qui citent un texte ou l'addendum :", runs_cit)

print("\n# 7. Sorties : reception_v4, passages (K2), sous_addendum (K3)")
for nom, t in V4.items():
    run, sortie = t[0], t[1]
    r = json.loads((ARBRE / "diag" / run / f"{sortie}.json").read_text())["resultat"]
    rv = r.get("reception_v4", {})
    constat(f"{nom} reception_v4.run_rejeu = 20261105-021737-r1-v4-rejeu-reel", rv.get("run_rejeu") == "20261105-021737-r1-v4-rejeu-reel")
    constat(f"{nom} reception_v4 texte = addendum v4 0f10881b…", rv.get("texte") == {"chemin": "prereg/R1-addendum-relance-v4.md", "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"})
    constat(f"{nom} reception_v4 commande rejeu_activations_v4", rv.get("commande") == "python -m controle_ia.runs_nuit.rejeu_activations_v4")
    tok = rv.get("tokenisation", {})
    constat(f"{nom} table_sha256 = sceau table = {rv.get('table', {}).get('sha256')}", tok.get("table_sha256") == rv.get("table", {}).get("sha256") and compagnon(ARBRE / "prereg/R1-table-tokenisation-v4.json") == tok.get("table_sha256"))
    constat(f"{nom} tokenisation.addendum", tok.get("addendum") == "prereg/R1-addendum-relance-v4.md")
    rep = rv.get("reparation", {})
    b_rep = git(ARBRE, "show", f"e13e5e28:{rep.get('chemin')}", binaire=True)
    c_rep = git(ARBRE, "show", f"e13e5e28:{rep.get('chemin')}.sha256").split()[0]
    constat(f"{nom} réparation sceau {rep.get('sha256', '')[:8]}… = compagnon et octets au commit e13e5e28 (git show)", c_rep == rep.get("sha256") == hashlib.sha256(b_rep).hexdigest())
    table = json.loads((ARBRE / "prereg/R1-table-tokenisation-v4.json").read_text())
    constat(f"{nom} table cite le sceau de la réparation", table.get("resultat_reparation_sha256") == rep.get("sha256"))
    man_rejeu = ARBRE / "runs/20261105-021737-r1-v4-rejeu-reel/manifeste.json"
    if man_rejeu.exists():
        constat(f"{nom} reception_v4.manifeste_sha256 = manifeste du rejeu sur disque", sha(man_rejeu) == rv.get("manifeste_sha256"))
    else:
        print(f"    (manifeste du rejeu non extrait dans l'arbre de lecture : comparé par git show)")
        h = hashlib.sha256(git(ARBRE, "show", f"e13e5e28:runs/20261105-021737-r1-v4-rejeu-reel/manifeste.json", binaire=True)).hexdigest()
        constat(f"{nom} reception_v4.manifeste_sha256 = manifeste du rejeu (git show)", h == rv.get("manifeste_sha256"))
    lien = r["lien_au_preenregistrement"]
    constat(f"{nom} lien.addendum = addendum scellé", lien["addendum"]["chemin"] == ADDENDUM and lien["addendum"]["sha256"] == ADDENDUM_SHA)
    pas = lien["passages"]
    print(f"    passages : {json.dumps(pas, ensure_ascii=False)}")
    permis = {V3[k][0] for k in V3} | {V4[k][0] for k in V4 if k != nom}
    tol = [x if isinstance(x, str) else (x.get("run") or x.get("run_id") or json.dumps(x)) for x in pas["toleres"]]
    constat(f"{nom} passages.toleres dans la liste close", all(any(p in t for p in permis) for t in tol), str(tol))
    print(f"    version : {r['version']} ; statut : {r['statut']} ; mode : {r.get('mode')}")
r = json.loads((ARBRE / "diag" / V4["par_episode"][0] / "analyse-par-episode-v1.json").read_text())["resultat"]
sa = r.get("principale", {}).get("sous_addendum")
print("    principale (par épisode) :", json.dumps({k: v for k, v in r.get("principale", {}).items()}, ensure_ascii=False)[:1500])
hp = sha(ARBRE / "diag" / V4["principale"][0] / "analyse-principale-r1-r2-v1.json")
mp = json.loads((ARBRE / "runs" / V4["par_episode"][0] / "manifeste.json").read_text())["config"]
constat("K3 config.principale = sortie v8 de la course v4", V4["principale"][0] in json.dumps(mp.get("principale")) and mp.get("principale_sha256") == hp, f"{mp.get('principale')} {mp.get('principale_sha256')}")
constat("K3 sous_addendum présent et cite code v8, addendum, même rejeu",
        bool(sa) and "code v8" in json.dumps(sa, ensure_ascii=False) and ADDENDUM_SHA in json.dumps(sa) and "20261105-021737-r1-v4-rejeu-reel" in json.dumps(sa))

print("\nBILAN :", "aucun écart" if ok_global else "ÉCART(S) — voir lignes ÉCART")
