from src.discord_utils import notify_discord
from src.fetch_utils import fetch_all_pages
from src.hash_utils import load_hashes, save_hashes
from src.object_utils import find_new_objects, save_objects


def check_for_updates(*, debug: bool = False) -> None:
    print("Fetching objects")
    objects = fetch_all_pages(sort_by_date=True)

    print("Loading hashes from disk")
    try:
        hashes = load_hashes()
    except FileNotFoundError:
        hashes = {}

    if debug:
        print("Saving objects to disk")
        save_objects(objects)

    print("Saving hashes to disk")
    save_hashes(objects)

    if hashes:
        print("Finding new objects based on previously loaded hashes")
        new_objects, _ = find_new_objects(objects, hashes)

        if new_objects:
            print("Sending messages about new objects to Discord")
            notify_discord(new_objects)


if __name__ == "__main__":
    check_for_updates()
