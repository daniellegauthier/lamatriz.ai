from typing import Dict, List
from .data import SEQUENCE_ALIASES, load_pathway_info
from .scoring import score_sentiment, classify_emotion, score_accomplishment
from .gnh import semantic_indicator_mapping, gnh_plot_base64, gnh_plot_png
from .assets import pathway_image_url
from backend.api.cache import store_png   

SEQ_TO_COLORS, SEQ_PHRASE = load_pathway_info()

def analyze(
    text: str,
    sequence: str,
    color_inputs: List[str] | None = None,
) -> Dict:

    key = SEQUENCE_ALIASES.get(sequence)
    if not key or key not in SEQ_PHRASE:
        raise ValueError("Invalid sequence")

    colors = SEQ_TO_COLORS.get(key, [])
    phrase = SEQ_PHRASE[key]

    combined_text = " ".join([text, phrase]).strip()

    sentiment = score_sentiment(combined_text)
    emotion, emo_conf = classify_emotion(combined_text)
    accomplishment = score_accomplishment(combined_text)

    indicators = semantic_indicator_mapping(
        combined_text,
        sentiment_score=sentiment
    )
    
    png_bytes = gnh_plot_png(indicators)
    plot_key = store_png(png_bytes)

    top5 = dict(list(indicators.items())[:5])
    gnh_plot = gnh_plot_base64(indicators)
    image_url = pathway_image_url(key)

    return {
        "sequence": key,
        "colors": colors,

        "sentiment": sentiment,
        "emotion": emotion,
        "emotion_confidence": round(emo_conf, 3),
        "accomplishment": accomplishment,

        "pathway_phrase": phrase,

        "gnh_top_5": top5,
        "gnh_plot_base64": gnh_plot,
        "gnh_plot_png_url": f"/api/gnh-plot/{plot_key}/",

        "pathway_image": image_url,
    }



