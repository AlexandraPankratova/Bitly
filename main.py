import argparse
import os

import requests
from dotenv import load_dotenv


def check_url(token, url):
    headers = {
        "Authorization": token
    }
    response = requests.get(
            "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url),
            headers=headers,
    )
    return response.ok


def shorten_link(token, url):
    headers = {
        "Authorization": token,
    }
    payload = {
        "long_url": url,
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    decoded_response = response.json()
    bitlink = decoded_response["id"]
    return bitlink


def count_clicks(token, bitlink):
    headers = {
        "Authorization": token
    }
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(
            bitlink,
        ),
        headers=headers,
    )
    response.raise_for_status()
    decoded_response = response.json()
    return decoded_response["total_clicks"]


def main():

    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Программа создает битлинк длинной ссылки \
        или выводит кол-во кликов для битлинка"
    )
    parser.add_argument("url", help="Ссылка")
    entered_url = parser.parse_args().url

    bitly_token = os.getenv("BITLY_TOKEN")

    try:
        if check_url(bitly_token, entered_url):
            amount_of_clicks = count_clicks(bitly_token, entered_url)
            print("Было соверешено следующее количество кликов: {}.".format(
                amount_of_clicks,
            ))
        else:
            bitlink = shorten_link(bitly_token, entered_url)
            print("Битлинк {}.".format(bitlink))
    except requests.exceptions.HTTPError:
        print("Ссылка введена неверно.")


if __name__ == "__main__":
    main()
