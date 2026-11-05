"""Vérifie que chaque transcription d'invite est fidèle au PDF.

Usage : python3 -I verifier.py [ESPACE]        (par défaut : le dossier parent de scripts/)
Lit ESPACE/index.json et ESPACE/invites/*.txt ; n'utilise que pdftotext (poppler) et la bibliothèque standard.
Code de sortie : 0 si tout est conforme, 1 sinon.

Contrôle A — contenu (exigé) : pour chaque invite, le texte des pages citées est extrait à nouveau par
  « pdftotext -f N -l N » (mode par défaut). Les deux côtés sont normalisés de la même façon :
    1. ligatures typographiques remplacées par leurs lettres (ﬀ ﬁ ﬂ ﬃ ﬄ ﬅ ﬆ) ;
    2. marqueur de continuation « , » suivi de « → » (blancs éventuels entre les deux) remplacé par une espace ;
    3. toute suite de blancs ASCII (espace, tabulation, retours, saut de page) réduite à une espace ; bords rognés.
  Côté PDF, avant normalisation, on retire le numéro de page (dernière ligne non vide, qui doit être égale au
  numéro) ; après normalisation, on retire les intrusions déclarées dans index.json (« retraits » : page
  entière, ou passage borné par un début et une fin qui doivent apparaître une seule fois sur la page).
  Côté transcription, on applique les substitutions déclarées (forme transcrite -> forme produite par
  pdftotext), chacune devant s'appliquer au moins une fois.
  Puis on exige que « avant + transcription + après » apparaisse tel quel dans le texte des pages :
  correspondance exacte, en entier et dans l'ordre, encadrée par le contexte déclaré (rien ne manque aux bords).

Contrôle B — structure (complément) : à partir des positions des mots (« pdftotext -bbox ») dans les zones
  déclarées, on reconstruit les lignes sur la grille à chasse fixe : retrait et espaces = écart / chasse,
  lignes de continuation (marqueur « ,→ » en petit corps) recollées par une espace, lignes vides = écart
  vertical / interligne, lignes vides aux passages de page = valeurs déclarées. Les chiffres en indice,
  en exposant ou en fraction sont comparés en chiffres simples (₁ -> 1, ² -> 2, ½ -> 12). Le texte
  reconstruit doit être identique, caractère pour caractère, à la transcription.
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys

ESPACE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = json.load(open(os.path.join(ESPACE, 'index.json'), encoding='utf-8'))
PDF = INDEX['source']['chemin']

LIGATURES = str.maketrans({'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬅ': 'st', 'ﬆ': 'st'})
BLANCS = re.compile(r'[ \t\n\r\f\v]+')
MARQUEUR = re.compile(r',[ \t\n\r\f\v]*→')


def normaliser(s):
    s = s.translate(LIGATURES)
    s = MARQUEUR.sub(' ', s)
    return BLANCS.sub(' ', s).strip()


def pdftotext(*args):
    return subprocess.run(['pdftotext', *args], capture_output=True, check=True).stdout.decode('utf-8')


_PAGES = {}


NOTES_PAGES = {}


def texte_page(p):
    """Texte (mode par défaut) de la page p, sans le numéro de page (pied de page).
    Règle : on retire la dernière ligne isolée égale au numéro de page ; elle doit exister."""
    if p not in _PAGES:
        t = pdftotext('-f', str(p), '-l', str(p), PDF, '-')
        lignes = t.replace('\f', '').rstrip('\n').split('\n')
        while lignes and not lignes[-1].strip():
            lignes.pop()
        idx = [i for i, l in enumerate(lignes) if l.strip() == str(p)]
        if not idx:
            raise SystemExit(f'page {p} : numéro de page introuvable')
        k = idx[-1]
        reste = [l for l in lignes[k + 1:] if l.strip()]
        if reste:
            NOTES_PAGES[p] = (f"numéro de page {p} retiré ; dans l'ordre de lecture de pdftotext il précède "
                              f"{len(reste)} ligne(s) : {' | '.join(reste)[:80]!r}")
        _PAGES[p] = '\n'.join(lignes[:k] + lignes[k + 1:])
    return _PAGES[p]


def contexte(s, i, n=70):
    return s[max(0, i - n):i] + '⟦' + s[i:i + n] + '…'


def controle_contenu(inv):
    v = inv['verification']
    morceaux, journal = [], []
    for p in v['pages']:
        t = normaliser(texte_page(p))
        if p in NOTES_PAGES:
            journal.append(NOTES_PAGES[p])
        for r in [r for r in v['retraits'] if r['page'] == p]:
            if r.get('tout'):
                journal.append(f"page {p} retirée en entier ({len(t)} car.) : {r['motif']}")
                t = ''
                continue
            d, f = normaliser(r['debut']), normaliser(r['fin'])
            if t.count(d) != 1:
                return False, f"retrait p{p} : début trouvé {t.count(d)} fois : {d!r}", journal
            i = t.index(d)
            j = t.find(f, i)
            if j < 0:
                return False, f"retrait p{p} : fin introuvable : {f!r}", journal
            journal.append(f"page {p} : retiré {j + len(f) - i} car. ({r['motif']}) : « {t[i:i + 50]}…{t[j + len(f) - 30:j + len(f)]} »")
            t = (t[:i] + ' ' + t[j + len(f):]).strip()
        morceaux.append(t)
    texte_pdf = BLANCS.sub(' ', ' '.join(morceaux)).strip()
    trans = open(os.path.join(ESPACE, inv['fichier']), encoding='utf-8').read()
    for s in v['substitutions']:
        n = trans.count(s['transcription'])
        if n < 1:
            return False, f"substitution sans effet : {s['transcription']!r}", journal
        trans = trans.replace(s['transcription'], s['pdf'])
        vu = lambda x: x.replace('\n', '␤')  # retour à la ligne affiché par le symbole ␤
        journal.append(f"substitution ×{n} : « {vu(s['transcription'])} » -> « {vu(s['pdf'])} » ({s['raison']})")
    t_tr = normaliser(trans)
    avant, apres = normaliser(v['avant']), normaliser(v['apres'])
    cible = ' '.join(x for x in (avant, t_tr, apres) if x)
    if v['apres'] == '':
        ok = texte_pdf.endswith(cible)
    else:
        ok = cible in texte_pdf
    if ok:
        n = texte_pdf.count(cible) if v['apres'] else 1
        return True, f"trouvée en entier et dans l'ordre, entre les bornes ({len(t_tr)} car. normalisés, {n} occurrence)", journal
    # premier écart
    if texte_pdf.count(avant) == 0:
        return False, f"borne « avant » introuvable : {avant!r}", journal
    meilleur = (-1, 0)
    for m in re.finditer(re.escape(avant), texte_pdf):
        i0 = m.start()
        k = 0
        while i0 + k < len(texte_pdf) and k < len(cible) and texte_pdf[i0 + k] == cible[k]:
            k += 1
        meilleur = max(meilleur, (k, i0))
    k, i0 = meilleur
    if k >= len(avant) + 1 + len(t_tr):
        return False, (f"transcription trouvée en entier, mais la borne « après » ne suit pas : "
                       f"PDF {contexte(texte_pdf, i0 + k)!r}"), journal
    return False, (f"premier écart au caractère {k - len(avant) - 1} de la transcription normalisée :\n"
                   f"      transcription : {contexte(cible, k)!r}\n"
                   f"      PDF           : {contexte(texte_pdf, i0 + k)!r}"), journal


# ---------------------------------------------------------------- contrôle B (structure, pdftotext -bbox)
CHASSE = 4.7062
MARGE = 108.0
INTERLIGNE = 9.847
CHIFFRES = str.maketrans('₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹', '01234567890123456789')
FRACTIONS = {'½': '12', '⅓': '13', '⅔': '23', '¼': '14', '¾': '34'}


def simplifier(s):
    for k, w in FRACTIONS.items():
        s = s.replace(k, w)
    return s.translate(CHIFFRES)


_MOTS = {}


def mots(p):
    if p not in _MOTS:
        out = pdftotext('-bbox', '-f', str(p), '-l', str(p), PDF, '-')
        _MOTS[p] = [dict(x0=float(a), y0=float(b), x1=float(c), y1=float(d), t=html.unescape(t))
                    for a, b, c, d, t in re.findall(
                        r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', out)]
    return _MOTS[p]


def lignes_zone(z):
    haut, bas = z['haut_pt'] - 2, z['bas_pt'] + 2
    ws = [w for w in mots(z['page']) if haut <= (w['y0'] + w['y1']) / 2 <= bas]
    principaux = [w for w in ws if w['y1'] - w['y0'] >= 10]
    auxiliaires = [w for w in ws if w['y1'] - w['y0'] < 10]
    lignes = []
    for w in sorted(principaux, key=lambda w: w['y0']):
        if lignes and abs(lignes[-1]['y0'] - w['y0']) < 2:
            lignes[-1]['mots'].append(w)
        else:
            lignes.append(dict(y0=w['y0'], centre=(w['y0'] + w['y1']) / 2, mots=[w], marqueurs=[]))
    for w in auxiliaires:
        c = (w['y0'] + w['y1']) / 2
        if w['t'] in (',', '→') and w['y1'] - w['y0'] < 7:
            cand = sorted(lignes, key=lambda l: abs(l['centre'] - c))
            cand[0]['marqueurs'].append(w)
            continue
        cand = sorted((l for l in lignes if abs(l['centre'] - c) <= 12), key=lambda l: abs(l['centre'] - c))
        choix = None
        for l in cand:
            if not any(w['x0'] < m['x1'] - 0.5 and m['x0'] < w['x1'] - 0.5 for m in l['mots']):
                choix = l
                break
        if choix is None:
            raise SystemExit(f"p{z['page']} : mot isolé non rattaché {w['t']!r} y={w['y0']:.1f}")
        choix['mots'].append(w)
    for l in lignes:
        l['continuation'] = (any(m['t'] == '→' for m in l['marqueurs']) and any(m['t'] == ',' for m in l['marqueurs']))
        ms = sorted(l['mots'], key=lambda w: (round(w['x0'], 1), w['y0']))
        txt, prec = '', None
        for w in ms:
            base = MARGE if prec is None else prec
            n = max(0, round((w['x0'] - base) / CHASSE))
            txt += ' ' * n + w['t']
            prec = w['x1']
        l['texte'] = txt
    return lignes


def controle_structure(inv):
    v = inv['verification']
    logiques = []
    for i, z in enumerate(v['zones']):
        if i > 0:
            logiques.extend([''] * v['sauts'][i - 1])
        prec = None
        for l in lignes_zone(z):
            if l['continuation']:
                if not logiques or prec is None:
                    return False, f"p{z['page']} : ligne de continuation en tête de zone"
                logiques[-1] = logiques[-1].rstrip(' ') + ' ' + l['texte'].lstrip(' ')
            else:
                if prec is not None:
                    logiques.extend([''] * (round((l['y0'] - prec['y0']) / INTERLIGNE) - 1))
                logiques.append(l['texte'])
            prec = l
    reconstruit = '\n'.join(logiques) + '\n'
    trans = simplifier(open(os.path.join(ESPACE, inv['fichier']), encoding='utf-8').read())
    if reconstruit == trans:
        return True, f"lignes, lignes vides, retraits et espaces identiques ({len(logiques)} lignes)"
    a, b = trans.split('\n'), reconstruit.split('\n')
    for k in range(max(len(a), len(b))):
        x = a[k] if k < len(a) else '∅'
        y = b[k] if k < len(b) else '∅'
        if x != y:
            j = next((i for i in range(min(len(x), len(y))) if x[i] != y[i]), min(len(x), len(y)))
            return False, (f"première ligne différente : n° {k + 1}, colonne {j + 1}\n"
                           f"      transcription : {x[max(0, j - 40):j + 40]!r}\n"
                           f"      positions PDF : {y[max(0, j - 40):j + 40]!r}")
    return False, 'différence de fin de fichier'


def main():
    h = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()
    print(f"Source : {PDF}")
    print(f"sha256 : {h} ({'conforme' if h == INDEX['source']['sha256'] else 'DIFFÉRENT — ARRÊT'})")
    if h != INDEX['source']['sha256']:
        sys.exit(1)
    version = subprocess.run(['pdftotext', '-v'], capture_output=True).stderr.decode().splitlines()[0]
    print(f"Outil  : {version} ; Python {sys.version.split()[0]}")
    print()
    tout_ok, bilan = True, []
    for inv in INDEX['invites']:
        data = open(os.path.join(ESPACE, inv['fichier']), 'rb').read()
        empreinte = hashlib.sha256(data).hexdigest() == inv['sha256']
        fin_ok = data.endswith(b'\n') and not data.endswith(b'\n\n')
        a_ok, a_msg, journal = controle_contenu(inv)
        b_ok, b_msg = controle_structure(inv)
        ok = a_ok and b_ok and empreinte and fin_ok
        tout_ok &= ok
        bilan.append((inv['id'], ok))
        print(f"== {inv['id']} ({inv['section']}, p. {inv['pages']['debut']}-{inv['pages']['fin']}) : "
              f"{'CONFORME' if ok else 'NON CONFORME'}")
        print(f"   empreinte du fichier : {'conforme' if empreinte else 'DIFFÉRENTE de index.json'} ; "
              f"fin de ligne finale unique : {'oui' if fin_ok else 'NON'}")
        print(f"   A contenu   : {'conforme' if a_ok else 'NON CONFORME'} — {a_msg}")
        for j in journal:
            print(f"      · {j}")
        print(f"   B structure : {'conforme' if b_ok else 'NON CONFORME'} — {b_msg}")
    print()
    n = sum(ok for _, ok in bilan)
    print(f"BILAN : {n}/{len(bilan)} invites conformes"
          + ('' if tout_ok else ' ; non conformes : ' + ', '.join(i for i, ok in bilan if not ok)))
    sys.exit(0 if tout_ok else 1)


if __name__ == '__main__':
    main()
