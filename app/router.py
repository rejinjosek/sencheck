from typing import List
from fastapi import APIRouter, HTTPException

from services import SentimentAnalyzer
from schemas import ScoresRequest, ScoresResponse

router = APIRouter()
sentiment_analyzer = SentimentAnalyzer()

@router.get("/hello")
def hello_world():
    return {"message": "Hello, world from router!"}

@router.get("/scores/", summary="Get sentiment scores for comments in a subfeddit.")
def get_scores(subfeddit_title:str, skip_records:int=0, limit_records:int=25):
    try:
        scores = sentiment_analyzer.get_scores(subfeddit_title, skip_records, limit_records)
        if isinstance(scores, str):
            # Handle case where there is an error message returned
            raise HTTPException(status_code=404, detail=scores)
        return scores
    except Exception as e:
        # Handle any unexpected exceptions
        raise HTTPException(status_code=500, detail=str(e))

