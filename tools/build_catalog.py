#!/usr/bin/env python3
"""Build catalog + search index + glossary for the static hub.

Run:  python tools/build_catalog.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hub" / "data"
OUT_STATIC = ROOT / "hub" / "static" / "data"
DAY_RE = re.compile(r"^Day(\d+)$")
TITLE_RE = re.compile(r"^#\s+Day\s+\d+\s*[-—–]+\s*(.+)$", re.M)

HELP = {
    "gradient": {
        "title": "Gradient",
        "body": "The vector of partial derivatives of the loss with respect to every parameter. It points uphill, so training steps against it. If the loss is not falling, the gradient is either vanishing (too small to move anything), exploding (steps overshoot), or being zeroed incorrectly between steps.",
    },
    "overfitting": {
        "title": "Overfitting",
        "body": "The model memorised the training set instead of learning the pattern: training score high, validation score much lower. Fix with more data, augmentation, regularisation, or a smaller model. The opposite is underfitting — both scores low — which needs more capacity or better features.",
    },
    "leakage": {
        "title": "Data leakage",
        "body": "Information in training that will not exist at prediction time: preprocessing fitted before the split, a column filled in after the outcome, or the same entity on both sides of a split. Symptom: an unbelievably good validation score followed by collapse in production.",
    },
    "regularization": {
        "title": "Regularisation",
        "body": "Any pressure toward simpler models: L2 (ridge) shrinks weights smoothly, L1 (lasso) drives some to exactly zero, dropout removes random activations, early stopping halts before memorisation. Scale features before regularising or the penalty punishes whichever column has small units.",
    },
    "crossvalidation": {
        "title": "Cross-validation",
        "body": "Rotate which slice of data is held out, so every row is validated once. Report the mean AND the spread across folds — a 2% fold-to-fold spread makes a 0.3% difference between models meaningless. Use stratified folds for imbalance, grouped for repeated entities, time-ordered for time series.",
    },
    "embedding": {
        "title": "Embedding",
        "body": "A dense vector where distance means semantic similarity. 'Car trouble' lands near 'engine won't start' even with no shared words. Normalise embeddings and cosine similarity becomes a dot product. Never mix vectors from two different embedding models — the spaces are unrelated.",
    },
    "attention": {
        "title": "Attention",
        "body": "Every token emits a query, a key and a value; query-key dot products become weights over the values, so each position pulls in whatever else matters. Scaled by 1/sqrt(d) to keep softmax out of saturation. Cost grows with the square of sequence length, which is why long context is expensive.",
    },
    "transformer": {
        "title": "Transformer",
        "body": "A stack of blocks, each: LayerNorm -> multi-head attention -> residual add -> LayerNorm -> feed-forward -> residual add. Encoder-only (BERT) for understanding, decoder-only (GPT) for generation, encoder-decoder (T5) for translation-shaped tasks. Positions are injected explicitly since attention is order-blind.",
    },
    "token": {
        "title": "Token",
        "body": "The unit a model actually reads — a subword piece, not a word. Roughly 4 characters of English per token; other scripts cost far more. Tokens determine your bill, your context limit, and why models are bad at counting letters. Estimate cost in tokens of your users' real language.",
    },
    "rag": {
        "title": "RAG (retrieval augmented generation)",
        "body": "Chunk your documents, embed them, retrieve the top matches for a question, and put them in the prompt. Use it for knowledge that changes; fine-tune for behaviour and format. Retrieval quality is the bottleneck — a perfect model answering from the wrong three chunks is still wrong.",
    },
    "hallucination": {
        "title": "Hallucination",
        "body": "The model predicts plausible tokens, not true ones, so fluent-and-wrong is its default failure. Reduce it by grounding answers in retrieved sources, requiring citations, and giving the system an explicit 'not in my sources' path. An abstain option beats any confidence score.",
    },
    "finetuning": {
        "title": "Fine-tuning",
        "body": "Continue training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches facts. A few hundred excellent examples beat ten thousand mediocre ones. LoRA trains ~0.1% of the parameters and produces a megabyte-sized adapter instead of a new model.",
    },
    "lora": {
        "title": "LoRA",
        "body": "Freeze the base weights and train two small low-rank matrices whose product is added to target layers. Initialise B to zeros so the adapted model starts identical to the base. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU. Too high a rank loses the efficiency and gains the overfitting.",
    },
    "agent": {
        "title": "Agent",
        "body": "A loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Always bound the iterations, log every step, and require explicit confirmation before anything irreversible.",
    },
    "promptinjection": {
        "title": "Prompt injection",
        "body": "Retrieved documents, web pages and uploaded files are untrusted input. An attacker can write 'ignore previous instructions' inside a PDF and steer your agent. Delimit untrusted content explicitly, and enforce authorisation in code — a prompt is not a security boundary.",
    },
    "temperature": {
        "title": "Temperature",
        "body": "Scales the logits before sampling. Near 0 is nearly deterministic — correct for extraction and classification. Higher values add diversity for creative work. Top-p keeps the smallest set of tokens covering p of the probability mass. Running extraction at temperature 1 causes 'random' JSON failures.",
    },
    "drift": {
        "title": "Drift",
        "body": "Models rot. Data drift is inputs shifting; concept drift is the input-output relationship changing. Monitor input and prediction distributions daily because ground-truth labels arrive weeks late. PSI under 0.1 is stable, 0.1-0.2 watch, above 0.2 investigate.",
    },
    "calibration": {
        "title": "Calibration",
        "body": "A calibrated model that says 0.8 is right 80% of the time. Boosted trees and Naive Bayes are famously overconfident. Fix with Platt scaling or isotonic regression on a held-out set. You need calibration whenever a threshold turns a score into a business decision.",
    },
    "baseline": {
        "title": "Baseline",
        "body": "The dumbest thing that could work: predict the majority class, predict the mean, predict yesterday's value, or apply the existing keyword rules. Every model score must be reported next to a baseline score. 92% accuracy where 91% of rows are one class is not a result.",
    },
    "backpropagation": {
        "title": "Backpropagation",
        "body": "The chain rule applied backwards through the computation graph, reusing cached forward values so the cost is roughly one extra forward pass. Frameworks do it for you. Gradient-check any hand-written backward pass numerically, and zero the gradients between steps — PyTorch accumulates by design.",
    },
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    OUT_STATIC.mkdir(parents=True, exist_ok=True)
    days = []
    search_docs = []

    for path in sorted(ROOT.iterdir()):
        if not path.is_dir():
            continue
        m = DAY_RE.match(path.name)
        if not m:
            continue
        n = int(m.group(1))
        theme = f"Day {n:02d}"
        notes_path = path / "notes.md"
        if notes_path.exists():
            tm = TITLE_RE.search(notes_path.read_text(encoding="utf-8", errors="replace"))
            if tm:
                theme = tm.group(1).strip()
        examples = sorted(p.name for p in (path / "examples").glob("*.py"))
        days.append({
            "n": n,
            "id": path.name,
            "theme": theme,
            "examples": examples,
            "project": (path / "project.md").exists(),
        })
        for name in ("notes.md", "questions.md", "answers.md", "project.md"):
            f = path / name
            if not f.exists():
                continue
            search_docs.append({
                "day": n,
                "file": name,
                "theme": theme,
                "text": f.read_text(encoding="utf-8", errors="replace")[:12000],
            })

    days.sort(key=lambda d: d["n"])
    payloads = {
        "catalog.json": json.dumps({"days": days}, ensure_ascii=False),
        "search_index.json": json.dumps({"docs": search_docs}, ensure_ascii=False),
        "help.json": json.dumps(HELP, ensure_ascii=False, indent=2),
    }
    for dest in (OUT, OUT_STATIC):
        for name, blob in payloads.items():
            (dest / name).write_text(blob, encoding="utf-8")

    projects = sum(1 for d in days if d["project"])
    print(f"wrote {len(days)} days ({projects} with projects), {len(search_docs)} search docs -> {OUT}")


if __name__ == "__main__":
    main()
