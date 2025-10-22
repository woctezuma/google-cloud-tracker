from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def chunks(lst: list, n: int) -> Generator[list]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]
