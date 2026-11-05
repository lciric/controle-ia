"""Inspection de la lentille réelle : clés, provenance, types des clés de J, forme, dtype."""
import sys, json, torch
ck = torch.load(sys.argv[1], map_location="cpu", weights_only=True)
print("clés :", list(ck.keys()))
for k, v in ck.items():
    if k == "J":
        ks = list(v.keys())
        print("J : n =", len(ks), "type de clé :", type(ks[0]).__name__, "clés :", ks)
        t = v[ks[0]]
        print("   forme", tuple(t.shape), t.dtype)
    else:
        print(k, ":", json.dumps(v, default=str, indent=1) if isinstance(v, (dict, list)) else v)
