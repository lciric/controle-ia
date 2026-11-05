"""Diagnostic : liste tous les écarts (difflib, par caractères) entre une transcription normalisée et le
texte pdftotext normalisé des pages, à partir de la borne « avant ». Usage : python3 -I ecarts_contenu.py ESPACE ID"""
import difflib, json, os, re, subprocess, sys
esp, ident = sys.argv[1], sys.argv[2]
idx = json.load(open(os.path.join(esp, 'index.json'), encoding='utf-8'))
inv = next(i for i in idx['invites'] if i['id'] == ident)
LIG = str.maketrans({'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬆ': 'st'})
def norm(s):
    return re.sub(r'[ \t\r\n\f\v]+', ' ', re.sub(r',[ \t\r\n\f\v]*→', ' ', s.translate(LIG))).strip()
pdf = ' '.join(norm(subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), idx['source']['chemin'], '-'],
                                   capture_output=True).stdout.decode()) for p in inv['verification']['pages'])
tr = norm(open(os.path.join(esp, inv['fichier']), encoding='utf-8').read())
i = pdf.find(norm(inv['verification']['avant'])) + len(norm(inv['verification']['avant'])) + 1
seg = pdf[i:i + len(tr) + 200]
sm = difflib.SequenceMatcher(None, tr, seg, autojunk=False)
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != 'equal':
        print(f"{op:8s} tr[{a0}:{a1}]={tr[a0:a1]!r:30s} pdf={seg[b0:b1]!r:30s} contexte: …{tr[max(0,a0-30):a0]}⟦{tr[a0:a1]}⟧{tr[a1:a1+20]}…")
