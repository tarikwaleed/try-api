import requests
import os
import json

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(), override=True)
api_key = os.getenv("API_KEY")

url="https://www.qoyod.com/api/2.0/products"

headers = {
    "API-KEY": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json",
}


try:
    response = requests.get(url, headers=headers)

    with open(
          "./resources/qoyod/all_products.json" , "w"
    ) as outfile:
        outfile.write(json.dumps(response.json()))
        # outfile.write(json.dumps(response.json()))


except Exception as e:
    raise e
