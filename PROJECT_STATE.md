# LLM Training Framework From Scratch

## Current Version

v0.1

---

## Environment

Python: 3.12.13

GPU:
RTX 3050 Laptop GPU (4GB)

Framework:
PyTorch 2.11.0+cu128

---

## Design Decisions

Model:
- Decoder Only GPT

Tokenizer:
- Custom BPE

Trainer:
- Custom Trainer

Architecture:
- Pre LayerNorm

Activation:
- GELU

Attention:
- Causal Self Attention

Environment:
- Conda

---

## Completed Modules

### Module 1.0
Environment Setup

Status: Complete

Completed:
- Conda Environment Created
- Python 3.12 Installed
- PyTorch Installed
- CUDA Verified
- GPU Verified

---

### Module 1.1
Project Structure

Status: Complete

Folders:
- configs
- datasets
- tokenizer
- dataloader
- models
- training
- evaluation
- inference
- finetuning
- quantization
- serving
- deployment
- checkpoints
- tests
- scripts
- docs

Files:
- README.md
- PROJECT_STATE.md
- requirements.txt
- .gitignore
- train.py

---

## Current Folder Structure

```text
llm-training-framework/

configs/
datasets/
tokenizer/
dataloader/
models/
training/
evaluation/
inference/
finetuning/
quantization/
serving/
deployment/
checkpoints/
tests/
scripts/
docs/

README.md
PROJECT_STATE.md
requirements.txt
.gitignore
train.py
```

---

## Public Interfaces

None Yet

---

## Next Module

Module 1.2 Dataset Abstraction