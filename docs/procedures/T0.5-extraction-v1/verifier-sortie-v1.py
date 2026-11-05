"""Checker of the extraction outputs of one paper (T0.5, extraction procedure v1).

Usage: python3 -I verifier_sortie.py FOLDER
FOLDER holds papier/partie-*.md (the paper) and sorties/{h9,h10,cibles}.json (the answers).
Standard library only. Same checks and same error codes as controle_ia.environnements.extraction (anomalies_h9,
anomalies_h10, anomalies_cibles, anomalies_texte, anomalies_fuite: errors; alertes_h9: warnings); a test of the
repository compares the lists of codes of both on sound cases and on artefacts.
"""
import json
import math
import re
import sys
import unicodedata
from pathlib import Path

FIGURE = re.compile(r"\[FIGURE\s*\d*\]|\bFig(?:ure|\.)\s*\d+|\bTable\s*\d+", re.I)
ESCAPE = re.compile(r"\\([!-/:-@\[-`{-~])")
CUES = re.compile(
    r"\bwe\s+(?:propose|present|introduce|develop|design|show|find|demonstrate|evaluate|conduct|train)\b"
    r"|\bour\s+(?:method|approach|framework|model|algorithm|results?|experiments?|contributions?|findings?"
    r"|analysis|solution)\b"
    r"|\b(?:in\s+)?this\s+(?:paper|work)\b", re.I)
CONTROL = re.compile(r"[\x00-\x09\x0b-\x1f]")
SURROGATE = re.compile(r"[\ud800-\udfff]")
DOLLAR = re.compile(r"(?<!\\)\$\$?")
BLANK_LINE = re.compile(r"\n[ \t]*\n")
BREAK_LOWER = re.compile(r"\n[a-z]")
PAPER_TYPES = ["theory_only", "mostly_theory", "mostly_experiments", "experiments_only"]
DATA_TYPES = {"synthetic_only", "mostly_synthetic", "mostly_real", "real_only", "not_applicable"}
BOUNDS = {"controls": (3, 6), "fruitful_directions": (1, 3), "sterile_directions": (0, 3)}
TYPO = {**{ord(a): b for a, b in zip("\u2018\u2019\u201c\u201d\u2013\u2014\u2010\u2011\u2012\u2212\u00a0",
                                     "''\"\"------- ")}, 0x00AD: None}
LEAK_WORDS = 8
BACKSLASH = "a LaTeX backslash must be written \\\\ inside a JSON string (\\t, \\b, \\f, \\r, \\n are escapes)"


def normalize(text):
    t = unicodedata.normalize("NFKC", text).translate(TYPO)
    t = ESCAPE.sub(r"\1", t).replace("*", "")
    return re.sub(r"\s+", " ", t).strip().lower()


def key(value):
    return str(value).replace("\\_", "_").strip()


def reject_constant(name):
    raise ValueError(f"non-standard JSON constant: {name}")


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings(k)
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def excerpt(s, i, radius=30):
    return repr(s[max(0, i - radius):i + radius])


def broken_formula(s):
    """Position of a line break that comes from an undoubled backslash, or None: a line break followed by "abla"
    (\\nabla), anywhere; or, between two unescaped $ (or $$) delimiters paired in order with no blank line between
    them, a line break followed by a lowercase letter (\\nu, \\neq, \\not...). A segment that spans a blank line
    joins two amounts in two paragraphs, not a formula."""
    i = s.find("\nabla")
    if i >= 0:
        return i
    delims = list(DOLLAR.finditer(s))
    for opening, closing in zip(delims[0::2], delims[1::2]):
        segment = s[opening.end():closing.start()]
        if BLANK_LINE.search(segment):
            continue
        m = BREAK_LOWER.search(segment)
        if m:
            return opening.end() + m.start()
    return None


def check_text(obj, name):
    e = []
    for s in strings(obj):
        m = CONTROL.search(s)
        if m:
            e.append(f"[texte.controle] {name}: control character near {excerpt(s, m.start())}; {BACKSLASH}; "
                     "a tab copied from the paper can be replaced by a space")
            break
    for s in strings(obj):
        i = broken_formula(s)
        if i is not None:
            e.append(f"[texte.formule] {name}: line break inside a formula near {excerpt(s, i)}; {BACKSLASH}; "
                     "if the $ signs are amounts, not a formula, write the amounts without $; if the paper itself "
                     "has a line break at this place (a formula split over two lines), replace this line break with "
                     "a space")
            break
    for s in strings(obj):
        m = SURROGATE.search(s)
        if m:
            e.append(f"[texte.substitut] {name}: lone surrogate character near {excerpt(s, m.start())} "
                     "(an escaped \\uD8xx without its pair)")
            break
    return e


def positive_number(h):
    if isinstance(h, bool) or not isinstance(h, (int, float)):
        return False
    try:
        f = float(h)
    except OverflowError:
        return False
    return math.isfinite(f) and f > 0


def check_h9(out):
    if not isinstance(out, dict):
        return ["[h9.objet] h9.json: a JSON object is expected"]
    e = []
    rq = out.get("research_questions")
    if not isinstance(rq, str) or len(rq.strip()) < 200:
        e.append("[h9.enonce_court] h9.json: research_questions is missing or too short (under 200 characters)")
    elif FIGURE.search(rq):
        e.append(f"[h9.figure] h9.json: research_questions refers to a figure or a table: "
                 f"{FIGURE.search(rq).group(0)!r}")
    if not isinstance(out.get("affiliations"), list):
        e.append("[h9.affiliations] h9.json: affiliations must be a list")
    costs = out.get("costs")
    if not isinstance(costs, dict) or "total" not in costs or not isinstance(costs.get("splits", []), list):
        e.append("[h9.couts] h9.json: costs must be an object {total, splits}")
    return e + check_text(out, "h9.json")


def check_h10(out):
    if not isinstance(out, dict):
        return ["[h10.objet] h10.json: a JSON object is expected"]
    s, e = {key(k): v for k, v in out.items()}, []
    if key(s.get("theory_experiment", "")) not in PAPER_TYPES:
        e.append(f"[h10.type_papier] h10.json: unexpected theory_experiment value: {s.get('theory_experiment')!r}")
    if key(s.get("data_type", "")) not in DATA_TYPES:
        e.append(f"[h10.type_donnees] h10.json: unexpected data_type value: {s.get('data_type')!r}")
    if not isinstance(s.get("domains", None), list):
        e.append("[h10.domaines] h10.json: domains must be a list")
    return e + check_text(out, "h10.json")


def check_targets(out, paper):
    if not isinstance(out, dict):
        return ["[cibles.objet] cibles.json: a JSON object is expected"]
    e, ids = [], set()
    body = normalize(paper)
    for family, (lo, hi) in BOUNDS.items():
        items = out.get(family)
        if not isinstance(items, list) or not lo <= len(items) <= hi:
            n = len(items) if isinstance(items, list) else "no list"
            msg = f"[cibles.bornes] cibles.json: {family} must have between {lo} and {hi} items (found: {n})"
            if isinstance(items, list) and len(items) < lo:
                msg += "; add items only if the paper truly supports them, never invent one"
            e.append(msg)
            continue
        for it in items:
            if not isinstance(it, dict):
                e.append(f"[cibles.element] cibles.json: {family}: an item is not an object")
                continue
            ident = it.get("id")
            if not isinstance(ident, str) or not ident.strip() or ident in ids:
                e.append(f"[cibles.identifiant] cibles.json: {family}: id missing, not a string, or duplicate "
                         f"({ident!r})")
            else:
                ids.add(ident)
            if len(str(it.get("description", "")).strip()) < 10:
                e.append(f"[cibles.description] cibles.json: {ident!r}: description missing or too short")
            quote = str(it.get("evidence", "")).strip()
            if len(quote) < 20:
                e.append(f"[cibles.citation_courte] cibles.json: {ident}: quote missing or too short "
                         "(under 20 characters)")
            elif normalize(quote) not in body:
                e.append(f"[cibles.citation_introuvable] cibles.json: {ident}: quote not found in the paper")
    compute = out.get("compute")
    if not isinstance(compute, dict) or compute.get("basis") not in ("reported", "estimated"):
        e.append('[cibles.calcul] cibles.json: compute must be an object {reference_gpu_hours, basis, evidence}, '
                 'basis "reported" or "estimated"')
    else:
        h = compute.get("reference_gpu_hours")
        if h is not None and not positive_number(h):
            e.append(f"[cibles.calcul_valeur] cibles.json: compute.reference_gpu_hours must be a positive number "
                     f"or null ({str(h)[:40]})")
    return e + check_text(out, "cibles.json")


def ngrams(text, n):
    words = normalize(text).split()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def check_leak(h9, targets):
    rq = h9.get("research_questions") if isinstance(h9, dict) else None
    items = targets.get("fruitful_directions") if isinstance(targets, dict) else None
    if not isinstance(rq, str) or not isinstance(items, list):
        return []
    statement, e = ngrams(rq, LEAK_WORDS), []
    for it in items:
        if isinstance(it, dict) and ngrams(str(it.get("evidence", "")), LEAK_WORDS) & statement:
            e.append(f"[h9.fuite_citation] the problem statement repeats {LEAK_WORDS} or more consecutive words of the "
                     f"evidence of fruitful direction {it.get('id')!r}: it may reveal the paper's approach; remove what "
                     "reveals the approach from the statement (prompt H9); edit the statement, not the quote")
    return e


def main(folder):
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    folder = Path(folder)
    parts = sorted((folder / "papier").glob("partie-*.md"))
    if not parts:
        print("NOT OK: the paper is missing")
        return 2
    paper = "".join(p.read_text(encoding="utf-8") for p in parts)
    errors, warnings, outs = [], [], {}
    for name in ("h9", "h10", "cibles"):
        path = folder / "sorties" / f"{name}.json"
        if not path.is_file():
            errors.append(f"[fichier.absent] {name}.json is missing")
            continue
        try:
            outs[name] = json.loads(path.read_bytes().decode("utf-8"), parse_constant=reject_constant)
        except ValueError as exc:
            errors.append(f"[json.illisible] {name}.json is not valid JSON: {exc}")
    if "h9" in outs:
        errors += check_h9(outs["h9"])
        rq = outs["h9"].get("research_questions") if isinstance(outs["h9"], dict) else None
        if isinstance(rq, str):
            for cue in sorted({" ".join(m.group(0).lower().split()) for m in CUES.finditer(rq)}):
                warnings.append(f"h9.json: the statement contains {cue!r}; prompt H9 forbids revealing the method, "
                                "the experimental setup, the results or the contributions: edit only if it does")
    if "h10" in outs:
        errors += check_h10(outs["h10"])
    if "cibles" in outs:
        errors += check_targets(outs["cibles"], paper)
    if "h9" in outs and "cibles" in outs:
        errors += check_leak(outs["h9"], outs["cibles"])
    for m in errors:
        print("ERROR:", m)
    for m in warnings:
        print("WARNING:", m)
    print(f"{'OK' if not errors else 'NOT OK'}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
