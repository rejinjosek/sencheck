from app.services import get_subfeddit_by_title, SentimentAnalyzer

import pytest


present_title = "Dummy Topic 1"
absent_title = "Rejin"
skip_records = 0
limit_records = 2


def test_get_subfeddit_by_title_present_title():
    present_subfeddit = get_subfeddit_by_title(present_title)
    assert isinstance(present_subfeddit, dict)
    assert present_subfeddit.get("title") == present_title


def test_get_subfeddit_by_title_absent_title():
    absent_title = "Rejin"
    absent_subfeddit = get_subfeddit_by_title(absent_title)
    assert isinstance(absent_subfeddit, str)


def test_sentiment_analyzer_get_scores():
    sa = SentimentAnalyzer()
    scores = sa.get_scores(present_title, limit_records, skip_records, sort_by_scores=True)

    assert len(scores) == 2
    assert "type" in scores[0].keys()
    # Test sorting
    assert all(scores[i]["score"] <= scores[i + 1]["score"] for i in range(len(scores) - 1))


def test_sentiment_analyzer_get_scores_absent_title():
    sa = SentimentAnalyzer()
    with pytest.raises(ValueError):
        sa.get_scores(absent_title)
