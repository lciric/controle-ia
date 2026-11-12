"""Garde d'encodage v2 et jetons terminaux sur les vrais tokeniseurs (fichiers de données seuls, aucun code distant)."""
import sys, json
from transformers import PreTrainedTokenizerFast
from controle_ia.environnements import noter_rejeu_juges_v2 as v2
from controle_ia.environnements import noter_rejeu_juges_v1 as v1
from controle_ia.environnements.rubrique import CRITERES

for d in sys.argv[1:]:
    tok = PreTrainedTokenizerFast(tokenizer_file=f"{d}/tokenizer.json")
    fins = {tok.convert_tokens_to_ids(t) for t in ("<|eot_id|>", "<|eom_id|>", "<|end_of_text|>")}
    term = v2.jetons_terminaux(tok, fins)
    print(d.rsplit("/", 1)[-1], "vocabulaire", len(tok), "terminaux", len(term), "fins", sorted(fins))
    print("  exemples de terminaux :", [tok.decode([i]) for i in term[:12]])
    try:
        e = v2.controler_encodage_v2(tok, "reel", term)
        print("  garde v2 : PASSE", {k: e[k] for k in ("valeurs_controlees", "valeurs_controlees_v2")}, e["sondes"])
    except Exception as x:
        print("  garde v2 : ARRÊT", x)
    for s in ("BALANCE (0 to 3): 2\n", "REDUNDANCY_PENALTY (-2 to 0): -1\n", "REDUNDANCY_PENALTY: 0\n",
              "SPECIFICITY: 3\nCOHERENCE: 4", "RESULT_REASONING (0 to 3): 2\n\nAnalysis", "BALANCE: 2.5\n",
              "BALANCE: 10\n", "BALANCE: **2**\n", "BALANCE:2\n", "BALANCE: 2 \n", "BALANCE: 2\r\n"):
        ids = tok.encode(s, add_special_tokens=False)
        print("  ", repr(s), [tok.decode([i]) for i in ids])
    # consigne : nombre de jetons
    print("  consigne v2 :", len(tok.encode(v2.CONSIGNE_VERDICT_ECHELLES, add_special_tokens=False)), "jetons ;",
          "bloc à échelles :", len(tok.encode("\n".join(f"{n} ({lo} to {hi}): {hi}" for n, lo, hi in CRITERES) + "\n",
                                                add_special_tokens=False)), "jetons")
    # jetons de saut (déclencheurs de l'arrêt)
    print("  jetons portant un saut de ligne :", len(v2.jetons_de_saut(tok)))
