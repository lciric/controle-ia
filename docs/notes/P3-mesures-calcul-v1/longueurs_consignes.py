"""Longueurs en jetons des consignes et indications privées de P3, lues dans le fichier des consignes (citations « > »).

Usage : python -I longueurs_consignes.py TOKENIZER_JSON FICHIER_CONSIGNES
Chaque bloc de lignes « > » consécutives est un texte (lignes jointes par une espace) ; encodage sans jetons spéciaux.
"""
import hashlib
import sys

from tokenizers import Tokenizer

tok_chemin, consignes = sys.argv[1], sys.argv[2]
tok = Tokenizer.from_file(tok_chemin)
blocs, courant = [], []
for ligne in open(consignes, encoding="utf-8"):
    if ligne.startswith("> "):
        courant.append(ligne[2:].strip())
    elif courant:
        blocs.append(" ".join(courant))
        courant = []
if courant:
    blocs.append(" ".join(courant))
print("tokenizer.json", hashlib.sha256(open(tok_chemin, "rb").read()).hexdigest())
print("consignes", hashlib.sha256(open(consignes, "rb").read()).hexdigest())
for k, b in enumerate(blocs):
    print(k, len(tok.encode(b, add_special_tokens=False).ids), hashlib.sha256(b.encode("utf-8")).hexdigest()[:16], b[:60])
