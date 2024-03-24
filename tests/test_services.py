"""
return subfeddits of given skip and limit values
url = "http://localhost:8080/api/v1/subfeddits/?skip=2&limit=10"
response: ['limit', 'skip', 'subfeddits']
subfeddits: [{'id': 3, 'username': 'admin_3', 'title': 'Dummy Topic 3', 'description': 'Dummy Topic 3'}]

return subfeddit for given ID
url = "http://localhost:8080/api/v1/subfeddit/?subfeddit_id=2"
Id is mandatory field
response:['id', 'username', 'title', 'description', 'limit', 'skip', 'comments']
comments: ['id', 'username', 'text', 'created_at'] unix epochs

Return comments of given subfeddit ID with skip and limit range
http://localhost:8080/api/v1/comments/?subfeddit_id=2&skip=0&limit=10
response: ['subfeddit_id', 'limit', 'skip', 'comments']
commentsList[dict]: ['id', 'username', 'text', 'created_at']


"""
from app.services import get_subfeddit_by_title, SentimentAnalyzer


def test_get_subfeddit_by_title_present_title():
    present_title = "Dummy Topic 1"
    present_subfeddit = get_subfeddit_by_title(present_title)
    assert isinstance(present_subfeddit,dict)
    assert present_subfeddit.get('title')==present_title

def test_get_subfeddit_by_title_absent_title():
    absent_title = "Rejin"
    absent_subfeddit = get_subfeddit_by_title(absent_title)
    assert isinstance(absent_subfeddit, str)

def test_sentiment_analyzer_get_scores():
    subfeddit_title = "Dummy Topic 1"
    skip_records = 0
    limit_records = 2
    sa = SentimentAnalyzer(subfeddit_title, skip_records, limit_records)
    scores = sa.get_scores()
    
    assert len(scores)==2
    assert 'type' in scores[0].keys()    

def test_sentiment_analyzer_get_scores_absent_title():
    subfeddit_title = "Rejin"
    sa = SentimentAnalyzer()
    scores = sa.get_scores(subfeddit_title)
    assert isinstance(scores,str)
