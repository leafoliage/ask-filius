import requests
from dotenv import dotenv_values
import json
from bs4 import BeautifulSoup
import pandas as pd

config = dotenv_values(".env")
commands_df = pd.read_csv('commands.csv')

def extract_links(response):
    j = response.json()
    text = json.dumps(j)
    return text.replace("{\"items\": [{\"link\": \"", "").replace("\"}]}", "").split("\"}, {\"link\": \"")

def extract_text(link):
    bs = BeautifulSoup(requests.get(link).text, "html.parser")
    doc = ""
    for h1 in bs.find_all('h1'):
        doc += h1.text
    for h2 in bs.find_all('h2'):
        doc += h2.text
    for h3 in bs.find_all('h3'):
        doc += h3.text
    for p in bs.find_all('p'):
        doc += p.text
    return doc

def process(command):
    q = "linux command" + command
    fields = "items/link"
    url = f"https://www.googleapis.com/customsearch/v1?cx={config['SE_ID']}&key={config['API_KEY']}&q={q}&fields={fields}"
    r = requests.get(url)
    links = extract_links(r)
    docs = ""
    for link in links:
        docs += extract_text(link)
    return docs

data = []
for cmd in commands_df['command']:
    data.append([cmd, process(cmd)])
    print(f" {cmd} finished \x1b[1A")
text_df = pd.DataFrame(data=data, columns=['command', 'document'])
text_df.to_csv('text.csv', index=False)
print('\x1b[2K')
print('job done')