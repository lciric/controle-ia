"""Ordres de grandeur du pilier « génération » de la couche 4 (note de conception v1).

Aucun devis. Aucun appel de modèle, aucun réseau. Chaque prix et chaque profil est une
HYPOTHÈSE NOMMÉE, non vérifiée ; les prix et les profils de l'essai Lean sont repris de
`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md`
(717259ed…, § 4.1 et § 4.2) tels quels, avec leur statut d'origine (« à vérifier »,
« SUPPOSÉ »). Tout le reste est une supposition du rédacteur, marquée S-xx.

Lancement : python -I -B ordres-de-grandeur-pilier-generation-v1.py
"""

# Prix par million de jetons (entrée, sortie), repris de l'essai (§ 4.1), non vérifiés ici.
PRIX = {
    "opus-5.5": (4.0, 20.0),      # « à vérifier » (référence locale claude-api)
    "kimi-k3.1-pro": (2.0, 10.0), # « vérifiés le 30 octobre » (rapporté)
    "argon-prudent": (10.0, 50.0),# barème volontairement haut (page archivée : plus bas jusqu'au 30 novembre)
    "astra": (10.0, 50.0),        # « SUPPOSÉS », identifiant à confirmer
}


def appel(modele, k_entree, k_sortie):
    e, s = PRIX[modele]
    return k_entree * 1e3 * e / 1e6 + k_sortie * 1e3 * s / 1e6


# Coût d'un énoncé candidat traité par toute la chaîne, trois profils.
# Formalisation et preuve : l'item du bras L de l'essai (§ 4.2) sert d'unité.
ITEM_L_ATTENDU = 1.162      # essai, profil supposé
ITEM_L_PIRE_REALISTE = 3.082  # essai, profil pire réaliste (CLP-09)
PLAFOND_ENONCE_OUVERT = 10.0  # S-01 : plafond par énoncé neuf, choix de dessin du rédacteur (non mesuré)

maillons = {
    # S-02 : proposition d'une conjecture, 10 k d'entrée, 3 k de sortie (Opus 5.5) ; borne haute Argon prudent.
    "proposition": (appel("opus-5.5", 10, 3), appel("argon-prudent", 10, 3)),
    # Formalisation et tentative de preuve : item L de l'essai, puis plafond S-01.
    "formalisation_et_preuve": (ITEM_L_ATTENDU, PLAFOND_ENONCE_OUVERT),
    # Fidélité : relecteur d'une autre famille (profil du relecteur de l'essai, 6 k ; 3 k) + rétro-traduction (S-03, même profil).
    "fidelite": (2 * appel("kimi-k3.1-pro", 6, 3), 2 * appel("kimi-k3.1-pro", 6, 3)),
    # Juge de nouveauté à modèle : deux recherches (S-04), 8 k ; 4 k chacune, Argon au barème prudent.
    "nouveaute": (appel("argon-prudent", 8, 4), 2 * appel("argon-prudent", 8, 4)),
    # Juge d'utilité, information seulement (S-05), 6 k ; 3 k, Argon prudent.
    "utilite": (appel("argon-prudent", 6, 3), appel("argon-prudent", 6, 3)),
}

print("Bloc 1 — coût d'un énoncé candidat par maillon (USD ; bas, haut)")
bas = haut = 0.0
for nom, (b, h) in maillons.items():
    print(f"  {nom:28s} {b:7.3f}  {h:7.3f}")
    bas += b
    haut += h
print(f"  {'total par énoncé':28s} {bas:7.3f}  {haut:7.3f}")
print(f"  (variante pire réaliste de l'essai pour la preuve : "
      f"{bas - ITEM_L_ATTENDU + ITEM_L_PIRE_REALISTE:7.3f})")

# Bloc 2 — un pilote hypothétique (S-06 : effectifs choisis pour l'ordre de grandeur, non dimensionnés).
N_CANDIDATS = 200        # énoncés candidats sur les cibles du programme et les mondes plantés
N_CONNUS_PLANTES = 100   # banque d'énoncés connus plantés (juge de nouveauté)
PLANTEUR_ATTENDU, PLANTEUR_PIRE = 0.55, 1.68  # essai § 4.2, par graine (supposé)
ATTAQUE_BAS, ATTAQUE_HAUT = 50.0, 200.0       # S-07 : attaque adaptative de la chaîne (ordre de grandeur)

candidats = (N_CANDIDATS * bas, N_CANDIDATS * haut)
# Chaque connu planté : planteur + formalisation (attendu ou pire réaliste) + juge de nouveauté.
connus = (N_CONNUS_PLANTES * (PLANTEUR_ATTENDU + ITEM_L_ATTENDU + maillons["nouveaute"][0]),
          N_CONNUS_PLANTES * (PLANTEUR_PIRE + ITEM_L_PIRE_REALISTE + maillons["nouveaute"][1]))
print()
print("Bloc 2 — pilote hypothétique (USD ; bas, haut) — aucun devis")
print(f"  {N_CANDIDATS} candidats par toute la chaîne   {candidats[0]:9.2f}  {candidats[1]:9.2f}")
print(f"  {N_CONNUS_PLANTES} connus plantés               {connus[0]:9.2f}  {connus[1]:9.2f}")
print(f"  attaque adaptative (S-07)          {ATTAQUE_BAS:9.2f}  {ATTAQUE_HAUT:9.2f}")
print(f"  banc des tricheurs scriptés        {0.0:9.2f}  {0.0:9.2f}  (processeur seul : voir bloc 3)")
tot = (candidats[0] + connus[0] + ATTAQUE_BAS, candidats[1] + connus[1] + ATTAQUE_HAUT)
print(f"  total d'appels                     {tot[0]:9.2f}  {tot[1]:9.2f}")

# Bloc 3 — machine (S-08 : 15 à 60 minutes de processus par énoncé ; 5 minutes par tricheur scripté ;
# 3 processus Lean en parallèle ; prix horaire 0,10 à 0,40 sans source, borne haute 1,30 : essai § 4.5).
N_TRICHEURS = 100
h_bas = (N_CANDIDATS + N_CONNUS_PLANTES) * 15 / 60 + N_TRICHEURS * 5 / 60
h_haut = (N_CANDIDATS + N_CONNUS_PLANTES) * 60 / 60 + N_TRICHEURS * 5 / 60
mural_bas, mural_haut = h_bas / 3, h_haut / 3
print()
print("Bloc 3 — machine")
print(f"  heures de processus                {h_bas:9.1f}  {h_haut:9.1f}")
print(f"  heures murales (3 en parallèle)    {mural_bas:9.1f}  {mural_haut:9.1f}")
print(f"  coût à 0,10 et 0,40 USD l'heure    {mural_bas * 0.10:9.2f}  {mural_haut * 0.40:9.2f}")
print(f"  coût à la borne haute 1,30         {mural_bas * 1.30:9.2f}  {mural_haut * 1.30:9.2f}")

# Bloc 4 — temps humain (S-09 : 5 % à 20 % des candidats franchissent toutes les gardes mécaniques ;
# 15 à 30 minutes de relecture par énoncé retenu).
for part in (0.05, 0.20):
    n = N_CANDIDATS * part
    print(f"Bloc 4 — part {part:.2f} : {n:5.0f} énoncés à relire ; {n * 15 / 60:5.1f} à {n * 30 / 60:5.1f} heures de relecture humaine")
