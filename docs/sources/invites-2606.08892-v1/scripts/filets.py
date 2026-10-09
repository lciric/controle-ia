"""Repère les filets horizontaux (traits longs) et les rangées d'encre d'une page rendue en PGM.
Usage : python3 -I filets.py FICHIER.pgm DPI Y_MIN_PT Y_MAX_PT
Affiche, en points PDF, les rangées contenant un trait sombre continu de plus de 100 pt
et le début/fin de chaque bande d'encre."""
import sys
fn, dpi, y0, y1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
data = open(fn, 'rb').read()
# en-tête PGM binaire
parts = data.split(b'\n', 3)
w, h = map(int, parts[1].split()); maxv = int(parts[2]); pix = parts[3]
assert len(pix) >= w * h
k = dpi / 72.0
encre_prec = False
for row in range(int(y0 * k), min(h, int(y1 * k))):
    ligne = pix[row * w:(row + 1) * w]
    sombres = [i for i in range(w) if ligne[i] < 128]
    encre = bool(sombres)
    # plus long segment sombre continu
    best = cur = 0
    prev = -2
    for i in sombres:
        cur = cur + 1 if i == prev + 1 else 1
        best = max(best, cur); prev = i
    if best / k > 100:
        print(f'filet  y={row / k:8.2f} pt  longueur={best / k:6.1f} pt  x={sombres[0] / k:6.1f}..{sombres[-1] / k:6.1f}')
    if encre != encre_prec:
        print(f"{'debut' if encre else 'fin  '} encre y={row / k:8.2f} pt")
        encre_prec = encre
