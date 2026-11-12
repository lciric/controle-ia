"""Épreuve : le brouillon 1 du texte v4, marqueur du commit du lanceur rempli par un hash factice, renommé `…-v3-v4.md` dans un extrait
jetable de `08ad8f35`, compagnon simulé (extrait du bloc-notes, hors de tout dépôt), lu par `lire_preenregistrement` du lanceur gelé ;
puis le même texte avec le marqueur laissé : refus attendu."""
import hashlib, importlib, os, sys
racine, brouillon = sys.argv[1], sys.argv[2]
sys.path.insert(0, racine); os.chdir(racine)
m = importlib.import_module("demonstrations.attaque_goodhart_v3")
t = open(brouillon, encoding="utf-8").read()
for nom, texte in (("marqueur rempli (simulé)", t.replace("<<COMMIT_LANCEUR_DURABLE>>", "f" * 40)), ("marqueur laissé", t)):
    dst = os.path.join(racine, "prereg", "preenregistrement-attaque-goodhart-v3-v4.md")
    open(dst, "w", encoding="utf-8").write(texte)
    open(dst + ".sha256", "w").write(f"{hashlib.sha256(texte.encode()).hexdigest()}  preenregistrement-attaque-goodhart-v3-v4.md\n")
    try:
        r = m.lire_preenregistrement(dst)
        plan = r[3] if len(r) > 3 else r
        print(nom, ": ACCEPTÉ ; empreinte", r[1][:16], "; plan", {k: plan[k] for k in sorted(plan)} if isinstance(plan, dict) else plan)
    except Exception as e:
        print(nom, ": REFUS", type(e).__name__, str(e)[:300])
    os.remove(dst); os.remove(dst + ".sha256")
