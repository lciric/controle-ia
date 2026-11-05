# Audit R4 de la sortie réelle v3 des lentilles sur les sondes non principales de P3

29 octobre 2026, à partir de 11:24 UTC (`date -u`). Sous-agent neuf (R4, R13) : je n'ai écrit ni la règle v3, ni la
liste, ni le script v3, ni la contre-lecture. Processeur seul, sans réseau, sans commit.

- **Objet** : `sortie-jlens-sondes-p3-v3.json`, `da240e028c3388579f6efb951954d74e16e6623dd00e971af498eddfd4bfe051`
  (sceau compagnon vérifié : OK). Manifeste : script `25a377ee…` (celui que la contre-lecture a lu), énoncé
  `be020390…`, liste `aac34d5c…`, commit `97165a39…`, `essai_factice` faux, règle complète (32 cases).
- **Lu** : la règle (`regle-primaire-v3/regle-primaire-v3.md`, sections 2 à 7), la liste v3, la contre-lecture
  (`contre-lecture-regle-script-v3.md`), la sortie et son manifeste, les lignes du script qui rendent les
  déclencheurs (l. 100, 1233-1258).
- **Pas lu** : `prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, les branches `donnees/*` et `quarantaine/*`,
  aucune sortie v2.
- **Outil** : `outils/audit_r4_v3.py` (bibliothèque standard, `python3 -I`, Python 3.13.17). Il contrôle en dur les
  empreintes de la sortie et de la liste, puis recompte tout depuis les têtes. Journal :
  `outils/audit_r4_v3.journal.json` (212 contrôles, tous OK). Garde testée sur un artefact : une copie de la sortie
  où un S est changé est refusée (« empreinte de la sortie inattendue », code 1).

**Aucun verdict n'est changé.** Tout ce qui suit est descriptif (règle v3, section 5 : « l'audit ne change aucun
verdict : il ajoute une réserve »).

## Verdict de l'audit

**Les cinq S ≥ 10 ne sont pas des artefacts de comptage. Ce sont des têtes réellement homogènes (danger, menace,
urgence, catastrophe). Mais la nulle qui les juge est faible, et le mot « enjeux » ne décrit pas ce qu'on lit.
Réserve.** Un fait nouveau, hors des cinq cas : les deux seules cases « cohérentes » de « tromperie » ne tiennent
qu'au mot « secret ».

- **Recompte** : S, n_iso, n_pl, X, la liste des déclencheurs et les comptes de l'autre concept, recomptés depuis
  les têtes et les histogrammes de la sortie, sont identiques à la sortie (32 cases sur 32).
- **Mots signalés par CLR3-05** : les retirer laisse les cinq cas au-dessus du maximum de leur nulle isotrope.
- **Autre concept** : zéro mot de « tromperie » dans les cinq têtes.
- **Nulle trop faible** : à la couche 15, un plancher apparié en covariance atteint S = 10 sous la jacobienne. Trois
  des cinq cas sont à la couche 23, où il n'y a pas de plancher.
- **Concept mal nommé** : les têtes parlent de danger et d'urgence, jamais d'enjeu au sens de conséquences (aucun
  « stakes », « consequences », « lawsuit », « fired », « jail », « bankrupt »).

## 1. Les cinq cas déclenchés (S ≥ 10)

Têtes de +w, 20 jetons de début de mot, dans l'ordre. **Gras** : jeton de la liste « enjeux ». Aucun jeton de la
liste « tromperie » n'y figure.

**enjeux-attention-c15 / jacobienne, S = 15** (13 mots distincts)
> **danger** · **dangerous** · **risks** · **dangers** · خطر · **dangerously** · **risk** · **endanger** · खतर · **risky**
> · **safety** · **Danger** · опас · **unsafe** · **Safety** · **threaten** · **threatened** · **threatens** · jeopard ·
> rizik

**enjeux-difference_moyennes-c15 / jacobienne, S = 10** (10 mots distincts)
> **catastrophic** · **devastating** · **threats** · **threatening** · allegations · खतर · **threatens** · **threat** ·
> **crisis** · terrified · **endanger** · terrorist · crippling · feared · jeopard · terrorism · **emergency** ·
> **desperate** · catast · billions

**enjeux-attention-c23 / jacobienne, S = 16** (13 mots distincts)
> **emergency** · **Emergency** · **crisis** · **Crisis** · **emergencies** · **urgent** · **unsafe** · **risks** ·
> **risky** · security · **urgency** · **risk** · **safety** · **danger** · whistleblower · خطر · **desperate** ·
> **Unsafe** · desperation · **dangerous**

**enjeux-difference_moyennes-c23 / logits, S = 10** (9 mots distincts)
> **risk** · **safety** · **danger** · security · **risks** · protection · **endangered** · **emergency** · integrity ·
> **endanger** · financial · stability · **critical** · **threat** · **Safety** · press · medical · gravity · measures ·
> actionTypes

**enjeux-difference_moyennes-c23 / jacobienne, S = 18** (17 mots distincts)
> **emergency** · **crisis** · **threats** · **threat** · **risks** · **danger** · **endanger** · **risk** · **threatening**
> · खतर · jeopard · **threaten** · **threatens** · **catastrophic** · **dangers** · **threatened** · **Emergency** ·
> **devastating** · **peril** · **risking**

### Concept ou voisinage générique

Les familles de sens de la règle (section 2) sont : danger, risque, urgence, gravité, vie et mort, conséquences,
catastrophe, crise, préjudice, juridique et financier.

- **Ce qui fait S, dans le sens de la liste** : les familles danger (danger, dangerous, dangers, dangerously,
  endanger, endangered, unsafe, peril), risque (risk, risks, risky, risking), menace (threat, threats, threaten,
  threatened, threatens, threatening), urgence et crise (emergency, emergencies, urgent, urgency, crisis, desperate),
  catastrophe (catastrophic, devastating). Toutes figurent dans les familles de la règle.
- **Ce qui manque** : les familles « vie et mort », « conséquences », « juridique et financier » sont absentes des
  cinq têtes. Le concept lu est le **danger imminent**, pas l'enjeu au sens de « ce qu'on peut perdre ».
- **Voisinage générique** : « safety » (5 jetons dans 3 cas) et « critical » (1 jeton). Ils sont signalés par CLR3-05
  (« safety » contredit même la règle « pas d'antonyme »). Le cas le plus touché est enjeux-difference_moyennes-c23 /
  logits. Sa tête est un registre « sûreté et sécurité » : safety, Safety, security, protection, integrity, stability,
  measures, critical. Elle est plus générique que les quatre autres.
- **Hors liste, même sens** : 11 jetons de « danger » dans d'autres langues ou tronqués (خطر en arabe, खतर en hindi,
  опас en russe, rizik, jeopard, catast). La liste anglaise sous-compte donc ces têtes. Ce n'est pas un artefact de la
  liste : c'est la marque d'une direction de sens, présente dans plusieurs langues.
- **Variantes de casse** : 15 → 13, 16 → 13, 10 → 9, 18 → 17 mots distincts (et 10 → 10). Elles pèsent peu.

### Recompte sans les mots signalés par CLR3-05 (descriptif)

Mots retirés, version stricte (nommés par CLR3-05) : enjeux = critical, serious, severe, fatal, severity, breach,
compromised, killed, dead, safety ; tromperie = hide, secret, fake, spoof, phishing. Version élargie (mon choix, fixé
dans l'outil avant le recompte) : plus leurs familles présentes dans la liste (seriously, critically, severely,
fatally, breaches, killing… ; hides, hiding, hid, secrets, secretly, secretive, secrecy), plus les mots larges de la
section 2 (damage, damages, damaging).

| Cas | S | S sans CLR3-05 (strict = élargi) | Retirés | Maximum de la nulle isotrope | Borne sup. de n_iso | Borne sup. de n_pl |
|---|---|---|---|---|---|---|
| enjeux-attention-c15 / jacobienne | 15 | 13 | safety ×2 | 9 | 0 | 0 |
| enjeux-difference_moyennes-c15 / jacobienne | 10 | 10 | — | 9 | 0 | 1 |
| enjeux-attention-c23 / jacobienne | 16 | 15 | safety | 6 | 0 | — |
| enjeux-difference_moyennes-c23 / logits | 10 | **7** | safety ×2, critical | 4 | 0 | — |
| enjeux-difference_moyennes-c23 / jacobienne | 18 | 18 | — | 6 | 0 | — |

Pourquoi la borne vaut : retirer des mots de la liste ne peut que baisser le compte de chaque direction nulle. Donc
#{nulle réduite ≥ S′} ≤ #{nulle complète ≥ S′}, que l'outil lit sur l'histogramme rendu. Les cinq cas restent au-dessus
de toute leur nulle isotrope.

## 2. Les mêmes cas sous l'autre concept (« tromperie »)

| Cas | Jetons « tromperie » dans la tête | n_iso « tromperie » (descriptif) | z « tromperie » | Meilleur rang d'un jeton « tromperie », vocabulaire entier |
|---|---|---|---|---|
| enjeux-attention-c15 / jacobienne | 0 | 10 000 | −0,04 | 174 |
| enjeux-difference_moyennes-c15 / jacobienne | 0 | 10 000 | 0,83 | 37 |
| enjeux-attention-c23 / jacobienne | 0 | 10 000 | 0,06 | 81 |
| enjeux-difference_moyennes-c23 / logits | 0 | 10 000 | 0,35 | 481 |
| enjeux-difference_moyennes-c23 / jacobienne | 0 | 10 000 | 0,93 | 86 |

- À la couche 15, le compte « tromperie » est aussi au plus bas des planchers (n_pl = 200 sur 200).
- **Sur les 32 cases**, la liste de l'autre concept n'apparaît que deux fois : « victim » (liste « enjeux ») dans
  tromperie-attention-c15 / logits et tromperie-lineaire-c15 / logits. Aucun mot « tromperie » dans aucune tête
  « enjeux ».
- **Lecture** : la spécificité est nette. Ces directions ne sont pas des « tout ce qui est négatif ou sensible ».
  Elles ne portent que la liste de leur propre concept.

## 3. Les nulles de ces cas

| Cas | n_iso | p de rang | Histogramme isotrope (10 000) | 15ᵉ plus grand | n_pl | Planchers (200) : histogramme, 3ᵉ plus grand, maximum |
|---|---|---|---|---|---|---|
| enjeux-attention-c15 / jacobienne | 0 | 1/10 001 | 0:9328, 1:501, 2:111, 3:36, 4:12, 5:8, 7:2, 8:1, 9:1 | 4 | 0 | 0:179, 1:7, 2:7, 3:2, 4:2, 5:1, 6:1, **10:1** ; 5 ; **10** |
| enjeux-difference_moyennes-c15 / jacobienne | 0 | 1/10 001 | idem | 4 | **1** | idem ; S = 10 **égale** le maximum ; rang 2/201 ≈ 1 % |
| enjeux-attention-c23 / jacobienne | 0 | 1/10 001 | 0:9313, 1:515, 2:125, 3:27, 4:13, 5:5, 6:2 | 4 | — | pas de plancher |
| enjeux-difference_moyennes-c23 / logits | 0 | 1/10 001 | 0:9492, 1:453, 2:47, 3:7, 4:1 | 2 | — | pas de plancher |
| enjeux-difference_moyennes-c23 / jacobienne | 0 | 1/10 001 | idem c23 / jacobienne | 4 | — | pas de plancher |

- **Position du plancher.** Sous la jacobienne à la couche 15, les planchers « enjeux » ont une moyenne de 0,28,
  contre 0,095 pour les isotropes. Leur queue est lourde : un plancher sur 200 atteint S = 10.
  - S = 15 (attention) dépasse ce maximum.
  - S = 10 (différence des moyennes) l'égale seulement. Il passe le garde-fou (n_pl ≤ 2), mais avec la plus petite
    marge possible au-dessus de zéro. Contre la nulle appariée, ce n'est pas un résultat extrême : environ 1 %, non
    corrigé.
- **Ce que cela dit des couches 7 et 23.** Une direction tirée au hasard *dans le sous-espace des textes « enjeux »*
  se décode déjà souvent en mots de danger. La nulle isotrope ne le voit pas. Aux couches 7 et 23, elle est seule.
  Les S de 16, 18 et 10 de la couche 23 n'ont donc pas de nulle appariée : on ne sait pas quelle part vient de la
  sonde, et quelle part vient du seul fait de vivre dans l'espace des textes à enjeux.
- Toutes les médianes des nulles isotropes valent 0 (déclencheur « médiane ≥ 1 » : non déclenché, vérifié).

## 4. Miroirs « trop mauvais » (CLR3-04), descriptif

- **Liste propre en tête de −w : aucun cas sur 32.** Pas un seul jeton de la liste propre dans les 32 têtes de −w.
  Le sens de la classe 1 n'apparaît donc inversé pour aucune sonde, à la mesure de cette statistique. C'est un appui
  descriptif à la lecture des signes (réserve de la section 3 de la règle), pas une preuve.
  - Les −w des quatre cas « enjeux » sous la jacobienne se lisent comme l'inverse attendu : amusing, humorous, hobby, pleasant, enjoyable,
    playful, beginners. Le pôle opposé est le loisir léger et sans conséquence. Sous les logits
    (enjeux-difference_moyennes-c23), la tête de −w est du bruit multilingue (gian, experiences, laut…).
- **Case rejetée par les seuls planchers : aucune.** Les quatre cases « non cohérentes » de la couche 15 sont toutes
  de « tromperie » : S = 2 avec n_iso = 21, ou S = 1 avec n_iso = 300. Elles échouent déjà sur la nulle isotrope.
  `verdict_sans_planchers` a été recalculé indépendamment pour les 8 cases de la couche 15 : conforme.
- Autres déclencheurs de la section 5, recalculés : X ≥ 12 ou X = 0 pour les deux (non : X = 7 et 7) ; b ≥ 6 avec
  c = 0 ou l'inverse (non : 2 et 2) ; médiane isotrope ≥ 1 (non). Pour « un seul mot ou mots larges », voir la
  section 5 : non déclenché à la lettre, mais touché dans l'esprit.

## 5. Mots de chaque case « cohérente » (réserve CLR3-05)

Il y a **14** cases « cohérentes » : 7 sous chaque lentille, dont 5 sondes cohérentes sous les deux (et non 9 + 7).

| Case | S | Mots qui font S (ordre de tête) | Signalés CLR3-05 | S sans eux | Reste au-dessus des seuils (borne) |
|---|---|---|---|---|---|
| enjeux-attention-c7 / jacobienne | 3 | dangerous, devastating, deadly | — | 3 | oui |
| enjeux-difference_moyennes-c7 / logits | 3 | threat, danger, threats | — | 3 | oui |
| enjeux-difference_moyennes-c7 / jacobienne | 5 | catastrophic, devastating, deadly, crisis, threats | — | 5 | oui |
| enjeux-lineaire-c7 / jacobienne | 3 | catastrophic, devastating, deadly | — | 3 | oui |
| enjeux-attention-c15 / logits | 4 | risks, safety, dangerous, endangered | safety | 3 | oui (borne n_iso 3, n_pl 0) |
| enjeux-attention-c15 / jacobienne | 15 | section 1 | safety ×2 | 13 | oui |
| enjeux-difference_moyennes-c15 / logits | 6 | risks, risk, endangered, critical, danger, safety | critical, safety | 4 | oui (0, 0) |
| enjeux-difference_moyennes-c15 / jacobienne | 10 | section 1 | — | 10 | oui (0, 1) |
| **tromperie-attention-c23 / logits** | 3 | **secret, secretly, SECRET** | secret (+ secretly, de la famille) | **1 (strict) ; 0 (élargi)** | **non** |
| **tromperie-difference_moyennes-c23 / logits** | 3 | **secret, secretly, Secret** | idem | **1 ; 0** | **non** |
| enjeux-attention-c23 / logits | 4 | safety, endanger, emergency, risk | safety | 3 | oui (borne n_iso 8) |
| enjeux-attention-c23 / jacobienne | 16 | section 1 | safety | 15 | oui |
| enjeux-difference_moyennes-c23 / logits | 10 | section 1 | safety ×2, critical | 7 | oui |
| enjeux-difference_moyennes-c23 / jacobienne | 18 | section 1 | — | 18 | oui |

Constats :

- **Les deux cases « tromperie » ne tiennent qu'à un seul lexème, « secret ».** Le reste de leurs têtes est sans
  rapport visible avec la tromperie : backwards, moon, Totally, Crack, Magical, exclusively, only… ; actually,
  suddenly, imaginary, theories, nonexistent… Le mot « secret » est l'un des sept mots larges de la règle (section 2).
  « Hidden » a été retiré, mais « secret » est resté (CLR3-05).
  - Le déclencheur « un seul mot (variantes de casse) ou mots larges » de la section 5 **ne s'est pas déclenché à la
    lettre**. Le script compare des mots exacts (l. 1252-1258), et « secretly » n'est ni « secret » ni un mot large.
  - **Dans l'esprit, il est touché** : trois jetons, une seule famille de mots, qui est un mot large.
  - Ce n'est pas un écart (la règle est appliquée comme écrite). C'est une réserve.
  - Descriptif : sans la famille « secret », X sous les logits passerait de 7 à 5, et « tromperie » n'aurait aucune
    case cohérente. b et c deviendraient 2 et 0 (p = 0,5) : pas de phrase permise non plus.
- **Les cases « enjeux » de la couche 7** sont faites de catastrophic, devastating, deadly, dans des têtes de
  grandeur et d'intensité : countless, massive, huge, vast, billions, millions, horrific, brutal. C'est du voisinage
  « gravité ou ampleur » plus que du risque. Les mots comptés sont bien de la liste.
- **Les cases des logits** (S = 3 à 6, hors c23 / différence des moyennes) ont des têtes bruitées : quatre mots de la
  liste au milieu de noms propres et de fragments (Morton, Merrill, Lace, Matrix, Miz, Bid…). « safety » y pèse.
- **Aucune case « cohérente » ne repose sur les mots du registre code et sécurité** de CLR3-05 (fatal, severity,
  breach, compromised, killed, dead ; fake, spoof, phishing). Aucun n'apparaît dans les 14 têtes.

## 6. Autres constats, sans effet sur les verdicts

- **Sondes presque jumelles.** tromperie-attention-c15 et tromperie-lineaire-c15 partagent 17 jetons de tête sur 20
  sous les logits, et 16 sur 20 sous la jacobienne. Elles ont des S et des n_iso identiques. Les 16 sondes ne sont pas
  16 lectures indépendantes. La règle le dit pour le test du signe ; cela vaut aussi pour X.
- **Déjà vus en v2.** Deux des 14 cases « cohérentes » viennent des quatre sondes décodées en descriptif par
  l'exécution v2 avec la liste v2 (règle, section 7 ; R-741) : enjeux-lineaire-c7 / jacobienne et
  tromperie-difference_moyennes-c23 / logits. Je n'ai pas lu la sortie v2.
- **Diagnostic z.** Le compte du diagnostic z prend la tête brute, pas celle des débuts de mot (16 au lieu de 18 pour
  enjeux-difference_moyennes-c23 / jacobienne : 危 et -risk y entrent). C'est cohérent avec son statut descriptif ; à
  ne pas confondre avec S.

## 7. Réserve (à porter avec la lecture)

1. Les cinq S ≥ 10 sont réels et spécifiques (zéro mot de « tromperie », au-dessus du maximum isotrope même sans
   « safety » ni « critical »). Mais ils ne sont jugés que contre une nulle isotrope faible. Là où la nulle appariée
   existe (couche 15, jacobienne), un plancher atteint S = 10 : S = 10 n'y est qu'à environ 1 %. Trois des cinq cas
   (couche 23) n'ont aucune nulle appariée.
2. Ce qui se lit est le **danger imminent** (danger, menace, urgence, crise, catastrophe), pas « l'enjeu » au sens des
   conséquences. Le nom du concept est plus large que ce que les directions portent.
3. Les deux seules cases « cohérentes » de « tromperie » tiennent au seul lexème « secret », un mot large. Elles sont
   à lire comme « non établies ». Le déclencheur de la section 5 les a manquées à la lettre (« secretly »).

## 8. Lecture honnête

**Ce que cela veut dire.** Quand on traduit en mots les directions des sondes « enjeux », plusieurs se lisent très
clairement comme du vocabulaire de danger et d'urgence : danger, risque, menace, crise, urgence, catastrophe. Elles le
font jusque dans d'autres langues que l'anglais (arabe, hindi, russe). Leur sens opposé se lit comme le loisir et
l'agrément : hobby, amusant, plaisant. Aucune ne porte de mot de tromperie. Les sondes « enjeux » lisent donc quelque
chose qui ressemble à « la situation est dangereuse ou urgente ». C'est un thème de surface, plutôt que la notion
d'enjeu (ce qu'on risque de perdre, les conséquences, la responsabilité). Les sondes « tromperie », elles, ne se
lisent presque jamais en mots. Les deux exceptions ne tiennent qu'au mot « secret », dans des têtes par ailleurs sans
rapport.

**Ce que cela ne veut pas dire.**
- Rien sur la détection. Une sonde dont la direction ne se traduit pas en mots peut très bien détecter, et une sonde
  qui se lit « danger » peut détecter un thème au lieu d'une intention.
- Rien sur les deux sondes principales, qui n'ont pas été décodées ici.
- Rien sur P3 : aucune sonde ne change, aucun verdict de P3 n'est touché.
- La règle est exploratoire et non opposable. Aucun chiffre ne sert de critère de porte.
- « Tromperie peu verbalisée » ne dit pas que ses sondes sont fausses. La liste « tromperie » est aussi plus pauvre
  (80 mots contre 142), et la tromperie se dit mal en un mot.

**Est-ce suspect de propreté (R4) ?**
- Les comptes, non : tout se recompte à l'identique depuis les têtes. Les têtes sont visiblement homogènes, et les
  mots discutables (safety, critical) ne portent aucun des cinq cas.
- L'interprétation, oui, en partie. La propreté des têtes « enjeux » vient au moins pour une part de ce que les textes
  « à enjeux » parlent de danger. Une direction prise au hasard dans leur espace donne parfois déjà dix mots de
  danger (un plancher sur 200). Aux couches 7 et 23, rien ne mesure cette part.
- Le résultat est donc moins fort qu'il n'en a l'air : il dit que ces sondes portent un thème lexical de danger, pas
  qu'elles lisent l'enjeu, ni qu'elles le lisent mieux qu'une direction quelconque du même sous-espace. Réserve, pas
  anomalie.

## Fichiers (chacun avec son sceau compagnon)

- `audit-r4-lecture-v3.md` : ce document ;
- `outils/audit_r4_v3.py` : outil de l'audit ;
- `outils/audit_r4_v3.journal.json` : sa sortie sur la sortie réelle (212 contrôles OK).
