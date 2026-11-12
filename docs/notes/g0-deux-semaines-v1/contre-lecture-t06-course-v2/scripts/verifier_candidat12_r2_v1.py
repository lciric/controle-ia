"""Candidat 12 révision 2 : (1) rejoue le générateur `appliquer-candidat12-r2-v1.py` (copie dans un arbre jetable) sur le
candidat 12 et compare à la révision 2 du commit ; (2) applique, sur le texte de la révision 2, les lectures exactes du
lanceur v12 (`controles` : huit motifs, chacun une seule fois) et de l'amorce v10 (`lire_unique` : « Tests attendus », chemins
cités), et la lecture de l'empreinte de l'amorce (« `scripts/amorce_instance_t06_v10.sh` (`<sha>` »), après repliage des
lignes ; (3) relève chaque empreinte complète (64 caractères) citée par la révision 2 avec le chemin qui la précède, et la
compare au fichier du commit 8cb539f9 quand le chemin y existe ; (4) relève les marqueurs `<<…>>` restants.

Usage : python -I verifier_candidat12_r2_v1.py DEPOT DOSSIER_JETABLE
N'écrit que sous DOSSIER_JETABLE.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DEPOT, JET = Path(sys.argv[1]), Path(sys.argv[2])
C = "8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63"
C12 = "brouillons/T0.6-organismes-v0-v1-candidat12.md"
C12R2 = "brouillons/T0.6-organismes-v0-v1-candidat12-r2.md"
GEN = "brouillons/T0.6-organismes-v0-v1-candidat9-pieces/appliquer-candidat12-r2-v1.py"


def show(chemin: str, commit: str = C) -> bytes | None:
    r = subprocess.run(["git", "-C", str(DEPOT), "show", f"{commit}:{chemin}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


rapport: dict = {}
# (1) rejeu du générateur
racine = JET / "depot-c12"
(racine / "brouillons/T0.6-organismes-v0-v1-candidat9-pieces").mkdir(parents=True, exist_ok=False)
(racine / C12).write_bytes(show(C12))
(racine / GEN).write_bytes(show(GEN))
r = subprocess.run([sys.executable, "-I", "-B", str(racine / GEN), str(racine)], capture_output=True, text=True)
produit = (racine / C12R2).read_bytes() if (racine / C12R2).exists() else b""
r2 = show(C12R2)
rapport["generateur_code"] = r.returncode
rapport["generateur_sortie"] = r.stdout.strip()
rapport["rejeu_egal_au_commit"] = produit == r2
rapport["sha256_r2_commit"] = hashlib.sha256(r2).hexdigest()

texte = r2.decode("utf-8")
# (2) lectures du lanceur v12 (controles) et de l'amorce v10
motifs = ["Entropie : `[0-9]+`", "Configuration de T0.6 \\(empreinte canonique\\) : `[0-9a-f]{64}`", "Tâches d'évaluation de T0.6 : `[0-9a-f]{64}`",
          "Tests attendus : `[0-9]+`", "Chemin de la configuration de T0.6 : `[^`]+`", "Chemin des tâches d'évaluation de T0.6 : `[^`]+`",
          "Chemin des tâches de distillation de T0.6 : `[^`]+`", "Chemin des consignes de P3 : `[^`]+`"]
lignes = texte.splitlines()
rapport["motifs_du_lanceur_v12"] = {m.split(" :")[0]: sum(1 for l in lignes if re.search(m, l)) for m in motifs}
n_ta = sum(1 for l in lignes if "Tests attendus : `" in l)
val = [re.sub(r".*Tests attendus : `([^`]*)`.*", r"\1", l) for l in lignes if "Tests attendus : `" in l]
rapport["amorce_lire_unique_tests_attendus"] = {"lignes": n_ta, "valeur": val, "entier": bool(val) and len(val) == 1 and val[0].isdigit()}
plie = " ".join(texte.replace("\n", " ").split())
rapport["empreinte_amorce_v10_citee"] = {}
for nom in ("scripts/amorce_instance_t06_v10.sh", "scripts/lancer_t06_v12.sh"):
    sha = hashlib.sha256(show(nom)).hexdigest()
    rapport["empreinte_amorce_v10_citee"][nom] = {"sha256": sha, "cite_sous_la_forme_du_lanceur": f"`{nom}` (`{sha}`" in plie,
                                                  "empreinte_presente": sha in plie, "prefixe16_present": sha[:16] in plie}
# (3) empreintes complètes citées
cites = []
for m in re.finditer(r"`([A-Za-z0-9_./+-]+\.[A-Za-z0-9]+)`[^`]{0,40}?`([0-9a-f]{64})`", plie):
    chemin, sha = m.group(1), m.group(2)
    contenu = show(chemin)
    cites.append({"chemin": chemin, "sha256_cite": sha, "existe_au_commit": contenu is not None,
                  "egal": (hashlib.sha256(contenu).hexdigest() == sha) if contenu is not None else None})
rapport["empreintes_completes_citees"] = cites
rapport["empreintes_completes_ecarts"] = [c for c in cites if c["egal"] is False]
# préfixes de 16 caractères cités : `chemin` (`xxxxxxxxxxxxxxxx…`
pref = []
for m in re.finditer(r"`([A-Za-z0-9_./+-]+\.[A-Za-z0-9]+)`[^`]{0,40}?`([0-9a-f]{8,63})…", plie):
    chemin, p = m.group(1), m.group(2)
    contenu = show(chemin)
    pref.append({"chemin": chemin, "prefixe_cite": p, "existe_au_commit": contenu is not None,
                 "egal": hashlib.sha256(contenu).hexdigest().startswith(p) if contenu is not None else None})
rapport["prefixes_cites_ecarts"] = [x for x in pref if x["egal"] is False]
rapport["prefixes_cites_compte"] = {"total": len(pref), "verifiables": sum(1 for x in pref if x["egal"] is not None),
                                    "egaux": sum(1 for x in pref if x["egal"] is True)}
# (4) marqueurs
rapport["marqueurs_restants"] = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
print(json.dumps(rapport, ensure_ascii=False, indent=1))
