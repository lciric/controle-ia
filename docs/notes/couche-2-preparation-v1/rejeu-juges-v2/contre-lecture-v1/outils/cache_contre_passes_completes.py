"""Lecture v2 par le cache rogné puis prolongé contre une référence par passes complètes (une passe sans cache par
valeur), sur un modèle jouet de type Llama au vocabulaire du vrai tokeniseur de Llama 3.1, sur processeur.
Usage : python cache_contre_passes_completes.py DOSSIER_TOKENISEUR"""
import math, sys, torch
from transformers import PreTrainedTokenizerFast, LlamaConfig, LlamaForCausalLM
from controle_ia.environnements import noter_rejeu_juges_v2 as v2
from controle_ia.environnements import noter_rejeu_juges_v1 as v1
from controle_ia.environnements.rubrique import CRITERES

tok = PreTrainedTokenizerFast(tokenizer_file=f"{sys.argv[1]}/tokenizer.json")
fins = {tok.convert_tokens_to_ids(t) for t in ("<|eot_id|>", "<|eom_id|>", "<|end_of_text|>")}
term = v2.jetons_terminaux(tok, fins)

def modele(graine, dtype=torch.float32):
    cfg = LlamaConfig(vocab_size=len(tok), hidden_size=64, intermediate_size=128, num_hidden_layers=3,
                      num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=4096,
                      tie_word_embeddings=False)
    torch.manual_seed(graine)
    m = LlamaForCausalLM(cfg).eval()
    with torch.no_grad():   # logits plus contrastés : masses loin de 0 et de 1
        m.lm_head.weight.mul_(40.0)
    return m.to(dtype)

def reference(m, contexte, texte):
    car = v2.positions_des_valeurs_v2(texte, CRITERES)
    ids_rep, offs = v1._encoder(tok, texte)
    sortie = {}
    for nom, lo, hi in CRITERES:
        k, prefixe = v1.jeton_de_decision(texte, offs, car[nom])
        base = list(contexte) + ids_rep[:k]
        p = {}
        for v, c in v1.candidats_de_valeur(tok, prefixe, lo, hi).items():
            with torch.no_grad():
                lg = m(input_ids=torch.tensor([base + c]), use_cache=False).logits[0]
            lp = torch.log_softmax(lg.float(), -1)
            s = sum(float(lp[len(base) - 1 + t, c[t]]) for t in range(len(c)))
            p[v] = math.exp(s + float(torch.logsumexp(lp[len(base) - 1 + len(c), term], 0)))
        sortie[nom] = p
    return sortie

def bloc(echelle=True, brut=None):
    notes = {"SPECIFICITY": 3, "COHERENCE": 2, "COVERAGE": 4, "FEASIBILITY": 1, "NOVELTY": 2, "RIGOR": 3,
             "BALANCE": 1, "RESULT_REASONING": 2, "REDUNDANCY_PENALTY": -1, "IRRELEVANCE_PENALTY": 0}
    brut = brut or {}
    return "\n".join((f"{n} ({lo} to {hi}):" if echelle else f"{n}:") + f" {brut.get(n, notes[n])}"
                     for n, lo, hi in CRITERES)

CAS = {
    "forme à échelle, saine": bloc(),
    "forme v1": bloc(echelle=False),
    "demi-point, gras, dix, sans espace, espaces de fin": bloc(brut={"COHERENCE": "2.5", "RIGOR": "**3**",
        "SPECIFICITY": "10", "BALANCE": "", "RESULT_REASONING": "2  "}).replace("BALANCE (0 to 3): ", "BALANCE (0 to 3):2"),
    "pénalités -2 et 0, dernière ligne à -2": bloc(brut={"REDUNDANCY_PENALTY": "-2", "IRRELEVANCE_PENALTY": "-2"}),
    "préambule et puces": "Scores:\n" + "\n".join("- " + l for l in bloc().splitlines()),
}
contexte = tok.encode("<|begin_of_text|>Rate the following ensemble of research questions." * 3, add_special_tokens=False)
pire = 0.0
for graine in (1, 2, 3):
    m = modele(graine)
    for nom_cas, texte in CAS.items():
        r = v2.lire_par_probabilite_v2(m, tok, contexte, texte, CRITERES, True, 0.0, term)
        ref = reference(m, contexte, texte)
        for nom, p in ref.items():
            lu = r["criteres"][nom]
            M = sum(p.values())
            ecart_m = abs(lu["masse"] - M) / max(M, 1e-300)
            ecart_p = max(abs(lu["probabilites"][str(v)] - x / M) for v, x in p.items())
            pire = max(pire, ecart_m, ecart_p)
            assert ecart_m < 1e-4 and ecart_p < 1e-5, (graine, nom_cas, nom, ecart_m, ecart_p)
        print(f"graine {graine} ; {nom_cas} : passes {r['passes']} ; masses "
              f"{min(l['masse'] for l in r['criteres'].values()):.3g} à {max(l['masse'] for l in r['criteres'].values()):.3g} ; égal à la référence")
print(f"écart relatif maximal (masse ou probabilité renormalisée), simple précision : {pire:.2e}")
# demi-précision bfloat16 : même modèle, chemin du cache contre passes complètes, tous deux en bfloat16
m = modele(1, torch.bfloat16)
r = v2.lire_par_probabilite_v2(m, tok, contexte, CAS["forme à échelle, saine"], CRITERES, True, 0.0, term)
ref = reference(m, contexte, CAS["forme à échelle, saine"])
e = max(abs(math.log(r["criteres"][n]["masse"]) - math.log(sum(p.values()))) for n, p in ref.items())
print(f"bfloat16 : écart maximal de log-masse cache contre passes complètes : {e:.3g}")
