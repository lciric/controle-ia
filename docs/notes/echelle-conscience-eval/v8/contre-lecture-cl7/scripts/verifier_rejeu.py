"""Contrôle indépendant du rejeu versé : (1) intervalles de λ du rejeu = ceux des bancs (lus moi-même) ;
(2) écart ponctuel e(m) du rejeu = différence des λ ponctuels consignés par les bancs (à l'arrondi près) ;
(3) lecture v7 reconstituée à partir des issues tenues v6 consignées et de e(m) : la règle de la v7 appliquée à la main."""
import json, pathlib, collections
N = pathlib.Path("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval")
rej = [json.loads(l) for l in (N / "v7/rejeu-bancs-cl5-cl6/rejeu-bancs-cl5-cl6-v7.jsonl").read_text().splitlines()]
bancs = {}
for p in list((N / "v6/contre-lecture-cl5/banc").glob("banc-cl5-lot*.jsonl")) + [x for x in (N / "v7/contre-lecture-cl6/banc").glob("banc-cl6-*.jsonl") if "rejeu" not in x.name]:
    for l in p.read_text().splitlines():
        d = json.loads(l)
        bancs[(p.name, d["scenario"], d["graine"])] = d
print("lignes du rejeu", len(rej), "lignes des bancs", len(bancs))
ok_ic = ok_e = 0; ecarts_e = []; manque_point = 0
for r in rej:
    b = bancs[(r["banc"], r["scenario"], r["graine"])]
    ic = {f"{s}_{m}": b[f"lambda_{s}_{m}_ic"] for s in ("ab", "ba") for m in ("petit", "grand")}
    ok_ic += ic == r["lambda_ic"]
    if "lambda_ab_petit" in b:
        for m in ("petit", "grand"):
            e = b[f"lambda_ab_{m}"] - b[f"lambda_ba_{m}"]
            ecarts_e.append(abs(e - r["ecart_sens"][m]))
    else:
        manque_point += 1
print("intervalles identiques (mon contrôle) :", ok_ic, "sur", len(rej))
print("écart ponctuel : lignes sans λ ponctuel consigné :", manque_point, "; plus grand écart |e_banc − e_rejeu| :", max(ecarts_e) if ecarts_e else None, "sur", len(ecarts_e))
# (3) lecture v7 par la règle : issues tenues par sens consignées par le rejeu (calculées par v7, mais les issues tenues par
# sens ne dépendent pas de la cohérence) ; comparaison avec issues tenues du banc (v6) quand elles y sont
diff_tenues = 0
for r in rej:
    b = bancs[(r["banc"], r["scenario"], r["graine"])]
    t6 = b.get("issues_tenues")
    if t6 is not None and t6 != r["issues_tenues_v7"]:
        diff_tenues += 1
print("issues tenues par sens : v6 (banc) ≠ v7 (rejeu) :", diff_tenues)
# changements de lecture et motif
c = collections.Counter()
for r in rej:
    v6 = r["lecture_v6"].split(" (")[0] if not r["lecture_v6"].startswith("fuite") else r["lecture_v6"].rsplit(" (", 1)[0] if r["lecture_v6"].endswith("réserve(s))") else r["lecture_v6"]
    if r["lecture_v6"].split(" (")[0] != r["lecture_v7"].split(" (")[0] or (r["lecture_v6"] != r["lecture_v7"] + (f" ({len(r['reserves_v7'])} réserve(s))" if r["reserves_v7"] else "")):
        e = r["ecart_sens"]
        c[(r["scenario"], r["lecture_v6"], r["lecture_v7"], "incohérents=" + str(sum(abs(v) > 0.25 for v in e.values())))] += 1
        print("CHANGE", r["banc"], r["scenario"], r["graine"], r["lecture_v6"], "→", r["lecture_v7"], "e =", e, "tenues", r["issues_tenues_v7"])
print(sum(c.values()), "changements")
# plage des |e| du modèle le plus touché, dans les 10 artefacts de cl6
arte = [r for r in rej if r["scenario"].startswith("d256_H0_croise_oppose") and r["lecture_v7"] == "désaccord des deux sens"]
print("artefacts cl6 bloqués :", len(arte), "; |e| min/max des deux modèles :", min(min(abs(v) for v in r["ecart_sens"].values()) for r in arte), max(max(abs(v) for v in r["ecart_sens"].values()) for r in arte))
print("dans les 10, nombre de modèles incohérents :", collections.Counter(sum(abs(v) > 0.25 for v in r["ecart_sens"].values()) for r in arte))
