"""Appel de contrôle du tour « mémoire du pôle » (27 octobre 2026), copie de test_depense_v4.py sous un nom nouveau (R12), seuls les noms des variables de clés changent (clés de ce compte). Test de dépense du second pilote : un appel payant par espèce, par les appelants du collisionneur v2.5
(`collisionneur_v2.py`, 213b52ef…). Usage : python -I -B appel_controle_v5.py COLLISIONNEUR SORTIE.json GO_ID (v2 : GO en argument)"""
import datetime, importlib.util, json, sys
spec = importlib.util.spec_from_file_location("collisionneur_v2", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
ESP = {"CLAUDE_FABLE_5_1": ("A", cv.appeler_anthropic), "CLAUDE_OPUS_5_5": ("B", cv.appeler_anthropic), "GEMINI_ARGON": ("C", cv.appeler_gemini)}
d = {"go": sys.argv[3], "variables_cles": {"anthropic": "RR_ANTHROPIC_API_KEY (en-tête RR_ANTHROPIC_WORKSPACE_ID)", "gemini": "GEMINI_API_KEY"}, "especes": {}}
total = 0.0
for e, (l, f) in ESP.items():
    m = cv.MODELES[l]
    h = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        r = f(m["id"], "Réponds par le seul mot : prêt.", 1024)
        st = "ECHEC" if r.echec else cv.statut_reponse(m["fournisseur"], r)
        c = cv.cout(m["prix"], r.usage)
        d["especes"][e] = {"statut": st, "modele_servi": r.modele_servi, "cout_usd": c, "jetons_sortie": r.usage.get("sortie"), "heure_utc": h}
        total += c
    except Exception as ex:
        d["especes"][e] = {"statut": "ECHEC", "erreur": type(ex).__name__, "heure_utc": h}
d["cout_usd"] = total
json.dump(d, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({e: (v.get("statut"), v.get("modele_servi"), round(v.get("cout_usd") or 0, 5)) for e, v in d["especes"].items()}, round(total, 5))
