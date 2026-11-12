"""Manifeste des copies du bras B (R12 : rien d'existant n'est écrasé ; chaque fichier est copié à l'octet, au même chemin, depuis un objet git cité). Pour chaque fichier : commit source,
chemin, empreinte de l'objet source et empreinte du fichier de l'arbre ; arrêt au premier écart. Écrit le manifeste en Markdown.

    python3 -I -B scripts/manifeste_copies_bras_b_v1.py DEPOT_GIT_SOURCE ARBRE SORTIE.md
"""
import hashlib
import subprocess
import sys
from pathlib import Path

C_CALCUL, C_AUDIT = "1d6bdc8dd30afe1e77bcfa38164b327ec5d37c52", "05aa560f64c6caf173a322c447d98e616ab5ea99"
COPIES = ([(C_CALCUL, f"src/controle_ia/runs_nuit/{n}.py") for n in ("__init__", "alignement_v1", "rejeu_activations_v1")]
          + [(C_AUDIT, f"src/controle_ia/agregation_r1_v4/{n}.py") for n in ("__init__", "agregateurs_v1", "analyse_v1", "analyse_v2", "analyse_v3", "comparaisons_v1", "entrees_v1", "puissance_v1")]
          + [(C_AUDIT, f"src/controle_ia/audit_fuite_r1_v4/{n}.py") for n in ("__init__", "audit_v1")]
          + [(C_CALCUL, f"{d}/{n}") for d, n in (("donnees/20261105-021737-r1-v4-rejeu-reel", "activations-p3-rejeu-v1-maximum.npz"),
                                                  ("donnees/20261105-021737-r1-v4-rejeu-reel", "activations-p3-rejeu-v1-maximum.npz.sha256"),
                                                  ("donnees/20261105-021737-r1-v4-rejeu-reel", "activations-p3-rejeu-v1-complement-hors-cout.npz"),
                                                  ("donnees/20261105-021737-r1-v4-rejeu-reel", "activations-p3-rejeu-v1-complement-hors-cout.npz.sha256"),
                                                  ("diag/20261105-021737-r1-v4-rejeu-reel", "rejeu-activations.json"), ("diag/20261105-021737-r1-v4-rejeu-reel", "rejeu-activations.json.sha256"),
                                                  ("runs/20261105-021737-r1-v4-rejeu-reel", "manifeste.json"), ("runs/20261105-021737-r1-v4-rejeu-reel", "manifeste.json.sha256"))]
          + [(C_AUDIT, f"{d}/{n}") for d, n in (("diag/20261107-094957-audit-fuite-r1-v4", "audit-fuite-r1-v4-v1.json"), ("diag/20261107-094957-audit-fuite-r1-v4", "audit-fuite-r1-v4-v1.json.sha256"),
                                                 ("runs/20261107-094957-audit-fuite-r1-v4", "manifeste.json"), ("runs/20261107-094957-audit-fuite-r1-v4", "manifeste.json.sha256"),
                                                 ("prereg", "audit-fuite-r1-v4-v1.md"), ("prereg", "audit-fuite-r1-v4-v1.md.sha256"))])


def main(depot: Path, arbre: Path, sortie: Path) -> int:
    lignes = ["# Manifeste des copies du bras B — copies à l'octet, aux mêmes chemins (R12)", "",
              "| commit source | chemin | sha256 de l'objet source | sha256 du fichier de l'arbre | octets |", "|---|---|---|---|---|"]
    for commit, chemin in COPIES:
        if chemin.startswith("prereg/"):
            commit_lu = "9f51e42a708a0b9832107a85103e0338be3573cc"            # `main`, qui porte le texte scellé de l'audit
            src = subprocess.run(["git", "-C", str(depot), "show", f"{commit_lu}:{chemin}"], capture_output=True, check=True).stdout
            commit = commit_lu
        else:
            src = subprocess.run(["git", "-C", str(depot), "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout
        f = (arbre / chemin).read_bytes()
        hs, hf = hashlib.sha256(src).hexdigest(), hashlib.sha256(f).hexdigest()
        if hs != hf:
            raise SystemExit(f"ÉCART : {chemin} (objet source {hs[:12]} ≠ arbre {hf[:12]})")
        lignes.append(f"| `{commit[:8]}` | `{chemin}` | `{hs}` | `{hf}` | {len(f)} |")
    sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(COPIES)} fichiers égaux à leurs objets sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])))
