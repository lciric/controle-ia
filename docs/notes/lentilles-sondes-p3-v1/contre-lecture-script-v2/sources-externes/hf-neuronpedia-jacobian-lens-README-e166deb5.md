---
license: apache-2.0
tags:
- jacobian_lens
- jpp_lens
- interpretability
---
This folder contains pre-fitted Jacobian Lenses and J++ Lenses for specific models.

Jacobian Lens and J++ Lens can be explored on Neuronpedia at [https://neuronpedia.org/jlens](https://neuronpedia.org/jlens).

## Jacobian Lens

The Jacobian Lenses (`<model>/jlens/`) were trained using Anthropic's [Jacobian Lens](https://github.com/anthropics/jacobian-lens) library. The same library can be used to load the lens and local visualizer.

## J++ Lens

The J++ Lenses (`<model>/jpp/`) are from *J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses* (Ayonrinde & Lindsey, 2026). J++ Lens is an improved, drop-in replacement for the Jacobian Lens. It is more coherent on earlier layers, where the Jacobian Lens is often unreliable.

Credit for the method and for the lenses marked "Ayonrinde & Lindsey" goes to the authors. Their original lens files are at [koayon/jpp-lenses](https://huggingface.co/koayon/jpp-lenses). We changed those files to the format that the Neuronpedia inference server and the Jacobian Lens files use. We cast the maps from fp32 to fp16 (relative error 2.7e-4 or less; 1.1e-3 for Gemma 4 31B, which has very small values in some layers). We did not change them in other ways. We fitted the lenses marked "Neuronpedia" with the paper's code and recipe.

| Model | File | Fitted by | Recall@10 |
|---|---|---|---|
| [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) | `qwen3.6-27b/jpp/Salesforce-wikitext/Qwen3.6-27B_jpp_lens.pt` | Ayonrinde & Lindsey | 55.2% |
| [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | `qwen3.5-9b/jpp/Salesforce-wikitext/Qwen3.5-9B_jpp_lens.pt` | Ayonrinde & Lindsey | 55.0% |
| [google/gemma-4-31B](https://huggingface.co/google/gemma-4-31B) | `gemma-4-31b/jpp/Salesforce-wikitext/gemma-4-31B_jpp_lens.pt` | Ayonrinde & Lindsey | 58%* |
| [allenai/Olmo-3-1125-32B](https://huggingface.co/allenai/Olmo-3-1125-32B) | `olmo-3-1125-32b/jpp/Salesforce-wikitext/Olmo-3-1125-32B_jpp_lens.pt` | Ayonrinde & Lindsey | 50.0% |
| [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | `qwen3.5-122b-a10b/jpp/Salesforce-wikitext/Qwen3.5-122B-A10B_jpp_lens.pt` | Ayonrinde & Lindsey | 48.4% |
| [deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | `deepseek-v4-flash/jpp/Salesforce-wikitext/DeepSeek-V4-Flash_jpp_lens.pt` | Ayonrinde & Lindsey | 61.4% |
| [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | `qwen3.5-0.8b/jpp/Salesforce-wikitext/Qwen3.5-0.8B_jpp_lens.pt` | Neuronpedia | 44.9% |
| [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | `qwen3.5-2b/jpp/Salesforce-wikitext/Qwen3.5-2B_jpp_lens.pt` | Neuronpedia | 51.5% |
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | `qwen3-4b/jpp/Salesforce-wikitext/Qwen3-4B_jpp_lens.pt` | Neuronpedia | 53.8% |

Recall@10 is macro recall on the paper's labelled readout items. The scores for the "Ayonrinde & Lindsey" lenses are from [koayon/jpp-lenses](https://huggingface.co/koayon/jpp-lenses). We scored the "Neuronpedia" lenses with the paper's evaluation, on its held-out items.

\*The poetry task is dropped for Gemma 4 31B, where only 1 of its 98 items passes the correctness filter.

### File format

Each `<model>_jpp_lens.pt` is a `torch.save` dictionary, loadable with `torch.load(path, weights_only=True)`:

| Key | Value |
|---|---|
| `J` | `{layer: fp16 Tensor[d_model, d_model]}`, the map from that layer's residual stream to the final block's |
| `source_layers` | the layers in `J`: every block except the final one |
| `d_model` | the residual width |
| `n_prompts` | the number of WikiText-103 prompts in the fit |
| `provenance` | the source file, the method, the fitting configuration, and the activation that the maps read (`capture_point`, `stream_reduce`) |

The readout at layer ℓ for a residual `h` is `logits = unembed(h @ J[ℓ].T)`, where `unembed` is the model's final norm followed by its LM head. For DeepSeek-V4-Flash, `h` is the mean of the four residual streams.

The `config.yaml` beside each file records the source, the fitting configuration, and the command that wrote the file.

### Licence

The J++ Lens files (`<model>/jpp/`) are Apache-2.0, as the source lenses. Each lens is derived from its base model. The method builds on the Jacobian Lens of Gurnee et al. (2026) and the R-Lens of Camila Blank and Agam Bhatia.

### Citation

Citation information for the J++ Lens paper is coming soon.
