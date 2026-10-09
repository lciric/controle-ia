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
"""
from __future__ import annotations

import json
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
            accorde_d, echeance_d = date.fromisoformat(accorde), date.fromisoformat(echeance)
        except ValueError:
            bloquer(f"registre GO mal formé ligne {n} : dates illisibles")
        if ident in go:
            bloquer(f"registre GO : identifiant {ident} en double")
        go[ident] = {"accorde": accorde_d, "type": typ, "echeance": echeance_d, "par": par}
    return go


def decider(commande: str, aujourd_hui: date) -> None:
    for motif in ARRETS_PAR_MOTIF:
        if re.search(motif, commande):
            bloquer("R10 — arrêt par motif de ligne de commande interdit ; arrêter par PID ou identifiant d'instance")
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


def main() -> None:
    try:
        entree = json.load(sys.stdin)
        commande = entree["tool_input"]["command"]
    except Exception as e:  # entrée illisible : on bloque, on ne devine pas
        bloquer(f"entrée du hook illisible ({type(e).__name__})")
    if not isinstance(commande, str):
        bloquer("commande non textuelle")
    decider(commande, date.today())
    sys.exit(0)


if __name__ == "__main__":
    main()
