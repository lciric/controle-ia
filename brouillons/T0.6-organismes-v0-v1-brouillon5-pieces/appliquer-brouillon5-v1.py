"""Brouillon 5 de T0.6 = brouillon 4 + les 14 couples L01 à L14 de la contre-lecture du lanceur v1, appliqués dans l'ordre,
puis les substitutions S01 et suivantes (`substitutions-brouillon5-v1.json`). Chaque « ancien » doit apparaître exactement
le nombre de fois attendu (1 par défaut) au moment de son application ; sinon arrêt, rien d'écrit. Bibliothèque standard
seule ; aucun réseau. Journal écrit à côté (`journal-brouillon5-v1.md`) : empreintes des entrées, ligne de chaque
application, marqueurs du résultat, empreinte du résultat.

    python3 -I -B appliquer-brouillon5-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
BROUILLON4 = "brouillons/T0.6-organismes-v0-v1-brouillon4.md"
SHA_BROUILLON4 = "8df90b8be08452a9f1600481087e813ba7fbb1384c0c04888c1d30f7003379af"
COUPLES = "docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v1/couples-contre-lecture-lanceur-T0.6-v1.json"
CONTRE_LECTURE = "docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v1/contre-lecture-lanceur-T0.6-v1.md"
PREFIXE_SHA_COUPLES = "a65e8d584f50bd7c"
PREFIXE_SHA_CL = "5e35956554395686"
BROUILLON5 = "brouillons/T0.6-organismes-v0-v1-brouillon5.md"
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def compagnon_ok(p: Path) -> bool:
    c = p.with_name(p.name + ".sha256")
    if not c.exists():
        return False
    return c.read_text(encoding="utf-8").split()[0] == sha(p)


def ligne_de(texte: str, ancien: str) -> int:
    return texte[: texte.index(ancien)].count("\n") + 1


def appliquer(texte: str, ident: str, ancien: str, nouveau: str, attendu: int, journal: list[str]) -> str:
    n = texte.count(ancien)
    if n != attendu:
        raise SystemExit(f"{ident} : « ancien » trouvé {n} fois, {attendu} attendu : arrêt, rien d'écrit")
    ligne = ligne_de(texte, ancien)
    journal.append(f"| {ident} | {ligne} | {attendu} | {len(ancien)} | {len(nouveau)} |")
    return texte.replace(ancien, nouveau)


def main(racine: Path) -> int:
    b4 = racine / BROUILLON4
    if sha(b4) != SHA_BROUILLON4 or not compagnon_ok(b4):
        raise SystemExit("brouillon 4 : empreinte ou compagnon non conformes")
    couples_p, cl_p = racine / COUPLES, racine / CONTRE_LECTURE
    sha_couples, sha_cl = sha(couples_p), sha(cl_p)
    if not (sha_couples.startswith(PREFIXE_SHA_COUPLES) and compagnon_ok(couples_p)):
        raise SystemExit("couples : empreinte ou compagnon non conformes")
    if not (sha_cl.startswith(PREFIXE_SHA_CL) and compagnon_ok(cl_p)):
        raise SystemExit("contre-lecture : empreinte ou compagnon non conformes")
    couples = json.loads(couples_p.read_text(encoding="utf-8"))
    if couples["brouillon_sha256"] != SHA_BROUILLON4:
        raise SystemExit("les couples ne visent pas le brouillon 4")
    subs = json.loads((ICI / "substitutions-brouillon5-v1.json").read_text(encoding="utf-8"))
    texte = b4.read_text(encoding="utf-8")
    journal = ["| couple | ligne (au moment de l'application) | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    for c in couples["couples"]:
        texte = appliquer(texte, c["id"], c["ancien"], c["nouveau"], 1, journal)
    for s in subs["substitutions"]:
        nouveau = s["nouveau"].replace("{SHA_CL}", sha_cl).replace("{SHA_COUPLES}", sha_couples)
        ancien = s["ancien"].replace("{SHA_CL}", sha_cl).replace("{SHA_COUPLES}", sha_couples)
        texte = appliquer(texte, s["id"], ancien, nouveau, int(s.get("occurrences", 1)), journal)
    marqueurs = sorted(set(MARQUEUR.findall(texte)))
    comptes = {m: texte.count(m) for m in marqueurs}
    if len(marqueurs) != 9:
        raise SystemExit(f"marqueurs : {len(marqueurs)} distincts, 9 attendus : {marqueurs}")
    sortie = racine / BROUILLON5
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà : rien d'écrasé (R12)")
    sortie.write_text(texte, encoding="utf-8")
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    j = [f"# Journal du brouillon 5 de T0.6 — {maintenant} (`date -u`)", "",
         f"- brouillon 4 : `{BROUILLON4}`, `{SHA_BROUILLON4}` (compagnon OK)",
         f"- contre-lecture : `{CONTRE_LECTURE}`, `{sha_cl}` (compagnon OK)",
         f"- couples : `{COUPLES}`, `{sha_couples}` (compagnon OK), {len(couples['couples'])} couples, appliqués dans l'ordre",
         f"- substitutions : `substitutions-brouillon5-v1.json`, `{sha(ICI / 'substitutions-brouillon5-v1.json')}`, {len(subs['substitutions'])} substitutions, appliquées après les couples",
         f"- script : `appliquer-brouillon5-v1.py`, `{sha(Path(__file__).resolve())}`", "", *journal, "",
         "Marqueurs du brouillon 5 (`<<[A-Z0-9_]+>>`), neuf distincts :", "",
         *[f"- `{m}` : {n}" for m, n in comptes.items()], "",
         f"- résultat : `{BROUILLON5}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-brouillon5-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
