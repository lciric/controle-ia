"""Teste que verifier.py détecte des altérations (cas témoins) et accepte le cas sain.

Usage : python3 -I tester_verifier.py ESPACE
Pour chaque cas, une copie de l'espace est faite dans ESPACE/tests-verificateur/<cas>/ (index.json + invites/),
une transcription y est altérée, son empreinte est mise à jour dans l'index copié (pour que seuls les
contrôles A et B décident), puis verifier.py est lancé sur la copie. Les vraies transcriptions ne sont pas touchées.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

ESPACE = sys.argv[1]
ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ESPACE, 'tests-verificateur')

CAS = [
    # (nom, id, ancien, nouveau, contrôles attendus en échec)
    ('sain (aucune altération)', 'H12', None, None, set()),
    ('mot changé', 'H2', 'senior ML researcher', 'seniour ML researcher', {'A', 'B'}),
    ('dernière phrase tronquée', 'H3', ' Reserve top scores for proposals that demonstrate the kind of deep domain understanding and creative experimental thinking you would see from a leading researcher in the specific subfield, not from an average AI model or a mediocre PhD student.', '', {'A', 'B'}),
    ('premier mot retiré', 'H5', 'You are a senior', 'are a senior', {'A', 'B'}),
    ('ligne vide supprimée', 'H6', 'datasets).\n\nYour goal', 'datasets).\nYour goal', {'B'}),
    ('retrait modifié (4 -> 3 espaces)', 'H9', '\n    {"author": "Author 2"', '\n   {"author": "Author 2"', {'B'}),
    ('double espace réduite', 'H12', 'and  score of a 100', 'and score of a 100', {'B'}),
    ('guillemet droit -> courbe', 'H10', '"theory_only": Only', '“theory_only": Only', {'A', 'B'}),
    ('deux lignes interverties', 'H13-expansion-utilisateur', 'Idea kernel: {name}\nDescription: {description}', 'Description: {description}\nIdea kernel: {name}', {'A', 'B'}),
    ('indice remplacé par un chiffre simple', 'I3', 'β₁=0.9', 'β1=0.9', {'A'}),
    ('ligne coupée à tort (retour au lieu d\'espace)', 'H1', 'theoretical results to address', 'theoretical\nresults to address', {'B'}),
    ('fin de ligne finale doublée', 'H1-format', 'PROPOSAL 1.\n', 'PROPOSAL 1.\n\n', {'B', 'F'}),
]


def lancer(cas_dir):
    r = subprocess.run([sys.executable, '-I', os.path.join(ICI, 'verifier.py'), cas_dir], capture_output=True)
    return r.returncode, r.stdout.decode('utf-8')


def echecs(sortie, ident):
    bloc, dedans = [], False
    for l in sortie.splitlines():
        if l.startswith('== '):
            dedans = l.startswith(f'== {ident} (')
        elif dedans:
            bloc.append(l)
    e = set()
    for l in bloc:
        if l.strip().startswith('A contenu') and 'NON CONFORME' in l:
            e.add('A')
        if l.strip().startswith('B structure') and 'NON CONFORME' in l:
            e.add('B')
        if 'fin de ligne finale unique : NON' in l:
            e.add('F')
    return e, bloc


def main():
    if os.path.exists(BASE):
        shutil.rmtree(BASE)
    total_ok = True
    print('Test du vérificateur sur des copies altérées (les transcriptions réelles ne sont pas modifiées)\n')
    for i, (nom, ident, ancien, nouveau, attendu) in enumerate(CAS):
        d = os.path.join(BASE, f'cas{i:02d}')
        shutil.copytree(os.path.join(ESPACE, 'invites'), os.path.join(d, 'invites'))
        index = json.load(open(os.path.join(ESPACE, 'index.json'), encoding='utf-8'))
        if ancien is not None:
            chemin = os.path.join(d, 'invites', ident + '.txt')
            t = open(chemin, encoding='utf-8').read()
            if t.count(ancien) != 1:
                raise SystemExit(f'cas {nom!r} : motif trouvé {t.count(ancien)} fois')
            t = t.replace(ancien, nouveau)
            open(chemin, 'w', encoding='utf-8').write(t)
            inv = next(x for x in index['invites'] if x['id'] == ident)
            inv['sha256'] = hashlib.sha256(t.encode('utf-8')).hexdigest()
        json.dump(index, open(os.path.join(d, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        code, sortie = lancer(d)
        obtenu, bloc = echecs(sortie, ident)
        ok = (obtenu == attendu) and ((code == 0) == (not attendu))
        total_ok &= ok
        print(f"{'OK ' if ok else 'ÉCHEC'} cas {i:02d} — {nom} ({ident}) : contrôles en échec attendus "
              f"{sorted(attendu) or 'aucun'}, obtenus {sorted(obtenu) or 'aucun'} ; code de sortie {code}")
        for l in bloc:
            if 'transcription :' in l or 'positions PDF' in l or 'PDF           :' in l or 'premier' in l or 'substitution sans effet' in l:
                print('      ' + l.strip()[:200])
    shutil.rmtree(BASE)
    print('\nRÉSULTAT :', 'le vérificateur détecte toutes les altérations et accepte le cas sain'
          if total_ok else 'AU MOINS UN CAS INATTENDU')
    sys.exit(0 if total_ok else 1)


if __name__ == '__main__':
    main()
