"""Banc de la chaîne v2 : pilote jouet arrêté et notations jouet (réponses remplacées), construits dans le clone
jetable du banc ; configuration jouet v2 scellée. Lancer depuis la racine du clone, PYTHONPATH=src."""
import json, sys
from pathlib import Path
sys.path.insert(0, "tests")
from _pytest.monkeypatch import MonkeyPatch
from controle_ia.environnements import noter_pilote_a as npa, pilote_a as pa, noter_rejeu_juges_v1 as nrj
from controle_ia.environnements import noter_rejeu_juges_v2 as nrj2
from controle_ia.environnements.rubrique import CRITERES
from controle_ia.scellement import sceller
import test_noter_pilote_a as tn
import test_noter_rejeu_juges_v1 as tr
depot = Path(".").resolve()
mp = MonkeyPatch()
f, _ = tn._construire_pilote_arrete(depot, mp)
vrai = pa.noter_ensembles
def noter(m, fmt, morceau, graines, lot, max_nouveaux, temperature, echeance=None):
    sortie = vrai(m, fmt, morceau, graines, lot, max_nouveaux, temperature, echeance=echeance)
    for x in sortie:
        texte, tronquee = tr.TEXTES[x["cle"].split("/", 1)[1]]
        x.update(reponse=texte, tronquee=tronquee, jetons_reponse=len(tr.TOK.encode(texte, add_special_tokens=False)),
                 **nrj.lecture_ecrite(texte, CRITERES, tronquee))
    return sortie
mp.setattr(npa, "noter_ensembles", noter)
npa.executer(tn._config(), depot, tr.NOTATIONS, None, str(f), autoriser_depot_sale=True)
mp.undo()
c = tn._config()
config = {**{k: c[k] for k in nrj.CLES_EGALES_AUX_NOTATIONS}, "mode": "jouet", "run_notations": tr.NOTATIONS,
          "phases": [{"juge": j, "variante": nrj2.VARIANTE, "duree_max_s": 600} for j in ("jouet-8B", "jouet-3B")],
          "juge_decisif": "jouet-8B", "max_nouveaux_verdict": 64, "masse_min_appui": 0.5, "duree_globale_s": 1800}
nrj2.exiger_config_rejeu_v2(config)
Path("config-rejeu-v2-jouet.json").write_text(json.dumps(config, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
sceller("config-rejeu-v2-jouet.json")
Path("taches-jouet.txt").write_text(str(f) + "\n")
print("construit ; tâches", f)
