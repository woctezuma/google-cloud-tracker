from pathlib import Path

from src.constants import DATA_FOLDER, HASH_FIELD, LINE_SEP, TIME_FIELD

HASH_FNAME: str = f"{DATA_FOLDER}{HASH_FIELD}.txt"


def to_hashes(objects: list) -> dict[str, str]:
    return {obj[HASH_FIELD]: obj[TIME_FIELD] for obj in objects}


def save_raw_hashes(hashes: dict[str, str]) -> None:
    with Path(HASH_FNAME).open("w") as f:
        f.write(LINE_SEP.join(hashes.keys()))


def save_hashes(objects: list) -> None:
    hashes = to_hashes(objects)
    save_raw_hashes(hashes)


def load_hashes() -> dict[str, None]:
    with Path(HASH_FNAME).open() as f:
        return dict.fromkeys(f.read().splitlines())
