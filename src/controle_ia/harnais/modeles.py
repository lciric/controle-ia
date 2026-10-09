"""Modèles et tokeniseurs du harnais (T0.4).

- `modele_jouet` et `tokeniseur_caracteres` : un petit modèle de type Llama à poids aléatoires et un
  tokeniseur par caractères, construits hors ligne, pour développer et tester le harnais sur
  processeur. Ils ne servent à aucune mesure.
- `charger_modele` : modèles réels, réservés aux machines de calcul. Liste blanche : utiliser un autre
  modèle est un changement de modèle, interdit sans GO de Lazar ; révision (commit) obligatoire.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import types
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret

# Modèles prévus par le programme (agent) et par les propositions D1 et D2 (moniteurs, juges).
# Tout ajout passe par un GO de Lazar (« changer de modèle sans GO » est interdit).
MODELES_AUTORISES = {
    "meta-llama/Llama-3.1-8B-Instruct": "agent ; juge (D1, D2)",
    "Qwen/Qwen2.5-7B-Instruct": "second modèle du programme ; juge (D2)",
    "meta-llama/Llama-3.2-3B-Instruct": "moniteur de confiance plus faible (D1, proposition)",
    "mistralai/Mistral-7B-Instruct-v0.3": "juge (D2, proposition)",
}

ALPHABET = ([chr(c) for c in range(32, 127)] + ["\n", "\t"]
            + list("éèêëàâäçîïôöûùüÿœæÉÈÊÀÂÇÎÔÛ’«»—–…"))
SPECIAUX = {"<pad>": 0, "<s>": 1, "</s>": 2, "<unk>": 3}


def tokeniseur_caracteres():
    """Tokeniseur par caractères, construit hors ligne (aucun téléchargement)."""
    from tokenizers import Tokenizer, decoders, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast

    vocab = dict(SPECIAUX)
    for ch in ALPHABET:
        vocab.setdefault(ch, len(vocab))
    tok = Tokenizer(models.WordLevel(vocab=vocab, unk_token="<unk>"))
    tok.pre_tokenizer = pre_tokenizers.Split(pattern="", behavior="isolated")
    tok.decoder = decoders.Fuse()
    return PreTrainedTokenizerFast(tokenizer_object=tok, bos_token="<s>", eos_token="</s>",
                                   pad_token="<pad>", unk_token="<unk>")


GABARIT_JOUET = ("{% for m in messages %}<|im_start|>{{ m['role'] }}\n{{ m['content'] }}<|im_end|>\n{% endfor %}"
                 "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")


def tokeniseur_caracteres_chat():
    """Tokeniseur par caractères muni d'un gabarit de conversation (balises de tour à la manière de
    ChatML), hors ligne, pour éprouver `FormatChat` sans modèle réel. Ne sert à aucune mesure."""
    tok = tokeniseur_caracteres()
    tok.add_special_tokens({"additional_special_tokens": ["<|im_start|>", "<|im_end|>"]})
    tok.chat_template = GABARIT_JOUET
    return tok


def modele_jouet(graine: int, taille_vocabulaire: int, couches: int = 4, largeur: int = 64,
                 tetes: int = 4, tetes_cle_valeur: int = 2, intermediaire: int = 128):
    """Petit modèle de type Llama à poids aléatoires, initialisation déterministe par la graine."""
    from transformers import LlamaConfig, LlamaForCausalLM

    cfg = LlamaConfig(vocab_size=taille_vocabulaire, hidden_size=largeur, intermediate_size=intermediaire,
                      num_hidden_layers=couches, num_attention_heads=tetes, num_key_value_heads=tetes_cle_valeur,
                      max_position_embeddings=4096, bos_token_id=SPECIAUX["<s>"], eos_token_id=SPECIAUX["</s>"],
                      pad_token_id=SPECIAUX["<pad>"], tie_word_embeddings=False)
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(int(graine))
        modele = LlamaForCausalLM(cfg)
    return modele.eval()


def empreinte_poids(modele) -> str:
    """sha256 des poids (ordre des paramètres nommés, type compris) : identifie le modèle exact d'un run.
    Les tenseurs bfloat16, que numpy ne connaît pas, sont lus bit à bit (vue en entiers de 16 bits)."""
    h = hashlib.sha256()
    for nom, p in sorted(modele.state_dict().items()):
        t = p.detach().to("cpu").contiguous()
        h.update(f"{nom}/{t.dtype}".encode("utf-8") if t.dtype == torch.bfloat16 else nom.encode("utf-8"))
        if t.dtype == torch.bfloat16:
            t = t.view(torch.int16)
        h.update(t.numpy().tobytes())
    return h.hexdigest()


COMMIT = re.compile(r"^[0-9a-f]{40}$")


def exiger_modele_autorise(nom: str, revision: str | None) -> None:
    if nom not in MODELES_AUTORISES:
        raise GardeArret(f"modèle {nom!r} hors liste blanche : changer de modèle exige un GO de Lazar")
    if not revision or not COMMIT.match(revision):
        raise GardeArret(f"modèle {nom!r} sans révision figée (commit complet, 40 caractères hexadécimaux) : "
                         "une branche comme « main » peut bouger, la reproductibilité l'exige")


def charger_modele(nom: str, revision: str, dtype: str = "bfloat16", appareil: str = "cuda",
                   attention: str = "sdpa"):
    """Modèle réel (machines de calcul seulement). Aucun téléchargement sans liste blanche et révision figée.

    Le point de contrôle (bfloat16, vérifié) est chargé tel quel, puis porté sur la carte ; une demande en simple
    précision s'y convertit ensuite, sans perte (bfloat16 ⊂ float32). La mémoire vive n'accueille ainsi que
    16 Go pour un modèle de 8 milliards de paramètres, au lieu de 32 Go en simple précision. Une demande en double
    précision (bfloat16 ⊂ float64, sans perte) se convertit sur le processeur avant le transfert : la carte ne porte
    jamais les deux copies à la fois (64 Go en double précision pour 8 milliards de paramètres)."""
    exiger_modele_autorise(nom, revision)
    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

    natif = type_natif(AutoConfig.from_pretrained(nom, revision=revision))
    if natif != "bfloat16":
        raise GardeArret(f"{nom} : point de contrôle en {natif}, pas en bfloat16 ; la conversion ne serait pas exacte")
    tokeniseur = AutoTokenizer.from_pretrained(nom, revision=revision)
    modele = AutoModelForCausalLM.from_pretrained(nom, revision=revision, dtype=torch.bfloat16,
                                                  attn_implementation=attention)
    if dtype == "float64":
        modele = modele.to(torch.float64).to(appareil)
        normalisations_en_double(modele)
    else:
        modele = modele.to(appareil)
        if dtype != "bfloat16":
            modele = modele.to(getattr(torch, dtype))
    exiger_type_des_poids(modele, dtype)
    return modele.eval(), tokeniseur


def _rms_en_double(self, x):
    """Normalisation RMS entièrement en double précision : même formule que la bibliothèque, sans son passage par la
    simple précision."""
    variance = x.pow(2).mean(-1, keepdim=True)
    return self.weight * (x * torch.rsqrt(variance + self.variance_epsilon))


def normalisations_en_double(modele) -> int:
    """Version 2, phase de logique : la bibliothèque calcule ses normalisations RMS en simple précision (variance
    réduite en simple précision), même dans un modèle en double précision. Sur carte, l'ordre de cette réduction peut
    dépendre de la forme du lot (8 lignes au décodage, L en passe unique) : un bruit de simple précision viendrait dans
    la seule zone générée, celle où la garde d'équivalence lit un défaut de décodage (contre-lecture 1 de la v2, V-1).
    Ici, chaque normalisation de ce modèle (attribut d'instance, la classe n'est pas touchée) calcule en double
    précision. Garde : modèle en double précision, au moins une normalisation. Rend le nombre de normalisations."""
    n = 0
    for m in modele.modules():
        if type(m).__name__.endswith("RMSNorm"):
            if m.weight.dtype != torch.float64:
                raise GardeArret(f"normalisation en double précision demandée sur des poids en {m.weight.dtype}")
            m.forward = types.MethodType(_rms_en_double, m)
            n += 1
    if n == 0:
        raise GardeArret("aucune normalisation RMS dans le modèle : structure inattendue")
    modele.normalisations_en_double = n
    return n


def type_natif(config) -> str:
    """Type des poids déclaré par la configuration (`dtype`, ou `torch_dtype` dans les versions anciennes)."""
    t = config.dtype if hasattr(config, "dtype") else getattr(config, "torch_dtype", None)
    return str(t).replace("torch.", "") if t is not None else "inconnu"


def exiger_type_des_poids(modele, dtype: str) -> None:
    """Garde : tous les paramètres sont du type demandé (pas de demi-mesure silencieuse)."""
    attendu = getattr(torch, dtype)
    autres = sorted({str(p.dtype) for p in modele.parameters() if p.dtype != attendu})
    if autres:
        raise GardeArret(f"poids de type {autres} alors que {dtype} est demandé")


def sha1_git(donnees: bytes) -> str:
    """Identifiant git d'un fichier (« blob »), celui que publie un dépôt de modèle pour ses petits fichiers."""
    return hashlib.sha1(b"blob %d\0" % len(donnees) + donnees).hexdigest()


def comparer_fichiers(dossier: Path, publies: dict[str, dict]) -> dict:
    """Empreintes des fichiers d'un dossier de modèle, comparées aux empreintes publiées : sha256 pour les fichiers
    stockés en LFS (`{"sha256": …}`), identifiant git sinon (`{"git_sha1": …}`). Garde : fichier inconnu du dépôt
    ou empreinte différente → arrêt."""
    sortie = {}
    for f in sorted(x for x in Path(dossier).iterdir() if x.is_file()):
        if f.name not in publies:
            raise GardeArret(f"{f.name} : fichier absent de la révision publiée")
        attendu = publies[f.name]
        h = hashlib.sha256()
        with open(f, "rb") as fic:
            for bloc in iter(lambda: fic.read(1 << 24), b""):
                h.update(bloc)
        ligne = {"octets": f.stat().st_size, "sha256": h.hexdigest()}
        if attendu.get("sha256"):
            ligne["conforme"] = ligne["sha256"] == attendu["sha256"]
        else:
            ligne["git_sha1"] = sha1_git(f.read_bytes())
            ligne["conforme"] = ligne["git_sha1"] == attendu.get("git_sha1")
        if not ligne["conforme"]:
            raise GardeArret(f"{f.name} : empreinte différente de celle publiée pour la révision")
        sortie[f.name] = ligne
    return sortie


def empreintes_fichiers_modele(nom: str, revision: str, essentiels=("config.json", "generation_config.json",
                                                                    "tokenizer.json", "tokenizer_config.json"),
                               publies: dict | None = None, cache_dir: str | None = None) -> dict:
    """Fichiers du modèle en cache local (dossier de la révision figée) contre les empreintes publiées par son dépôt
    (`publies` : injecté par les tests ; sinon lu sur le dépôt du modèle)."""
    from huggingface_hub import HfApi, try_to_load_from_cache

    chemin = try_to_load_from_cache(nom, "config.json", cache_dir=cache_dir, revision=revision)
    if not isinstance(chemin, str):
        raise GardeArret(f"{nom}@{revision[:12]} : configuration absente du cache local")
    dossier = Path(chemin).parent
    if publies is None:
        publies = {}
        for x in HfApi().model_info(nom, revision=revision, files_metadata=True).siblings:
            publies[x.rfilename] = {"sha256": x.lfs.sha256} if x.lfs else {"git_sha1": x.blob_id}
    fichiers = comparer_fichiers(dossier, publies)
    manquants = [e for e in essentiels if e not in fichiers]
    if manquants or not any(n.endswith(".safetensors") for n in fichiers):
        raise GardeArret(f"fichiers du modèle manquants en cache : {manquants or 'poids'}")
    return fichiers


def fins_du_modele(modele, tokeniseur) -> set[int]:
    """Jetons d'arrêt : ceux de la configuration de génération du modèle, plus la fin du tokeniseur."""
    fins = set()
    cfg = getattr(modele, "generation_config", None)
    eos = getattr(cfg, "eos_token_id", None) if cfg is not None else None
    if isinstance(eos, int):
        fins.add(eos)
    elif eos:
        fins.update(int(e) for e in eos)
    if tokeniseur.eos_token_id is not None:
        fins.add(int(tokeniseur.eos_token_id))
    if not fins:
        raise GardeArret("aucun jeton d'arrêt connu pour ce modèle")
    return fins


def regler_determinisme(fils: int = 1, appareil: str = "cpu") -> dict:
    """Réglages consignés au manifeste : algorithmes déterministes, nombre de fils fixé ; sur processeur
    graphique, espace de travail de cuBLAS fixé (avant toute opération), TF32 coupé, cuDNN déterministe."""
    reglages = {"deterministe": True, "fils": int(fils), "torch": torch.__version__, "numpy": np.__version__,
                "appareil": appareil}
    if appareil.startswith("cuda"):
        if not torch.cuda.is_available():
            raise GardeArret("processeur graphique demandé mais indisponible")
        os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        if os.environ["CUBLAS_WORKSPACE_CONFIG"] not in (":4096:8", ":16:8"):
            raise GardeArret(f"CUBLAS_WORKSPACE_CONFIG={os.environ['CUBLAS_WORKSPACE_CONFIG']!r} : déterminisme non garanti")
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction = False
        torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction = False
        reglages.update({"cublas_workspace": os.environ["CUBLAS_WORKSPACE_CONFIG"], "tf32": False,
                         "reduction_reduite_bf16_fp16": False,
                         "carte": torch.cuda.get_device_name(0), "capacite": list(torch.cuda.get_device_capability(0)),
                         "cuda": torch.version.cuda, "cudnn": torch.backends.cudnn.version(), "pilote": pilote()})
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(fils))
    reglages["relus"] = etats_effectifs()
    return reglages


def etats_effectifs() -> dict:
    """Réglages relus dans la bibliothèque, et non seulement écrits : ce qui s'applique vraiment aux calculs."""
    m, d = torch.backends.cuda.matmul, torch.backends.cudnn
    return {"algorithmes_deterministes": bool(torch.are_deterministic_algorithms_enabled()),
            "precision_produits_simple": torch.get_float32_matmul_precision(),
            "precision_produits_cuda": str(getattr(m, "fp32_precision", "inconnue")),
            "tf32_produits": bool(m.allow_tf32), "tf32_cudnn": bool(d.allow_tf32),
            "reduction_reduite_bf16": bool(m.allow_bf16_reduced_precision_reduction),
            "reduction_reduite_fp16": bool(m.allow_fp16_reduced_precision_reduction),
            "cudnn_deterministe": bool(d.deterministic), "cudnn_banc_essai": bool(d.benchmark),
            "fils": int(torch.get_num_threads())}


def noyaux_attention_permis() -> dict:
    """Noyaux d'attention permis à l'instant de l'appel (à lire dans le contexte du noyau choisi)."""
    b = torch.backends.cuda
    lire = lambda f: bool(getattr(b, f)()) if hasattr(b, f) else None      # noqa: E731
    return {"flash": lire("flash_sdp_enabled"), "memoire_efficace": lire("mem_efficient_sdp_enabled"),
            "math": lire("math_sdp_enabled"), "cudnn": lire("cudnn_sdp_enabled"),
            "reduction_demi_dans_math": lire("fp16_bf16_reduction_math_sdp_allowed")}


def pilote() -> str | None:
    """Version du pilote de la carte (outil nvidia-smi), consignée avec les réglages."""
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"], capture_output=True,
                           text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() or None
