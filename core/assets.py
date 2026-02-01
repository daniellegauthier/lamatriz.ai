SEQUENCE_IMAGE_FILES = {
    "direct": "direct pathway.png",
    "feminine": "fem pathway.png",
    "knot": "knot pathway.png",
    "masc": "masc pathway.png",
    "pain": "pain pathway.png",
    "prayer": "prayer pathway.png",
    "precise": "precise pathway.png",
    "practical": "practical pathway.png",
    "plot": "plot pathway.png",
    "spiritual": "spiritual pathway.png",
    "sad": "sad pathway.png",
}

ASSET_IMAGE_BASE_URL = "https://daniellegauthier.github.io/lamatriz.ai/assets/img/"

def pathway_image_url(seq_key: str) -> str | None:
    fname = SEQUENCE_IMAGE_FILES.get(seq_key)
    if not fname:
        return None
    return ASSET_IMAGE_BASE_URL + fname.replace(" ", "%20")
