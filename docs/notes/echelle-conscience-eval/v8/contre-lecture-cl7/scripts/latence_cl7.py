"""cl7 : rejeu de l'essai de latence versé (`essai_latence_reelle_v7.py`, fonction `cas` reprise telle quelle par
import du fichier versé) sur la surveillance v7 du commit, puis deux cas de cl7 :
  (g) réglages réels complets (ATTENTE_ARRET_S laissé à son défaut, 20 s), appels de 29 s ;
  (h) faux outil qui IGNORE le signal TERM de `timeout` et ne rend pas la main (300 s) : la borne de 30 s tient-elle ?
Usage : python -I -B latence_cl7.py DOSSIER_NEUF"""
import importlib.util, json, os, pathlib, subprocess, sys, time, hashlib, stat
ESSAI = pathlib.Path("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v7/latence-surveillance/essai_latence_reelle_v7.py")
SURV = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v7/scripts/surveiller_echelle_v7.sh")
spec = importlib.util.spec_from_file_location("essai", ESSAI)
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
base = pathlib.Path(sys.argv[1]); base.mkdir(parents=True)
print(json.dumps({"surveillance": SURV.name, "sha256": hashlib.sha256(SURV.read_bytes()).hexdigest()}), flush=True)
res = [E.cas(SURV, base, "a-appels-29s", 29, 2), E.cas(SURV, base, "b-appels-bloques", 300, 2),
       E.cas(SURV, base, "c-pause-bornee", 0, 40), E.cas(SURV, base, "d-pause-bornee-apres-appels", 10, 50),
       E.cas(SURV, base, "e-appel-s-zero", 45, 2, {"APPEL_S": "0"}), E.cas(SURV, base, "f-pas-s-illisible", 0, 20, {"PAS_S": "abc"})]
# (g) : ATTENTE_ARRET_S retiré de l'environnement (défaut réel 20 s) ; `cas` le fixe à 0 : on le retire après coup
orig = E.cas
def cas_g(surv, base, nom, lenteur, plafond):
    env_old = dict(os.environ)
    try:
        return orig(surv, base, nom, lenteur, plafond, {"ATTENTE_ARRET_S": "20"})
    finally:
        os.environ.clear(); os.environ.update(env_old)
res.append(cas_g(SURV, base, "g-reglages-reels-attente-20", 29, 2))
# (h) : faux outil qui ignore TERM
E.FAUX = E.FAUX.replace("#!/usr/bin/env bash\n", "#!/usr/bin/env bash\ntrap '' TERM\n", 1)
t0 = time.time()
try:
    res.append(E.cas(SURV, base, "h-outil-sourd-a-term", 300, 2))
except subprocess.TimeoutExpired:
    res.append({"cas": "h-outil-sourd-a-term", "resultat": "surveillance toujours bloquée à la borne de l'essai (900 s)"})
print(json.dumps({"fin": time.time() - t0}), flush=True)
(base / "resultat.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
