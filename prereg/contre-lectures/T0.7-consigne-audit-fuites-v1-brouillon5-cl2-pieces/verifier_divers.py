import hashlib,re,subprocess
h=lambda s:hashlib.sha256(s.encode()).hexdigest()
B5=open("brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md",encoding="utf-8").read()
B21=open("brouillons/T0.7-sondes-v0-v1-brouillon21.md",encoding="utf-8").read().split("\n")
c2=re.split(r"(?<!\\) \| ",B21[2086][2:-2])[1]
A=[("une **différence de construction** entre les deux conditions d'un jeu décisif, fixée par la chaîne de T0.6 (consignes, gabarit de l'environnement, découpage des jetons notés, format des champs) et **non produite par l'action de l'organisme**",
    "une **différence entre les deux conditions** d'un jeu décisif dans la présence d'un **élément de construction** fixé par la chaîne de T0.6 (consignes, gabarit de l'environnement, découpage des jetons notés, format des champs), dont la source est **propre à une condition ou commune aux deux** et dont la **reproduction par l'organisme ne l'exclut pas** (lecture (a), R-2203 ; le fichier d'audit dit si la source est propre ou commune ; un contenu d'action sans source de construction citée relève de l'exclusion (b))"),
   ("(`aire_simple` rend `null` : pas une fuite)","(son aire vaut 0,5 : pas une fuite ; `aire_simple` ne rend `null` que si l'une des deux conditions n'a aucune action notée, et le jeu n'est alors pas auditable)"),
   ("(l. 133-140 au commit `7a54d431…`","(l. 133-144 au commit `7a54d431…`"),
   ("`empan` (premier ou dernier jeton noté, jeton de fin, fixés par le découpage)","`empan` (premier ou dernier jeton noté, jeton de fin, fixés par le découpage ; le jeton de fin, que le découpage retire des jetons notés, n'est pas lu par la sonde, et une fuite qui le cite le dit)")]
t=c2
for a,n in A: print("ancien présent:",t.count(a)); t=t.replace(a,n)
print("couples A-D du journal → cellule:",h(t))
# annexe A
I=open("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md",encoding="utf-8").read()
print("annexe A : interdits v2 présents en entier dans b5 :",B5.count(I.rstrip("\n")))
for s in ["Aucun autre chemin n'est écrit.","le commit cité par la ligne `CODE-T07` si elle existe, sinon `8ae9fc44`","`CODE-T07` (si\n   présente)","(même contrôle que le module, T0.7 l. 2078)","T0.7 l. 2046","(garde d'ordre, l. 2047-2050)","(étape A, l. 1385-1390)","7. T0.7 : les seules lignes recopiées au § 2,","8. Le découpeur du modèle de 7b, au chemin donné par la mère (`CHEMIN_DECOUPEUR`, § 6.1), et rien d'autre de ce dossier.","empreinte du découpeur fausse → arrêt ;","cellules du § 2 égales au texte de T0.7 en vigueur","Cellules du § 2 différentes au texte de T0.7 en vigueur"]:
    print(B5.count(s),"|",s[:90].replace("\n","⏎"))
for m in re.finditer(r"T0\.7 l\. 2046",B5): print(repr(B5[m.start()-60:m.end()+40]))
