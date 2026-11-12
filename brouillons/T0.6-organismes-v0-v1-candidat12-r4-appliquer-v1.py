"""Applique les couples de la révision 4 de T0.6 candidat 12 (révision 3 → révision 4) et écrit le texte et son journal.

Usage (depuis la racine du dépôt) :
  .venv/bin/python -I -B brouillons/T0.6-organismes-v0-v1-candidat12-r4-appliquer-v1.py \
      --couples brouillons/T0.6-organismes-v0-v1-candidat12-r4-couples-v1.json \
      --variante brouillons/T0.6-organismes-v0-v1-candidat12-r4-couples-variante-a-v1.json \
      --sortie brouillons/T0.6-organismes-v0-v1-candidat12-r4.md \
      --journal brouillons/T0.6-organismes-v0-v1-candidat12-r4-journal-v1.md \
      --temp <dossier temporaire neuf> --heure "<sortie de date -u>" [--code-1609a4bf <dossier contenant src/ du commit 1609a4bf>]

Règles :
  - la révision 3 et le fichier des couples de la contre-lecture 3 sont vérifiés par leur sha256 avant tout ;
  - chaque couple Y du fichier doit être égal à l'octet au couple de même identifiant de la contre-lecture 3 ;
  - les couples sont appliqués dans l'ordre ; chaque « ancien » doit être présent exactement une fois au moment de son
    application, sinon arrêt sans rien écrire ; la variante (a) est appliquée de même, dans le dossier temporaire ;
  - le texte et le journal ne sont écrits que si tout passe, et jamais par-dessus un fichier existant (R12) ;
  - contrôles écrits au journal : marqueurs restants ; `controle_ia.prereg.problemes` (réel, puis à valeurs factices
    pour les marqueurs laissés) ; les huit citations lues par `controles` du lanceur v13 (mêmes motifs, `grep -cE`) ;
    les quatre chemins extraits comme le lanceur (`sed`) ; la forme de la citation de l'amorce (l. 143 du lanceur) ;
    avec `--code-1609a4bf` : empreinte canonique de la configuration, `exiger_citations_t06` et `exiger_prereg_scelle`
    joués sur une copie à valeurs factices dans le dossier temporaire.
Aucun réseau, aucun modèle ; git en lecture seule (`git show`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

SOURCE = "brouillons/T0.6-organismes-v0-v1-candidat12-r3.md"
SHA_SOURCE = "c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331"
CL3 = "prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3-couples-v1.json"
SHA_CL3 = "e3846ae5d91cf9de5b437710188d514ae1e563ce610e306833c0c582024a8e54"
COMMIT = "1609a4bf2c1572f72bb8542d81d963ac6a8481c4"
CONFIG_SOURCE = "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json"
AMORCE = "scripts/amorce_instance_t06_v11.sh"
LAISSES = {"b": ("MOT_LAZAR_GO_7B", "DECISION_LAZAR_ECART_DT4_R2041"),
           "a": ("MOT_LAZAR_GO_7B", "DECISION_LAZAR_ECART_DT4_R2041", "MOT_LAZAR_GRANDEURS_COUT_7A")}
# motifs de `controles` (scripts/lancer_t06_v13.sh au commit 1609a4bf, l. 129-131), recopiés tels quels (grep -E)
MOTIFS = ["Entropie : `[0-9]+`", "Configuration de T0.6 \\(empreinte canonique\\) : `[0-9a-f]{64}`",
          "Tâches d'évaluation de T0.6 : `[0-9a-f]{64}`", "Tests attendus : `[0-9]+`",
          "Chemin de la configuration de T0.6 : `[^`]+`", "Chemin des tâches d'évaluation de T0.6 : `[^`]+`",
          "Chemin des tâches de distillation de T0.6 : `[^`]+`", "Chemin des consignes de P3 : `[^`]+`"]
CLES_CHEMINS = ["Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6",
                "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str) -> None:
    print("ARRÊT, rien n'est écrit : " + msg, file=sys.stderr)
    sys.exit(2)


def section_de(texte: str, pos: int) -> str:
    titres = [m for m in re.finditer(r"^## +(.+?)\s*$", texte[:pos], flags=re.M)]
    return titres[-1].group(1) if titres else "en-tête (avant la première section)"


def appliquer(texte: str, couples: list[dict]) -> tuple[str, list[dict]]:
    journal = []
    for k, c in enumerate(couples, start=1):
        n = texte.count(c["ancien"])
        if n != 1:
            arret(f"couple {k} ({c['id']}) : « ancien » présent {n} fois")
        pos = texte.index(c["ancien"])
        journal.append({"rang": k, "ligne": texte.count("\n", 0, pos) + 1, "section": section_de(texte, pos), **c})
        texte = texte.replace(c["ancien"], c["nouveau"], 1)
        if texte.count(c["nouveau"]) < 1:
            arret(f"couple {k} : « nouveau » absent après application")
    return texte, journal


def remplir_factice(texte: str, noms) -> str:
    for nom in noms:
        texte = texte.replace(f"<<{nom}>>", f"FACTICE-{nom} (R-0000, essai à blanc)")
    return texte


def controles_chaine(chemin: Path) -> dict:
    r = {}
    r["citations"] = []
    for motif in MOTIFS:
        out = subprocess.run(["grep", "-cE", motif, str(chemin)], capture_output=True, text=True)
        lignes = subprocess.run(["grep", "-nE", motif, str(chemin)], capture_output=True, text=True).stdout.splitlines()
        forme = [l.split(":", 1)[0] + " : " + re.search(motif, l.split(":", 1)[1]).group(0) for l in lignes]
        r["citations"].append((motif, out.stdout.strip(), forme))
    r["chemins"] = []
    for cle in CLES_CHEMINS:
        out = subprocess.run(["sed", "-n", f"s/.*{cle} : `\\([^`]*\\)`.*/\\1/p", str(chemin)], capture_output=True, text=True)
        r["chemins"].append((cle, out.stdout.strip()))
    return r


def forme_amorce(chemin: Path, empreinte: str) -> bool:
    cmd = f"tr '\\n' ' ' < '{chemin}' | tr -s ' ' | grep -qF '`{AMORCE}` (`{empreinte}`'"
    return subprocess.run(["bash", "-c", cmd]).returncode == 0


def bloc(t: str) -> str:
    return "\n".join("    " + l for l in t.split("\n"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--depot", default=".")
    ap.add_argument("--couples", required=True)
    ap.add_argument("--variante", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--journal", required=True)
    ap.add_argument("--temp", required=True)
    ap.add_argument("--heure", required=True)
    ap.add_argument("--code-1609a4bf", default=None)
    a = ap.parse_args()
    depot = Path(a.depot).resolve()
    temp = Path(a.temp)
    temp.mkdir(parents=True, exist_ok=True)
    sortie, journal_p = Path(a.sortie), Path(a.journal)
    for p in (sortie, journal_p):
        if p.exists():
            arret(f"{p} existe déjà (R12)")

    src = (depot / SOURCE).read_bytes()
    if sha(src) != SHA_SOURCE:
        arret("empreinte de la révision 3 différente")
    cl3_b = (depot / CL3).read_bytes()
    if sha(cl3_b) != SHA_CL3:
        arret("empreinte des couples de la contre-lecture 3 différente")
    cl3 = {c["id"]: c for c in json.loads(cl3_b.decode("utf-8"))}
    docs = {}
    for nom, chemin in (("principal", a.couples), ("variante", a.variante)):
        b = Path(chemin).read_bytes()
        d = json.loads(b.decode("utf-8"))
        if d["source_sha256"] != SHA_SOURCE or d["couples_contre_lecture_3_sha256"] != SHA_CL3:
            arret(f"{chemin} : source ou couples de la contre-lecture 3 inattendus")
        for c in d["couples"]:
            if c["id"].startswith("Y"):
                ref = cl3.get(c["id"])
                if ref is None or ref["ancien"] != c["ancien"] or ref["nouveau"] != c["nouveau"]:
                    arret(f"{chemin} : couple {c['id'][:4]} différent de celui de la contre-lecture 3")
        docs[nom] = (chemin, sha(b), d)

    texte_r3 = src.decode("utf-8")
    texte, jr = appliquer(texte_r3, docs["principal"][2]["couples"])
    texte_a, _ = appliquer(texte_r3, docs["variante"][2]["couples"])
    var = docs["principal"][2]["variante"]

    # --- contrôles ---------------------------------------------------------------------------------------------
    sys.path.insert(0, str(depot / "src"))
    from controle_ia import prereg  # noqa: E402

    resultats = {}
    for nom, t, v in (("r4", texte, var), ("variante (a)", texte_a, docs["variante"][2]["variante"])):
        brut = temp / f"{nom.replace(' ', '-').replace('(', '').replace(')', '')}-brut.md"
        brut.write_text(t, encoding="utf-8")
        fact = temp / f"{nom.replace(' ', '-').replace('(', '').replace(')', '')}-factice" / "prereg" / "T0.6-organismes-v0-v1.md"
        fact.parent.mkdir(parents=True, exist_ok=True)
        if fact.exists():
            arret(f"{fact} existe déjà : dossier temporaire neuf exigé")
        fact.write_text(remplir_factice(t, LAISSES[v]), encoding="utf-8")
        resultats[nom] = {
            "sha": sha(t.encode("utf-8")),
            "marqueurs": sorted(set(GABARIT.findall(t))),
            "occurrences": {m: t.count(m) for m in sorted(set(GABARIT.findall(t)))},
            "problemes": prereg.problemes(brut),
            "problemes_factice": prereg.problemes(fact),
            "chaine": controles_chaine(fact),
            "amorce": forme_amorce(fact, "43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859"),
            "commit_cite": [m.group(1) for m in re.finditer(r"Commit du code d'analyse : `([0-9a-f]{40})`", t)],
            "factice": fact,
        }

    extra = []
    if a.code_1609a4bf:
        cfg = temp / "T0.6-organismes-config-7b-v1.json"
        cfg.write_bytes(subprocess.run(["git", "-C", str(depot), "show", f"{COMMIT}:{CONFIG_SOURCE}"],
                                       capture_output=True, check=True).stdout)
        for nom in ("r4", "variante (a)"):
            fact = resultats[nom]["factice"]
            prog = (
                "import json, sys\n"
                "from controle_ia.t06.lanceur import empreinte_config, exiger_citations_t06\n"
                "from controle_ia.prereg import sceller_prereg, exiger_prereg_scelle\n"
                "c = json.load(open(sys.argv[1], encoding='utf-8'))\n"
                "print('empreinte canonique de la configuration :', empreinte_config(c))\n"
                "print('exiger_citations_t06 : passe, entropie', exiger_citations_t06(sys.argv[2], c, c['taches_evaluation']['sha256']))\n"
                "print('sceller_prereg (copie factice, dossier temporaire) :', sceller_prereg(sys.argv[2]))\n"
                "print('exiger_prereg_scelle : passe,', exiger_prereg_scelle(sys.argv[2]))\n")
            r = subprocess.run([sys.executable, "-B", "-c", prog, str(cfg), str(fact)], capture_output=True, text=True,
                               env={"PYTHONPATH": str(Path(a.code_1609a4bf) / "src"), "PATH": "/usr/bin:/bin"})
            extra.append((nom, sha(cfg.read_bytes()), r.returncode, r.stdout.strip(), r.stderr.strip()[-600:]))
            if r.returncode != 0:
                arret(f"essai au code de 1609a4bf en échec ({nom}) : {r.stderr.strip()[-300:]}")

    attendus = sorted(f"<<{m}>>" for m in LAISSES[var])
    if resultats["r4"]["marqueurs"] != attendus:
        arret(f"marqueurs restants {resultats['r4']['marqueurs']} ≠ {attendus}")
    if resultats["r4"]["problemes_factice"]:
        arret(f"problemes à valeurs factices non vide : {resultats['r4']['problemes_factice']}")
    for motif, n, _ in resultats["r4"]["chaine"]["citations"]:
        if n != "1":
            arret(f"citation {motif} : {n} lignes")
    if not resultats["r4"]["amorce"]:
        arret("forme de la citation de l'amorce absente")

    # --- écriture --------------------------------------------------------------------------------------------
    d = docs["principal"][2]
    L = []
    L.append("# Journal du candidat 12 r4 de T0.6 (r3 → r4) — v1\n")
    L.append(f"- Écrit par le script `{Path(sys.argv[0]).as_posix()}` le {a.heure} (heure relevée par `date -u` et passée au script), "
             "pour le rédacteur neuf de la révision 4 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5).")
    L.append(f"- Source : `{SOURCE}`, `{SHA_SOURCE}` (vérifiée par le script) ; couples de la contre-lecture 3 : `{CL3}`, `{SHA_CL3}` (vérifiée).")
    L.append(f"- Couples appliqués : `{docs['principal'][0]}`, `{docs['principal'][1]}` ({len(d['couples'])} couples, variante ({var})).")
    L.append(f"- Couples de la variante (a) : `{docs['variante'][0]}`, `{docs['variante'][1]}` "
             f"({len(docs['variante'][2]['couples'])} couples) ; appliqués de même à la révision 3 dans le dossier temporaire : "
             f"texte `{resultats['variante (a)']['sha']}`, non écrit dans le dépôt.")
    L.append(f"- Sortie : `{sortie.as_posix()}`, `{resultats['r4']['sha']}`.")
    L.append(f"- Règle : {d['regle']}. Chaque couple Y est égal à l'octet au couple de même identifiant de la contre-lecture 3 (vérifié).")
    L.append("")
    for note in d.get("notes_journal", []):
        L.append(note)
        L.append("")
    L.append("## Couples, dans l'ordre d'application\n")
    for c in jr:
        L.append(f"### {c['rang']}. {c['id']}\n")
        L.append(f"- Source : {c['source']}.")
        L.append(f"- Lieu : {c['lieu']} ; section « {c['section']} », ligne {c['ligne']} du texte courant au moment de l'application.")
        L.append(f"- Raison : {c['raison']}.")
        L.append("- Avant :\n")
        L.append(bloc(c["ancien"]))
        L.append("\n- Après :\n")
        L.append(bloc(c["nouveau"]))
        L.append("")
    L.append("## Contrôles du texte obtenu (faits par ce script)\n")
    for nom in ("r4", "variante (a)"):
        r = resultats[nom]
        L.append(f"### {nom}\n")
        L.append(f"- Empreinte du texte : `{r['sha']}`.")
        L.append("- Marqueurs restants (`<<[A-Z0-9_]+>>`, écrits ici sans chevrons) : "
                 + ", ".join(f"{m[2:-2]} ({n})" for m, n in r["occurrences"].items()) + ".")
        L.append("- `controle_ia.prereg.problemes` sur le texte : " + (" ; ".join(r["problemes"]).replace("<<", "").replace(">>", "") or "liste vide") + ".")
        L.append("- Même contrôle, marqueurs laissés remplis de valeurs factices (copie dans le dossier temporaire) : "
                 + (" ; ".join(r["problemes_factice"]) or "**liste vide**") + ".")
        L.append(f"- « Commit du code d'analyse » : {len(r['commit_cite'])} occurrence(s), valeur `{r['commit_cite'][0] if r['commit_cite'] else '—'}`.")
        L.append("- Huit citations lues par `controles` (`grep -cE`, motifs du lanceur v13, l. 129-131), sur la copie factice :")
        for motif, n, forme in r["chaine"]["citations"]:
            L.append(f"  - `{motif}` : {n} ligne ; " + " ; ".join(f"l. {f}" for f in forme))
        L.append("- Chemins extraits comme le lanceur (`sed`, l. 135) : "
                 + " ; ".join(f"{cle} → `{v}`" for cle, v in r["chaine"]["chemins"]) + ".")
        L.append(f"- Forme de la citation de l'amorce (`tr '\\n' ' ' | tr -s ' ' | grep -qF`, l. 143 du lanceur) : {'présente' if r['amorce'] else 'ABSENTE'}.")
        L.append("")
    if extra:
        L.append("### Essais au code du commit `1609a4bf` (dossier temporaire, copies à valeurs factices)\n")
        for nom, shacfg, rc, out, err in extra:
            L.append(f"- {nom} : configuration `{CONFIG_SOURCE}` au commit `1609a4bf` (sha256 du fichier `{shacfg}`) ; code de retour {rc} ;")
            for l in out.splitlines():
                L.append(f"  - {l}")
        L.append("")
    sortie.write_text(texte, encoding="utf-8")
    journal_p.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"écrit : {sortie} {resultats['r4']['sha']}")
    print(f"écrit : {journal_p} {sha(journal_p.read_bytes())}")
    print(f"variante (a) (non écrite) : {resultats['variante (a)']['sha']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
