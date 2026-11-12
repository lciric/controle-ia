"""Contre-lecture de la v2 par Gemini Argon (GO-2026-10-28-12) : un appel, au plus une relance sur sortie vide ou coupée.
Usage : python -I -B appeler_argon_v2.py COLLISIONNEUR_V2 DOSSIER ; clé lue dans GEMINI_API_KEY (passée sous env -i)."""
import datetime, hashlib, importlib.util, json, os, sys
spec = importlib.util.spec_from_file_location("cv", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
D = sys.argv[2]; PLAFOND = 5.0; PRIX = cv.MODELES["C"]["prix"]
lire = lambda p: open(os.path.join(D, p), encoding="utf-8").read()
doc = lire("conception-affinage-equipe-rouge-v2.md")
assert hashlib.sha256(doc.encode()).hexdigest().startswith("ba95bb83"), "empreinte de la v2"
parties = [lire("consigne-contre-lecture-affinage-v2.md"),
           "\n\nPréfixe de tes constats neufs : CL2-A-01, … ; attaques manquantes : AM2-A-01, … (la version 1 de la conception ne t'est pas servie : les rapports la citent).\n",
           "\n\n=============== DOCUMENT À CONTRE-LIRE : conception-affinage-equipe-rouge-v2.md ===============\n\n", doc]
for f in ("contre-lecture-opus-v1.md", "contre-lecture-argon-v1.md", "contre-lecture-des-contre-lectures-fable-v1.md"):
    parties += [f"\n\n=============== RAPPORT SUR LA V1 : {f} ===============\n\n", lire("rapports-v1/" + f)]
for f in ("LISEZMOI.md", "NOTE-renvois-absents-v1.md", "brief-affinage-equipe-rouge-fable-v2.md",
          "passation-affinage-equipe-rouge-fable-v1.md", "integration-proposeurs-ia-v1.md", "conception-pole-scientifique-v1.md"):
    parties += [f"\n\n=============== LOT DE L'AUTEUR : {f} ===============\n\n", lire("lot/" + f)]
prompt = "".join(parties)
open(os.path.join(D, "argon-prompt-v2.txt"), "w", encoding="utf-8").write(prompt)
journal, depense = [], 0.0
for essai, mx in ((1, cv.MODELES["C"]["max"]), (2, cv.MODELES["C"]["max_relance"])):
    pire = cv.cout_pire_cas(PRIX, len(prompt), mx)
    if depense + pire > PLAFOND:
        print(f"ARRÊT : dépense {depense:.2f} + pire cas {pire:.2f} > plafond {PLAFOND}"); break
    h = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    r = cv.appeler_gemini(cv.MODELES["C"]["id"], prompt, mx)
    c = cv.cout(PRIX, r.usage); depense += c
    statut = cv.statut_reponse("gemini", r)
    journal.append({"essai": essai, "heure": h, "statut": statut, "fin": str(r.fin), "modele_servi": r.modele_servi,
                    "usage": r.usage, "cout_usd": round(c, 4), "echec": r.echec, "caracteres": len(r.texte or "")})
    print(journal[-1], flush=True)
    if r.texte:
        open(os.path.join(D, f"contre-lecture-argon-v2.essai{essai}.md"), "w", encoding="utf-8").write(r.texte)
    if statut in ("OK", "REFUS") or r.echec:
        break
json.dump({"go": "GO-2026-10-28-12", "plafond_usd": PLAFOND, "depense_usd": round(depense, 4), "journal": journal,
           "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()},
          open(os.path.join(D, "argon-journal-v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"dépense {depense:.4f} USD")
