"""Recherche de chaînes dans la liste de concepts (aucune métrique de résultat)."""
import re, sys
concepts = [l.strip() for l in open(sys.argv[1], encoding="ascii") if l.strip()]
print(f"# concepts lus : {len(concepts)}")
termes = [
 "probe","probing","linear probe","monitor","monitoring","sabotage","e value","e-value","evalue",
 "safety","ai safety","alignment","misalignment","control","deception","deceptive","honesty","interpretability",
 "mechanistic","sparse autoencoder","autoencoder","steering","activation","residual stream","reward hacking",
 "reward model","red team","jailbreak","backdoor","trojan","steganography","sandbagging","scheming",
 "situational awareness","chain of thought","reasoning","language model","large language model","llm",
 "transformer","attention","agent","multi agent","reinforcement learning","fine tuning","anomaly detection",
 "out of distribution","adversarial","adversarial attack","sequential test","hypothesis test","martingale",
 "betting","conformal","calibration","classifier","neural network","machine learning","artificial intelligence",
 "watermark","oversight","audit","collusion","evaluation awareness","sycophancy","hallucination",
]
for t in termes:
    mot = [c for c in concepts if re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", c)]
    sous = [c for c in concepts if t in c]
    exact = t in concepts
    ex = "; ".join(sorted(mot, key=len)[:6])
    print(f"{t}\texact={'oui' if exact else 'non'}\tmot_entier={len(mot)}\tsous_chaine={len(sous)}\texemples: {ex}")
