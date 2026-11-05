"""Checker of the form of one counter-verification verdict (T0.5, extraction procedure v1).

Usage: python3 -I verifier_avis.py FOLDER
FOLDER holds a-verifier/{h9,h10,cibles}.json (the answers checked) and avis.json (the verdict).
Standard library only. Same checks and same error codes as controle_ia.environnements.extraction.anomalies_avis; a
test of the repository compares the lists of codes of both. It checks form and consistency only, never the
judgement itself.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ESCAPE = re.compile(r"\\([!-/:-@\[-`{-~])")
CONTROL = re.compile(r"[\x00-\x09\x0b-\x1f]")
SURROGATE = re.compile(r"[\ud800-\udfff]")
DOLLAR = re.compile(r"(?<!\\)\$\$?")
BLANK_LINE = re.compile(r"\n[ \t]*\n")
BREAK_LOWER = re.compile(r"\n[a-z]")
PAPER_TYPES = {"theory_only", "mostly_theory", "mostly_experiments", "experiments_only"}
DATA_TYPES = {"synthetic_only", "mostly_synthetic", "mostly_real", "real_only", "not_applicable"}
FAMILIES = ("controls", "fruitful_directions", "sterile_directions")
FIELDS = {"statement_leaks": bool, "leak_passages": list, "theory_experiment_correct": bool,
          "theory_experiment_expected": str, "data_type_correct": bool, "data_type_expected": str,
          "domains_reasonable": bool, "targets": list, "compute_plausible": bool, "comment": str}
TYPO = {**{ord(a): b for a, b in zip("\u2018\u2019\u201c\u201d\u2013\u2014\u2010\u2011\u2012\u2212\u00a0",
                                     "''\"\"------- ")}, 0x00AD: None}
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


def check_verdict(v, h9, h10, targets):
    if not isinstance(v, dict):
        return ["[avis.objet] avis.json: a JSON object is expected"]
    e = []
    if set(v) != set(FIELDS):
        e.append(f"[avis.champs] avis.json: missing fields {sorted(set(FIELDS) - set(v))}, extra fields "
                 f"{sorted(set(v) - set(FIELDS))}")
    for k, t in FIELDS.items():
        if k in v and not isinstance(v[k], t):
            e.append(f"[avis.type] avis.json: {k} is a {type(v[k]).__name__}, a {t.__name__} is expected")
    if e:
        return e
    h10 = {key(k): x for k, x in h10.items()} if isinstance(h10, dict) else {}
    for k, values, actual in (("theory_experiment", PAPER_TYPES, h10.get("theory_experiment")),
                              ("data_type", DATA_TYPES, h10.get("data_type"))):
        expected = key(v[f"{k}_expected"])
        if expected not in values:
            e.append(f"[avis.valeur] avis.json: {k}_expected is not one of H10's values ({expected!r})")
        elif v[f"{k}_correct"] != (expected == key(actual)):
            e.append(f"[avis.coherence] avis.json: {k}_correct does not agree with {k}_expected and h10.json")
    ids = [t.get("id") if isinstance(t, dict) else None for t in v["targets"]]
    wanted = [it["id"] for f in FAMILIES for it in targets[f]]
    if ids != wanted:
        e.append(f"[avis.cibles] avis.json: targets {ids} differ from the targets of cibles.json {wanted} "
                 "(same ids, same order)")
    for t in v["targets"]:
        if not (isinstance(t, dict) and isinstance(t.get("grounded"), bool) and isinstance(t.get("observable"), bool)):
            e.append(f"[avis.cible] avis.json: target {str(t)[:60]} needs boolean grounded and observable")
    if v["statement_leaks"] != bool(v["leak_passages"]):
        e.append("[avis.fuite] avis.json: statement_leaks does not agree with leak_passages "
                 "(true if and only if not empty)")
    statement = normalize(str(h9.get("research_questions", "")))
    for p in v["leak_passages"]:
        if not isinstance(p, str) or not normalize(p) or normalize(p) not in statement:
            e.append(f"[avis.passage] avis.json: passage not found in the statement: {str(p)[:60]!r}")
    return e + check_text(v, "avis.json")


def main(folder):
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    folder = Path(folder)
    try:
        h9, h10, targets = (json.loads((folder / "a-verifier" / f"{n}.json").read_text(encoding="utf-8"))
                            for n in ("h9", "h10", "cibles"))
    except (OSError, ValueError) as exc:
        print(f"NOT OK: the answers to check cannot be read ({exc})")
        return 2
    path = folder / "avis.json"
    if not path.is_file():
        errors = ["[fichier.absent] avis.json is missing"]
    else:
        try:
            v = json.loads(path.read_bytes().decode("utf-8"), parse_constant=reject_constant)
            errors = check_verdict(v, h9, h10, targets)
        except ValueError as exc:
            errors = [f"[json.illisible] avis.json is not valid JSON: {exc}"]
    for m in errors:
        print("ERROR:", m)
    print(f"{'OK' if not errors else 'NOT OK'}: {len(errors)} error(s)")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
