"""Ordre de 7b, brouillon 5 : brouillon 4 (`5f2167d7…`) avec deux marqueurs de la mère remplis (R-2324, R-2325) ;
`COMMIT_MAIN_REMISE` reste, rempli au scellement (parent du commit de l'ordre scellé). Aucun autre octet ne change."""
import hashlib, sys
from pathlib import Path
R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
B4 = R / "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4.md"
B5 = R / "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon5.md"
assert hashlib.sha256(B4.read_bytes()).hexdigest().startswith("5f2167d7"), "brouillon 4 changé"
ligne = [l for l in (R / "registres/scellements-v1.md").read_text(encoding="utf-8").splitlines() if l.startswith("| SCELLEMENT-T07 ")]
assert len(ligne) == 1
t = B4.read_text(encoding="utf-8")
couples = [("<<LIGNE_SCELLEMENT_T07>>", ligne[0]),
           ("`<<ID_SESSION_FILLE>>`", "à laquelle Lazar remet cet ordre (session non ouverte au scellement : règle du marqueur, § 14)")]
for a, n in couples:
    assert t.count(a) == 1, a
    t = t.replace(a, n)
import re
assert re.findall(r"<<[A-Z0-9_]+>>", t) == ["<<COMMIT_MAIN_REMISE>>"]   # les deux « <<'FIN' » de bash ne sont pas des marqueurs
assert not B5.exists(), "brouillon 5 existe déjà (R12)"
B5.write_text(t, encoding="utf-8")
# défaire les couples redonne le brouillon 4
u = t
for a, n in couples:
    assert u.count(n) == 1, n
    u = u.replace(n, a)
assert u == B4.read_text(encoding="utf-8")
print("brouillon 5", hashlib.sha256(B5.read_bytes()).hexdigest())
