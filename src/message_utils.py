from src.constants import HASH_FIELD, LINE_SEP, TIME_FIELD
from src.env_utils import GOOGLE_BUCKET_NAME

BULLET_POINT_SEP = "- "
ITEM_SEP = f"{LINE_SEP}{BULLET_POINT_SEP}"
DATE_LENGTH = len("2001-01-01T00:00")

DISPLAY_URL = f"https://storage.googleapis.com/{GOOGLE_BUCKET_NAME}/"

NAME_FIELD = "name"
CONTENT_FIELD = "contentType"
SIZE_FIELD = "size"


def concatenate_lines(lines: list[str]) -> str:
    return ITEM_SEP + ITEM_SEP.join(lines) + LINE_SEP


def object_to_sentences(obj: list) -> list[str]:
    return [
        f"URL: {DISPLAY_URL}{obj[NAME_FIELD]}",
        f"Created at: {obj[TIME_FIELD][:DATE_LENGTH]}",
        f"Content-Type: {obj[CONTENT_FIELD]}",
        f"Size: {obj[SIZE_FIELD]} bytes",
        f"Hash: {obj[HASH_FIELD]}",
    ]


def object_to_message(obj: list) -> str:
    return concatenate_lines(object_to_sentences(obj))


def object_batch_to_message(objs: list) -> str:
    messages = [object_to_message(obj) for obj in objs]
    return f"{LINE_SEP}{LINE_SEP}".join(messages)
