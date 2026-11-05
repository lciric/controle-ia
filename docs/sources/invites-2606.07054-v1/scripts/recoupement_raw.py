"""Recoupement (diagnostic, hors contrôles A et B) : chaque transcription se retrouve-t-elle dans le texte de
« pdftotext -raw » (ordre du flux de contenu du PDF, pages 12 et 13 entières, sans rognage) ?

Usage : python3 -I recoupement_raw.py ESPACE
Règles appliquées au texte -raw, et seulement celles-ci : un trait d'union en fin de ligne est retiré et la ligne
recollée sans espace, sauf pour les mots composés déclarés dans index.json ; toute autre fin de ligne vaut une
espace ; blancs réduits à une espace. La transcription est seulement réduite (blancs -> une espace).
"""
import json
import os
import re
import subprocess
import sys

ESPACE = sys.argv[1]
INDEX = json.load(open(os.path.join(ESPACE, 'index.json'), encoding='utf-8'))
PDF = INDEX['source']['chemin']
conserves = {c for inv in INDEX['invites'] for c in inv['verification']['B']['traits_d_union_conserves']}
brut = subprocess.run(['pdftotext', '-raw', '-f', '12', '-l', '13', PDF, '-'], capture_output=True,
                      check=True).stdout.decode('utf-8')
lignes = [l.strip() for l in brut.replace('\f', '\n').split('\n') if l.strip()]
texte = ''
for i, l in enumerate(lignes):
    texte += l
    if i + 1 < len(lignes):
        if l.endswith('-') and (l.split(' ')[-1] + lignes[i + 1].split(' ')[0]) not in conserves:
            texte = texte[:-1]
        elif not l.endswith('-'):
            texte += ' '
texte = re.sub(r'\s+', ' ', texte)
for inv in INDEX['invites']:
    t = re.sub(r'\s+', ' ', open(os.path.join(ESPACE, inv['fichier']), encoding='utf-8').read()).strip()
    n = texte.count(t)
    print(f"{inv['id']:5s} : {'retrouvée' if n == 1 else 'NON RETROUVÉE'} dans le texte -raw ({n} occurrence(s))")
    if n != 1:
        i = max(range(len(t) + 1), key=lambda k: k if t[:k] in texte else -1)
        print(f"      plus long début retrouvé : {i} car. ; suite attendue : {t[i:i + 60]!r}")
