"""Construit les transcriptions des invites à partir du PDF, par la voie « pdftohtml -xml ».

Usage :
  python3 -I construire.py CHEMIN_PDF ESPACE                 (construit invites/*.txt + extrait/construction.json)
  python3 -I construire.py CHEMIN_PDF ESPACE inventaire P…   (liste les lignes physiques reconstruites des pages P)

Méthode (voie 1 ; la vérification passe par pdftotext, voie indépendante) :
- pdftohtml -xml donne, pour chaque fragment de texte, sa police, sa couleur et sa position
  (unités du XML = points PDF × 1,5).
- Les blocs cités sont composés en police à chasse fixe (SFTT0900 droit, SFIT0900 italique).
  Le texte des auteurs (Times : NimbusRomNo9L), les figures, tableaux, notes et numéros de page
  sont dans d'autres polices : ils sont exclus d'office et signalés s'ils tombent dans un bloc.
- Ligne physique = fragments à chasse fixe de même ordonnée, plus les glyphes mathématiques
  (CMMI9, CMSY9, CMR6) et les marqueurs de continuation (« , » CMMI6 + « → » CMSY6) dont le
  centre vertical tombe dans la ligne (en cas de chevauchement horizontal : ligne voisine).
- Espaces : retrait initial = round((x - marge) / chasse) ; entre deux fragments = round(écart / chasse).
- Marqueur « ,→ » en tête de ligne = ligne de continuation : recollée à la précédente par une espace,
  son retrait (dû à la coupure) est ignoré.
- Lignes vides dans une page : round(écart vertical / interligne) - 1.
- Passage de page : nombre de lignes vides fixé dans la configuration (voir justifications).
- Chiffres en petit corps (CMR6) : indice ou exposant selon la position verticale, rendus par les
  chiffres Unicode en indice (₀…₉) ou en exposant (⁰…⁹) ; deux chiffres empilés = fraction (½).
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys

PDF = sys.argv[1]
ESPACE = sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
XMLDIR = os.path.join(ESPACE, 'extrait', 'xml')
SORTIE = os.path.join(ESPACE, 'invites')

MARGE = 162.0          # marge gauche des blocs (108 pt × 1,5)
CHASSE = 7.0593        # avance d'un caractère SFTT0900 (4,7062 pt × 1,5)
INTERLIGNE = 14.77     # pas des lignes du verbatim (9,85 pt × 1,5)
BAS_DE_PAGE = 1070     # ordonnée maximale d'une ligne de bloc (pages pleines)
HAUT_DE_PAGE = 110     # ordonnée de la première ligne d'une page sans ligne vide reportée
POLICES_BLOC = {'SFTT0900', 'SFIT0900'}
POLICES_MATH = {'CMMI9', 'CMSY9', 'CMR6'}
POLICES_MARQUEUR = {'CMMI6', 'CMSY6'}
INDICES = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
EXPOSANTS = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
FRACTIONS = {('1', '2'): '½', ('1', '3'): '⅓', ('2', '3'): '⅔', ('1', '4'): '¼', ('3', '4'): '¾'}


def xml_page(p):
    os.makedirs(XMLDIR, exist_ok=True)
    chemin = os.path.join(XMLDIR, f'p{p}.xml')
    if not os.path.exists(chemin):
        out = subprocess.run(['pdftohtml', '-xml', '-i', '-q', '-f', str(p), '-l', str(p), '-stdout', PDF],
                             check=True, capture_output=True).stdout
        with open(chemin, 'wb') as f:
            f.write(out)
    src = open(chemin, encoding='utf-8').read()
    polices = {m.group(1): (m.group(3).split('+')[-1], m.group(4))
               for m in re.finditer(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]+)" color="([^"]+)"/>', src)}
    frags = []
    for m in re.finditer(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', src, re.S):
        t, l, w, h, f, s = m.groups()
        texte = html.unescape(re.sub(r'<[^>]+>', '', s))
        frags.append(dict(top=int(t), left=int(l), width=int(w), height=int(h),
                          police=polices[f][0], couleur=polices[f][1], texte=texte))
    return frags


_BBOX = {}


def mots_bbox(p):
    """Mots de pdftotext -bbox (coordonnées converties en unités XML : points × 1,5)."""
    if p not in _BBOX:
        out = subprocess.run(['pdftotext', '-bbox', '-f', str(p), '-l', str(p), PDF, '-'],
                             check=True, capture_output=True).stdout.decode('utf-8')
        _BBOX[p] = [(float(a) * 1.5, float(b) * 1.5, float(c) * 1.5, float(d) * 1.5, html.unescape(t))
                    for a, b, c, d, t in re.findall(
                        r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', out)]
    return _BBOX[p]


def reespacer(page, f):
    """Recalcule les espaces internes d'un fragment à chasse fixe à partir des mots -bbox qu'il couvre."""
    mots = sorted(m for m in mots_bbox(page)
                  if abs(m[1] - f['top']) <= 3 and f['left'] - 2 <= m[0] and m[2] <= f['left'] + f['width'] + 2)
    if not mots:
        return None
    t = mots[0][4]
    for a, b in zip(mots, mots[1:]):
        t += ' ' * max(1, round((b[0] - a[2]) / CHASSE)) + b[4]
    return t


class Ligne:
    def __init__(self, page, top):
        self.page = page
        self.top = top
        self.frags = []          # fragments à chasse fixe et mathématiques
        self.marqueurs = []
        self.etrangers = []      # autres polices tombant dans la ligne

    @property
    def continuation(self):
        txt = ''.join(m['texte'] for m in sorted(self.marqueurs, key=lambda m: m['left']))
        return ',' in txt and '→' in txt

    def texte(self, notes=None):
        notes = [] if notes is None else notes
        debut_notes = len(notes)
        ref = f'p. {self.page}'
        frs = sorted(self.frags, key=lambda f: (f['left'], f['top']))
        petits = [f for f in frs if f['police'] == 'CMR6']
        consommes, remplacements = set(), {}
        for i, a in enumerate(petits):
            for b in petits[i + 1:]:
                if abs(a['left'] - b['left']) <= 1 and a['top'] != b['top'] and id(b) not in consommes:
                    haut, bas = (a, b) if a['top'] < b['top'] else (b, a)
                    frac = FRACTIONS.get((haut['texte'], bas['texte']), haut['texte'] + '⁄' + bas['texte'])
                    remplacements[id(haut)] = dict(haut, texte=frac, width=max(a['width'], b['width']), fraction=True)
                    consommes.add(id(bas))
                    notes.append(('fraction', ref, f"{haut['texte']} sur {bas['texte']}", frac))
        sortie, prec_droite = [], None
        centre = self.top + 8.5
        for f in frs:
            if id(f) in consommes:
                continue
            f = remplacements.get(id(f), f)
            t = f['texte']
            if f['police'] == 'CMR6' and not f.get('fraction') and len(t) == 1 and t.isdigit():
                c = f['top'] + f['height'] / 2
                if c > centre + 2:
                    t = t.translate(INDICES)
                    notes.append(('indice', ref, f['texte'], t))
                elif c < centre - 2:
                    t = t.translate(EXPOSANTS)
                    notes.append(('exposant', ref, f['texte'], t))
            elif f['police'] in POLICES_MATH and f['police'] != 'CMR6':
                notes.append(('glyphe mathématique', ref, f"{t} ({f['police']})", t))
            base = MARGE if prec_droite is None else prec_droite
            brut = (f['left'] - base) / CHASSE
            n = max(0, round(brut))
            if abs(brut - round(brut)) > 0.3 and f['police'] in POLICES_BLOC:
                notes.append(('espacement ambigu', ref, f'{brut:+.2f} chasse avant « {t[:20]} »', ' ' * n))
            sortie.append(' ' * n + t)
            if f['police'] in POLICES_BLOC:
                attendu = f['width'] / CHASSE
                if abs(attendu - len(t)) > 0.6:
                    t2 = reespacer(self.page, f)
                    if t2 is None or ' '.join(t2.split()) != ' '.join(t.split()) or abs(attendu - len(t2)) > 0.6:
                        raise SystemExit(f'{ref}: largeur incohérente non résolue « {t} » / « {t2} »')
                    notes.append(('espace multiple', ref, f'fragment de {attendu:.2f} chasses pour {len(t)} car. ; '
                                  f'espacement repris des positions des mots', t2))
                    sortie[-1] = ' ' * n + t2
            prec_droite = f['left'] + f['width']
        res = ''.join(sortie)
        for k in range(debut_notes, len(notes)):
            n = notes[k]
            notes[k] = (n[0], f"{n[1]}, ligne « {res.strip()[:60]}… »", n[2], n[3])
        return res


def lignes_page(p):
    frags = xml_page(p)
    lignes = {}
    for f in frags:
        if f['police'] in POLICES_BLOC and f['height'] == 17:
            cle = next((k for k in lignes if abs(k - f['top']) <= 2), f['top'])
            lignes.setdefault(cle, Ligne(p, cle)).frags.append(f)
    tops = sorted(lignes)
    for f in frags:
        if f['police'] in POLICES_BLOC and f['height'] == 17:
            continue
        c = f['top'] + f['height'] / 2
        if f['police'] in POLICES_MARQUEUR:
            candidats = sorted((k for k in tops if k <= c <= k + 17), key=lambda k: abs(k + 8.5 - c))
        else:
            candidats = sorted((k for k in tops if abs(k + 8.5 - c) <= 20), key=lambda k: abs(k + 8.5 - c))
        if not candidats:
            continue
        choisi = candidats[0]
        if f['police'] not in POLICES_MARQUEUR:
            for k in candidats:
                if not any(not (f['left'] + f['width'] <= g['left'] + 1 or g['left'] + g['width'] <= f['left'] + 1)
                           for g in lignes[k].frags):
                    choisi = k
                    break
        if f['police'] in POLICES_MARQUEUR:
            lignes[choisi].marqueurs.append(f)
        elif f['police'] in POLICES_MATH:
            lignes[choisi].frags.append(f)
        else:
            lignes[choisi].etrangers.append(f)
    return [lignes[k] for k in tops]


def chercher(lignes, motif, debut=0, exacte=False, continuation_ok=True):
    for i in range(debut, len(lignes)):
        t = lignes[i].texte()
        ok = (t == motif) if exacte else t.lstrip().startswith(motif)
        if ok and (continuation_ok or not lignes[i].continuation):
            return i
    raise SystemExit(f'ligne introuvable : {motif!r}')


def construire(inv, cache):
    lignes_logiques = []      # (texte, page, top) ; texte None = ligne vide
    notes, etrangers, zones, diag = [], [], [], []
    for s_i, seg in enumerate(inv['segments']):
        p = seg['page']
        lp = cache.setdefault(p, lignes_page(p))
        i0 = chercher(lp, seg['debut'], continuation_ok=False)
        i1 = chercher(lp, seg['fin'], debut=i0, exacte=seg.get('fin_exacte', False))
        if s_i > 0:
            saut = inv['sauts'][s_i - 1]
            lignes_logiques.extend([(None, p, None)] * saut['lignes_vides'])
            prec = inv['segments'][s_i - 1]
            diag.append(dict(passage=f"p{prec['page']}→p{p}", derniere_ligne_y=prec_top,
                             places_libres=round((BAS_DE_PAGE - prec_top) / INTERLIGNE, 2),
                             premiere_ligne_y=lp[i0].top,
                             lignes_vides_en_haut=round((lp[i0].top - HAUT_DE_PAGE) / INTERLIGNE, 2),
                             retenu=saut['lignes_vides'], certitude=saut['certitude']))
        if lp[i0].continuation:
            raise SystemExit(f"{inv['id']}: le segment p{p} commence sur une ligne de continuation")
        zone = dict(page=p, haut_xml=lp[i0].top, bas_xml=lp[i1].top + 17)
        zones.append(zone)
        for k in range(i0, i1 + 1):
            l = lp[k]
            if l.etrangers:
                etrangers.extend(f"p{p} y{l.top}: {e['texte']} ({e['police']})" for e in l.etrangers)
            t = l.texte(notes)
            if l.continuation:
                if not lignes_logiques or lignes_logiques[-1][0] is None:
                    raise SystemExit(f"{inv['id']}: continuation sans ligne précédente p{p} y{l.top}")
                prev = lignes_logiques[-1]
                lignes_logiques[-1] = (prev[0].rstrip(' ') + ' ' + t.lstrip(' '), prev[1], prev[2])
            else:
                if k > i0:
                    vides = round((l.top - lp[k - 1].top) / INTERLIGNE) - 1
                    if vides < 0:
                        raise SystemExit(f'écart vertical négatif p{p} y{l.top}')
                    lignes_logiques.extend([(None, p, None)] * vides)
                lignes_logiques.append((t, p, l.top))
        prec_top = lp[i1].top
        # fragments d'autres polices dans la zone verticale du segment
        for f in xml_page(p):
            if zone['haut_xml'] - 2 <= f['top'] <= zone['bas_xml'] and \
               f['police'] not in POLICES_BLOC | POLICES_MATH | POLICES_MARQUEUR:
                etrangers.append(f"p{p} y{f['top']} (zone): {f['texte']} ({f['police']})")
    texte = '\n'.join('' if t is None else t for t, _, _ in lignes_logiques) + '\n'
    return texte, notes, etrangers, zones, diag


def decrire(inv, texte, notes, zones, diag):
    """Assemble l'entrée d'index.json : retraits, normalisations, doutes, remarques, vérification."""
    pages_bloc = [seg['page'] for seg in inv['segments']]
    retraits, normalisations, doutes, remarques = [], [], [], list(inv.get('remarques', []))
    n_cont = inv['_continuations']
    if n_cont:
        retraits.append(f"marqueurs de continuation « ,→ » : {n_cont} retirés, chaque ligne coupée recollée "
                        f"à la précédente par une espace")
    entieres = {r['page'] for r in inv['verification']['retraits'] if r.get('tout')}
    for pg in range(pages_bloc[0], pages_bloc[-1]):
        if pg not in entieres:
            retraits.append(f"numéro de page « {pg} » (pied de page) entre deux parties du bloc")
    for r in inv['verification']['retraits']:
        retraits.append(f"page {r['page']} : {r['motif']}")
    retraits.extend(inv.get('retraits_supplementaires', []))
    glyphes = sorted({n[3] for n in notes if n[0] == 'glyphe mathématique'})
    if glyphes:
        normalisations.append('glyphes composés en police mathématique, gardés tels que pdftotext les décode : '
                              + ' '.join(glyphes))
    for n in notes:
        if n[0] in ('indice', 'exposant'):
            normalisations.append(f"{n[1]} : chiffre « {n[2]} » composé en {n[0]} (petit corps, décalé) "
                                  f"rendu par le caractère Unicode « {n[3]} »")
        elif n[0] == 'fraction':
            normalisations.append(f"{n[1]} : fraction empilée {n[2]} (deux chiffres l'un au-dessus de l'autre) rendue par « {n[3]} »")
        elif n[0] == 'espace multiple':
            remarques.append(f"{n[1]} : espace double de l'original conservée (mesurée sur la grille à chasse "
                             f"fixe) : « {n[3].strip()} »")
    normalisations.append('ligatures : aucune rencontrée dans le bloc (police à chasse fixe)')
    sauts = []
    for d, sj in zip(diag, inv['sauts']):
        e = dict(passage=d['passage'], lignes_vides=sj['lignes_vides'], certitude=sj['certitude'],
                 justification=sj['justification'])
        sauts.append(e)
        if sj['certitude'] == 'doute':
            doutes.append(f"passage {d['passage']} : {sj['lignes_vides']} ligne(s) vide(s) retenue(s) — {sj['justification']}")
        else:
            remarques.append(f"passage {d['passage']} : {sj['lignes_vides']} ligne(s) vide(s), établi par mesure — "
                             f"{sj['justification']}")
    doutes.extend(inv.get('doutes', []))
    v = dict(inv['verification'])
    v['zones'] = [dict(page=z['page'], haut_pt=round(z['haut_xml'] / 1.5, 2), bas_pt=round(z['bas_xml'] / 1.5, 2))
                  for z in zones]
    v['sauts'] = [sj['lignes_vides'] for sj in inv['sauts']]
    data = texte.encode('utf-8')
    return dict(id=inv['id'], fichier=f"invites/{inv['id']}.txt", section=inv['section'], titre=inv['titre'],
                pages=dict(debut=pages_bloc[0], fin=pages_bloc[-1]),
                introduction=inv.get('introduction'), caracteres=len(texte),
                octets=len(data), lignes=texte.count('\n'), sha256=hashlib.sha256(data).hexdigest(),
                retraits=retraits, normalisations=normalisations, doutes=doutes,
                elisions=inv.get('elisions', []), remarques=remarques, sauts_de_page=sauts, verification=v)


def main():
    cfg = json.load(open(os.path.join(ICI, 'config_invites.json'), encoding='utf-8'))
    os.makedirs(SORTIE, exist_ok=True)
    cache, entrees, journal = {}, [], {}
    for inv in cfg['invites']:
        texte, notes, etrangers, zones, diag = construire(inv, cache)
        if etrangers:
            raise SystemExit(f"{inv['id']}: fragments d'autres polices dans le bloc : {etrangers}")
        for ch in texte:
            if ch != '\n' and (ord(ch) < 32 or 0xFB00 <= ord(ch) <= 0xFB06 or ch in '\u00a0\u2009\u202f\u200b'):
                raise SystemExit(f"{inv['id']}: caractère à examiner {ch!r}")
        chemin = os.path.join(SORTIE, inv['id'] + '.txt')
        data = texte.encode('utf-8')
        if os.path.exists(chemin) and open(chemin, 'rb').read() != data:
            print(f"ATTENTION {inv['id']}: le fichier existant diffère ; réécrit")
        with open(chemin, 'wb') as f:
            f.write(data)
        inv['_continuations'] = sum(1 for z in zones for l in cache[z['page']]
                                    if z['haut_xml'] <= l.top <= z['bas_xml'] - 17 and l.continuation)
        entrees.append(decrire(inv, texte, notes, zones, diag))
        journal[inv['id']] = dict(notes=notes, passages=diag)
        print(f"{inv['id']:28s} {len(texte):6d} car.  {hashlib.sha256(data).hexdigest()[:16]}  notes={len(notes)}")
    with open(os.path.join(ESPACE, 'extrait', 'construction.json'), 'w', encoding='utf-8') as f:
        json.dump(journal, f, ensure_ascii=False, indent=1)
    versions = {o: subprocess.run([o, '-v'], capture_output=True).stderr.decode().splitlines()[0]
                for o in ('pdftotext', 'pdftohtml')}
    index = dict(
        source=dict(chemin=PDF, sha256=hashlib.sha256(open(PDF, 'rb').read()).hexdigest(),
                    titre='Diffuse AI Control on Fuzzy Tasks (Terekhov, Gulcehre, Hebbar, Benton), arXiv 2606.08892v2',
                    pages=71, pagination='numéro de page du fichier = numéro imprimé'),
        outils=dict(versions, python=sys.version.split()[0]),
        methode=cfg['methode'], invites=entrees)
    with open(os.path.join(ESPACE, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('index.json écrit :', len(entrees), 'invites')


def inventaire(pages):
    for p in pages:
        print(f'=== page {p}')
        for i, l in enumerate(lignes_page(p)):
            t = l.texte()
            etr = ' ETRANGER:' + '|'.join(e['texte'] for e in l.etrangers) if l.etrangers else ''
            print(f"{i:3d} {l.top:5d} {'C' if l.continuation else ' '} {t}{etr}")


if __name__ == '__main__':
    if len(sys.argv) > 3 and sys.argv[3] == 'inventaire':
        inventaire([int(x) for x in sys.argv[4:]])
    else:
        main()
