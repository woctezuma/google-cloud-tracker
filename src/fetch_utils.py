import requests

from src.constants import TIMEOUT_IN_SECONDS
from src.env_utils import GOOGLE_BUCKET_NAME
from src.object_utils import sort_objects

MAX_NUM_RESULTS_PER_PAGE: int = 5000
BASE_URL: str = f"https://www.googleapis.com/storage/v1/b/{GOOGLE_BUCKET_NAME}/o?maxResults={MAX_NUM_RESULTS_PER_PAGE}"


def get_url(token: str | None = None) -> str:
    if token:
        return f"{BASE_URL}&pageToken={token}"
    return BASE_URL


def fetch_page(token: str | None = None) -> (list, str):
    response = requests.get(url=get_url(token), timeout=TIMEOUT_IN_SECONDS)
    data = response.json()
    page_objects = data.get("items", [])
    token = data.get("nextPageToken")
    return page_objects, token


def fetch_all_pages(*, sort_by_date: bool = True) -> list:
    counter = 0
    objects = []
    token = None
    while counter == 0 or token:
        page_objects, token = fetch_page(token)
        counter += 1
        objects += page_objects
        print(
            f"[{counter}] total #items: {len(objects)}, nextPageToken: {token}",
        )
    if sort_by_date:
        objects = sort_objects(objects)
    return objects
