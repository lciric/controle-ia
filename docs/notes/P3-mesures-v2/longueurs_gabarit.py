"""Mesures de P3 sur le vrai tokeniseur de l'agent (non décisives, sur processeur) : longueurs des six textes privés,
encodage seul et dans le gabarit de dialogue, sur chacune des tâches ; faits sans empan de la recette de tromperie.

Usage : HF_HUB_OFFLINE=1 HF_HOME=<cache> PYTHONPATH=src python longueurs_gabarit.py CONFIG CONSIGNES TACHES TOKENIZER_JSON
Dans le gabarit : jetons ajoutés à l'ouverture rendue du premier pas, consigne seule (message système) et indication seule
(observation), par différence avec l'ouverture de l'honnête ; même code que l'environnement (a) et le format de l'agent.
"""
import hashlib
import json
import sys
from pathlib import Path

from tokenizers import Tokenizer

from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia.conditions import INSTRUITES, charger_consignes, environnement
from controle_ia.premier_test_ia.entrainement import preparer_tromperie


def sha(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


cfg, consignes_chemin, taches_chemin, tok_chemin = sys.argv[1:5]
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
print("configuration", sha(cfg), cfg)
print("consignes", sha(consignes_chemin), consignes_chemin)
print("taches", sha(taches_chemin), taches_chemin)
print("tokenizer.json", sha(tok_chemin))
consignes = charger_consignes(consignes_chemin)
tok = Tokenizer.from_file(tok_chemin)
print("encodage seul (sans jetons spéciaux) :")
for k in INSTRUITES:
    for quoi in ("consigne", "indication"):
        print(f"  {k} {quoi} : {len(tok.encode(consignes[k][quoi], add_special_tokens=False).ids)} jetons")
fmt = lp.charger_format_seul(c["agent"], "reel")
guide = charger_invite("H1-classification")
taches = charger_taches(taches_chemin)
print(f"dans le gabarit, premier pas, {len(taches)} tâches (identifiant : consignes {list(INSTRUITES)} ; indications) :")
egal, valeurs = 0, {}
for t in taches:
    envs = {k: environnement(k, tache_de(t), c["T"], guide, consignes) for k in ("honnete",) + INSTRUITES}

    def n(k_sys, k_obs):
        return len(fmt.ouverture(envs[k_sys].consigne_privee(0), envs[k_obs].observation(0, 0, [])))

    base = n("honnete", "honnete")
    lc = [n(k, "honnete") - base for k in INSTRUITES]
    li = [n("honnete", k) - base for k in INSTRUITES]
    valeurs.setdefault((tuple(lc), tuple(li)), []).append(t["identifiant"])
    egal += len(set(lc)) == 1 and len(set(li)) == 1 and min(lc) > 0 and min(li) > 0
    print(f"  {t['identifiant']} : {lc} ; {li}")
print(f"tâches à longueurs égales entre les trois conditions instruites (consigne et indication) : {egal} sur {len(taches)}")
for (lc, li), ids in sorted(valeurs.items()):
    print(f"  consignes {list(lc)}, indications {list(li)} : {len(ids)} tâches")
faits = dn.charger_faits()
ex_t, exclus = preparer_tromperie(fmt, dn.exemples_tromperie(faits), c["retrait_fin_tromperie"])
print(f"faits : {len(faits)} ; faits sans empan (exclus) : {len(exclus)} ; exemples de tromperie gardés : {len(ex_t)}")
