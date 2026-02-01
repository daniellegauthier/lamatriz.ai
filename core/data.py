import os, re, pandas as pd
from typing import Dict, List

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets", "data")

CSV_PATH_PLUS  = os.path.join(ASSETS, "la matrice plus.csv")
CSV_PATH_COLOR = os.path.join(ASSETS, "la matrice.csv")

SEQUENCE_ALIASES = {
    "Direct": "direct",
    "Feminine": "feminine",
    "Knot": "knot",
    "Masculine": "masc",
    "Pain": "pain",
    "Prayer": "prayer",
    "Precise": "precise",
    "Practical": "practical",
    "Plot": "plot",
    "Spiritual": "spiritual",
    "Sad": "sad",
}

def load_pathway_info():
    df = pd.read_csv(CSV_PATH_PLUS)
    rows = df[df["color"].astype(str).str.lower().isin(SEQUENCE_ALIASES.values())]

    seq_to_colors = {}
    seq_phrase = {}

    for _, row in rows.iterrows():
        key = row["color"].strip().lower()
        colors = [c.strip() for c in str(row.get("r", "")).split(",") if c]
        seq_to_colors[key] = colors

        phrase = " ".join(
            str(row[c]).strip()
            for c in df.columns
            if c not in ("color", "r", "g", "b") and pd.notna(row[c])
        )
        seq_phrase[key] = phrase

    return seq_to_colors, seq_phrase
