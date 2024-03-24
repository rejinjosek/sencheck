# Sentiment Analysis API 

## Overview

This API provides sentiment analysis scores for comments within a subreddit (referred to as 'subfeddit'). The sentiment scores help in understanding the general sentiment of the comments in a particular subreddit.

## Endpoints

### Get Sentiment Scores
#### `GET /scores/`

This endpoint retrieves sentiment scores for comments within a specified subreddit.

#### Parameters
- `subfeddit_title` (required): The title of the subreddit for which sentiment scores are requested.
- `skip_records` (optional): Number of records to skip. Defaults to 0.
- `limit_records` (optional): Maximum number of records to return. Defaults to 25.
- `sort_by_scores` (optional): Whether to sort the results by sentiment scores. Defaults to `False`.

#### Response
- **200 OK**: Returns a list of sentiment scores for comments in the specified subreddit.
- **404 Not Found**: If the specified subreddit title is invalid or not found.
- **500 Internal Server Error**: If any unexpected error occurs.

#### Example
```http
GET /scores/?subfeddit_title=science&skip_records=10&limit_records=5&sort_by_scores=true

#### Example Response

```json
[
  {
    "id": 303571,
    "text": "It looks great!",
    "type": "positive",
    "score": 0.797954407,
    "created_at": 1711182014
  },
  {
    "id": 303572,
    "text": "Love it.",
    "type": "positive",
    "score": 0.917220858,
    "created_at": 1711178414
  },
  {
    "id": 303573,
    "text": "Awesome.",
    "type": "positive",
    "score": 0.823558987,
    "created_at": 1711174814
  }
]