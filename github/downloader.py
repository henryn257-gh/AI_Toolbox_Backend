import requests

from config.settings import CONTENT_BASE_URL


def validate_path(path: str):

    if ".." in path:
        raise ValueError(
            "Invalid path"
        )

    if path.startswith("/"):
        raise ValueError(
            "Invalid path"
        )


def download(path: str):

    validate_path(path)

    url = (
        f"{CONTENT_BASE_URL}/{path}"
    )

    response = requests.get(
        url,
        headers={
            "Accept-Encoding": "gzip"
        }
    )

    response.raise_for_status()

    return response.content
