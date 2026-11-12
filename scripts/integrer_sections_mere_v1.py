"""Version intégrée v1 (session-dépôt) : insère une section de résultats de la mère dans le bloc réservé d'un document
du bras, mécaniquement, sans afficher le contenu du bras.

Usage : python -I scripts/integrer_sections_mere_v1.py DOC_BRAS.html SHA_DOC SECTION_MERE.html SHA_SECTION SORTIE.html ETIQUETTE

- Vérifie les deux empreintes (arrêt sinon) ; exige exactement un `<div class="reserve">` dans le document du bras.
- Remplace ce bloc (jusqu'à son `</div>` fermant, sans div imbriqué : arrêt sinon) par le corps (`<body>…</body>`), ou
  par le fragment `<section>…</section>` entier, de la section de la mère, encadré d'un `<section class="resultats-mere">` avec une ligne de provenance ; le `<style>` de la
  section est ajouté, préfixé par `.resultats-mere`.
- Contrôle : le texte du document hors du bloc est identique avant et après (comparaison de textes sans balises) ; le
  texte de la section de la mère est contenu en entier. Imprime seulement des longueurs et des empreintes.
"""
import hashlib, html, re, sys

def sha(b): return hashlib.sha256(b).hexdigest()
def texte(h): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", h, flags=re.S)))).strip()

doc_p, sha_doc, sec_p, sha_sec, out_p, etiquette = sys.argv[1:]
db, sb = open(doc_p, "rb").read(), open(sec_p, "rb").read()
if sha(db) != sha_doc: sys.exit(f"ARRÊT : empreinte du document {sha(db)} ≠ {sha_doc}")
if sha(sb) != sha_sec: sys.exit(f"ARRÊT : empreinte de la section {sha(sb)} ≠ {sha_sec}")
d, s = db.decode(), sb.decode()
if d.count('<div class="reserve">') != 1: sys.exit("ARRÊT : il faut exactement un bloc réservé")
i = d.index('<div class="reserve">'); j = d.index("</div>", i)
if "<div" in d[i + 5:j]: sys.exit("ARRÊT : div imbriqué dans le bloc réservé")
j += len("</div>")
corps = re.search(r"<body[^>]*>(.*)</body>", s, re.S) or re.fullmatch(r"\s*(<section[^>]*>.*</section>)\s*", s, re.S)
if not corps: sys.exit("ARRÊT : section ni document à <body> ni fragment <section> unique")
style = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
def prefixe(css):
    out = []
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", re.sub(r"@page[^{]*\{[^{}]*\}", "", css)):
        sel = ",".join(".resultats-mere " + x.strip() if x.strip() not in ("body", "html", ":root") else ".resultats-mere" for x in m.group(1).split(","))
        out.append(f"{sel} {{{m.group(2)}}}")
    return "\n".join(out)
prov = (f'<p class="provenance-mere" style="font-size:85%;color:#555"><b>Section insérée par la session-dépôt</b> '
        f"({etiquette}) : section de résultats de la session mère, copiée sans retouche, empreinte de la source "
        f"<code>{sha_sec[:16]}…</code> ; elle remplace le bloc réservé du document.</p>")
bloc = f'<section class="resultats-mere">\n{prov}\n{corps.group(1)}\n</section>'
o = d[:i] + bloc + d[j:]
if style.strip():
    o = o.replace("</head>", f"<style>\n/* style de la section de la mère, préfixé */\n{prefixe(style)}\n</style>\n</head>", 1)
# contrôles
hors_avant = texte(d[:i]) + " " + texte(d[j:])
hors_apres = texte(o[:i]) + " " + texte(o[i + len(bloc):])
if texte(d[:i]) != texte(o[:i]) or texte(d[j:]) != texte(o[i + len(bloc):]): sys.exit("ARRÊT : texte du document hors du bloc modifié")
if texte(corps.group(1)) not in texte(o): sys.exit("ARRÊT : section de la mère incomplète")
open(out_p, "w").write(o)
print(f"bloc remplacé : {j - i} caractères → {len(bloc)} ; texte hors du bloc identique ({len(hors_avant)} caractères) ; "
      f"section contenue en entier ; sortie {sha(o.encode())}")
