"""Révision 6 de T0.6 (r5 + couples de concordance CONC-T06-01 à 05 + en-tête de la mère) et brouillon 19 de T0.7
(brouillon 18 + couples CONC-T07-01 et 02 + NIVEAU_BASE_T06 = 0,95 + en-tête), par la session mère (R-2070).
Chaque « ancien » doit être présent exactement une fois au moment de son application ; sinon arrêt sans écriture (R12 : jamais d'écrasement)."""
import hashlib, json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
h = lambda b: hashlib.sha256(b).hexdigest()
def lire(p, attendu):
    b = (R / p).read_bytes(); assert h(b) == attendu, (p, h(b)); return b.decode("utf-8")
def appliquer(t, couples, nom):
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1: sys.exit(f"{nom} {c['id']} : « ancien » présent {n} fois ; arrêt sans écriture")
        t = t.replace(c["ancien"], c["nouveau"])
    return t
C = "docs/notes/g0-deux-semaines-v1/concordance-t06-t07-v1/"
# --- T0.6 ---
t6 = lire("brouillons/T0.6-organismes-v0-v1-candidat12-r5.md", "8fde62dbd7e44ebdfd163bbf0624c9e91c5aba5a7a50fc1a4fa41e2414d9f9d1")
c6 = json.loads(lire(C + "couples-t06-r5-concordance-v1.json", "70c3319fc1f3a5c45632fd72d39fe47308719c4f4ad78d4890c8ef397a64ca2d"))
t6 = appliquer(t6, c6, "T0.6")
assert h(t6.encode()) == "f446028bb6672580302575e2b033b7bf57dbb39d1653cd34fe14ffc2a511a07f", h(t6.encode())
t6 = appliquer(t6, [
 {"id": "MERE-R6-01 titre", "ancien": "— v1 — candidat 12, révision 4\n", "nouveau": "— v1 — candidat 12, révision 6\n"},
 {"id": "MERE-R6-02 statut", "ancien": "- Statut : **candidat 12, révision 4** (nouveau fichier",
  "nouveau": "- Statut : **candidat 12, révision 6** (session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026, par script `brouillons/T0.6-T0.7-concordance-appliquer-v1.py` ; R-2068, R-2070). **Révision 5** (R-2068) = révision 4 + couples U1 à U13 de la contre-lecture 4 + trois marqueurs remplis par la mère (`EMPREINTE_RAPPORT_CL4_T06`, `PIECES_PUISSANCE_T06`, `DECISION_LAZAR_ECART_DT4_R2041`) ; son titre et ce statut disaient encore « révision 4 » (corrigé ici). **Révision 6** = révision 5 + les cinq couples de la note de concordance avec T0.7 (`docs/notes/g0-deux-semaines-v1/concordance-t06-t07-v1/note-concordance-t06-r5-t07-b18-v1.md`, `6146fe85df179bf28b9fd20b07ec68f3e4a306a138e025370a7457f9fe66792e` ; couples `couples-t06-r5-concordance-v1.json`, `70c3319fc1f3a5c45632fd72d39fe47308719c4f4ad78d4890c8ef397a64ca2d`), puis ces deux couples d'en-tête. **Sections gelées touchées, déclaré** : CONC-T06-01 à 04 changent les sections « Métrique » (une fois) et « Critères de lecture gelés » (trois fois) — règle « mots et coût » limitée aux doses `S25` à `S100` (N-063 v2), « non calculable » distinct de « échoue », vocabulaire du sac de mots figé sur le pli d'apprentissage, témoin lexical retiré des bases rapportées (la chaîne gelée l'exige nul) ; raison : sans eux, la règle ne peut pas être lue par T0.7 (issues L7c, L1 ou L7b à coup sûr) ; aucune hypothèse, prédiction, signe ni seuil ne change ; CONC-T06-05 ajoute la section « Concordance avec T0.7 » hors des sections gelées (pièce de lecture « mots et coût » jouée après la course, hors de l'arbre gelé, qui ne lit jamais `lecture-sondes-t06.json`). **Contre-lecture 5 (R2) du différentiel r4 → r6 à faire par un autre modèle que l'analyste et la mère** avant le scellement. Statut antérieur, révision 4 : **candidat 12, révision 4** (nouveau fichier"},
], "T0.6 en-tête")
o6 = R / "brouillons/T0.6-organismes-v0-v1-candidat12-r6.md"
# --- T0.7 ---
t7 = lire("brouillons/T0.7-sondes-v0-v1-brouillon18.md", "fe02da17018c04765ab98a6251ef3216dc88a49dadd0db8786328ce507b8a382")
c7 = json.loads(lire(C + "couples-t07-b18-concordance-v1.json", "d588ba87418a8a1a3e5761203d9619f26fd454cb47375a1225c2f3d88facf3f6"))
t7 = appliquer(t7, c7, "T0.7")
assert h(t7.encode()) == "7aa36de12124865a99b3e14c53b02236521702d69a62929ab0d890b32ea049d2", h(t7.encode())
n = t7.count("<<NIVEAU_BASE_T06>>"); assert n == 9, n
t7 = t7.replace("<<NIVEAU_BASE_T06>>", "0,95")
t7 = appliquer(t7, [
 {"id": "MERE-B19-01 titre", "ancien": "— v1 — brouillon 18\n", "nouveau": "— v1 — brouillon 19\n"},
 {"id": "MERE-B19-02 statut", "ancien": "- Statut : **brouillon 18**, écrit le 2026-11-10",
  "nouveau": "- Statut : **brouillon 19** (session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026, par script `brouillons/T0.6-T0.7-concordance-appliquer-v1.py`, R-2070) = brouillon 18 + couples CONC-T07-01 et 02 de la note de concordance (`docs/notes/g0-deux-semaines-v1/concordance-t06-t07-v1/couples-t07-b18-concordance-v1.json`, `d588ba87418a8a1a3e5761203d9619f26fd454cb47375a1225c2f3d88facf3f6` ; aucune section gelée touchée) + marqueur `NIVEAU_BASE_T06` rempli à 0,95 (neuf occurrences ; T0.6 : « comme pour les sondes », lues à 95 % ; code : `niveau=0.95` par défaut, jamais modifié par `lanceur_v6`, note de concordance, D7) + ces deux couples d'en-tête. Le texte de T0.6 visé est la révision 6 (`brouillons/T0.6-organismes-v0-v1-candidat12-r6.md`) ; son empreinte scellée entrera par `EMPREINTE_PREREG_T06`. Statut antérieur : **brouillon 18**, écrit le 2026-11-10"},
], "T0.7 en-tête")
o7 = R / "brouillons/T0.7-sondes-v0-v1-brouillon19.md"
for o in (o6, o7):
    assert not o.exists(), f"R12 : {o} existe déjà"
o6.write_text(t6, encoding="utf-8"); o7.write_text(t7, encoding="utf-8")
print("T0.6 r6 :", h(t6.encode())); print("T0.7 b19 :", h(t7.encode()))
