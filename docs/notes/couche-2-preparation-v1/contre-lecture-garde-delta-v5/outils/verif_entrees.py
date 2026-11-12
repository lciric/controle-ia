"""Contre-lecture v5 : GD4-03, GD4-04, GD4-05, GD4-06 — essais d'entrées propres au contre-lecteur.
Chaque essai lance la copie conforme du script (python3 -I -B) dans un dossier neuf, petits réglages ; on lit le code de
retour et le premier message « refus : … ». « erreur brute » = code ≠ 0 sans « refus : ».
Git : simulé par un faux exécutable `git` placé en tête du PATH (aucun dépôt créé).
Usage : python3 -I -B verif_entrees.py SCRIPT DOSSIER_NEUF SORTIE.json
"""
import json
import os
import subprocess
import sys

SCRIPT, DOSSIER, SORTIE = sys.argv[1:4]
os.makedirs(DOSSIER)
os.chdir(DOSSIER)
PETIT = ["--repetitions", "100", "--tailles", "6", "--K", "10", "--taux", "0.01", "--biais", "0", "--deltas", "0.05", "--m", "8",
         "--sans-n80", "--comparateurs", "1"]


def ecrire(nom, texte, mode="w"):
    with open(nom, mode, encoding=None if "b" in mode else "utf-8") as f:
        f.write(texte)


ids = [f"u{i}" for i in range(6)]
G = [0.0, 0.1, -0.1, 0.0, 0.1, 0.0]
ecrire("g1.json", json.dumps({"ecarts": G}))
ecrire("g2.json", json.dumps({"ecarts": [0.0, 0.0, 0.1, -0.1, 0.0, 0.1]}))
ecrire("c1.json", json.dumps({"rA": [0.5] * 6, "rB": [0.4] * 6}))
ecrire("c2.json", json.dumps({"rA": [0.6] * 6, "rB": [0.4] * 6}))
ecrire("g1_espaces.json", json.dumps({"ecarts": G}, indent=2))  # mêmes valeurs, autre encodage
ecrire("g1.csv", "ecart\n" + "\n".join(str(x) for x in G) + "\n")  # mêmes valeurs en CSV
ecrire("g1_zeros.json", json.dumps({"ecarts": [0.0, 0.10, -0.10, 0.0, 0.10, 0.0]}).replace("0.1", "0.100"))
os.link("g1.json", "g1_dur.json")
os.symlink("g1.json", "g1_lien.json")
ecrire("csv_pleine_chasse.csv", "ecart\n０.０５\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_long.csv", "ecart\n0." + "0" * 70 + "5\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_souligne_debut.csv", "ecart\n_0.05\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_point_virgule.csv", "ecart\n0;05\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_guillemets_ok.csv", 'ecart\n"0.05"\n0.0\n0.0\n0.0\n0.0\n0.0\n')
ecrire("csv_bom.csv", "﻿ecart\n0.05\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_crlf.csv", "ecart\r\n0.05\r\n0.0\r\n0.0\r\n0.0\r\n0.0\r\n0.0\r\n")
ecrire("csv_espace_insecable.csv", "ecart\n 0.05\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_infinity.csv", "ecart\nInfinity\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_moins_nan.csv", "ecart\n-nan\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("csv_sous_flux.csv", "ecart\n1e-400\n0.0\n0.0\n0.0\n0.0\n0.0\n")
ecrire("json_chaine.json", json.dumps({"ecarts": ["0.05", 0, 0, 0, 0, 0]}))
ecrire("json_bool.json", '{"ecarts": [true, 0, 0, 0, 0, 0]}')
ecrire("json_imbrique.json", '{"ecarts": [[0.1], 0, 0, 0, 0, 0]}')
ecrire("json_infini.json", '{"ecarts": [Infinity, 0, 0, 0, 0, 0]}')
ecrire("json_grand.json", '{"ecarts": [1e400, 0, 0, 0, 0, 0]}')
ecrire("json_ids_zwsp.json", json.dumps({"ecarts": G, "unite": ["​"] + ids[1:]}))
ecrire("json_ids_espace.json", json.dumps({"ecarts": G, "unite": [" "] + ids[1:]}))
ecrire("json_ids_doubles.json", json.dumps({"ecarts": G, "unite": ["u0"] + ids[:5]}))
ecrire("g_ids.json", json.dumps({"ecarts": G, "unite": ids}))
ecrire("c_ids_ordre.json", json.dumps({"rA": [0.5] * 6, "rB": [0.4] * 6, "unite": ids[::-1]}))
ecrire("c_ids.json", json.dumps({"rA": [0.5] * 6, "rB": [0.4] * 6, "unite": ids}))
ecrire("c_ecarts_forme.json", json.dumps({"ecarts": [0.1, 0.0, 0.2, 0.1, 0.0, 0.1]}))
os.mkdir("dossier.json")
ecrire("latin1.csv", "ecart\n0.05\n0.0\n0.0\n0.0\n0.0\n\xe9\n".encode("latin-1"), "wb")

E = ["--effectif-attendu", "6"]
S = ["--contraste-synthetique-de-secours"]
essais = [
    # GD4-03
    ("csv chiffres pleine chasse", "GD4-03", ["--ecarts", "csv_pleine_chasse.csv"] + S + E, "refus"),
    ("csv nombre de 73 caractères", "GD4-03", ["--ecarts", "csv_long.csv"] + S + E, "refus"),
    ("csv souligné en tête", "GD4-03", ["--ecarts", "csv_souligne_debut.csv"] + S + E, "refus"),
    ("csv point-virgule", "GD4-03", ["--ecarts", "csv_point_virgule.csv"] + S + E, "refus"),
    ("csv Infinity", "GD4-03", ["--ecarts", "csv_infinity.csv"] + S + E, "refus"),
    ("csv -nan", "GD4-03", ["--ecarts", "csv_moins_nan.csv"] + S + E, "refus"),
    ("csv espace insécable", "GD4-03", ["--ecarts", "csv_espace_insecable.csv"] + S + E, "refus"),
    ("csv entre guillemets (sain)", "GD4-03 sain", ["--ecarts", "csv_guillemets_ok.csv"] + S + E, "accepte"),
    ("csv BOM (sain)", "GD4-03 sain", ["--ecarts", "csv_bom.csv"] + S + E, "accepte"),
    ("csv CRLF (sain)", "GD4-03 sain", ["--ecarts", "csv_crlf.csv"] + S + E, "accepte"),
    ("csv 1e-400 (lu 0)", "GD4-03 note", ["--ecarts", "csv_sous_flux.csv"] + S + E, "accepte"),
    ("csv latin-1", "GD4-03", ["--ecarts", "latin1.csv"] + S + E, "refus"),
    ("json chaîne dans la liste", "GD4-03", ["--ecarts", "json_chaine.json"] + S + E, "refus"),
    ("json true dans la liste", "GD4-03", ["--ecarts", "json_bool.json"] + S + E, "refus"),
    ("json liste imbriquée", "GD4-03", ["--ecarts", "json_imbrique.json"] + S + E, "refus"),
    ("json Infinity", "GD4-03", ["--ecarts", "json_infini.json"] + S + E, "refus"),
    ("json 1e400", "GD4-03", ["--ecarts", "json_grand.json"] + S + E, "refus"),
    ("--alpha .05 (sain)", "GD4-03 sain", ["--alpha", ".05"], "accepte"),
    ("--alpha 5e-2 (sain)", "GD4-03 sain", ["--alpha", "5e-2"], "accepte"),
    ("--alpha 0x1p-4", "GD4-03", ["--alpha", "0x1p-4"], "refus"),
    ("--alpha '0.05\\n'", "GD4-03", ["--alpha", "0.05\n"], "refus"),
    ("--deltas ０.05 (pleine chasse)", "GD4-03", ["--deltas", "０.05"], "refus"),
    ("--graine 1.0", "GD4-03", ["--graine", "1.0"], "refus"),
    ("--graine +5 (sain)", "GD4-03 sain", ["--graine", "+5"], "accepte"),
    ("--tailles 6,,6", "GD4-03", ["--tailles", "6,,6"], "refus"),
    ("--effectif-attendu 6.0", "GD4-03", ["--ecarts", "g1.json"] + S + ["--effectif-attendu", "6.0"], "refus"),
    ("--m-fiches 2.0", "GD4-03", ["--lecture-ebh", "A", "--m-fiches", "2.0"], "refus"),
    # GD4-04
    ("lien dur (même contenu)", "GD4-04", ["--ecarts", "g1.json,g1_dur.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("lien symbolique", "GD4-04", ["--ecarts", "g1.json,g1_lien.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("chemin avec ../", "GD4-04", ["--ecarts", "g1.json,../" + os.path.basename(DOSSIER) + "/g1.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("mêmes valeurs, JSON réindenté", "GD4-04 reste", ["--ecarts", "g1.json,g1_espaces.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("mêmes valeurs, CSV et JSON", "GD4-04 reste", ["--ecarts", "g1.json,g1.csv", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("mêmes valeurs, 0.100 contre 0.1", "GD4-04 reste", ["--ecarts", "g1.json,g1_zeros.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus"),
    ("forme ecarts en contraste", "GD4-04 reste", ["--ecarts", "g1.json", "--ecarts-contraste", "c_ecarts_forme.json"] + E, "refus"),
    ("distincts (sain)", "GD4-04 sain", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "accepte"),
    # GD4-06
    ("--ecarts ' '", "GD4-06", ["--ecarts", " "] + S + E, "refus"),
    ("--ecarts ,g1.json", "GD4-06", ["--ecarts", ",g1.json"] + S + E, "refus"),
    ("dossier", "GD4-06", ["--ecarts", "dossier.json"] + S + E, "refus"),
    ("identifiant espace seule", "GD4-06", ["--ecarts", "json_ids_espace.json"] + S + E, "refus"),
    ("identifiant espace de largeur nulle", "GD4-06 note", ["--ecarts", "json_ids_zwsp.json"] + S + E, "refus"),
    ("identifiants doublés", "GD4-06", ["--ecarts", "json_ids_doubles.json"] + S + E, "refus"),
    ("identifiants dans un autre ordre", "GD3-02", ["--ecarts", "g_ids.json", "--ecarts-contraste", "c_ids_ordre.json"] + E, "refus"),
    ("identifiants sur un seul fichier", "GD3-02", ["--ecarts", "g_ids.json", "--ecarts-contraste", "c1.json"] + E, "refus"),
    ("identifiants égaux (sain)", "GD3-02 sain", ["--ecarts", "g_ids.json", "--ecarts-contraste", "c_ids.json"] + E, "accepte"),
    ("secours et contraste réel", "GD4-06", ["--ecarts", "g1.json", "--ecarts-contraste", "c1.json"] + S + E, "refus"),
    ("effet logit, τ + biais = 1", "GD4-06", ["--effet-unite-a", "1", "--taux", "0.98", "--biais", "0.02", "--deltas", "0.01"], "refus"),
    ("--taux 0.0", "GD4-06", ["--taux", "0.0"], "refus"),
    # options e-BH
    ("--lecture-ebh vide", "e-BH", ["--lecture-ebh", ""], "refus"),
    ("--lecture-ebh ' A , B ' (sain)", "e-BH sain", ["--lecture-ebh", " A , B "], "accepte"),
    ("--m-fiches 0", "e-BH", ["--lecture-ebh", "A", "--m-fiches", "0"], "refus"),
    ("--fiches-nulles -1", "e-BH", ["--lecture-ebh", "A", "--fiches-nulles", "-1"], "refus"),
    ("--fiches-nulles sans lecture", "e-BH", ["--fiches-nulles", "2"], "refus"),
    ("--lecture-ebh B, k = 1,3 (sain)", "e-BH sain", ["--lecture-ebh", "B", "--comparateurs", "1,3", "--fiches-nulles", "1"], "accepte"),
]


def lancer(args, env=None):
    a = list(args)
    base = PETIT[:]
    # les options passées remplacent celles de PETIT
    for i in range(0, len(a)):
        if a[i].startswith("--") and a[i] in base:
            j = base.index(a[i])
            if j + 1 < len(base) and not base[j + 1].startswith("--"):
                del base[j:j + 2]
            else:
                del base[j]
    r = subprocess.run([sys.executable, "-I", "-B", SCRIPT] + base + a, capture_output=True, text=True, env=env, timeout=600)
    lignes = [l for l in r.stderr.splitlines() if l.strip()]
    msg = lignes[-1] if lignes else ""
    return r.returncode, msg, r.stdout


res, n_ref, n_brut, nc = [], 0, 0, []
for nom, constat, args, attendu in essais:
    code, msg, out = lancer(args)
    obtenu = "accepte" if code == 0 else ("refus" if msg.startswith("refus : ") else "erreur brute")
    n_ref += obtenu == "refus"
    n_brut += obtenu == "erreur brute"
    detail = None
    if code == 0 and out:
        d = json.loads(out)
        detail = {"lois": list(d["lois"])[:3], "fichiers": [(x["chemin"], x.get("forme"), x["role"]) for x in d.get("fichiers_observes", [])],
                  "secours_ecrit": "contraste_synthetique_de_secours" in d["reglages"]}
        if "csv_sous_flux" in " ".join(args):
            detail["moyenne"] = d["fichiers_observes"][0]["moyenne_brute"]
    ok = obtenu == attendu
    if not ok:
        nc.append(nom)
    res.append({"essai": nom, "constat": constat, "arguments": args, "attendu": attendu, "obtenu": obtenu, "code": code,
                "message": msg[:300], "detail": detail, "conforme": ok})

# --- GD4-05 : git simulé (faux exécutable), aucun dépôt
os.mkdir("fauxgit")
FAUX = r'''#!/bin/sh
case "$1 $2" in
 "rev-parse --show-toplevel") [ -n "$TOP_ERR" ] && { echo "$TOP_ERR" >&2; exit ${TOP_CODE:-128}; }; echo /depot; exit 0;;
 "rev-parse --verify") [ -n "$HEAD_ERR" ] && { echo "$HEAD_ERR" >&2; exit 128; }; printf '%s\n' "${HEAD_SORTIE:-0123456789abcdef0123456789abcdef01234567}"; exit 0;;
 "ls-files --error-unmatch") exit ${LS_CODE:-0};;
 "status --porcelain") [ -n "$ST_CODE" ] && { echo "fatal: status" >&2; exit $ST_CODE; }; printf '%s' "$ST_SORTIE"; exit 0;;
esac
exit 0
'''
ecrire("fauxgit/git", FAUX)
os.chmod("fauxgit/git", 0o755)
cas_git = [
    ("hors dépôt", {"TOP_ERR": "fatal: not a git repository (or any of the parent directories): .git"}, "hors dépôt git"),
    ("propriétaire douteux", {"TOP_ERR": "fatal: detected dubious ownership in repository at '/depot'"}, "inconnu"),
    ("sans commit", {"HEAD_ERR": "fatal: Needed a single revision"}, "inconnu"),
    ("HEAD littéral", {"HEAD_SORTIE": "HEAD"}, "inconnu"),
    ("ls-files code 128", {"LS_CODE": "128"}, "inconnu"),
    ("status code 128", {"ST_CODE": "128"}, "inconnu"),
    ("non suivi, non ignoré", {"LS_CODE": "1", "ST_SORTIE": "?? script.py"}, "?? script.py"),
    ("ignoré", {"LS_CODE": "1", "ST_SORTIE": ""}, "non suivi (ignoré ou hors arbre)"),
    ("modifié", {"ST_SORTIE": " M script.py"}, "M script.py"),
    ("propre", {}, "commité, non modifié"),
    ("rev-parse code 1 sans message", {"TOP_ERR": " ", "TOP_CODE": "1"}, "inconnu"),
]
gits = []
for nom, env_sup, attendu in cas_git:
    env = {"PATH": os.path.abspath("fauxgit") + ":/usr/bin:/bin", **env_sup}
    code, msg, out = lancer([], env=env)
    d = json.loads(out) if code == 0 else {}
    etat = d.get("etat_du_script", f"code {code} {msg}")
    ok = etat.startswith(attendu)
    gits.append({"cas": nom, "attendu": attendu, "obtenu": etat, "commit": d.get("commit"), "conforme": ok})
    if not ok:
        nc.append("git " + nom)
code, msg, out = lancer([], env={"PATH": "/nonexistent"})
d = json.loads(out) if code == 0 else {}
gits.append({"cas": "git absent", "obtenu": d.get("etat_du_script", msg), "conforme": d.get("etat_du_script", "").startswith("inconnu")})

# --- R12 : refus d'écraser ; refus si seul le journal existe (passage interrompu)
code1, m1, _ = lancer(["--sortie", "p.json"])
code2, m2, _ = lancer(["--sortie", "p.json"])
ecrire("q-journal.txt", "reste d'un passage interrompu\n")
code3, m3, _ = lancer(["--sortie", "q.json"])
man = json.load(open("manifeste-p.json"))
import hashlib
h = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
r12 = {"premier": code1, "second": [code2, m2[:160]], "journal_seul": [code3, m3[:160]],
       "manifeste_empreintes_justes": man["fichiers"] == {"p.json": h("p.json"), "p-journal.txt": h("p-journal.txt")},
       "manifeste_commit": man["script"].get("commit"), "manifeste_etat": man["script"].get("etat_du_script")}

bilan = {"script": SCRIPT, "script_sha256": h(SCRIPT), "essais": len(res), "refus_nommes": n_ref, "erreurs_brutes": n_brut,
         "non_conformes": nc, "resultats": res, "git_simule": gits, "R12": r12}
os.chdir("..")
json.dump(bilan, open(SORTIE, "x"), indent=1, ensure_ascii=False)
for x in res:
    print(("OK " if x["conforme"] else "NC ") + x["essai"], "→", x["obtenu"], x["message"][:110], x["detail"] if x["detail"] else "")
for g in gits:
    print(("OK " if g["conforme"] else "NC ") + "git", g["cas"], "→", g["obtenu"], g.get("commit"))
print(r12)
print({k: bilan[k] for k in ("essais", "refus_nommes", "erreurs_brutes", "non_conformes")})
