from typing import Dict, Tuple
import torch
import torch.nn.functional as F
from sentence_transformers import util
from .models import sbert_model, bert_sentiment, emotion_model, emotion_tokenizer, nlp

def encode_text(text: str):
    return sbert_model.encode(text, convert_to_tensor=True)

def score_sentiment(text: str) -> float:
    out = bert_sentiment(text[:512])[0]
    score = out["score"]
    return round(5 + 5 * score if out["label"] == "POSITIVE" else 1 + 4 * (1 - score), 2)

def classify_emotion(text: str) -> Tuple[str, float]:
    inputs = emotion_tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = emotion_model(**inputs).logits
        probs = F.softmax(logits, dim=1).squeeze()
    idx = int(torch.argmax(probs))
    return emotion_model.config.id2label[idx], float(probs[idx])

def score_accomplishment(text: str) -> float:
    doc = nlp(text)
    score = 5.0
    for t in doc:
        if t.tag_ in {"VBD", "VBN"}:
            score += 0.5
    return round(min(10, score), 2)
