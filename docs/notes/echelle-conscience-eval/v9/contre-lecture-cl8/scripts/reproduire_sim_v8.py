"""Reproduit des analyses de la simulation scellée v8 (cas nouveaux de la v8) avec le script du commit (un_travail),
et compare au détail versé (lecture, réserves, e(m), rapport des Ec)."""
import importlib.util, json, multiprocessing, pathlib, sys
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("sim8", ARBRE / "scripts" / "simuler_atteignabilite_v8.py")
SIM = importlib.util.module_from_spec(spec); spec.loader.exec_module(SIM)
VER = json.load(open("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v8/atteignabilite-echelle-v8.json", encoding="utf-8"))
STIM = str((ARBRE / "stimuli" / "echelle-v2.json").resolve())
def un(t):
    return SIM.un_travail((STIM,) + t)
if __name__ == "__main__":
    tr = SIM.travaux()
    assert [(c, g) for c, _, g, *_ in tr] == [(e["cas"], e["graine"]) for e in VER["detail"]], "ordre"
    choix = [t for t in tr[386:] if t[2] % 4 == 0][int(sys.argv[3]) if len(sys.argv) > 3 else 0: int(sys.argv[1])]
    with multiprocessing.get_context("fork").Pool(int(sys.argv[2])) as pool:
        res = pool.map(un, choix, chunksize=1)
    det = {(e["cas"], e["graine"]): e for e in VER["detail"]}
    ok = 0
    for cle, graine, lecture, sens, tenues, reserves, coh in res:
        e = det[(cle, graine)]
        same = (lecture == e["lecture"] and reserves == e["reserves"] and coh["ecart_sens"] == e["ecart_sens"]
                and coh["rapport_Ec"] == e["rapport_Ec"] and coh["ecart_sens_ic"] == e["ecart_sens_ic"])
        ok += same
        print(cle, graine, lecture, "identique" if same else "ÉCART")
    print(f"identiques : {ok} / {len(res)}")
