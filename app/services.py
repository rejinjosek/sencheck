"""
This contains the following services:
- Fetch data from subfeddit API
- Search for subfeddit with given title
- Fetch comments of the given subfeddit ID

"""

from urllib.parse import urljoin
from typing import List, Optional, Dict, Any

from utils import http_get_response, base_url, rapid_api_url, api_headers


def _get_subfeddits(skip_records: Optional[int] = None, limit_records: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Fetches subfeddits from the API.

    Args:
        skip_records (int): Number of records to skip.
        limit_records (int): Maximum number of records to fetch.

    Returns:
        List[Dict[str, Any]]: List of subfeddits.
    """
    path_params = "subfeddits/"
    if skip_records is not None and limit_records is not None:
        path_params = f"subfeddits/?skip={skip_records}&limit={limit_records}"
        
    response = http_get_response(urljoin(base_url, path_params))
    if response:
        return response.get('subfeddits', "Feddit API returned an empty response")
    return "Connection to Subfeddit API failed"

def get_subfeddit_by_title(subfeddit_title: str, skip_records: Optional[int]=None, limit_records: Optional[int]=None) -> Optional[Dict[str, Any]]:
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
    if len(subfeddits) == 0 or isinstance(subfeddits, str):
        return subfeddits

    title_dict = {each_subfeddit['title']: each_subfeddit for each_subfeddit in subfeddits}
    return title_dict.get(subfeddit_title, "Title not found")    

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
        return subfeddit.get('comments', "Feddit API send an empty response")
    return "Connection to Feddit API Failed"


class SentimentAnalyzer:
    def _get_score_from_twinword(self, query_string):
        # Get score using twinword API
        query_param = {"text":query_string}
        score = http_get_response(url=rapid_api_url, headers=api_headers, params=query_param)

        return score    

    def _get_comment_scores(self, comments:List[Dict], sort_by_scores:bool):
        comment_scores = []
        for comment in comments:
            text = comment.get('text')
            if text:
                score_data = self._get_score_from_twinword(text)
                if score_data and 'type' in score_data and 'score' in score_data:
                    score_info = {
                        'id':comment.get('id'),
                        'text': text,
                        'type': score_data.get('type'),
                        'score': score_data.get('score'),
                        'created_at':comment.get('created_at')
                    }
                    comment_scores.append(score_info)
                else:
                    # Handle case where score data is missing or incomplete
                    print(f"Unable to get score for comment: {text}")
                    score_info = {'id':comment.get('id'),'text': text, 'type': None, 'score': None}
                    comment_scores.append(score_info)
        if sort_by_scores:
            return self._sort_comments_by_score(comment_scores)
        return comment_scores

    def _sort_comments_by_score(self, list_of_comments:List[Dict]):
        #Sort comments based on scores
        return sorted(list_of_comments, key=lambda x: x['score'], reverse=True)

    def get_scores(self, subfeddit_title:str, skip_records:int=0, limit_records:int=25, sort_by_scores:bool=False):
        """
        Get sentiment score for each comment
        
        Args:
            subfeddit_title(str): Title of the subfeddit.
            skip_records (int): Number of records to skip.
            limit_records (int): Maximum number of records to fetch.
            sort_by_scores(bool): Sor the results based on scores

        Returns:
            List[Dict: List comments with ID, score and created timestamp]
        """
        subfeddit = get_subfeddit_by_title(subfeddit_title=subfeddit_title)
        if isinstance(subfeddit, str):
            # Return the error message
            return subfeddit
        
        comments = get_comments_by_id(subfeddit_id=subfeddit['id'],skip_records=skip_records,limit_records=limit_records)
        if isinstance(comments, str):
            # Return the error message
            return comments
        
        return self._get_comment_scores(comments, sort_by_scores)
