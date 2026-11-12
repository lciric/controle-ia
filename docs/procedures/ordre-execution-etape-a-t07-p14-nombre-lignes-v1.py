"""P14 (R-2314 (4) ; vérification finale de T0.7, `26efc4df…`, § 4, recopié) : nombre de lignes des mesures de 7b, lu à
l'en-tête du tableau `jetons_notes` ; n'imprime qu'un entier. Aucune colonne chargée, aucune valeur lue.
Usage : python3 -I ordre-execution-etape-a-t07-p14-nombre-lignes-v1.py donnees/<RUN6>/mesures-t06.npz (sceau vérifié à part)."""
import sys, zipfile
from numpy.lib import format as f
with zipfile.ZipFile(sys.argv[1]) as z, z.open("jetons_notes.npy") as h:
    v = f.read_magic(h)
    forme = (f.read_array_header_1_0 if v == (1, 0) else f.read_array_header_2_0)(h)[0]
print(int(forme[0]))
