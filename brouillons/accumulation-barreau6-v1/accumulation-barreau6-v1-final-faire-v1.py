"""Barreau 6, texte final : candidat 5 (`d4c7f96e…`) + les six couples VB5 de la vérification courte (`6d290434…`,
couples `272bd85a…` : deux demandés, quatre recommandés, tous retenus, R-2343) + deux couples d'état de la mère (statut, pas 5).
Écrit `prereg/accumulation-barreau6-v1.md` (jamais d'écrasement) ; défaire les couples redonne le candidat 5 à l'octet."""
import hashlib, json, sys
from pathlib import Path
R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
C5 = R / "brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat5.md"
J = R / "prereg/contre-lectures/accumulation-barreau6-v1-candidat5-verification-courte-v1-pieces/couples-proposes-vb5-v1.json"
SORTIE = R / "prereg/accumulation-barreau6-v1.md"
h = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert h(C5).startswith("d4c7f96e") and h(J).startswith("272bd85a")
t0 = C5.read_text(encoding="utf-8"); t = t0
d = json.loads(J.read_text(encoding="utf-8"))
couples = [(c["ancien"], c["nouveau"]) for c in d["couples"]]
assert len(couples) == 6, len(couples)
for a, n in couples:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, n)
assert hashlib.sha256(t.encode("utf-8")).hexdigest() == "808ae30794c13ba5900a6acbeffee9d54f164dc96826841f4b8c7139a8221fc2", "VB5 appliqués ≠ 808ae307"
mere = [("**Statut** : **candidat 5**",
         "**Statut** : **texte scellé** (R-2343) = candidat 5 + les six couples VB5-C1 à VB5-C6 de la vérification courte "
         "(`prereg/contre-lectures/accumulation-barreau6-v1-candidat5-verification-courte-v1.md`, `6d290434bef826678151fa1c28e2bc68532b9fbd83497d355c19a5199a5039a3`, "
         "Claude Fable 5.2 : « scellable après corrections », aucun nœud) ; **candidat 5**"),
        ("5. **Vérification courte du différentiel du candidat 2 au candidat final**",
         "5. **Faite** (R-2343 : « scellable après corrections », couples VB5 appliqués au texte scellé) — **Vérification courte du différentiel du candidat 2 au candidat final**")]
for a, n in mere:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, n)
assert not SORTIE.exists(), "texte scellé déjà présent (R12)"
SORTIE.write_text(t, encoding="utf-8")
u = t
for a, n in reversed(couples + mere):
    assert u.count(n) == 1, n[:60]
    u = u.replace(n, a)
assert u == t0
print("texte final", h(SORTIE))
