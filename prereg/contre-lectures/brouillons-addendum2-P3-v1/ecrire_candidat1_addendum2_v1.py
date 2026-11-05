"""Candidat 1 de l'addendum 2 de P3, par la session : copie du script d'essai de la vérification « texte »
(`verification-v3/texte/outils/candidat_essai_v1.py`, `candidat_essai_v1.py.sha256`), avec les empreintes réelles de la
contre-lecture 5, les tests v4 (128) et la phrase de durée de VV3-code-05. Brouillon 5 + VV3-texte-01 à 07.

Usage : python -B candidat_essai_v1.py <brouillon5.md> <sortie.md> <module.py>
Écrit seulement <sortie.md> (dans le dossier de la vérification), puis imprime `prereg.problemes` et ce que lisent les
deux expressions de la garde 1. Les empreintes des deux rapports de la contre-lecture 5 sont fictives ici (0…0 et 1…1).
"""
import importlib.util
import sys
from pathlib import Path

from controle_ia.prereg import problemes, sections

src, dst, module = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
t = src.read_text(encoding="utf-8")


def remplace(ancien, nouveau):
    global t
    assert t.count(ancien) == 1, ancien[:80]
    t = t.replace(ancien, nouveau)


# en-tête
remplace("<<EMPREINTE_MODULE>>", "967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d")
remplace("<<EMPREINTE_TESTS>>", "f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07")
remplace("<<NOMBRE_TESTS>>", "128")
# plan, point 9 (VV3-texte-04)
remplace("`<<DUREE_MESUREE>>`",
         "environ 5,5 s pour la ligne de commande complète (de 5,4 à 5,7 s sur quatre mesures ; processus séparé ;\n"
         "   module cité en tête, ses constantes du run réel remplacées par celles du dépôt jouet, comme dans les tests ;\n"
         "   dépôt jouet à taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes, les cinq\n"
         "   formes présentes ; 10 000 tirages ; machine partagée, 4 cœurs), dont 3,2 à 3,4 s\n"
         "   d'imports, mesurés dans un processus qui ne fait qu'importer (surtout `harnais.validation_reelle`, qui importe la\n"
         "   bibliothèque de calcul tensoriel : 2,05 à 2,15 s) et\n"
         "   0,45 à 0,52 s pour la fonction pure ; mémoire maximale ≈ 683 Mio (≈ 717 Mo) ; mesures brutes :\n"
         "   `prereg/contre-lectures/notes-module-v3-addendum2-P3-v1/mesures-duree-v1.txt` (sha256\n"
         "   `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba`)")
# section « Contre-lecture » : empreintes des traitements et de la vérification 2
remplace("<<SHA_TRAITEMENT_1>>", "dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392")
remplace("<<SHA_VERIFICATION_2>>", "65afdd6c7e23d6cba334442ff1b99ec7ef89a2d35e327d47b7d1cb98e7be1461")
remplace("<<SHA_TRAITEMENT_2>>", "155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca")
# section « Contre-lecture » : l'entrée unique du code devient trois entrées numérotées (VV3-texte-01)
debut = t.index("- **Contre-lecture du code** —")
t = t[:debut] + Path(sys.argv[0]).with_name("section-contre-lecture-code-v1.md").read_text(encoding="utf-8")
# précision 14 (VV3-texte-02)
remplace("14. Un [SF] sans `principales` arrête avec un motif écrit, jamais par une exception nue (brouillon 5, CV2-10).",
         "14. Un [SF] sans `principales`, ou dont `principales.tromperie` ou `principales.enjeux` est absente, vide ou non\n"
         "    textuelle, arrête au titre de la garde 7 (« run source hors de forme »), avec un motif écrit, jamais par une\n"
         "    exception nue (brouillon 5, CV2-10) ; de même des tables de [S] hors de forme (tables ou colonnes lues absentes,\n"
         "    colonnes de longueurs différentes, table des scores mal formée).")
# précision 2 (VV3-texte-03)
remplace("une part dont l'intervalle est en échec\n   (garde 15) garde sa valeur ponctuelle et ne fait pas taire le déclencheur",
         "une part dont l'intervalle est en échec\n   (garde 15) garde sa valeur ponctuelle (écrite dans "
         "`audit_symetrie_addendum2.part_hors_bornes.part` ; le descriptif\n   de la part reste « échec », sans valeur) et ne "
         "fait pas taire le déclencheur")
# préambule des précisions (VV3-texte-05)
remplace("Règles déjà appliquées par le module là où le texte se taisait (contre-lecture du code, CC-texte-06) ; aucune ne change un\nnombre, une réserve ni le verrou :",
         "Règles appliquées par le module v3 là où le texte se taisait ou restait implicite (contre-lectures du code :\n"
         "CC-texte-06 pour 1 à 10 ; CV2-01, CV2-07, CV2-08 et CV2-10 pour 1, 2 et 11 à 14) ; aucune ne change un nombre, une\n"
         "réserve ni le verrou ; la précision 2 redit la règle de l'audit, point 3 :")
# imports des tests (VV3-texte-06)
remplace("les tests peuvent importer les aides de `tests/test_premier_test_ia_lecture.py`.",
         "les tests peuvent importer `pytest`, les aides de `tests/test_premier_test_ia_lecture.py` et les aides\n"
         "  `committer` et `git` de `tests/conftest.py` (arbre gelé, sans copie).")
# M5 (VV3-texte-07)
remplace("(plus de 1 % : « échec » de la part, motif écrit).",
         "(plus de 1 % : « échec » de la part, motif écrit ; à 1 % au plus,\n  l'intervalle de la part est pris sur les seuls "
         "tirages non dégénérés, dont le nombre est écrit).")

dst.write_text(t, encoding="utf-8")
print("sections :", sorted(sections(t)))
print("problemes :", problemes(dst))
spec = importlib.util.spec_from_file_location("av_essai", module)
av = importlib.util.module_from_spec(spec)
spec.loader.exec_module(av)
print("garde 1, module :", av.EMPREINTE_MODULE_CITEE.findall(t))
print("garde 1, tests  :", av.EMPREINTE_TESTS_CITEE.findall(t))
