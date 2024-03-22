"""
This contains the following services:
- Fetch data from subfeddit API
- Search for subfeddit with given title
- Fetch comments of the given subfeddit ID

"""

from urllib.parse import urljoin
from typing import List, Optional, Dict, Any

from utils import http_get_response, base_url, rapid_api_url, api_headers


def _get_subfeddits(skip_records: int = 0, limit_records: int = 25) -> List[Dict[str, Any]]:
    """
    Fetches subfeddits from the API.

    Args:
        skip_records (int): Number of records to skip.
        limit_records (int): Maximum number of records to fetch.

    Returns:
        List[Dict[str, Any]]: List of subfeddits.
    """
    path_params = f"subfeddits/?skip={skip_records}&limit={limit_records}"
    response = http_get_response(urljoin(base_url, path_params))
    if response:
        return response.get('subfeddits', [])
    return []

def get_subfeddit_by_title(subfeddit_title: str, skip_records: int = 0, limit_records: int = 25) -> Optional[Dict[str, Any]]:
    """
    Searches for a subfeddit with the given title.

    Args:
        subfeddit_title (str): Title of the subfeddit to search for.
        skip_records (int): Number of records to skip.
        limit_records (int): Maximum number of records to fetch.

    Returns:
        Optional[Dict[str, Any]]: Subfeddit with the given title, if found.
    """
    subfeddits = _get_subfeddits(skip_records=skip_records, limit_records=limit_records)
    title_dict = {each_subfeddit['title']: each_subfeddit for each_subfeddit in subfeddits}
    return title_dict.get(subfeddit_title)

def get_comments_by_id(subfeddit_id: int, skip_records: int = 0, limit_records: int = 25) -> List[Dict[str, Any]]:
    """
    Fetches comments of the given subfeddit ID.

    Args:
        subfeddit_id (int): ID of the subfeddit whose comments to fetch.
        skip_records (int): Number of records to skip.
        limit_records (int): Maximum number of records to fetch.

    Returns:
        List[Dict[str, Any]]: List of comments of the given subfeddit ID.
    """
    path_params = f"comments/?subfeddit_id={subfeddit_id}&skip={skip_records}&limit={limit_records}"
    subfeddit = http_get_response(urljoin(base_url, path_params))
    if subfeddit:
        return subfeddit.get('comments', [])
    return []
