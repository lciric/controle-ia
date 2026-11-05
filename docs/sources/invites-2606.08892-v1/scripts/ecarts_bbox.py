"""Affiche, pour les lignes d'une page dont l'ordonnée (pt) est dans [ymin, ymax], les écarts entre mots
en nombre de chasses (4,7062 pt), d'après pdftotext -bbox.
Usage : python3 -I ecarts_bbox.py PDF PAGE YMIN YMAX"""
import sys, subprocess, re, html
pdf, page, y0, y1 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
out = subprocess.run(['pdftotext', '-bbox', '-f', page, '-l', page, pdf, '-'], capture_output=True, check=True).stdout.decode('utf-8')
mots = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in
        re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', out)]
CW = 4.7062
lignes = {}
for m in mots:
    if y0 <= m[1] <= y1 and m[3] - m[1] > 9:
        k = round(m[1], 1)
        lignes.setdefault(k, []).append(m)
for k in sorted(lignes):
    ws = sorted(lignes[k])
    parts = [f'[{(ws[0][0] - 108) / CW:.2f}]']
    for a, b in zip(ws, ws[1:]):
        g = (b[0] - a[2]) / CW
        parts.append(a[4] + (f' <{g:.2f}> ' if abs(g - 1) > 0.15 else ' '))
    parts.append(ws[-1][4])
    print(k, ''.join(parts))
