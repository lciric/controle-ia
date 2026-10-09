"""Affiche les fragments de texte d'une page XML (pdftohtml -xml), tries par position.
Usage : python3 -I voir_xml.py FICHIER.xml [top_min top_max]"""
import sys, re, html
src = open(sys.argv[1], encoding='utf-8').read()
lo = int(sys.argv[2]) if len(sys.argv) > 2 else -10**9
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
fonts = {m.group(1): (m.group(3).split('+')[-1], m.group(4)) for m in re.finditer(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]+)" color="([^"]+)"/>', src)}
runs = []
for m in re.finditer(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', src, re.S):
    t, l, w, h, f, s = m.groups()
    runs.append((int(t), int(l), int(w), int(h), f, html.unescape(re.sub(r'<[^>]+>', '', s))))
for r in sorted(runs):
    if lo <= r[0] <= hi:
        txt = r[5]
        cw = r[2] / len(txt) if txt else 0
        print(r[0], r[1], r[1] + r[2], r[3], fonts[r[4]][0], fonts[r[4]][1], f"{cw:.3f}", repr(txt))
