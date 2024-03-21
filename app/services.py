import requests


def http_get_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("HTTP GET request successful!")
            return response.json()
        else:
            print(f"HTTP GET request failed with status code: {response.status_code}")
            print("Response content:")
            return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


class FedditService:
    """Service provides retrieval and processing feddit data.
    
    """
    _endpoint_url:str = "http://localhost:8080/api/v1/"
    
    def get_subfeddits(self, skip_records:int, limit_records:int):
        pass
    
    def get_comments_by_id(self, feddit_id:int, skip_records:int, limit_records:int):
        pass