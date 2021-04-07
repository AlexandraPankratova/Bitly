import argparse
import os

import requests
from dotenv import load_dotenv

load_dotenv()

def shorten_link(token, url):
    headers = {
        "Authorization": token
    }
    long_url = {
        "long_url": url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/bitlinks", headers=headers, json=long_url)
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(token, bitlink):
    headers = {
        "Authorization": token
    }
    response = requests.get("https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(bitlink), headers=headers)
    return response.json()["total_clicks"]

def main():

    parser = argparse.ArgumentParser(
        description="Программа создает битлинк длинной ссылки"
    )
    parser.add_argument('url', help="Ссылка, которую требуется сократить")
    url_to_shorten = parser.parse_args().url

    bitly_token = os.getenv("BITLY_TOKEN")

    try:
        bitlink = shorten_link(bitly_token, url_to_shorten)
        print("Битлинк {}.".format(bitlink))
        amount_of_clicks = count_clicks(bitly_token, bitlink)
        print("По данному битлинку было соверешно следующее количество кликов: {}.".format(amount_of_clicks))
    except KeyError:
        print("Ссылка введена неверно.")

    
    
if __name__ == "__main__":
    main()
