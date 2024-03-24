from typing import List
import logging

from fastapi import APIRouter, HTTPException

from services import SentimentAnalyzer

logger = logging.getLogger(__name__)
router = APIRouter()
sentiment_analyzer = SentimentAnalyzer()


@router.get("/scores/", summary="Get sentiment scores for comments in a subfeddit.")
def get_scores(
    subfeddit_title: str,
    skip_records: int = 0,
    limit_records: int = 25,
    sort_by_scores: bool = False,
):
    """
    Get sentiment scores for comments in a subfeddit.

    Args:
        subfeddit_title (str): Title of the subfeddit.
        skip_records (int): Number of records to skip.
        limit_records (int): Maximum number of records to fetch.
        sort_by_scores (bool): Sort the results based on scores.

    Returns:
        List[Dict]: List of comments with ID, score, and created timestamp.
    """
    try:
        scores = sentiment_analyzer.get_scores(
            subfeddit_title, skip_records, limit_records, sort_by_scores
        )
        return scores
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(status_code=500, detail="Internal server error.")
