import requests
import os
from dotenv import dotenv_values

config = dotenv_values(".env")
query = "go"

url = f"https://www.googleapis.com/customsearch/v1?cx={config['SE_ID']}&key={config['API_KEY']}&q={query}"
r = requests.get(url)
print('request finished')
json = r.json()
for res in json.item:
    print(res.html)