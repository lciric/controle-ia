"""Calcul du devis v4 de la course 2 (génération 1) et du pré-pilote recentré.

Lignée session-depot, 30 octobre 2026. Aucun appel réseau, aucune dépense : arithmétique sur des bases écrites
ci-dessous, chacune marquée OBSERVÉ (registre cité), SOURCÉ (fichier du dépôt cité) ou SUPPOSÉ.
Usage : python3 -I calcul-devis-course-2-et-pre-pilote-v4.py > calcul-devis-course-2-et-pre-pilote-v4.sortie.txt
Graines (R9) : numpy.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)), cle_de_tache recopiée à l'identique
de src/controle_ia/manifeste.py (8 premiers octets du SHA-256 du nom de tâche).
"""
import hashlib
import sys

import numpy as np

RACINE = 20261030
TIRAGES = 20000


def cle_de_tache(tache: str) -> int:
    return int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")


def generateur(tache: str) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(tache),)))


# ---------------------------------------------------------------- prix (USD par million de jetons : entrée, sortie)
PRIX = {
    "opus": (4.0, 20.0),     # SOURCÉ : collisionneur_v2.py (MODELES, 0e63febd…) ; devis v1 § 1
    "kimi": (2.0, 10.0),     # SOURCÉ : page de prix lue le 30 oct. (devis v1 § 1, c62210a0…) ; OBSERVÉ conforme (depenses l. 255)
    "argon": (8.3, 41.5),    # entrée : borne lue par Lazar (R-718) ; sortie : SUPPOSÉ (commande_argon_v3d.py, 46c91df4…)
    "fable": (10.0, 50.0),   # SOURCÉ : collisionneur_v2.py (MODELES)
    "sonnet": (4.0, 20.0),   # SUPPOSÉ : prix absent du dépôt ; compté au prix d'Opus 5.5 par prudence
}


def cout(modele: str, entree: float, sortie: float) -> float:
    pe, ps = PRIX[modele]
    return entree * pe / 1e6 + sortie * ps / 1e6


# ---------------------------------------------------------------- profils d'un acte (jetons d'entrée, de sortie)
# OBSERVÉ : Kimi juge des 29 fiches de la course 1, un appel, 222 635 / 31 010 jetons, 0,755 USD (depenses l. 255).
JUGE_KIMI = (222_635 / 29, 31_010 / 29)
# OBSERVÉ en coût seulement : Opus 3,31 USD / 29 fiches (6 appels), Argon 2,28 / 29 (depenses l. 252) ;
# découpage en jetons SUPPOSÉ, choisi pour retrouver le coût observé au prix ci-dessus.
JUGE_OPUS = (17_000, 2_300)
JUGE_ARGON = (5_000, 900)
AIGUILLAGE = (8_500, 1_150)           # SUPPOSÉ (devis v3) : moitié d'un jugement d'Opus, au prix d'Opus
ANTERIORITE = (25_000, 5_000)          # SUPPOSÉ (devis v3) ; recherches comptées à part
RECHERCHES_PAR_FICHE, PRIX_RECHERCHE = 5, 0.01   # SUPPOSÉ : prix d'une recherche non lu
ETIQUETTE = (4_000, 450)               # SUPPOSÉ (brouillon 3 : 0,025 par lecture), au prix d'Opus
FUSION = (50_000, 30_000)              # SUPPOSÉ (brouillon 3 : 0,40 par fusion), par Kimi
RELECTEUR = (3_000, 340)               # SUPPOSÉ (brouillon 3 : 1,4 / 30 rendus), Fable 5.1 (D-f)
RENDU = {"kimi": 0.057, "argon": 0.079, "sonnet": 0.079}  # SUPPOSÉ (brouillon 3 : un rendu au prix d'un jugement)
PASSE_KIMI_COURSE = (250_000, 75_000)  # SUPPOSÉ : passe de 8 fiches ; retrouve 2,5 USD par sous-session (devis v3)
PASSE_ARGON_COURSE = (150_000, 24_000) # SUPPOSÉ : retrouve 4,5 USD par sous-session (devis v3 ; course 1 : 6,00 OBSERVÉ)
PASSE_KIMI_PREPILOTE = (300_000, 140_000)  # SUPPOSÉ : 10 fiches, raisonnement long (brouillon 3 : 2,0 la passe)

# coûts unitaires au pire (devis v3 : facteur 1,34 sur les juges, facteur 2 de plus sur Kimi ; antériorité × 3)
PIRE_UNITAIRE = {"juge_opus": 0.153, "juge_argon": 0.105, "juge_kimi": 0.153, "aiguillage": 0.153, "anteriorite": 0.75}


def u(modele, profil):
    return cout(modele, *profil)


UNIT = {
    "juge_opus": u("opus", JUGE_OPUS),
    "juge_argon": u("argon", JUGE_ARGON),
    "juge_kimi": u("kimi", JUGE_KIMI),
    "aiguillage": u("opus", AIGUILLAGE),
    "anteriorite": u("opus", ANTERIORITE) + RECHERCHES_PAR_FICHE * PRIX_RECHERCHE,
    "etiquette": u("opus", ETIQUETTE),
    "fusion": u("kimi", FUSION),
    "relecteur": u("fable", RELECTEUR),
}


def ligne(nom, appels, entree, sortie, attendu, pire):
    return {"poste": nom, "appels": appels, "entree": entree, "sortie": sortie, "attendu": attendu, "pire": pire}


# ================================================================ PRÉ-PILOTE RECENTRÉ (R-634, R-638, R-639)
N_TEMOINS = 24            # SUPPOSÉ (brouillon 4 non écrit) : P 8, N 11, C 3, G 2 ; un seul rendu par fond (auto-préférence retirée)
REND = {"kimi": 8, "argon": 8, "sonnet": 8}   # SUPPOSÉ : trois metteurs en forme, comme le brouillon 3
N_KIMI_PASSE1 = 10        # garde de niveau méthode chez Kimi (brouillon 3 : ≤ 10)
N_CONCRETS, N_DIFFICILES = 12, 6
N_FUSIONS_PP = 2          # une paire par bras, deux bras (méta, Gu-Krenn)
N_ANT_PP = 8
N_ETIQ_PP = 2 * N_KIMI_PASSE1

pp = []
# rédacteur : 24 squelettes et déclarations, 8 fiches d'antériorité, 6 difficiles ; 5 appels de 45 000 jetons d'entrée
red_e, red_s = 5 * 45_000, N_TEMOINS * 2_000 + N_ANT_PP * 2_500 + N_DIFFICILES * 2_500
pp.append(ligne("Rédacteur (Sonnet 5.5, au prix d'Opus)", 5, red_e, red_s, cout("sonnet", red_e, red_s), 1.5 * cout("sonnet", red_e, red_s)))
r_att = sum(REND[m] * RENDU[m] for m in REND)
pp.append(ligne("Rendus des 24 témoins (Kimi 8, Argon 8, T 8)", 24, None, None, r_att, 1.4 * r_att))
pp.append(ligne("Relecteur (Fable 5.1), 24 rendus", 24, 24 * RELECTEUR[0], 24 * RELECTEUR[1], 24 * UNIT["relecteur"], 1.36 * 24 * UNIT["relecteur"]))
k_att = cout("kimi", *PASSE_KIMI_PREPILOTE)
pp.append(ligne("Kimi proposeur, passe 1 (garde de niveau méthode)", 4, PASSE_KIMI_PREPILOTE[0], PASSE_KIMI_PREPILOTE[1], k_att, 2 * k_att))
n_aig = N_TEMOINS + N_KIMI_PASSE1 + N_DIFFICILES + N_CONCRETS + N_FUSIONS_PP
n_second, n_adjud_pire = N_KIMI_PASSE1, N_KIMI_PASSE1
aig_att = (n_aig + n_second) * UNIT["aiguillage"] + 0.1 + 0.3
aig_pire = (n_aig + n_second + n_adjud_pire) * PIRE_UNITAIRE["aiguillage"] + 0.3
pp.append(ligne(f"Aiguillage : aiguilleur {n_aig}, second lecteur {n_second}, adjudicateur ≤ {n_adjud_pire}, nouvel essai",
                n_aig + n_second, (n_aig + n_second) * AIGUILLAGE[0], (n_aig + n_second) * AIGUILLAGE[1], aig_att, aig_pire))
n_j = N_TEMOINS + N_FUSIONS_PP
for nom, cle, prof in (("Opus 5.5", "juge_opus", JUGE_OPUS), ("Argon", "juge_argon", JUGE_ARGON), ("Kimi", "juge_kimi", JUGE_KIMI)):
    pp.append(ligne(f"Juge {nom}, étalonnage : {n_j} fiches (24 témoins, 2 fusions)", "1 à 6", n_j * prof[0], n_j * prof[1],
                    n_j * UNIT[cle], n_j * PIRE_UNITAIRE[cle]))
pp.append(ligne("Antériorité (Opus 5.5 avec recherche), 8 fiches", N_ANT_PP, N_ANT_PP * ANTERIORITE[0], N_ANT_PP * ANTERIORITE[1],
                N_ANT_PP * UNIT["anteriorite"], N_ANT_PP * PIRE_UNITAIRE["anteriorite"]))
b_att = N_ETIQ_PP * UNIT["etiquette"] + N_FUSIONS_PP * UNIT["fusion"]
pp.append(ligne("Bisociation : 2 lecteurs × 10 fiches ; 2 fusions par Kimi ; notes sur processeur", N_ETIQ_PP + N_FUSIONS_PP,
                N_ETIQ_PP * ETIQUETTE[0] + N_FUSIONS_PP * FUSION[0], N_ETIQ_PP * ETIQUETTE[1] + N_FUSIONS_PP * FUSION[1], b_att, 1.5 * b_att))
pp.append(ligne("Appels de contrôle (un par modèle, cinq modèles)", 5, None, None, 0.01, 0.5))

# seconde version des témoins si les contrôles de forme échouent (brouillon 3 : C5 réussit en une version avec 0,56)
P_SECONDE = 0.44
sec = 0.6 * pp[0]["attendu"] + pp[1]["attendu"] + pp[2]["attendu"] + N_TEMOINS * UNIT["aiguillage"]
sec_pire = 0.6 * pp[0]["pire"] + pp[1]["pire"] + pp[2]["pire"] + N_TEMOINS * PIRE_UNITAIRE["aiguillage"]

# options hors liste de R-634 (à trancher au brouillon 4)
opt_tableau = (k_att, 2 * k_att)                       # passe « tableau » de Kimi
opt_memoire = (1.0 + 0.7, 1.4 + 1.0)                   # paraphrases + table seule de l'axe 7 (brouillon 3)

# ================================================================ COURSE 2 = GÉNÉRATION 1
SS = 4                     # sous-sessions (texte I axes 1-5 ; axe 7 ; axe 6 sans pistes ; axe 6 avec pistes)
FICHES_PAR_PROPOSEUR = 16  # 2 passes de 8
TEMOINS_PAR_SS = 8         # devis v3 ; notés par les trois juges
NOTABLES_PAR_SS = 10       # devis v3 : antériorité sur les fiches notables


def course(ss: int, fusions_par_ss: int, temoins_par_ss: int = TEMOINS_PAR_SS, notables_par_ss: int = NOTABLES_PAR_SS):
    f_kimi = f_argon = ss * FICHES_PAR_PROPOSEUR
    nf = ss * fusions_par_ss
    nt = ss * temoins_par_ss
    lignes = []
    e, s = 2 * ss * PASSE_KIMI_COURSE[0], 2 * ss * PASSE_KIMI_COURSE[1]
    lignes.append(ligne(f"Kimi proposeur ({ss} × 2 passes de 8)", f"≈ {6 * ss}", e, s, cout("kimi", e, s), 9.5 * ss))
    e, s = 2 * ss * PASSE_ARGON_COURSE[0], 2 * ss * PASSE_ARGON_COURSE[1]
    lignes.append(ligne(f"Argon proposeur ({ss} × 2 passes de 8)", f"≈ {6 * ss}", e, s, cout("argon", e, s), 6.0 * ss))
    lignes.append(ligne("Contrôles d'Argon (course 1 : 1,75 OBSERVÉ)", "—", None, None, 1.75 * ss / 4, 3.0 * ss / 4))
    na = f_kimi + f_argon + nf
    lignes.append(ligne(f"Aiguilleur ({na} fiches, avant tout juge)", na, na * AIGUILLAGE[0], na * AIGUILLAGE[1],
                        na * UNIT["aiguillage"], na * PIRE_UNITAIRE["aiguillage"]))
    # notation croisée : fiches de Kimi et fusions (faites par Kimi) notées par Argon ; fiches d'Argon par Kimi ;
    # témoins notés par Kimi et par Argon
    n_par_argon = f_kimi + nf + nt
    n_par_kimi = f_argon + nt
    att = n_par_argon * UNIT["juge_argon"] + n_par_kimi * UNIT["juge_kimi"]
    pire = n_par_argon * PIRE_UNITAIRE["juge_argon"] + n_par_kimi * PIRE_UNITAIRE["juge_kimi"]
    lignes.append(ligne(f"Juges croisés : Argon {n_par_argon}, Kimi {n_par_kimi} (témoins notés par les deux)", "≈ 2 par lot",
                        n_par_argon * JUGE_ARGON[0] + n_par_kimi * JUGE_KIMI[0], n_par_argon * JUGE_ARGON[1] + n_par_kimi * JUGE_KIMI[1], att, pire))
    no = f_kimi + f_argon + nf + nt
    lignes.append(ligne(f"Opus 5.5 troisième juge ({no} : fiches, fusions, témoins)", f"≈ {6 * ss}", no * JUGE_OPUS[0], no * JUGE_OPUS[1],
                        no * UNIT["juge_opus"], no * PIRE_UNITAIRE["juge_opus"]))
    nant = ss * notables_par_ss + nf // 2
    lignes.append(ligne(f"Antériorité ({nant} : {notables_par_ss} notables par sous-session, la moitié des fusions)", nant, nant * ANTERIORITE[0],
                        nant * ANTERIORITE[1], nant * UNIT["anteriorite"], nant * PIRE_UNITAIRE["anteriorite"]))
    ne = ss * 2 * 2 * 8   # deux lecteurs sur les 8 fiches de passe 1 de chacun des deux proposeurs, par sous-session
    b = ne * UNIT["etiquette"] + nf * UNIT["fusion"]
    lignes.append(ligne(f"Bisociation : {ne} lectures d'étiquettes, {nf} fusions (bras méta et Gu-Krenn)", ne + nf,
                        ne * ETIQUETTE[0] + nf * FUSION[0], ne * ETIQUETTE[1] + nf * FUSION[1], b, 1.5 * b))
    lignes.append(ligne("Tableau minimal (programme) ; appels de contrôle", "—", None, None, 0.01, 0.5))
    return lignes


def fmt(x):
    if x is None:
        return "—"
    if isinstance(x, str):
        return x
    if isinstance(x, int) and x > 1000:
        return f"{x:,}".replace(",", " ")
    if isinstance(x, float) and x > 1000:
        return f"{round(x):,}".replace(",", " ")
    return f"{x}"


def imprimer(titre, lignes):
    print(f"\n== {titre} ==")
    print("poste | appels | jetons d'entrée | jetons de sortie | attendu USD | pire USD")
    for l in lignes:
        print(f"{l['poste']} | {fmt(l['appels'])} | {fmt(l['entree'])} | {fmt(l['sortie'])} | {l['attendu']:.2f} | {l['pire']:.2f}")
    ta, tp = sum(l["attendu"] for l in lignes), sum(l["pire"] for l in lignes)
    print(f"TOTAL | | | | {ta:.2f} | {tp:.2f}")
    return ta, tp


print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; racine {RACINE} ; tirages {TIRAGES}")
print("coûts unitaires attendus (USD) : " + " ; ".join(f"{k} {v:.4f}" for k, v in UNIT.items()))
print("coûts unitaires au pire (USD) : " + " ; ".join(f"{k} {v:.3f}" for k, v in PIRE_UNITAIRE.items()))

pp_att, pp_pire = imprimer("Pré-pilote recentré (sans seconde version de témoins)", pp)
print(f"seconde version des témoins (conditionnelle, probabilité {P_SECONDE}) : {sec:.2f} attendu si elle a lieu, "
      f"{sec_pire:.2f} au pire ; pondérée {P_SECONDE * sec:.2f}")
print(f"pré-pilote attendu, seconde version pondérée : {pp_att + P_SECONDE * sec:.2f} ; pire avec seconde version : {pp_pire + sec_pire:.2f}")
print(f"options hors liste de R-634 : passe « tableau » de Kimi {opt_tableau[0]:.2f} / {opt_tableau[1]:.2f} ; "
      f"mémoire anti-redite et table de l'axe 7 {opt_memoire[0]:.2f} / {opt_memoire[1]:.2f}")

res_course = {}
for ss in (4, 3, 2):
    for fps, nom in ((2, "A : 2 fusions par sous-session (paires tirées sur les fiches des deux proposeurs)"),
                     (4, "B : 4 fusions par sous-session (une paire par bras et par proposeur)")):
        if ss != 4 and fps == 4:
            continue
        res_course[(ss, fps)] = imprimer(f"Course, {ss} sous-sessions, lecture {nom}", course(ss, fps))

# ---------------------------------------------------------------- incertitude (modèle grossier, SUPPOSÉ)
# Rapport mesuré ÷ attendu log-normal, indépendant par poste ; médiane et dispersion écrites ici.
# Médianes reprises de P11 (brouillon 3) : passes de Kimi 1,2 ; antériorité 1,2 ; fusion 1,3 ; Kimi juge 1,0
# (sa base est désormais OBSERVÉE) ; autres 1,0. Dispersion (écart-type du logarithme) : 0,35 ; Kimi 0,5.
MED = {"Kimi proposeur": 1.2, "Antériorité": 1.2, "Bisociation": 1.3, "Juge Kimi": 1.0}
SIG = {"Kimi proposeur": 0.5, "Juge Kimi": 0.5, "Juges croisés": 0.45}


def tirer(lignes, tache, n=TIRAGES):
    g = generateur(tache)
    tot = np.zeros(n)
    for l in lignes:
        m = next((v for k, v in MED.items() if l["poste"].startswith(k)), 1.0)
        s = next((v for k, v in SIG.items() if l["poste"].startswith(k)), 0.35)
        tot += l["attendu"] * np.exp(np.log(m) + s * g.standard_normal(n))
    return tot


tp = tirer(pp, "devis-v4-pre-pilote")
g2 = generateur("devis-v4-seconde-version")
tp = tp + (g2.random(TIRAGES) < P_SECONDE) * sec * np.exp(0.35 * g2.standard_normal(TIRAGES))
print("\n== Incertitude du pré-pilote (rapports log-normaux, SUPPOSÉ) ==")
print(f"médiane {np.median(tp):.1f} ; quantile 90 % {np.quantile(tp, 0.9):.1f} ; quantile 99 % {np.quantile(tp, 0.99):.1f}")
for cap in (32, 35, 40, 45):
    print(f"P(dépense > {cap} USD, avant toute règle de sacrifice) = {np.mean(tp > cap):.3f}")

print("\n== Incertitude de la course, lecture A (rapports log-normaux, SUPPOSÉ) ==")
tc = {}
for ss in (4, 3, 2):
    tc[ss] = tirer(course(ss, 2), "devis-v4-course")   # même graine : mêmes rapports par poste, quel que soit ss
    print(f"{ss} sous-sessions : médiane {np.median(tc[ss]):.1f} ; quantile 90 % {np.quantile(tc[ss], 0.9):.1f}")

print("\n== Reste du plafond total pour la course (dépense du pré-pilote tirée ci-dessus) ==")
for total in (110, 130, 140):
    reste = total - np.minimum(tp, 45.0)   # pré-pilote borné à 45 par sa règle de sacrifice
    t4 = np.mean(tc[4] <= reste)
    t3 = np.mean((tc[4] > reste) & (tc[3] <= reste))
    t2 = np.mean((tc[3] > reste) & (tc[2] <= reste))
    t0 = np.mean(tc[2] > reste)
    print(f"plafond total {total} USD (pré-pilote ≤ 45) : reste médian {np.median(reste):.1f} ; "
          f"course à 4 : {t4:.2f} ; à 3 : {t3:.2f} ; à 2 : {t2:.2f} ; à aucune : {t0:.3f}")

print("\n== Variante allégée (option c) : 4 témoins par lot, antériorité sur 6 notables par sous-session ==")
va = course(4, 2, temoins_par_ss=4, notables_par_ss=6)
imprimer("Course allégée, 4 sous-sessions, lecture A", va)
tv = tirer(va, "devis-v4-course")
tv3 = tirer(course(3, 2, temoins_par_ss=4, notables_par_ss=6), "devis-v4-course")
reste = 110 - np.minimum(tp, 45.0)
print(f"allégée, médiane {np.median(tv):.1f} ; quantile 90 % {np.quantile(tv, 0.9):.1f} ; plafond total 110 : "
      f"course à 4 : {np.mean(tv <= reste):.2f} ; à 3 : {np.mean((tv > reste) & (tv3 <= reste)):.2f}")
print("fin")
