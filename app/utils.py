import logging
from typing import Optional, Dict, Any
from config import RAPID_API_KEY

import requests


# API URL endpoints
base_url = "http://feddit:8080/api/v1/"
rapid_api_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

# Request header for rapid API
api_headers = {
    "X-RapidAPI-Key": RAPID_API_Key,
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
}


logger = logging.getLogger(__name__)


def http_get_response(
    url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None
) -> Optional[Dict[str, Any]]:
    """
    Makes an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to make the request to.
        headers (Optional[Dict[str, str]]): Optional headers to include in the request.
        params (Optional[Dict[str, Any]]): Optional parameters to include in the request.

    Returns:
        Optional[Dict[str, Any]]: The JSON response from the server, or None if an error occurred.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"An error occurred while API request: {e}")


def get_score_from_twinword(query_string):
    # Get score using twinword API
    query_param = {"text": query_string}
    score = http_get_response(url=rapid_api_url, headers=api_headers, params=query_param)

    return score
