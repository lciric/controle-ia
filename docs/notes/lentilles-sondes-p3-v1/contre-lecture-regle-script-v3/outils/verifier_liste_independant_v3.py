"""Contre-lecture v3 : contrôle indépendant de la liste de mots v3 contre le vrai vocabulaire (vocabulaire seul).

N'importe pas le script v3. Décode le tokenizer.json « ByteLevel » par sa propre table, retient les jetons
« espace + lettres » (forme stricte), et vérifie : (1) chaque mot de la liste finale a au moins un jeton ;
(2) chaque mot retiré par E6 (lu dans le candidat moins la liste finale) n'en a aucun ; (3) comptes de jetons.
Usage : python3 -I -B verifier_liste_independant_v3.py TOKENIZER CANDIDAT FINALE
"""
import json, sys, hashlib

def table():
    bs = list(range(33, 127)) + list(range(161, 173)) + list(range(174, 256))
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b); cs.append(256 + n); n += 1
    return {chr(c): b for b, c in zip(bs, cs)}

tok, cand, fin = sys.argv[1:4]
print("tokenizer", hashlib.sha256(open(tok, "rb").read()).hexdigest()[:12],
      "candidat", hashlib.sha256(open(cand, "rb").read()).hexdigest()[:12],
      "finale", hashlib.sha256(open(fin, "rb").read()).hexdigest()[:12])
inv = table()
d = json.load(open(tok, encoding="utf-8"))
jetons = {}
for s in d["model"]["vocab"]:
    try:
        t = bytes(inv[ch] for ch in s).decode("utf-8")
    except (KeyError, UnicodeDecodeError):
        continue
    if len(t) > 1 and t[0] == " " and t[1:].isascii() and t[1:].isalpha():
        jetons.setdefault(t[1:].lower(), []).append(t)
C = json.load(open(cand, encoding="utf-8")); F = json.load(open(fin, encoding="utf-8"))
ok = True
for c in ("tromperie", "enjeux"):
    sans = [m for m in F[c] if m not in jetons]
    e6 = [m for m in C[c] if m not in F[c]]
    e6_avec = [m for m in e6 if m in jetons]
    njet = sum(len(jetons[m]) for m in F[c] if m in jetons)
    print(f"{c} : {len(F[c])} mots, {njet} jetons ; finale sans jeton : {sans} ; E6 retirés {len(e6)}, dont avec jeton : {e6_avec}")
    ok &= not sans and not e6_avec and set(F[c]) <= set(C[c])
print("communs finale :", sorted(set(F["tromperie"]) & set(F["enjeux"])))
print("BILAN", "OK" if ok else "KO")
