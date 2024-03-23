
import logging
from typing import Optional, Dict, Any
from config import RAPID_API_Key

import requests


# API URL endpoints
base_url = "http://localhost:8080/api/v1/"
rapid_api_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

# Request header for rapid API
api_headers = {
    "X-RapidAPI-Key": RAPID_API_Key,
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def http_get_response(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
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


class SubfedditNotFound(Exception):
    """Exception raised when a subfeddit is not found."""

    def __init__(self, message="Subfeddit not found."):
        self.message = message
        super().__init__(self.message)

class CommentsNotFound(Exception):
    """Exception raised when comments are not found."""

    def __init__(self, message="Comments not found."):
        self.message = message
        super().__init__(self.message)

