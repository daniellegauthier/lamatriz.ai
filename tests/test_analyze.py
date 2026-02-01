import base64
import pytest

from core.analyze import analyze


@pytest.fixture
def sample_input():
    return {
        "text": "I finally decided to leave a toxic job and prioritize my mental health.",
        "sequence": "Knot",
        "color_inputs": []
    }


def test_analyze_returns_expected_keys(sample_input):
    result = analyze(**sample_input)

    expected_keys = {
        "sequence",
        "colors",
        "sentiment",
        "emotion",
        "emotion_confidence",
        "accomplishment",
        "pathway_phrase",
        "gnh_top_5",
        "gnh_plot_base64",
        "pathway_image",
    }

    assert expected_keys.issubset(result.keys())


def test_gnh_top_5_structure(sample_input):
    result = analyze(**sample_input)

    top5 = result["gnh_top_5"]

    assert isinstance(top5, dict)
    assert 1 <= len(top5) <= 5

    for domain, score in top5.items():
        assert isinstance(domain, str)
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0


def test_gnh_plot_is_valid_png(sample_input):
    result = analyze(**sample_input)

    b64 = result["gnh_plot_base64"]
    assert isinstance(b64, str)

    png_bytes = base64.b64decode(b64)
    assert png_bytes[:8] == b"\x89PNG\r\n\x1a\n"


def test_pathway_image_url(sample_input):
    result = analyze(**sample_input)

    img = result["pathway_image"]
    assert img is None or img.startswith("http")


def test_invalid_sequence_raises():
    with pytest.raises(ValueError):
        analyze(
            text="test",
            sequence="INVALID_SEQUENCE",
            color_inputs=[]
        )
