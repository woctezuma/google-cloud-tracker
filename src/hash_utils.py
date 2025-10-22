from pathlib import Path

from src.constants import DATA_FOLDER, HASH_FIELD, LINE_SEP

HASH_FNAME: str = f"{DATA_FOLDER}{HASH_FIELD}.txt"


def to_hashes(objects: list) -> set[str]:
    return {obj[HASH_FIELD] for obj in objects}


def save_raw_hashes(hashes: set[str]) -> None:
    with Path(HASH_FNAME).open("w") as f:
        f.write(LINE_SEP.join(hashes))


def save_hashes(objects: list) -> None:
    hashes = to_hashes(objects)
    save_raw_hashes(hashes)


def load_hashes() -> set[str]:
    with Path(HASH_FNAME).open() as f:
        return set(f.read().splitlines())
