import ast, sys, pathlib
racine = pathlib.Path(sys.argv[1]); pole = racine / "orchestrator" / "pole"
depart = sys.argv[2:]
vus, a_voir = set(), list(depart)
while a_voir:
    nom = a_voir.pop()
    if nom in vus: continue
    f = pole / nom
    if not f.is_file(): print("ABSENT", nom); continue
    vus.add(nom)
    arbre = ast.parse(f.read_text(encoding="utf-8"))
    for n in ast.walk(arbre):
        mods = []
        if isinstance(n, ast.ImportFrom):
            if n.level >= 1 and n.module: mods.append(n.module.split(".")[0])
            elif n.level >= 1 and not n.module: mods += [a.name for a in n.names]
            elif n.module and n.module.startswith("pole."): mods.append(n.module.split(".")[1])
            elif n.module == "pole": mods += [a.name for a in n.names]
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name.startswith("pole."): mods.append(a.name.split(".")[1])
        for m in mods:
            if (pole / f"{m}.py").is_file() and f"{m}.py" not in vus: a_voir.append(f"{m}.py")
print("FERMETURE", len(vus)); print(" ".join(sorted(vus)))
