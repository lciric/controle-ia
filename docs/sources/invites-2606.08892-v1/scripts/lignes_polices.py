"""Liste les lignes d'une page XML (pdftohtml -xml) avec la police de leur premier fragment.
Usage : python3 -I lignes_polices.py FICHIER.xml"""
import sys, re, html
src = open(sys.argv[1], encoding='utf-8').read()
fonts = {m.group(1): m.group(3).split('+')[-1] for m in re.finditer(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]+)" color="([^"]+)"/>', src)}
runs = []
for m in re.finditer(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', src, re.S):
    t, l, w, h, f, s = m.groups()
    runs.append((int(t), int(l), int(w), int(h), fonts[f], html.unescape(re.sub(r'<[^>]+>', '', s))))
# regrouper par top exact pour les fragments de hauteur >= 12
lines = {}
for r in runs:
    if r[3] >= 12:
        lines.setdefault(r[0], []).append(r)
for t in sorted(lines):
    rs = sorted(lines[t], key=lambda r: r[1])
    fams = sorted(set(r[4] for r in rs))
    txt = ' | '.join(r[5] for r in rs)
    print(t, rs[0][1], ','.join(fams), txt[:90])
