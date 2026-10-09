"""Construit les transcriptions des gabarits d'invites de l'annexe B de TRACE (arXiv 2606.07054v1),
à partir du PDF, par la voie « pdftohtml -xml ».

Usage :
  python3 -I construire.py CHEMIN_PDF ESPACE                (construit invites/*.txt, index.json, extrait/construction.json)
  python3 -I construire.py CHEMIN_PDF ESPACE inventaire P…  (liste les lignes physiques reconstruites des pages P)

Méthode (voie 1 ; la vérification passe par pdftotext, voie indépendante) :
- pdftohtml -xml donne, pour chaque fragment de texte, sa police, sa couleur et sa position
  (unités du XML = points PDF × 1,5). Le zoom est plafonné : la résolution vaut 0,67 point.
- Mise en page : deux colonnes ; chaque gabarit est un encadré dont le titre est en blanc (texte de l'encadré
  en Times noir, NimbusRomNo9L-Regu, quelques mots en gras, NimbusRomNo9L-Medi). Le texte des auteurs est dans
  la même police : il se distingue par sa marge gauche (colonne : 106 ou 459 unités ; encadré : 129 à 130 ou
  482 à 483). Toute ligne qui sort de l'encadré arrête le script.
- Ligne physique = fragments de même ordonnée dans la colonne, joints par une espace si l'écart dépasse
  1 point (pdftohtml a déjà mis une espace simple entre les mots d'un même fragment).
- Le texte est justifié : les retours à la ligne de composition ne sont pas ceux de l'original.
  Règle de recollement (une ligne transcrite = un paragraphe ou un retour forcé du PDF) :
    1. ligne finie par « - » : césure, trait d'union retiré et mot recollé sans espace, sauf mot composé
       déclaré dans la configuration (« traits_d_union_conserves ») ;
    2. ligne pleine (fin à moins de 2 unités, 1,33 point, de la marge droite de l'encadré) : ligne justifiée,
       recollée à la suivante par une espace, sauf fin de paragraphe déclarée dans la configuration
       (« fins_de_paragraphe_declarees ») quand la résolution du XML ne permet pas de trancher ;
    3. sinon (ligne courte) : fin de paragraphe ou retour forcé, la ligne transcrite s'arrête.
- Lignes vides : aucune dans les encadrés (écarts verticaux réguliers) ; un écart anormal arrête le script.
- Caractères : rien n'est corrigé ; ligatures typographiques (aucune attendue) remplacées par leurs lettres
  et signalées.
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

E = 1.5                                   # unités XML par point PDF
MILIEU = 297.638 * E                      # séparation des deux colonnes (milieu de la page)
MARGE_COLONNE = {'g': 70.866 * E, 'd': 306.142 * E}          # marge gauche du texte des auteurs
MARGE_ENCADRE = {'g': 86.457 * E, 'd': 321.732 * E}          # marge gauche du texte des encadrés
MARGE_DROITE = {'g': 273.540 * E, 'd': 508.815 * E}          # marge droite du texte des encadrés
TOL_PLEINE = 2.0                          # unités : une ligne justifiée finit à la marge (+ protrusion)
INTERLIGNES = (20.3, 23.3)                # 13,55 pt ; 15,54 pt autour des listes à puces
POLICE_TEXTE = 'NimbusRomNo9L-Regu'
POLICE_GRAS = 'NimbusRomNo9L-Medi'
NOIR, BLANC = '#000000', '#ffffff'
LIGATURES = {'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬅ': 'st', 'ﬆ': 'st'}


def xml_page(p):
    os.makedirs(XMLDIR, exist_ok=True)
    chemin = os.path.join(XMLDIR, f'p{p}.xml')
    if not os.path.exists(chemin):
        out = subprocess.run(['pdftohtml', '-xml', '-i', '-q', '-f', str(p), '-l', str(p), '-stdout', PDF],
                             check=True, capture_output=True).stdout
        with open(chemin, 'wb') as f:
            f.write(out)
    src = open(chemin, encoding='utf-8').read()
    polices = {m.group(1): (m.group(3).split('+')[-1], m.group(4), int(m.group(2)))
               for m in re.finditer(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]+)" color="([^"]+)"/>', src)}
    frags = []
    for m in re.finditer(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', src, re.S):
        t, l, w, h, f, s = m.groups()
        texte = html.unescape(re.sub(r'<[^>]+>', '', s))
        police, couleur, corps = polices[f]
        frags.append(dict(top=int(t), left=int(l), width=int(w), height=int(h), police=police, couleur=couleur,
                          corps=corps, texte=texte, col='g' if int(l) < MILIEU else 'd'))
    return frags


class Ligne:
    def __init__(self, page, col, top):
        self.page, self.col, self.top = page, col, top
        self.frags = []

    @property
    def gauche(self):
        return min(f['left'] for f in self.frags)

    @property
    def droite(self):
        return max(f['left'] + f['width'] for f in self.frags)

    @property
    def blanche(self):
        return any(f['couleur'] == BLANC for f in self.frags)

    def texte(self):
        frs = sorted(self.frags, key=lambda f: f['left'])
        t, prec = '', None
        for f in frs:
            if prec is not None:
                t += ' ' if f['left'] - prec >= E else ''
            t += f['texte']
            prec = f['left'] + f['width']
        return t

    def gras(self):
        return [f['texte'] for f in self.frags if f['police'] == POLICE_GRAS]


def lignes_page(p):
    lignes = {}
    for f in xml_page(p):
        cle = next((k for k in lignes if k[0] == f['col'] and abs(k[1] - f['top']) <= 3), (f['col'], f['top']))
        lignes.setdefault(cle, Ligne(p, f['col'], cle[1])).frags.append(f)
    res = {'g': [], 'd': []}
    for k in sorted(lignes, key=lambda k: k[1]):
        res[k[0]].append(lignes[k])
    return res


def chercher(lignes, motif, debut=0):
    for i in range(debut, len(lignes)):
        if lignes[i].texte().startswith(motif):
            return i
    raise SystemExit(f'ligne introuvable : {motif!r}')


def construire(inv, cache):
    """Rassemble les lignes physiques des segments, contrôle leur appartenance à l'encadré, puis les recolle."""
    physiques, journal, zones, passages = [], [], [], []
    for s_i, seg in enumerate(inv['segments']):
        p, col = seg['page'], seg['colonne']
        lp = cache.setdefault(p, lignes_page(p))[col]
        i0 = chercher(lp, seg['debut'])
        i1 = chercher(lp, seg['fin'], i0)
        # bord haut : titre blanc de l'encadré (premier segment) ou haut de colonne (segment suivant)
        if s_i == 0:
            if i0 == 0 or not lp[i0 - 1].blanche or lp[i0 - 1].texte() != inv['titre_encadre']:
                raise SystemExit(f"{inv['id']}: la ligne qui précède le bloc n'est pas le titre blanc de l'encadré")
            journal.append(f"p{p} {col} : bloc précédé du titre blanc « {lp[i0 - 1].texte()} »")
        elif i0 != 0:
            raise SystemExit(f"{inv['id']}: le segment p{p} {col} ne commence pas en haut de colonne")
        # bord bas : intitulé suivant (marge de colonne) ou fin de colonne
        if s_i < len(inv['segments']) - 1:
            if i1 != len(lp) - 1:
                raise SystemExit(f"{inv['id']}: le segment p{p} {col} ne finit pas en bas de colonne")
        elif i1 + 1 < len(lp):
            suiv = lp[i1 + 1]
            if suiv.gauche > MARGE_COLONNE[col] + 3 or not suiv.gras():
                raise SystemExit(f"{inv['id']}: la ligne qui suit le bloc n'est pas un intitulé : {suiv.texte()!r}")
            journal.append(f"p{p} {col} : bloc suivi de l'intitulé « {suiv.texte()} »")
        else:
            journal.append(f"p{p} {col} : bloc en bas de colonne, rien en dessous")
        for k in range(i0, i1 + 1):
            l = lp[k]
            for f in l.frags:
                if f['couleur'] != NOIR or f['police'] not in (POLICE_TEXTE, POLICE_GRAS):
                    raise SystemExit(f"{inv['id']}: fragment étranger p{p} y{l.top} : {f}")
                if f['left'] < MARGE_ENCADRE[col] - 6:
                    raise SystemExit(f"{inv['id']}: texte hors encadré p{p} y{l.top} : {f['texte']!r}")
            if k > i0:
                dy = l.top - lp[k - 1].top
                if not any(abs(dy - v) <= 1.5 for v in INTERLIGNES):
                    raise SystemExit(f"{inv['id']}: écart vertical inattendu p{p} y{l.top} : {dy}")
            physiques.append(l)
        zones.append(dict(page=p, colonne=col, haut_pt=round(lp[i0].top / E, 2),
                          bas_pt=round((lp[i1].top + lp[i1].frags[0]['height']) / E, 2),
                          lignes_physiques=i1 - i0 + 1))
        if s_i > 0:
            prec = inv['segments'][s_i - 1]
            passages.append(dict(de=f"p. {prec['page']}, colonne {'gauche' if prec['colonne'] == 'g' else 'droite'}",
                                 vers=f"p. {p}, colonne {'gauche' if col == 'g' else 'droite'}"))
    # recollement
    conserves = set(inv.get('traits_d_union_conserves', []))
    fins = {d['ligne']: d for d in inv.get('fins_de_paragraphe_declarees', [])}
    logiques, cour = [], ''
    notes = dict(cesures=[], conserves=[], recollees=0, fins_declarees=[], gras=[])
    for n, l in enumerate(physiques):
        t = l.texte()
        notes['gras'].extend(l.gras())
        cour += t
        if n == len(physiques) - 1:
            logiques.append(cour)
            break
        suiv = physiques[n + 1].texte()
        if t.endswith('-'):
            gauche_mot = t.split(' ')[-1]
            droite_mot = suiv.split(' ')[0]
            compose = gauche_mot + droite_mot
            if compose in conserves:
                notes['conserves'].append(f"{gauche_mot}|{droite_mot}")
            else:
                cour = cour[:-1]
                notes['cesures'].append(f"{gauche_mot}|{droite_mot} → {gauche_mot[:-1]}{droite_mot}")
        elif l.droite >= MARGE_DROITE[l.col] - TOL_PLEINE and t not in fins:
            cour += ' '
            notes['recollees'] += 1
        else:
            if t in fins:
                notes['fins_declarees'].append(fins[t])
            logiques.append(cour)
            cour = ''
    for c in conserves:
        if not any(x.replace('|', '') == c for x in notes['conserves']):
            raise SystemExit(f"{inv['id']}: trait d'union déclaré sans effet : {c}")
    for t in fins:
        if not any(d['ligne'] == t for d in notes['fins_declarees']):
            raise SystemExit(f"{inv['id']}: fin de paragraphe déclarée sans effet : {t}")
    texte = '\n'.join(logiques) + '\n'
    return texte, physiques, notes, journal, zones, passages


def compter(texte, car):
    return texte.count(car)


def decrire(inv, texte, physiques, notes, journal, zones, passages, ligatures):
    pages = sorted({z['page'] for z in zones})
    n_phys, n_log = len(physiques), texte.count('\n')
    retraits = [f"titre de l'encadré « {inv['titre_encadre']} » (blanc sur bandeau de couleur), au-dessus du bloc ; "
                f"intitulé de section « {inv['section']} {inv['titre']} » (gras, texte des auteurs)"]
    retraits.append(f"retours à la ligne de composition (texte justifié) : {notes['recollees']} lignes physiques "
                    f"recollées à la suivante par une espace")
    if notes['cesures']:
        retraits.append(f"traits d'union de césure en fin de ligne : {len(notes['cesures'])} retirés, mots recollés "
                        f"sans espace")
    normalisations = []
    if notes['cesures']:
        normalisations.append('césures résolues (fin de ligne|début de ligne suivante → mot transcrit) : '
                              + ' ; '.join(notes['cesures']))
    else:
        normalisations.append('césures : aucune')
    if notes['conserves']:
        normalisations.append("traits d'union de fin de ligne conservés (mots composés ; fin de ligne|début de "
                              "ligne suivante) : " + ' ; '.join(notes['conserves']))
    normalisations.append(f"lignes : {n_phys} lignes physiques du PDF → {n_log} lignes transcrites (une par paragraphe "
                          f"ou retour forcé du PDF ; mots séparés par une espace simple)")
    if ligatures:
        normalisations.append('ligatures remplacées par leurs lettres : ' + ' '.join(ligatures))
    else:
        normalisations.append('ligatures : aucune dans le texte extrait (pdftotext et pdftohtml rendent déjà les lettres)')
    normalisations.append(f"guillemets et apostrophes : aucune normalisation ; « \" » droits (U+0022) : "
                          f"{compter(texte, chr(34))} ; apostrophes typographiques « ’ » (U+2019) : "
                          f"{compter(texte, '’')} ; tels qu'imprimés")
    if '•' in texte:
        normalisations.append(f"listes à puces : chaque élément sur sa ligne, « • » (U+2022) suivi d'une espace ; "
                              f"le retrait de la liste (mise en page) n'est pas transcrit ; {compter(texte, '•')} puces")
    remarques = list(inv.get('remarques', []))
    if notes['gras']:
        remarques.append('composé en gras dans le PDF (gras non transcrit) : '
                         + ' ; '.join(f"« {g} »" for g in notes['gras']))
    for d in notes['fins_declarees']:
        remarques.append(f"fin de paragraphe déclarée après « {d['ligne']} » : {d['justification']}")
    doutes = list(inv.get('doutes', []))
    doutes.append("structure des lignes : une ligne transcrite par paragraphe ou retour forcé du PDF ; les lignes vides "
                  "et les retours à la ligne internes de l'invite d'origine, s'il y en avait, ne sont pas visibles "
                  "(voir doutes_communs).")
    if '’' in texte:
        doutes.append(f"apostrophe « ’ » (U+2019), {compter(texte, '’')} fois : LaTeX compose l'apostrophe droite ' en ’ ; "
                      f"l'invite d'origine portait probablement « ' ». Transcrit tel qu'imprimé.")
    if '–' in texte:
        exemples = sorted(set(re.findall(r'\d–\d', texte)))
        doutes.append(f"tiret demi-cadratin « – » (U+2013), {compter(texte, '–')} fois ({', '.join(exemples)}) : "
                      f"produit par « -- » ou « – » dans la source LaTeX ; l'invite d'origine portait peut-être un "
                      f"trait d'union « - ». Transcrit tel qu'imprimé.")
    if '•' in texte:
        doutes.append("puces « • » : marques de liste de LaTeX ; la marque de l'invite d'origine (par exemple « - ») "
                      "n'est pas connue. Transcrit « • » suivi d'une espace.")
    for ps, sj in zip(passages, inv.get('passages', [])):
        ps.update(sj)
        remarques.append(f"passage {ps['de']} → {ps['vers']} : {sj['lignes_vides']} ligne vide, établi par mesure — "
                         f"{sj['justification']}")
    v = dict(inv['verification'])
    v['B'] = dict(zones=[{k: z[k] for k in ('page', 'colonne', 'haut_pt', 'bas_pt')} for z in zones],
                  titre_au_dessus=inv['titre_encadre'],
                  traits_d_union_conserves=inv.get('traits_d_union_conserves', []))
    data = texte.encode('utf-8')
    return dict(id=inv['id'], fichier=f"invites/{inv['id']}.txt", section=inv['section'], titre=inv['titre'],
                titre_encadre=inv['titre_encadre'], pages=dict(debut=pages[0], fin=pages[-1]),
                colonnes=[f"p. {z['page']}, colonne {'gauche' if z['colonne'] == 'g' else 'droite'}" for z in zones],
                introduction=None, caracteres=len(texte), octets=len(data), lignes=n_log,
                lignes_physiques=n_phys, sha256=hashlib.sha256(data).hexdigest(),
                retraits=retraits, normalisations=normalisations, doutes=doutes,
                elisions=inv.get('elisions', []), remarques=remarques, passages=passages,
                bords=journal, verification=v)


def main():
    cfg = json.load(open(os.path.join(ICI, 'config_invites.json'), encoding='utf-8'))
    os.makedirs(SORTIE, exist_ok=True)
    cache, entrees, journal = {}, [], {}
    for inv in cfg['invites']:
        texte, physiques, notes, bords, zones, passages = construire(inv, cache)
        ligatures = sorted({ch for ch in texte if ch in LIGATURES})
        for lg in ligatures:
            texte = texte.replace(lg, LIGATURES[lg])
        for ch in texte:
            if ch != '\n' and (ord(ch) < 32 or ch in ' ­  ​﻿'):
                raise SystemExit(f"{inv['id']}: caractère à examiner {ch!r}")
        if '  ' in texte or ' \n' in texte or '\n ' in texte or texte.startswith(' '):
            raise SystemExit(f"{inv['id']}: espace double ou espace en bord de ligne")
        chemin = os.path.join(SORTIE, inv['id'] + '.txt')
        data = texte.encode('utf-8')
        if os.path.exists(chemin) and open(chemin, 'rb').read() != data:
            print(f"ATTENTION {inv['id']}: le fichier existant diffère ; réécrit")
        with open(chemin, 'wb') as f:
            f.write(data)
        entrees.append(decrire(inv, texte, physiques, notes, bords, zones, passages, ligatures))
        journal[inv['id']] = dict(notes=notes, bords=bords, zones=zones,
                                  physiques=[dict(page=l.page, colonne=l.col, top=l.top, gauche=l.gauche,
                                                  droite=l.droite, texte=l.texte()) for l in physiques])
        print(f"{inv['id']:6s} {len(texte):6d} car.  {texte.count(chr(10)):3d} lignes  "
              f"{hashlib.sha256(data).hexdigest()[:16]}  césures={len(notes['cesures'])} "
              f"recollées={notes['recollees']}")
    with open(os.path.join(ESPACE, 'extrait', 'construction.json'), 'w', encoding='utf-8') as f:
        json.dump(journal, f, ensure_ascii=False, indent=1)
        f.write('\n')
    versions = {o: subprocess.run([o, '-v'], capture_output=True).stderr.decode().splitlines()[0]
                for o in ('pdftotext', 'pdftohtml')}
    index = dict(
        source=dict(chemin=PDF, sha256=hashlib.sha256(open(PDF, 'rb').read()).hexdigest(),
                    titre=cfg['source']['titre'], pages=cfg['source']['pages'],
                    pagination=cfg['source']['pagination']),
        outils=dict(versions, python=sys.version.split()[0]),
        methode=cfg['methode'], geometrie=cfg['geometrie'], doutes_communs=cfg['doutes_communs'],
        invites=entrees)
    with open(os.path.join(ESPACE, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('index.json écrit :', len(entrees), 'gabarits')


def inventaire(pages):
    for p in pages:
        for col, lignes in lignes_page(p).items():
            print(f'=== page {p}, colonne {col}')
            for i, l in enumerate(lignes):
                b = 'BLANC ' if l.blanche else ''
                pleine = 'P' if l.droite >= MARGE_DROITE[col] - TOL_PLEINE else ' '
                print(f"{i:3d} top={l.top:5d} g={l.gauche:4d} d={l.droite:4d} {pleine} {b}{l.texte()}")


if __name__ == '__main__':
    if len(sys.argv) > 3 and sys.argv[3] == 'inventaire':
        inventaire([int(x) for x in sys.argv[4:]])
    else:
        main()
