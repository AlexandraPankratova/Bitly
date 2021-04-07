import os

import requests
from dotenv import load_dotenv

load_dotenv()


def main():

    bitly_token = os.getenv("BITLY_TOKEN")
    headers = {
        "Authorization": bitly_token
    }
    response_get = requests.get("https://api-ssl.bitly.com/v4/user", headers=headers)

    url_to_shorten = {
        "long_url": "https://dvmn.org/modules/",
    }

    response_post = requests.post("https://api-ssl.bitly.com/v4/bitlinks", headers=headers, json=url_to_shorten)

    print(response_get.json())
    print(response_post.json()["id"])


if __name__ == "__main__":
    main()
    
