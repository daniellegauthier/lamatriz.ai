from typing import Dict, Tuple
import io, base64
import matplotlib.pyplot as plt
from sentence_transformers import util
from .models import sbert_model

GNH_DOMAINS = {
    "Mental Wellness": "mental health, emotional clarity, peace of mind",
    "Social Wellness": "relationships, community, friendship, social harmony",
    "Economic Wellness": "income, savings, financial stability, cost of living",
    "Workplace Wellness": "career, work-life balance, promotion, productivity",
    "Physical Wellness": "physical health, sleep, fitness, exercise",
    "Environmental Wellness": "green space, nature, environmental care",
    "Health": "healthcare, medical care, recovery, well-being",
    "Education Value": "learning, education, school, knowledge, wisdom",
    "Good Governance": "freedom, justice, fairness, democratic participation",
    "Living Standards": "housing, wealth, basic needs, affordability",
    "Cultural Diversity": "tradition, language, cultural expression, heritage",
    "Political Wellness": "rights, law, free speech, civic participation",
    "Ecological Diversity": "biodiversity, forest, ecosystem, wildlife",
}

GNH_COLORS = {
    "Economic Wellness": "#808080",
    "Mental Wellness": "#FA005A",
    "Workplace Wellness": "#ffd700",
    "Physical Wellness": "#FAB478",
    "Social Wellness": "#ffa500",
    "Political Wellness": "#ffffff",
    "Environmental Wellness": "#0000FF",
    "Ecological Diversity": "#00FF00",
    "Health": "#FF0000",
    "Good Governance": "#000000",
    "Education Value": "#8b4513",
    "Living Standards": "#ffff00",
    "Cultural Diversity": "#B432FF",
}

def encode(text: str):
    return sbert_model.encode(text, convert_to_tensor=True)

def semantic_indicator_mapping(
    text: str,
    sentiment_score: float,
    sentiment_weight: float = 0.3
) -> Dict[str, float]:

    v = encode(text)
    scores = {}

    for domain, desc in GNH_DOMAINS.items():
        sim = float(util.cos_sim(v, encode(desc)).item())
        blended = (1 - sentiment_weight) * sim + sentiment_weight * (sentiment_score / 10)
        scores[domain] = round(max(0.0, min(1.0, blended)), 3)

    return dict(sorted(scores.items(), key=lambda x: -x[1]))

def gnh_plot_base64(indicators: Dict[str, float]) -> str:
    labels = list(indicators.keys())
    values = list(indicators.values())
    colors = [GNH_COLORS.get(l, "#cccccc") for l in labels]

    fig = plt.figure(figsize=(8, 5))
    plt.barh(labels, values, color=colors)
    plt.gca().invert_yaxis()
    plt.xlabel("Score")
    plt.title("GNH Indicator Similarity")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return base64.b64encode(buf.read()).decode("utf-8")

def gnh_plot_png(indicators: Dict[str, float]) -> bytes:
    labels = list(indicators.keys())
    values = list(indicators.values())

    fig = plt.figure(figsize=(8, 5))
    plt.barh(labels, values)
    plt.gca().invert_yaxis()
    plt.xlabel("Score")
    plt.title("GNH Indicator Similarity")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)

    return buf.read()
