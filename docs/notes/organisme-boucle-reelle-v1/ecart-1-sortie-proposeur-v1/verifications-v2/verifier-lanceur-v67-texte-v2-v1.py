"""Vérification hors ligne : le lanceur v67 (copie jetable de l'arbre v67) accepte-t-il le brouillon du texte v2, la
configuration v8, le vrai registre des GO (GO-2026-11-12-06) et l'héritage de départ, et refuse-t-il les artefacts (texte v1,
configurations v6 et v7, GO-2026-11-10-11) ? Aucun appel, aucune porte, aucune machine : la chaîne réelle de `principal` doit
s'arrêter à la garde 22 (bwrap absent simulé, `WHICH` remplacée) pour le cas sain, et avant elle pour chaque artefact.
Arguments : ARBRE_ORG TEXTE_V2 TEXTE_V1 CONF_V8 CONF_V7 CONF_V6 GO_MD HERITAGE."""
import importlib.util, io, os, shutil, sys, tempfile
from contextlib import redirect_stderr, redirect_stdout
ORG, T2, T1, C8, C7, C6, GO, HER = sys.argv[1:9]
copie = os.path.join(tempfile.mkdtemp(prefix="verif-v67-"), "orchestrator")
shutil.copytree(ORG, copie, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
sys.path.insert(0, copie)
os.chdir(copie)
spec = importlib.util.spec_from_file_location("l67", os.path.join(copie, "demonstrations", "boucle_reelle_v67.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
from pole.outils import ecrire_scelle  # noqa: E402
prereg = os.path.join(copie, "prereg")
os.makedirs(prereg, exist_ok=True)
v2 = os.path.join(prereg, "preenregistrement-boucle-reelle-organisme-v1-v2.md")
ecrire_scelle(v2, open(T2, encoding="utf-8").read())
v1 = os.path.join(prereg, "preenregistrement-boucle-reelle-organisme-v1-v1.md")
ecrire_scelle(v1, open(T1, encoding="utf-8").read())
_, emp, gelees, plan, jeu = L.lire_preenregistrement(v2)
print(f"texte v2 (brouillon, scellé dans la copie seulement) : accepté ; {len(gelees)} empreintes égales au code ; plan go={plan['go']}, "
      f"configuration={plan['configuration_sha256'][:12]}…")
try:
    L.lire_preenregistrement(v1)
    print("ARTEFACT NON REFUSÉ : texte v1")
except L.PreenregistrementRefuse as e:
    print("artefact texte v1 : refusé :", str(e)[:120])
env_propre = {"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8", "TMPDIR": tempfile.gettempdir()}


def principal(texte, conf, go_id):
    argv = [tempfile.mkdtemp() + "/sortie", "--preenregistrement", texte, "--heritage-depart", HER, "--configuration", conf,
            "--moteur", "reel", "--confirmer-moteur-reel", "--registre-go", GO, "--go", go_id, "--bac", "reel", "--utilisateur-bac", "64097"]
    out, err = io.StringIO(), io.StringIO()
    sauve = dict(os.environ)
    os.environ.clear(); os.environ.update(env_propre)
    L.WHICH = lambda nom: None  # bwrap absent simulé : la garde 22 arrête toujours, avant toute porte
    try:
        with redirect_stdout(out), redirect_stderr(err):
            code = L.principal(argv)
    finally:
        os.environ.clear(); os.environ.update(sauve)
    return code, err.getvalue().strip().splitlines()[-1][:220]


cas = [("sain : texte v2, configuration v8, GO-2026-11-12-06", v2, C8, "GO-2026-11-12-06", "MachineRefusee"),
       ("artefact : texte v1", v1, C8, "GO-2026-11-12-06", "PreenregistrementRefuse"),
       ("artefact : configuration v7", v2, C7, "GO-2026-11-12-06", "ConfigurationRefusee"),
       ("artefact : configuration v6", v2, C6, "GO-2026-11-12-06", "ConfigurationRefusee"),
       ("artefact : GO-2026-11-10-11", v2, C8, "GO-2026-11-10-11", "GoAbsent")]
echecs = 0
for nom, texte, conf, go_id, attendu in cas:
    code, motif = principal(texte, conf, go_id)
    ok = code == 2 and attendu in motif
    echecs += not ok
    print(f"{'OK ' if ok else 'ÉCHEC'} {nom} : code {code} ; {motif}")
from pole import configuration_v56 as cfg  # noqa: E402
conf = cfg.lire_configuration_v56(C8)
s, res, delais = L.verifier_configuration_v67(conf, plan, os.path.dirname(os.path.abspath(C8)))
print("garde 24 sur la configuration v8 :", delais)
sauve = dict(os.environ); os.environ.clear(); os.environ.update(env_propre)
try:
    planT = {"plafond_usd": plan["plafond_modeles_usd"], "parts": {"kimi": plan["plafond_kimi_usd"], "argon": plan["plafond_argon_usd"]}}
    _, _, _, infos = L.roles_reels_v67(res, planT, tempfile.mkdtemp(), tempfile.mkdtemp(), transmettre=False)
finally:
    os.environ.clear(); os.environ.update(sauve)
print("rôles réels v67 (sans porte, sans appel) : délai des adaptateurs kimi", infos["adaptateurs"]["kimi"]["delai_s"], "s, argon",
      infos["adaptateurs"]["argon"]["delai_s"], "s ; budget d'appel des proposeurs", infos["budget_appel_usd"], "USD")
print("bilan :", "tout tient" if echecs == 0 else f"{echecs} cas en écart")
sys.exit(1 if echecs else 0)
