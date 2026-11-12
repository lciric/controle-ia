#!/usr/bin/env python3
"""Garde PreToolUse (Bash) de Claude Code pour ce dépôt.

1. Aucun lancement d'instance de calcul payante sans GO de calcul valide consigné
   dans `registres/go.md` : la commande doit citer l'identifiant du GO
   (par exemple `GO_ID=GO-2026-10-06-01 vastai create instance …`).
2. R10 : jamais d'arrêt par motif de ligne de commande (pkill, killall,
   kill $(pgrep …), pgrep … | xargs kill) — arrêt par PID ou identifiant d'instance.

Sortie 0 : la commande passe. Sortie 2 : la commande est bloquée, le motif est
écrit sur la sortie d'erreur (Claude Code le transmet à l'agent). Toute entrée
illisible ou registre mal formé bloque : aucun repli silencieux (R5).

Ligne d'extension (R-389) : une seconde ligne au même identifiant n'est admise que si son périmètre commence par
« extension », qu'elle est du même type, accordée par Lazar, ni antérieure à la première ni d'échéance plus lointaine ;
elle ne change ni le type ni la période de validité (ceux de la première ligne). Tout autre doublon bloque.

3. Garde d'empreinte du lanceur de l'organisme v2, version 3 (M2 de la contre-lecture
   `contre-lecture-lanceur-course-pilier-attaque-v2-v2-v1.md`, `4591fe97…`, R-1984) : la règle de permission autorise une
   commande, pas un contenu. Toute commande qui cite `lancer_course_ideation_pilier_attaque_v2_v3` est bloquée sauf si
   elle est exactement `COMMANDE_LANCEUR_V3`, lancée depuis `DEPOT_COURSE`, par le crochet de ce dépôt, et si l'empreinte
   du fichier égale à la fois `EMPREINTE_LANCEUR_V3` (épinglée ici) et son compagnon `.sha256`.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
REGISTRE_GO = RACINE / "registres" / "go.md"

LANCEMENTS = [
    r"\bvastai\s+(create|launch|start)\b",
    r"\brunpodctl\s+(create|start)\b",
    r"\bgcloud\s+compute\s+instances\s+(create|start)\b",
    r"\baws\s+ec2\s+(run-instances|start-instances)\b",
    r"\bsky\s+(launch|start)\b",
    r"\blambda-cloud\s+launch\b",
]
ARRETS_PAR_MOTIF = [
    r"(^|[\s;&|(])pkill\b",
    r"(^|[\s;&|(])killall\b",
    r"\bkill\b[^;&|]*\$\(\s*pgrep\b",
    r"\bkill\b[^;&|]*`\s*pgrep\b",
    r"\bpgrep\b[^;&]*\|\s*xargs\s+(-\S+\s+)*kill\b",
]
GO_ID = re.compile(r"\bGO-\d{4}-\d{2}-\d{2}-\d{2}\b")
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")

# --- 3. garde d'empreinte du lanceur v3 (M2, R-1984) ; GO-2026-11-08-13, décision R-1978 -------------------------------
NOM_LANCEUR_V3 = "lancer_course_ideation_pilier_attaque_v2_v3"
FICHIER_LANCEUR_V3 = NOM_LANCEUR_V3 + ".py"
EMPREINTE_LANCEUR_V3 = "0a704661f1b648ff329d173e8c015b85f6923ef893249b6240e971afaa0a93ca"
DEPOT_COURSE = Path("/home/user/controle-ia-travail")
COMMANDE_LANCEUR_V3 = "/usr/local/bin/python3 -I -B scripts/" + FICHIER_LANCEUR_V3
# le nom cité n'importe où (chemin, compagnon, forme abrégée) ; `test_lancer_…` (les essais) n'est pas une citation
CITE_LANCEUR_V3 = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(NOM_LANCEUR_V3) + r"(?![A-Za-z0-9_])")
LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


def bloquer(motif: str) -> None:
    print(f"GARDE (registres/go, R10) — commande bloquée : {motif}", file=sys.stderr)
    sys.exit(2)


def lire_go(chemin: Path) -> dict[str, dict]:
    """Table Markdown : | id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |"""
    if not chemin.is_file():
        bloquer(f"registre {chemin} absent : aucun GO ne peut être établi")
    go = {}
    for n, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) != 8:
            bloquer(f"registre GO mal formé ligne {n} : 8 colonnes attendues, {len(cellules)} trouvées")
        ident, accorde, typ, perimetre, plafond, echeance, par, ref = cellules
        try:
            accorde_d = date.fromisoformat(accorde)
            # « — » : sans échéance, admis seulement pour un GO qui n'est pas de calcul (GO-2026-10-07-01, dépôt
            # distant) ; un GO de calcul a toujours une échéance lisible (relecture du lancement de la revalidation, L-2)
            echeance_d = None if (echeance == "—" and typ != "calcul") else date.fromisoformat(echeance)
        except ValueError:
            bloquer(f"registre GO mal formé ligne {n} : dates illisibles")
        if ident in go:
            premier = go[ident]
            echeance_ok = ((premier["echeance"] is None and echeance_d is None)
                           or (premier["echeance"] is not None and echeance_d is not None
                               and echeance_d <= premier["echeance"]))
            if not (perimetre.lower().startswith("extension") and typ == premier["type"] and par == "Lazar"
                    and accorde_d >= premier["accorde"] and echeance_ok):
                bloquer(f"registre GO : identifiant {ident} en double")
            premier["extensions"].append(perimetre)  # R-389 : la validité reste celle de la première ligne
            continue
        go[ident] = {"accorde": accorde_d, "type": typ, "echeance": echeance_d, "par": par, "perimetre": perimetre,
                     "ref": ref, "extensions": []}
    return go


def _sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def garder_lanceur_v3(commande: str, cwd) -> None:
    """3. M2 : la commande permise ne s'exécute que sur le contenu épinglé. Rien ne passe en silence (R5)."""
    if not CITE_LANCEUR_V3.search(commande):
        return
    m2 = "empreinte du lanceur v3 (M2, R-1984)"
    if commande != COMMANDE_LANCEUR_V3:
        bloquer(f"{m2} : commande citant {NOM_LANCEUR_V3} qui n'est pas exactement « {COMMANDE_LANCEUR_V3} »")
    if not isinstance(cwd, str) or not cwd:
        bloquer(f"{m2} : dossier courant absent de l'entrée du crochet ; {DEPOT_COURSE} exigé")
    if os.path.realpath(cwd) != os.path.realpath(DEPOT_COURSE):
        bloquer(f"{m2} : lancé depuis {cwd}, {DEPOT_COURSE} exigé")
    if os.path.realpath(RACINE) != os.path.realpath(DEPOT_COURSE):
        bloquer(f"{m2} : crochet de {RACINE}, celui de {DEPOT_COURSE} exigé")
    chemin = DEPOT_COURSE / "scripts" / FICHIER_LANCEUR_V3
    compagnon = Path(str(chemin) + ".sha256")
    if chemin.is_symlink() or not chemin.is_file():
        bloquer(f"{m2} : {chemin} absent ou lien symbolique")
    lue = _sha256(chemin)
    if lue != EMPREINTE_LANCEUR_V3:
        bloquer(f"{m2} : empreinte du fichier {lue} ≠ empreinte épinglée dans le crochet {EMPREINTE_LANCEUR_V3}")
    try:
        lignes = [x for x in compagnon.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, UnicodeDecodeError) as e:
        bloquer(f"{m2} : compagnon {compagnon.name} illisible ({type(e).__name__})")
    ligne = LIGNE_COMPAGNON.match(lignes[0]) if len(lignes) == 1 else None
    if ligne is None or ligne.group(2) != FICHIER_LANCEUR_V3:
        bloquer(f"{m2} : compagnon {compagnon.name} mal formé (une ligne « <empreinte>  {FICHIER_LANCEUR_V3} » exigée)")
    if ligne.group(1) != lue:
        bloquer(f"{m2} : empreinte du compagnon {ligne.group(1)} ≠ empreinte du fichier {lue}")


def decider(commande: str, aujourd_hui: date, cwd=None) -> None:
    for motif in ARRETS_PAR_MOTIF:
        if re.search(motif, commande):
            bloquer("R10 — arrêt par motif de ligne de commande interdit ; arrêter par PID ou identifiant d'instance")
    garder_lanceur_v3(commande, cwd)
    if not any(re.search(m, commande) for m in LANCEMENTS):
        return
    ids = GO_ID.findall(commande)
    if not ids:
        bloquer("lancement d'instance payante sans identifiant de GO dans la commande (GO_ID=GO-AAAA-MM-JJ-NN)")
    registre = lire_go(REGISTRE_GO)
    for i in ids:
        g = registre.get(i)
        if g is None:
            bloquer(f"{i} absent de registres/go.md")
        if g["type"] != "calcul":
            bloquer(f"{i} est un GO de type {g['type']!r}, pas « calcul »")
        if g["par"] != "Lazar":
            bloquer(f"{i} n'est pas accordé par Lazar")
        if not (g["accorde"] <= aujourd_hui <= g["echeance"]):
            bloquer(f"{i} hors de sa période de validité ({g['accorde']} → {g['echeance']})")
        # une révocation est une ligne nouvelle de type « révocation » qui cite le GO révoqué (en-tête du registre ;
        # vérification 2 du remplissage de la revalidation, K-3)
        revocations = sorted(k for k, r in registre.items()
                             if r["type"] == "révocation" and (i in r["perimetre"] or i in r["ref"]))
        if revocations:
            bloquer(f"{i} révoqué par {', '.join(revocations)}")


def main() -> None:
    try:
        entree = json.load(sys.stdin)
        commande = entree["tool_input"]["command"]
        cwd = entree.get("cwd")  # champ commun des entrées de crochet : dossier courant de la session
    except Exception as e:  # entrée illisible : on bloque, on ne devine pas
        bloquer(f"entrée du hook illisible ({type(e).__name__})")
    if not isinstance(commande, str):
        bloquer("commande non textuelle")
    decider(commande, date.today(), cwd)
    sys.exit(0)


if __name__ == "__main__":
    main()
