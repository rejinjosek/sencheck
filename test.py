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
import requests

def test_http_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("HTTP GET request successful!")
            print("Response content:")
            print(response.json())  # Assuming response is JSON, adjust if otherwise
            breakpoint()
        else:
            print(f"HTTP GET request failed with status code: {response.status_code}")
            print("Response content:")
            print(response.text)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
url = "http://localhost:8080/api/v1/comments/?subfeddit_id=2&skip=0&limit=10"
test_http_endpoint(url)
