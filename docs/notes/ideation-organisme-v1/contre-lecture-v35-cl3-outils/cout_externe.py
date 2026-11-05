"""CL3 (CL34-03) : AdaptateurJugeExterne face à divers `cout_usd` (commande factice locale, aucun réseau)."""
import json, os, sys, tempfile
sys.path.insert(0, sys.argv[1])
from pole.adaptateurs import AdaptateurJugeExterne
cas = {
    "absent": '{"texte": "x"}', "nul 0": '{"texte": "x", "cout_usd": 0}', "négatif": '{"texte": "x", "cout_usd": -1}',
    "chaîne": '{"texte": "x", "cout_usd": "1.0"}', "null": '{"texte": "x", "cout_usd": null}',
    "booléen": '{"texte": "x", "cout_usd": true}', "NaN": '{"texte": "x", "cout_usd": NaN}',
    "Infinity": '{"texte": "x", "cout_usd": Infinity}', "1e308 (fini)": '{"texte": "x", "cout_usd": 1e308}',
    "liste": '{"texte": "x", "cout_usd": [1]}', "normal 0.4": '{"texte": "x", "cout_usd": 0.4}',
}
d = tempfile.mkdtemp(prefix="cout-ext-", dir=sys.argv[2])
for nom, ligne in cas.items():
    a = AdaptateurJugeExterne(["/bin/sh", "-c", "cat >/dev/null; printf '%s\\n' '" + ligne + "'"], environnement={"PATH": "/usr/bin:/bin"})
    r = a.lancer("juge_ideation", "consigne", d, 3.0, 2)
    print(f"{nom:14s} → statut={r.statut:15s} cout={r.cout_declare_usd!r:10} erreur={r.erreur!r}")
# sortie ≠ 0 alors que la commande a imprimé un coût (le devis lui demande d'imprimer TOUJOURS cout_usd)
a = AdaptateurJugeExterne(["/bin/sh", "-c", "cat >/dev/null; echo '{\"texte\": \"\", \"cout_usd\": 1.7}'; exit 3"], environnement={"PATH": "/usr/bin:/bin"})
r = a.lancer("juge_ideation", "consigne", d, 3.0, 2)
print(f"{'code 3 + 1.7':14s} → statut={r.statut:15s} cout={r.cout_declare_usd!r:10} erreur={r.erreur!r}")
