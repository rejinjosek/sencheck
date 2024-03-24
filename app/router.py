from typing import List
from fastapi import APIRouter, HTTPException

from services import SentimentAnalyzer

router = APIRouter()
sentiment_analyzer = SentimentAnalyzer()


@router.get("/scores/", summary="Get sentiment scores for comments in a subfeddit.")
def get_scores(subfeddit_title:str, skip_records:int=0, limit_records:int=25, sort_by_scores:bool=False):
    try:
        scores = sentiment_analyzer.get_scores(subfeddit_title, skip_records, limit_records, sort_by_scores)
        if isinstance(scores, str):
            # Handle case where there is an error message returned
            raise HTTPException(status_code=404, detail=scores)
        return scores
    except Exception as e:
        # Handle any unexpected exceptions
        raise HTTPException(status_code=500, detail=str(e))

