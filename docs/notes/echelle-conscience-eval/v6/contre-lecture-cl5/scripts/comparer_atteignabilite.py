"""cl5 : compare la simulation rejouée à la sortie scellée (champ par champ ; seul le commit peut différer)."""
import json, sys
a = json.load(open(sys.argv[1], encoding="utf-8"))
b = json.load(open(sys.argv[2], encoding="utf-8"))
diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
print("champs différents :", diff)
for k in diff:
    if k != "detail":
        print(f"  {k} : scellée {a.get(k)!r} ; rejouée {b.get(k)!r}")
print("détail identique :", a["detail"] == b["detail"], ";", len(a["detail"]), "analyses")
print("comptes identiques :", a["comptes"] == b["comptes"], ";", len(a["comptes"]), "cases")
