import json
from pathlib import Path

from src.constants import DATA_FOLDER, TIME_FIELD

DATA_FNAME: str = f"{DATA_FOLDER}bucket_data.json"
INDENT_LENGTH: int = 2


def sort_objects(objects: list, sort_field: str = TIME_FIELD) -> list:
    return sorted(objects, key=lambda x: x[sort_field])


def save_objects(objects: list) -> None:
    with Path(DATA_FNAME).open("w") as f:
        json.dump(objects, f, indent=INDENT_LENGTH)


def load_objects(*, sort_by_date: bool = True) -> list:
    with Path(DATA_FNAME).open() as f:
        objects = json.load(f)
    if sort_by_date:
        objects = sort_objects(objects)
    return objects
