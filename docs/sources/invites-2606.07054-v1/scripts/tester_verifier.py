"""Teste que verifier.py détecte des altérations (cas témoins) et accepte le cas sain (règle R5).

Usage : python3 -I tester_verifier.py ESPACE

1. Transcriptions altérées : pour chaque cas, une copie de l'espace est faite dans ESPACE/tests-verificateur/<cas>/
   (index.json + invites/), une transcription y est altérée, son empreinte est mise à jour dans l'index copié
   (pour que seuls les contrôles A et B décident), puis verifier.py est lancé sur la copie.
2. Déclarations altérées : même procédé, mais c'est l'index copié qui est modifié (zones du contrôle B,
   substitution du contrôle A, trait d'union déclaré, empreinte) ; chaque garde doit refuser.
3. Garde de classement des lignes (contrôle B) : la fonction classer() de verifier.py est appliquée à des lignes
   synthétiques (artefacts) et à deux lignes réelles du PDF ; les cas mixtes doivent être déclarés indécidables.
Les vraies transcriptions et le vrai index ne sont pas touchés. Contrôles attendus en échec : A (contenu),
B (structure), F (fin de ligne finale), E (empreinte du fichier).
"""
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys

ESPACE = sys.argv[1]
ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ESPACE, 'tests-verificateur')


def zone(i, cle, delta):
    def f(inv):
        inv['verification']['B']['zones'][i][cle] += delta
    return f


def garder_zones(n):
    def f(inv):
        inv['verification']['B']['zones'] = inv['verification']['B']['zones'][:n]
    return f


def vider(chemin):
    def f(inv):
        d = inv['verification']
        for c in chemin[:-1]:
            d = d[c]
        d[chemin[-1]] = []
    return f


def empreinte_fausse(inv):
    inv['sha256'] = '0' * 64


CAS = [
    # (nom, id, ancien, nouveau, modification de l'index ou None, contrôles attendus en échec)
    ('sain (aucune altération)', 'B3-2', None, None, None, set()),
    ('mot changé', 'B3-2', 'Compare two steps', 'Compare three steps', None, {'A', 'B'}),
    ('ligne supprimée', 'B3-1', 'STEP [{k}]: {step_text}\n', '', None, {'A', 'B'}),
    ('espace ajoutée dans un mot', 'B4', 'faithfully', 'faith fully', None, {'A', 'B'}),
    ('ordre de deux lignes inversé', 'B3-2', 'STEP [{i}]: {step_i_text}\nSTEP [{j}]: {step_j_text}',
     'STEP [{j}]: {step_j_text}\nSTEP [{i}]: {step_i_text}', None, {'A', 'B'}),
    ('premier mot retiré', 'B1', 'You are an AI safety monitor', 'are an AI safety monitor', None, {'A', 'B'}),
    ('dernier caractère retiré', 'B4', 'patterns"}\n', 'patterns"\n', None, {'A', 'B'}),
    ("césure réintroduite (trait d'union de fin de ligne gardé à tort)", 'B1', 'unrequested', 'unre-quested', None,
     {'A', 'B'}),
    ("trait d'union du mot composé retiré", 'B3-3', 'monitor-targeted', 'monitortargeted', None, {'A', 'B'}),
    ('apostrophe typographique remplacée par une droite', 'B3-2', 'agent’s', "agent's", None, {'A', 'B'}),
    ("tiret demi-cadratin remplacé par un trait d'union", 'B4', 'score 2–3', 'score 2-3', None, {'A', 'B'}),
    ('puce supprimée', 'B4', '• Base your score', 'Base your score', None, {'A', 'B'}),
    ('double espace', 'B2', 'known violation patterns. Arguments: {}', 'known violation patterns.  Arguments: {}',
     None, {'B'}),
    ("retour à la ligne à la place d'une espace", 'B3-4', 'made by an agent.', 'made\nby an agent.', None, {'B'}),
    ("deux lignes fusionnées (espace à la place d'un retour)", 'B4', 'USER REQUEST: {user_query}\nEVIDENCE LOG',
     'USER REQUEST: {user_query} EVIDENCE LOG', None, {'B'}),
    ('fin de ligne finale doublée', 'B3-3', 'Return plain text only.\n', 'Return plain text only.\n\n', None,
     {'B', 'F'}),
    # déclarations altérées (index copié)
    ('déclaration : zone B tronquée en haut (première ligne exclue)', 'B1', None, None, zone(0, 'haut_pt', 13.549),
     {'B'}),
    ('déclaration : zone B tronquée en bas (dernière ligne exclue)', 'B4', None, None, zone(-1, 'bas_pt', -13.549),
     {'B'}),
    ("déclaration : zone B étendue jusqu'à l'intitulé suivant", 'B3-2', None, None, zone(0, 'bas_pt', 30.0), {'B'}),
    ('déclaration : zone de la colonne suivante omise', 'B2', None, None, garder_zones(1), {'B'}),
    ("déclaration : trait d'union conservé non déclaré", 'B3-3', None, None,
     vider(('B', 'traits_d_union_conserves')), {'B'}),
    ('déclaration : substitution du passage de colonne retirée', 'B3-4', None, None, vider(('substitutions',)),
     {'A'}),
    ("déclaration : empreinte de l'index fausse", 'B1', None, None, empreinte_fausse, {'E'}),
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
        if 'empreinte du fichier : DIFFÉRENTE' in l:
            e.add('E')
    return e, bloc


def autres_conformes(sortie, ident):
    """Les gabarits non altérés doivent rester conformes dans chaque copie."""
    return all('NON CONFORME' not in l for l in sortie.splitlines()
               if l.startswith('== ') and not l.startswith(f'== {ident} ('))


def tester_classement():
    """Garde de classement du contrôle B, sur des artefacts synthétiques et sur deux lignes réelles."""
    sys.argv = [os.path.join(ICI, 'verifier.py'), ESPACE]
    sys.dont_write_bytecode = True          # pas de __pycache__ dans scripts/
    spec = importlib.util.spec_from_file_location('verifier', os.path.join(ICI, 'verifier.py'))
    v = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v)
    m = v.MARGE_DROITE['d']
    synth = [
        ('ligne pleine, espaces étirées (cas sain)', dict(texte='a b c', x1=m, col='d', glue=[3.1, 3.1]), 'justifiee'),
        ('ligne courte, espaces naturelles (cas sain)', dict(texte='a b.', x1=m - 30, col='d', glue=[2.72727]), 'fin'),
        ('ligne pleine finie par « - » (cas sain)', dict(texte='a ex-', x1=m + 1.81, col='d', glue=[2.9]), 'cesure'),
        ('artefact : ligne pleine à espaces naturelles', dict(texte='a b c', x1=m, col='d', glue=[2.72727]), 'indecidable'),
        ('artefact : ligne courte à espaces étirées', dict(texte='a b c', x1=m - 30, col='d', glue=[3.5]), 'indecidable'),
        ('artefact : ligne courte finie par « - »', dict(texte='a ex-', x1=m - 30, col='d', glue=[2.72727]), 'indecidable'),
        ('cas limite : ligne courte à 0,1 pt de la marge, espaces naturelles', dict(texte='a b', x1=m - 0.1, col='d',
                                                                            glue=[2.72727]), 'fin'),
        ('artefact : espace naturelle décalée de 0,001 pt, ligne courte', dict(texte='a b', x1=m - 30, col='d',
                                                                              glue=[2.72827]), 'indecidable'),
    ]
    reelles = []
    for z_page, col, debut, attendu in ((12, 'd', 'with assistant action and tool results paired.', 'justifiee'),
                                        (12, 'd', 'behaviour the user would have objected to.', 'fin')):
        l = next(l for l in v.lignes_colonne(z_page, col) if l['texte'] == debut)
        reelles.append((f'ligne réelle p. {z_page} : « {debut} »', dict(l, col=col), attendu))
    ok_total = True
    for nom, l, attendu in synth + reelles:
        obtenu = v.classer(l)
        ok = obtenu == attendu
        ok_total &= ok
        print(f"{'OK ' if ok else 'ÉCHEC'} classement — {nom} : attendu {attendu}, obtenu {obtenu}")
    return ok_total


def main():
    if os.path.exists(BASE):
        shutil.rmtree(BASE)
    total_ok = True
    print('Test du vérificateur sur des copies altérées (les transcriptions et l\'index réels ne sont pas modifiés)\n')
    for i, (nom, ident, ancien, nouveau, modif, attendu) in enumerate(CAS):
        d = os.path.join(BASE, f'cas{i:02d}')
        shutil.copytree(os.path.join(ESPACE, 'invites'), os.path.join(d, 'invites'))
        index = json.load(open(os.path.join(ESPACE, 'index.json'), encoding='utf-8'))
        inv = next(x for x in index['invites'] if x['id'] == ident)
        if ancien is not None:
            chemin = os.path.join(d, 'invites', ident + '.txt')
            t = open(chemin, encoding='utf-8').read()
            if t.count(ancien) != 1:
                raise SystemExit(f'cas {nom!r} : motif trouvé {t.count(ancien)} fois')
            t = t.replace(ancien, nouveau)
            with open(chemin, 'w', encoding='utf-8') as f:
                f.write(t)
            inv['sha256'] = hashlib.sha256(t.encode('utf-8')).hexdigest()
        if modif is not None:
            modif(inv)
        with open(os.path.join(d, 'index.json'), 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False)
        code, sortie = lancer(d)
        obtenu, bloc = echecs(sortie, ident)
        ok = (obtenu == attendu) and ((code == 0) == (not attendu)) and autres_conformes(sortie, ident)
        total_ok &= ok
        print(f"{'OK ' if ok else 'ÉCHEC'} cas {i:02d} — {nom} ({ident}) : contrôles en échec attendus "
              f"{sorted(attendu) or 'aucun'}, obtenus {sorted(obtenu) or 'aucun'} ; code de sortie {code}")
        for l in bloc:
            s = l.strip()
            if ('transcription :' in s or 'positions PDF' in s or 'PDF           :' in s or 'premier' in s
                    or 'NON CONFORME' in s or 'DIFFÉRENTE' in s):
                print('      ' + s[:220])
    shutil.rmtree(BASE)
    print()
    total_ok &= tester_classement()
    print('\nRÉSULTAT :', 'le vérificateur détecte toutes les altérations et accepte le cas sain'
          if total_ok else 'AU MOINS UN CAS INATTENDU')
    sys.exit(0 if total_ok else 1)


if __name__ == '__main__':
    main()
