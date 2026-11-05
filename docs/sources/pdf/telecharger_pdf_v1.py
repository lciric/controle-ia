"""Télécharge la dernière version des PDF d'arXiv donnés, dans un dossier cible ; rend une ligne JSON par papier."""
import hashlib, json, os, ssl, subprocess, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
NS = {"a": "http://www.w3.org/2005/Atom"}
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
def lire(url):
    r = urllib.request.Request(url, headers={"User-Agent": "controle-ia-corpus/1.0 (recherche ; usage non commercial)"})
    with urllib.request.urlopen(r, context=ctx, timeout=120) as f:
        return f.read()
cible = Path(sys.argv[1]); ids = sys.argv[2:]
cible.mkdir(parents=True, exist_ok=True)
api = lire("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)}))
racine = ET.fromstring(api)
versions = {}
for e in racine.findall("a:entry", NS):
    brut = e.find("a:id", NS).text.strip().rsplit("/", 1)[1]
    pid, v = brut.rsplit("v", 1)
    versions[pid] = (int(v), " ".join(e.find("a:title", NS).text.split()), e.find("a:published", NS).text[:10])
for pid in ids:
    time.sleep(3)
    v, titre, publie = versions[pid]
    nom = f"{pid}v{v}.pdf"
    chemin = cible / nom
    if chemin.exists():
        print(json.dumps({"id": pid, "erreur": "existe déjà"}, ensure_ascii=False)); continue
    octets = lire(f"https://export.arxiv.org/pdf/{pid}v{v}")
    if octets[:4] != b"%PDF":
        print(json.dumps({"id": pid, "erreur": "pas un PDF", "debut": octets[:20].hex()}, ensure_ascii=False)); continue
    chemin.write_bytes(octets)
    pages = subprocess.run(["pdfinfo", str(chemin)], capture_output=True, text=True).stdout
    n = next((l.split()[-1] for l in pages.splitlines() if l.startswith("Pages:")), "?")
    p1 = subprocess.run(["pdftotext", "-f", "1", "-l", "1", str(chemin), "-"], capture_output=True, text=True).stdout
    print(json.dumps({"id": pid, "version": v, "fichier": nom, "pages": n, "octets": len(octets),
                      "sha256": hashlib.sha256(octets).hexdigest(), "titre_api": titre, "premiere_version": publie,
                      "debut_page_1": " ".join(p1.split())[:120]}, ensure_ascii=False))
