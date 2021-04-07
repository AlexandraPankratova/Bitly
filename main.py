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


def main():

    parser = argparse.ArgumentParser(
        description="Программа создает битлинк длинной ссылки"
    )
    parser.add_argument('url', help="Ссылка, которую требуется сократить")
    url_to_shorten = parser.parse_args().url

    bitly_token = os.getenv("BITLY_TOKEN")

    try:
        bitly_link = shorten_link(bitly_token, url_to_shorten)
        print("Битлинк", bitly_link)
    except KeyError:
        print("Ссылка введена неверно.")    

    
if __name__ == "__main__":
    main()
