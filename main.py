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

    print(response_get.text)


if __name__ == "__main__":
    main()
    
