"""Vérification hors ligne : le lanceur v66 (arbre 7e415cba, copie jetable) accepte-t-il la configuration v7 et un texte v2
dont le plan nomme v7 et le GO neuf ? Aucun appel, aucune porte, aucune machine (garde 22 non jouée)."""
import importlib.util, json, os, shutil, sys, hashlib, tempfile
ORG, V6, V7, PREREG_V1, GO_MD, LIGNE = sys.argv[1:7]
sys.path.insert(0, ORG)
os.chdir(ORG)
spec = importlib.util.spec_from_file_location("lanceur", os.path.join(ORG, "demonstrations", "boucle_reelle_v66.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
from pole import configuration_v56 as cfg
from pole import registre_go_v66 as R
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
s6, s7 = sha(V6), sha(V7)
print("sha v6", s6, "\nsha v7", s7)
# texte v2 simulé : le v1 avec le plan qui nomme v7 et le GO neuf
t = open(PREREG_V1, encoding="utf-8").read()
assert t.count("configuration_sha256: " + s6) == 1 and t.count("go: GO-2026-11-10-11\n") == 1
t2 = t.replace("configuration_sha256: " + s6, "configuration_sha256: " + s7).replace("go: GO-2026-11-10-11\n", "go: GO-2026-11-12-06\n")
d = os.path.join(ORG, "prereg"); os.makedirs(d, exist_ok=True)
p2 = os.path.join(d, "preenregistrement-boucle-reelle-organisme-v1-v2.md")
open(p2, "w", encoding="utf-8").write(t2)
open(p2 + ".sha256", "w").write(f"{sha(p2)}  {os.path.basename(p2)}\n")
_, emp, gelees, plan, jeu = L.lire_preenregistrement(p2)
print("texte v2 simulé : accepté ; plan.configuration_sha256 =", plan["configuration_sha256"][:12], "go =", plan["go"], "; fichiers gelés vérifiés :", len(gelees))
# registre des GO : copie de main + ligne proposée
reg = os.path.join(tempfile.mkdtemp(), "go.md"); shutil.copy(GO_MD, reg)
open(reg, "a", encoding="utf-8").write(open(LIGNE, encoding="utf-8").read())
g = R.verifier_go_v66(plan["go"], reg, plan["go_montant_usd"], part=L.PART_DU_GO)
print("GO", g["identifiant"], ": accepté,", g["plafond_lu_usd"], "USD,", g["forme_du_plafond"])
for nom, chemin, attendu in (("v6 (cas sain contre son texte v1)", V6, None), ("v7", V7, plan)):
    conf = cfg.lire_configuration_v56(chemin)
    pl = attendu or plan
    section, resolue = L.verifier_configuration_v66(conf, pl, os.path.dirname(os.path.abspath(chemin)))
    k = resolue["fournisseurs"]["kimi"]["commande"]
    print(nom, ": lire_configuration_v56 et verifier_configuration_v66 acceptent ; proposeur",
          conf["plafonds_session"]["proposeur"], "USD ; kimi max-sortie-proposeur", k[k.index("--max-sortie-proposeur") + 1],
          "; délai commande", k[k.index("--delai-s") + 1], "; délai adaptateur", resolue["fournisseurs"]["kimi"]["delai_s"])
    env = {"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8", "TMPDIR": "/tmp", "POLE_MACHINE_JETABLE_V56": "1"}
    permis = L.L64.exiger_machine_jetable_reel(env, conf)
    planT = {"generations": 2, "cartes_par_proposeur": 6, "m_e_bh": plan["m_e_bh"], "plafond_usd": pl["plafond_modeles_usd"],
             "duree_max_s": pl["duree_h"] * 3600.0, "parts": {"kimi": pl["plafond_kimi_usd"], "argon": pl["plafond_argon_usd"]}, "bras": ["reel"]}
    base = tempfile.mkdtemp(); sortie = tempfile.mkdtemp()
    sauve = dict(os.environ); os.environ.clear(); os.environ.update(env)
    try:
        props, etage, roles, infos = L.L64.roles_reels(resolue, planT, base, sortie, transmettre=False)
    finally:
        os.environ.clear(); os.environ.update(sauve)
    print("   roles_reels (sans porte) : budget d'appel des proposeurs", infos["budget_appel_usd"], "USD ;",
          "adaptateur kimi délai", infos["adaptateurs"]["kimi"].get("delai_s"), "s ; accusés :", infos["accuses_plafond"])
# artefact : configuration v7 contre le texte v1 (qui gèle v6) -> refus attendu
try:
    if s7 != L.lire_plan(t)["configuration_sha256"]:
        raise L.ConfigurationRefusee("v7 contre le texte v1 : empreinte autre que celle que gèle le texte")
except L.ConfigurationRefusee as e:
    print("artefact : v7 sous le texte v1 refusée comme attendu :", e)
os.remove(p2); os.remove(p2 + ".sha256")
