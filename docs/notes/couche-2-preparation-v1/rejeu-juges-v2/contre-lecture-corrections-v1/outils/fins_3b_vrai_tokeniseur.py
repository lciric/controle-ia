"""CLC : diagnostic des fins de tour du 3B sur les vrais tokeniseurs (données seules) et la configuration de génération
publique (copie unsloth, non vérifiée contre la révision figée). Rejoue l'ancienne et la nouvelle comparaison."""
import json, sys
from types import SimpleNamespace
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from transformers import AutoTokenizer
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import fins_du_modele
from controle_ia.environnements import noter_rejeu_juges_v2 as v2
from controle_ia.environnements.lancer_pilote_a import controler_format

dtok, dgen = sys.argv[1], sys.argv[2]
var = {"date_string": "26 Jul 2024"}
cfg = {"mode": "reel", "variante_juge": "b0"}
spec = {"nom": "3B", "texte_attendu_ouverture": "Today Date: 26 Jul 2024", "variables_gabarit": var}
tok = AutoTokenizer.from_pretrained(dtok)
gen = json.load(open(dgen))
debut = FormatChat(tok, variables=var)                       # charger_format_seul
charge = FormatChat(AutoTokenizer.from_pretrained(dtok), variables=var)   # charger_modele_et_format
modele = SimpleNamespace(generation_config=SimpleNamespace(eos_token_id=gen["eos_token_id"]))
charge.fins = fins_du_modele(modele, charge.tok) | {charge._pieces(("x", "y"))["cloture"][0]}
print("fins début", sorted(debut.fins), "fins chargé", sorted(charge.fins))
try:
    print("format égal :", controler_format(debut, spec, "juge", cfg) == controler_format(charge, spec, "juge", cfg))
except Exception as x:
    print("format : exception", x)
t0 = v2.jetons_terminaux(debut.tok, debut.fins); t1 = v2.jetons_terminaux(charge.tok, charge.fins)
e0 = v2.controler_encodage_v2(debut.tok, "reel", t0); e1 = v2.controler_encodage_v2(charge.tok, "reel", t1)
print("ANCIENNE garde : terminaux égaux", t0 == t1, "; encodage égal", e0 == e1, "=> arrêt" if (t0 != t1 or v2.controler_encodage_v2(charge.tok, "reel", t0) != e0) else "=> passe")
print("  ajoutés :", sorted(set(t1) - set(t0)), [charge.tok.decode([i]) for i in sorted(set(t1) - set(t0))])
sans = lambda e: {k: v for k, v in e.items() if k != "terminaux"}
nouv = v2.jetons_terminaux(charge.tok, set()) == v2.jetons_terminaux(debut.tok, set()) and sans(e1) == sans(e0)
print("NOUVELLE garde : passe" if nouv else "NOUVELLE garde : arrêt")
print("sauts égaux :", v2.jetons_de_saut(debut.tok) == v2.jetons_de_saut(charge.tok))
