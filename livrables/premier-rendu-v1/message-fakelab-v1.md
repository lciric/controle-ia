# Message aux auteurs de FakeLab — v1 (rédigé par Claude, envoyé par Lazar)

**À vérifier avant envoi (R7)** : le titre exact et la liste des auteurs de arXiv 2607.07368 n'ont été vus qu'au niveau transcription (« Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors » — Oliver Makins, Orazio Angelini, Zohreh Shams, Mary Phuong). Le message ne cite volontairement aucun chiffre du papier. Destinataire : l'auteur de correspondance indiqué dans le PDF.
Champs à remplir : [Nom complet], [affiliation], [adresse].

---

**Objet :** Request for access to the FakeLab environment (arXiv:2607.07368)

Dear Dr. [Nom de l'auteur de correspondance],

I am [Nom complet], [affiliation]. I am leading a research programme on white-box control of diffuse threats: we study whether monitors that read an agent's internal activations, aggregated sequentially over time and across agents, can recover the evidence that fragmentation removes from per-action outputs. Your recent paper on distributed attacks against per-instance monitors (arXiv:2607.07368) is the closest black-box counterpart to the multi-agent part of our work, and we would like to build on it rather than reinvent it.

Would you be willing to share the FakeLab environment with us for research use?

What we would do with it:
- port the environment to open-weight models (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct), so that we can read activations;
- reproduce your fragmentation effect with black-box per-instance monitors as a baseline;
- compare it with activation-based monitors aggregated across agents and over time.

What we commit to:
- we will not redistribute the environment, its tasks or its attack objectives without your permission, and we will follow any terms or licence you specify;
- we will cite your paper and acknowledge the access in any publication;
- we will share our port, results and any bugs we find with you before publication, if you wish.

We would use FakeLab in the later phase of the programme (from early 2027), so there is no urgency on your side. If a version for open-weight models exists, or if a different environment would serve better, we would be grateful for your advice.

Thank you for considering this request.

Best regards,
[Nom complet]
[affiliation] — [adresse]
