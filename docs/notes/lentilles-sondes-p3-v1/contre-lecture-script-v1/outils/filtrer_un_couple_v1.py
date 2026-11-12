"""Copie de sondes-figees.json réduite à une sonde (pour un essai réel d'un seul couple sonde × couche), rescellée.
Le fichier de poids et son empreinte attendue (sondes_legeres_sha256) restent ceux de P3. Usage : json_source nom sortie"""
import sys, json, hashlib
from pathlib import Path
src, nom, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
d = json.loads(src.read_text(encoding="utf-8"))
r = d["resultat"]
concept = nom.split("-")[0]
r["sondes"] = [s for s in r["sondes"] if s["nom"] == nom]
assert len(r["sondes"]) == 1
r["principales"] = {concept: nom}
d["_filtre_contre_lecture"] = f"copie réduite à {nom} ; source {src.name} {hashlib.sha256(src.read_bytes()).hexdigest()}"
out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
Path(str(out) + ".sha256").write_text(f"{hashlib.sha256(out.read_bytes()).hexdigest()}  {out.name}\n", encoding="utf-8")
print(out, "écrit")
