"""(v2 : tables de l'inventaire à colonnes de largeur fixée.) Convertit le sous-ensemble Markdown du programme de l'organisme en une page HTML autonome (aucune ressource externe).

Usage : python3 -I md_vers_html.py SOURCE.md SORTIE.html "TITRE"
Gère : titres (# à ####), règles (---), paragraphes, listes à puces et numérotées (lignes de suite indentées),
tableaux à barres, **gras**, *italique*, `code`. Refuse d'écraser une sortie existante.
"""
import html
import pathlib
import re
import sys

CSS = """
:root { --encre: #1d2329; --doux: #56636f; --filet: #c9d1d8; --fond-tete: #eef2f5; --accent: #1f4e79; --fond: #ffffff; }
html { background: var(--fond); }
body { font-family: Carlito, "Liberation Sans", "DejaVu Sans", sans-serif; color: var(--encre); background: var(--fond);
       font-size: 10.5pt; line-height: 1.42; max-width: 1100px; margin: 0 auto; padding: 18px 16px 40px; }
h1 { font-size: 19pt; color: var(--accent); margin: 0 0 10px; line-height: 1.2; }
h2 { font-size: 14pt; color: var(--accent); margin: 22px 0 8px; border-bottom: 1.5px solid var(--filet); padding-bottom: 3px;
     break-after: avoid; page-break-after: avoid; }
h3 { font-size: 12pt; margin: 16px 0 6px; break-after: avoid; page-break-after: avoid; }
h4 { font-size: 11pt; margin: 12px 0 4px; }
p { margin: 6px 0; }
ul, ol { margin: 6px 0 6px 22px; padding: 0; }
li { margin: 3px 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; background: #f3f5f7; padding: 0 2px; border-radius: 2px;
       overflow-wrap: anywhere; }
hr { border: 0; border-top: 1px solid var(--filet); margin: 18px 0; }
.tableau { overflow-x: auto; margin: 8px 0 10px; }
table { border-collapse: collapse; width: 100%; font-size: 8.9pt; line-height: 1.32; }
th, td { border: 1px solid var(--filet); padding: 4px 5px; vertical-align: top; text-align: left; overflow-wrap: anywhere; }
th { background: var(--fond-tete); font-weight: bold; }
tr { break-inside: avoid; page-break-inside: avoid; }
strong { font-weight: bold; }
table.inventaire { table-layout: fixed; font-size: 8.2pt; }
table.inventaire th:nth-child(1) { width: 8%; } table.inventaire th:nth-child(2) { width: 40%; }
table.inventaire th:nth-child(3) { width: 10.5%; } table.inventaire th:nth-child(4) { width: 11%; }
table.inventaire th:nth-child(5) { width: 13%; } table.inventaire th:nth-child(6) { width: 10%; }
table.inventaire th:nth-child(7) { width: 7.5%; }
table.inventaire td:nth-child(1), table.inventaire td:nth-child(3), table.inventaire td:nth-child(7),
table.inventaire th { overflow-wrap: normal; word-break: normal; }
table.inventaire td:nth-child(1) { white-space: nowrap; }
@media print { body { max-width: none; padding: 0; } .tableau { overflow: visible; } }
@media (max-width: 640px) { body { font-size: 10pt; } table { font-size: 8.4pt; } }
"""


def en_ligne(texte: str) -> str:
    codes = []

    def jeton(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return f"\x00{len(codes) - 1}\x00"

    t = re.sub(r"`([^`]*)`", jeton, texte)
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], t)


def cellules(ligne: str) -> list:
    l = ligne.strip()
    if l.startswith("|"):
        l = l[1:]
    if l.endswith("|"):
        l = l[:-1]
    # découpe sur les barres hors du code en ligne
    out, cour, dans_code = [], [], False
    for ch in l:
        if ch == "`":
            dans_code = not dans_code
        if ch == "|" and not dans_code:
            out.append("".join(cour).strip())
            cour = []
        else:
            cour.append(ch)
    out.append("".join(cour).strip())
    return out


def convertir(md: str) -> str:
    lignes = md.split("\n")
    i, n, corps = 0, len(lignes), []
    while i < n:
        l = lignes[i]
        if not l.strip():
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", l)
        if m:
            niveau = len(m.group(1))
            corps.append(f"<h{niveau}>{en_ligne(m.group(2).strip())}</h{niveau}>")
            i += 1
            continue
        if l.strip() == "---":
            corps.append("<hr>")
            i += 1
            continue
        if l.lstrip().startswith("|"):
            bloc = []
            while i < n and lignes[i].lstrip().startswith("|"):
                bloc.append(lignes[i])
                i += 1
            tete = cellules(bloc[0])
            reste = bloc[1:]
            if reste and re.match(r"^\s*\|?\s*:?-{3,}", reste[0]):
                reste = reste[1:]
            classe = " class=\"inventaire\"" if tete and tete[0] == "n°" else ""
            h = [f"<div class=\"tableau\"><table{classe}><thead><tr>"]
            h += [f"<th>{en_ligne(c)}</th>" for c in tete]
            h.append("</tr></thead><tbody>")
            for r in reste:
                cs = cellules(r)
                h.append("<tr>" + "".join(f"<td>{en_ligne(c)}</td>" for c in cs) + "</tr>")
            h.append("</tbody></table></div>")
            corps.append("".join(h))
            continue
        m_puce = re.match(r"^(\s*)- (.*)$", l)
        m_num = re.match(r"^(\s*)(\d+)\. (.*)$", l)
        if m_puce or m_num:
            numerote = bool(m_num) and not m_puce
            balise = "ol" if numerote else "ul"
            elements = []
            while i < n:
                l2 = lignes[i]
                a = re.match(r"^(\s*)- (.*)$", l2) if not numerote else re.match(r"^(\s*)\d+\. (.*)$", l2)
                if a:
                    texte = a.group(2)
                    elements.append([texte])
                    i += 1
                    continue
                if l2.strip() and l2.startswith((" ", "\t")) and elements:
                    elements[-1].append(l2.strip())
                    i += 1
                    continue
                break
            corps.append(f"<{balise}>" + "".join("<li>" + en_ligne(" ".join(e)) + "</li>" for e in elements) + f"</{balise}>")
            continue
        para = [l.strip()]
        i += 1
        while i < n and lignes[i].strip() and not re.match(r"^(#{1,4}\s|\s*- |\s*\d+\. |\s*\||---\s*$)", lignes[i]):
            para.append(lignes[i].strip())
            i += 1
        corps.append("<p>" + en_ligne(" ".join(para)) + "</p>")
    return "\n".join(corps)


def main() -> int:
    source, sortie, titre = sys.argv[1:4]
    md = pathlib.Path(source).read_text(encoding="utf-8")
    out = pathlib.Path(sortie)
    if out.exists():
        print(f"refus : {out} existe déjà (R12)")
        return 2
    page = ("<!doctype html>\n<html lang=\"fr\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{html.escape(titre)}</title><style>{CSS}</style></head><body>\n"
            + convertir(md) + "\n</body></html>\n")
    out.write_text(page, encoding="utf-8")
    print(f"écrit {out} ({len(page)} caractères)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
