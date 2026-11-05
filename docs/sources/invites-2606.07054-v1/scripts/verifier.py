"""Vérifie que chaque transcription de gabarit (annexe B de TRACE, arXiv 2606.07054v1) est fidèle au PDF.

Usage : python3 -I verifier.py [ESPACE]        (par défaut : le dossier parent de scripts/)
Lit ESPACE/index.json et ESPACE/invites/*.txt ; n'utilise que pdftotext (poppler) et la bibliothèque standard.
Code de sortie : 0 si tout est conforme, 1 sinon.

Contrôle A — contenu (exigé) : le texte des pages 12 et 13 est extrait à nouveau par « pdftotext » en mode par
  défaut, colonne par colonne (rognage -x -y -W -H sur la moitié gauche puis la moitié droite de la page), puis
  mis bout à bout dans l'ordre de lecture : p. 12 gauche, p. 12 droite, p. 13 gauche, p. 13 droite. Le script
  s'assure d'abord qu'aucun mot n'est à cheval sur la séparation des colonnes. Les deux côtés sont normalisés de
  la même façon :
    1. ligatures typographiques remplacées par leurs lettres (ﬀ ﬁ ﬂ ﬃ ﬄ ﬅ ﬆ) ;
    2. toute suite de blancs ASCII (espace, tabulation, retours, saut de page) réduite à une espace ; bords rognés.
  Côté transcription, on applique les substitutions déclarées dans index.json (forme transcrite -> forme produite
  par pdftotext), chacune devant s'appliquer au moins une fois. Puis on exige que « avant + transcription +
  après » apparaisse exactement une fois, tel quel, dans le texte des colonnes : correspondance exacte, en entier
  et dans l'ordre, encadrée par le contexte déclaré (intitulé et titre d'encadré avant, intitulé suivant après).
  Comme pdftotext retire lui-même les traits d'union de fin de ligne, le contrôle A confirme aussi les césures.

Contrôle B — structure (complément) : à partir des positions des mots (« pdftotext -bbox ») dans les zones
  déclarées, on reconstruit les lignes transcrites sans rien emprunter à la construction :
    - mots d'une ligne physique joints par une espace (écart d'au moins 1 pt) ou collés (écart plus petit) ;
    - ligne finie par « - » : recollée sans espace, trait d'union retiré, sauf mot composé déclaré conservé ;
    - ligne justifiée (fin à la marge droite de l'encadré, à 0,05 pt près, et espaces différentes de la largeur
      naturelle) : recollée à la suivante par une espace ;
    - ligne courte dont toutes les espaces ont la largeur naturelle exacte (2,72727 pt, ou 3,38182 pt après une
      ponctuation forte ; à 0,0006 pt près) : fin de la ligne transcrite ;
    - tout autre cas : ligne indécidable, gabarit non conforme ;
    - la dernière ligne de la dernière zone doit être une fin de paragraphe (sinon le gabarit continue au-delà
      des zones déclarées : non conforme).
  Le script contrôle aussi les bords des zones (titre blanc de l'encadré juste au-dessus, intitulé ou bas de
  colonne juste en dessous, haut de colonne au passage de colonne), la marge gauche (aucun texte des auteurs dans
  la zone) et les écarts verticaux (13,549 pt, ou 15,545 pt autour d'une liste ; tout autre écart, par exemple
  une ligne vide, rend le gabarit non conforme). Le texte reconstruit doit être identique, caractère pour
  caractère, à la transcription.
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
PAGES = (12, 13)
COUPE = 298                                  # séparation des colonnes pour le rognage (points ; gouttière 276-305)
LARGEUR_PAGE, HAUTEUR_PAGE = 596, 842

# constantes du contrôle B, mesurées sur le PDF (points)
MILIEU = 297.638
MARGE_COLONNE = {'g': 70.866, 'd': 306.142}     # texte des auteurs
MARGE_ENCADRE = {'g': 86.457, 'd': 321.732}     # texte des encadrés
MARGE_DROITE = {'g': 273.540, 'd': 508.815}     # fin d'une ligne justifiée finie par une lettre sans protrusion
TOL_MARGE = 0.05
ESPACES_NATURELLES = (2.72727, 3.38182)          # 0,25 et 0,31 cadratin du corps 10,909 pt
TOL_ESPACE = 0.0006
INTERLIGNES = (13.549, 15.545)
TOL_INTERLIGNE = 0.1
SEUIL_ESPACE = 1.0


def normaliser(s):
    s = s.translate(LIGATURES)
    return BLANCS.sub(' ', s).strip()


def pdftotext(*args):
    return subprocess.run(['pdftotext', *args], capture_output=True, check=True).stdout.decode('utf-8')


_MOTS = {}


def mots(p):
    if p not in _MOTS:
        out = pdftotext('-bbox', '-f', str(p), '-l', str(p), PDF, '-')
        _MOTS[p] = [dict(x0=float(a), y0=float(b), x1=float(c), y1=float(d), t=html.unescape(t))
                    for a, b, c, d, t in re.findall(
                        r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', out)]
    return _MOTS[p]


def colonne(w):
    return 'g' if w['x0'] < MILIEU else 'd'


_DOC = {}


def texte_colonnes():
    """Texte (mode par défaut) des colonnes des pages 12 et 13, dans l'ordre de lecture, normalisé."""
    if not _DOC:
        morceaux, journal = [], []
        for p in PAGES:
            a_cheval = [w['t'] for w in mots(p) if w['x0'] < COUPE < w['x1']]
            if a_cheval:
                raise SystemExit(f'page {p} : mots à cheval sur la séparation des colonnes : {a_cheval}')
            for x, w in ((0, COUPE), (COUPE, LARGEUR_PAGE - COUPE)):
                t = pdftotext('-f', str(p), '-l', str(p), '-x', str(x), '-y', '0', '-W', str(w),
                              '-H', str(HAUTEUR_PAGE), PDF, '-')
                morceaux.append(normaliser(t))
            journal.append(f"page {p} : aucun mot à cheval sur la séparation des colonnes (x = {COUPE} pt)")
        _DOC['texte'] = ' '.join(morceaux)
        _DOC['journal'] = journal
    return _DOC['texte']


def contexte(s, i, n=70):
    return s[max(0, i - n):i] + '⟦' + s[i:i + n] + '…'


def controle_contenu(inv):
    v = inv['verification']
    journal = []
    texte_pdf = texte_colonnes()
    trans = open(os.path.join(ESPACE, inv['fichier']), encoding='utf-8').read()
    for s in v['substitutions']:
        n = trans.count(s['transcription'])
        if n < 1:
            return False, f"substitution sans effet : {s['transcription']!r}", journal
        trans = trans.replace(s['transcription'], s['pdf'])
        journal.append(f"substitution ×{n} : « {s['transcription']} » -> « {s['pdf']} » ({s['raison']})")
    t_tr = normaliser(trans)
    avant, apres = normaliser(v['avant']), normaliser(v['apres'])
    cible = ' '.join(x for x in (avant, t_tr, apres) if x)
    n = texte_pdf.count(cible)
    if n == 1:
        return True, f"trouvée en entier et dans l'ordre, entre les bornes ({len(t_tr)} car. normalisés, 1 occurrence)", journal
    if n > 1:
        return False, f"trouvée {n} fois (une seule occurrence attendue)", journal
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
def lignes_colonne(p, col):
    lignes = []
    for w in sorted((w for w in mots(p) if colonne(w) == col), key=lambda w: (w['y0'], w['x0'])):
        if lignes and abs(lignes[-1]['y0'] - w['y0']) < 1.5:
            lignes[-1]['mots'].append(w)
        else:
            lignes.append(dict(y0=w['y0'], mots=[w]))
    for l in lignes:
        l['mots'].sort(key=lambda w: w['x0'])
        l['x0'], l['x1'] = l['mots'][0]['x0'], l['mots'][-1]['x1']
        ys = sorted(w['y0'] for w in l['mots'])
        l['y'] = ys[len(ys) // 2]       # ordonnée médiane : les mots en gras ont une boîte un peu plus haute
        texte, glue = l['mots'][0]['t'], []
        for i, (a, b) in enumerate(zip(l['mots'], l['mots'][1:])):
            g = b['x0'] - a['x1']
            if g >= SEUIL_ESPACE:
                texte += ' '
                if not (i == 0 and a['t'] == '•'):      # écart après la puce : boîte d'étiquette, pas une espace
                    glue.append(g)
            texte += b['t']
        l['texte'], l['glue'] = texte, glue
    return lignes


def naturelle(glue):
    return all(min(abs(g - e) for e in ESPACES_NATURELLES) <= TOL_ESPACE for g in glue)


def classer(l):
    """Classe une ligne physique (dict : texte, x1, col, glue) d'après sa géométrie seule :
    'cesure' (finie par « - » et pleine), 'justifiee' (pleine, espaces non naturelles),
    'fin' (courte, espaces naturelles) ou 'indecidable' (tout autre cas)."""
    pleine = l['x1'] >= MARGE_DROITE[l['col']] - TOL_MARGE
    nat = naturelle(l['glue'])
    if l['texte'].endswith('-'):
        return 'cesure' if pleine else 'indecidable'
    if pleine and not nat:
        return 'justifiee'
    if not pleine and nat:
        return 'fin'
    return 'indecidable'


def raison_indecidable(l):
    pleine = l['x1'] >= MARGE_DROITE[l['col']] - TOL_MARGE
    nat = naturelle(l['glue'])
    return (f"{'pleine' if pleine else 'courte'}, espaces {'naturelles' if nat else 'non naturelles'}, "
            f"fin à {l['x1']:.3f} pt")


def controle_structure(inv):
    vb = inv['verification']['B']
    zones, conserves = vb['zones'], set(vb['traits_d_union_conserves'])
    physiques, bords = [], []
    for i, z in enumerate(zones):
        p, col = z['page'], z['colonne']
        lc = lignes_colonne(p, col)
        dedans = [k for k, l in enumerate(lc) if z['haut_pt'] - 1 <= (l['y0'] + l['mots'][0]['y1']) / 2 <= z['bas_pt'] + 1]
        if not dedans or dedans != list(range(dedans[0], dedans[-1] + 1)):
            return False, f"p{p} {col} : zone vide ou discontinue", bords
        k0, k1 = dedans[0], dedans[-1]
        # bord haut
        if i == 0:
            if k0 == 0 or lc[k0 - 1]['texte'] != vb['titre_au_dessus'] or lc[k0]['y0'] - lc[k0 - 1]['y0'] > 25:
                return False, f"p{p} {col} : la ligne au-dessus de la zone n'est pas le titre « {vb['titre_au_dessus']} »", bords
            bords.append(f"p{p} {col} : titre « {lc[k0 - 1]['texte']} » juste au-dessus de la zone")
        elif k0 != 0:
            return False, f"p{p} {col} : la zone suivante ne commence pas en haut de colonne", bords
        else:
            bords.append(f"p{p} {col} : la zone commence en haut de colonne")
        # bord bas
        if i < len(zones) - 1:
            if k1 != len(lc) - 1:
                return False, f"p{p} {col} : la zone ne finit pas en bas de colonne alors que le gabarit continue", bords
            bords.append(f"p{p} {col} : la zone finit en bas de colonne")
        elif k1 + 1 < len(lc):
            s = lc[k1 + 1]
            if s['x0'] > MARGE_COLONNE[col] + 3:
                return False, f"p{p} {col} : la ligne sous la zone n'est pas un intitulé : {s['texte']!r}", bords
            bords.append(f"p{p} {col} : intitulé « {s['texte']} » sous la zone (marge de colonne)")
        else:
            bords.append(f"p{p} {col} : rien sous la zone (bas de colonne)")
        for k in range(k0, k1 + 1):
            l = lc[k]
            if l['x0'] < MARGE_ENCADRE[col] - 4:
                return False, f"p{p} {col} y={l['y0']:.2f} : texte hors encadré (marge des auteurs) : {l['texte']!r}", bords
            if k > k0:
                dy = l['y'] - lc[k - 1]['y']
                if not any(abs(dy - v) <= TOL_INTERLIGNE for v in INTERLIGNES):
                    return False, f"p{p} {col} y={l['y0']:.2f} : écart vertical inattendu ({dy:.3f} pt)", bords
            physiques.append(dict(l, col=col, page=p))
    logiques, cour = [], ''
    n_cesures, n_recollees, utilises = 0, 0, set()
    for n, l in enumerate(physiques):
        t = l['texte']
        cour += t
        c = classer(l)
        if c == 'indecidable':
            return False, f"p{l['page']} y={l['y0']:.2f} : ligne indécidable ({raison_indecidable(l)}) : {t!r}", bords
        if n == len(physiques) - 1:
            if c != 'fin':
                return False, (f"p{l['page']} y={l['y0']:.2f} : la dernière ligne de la zone n'est pas une fin de "
                               f"paragraphe ({c}) : le gabarit continue au-delà des zones déclarées : {t!r}"), bords
            logiques.append(cour)
            break
        if c == 'cesure':
            compose = t.split(' ')[-1] + physiques[n + 1]['texte'].split(' ')[0]
            if compose in conserves:
                utilises.add(compose)
            else:
                cour = cour[:-1]
                n_cesures += 1
        elif c == 'justifiee':
            cour += ' '
            n_recollees += 1
        else:
            logiques.append(cour)
            cour = ''
    if utilises != conserves:
        return False, f"trait d'union déclaré conservé sans effet : {sorted(conserves - utilises)}", bords
    reconstruit = '\n'.join(logiques) + '\n'
    trans = open(os.path.join(ESPACE, inv['fichier']), encoding='utf-8').read()
    resume = (f"{len(physiques)} lignes physiques -> {len(logiques)} lignes ; {n_recollees} lignes justifiées "
              f"recollées par une espace, {n_cesures} césure(s), {len(utilises)} trait(s) d'union conservé(s) ; "
              f"espaces, fins de ligne et écarts verticaux conformes")
    if reconstruit == trans:
        return True, resume, bords
    a, b = trans.split('\n'), reconstruit.split('\n')
    for k in range(max(len(a), len(b))):
        x = a[k] if k < len(a) else '∅'
        y = b[k] if k < len(b) else '∅'
        if x != y:
            j = next((i for i in range(min(len(x), len(y))) if x[i] != y[i]), min(len(x), len(y)))
            return False, (f"première ligne différente : n° {k + 1}, colonne {j + 1}\n"
                           f"      transcription : {x[max(0, j - 40):j + 40]!r}\n"
                           f"      positions PDF : {y[max(0, j - 40):j + 40]!r}"), bords
    return False, 'différence de fin de fichier', bords


def main():
    h = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()
    print(f"Source : {PDF}")
    print(f"sha256 : {h} ({'conforme' if h == INDEX['source']['sha256'] else 'DIFFÉRENT — ARRÊT'})")
    if h != INDEX['source']['sha256']:
        sys.exit(1)
    version = subprocess.run(['pdftotext', '-v'], capture_output=True).stderr.decode().splitlines()[0]
    print(f"Outil  : {version} ; Python {sys.version.split()[0]}")
    texte_colonnes()
    for j in _DOC['journal']:
        print(f"Colonnes : {j}")
    print()
    tout_ok, bilan = True, []
    for inv in INDEX['invites']:
        data = open(os.path.join(ESPACE, inv['fichier']), 'rb').read()
        empreinte = hashlib.sha256(data).hexdigest() == inv['sha256']
        fin_ok = data.endswith(b'\n') and not data.endswith(b'\n\n')
        a_ok, a_msg, journal = controle_contenu(inv)
        b_ok, b_msg, bords = controle_structure(inv)
        ok = a_ok and b_ok and empreinte and fin_ok
        tout_ok &= ok
        bilan.append((inv['id'], ok))
        print(f"== {inv['id']} ({inv['section']} {inv['titre']}, p. {inv['pages']['debut']}-{inv['pages']['fin']}) : "
              f"{'CONFORME' if ok else 'NON CONFORME'}")
        print(f"   empreinte du fichier : {'conforme' if empreinte else 'DIFFÉRENTE de index.json'} ; "
              f"fin de ligne finale unique : {'oui' if fin_ok else 'NON'}")
        print(f"   A contenu   : {'conforme' if a_ok else 'NON CONFORME'} — {a_msg}")
        for j in journal:
            print(f"      · {j}")
        print(f"   B structure : {'conforme' if b_ok else 'NON CONFORME'} — {b_msg}")
        for j in bords:
            print(f"      · {j}")
    print()
    n = sum(ok for _, ok in bilan)
    print(f"BILAN : {n}/{len(bilan)} gabarits conformes"
          + ('' if tout_ok else ' ; non conformes : ' + ', '.join(i for i, ok in bilan if not ok)))
    sys.exit(0 if tout_ok else 1)


if __name__ == '__main__':
    main()
