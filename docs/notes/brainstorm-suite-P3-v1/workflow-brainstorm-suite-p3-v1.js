export const meta = {
  name: 'brainstorm-suite-p3-v1',
  description: "Brainstorm à protocole fermé sur la suite de P3 : propositions à l'aveugle, objections à l'aveugle classées, réponses, note de décision",
  phases: [
    { title: 'Propositions', detail: 'quatre proposeurs neufs, angles distincts, sans se voir' },
    { title: 'Objections', detail: "deux objecteurs neufs, à l'aveugle : fatales, sérieuses, mineures" },
    { title: 'Réponses', detail: 'un tour de réponses aux objections fatales et sérieuses' },
    { title: 'Note', detail: 'note de décision pour Lazar, conditionnée au verdict R13' },
  ],
}

const A = args
const COMMUN = `
Brainstorm demandé par Lazar (directeur du programme) sur la suite de P3, sous SON protocole fermé (décision R-203 (2)) :
pas de dialogue libre entre modèles ; propositions indépendantes ; un tour d'objections à l'aveugle classées fatales,
sérieuses et mineures ; un tour de réponses ; une note de décision. Rien ne change dans le programme sans sa décision.
Français, phrases courtes, quasi aucun acronyme (développe les termes).

Dépôt en LECTURE SEULE : ${A.repo} (aucune écriture, aucune commande git qui écrive, aucune commande Vast.ai, aucun service
payant, aucun contact externe). Tu écris seulement dans ${A.dossier}/ (le sous-dossier qu'on te donne). Ne lis jamais
prereg/P3-consignes-v1.md, ni les textes d'action (donnees/*/textes-actions-*.jsonl), ni aucune clé ou jeton.

Ce qu'on sait (2026-10-20, 08:00 UTC) :
- P3 : premier test boîte blanche sur l'organisme (i-a) (saboteur qui gonfle les coûts déclarés). Préenregistrement scellé
  ${A.repo}/prereg/P3-premier-test-i-a-v1.md (table d'issue gelée, critères de lecture, audit de symétrie). Run
  ${A.run} (2 400 actions, 430 sondes figées, deux sondes principales) ; conception des sondes : décisions P-011 et P-013
  (docs/decisions/), code src/controle_ia/sondes/.
- Lecture décisive faite (code gelé, ${A.repo}/diag/${A.lecture}/lecture-p3.json) : ligne d'issue mécanique « aucune sonde
  générique au-dessus du plancher sur (i-a) », sans réserve mécanique. Tu peux lire ce fichier en entier (P3-P1 : effet de
  l'organisme ; jeux et planchers ; audit R4 ; intention ; contrôles). ATTENTION : ce n'est pas encore un verdict. Le
  verdict R13 (sous-agents neufs) et l'addendum de lecture complémentaire (préenregistrement scellé
  ${A.repo}/prereg/P3-addendum-lecture-complementaire-v1.md, qui ne peut qu'ajouter des réserves) sont en cours. Toute
  proposition doit donc être conditionnée : (A) négatif confirmé sans réserve ; (B) négatif avec réserves (instrument,
  plancher, fuite) ; (C) instrument jugé en échec.
- Programme : docs/programme-controle-ia-v2.md (hypothèses, expériences, portes), docs/brief-claude-code-programme-complet-v2.md,
  docs/decisions/ (N-003 à N-024, P-007 : plan de la porte G0 au 1er novembre 2026, critères 2 organismes, 3 sondes, 4 base
  boîte noire), brouillons/programme-approfondi-ABC-v1.md (papiers A, B, C), registres/etat.md, registres/decisions.md
  (R-192 : P3 hors ordre ; N-022 : plan B des juges ; R-203 : appel EA Funds le 21 octobre 2026), registres/depenses.md
  (budget : GO-2026-10-04-08, plafond 150 USD ; crédit Vast.ai relu 11,79 USD).
Règles gelées du programme à respecter dans toute proposition : préenregistrement scellé avant toute expérience décisive
(R1) ; aucun run visant un signe positif (R3) ; un résultat négatif trop propre est audité comme un positif (R4) ; jamais de
moyenne ni de médiane sur les jetons d'une action dans une sonde de production ; aucun chiffre de l'état de l'art sans PDF
vérifié (R7) ; zone vierge = question, pas preuve (R8) ; aucune dépense sans GO de Lazar sur devis.
`
const SCHEMA_PROP = {
  type: 'object',
  properties: {
    chemin: { type: 'string' },
    options: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, branche: { type: 'string' }, titre: { type: 'string' }, contenu: { type: 'string' },
      tranche: { type: 'string' }, cout: { type: 'string' }, revendications: { type: 'string' }, piege: { type: 'string' },
    }, required: ['id', 'branche', 'titre', 'contenu', 'tranche', 'cout', 'piege'] } },
  },
  required: ['chemin', 'options'],
}
const SCHEMA_OBJ = {
  type: 'object',
  properties: {
    chemin: { type: 'string' },
    objections: { type: 'array', items: { type: 'object', properties: {
      option: { type: 'string' }, classe: { type: 'string', enum: ['fatale', 'sérieuse', 'mineure'] }, objection: { type: 'string' },
      preuve: { type: 'string' },
    }, required: ['option', 'classe', 'objection', 'preuve'] } },
  },
  required: ['chemin', 'objections'],
}
const SCHEMA_REP = {
  type: 'object',
  properties: { chemin: { type: 'string' }, reponses: { type: 'array', items: { type: 'object', properties: {
    option: { type: 'string' }, objection: { type: 'string' }, reponse: { type: 'string' }, statut: { type: 'string' },
  }, required: ['option', 'objection', 'reponse', 'statut'] } } },
  required: ['chemin', 'reponses'],
}
const SCHEMA_NOTE = {
  type: 'object',
  properties: { chemin: { type: 'string' }, resume: { type: 'string' }, recommandation: { type: 'string' }, noeuds: { type: 'array', items: { type: 'string' } } },
  required: ['chemin', 'resume', 'recommandation', 'noeuds'],
}

const ANGLES = [
  { cle: 'A', texte: "instrument : le négatif dit-il « pas de signal » ou « instrument aveugle » ? Quelles mesures ou expériences, les moins chères, distingueraient les deux (sondes génériques contre sonde entraînée sur un contraste propre à l'organisme, couches, agrégation, plancher trop fort, fuite par le coût écrit, taille d'effet de l'organisme) ? Lis le code des sondes et la lecture en détail." },
  { cle: 'B', texte: "programme et revendications : ce que ce négatif change aux hypothèses, aux revendications (N-013 et suivantes), aux critères de la porte G0 (P-007 : critère 3, sondes), aux papiers A, B et C, et à la présentation à l'appel EA Funds du 21 octobre ; ce qu'on peut affirmer honnêtement, et ce qu'on ne peut plus." },
  { cle: 'C', texte: "expérience suivante : une à trois expériences décisives possibles (P4), chacune avec son préenregistrement en une page (hypothèse, prédiction chiffrée et signe, métrique, seuil, ce qui la falsifie), son coût de calcul (heures de carte, dollars), son délai jusqu'au 1er novembre, et son rang ; inclure au moins une expérience boîte noire de comparaison (base T0.8) et une qui teste l'instrument sur un cas où le signal est connu." },
  { cle: 'D', texte: "avocat du diable : supposer que le négatif est un artefact ou au contraire qu'il est le résultat le plus important du programme ; chercher les explications concurrentes (organisme qui gonfle sans « intention » lisible, sondes génériques mal choisies, plancher qui absorbe le signal, effet trop petit pour la puissance), et ce qui serait une erreur coûteuse dans chaque direction (R4 : symétrie)." },
]

phase('Propositions')
const props = await parallel(ANGLES.map(an => () => agent(`${COMMUN}
Tu es PROPOSEUR ${an.cle} (neuf ; tu ne vois pas les autres proposeurs). Angle : ${an.texte}
Écris ${A.dossier}/propositions/proposition-${an.cle}.md : 3 à 6 options numérotées ${an.cle}1, ${an.cle}2…, chacune avec
la branche du verdict où elle vaut (A, B, C ou toutes), ce qu'elle tranche, son coût (calcul et temps), les revendications
touchées, le piège principal ; appuie chaque affirmation sur un fichier du dépôt (chemin, clé ou ligne). Rends les options.`,
  { label: `proposeur:${an.cle}`, phase: 'Propositions', schema: SCHEMA_PROP })))

const gemini = A.gemini ? `\nProposition externe (Gemini 4 Argon, binôme, à l'aveugle et sans aucun résultat de P3 ; non opposable ; ses renvois de
ligne ont déjà été trouvés faux dans une autre relecture : vérifie tout ce que tu en retiens) : ${A.gemini} (options G).` : ''
const liste = props.filter(Boolean).map(p => p.chemin).join(', ')

phase('Objections')
const objs = await parallel([1, 2].map(k => () => agent(`${COMMUN}
Tu es OBJECTEUR ${k} (neuf ; tu ne vois ni l'autre objecteur ni les réponses). Propositions à examiner : ${liste}.${gemini}
Pour CHAQUE option, écris tes objections, chacune classée fatale (l'option est fausse, dangereuse ou contraire à une règle
gelée), sérieuse (elle doit changer avant d'être retenue) ou mineure ; chaque objection avec sa preuve (fichier, ligne,
calcul). Cherche aussi ce qui manque à l'ensemble : une option absente que tu jugerais nécessaire (objection « manque »,
option « ensemble »). Écris ${A.dossier}/objections/objections-${k}.md. Rends les objections.`,
  { label: `objecteur:${k}`, phase: 'Objections', schema: SCHEMA_OBJ })))

const objsTexte = objs.filter(Boolean).map(o => o.chemin).join(', ')
phase('Réponses')
const reps = await agent(`${COMMUN}
Tu es le RÉPONDANT (neuf ; tu n'as écrit ni les propositions ni les objections). Propositions : ${liste}.${gemini}
Objections : ${objsTexte}. Pour chaque objection fatale ou sérieuse, réponds au nom de l'option : accepter (l'option tombe),
corriger (écris l'option corrigée), ou réfuter (avec la preuve). Les mineures : une ligne chacune au plus. N'invente aucune
option nouvelle, sauf pour combler un « manque » relevé par un objecteur. Écris ${A.dossier}/reponses/reponses.md.`,
  { label: 'repondant', phase: 'Réponses', schema: SCHEMA_REP })

phase('Note')
const note = await agent(`${COMMUN}
Tu es le RÉDACTEUR de la note de décision (neuf). Pièces : propositions ${liste}${A.gemini ? ', ' + A.gemini : ''} ; objections
${objsTexte} ; réponses ${reps ? reps.chemin : A.dossier + '/reponses/reponses.md'}.
Écris ${A.dossier}/note-decision-suite-P3-v1.md, pour Lazar, au format du programme : verdict d'abord (1 à 3 lignes) ; puis,
pour chaque branche du verdict (A, B, C), la décision en une phrase, l'enjeu, 2 ou 3 options survivantes (avantage,
inconvénient, coût, délai jusqu'au 1er novembre), la recommandation et sa confiance ; les options tombées et pourquoi (une
ligne chacune) ; les nœuds qui reviennent à Lazar (modification d'hypothèse ou de revendication, dépense, contact) ; ce
qu'il faut préenregistrer en premier. Pas plus de trois pages. Rends le chemin, un résumé, la recommandation et les nœuds.`,
  { label: 'redacteur', phase: 'Note', schema: SCHEMA_NOTE })

return { propositions: props.filter(Boolean).map(p => p.chemin), objections: objsTexte, reponses: reps ? reps.chemin : null, note }
