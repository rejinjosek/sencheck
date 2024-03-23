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
#import pytest
#from unittest.mock import patch
#from utils import get_subfeddit_by_title, get_comments_by_id
"""

# Dummy data for testing
dummy_subfeddits = [
    {"title": "python", "id": 1},
    {"title": "programming", "id": 2},
    {"title": "data science", "id": 3}
]

dummy_comments = [
    {"id": 1, "text": "Great post!"},
    {"id": 2, "text": "Interesting discussion."},
    {"id": 3, "text": "I have a question."}
]

# Mocking the _http_get_response function
@patch('utils._http_get_response')
def test_get_subfeddit_by_title(mock_http_get_response):
    # Mocking the return value of _http_get_response
    mock_http_get_response.return_value = {"subfeddits": dummy_subfeddits}

    # Test case for existing subfeddit
    assert get_subfeddit_by_title("python") == {"title": "python", "id": 1}

    # Test case for non-existing subfeddit
    assert get_subfeddit_by_title("java") is None

@patch('utils._http_get_response')
def test_get_comments_by_id(mock_http_get_response):
    # Mocking the return value of _http_get_response
    mock_http_get_response.return_value = {"comments": dummy_comments}

    # Test case for existing subfeddit ID
    assert get_comments_by_id(1) == dummy_comments

    # Test case for non-existing subfeddit ID
    assert get_comments_by_id(10) == []

"""
def test_api():
    url = "http://localhost:8000/v1/scores/?subfeddit_title=Dummy%Topic%1&skip_records=0&limit_records=10"
    import requests
    response = requests.get(url)
    print(response.json())
if __name__ == "__main__":
    pytest.main()
