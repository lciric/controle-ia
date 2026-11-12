"""Ordre de 7b, brouillon 6 : brouillon 5 (`876f85e8…`) + couples CL5-1 à CL5-6 de sa contre-lecture
(`docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon5-contre-lecture-v1.md`, `6bab9753…`), tels qu'écrits,
sauf CL5-2 (troisième couple) complété du chemin entier et de l'empreinte de la contre-lecture (R-2327). Rien d'autre."""
import hashlib, re, sys
from pathlib import Path
R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
B5 = R / "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon5.md"
B6 = R / "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon6.md"
CL = R / "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon5-contre-lecture-v1.md"
assert hashlib.sha256(B5.read_bytes()).hexdigest().startswith("876f85e8"), "brouillon 5 changé"
assert hashlib.sha256(CL.read_bytes()).hexdigest().startswith("6bab9753"), "contre-lecture changée"
C = [
 ('cd "$M" && "$PY" -I -B -c "$G" 2>&1 | tail -n 3;', 'cd "$M" && "$PY" -I -B -u -c "$G" 2>&1 | tail -n 3;'),
 ('**Artefact** (R5), code 1 : mêmes lignes, puis « ', '**Artefact** (R5), code 1 : en dernière des trois lignes affichées, « '),
 ('(refus observé par le rédacteur des brouillons 1 à 3, non rejoué au brouillon 4)',
  '(`-u` : sans lui, la sortie mise en tampon masque ce message ; cas sain et artefact rejoués hors ligne par la contre-lecture du brouillon 5, CL5-1)'),
 ('— v1, brouillon 4', '— v1'),
 ('- **Statut** : brouillon 4, écrit le', '- **Statut** : ordre v1 à sceller ; texte du brouillon 4, écrit le'),
 ("**Non contre-lu dans cette forme** ; avant la remise : marqueurs dans l'ordre du § 14, scellement, commit, remise par Lazar ; contre-lecture du brouillon 4 (au moins du différentiel) si la mère la commande.",
  "Marqueurs de la mère remplis au brouillon 5 (`876f85e8…`, R-2324, R-2325). **Différentiel depuis le brouillon 3 contre-lu** par un lecteur neuf (`docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon5-contre-lecture-v1.md`, `6bab9753fd9bb840e755a95b04c64c0f93b33b657ecf965ee8381953cbdb17c8`, Claude Fable 5.2), ses corrections CL5-1 à CL5-6 appliquées par couples au brouillon 6 (R-2327), CL5-7 portée par le message de remise ; reste avant la remise : `COMMIT_MAIN_REMISE`, scellement, commit, remise par Lazar."),
 ("**parent** du commit qui ajoute cet ordre scellé ; l'ordre lui-même se vérifie par son compagnon et par l'empreinte du message de remise (§ 4.1) ; la mère, au commit de l'engagement (C3)",
  "**ancêtre** du commit qui ajoute cet ordre scellé : la tête de `main` relevée par la mère au moment du scellement (quarante caractères), déjà poussée, descendante du commit de l'engagement ; c'est le parent de ce commit si rien ne s'intercale ; l'ordre lui-même se vérifie par son compagnon et par l'empreinte du message de remise (§ 4.1) ; la mère, au scellement (C3, CL5-3)"),
 ("; non remplissable le 10 novembre (le registre ne porte que les lignes des jeux J-D et J-A)", "; remplie le 11 novembre (R-2321, R-2325)"),
 ("**Remplis au brouillon 4** (registres",
  "**Remplis au brouillon 5** (11 novembre, R-2324, R-2325) : `LIGNE_SCELLEMENT_T07` = la ligne du registre, à l'octet ; `ID_SESSION_FILLE` = valeur de repli (session non ouverte au scellement). **Remplis au brouillon 4** (registres"),
 ("en tête du journal, l'identifiant de la session (égal à celui de l'en-tête quand la mère l'y a écrit)",
  "en tête du journal, l'identifiant de la session, que la fille met à la place du gabarit `<identifiant de la session fille>` avant de jouer le bloc (elle le tient du message de remise de Lazar ou de son outil de session, jamais de `env` ; l'en-tête ne le porte pas : session ouverte après le scellement)"),
 ("- **La fille nommée en en-tête** exécute", "- **La fille désignée en en-tête** (celle à qui Lazar remet l'ordre) exécute"),
 ("(R-2113), au plus tard le 16 à 23:00Z.",
  "(R-2113) ; sans mot le 16 à 23:00Z, la borne joue : destruction, et le compte rendu nomme les données non poussées perdues avec l'instance."),
]
t0 = B5.read_text(encoding="utf-8"); t = t0
for a, n in C:
    assert t.count(a) == 1, ("ancien absent ou multiple", a[:60])
    t = t.replace(a, n)
assert re.findall(r"<<[A-Z0-9_]+>>", t) == ["<<COMMIT_MAIN_REMISE>>"]
assert not B6.exists(), "brouillon 6 existe déjà (R12)"
B6.write_text(t, encoding="utf-8")
u = t
for a, n in reversed(C):
    assert u.count(n) == 1, ("nouveau absent ou multiple", n[:60])
    u = u.replace(n, a)
assert u == t0, "défaire les couples ne redonne pas le brouillon 5"
print("brouillon 6", hashlib.sha256(B6.read_bytes()).hexdigest(), len(C), "couples")
