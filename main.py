import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def check_url(url):
    return urlparse(url).scheme == ""


def shorten_link(token, url):
    headers = {
        "Authorization": token
    }
    long_url = {
        "long_url": url
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=long_url,
    )
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(token, bitlink):
    headers = {
        "Authorization": token
    }
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(
            bitlink
        ),
        headers=headers,
    )
    return response.json()["total_clicks"]


def main():

    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Программа создает битлинк длинной ссылки \
        или выводит кол-во кликов для битлинка"
    )
    parser.add_argument('url', help="Ссылка")
    entered_url = parser.parse_args().url

    bitly_token = os.getenv("BITLY_TOKEN")

    try:
        if check_url(entered_url):
            amount_of_clicks = count_clicks(bitly_token, entered_url)
            print("Было соверешено следующее количество кликов: {}.".format(
                amount_of_clicks
            ))
        else:
            bitlink = shorten_link(bitly_token, entered_url)
            print("Битлинк {}.".format(bitlink))
    except KeyError:
        print("Ссылка введена неверно.")


if __name__ == "__main__":
    main()
