"""v9 (1er novembre 2026, R-962) : copie de appel_controle_v8.py (e6615534…) ; seuls changements : cinquième espèce E = GPT-6 Astra
(`gpt-6-astra`, appelant `appeler_openai` du collisionneur v8, clé OPENAI_API_KEY), nom de la variable de clé d'OpenAI consigné,
modèle demandé et jetons d'entrée consignés par espèce. Un appel payant par espèce, 1024 jetons de sortie au plus : c'est l'appel de
contrôle des cinq espèces avant tout lancement (modèle servi exact, statut, coût au barème du collisionneur).
v8 (30 octobre, R-830) : copie de la v7, espèce B nommée CLAUDE_OPUS_4_6 (collisionneur v6) : copie de appel_controle_v6.py, plus
l'espèce Kimi (D) par le relais local.
Origine : appel de contrôle du tour « mémoire du pôle » (27 octobre 2026), copie de test_depense_v4.py (R12).
Usage : python -I -B appel_controle_v9.py COLLISIONNEUR_V8 SORTIE.json GO_ID
Variables lues par les appelants : ANTHROPIC_API_KEY (et ANTHROPIC_WORKSPACE_ID si la clé l'exige), GEMINI_API_KEY,
KIMI_RELAIS_URL (relais local lancé à part), OPENAI_API_KEY ; jamais affichées ni écrites."""
import datetime, importlib.util, json, sys
spec = importlib.util.spec_from_file_location("collisionneur_v8", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
ESP = {"CLAUDE_FABLE_5_1": ("A", cv.appeler_anthropic), "CLAUDE_OPUS_4_6": ("B", cv.appeler_anthropic), "GEMINI_ARGON": ("C", cv.appeler_gemini),
       "KIMI_K3_1_PRO": ("D", cv.appeler_kimi), "GPT_6_ASTRA": ("E", cv.appeler_openai)}
assert tuple(l for l, _ in ESP.values()) == cv.LETTRES, "l'appel de contrôle doit couvrir exactement les lettres du collisionneur"
d = {"go": sys.argv[3], "collisionneur": {"version": cv.VERSION, "sha256": cv.empreinte_script()},
     "variables_cles": {"anthropic": "RR_ANTHROPIC_API_KEY_3 (sans en-tête d espace de travail)", "gemini": "GEMINI_API_KEY_2",
                        "kimi": "relais local, aucune clé ici", "openai": "OPENAI_API_KEY"}, "especes": {}}
total = 0.0
for e, (l, f) in ESP.items():
    m = cv.MODELES[l]
    h = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        r = f(m["id"], "Réponds par le seul mot : prêt.", 1024)
        st = "ECHEC" if r.echec else ("MODELE_DIFFERENT" if not cv.modele_conforme(m["id"], r.modele_servi) else cv.statut_reponse(m["fournisseur"], r))
        c = cv.cout(m["prix"], r.usage)
        d["especes"][e] = {"lettre": l, "modele_demande": m["id"], "statut": st, "modele_servi": r.modele_servi, "fin": r.fin, "echec": r.echec,
                           "cout_usd": c, "jetons_entree": r.usage.get("entree"), "jetons_sortie": r.usage.get("sortie"), "heure_utc": h}
        total += c
    except Exception as ex:  # jamais la clé : seul le type de l'exception est consigné
        d["especes"][e] = {"lettre": l, "modele_demande": m["id"], "statut": "ECHEC", "erreur": type(ex).__name__, "heure_utc": h}
d["cout_usd"] = total
json.dump(d, open(sys.argv[2], "x", encoding="utf-8"), ensure_ascii=False, indent=1)
print({e: (v.get("statut"), v.get("modele_servi"), round(v.get("cout_usd") or 0, 5)) for e, v in d["especes"].items()}, round(total, 5))
