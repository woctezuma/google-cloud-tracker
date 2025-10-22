import time

import requests

from src.batch_utils import chunks
from src.constants import TIMEOUT_IN_SECONDS
from src.env_utils import DISCORD_WEBHOOK
from src.message_utils import object_batch_to_message

DISCORD_API_URL: str = "https://discord.com/api/webhooks/"
BATCH_SIZE: int = 5
SLEEP_DURATION_IN_SECONDS: int = 1


def get_webhook_url(webhook_id: str) -> str:
    return f"{DISCORD_API_URL}{webhook_id}"


def post_message_to_discord(message: str, webhook_id: str) -> requests.Response | None:
    if webhook_id is None or not message:
        response = None
    else:
        json_data = {"content": message}
        response = requests.post(
            url=get_webhook_url(webhook_id),
            json=json_data,
            timeout=TIMEOUT_IN_SECONDS,
        )

    return response


def notify_discord_for_a_single_batch(objs: list) -> None:
    message = object_batch_to_message(objs)
    post_message_to_discord(message, webhook_id=DISCORD_WEBHOOK)


def notify_discord(new_objects: list) -> None:
    num_batches = 1 + len(new_objects) // BATCH_SIZE

    for counter, objs in enumerate(chunks(new_objects, BATCH_SIZE), start=1):
        notify_discord_for_a_single_batch(objs)
        print(f"Posted batch {counter}/{num_batches} with {len(objs)} objects.")
        time.sleep(SLEEP_DURATION_IN_SECONDS)
