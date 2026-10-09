"""Diagnostic : contexte avant/après chaque invite dans le texte pdftotext (mode par défaut, normalisé).
Usage : python3 -I contexte.py PDF ESPACE"""
import json, os, re, subprocess, sys
pdf, esp = sys.argv[1], sys.argv[2]
cfg = json.load(open(os.path.join(esp, 'scripts', 'config_invites.json'), encoding='utf-8'))
LIG = str.maketrans({'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬆ': 'st'})
def norm(s):
    s = s.translate(LIG)
    s = re.sub(r',[ \t\r\n\f\v]*→', ' ', s)
    return re.sub(r'[ \t\r\n\f\v]+', ' ', s).strip()
def page(p):
    return subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), pdf, '-'], capture_output=True, check=True).stdout.decode('utf-8')
for inv in cfg['invites']:
    t = norm(open(os.path.join(esp, 'invites', inv['id'] + '.txt'), encoding='utf-8').read())
    p0, p1 = inv['segments'][0]['page'], inv['segments'][-1]['page']
    a = norm(page(p0)); b = norm(page(p1)) if p1 != p0 else a
    i = a.find(t[:50]); j = b.find(t[-40:])
    print('=====', inv['id'], f'p{p0}-p{p1}')
    print('  AVANT :', a[max(0, i - 300):i] if i >= 0 else 'DEBUT INTROUVABLE')
    print('  APRES :', b[j + 40:j + 40 + 150] if j >= 0 else 'FIN INTROUVABLE')
