"""Cas limites de lire() (analyse v4 telle quelle) : issues compatibles entre elles, masquées par l'ordre de lecture.
Intervalles fabriqués, aucun bootstrap. Lecture seule de l'analyse (importée par chemin, sans bytecode)."""
import importlib.util, json, sys
WT = "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1"
spec = importlib.util.spec_from_file_location("an", WT + "/echelle-v4/scripts/analyser_echelle_v4.py")
AN = importlib.util.module_from_spec(spec); spec.loader.exec_module(AN)

def r(ab, ba, cert=(0.8, 0.8), cert_ba=(0.8, 0.8), sp=(0.1, 0.5)):
    def m(k, s, c):
        return {"A_ctx_fixe_ic": [c, 0.95], "lambda_ic": list(s[k])}
    return {"petit": {"ab": m("lp", ab, cert[0]), "ba": m("lp", ba, cert_ba[0])},
            "grand": {"ab": m("lg", ab, cert[1]), "ba": m("lg", ba, cert_ba[1])},
            "delta_lambda_ic": {"ab": list(ab["dl"]), "ba": list(ba["dl"])},
            "specificite_ic": {"ab": list(sp), "ba": list(sp)},
            "profondeur_contraire": {"ab": False, "ba": False}}

def tient(res, s, issue):
    return all(t for _, t in AN.conditions(res, s)[issue])

cas = {
 # sens a→b : « pas de fuite » ET « nul » tiennent ; sens b→a : « nul » seul tient
 "pdf+nul / nul": (dict(lp=(0.05, 0.22), lg=(0.0, 0.20), dl=(-0.10, 0.15)),
                   dict(lp=(0.10, 0.32), lg=(0.08, 0.30), dl=(-0.12, 0.14))),
 # sens a→b : « fuite de signe inverse » ET « nul » ; sens b→a : « nul » seul
 "fsi+nul / nul": (dict(lp=(-0.70, -0.30), lg=(-0.65, -0.35), dl=(-0.15, 0.10)),
                   dict(lp=(-0.45, -0.15), lg=(-0.40, -0.20), dl=(-0.12, 0.08))),
 # sens a→b : « fuite de signe inverse » ET « nul » ; sens b→a : « pas de fuite » ET « nul »
 "fsi+nul / pdf+nul": (dict(lp=(-0.70, -0.30), lg=(-0.65, -0.35), dl=(-0.15, 0.10)),
                       dict(lp=(-0.20, 0.05), lg=(-0.22, 0.02), dl=(-0.10, 0.12))),
 # contrôle : les deux sens « pas de fuite » et « nul »
 "pdf+nul / pdf+nul": (dict(lp=(0.05, 0.22), lg=(0.0, 0.20), dl=(-0.10, 0.15)),
                       dict(lp=(0.02, 0.20), lg=(-0.03, 0.18), dl=(-0.12, 0.14))),
}
for nom, (ab, ba) in cas.items():
    res = r(ab, ba)
    lecture, reserves, detail = AN.lire(res)
    tenues = {s: [i for i in AN.ISSUES if tient(res, s, i)] for s in ("ab", "ba")}
    print(f"{nom:22s} -> lecture « {lecture} » ; par sens {detail['lecture_par_sens']} ; "
          f"issues dont toutes les conditions tiennent : a→b {tenues['ab']}, b→a {tenues['ba']}")
    if detail["conditions_manquantes"]:
        print("    conditions manquantes rapportées :", json.dumps(detail["conditions_manquantes"], ensure_ascii=False))
