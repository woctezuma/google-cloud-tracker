from src.discord_utils import notify_discord
from src.fetch_utils import fetch_all_pages
from src.hash_utils import load_hashes, save_hashes
from src.object_utils import find_new_objects, save_objects


def check_for_updates(*, debug: bool = False) -> None:
    objects = fetch_all_pages(sort_by_date=True)

    try:
        hashes = load_hashes()
    except FileNotFoundError:
        hashes = set()

    if debug:
        save_objects(objects)

    save_hashes(objects)

    if hashes:
        new_objects, _ = find_new_objects(objects, hashes)

        if new_objects:
            notify_discord(new_objects)


if __name__ == "__main__":
    check_for_updates()
