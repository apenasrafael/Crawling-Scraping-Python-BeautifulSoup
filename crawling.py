import requests
from requests.exceptions import HTTPError


def crawl_site(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except HTTPError as exc:
        print(exc)
    else:
        return resposta.text
