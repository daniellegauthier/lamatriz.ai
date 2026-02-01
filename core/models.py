import nltk, spacy, torch
import torch.nn.functional as F
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer

def ensure_spacy():
    try:
        return spacy.load("en_core_web_sm")
    except Exception:
        import spacy.cli
        spacy.cli.download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

def ensure_nltk():
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")

ensure_nltk()

nlp = ensure_spacy()
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

bert_sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

emotion_tokenizer = AutoTokenizer.from_pretrained(
    "j-hartmann/emotion-english-distilroberta-base"
)
emotion_model = AutoModelForSequenceClassification.from_pretrained(
    "j-hartmann/emotion-english-distilroberta-base"
)
