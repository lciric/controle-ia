"""Mutants du lanceur v2 : chaque garde nouvelle retirée une à une ; le banc doit compter au moins un cas non conforme."""
import shutil, sys
from pathlib import Path
src, hn, dest = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
t = src.read_text(encoding="utf-8")
M = {
 "M01-prix-booleen": ("return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)", "return isinstance(v, (int, float)) and math.isfinite(v)"),
 "M02-prix-positif": ("return float(p) if nombre(p) and p > 0 else None", "return float(p) if nombre(p) else None"),
 "M03-nombre-fini": ("and not isinstance(v, bool) and math.isfinite(v)", "and not isinstance(v, bool)"),
 "M04-memoire-80-go": (' and o["gpu_ram"] >= 79000', ""),
 "M05-une-carte": (' and o["num_gpus"] == 1', ""),
 "M06-relance-exclusion": ("conformes = sorted((o for o in conformes if not exclue(o))", "conformes = sorted((o for o in conformes)"),
 "M07-constantes-du-v1": ('    [ -n "$a" ] && [ "$a" = "$b" ] || { rm -f "$T/lanceur-v1-S.sh"; echo "constante $k du lanceur v2 ≠ celle du lanceur v1 versé à S"; exit 2; }\n', "    :\n"),
 "M08-c3-hors-v3": ('[ -z "$HORS_V3" ] || {', 'true || {'),
 "M09-sommet-du-distant": ('|| { echo "lancer_notations_v2.sh exécuté ≠ copie au sommet du dépôt distant"; exit 2; }', '|| true'),
 "M10-trois-scripts": ("if set(vus) != set(attendus):", "if False:"),
 "M11-lignes-mal-formees": ("if not m or vus.setdefault(m.group(1), m.group(2)) != m.group(2):", "if m and vus.setdefault(m.group(1), m.group(2)) and False:"),
 "M12-empreintes-eprouvees": ("    if vus[s] != e:", "    if False:"),
 "M13-traces-numeriques": ('[[ "$(basename "$1")" =~ ^[0-9]+$ ]] && {', 'false && {'),
 "M14-machine-illisible": ("if not all(isinstance(x, int) and not isinstance(x, bool) for x in (m, h)):", "if False:"),
 "M15-identifiant-en-double": ("if len(vus) != len(set(vus)):", "if False:"),
 "M16-machine-entiere-en-relance": ("    if not (entier(m) and entier(h)):\n        return True", "    if False:\n        return True"),
 "M17-renommages": ('diff --no-renames --name-only', 'diff --name-only'),
 "M19-offre-json-sans-machine": ('champs = ("id", "machine_id", "host_id", "gpu_name",', 'champs = ("id", "gpu_name",'),
 "M20-constantes-reduites": ("for k in PRIX_MAX HEURES_CREDIT PLAFOND_GO PLAFOND_SURVEILLANCE_S FILTRE ARRETEES_TOLEREES; do", "for k in PRIX_MAX; do"),
}
DEPL_A = """json.dump([{k: o.get(k) for k in extrait} if isinstance(o, dict) else {"illisible": type(o).__name__} for o in offres],
          open(relues, "w"), indent=1)
"""
DEPL_B = "o = conformes[0]\n"
for nom, (a, b) in M.items():
    assert t.count(a) == 1, (nom, t.count(a))
    d = dest / nom
    shutil.copytree(hn, d)
    (d / "lancer_notations_v2.sh").write_text(t.replace(a, b), encoding="utf-8")
    print(nom)

# M18 : extrait des offres relues écrit seulement s'il existe une offre conforme (mutant MR1 de la relecture courte)
assert t.count(DEPL_A) == 1 and t.count(DEPL_B) == 1
d = dest / "M18-offres-relues-si-conformes"
shutil.copytree(hn, d)
(d / "lancer_notations_v2.sh").write_text(t.replace(DEPL_A, "").replace(DEPL_B, DEPL_A + DEPL_B), encoding="utf-8")
print("M18-offres-relues-si-conformes")
