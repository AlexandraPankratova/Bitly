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
    print("Битлинк", response.json()["id"])


def main():

    bitly_token = os.getenv("BITLY_TOKEN")
    
    url_to_shorten = "https://dvmn.org/modules/"

    shorten_link(bitly_token, url_to_shorten)



if __name__ == "__main__":
    main()
    
