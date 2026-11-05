"""Diagnostic : lignes physiques d'une page d'après pdftotext -bbox (positions en points PDF).
Usage : python3 -I lignes_bbox.py FICHIER_BBOX.html [colonne: g|d|toutes]
Pour chaque ligne : ordonnée du haut, abscisse du premier mot, abscisse de fin du dernier mot,
puis les mots séparés par l'écart mesuré entre eux (en points) quand il s'écarte de l'espace naturelle
(2,727 pt) de plus de 0,4 pt, ou quand il est inférieur à 1 pt (pas d'espace)."""
import html
import re
import sys

src = open(sys.argv[1], encoding='utf-8').read()
col = sys.argv[2] if len(sys.argv) > 2 else 'toutes'
mots = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in re.findall(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', src)]
MILIEU = 297.6
lignes = {}
for m in mots:
    c = 'g' if m[0] < MILIEU else 'd'
    if col != 'toutes' and c != col:
        continue
    cle = next((k for k in lignes if k[0] == c and abs(k[1] - m[1]) < 2), (c, m[1]))
    lignes.setdefault(cle, []).append(m)
for k in sorted(lignes):
    ws = sorted(lignes[k])
    parts = []
    for a, b in zip(ws, ws[1:]):
        g = b[0] - a[2]
        marque = f' <{g:.2f}> ' if (g < 1 or abs(g - 2.727) > 0.4) else ' '
        parts.append(a[4] + marque)
    parts.append(ws[-1][4])
    h = ws[0][3] - ws[0][1]
    print(f"{k[0]} y={k[1]:7.2f} h={h:5.2f} x0={ws[0][0]:7.2f} x1={ws[-1][2]:7.2f} | {''.join(parts)}")
