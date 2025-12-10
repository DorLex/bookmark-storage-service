import requests

from .headers import get_headers


def get_page_html(link: str) -> str:
    headers = get_headers()
    response = requests.get(link, headers=headers)

    return response.text
