"""Liste le répertoire central d'un zip distant par requêtes HTTP partielles (Range), sans télécharger le contenu."""
import io, sys, zipfile, urllib.request, ssl, os

class FichierDistant(io.RawIOBase):
    def __init__(self, url, taille):
        self.url, self.taille, self.pos, self.octets = url, taille, 0, 0
        self.ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt")
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.taille + off)
        return self.pos
    def read(self, n=-1):
        if n is None or n < 0: n = self.taille - self.pos
        if n == 0 or self.pos >= self.taille: return b""
        fin = min(self.pos + n, self.taille) - 1
        if fin - self.pos > 64 * 1024 * 1024: raise RuntimeError("lecture trop grande refusée")
        req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.pos}-{fin}"})
        with urllib.request.urlopen(req, context=self.ctx) as r:
            if r.status != 206: raise RuntimeError(f"Range non honoré : {r.status}")
            data = r.read()
        self.pos += len(data); self.octets += len(data)
        return data
    def readinto(self, b):
        d = self.read(len(b)); b[:len(d)] = d; return len(d)

url, taille = sys.argv[1], int(sys.argv[2])
f = FichierDistant(url, taille)
z = zipfile.ZipFile(io.BufferedReader(f, buffer_size=1 << 20))
for i in z.infolist():
    print(f"{i.file_size}\t{i.compress_size}\t{i.date_time[0]:04d}-{i.date_time[1]:02d}-{i.date_time[2]:02d}\t{i.filename}")
print(f"# entrees={len(z.infolist())} octets_lus={f.octets}", file=sys.stderr)
