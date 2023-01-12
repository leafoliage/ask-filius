import requests
from dotenv import dotenv_values
import json
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

config = dotenv_values(".env")
commands_df = pd.read_csv('commands.csv')

def extract_links(response):
    j = response.json()
    text = json.dumps(j)
    return text.replace("{\"items\": [{\"link\": \"", "").replace("\"}]}", "").split("\"}, {\"link\": \"")

def extract_text(link):
    bs = BeautifulSoup(requests.get(link).text, "html.parser")
    doc = ""
    for pre in bs.find_all('pre'):
        doc += pre.text
    for code in bs.find_all('code'):
        doc += code.text
    for span in bs.find_all('span'):
        doc += span.text
    for p in bs.find_all('p'):
        doc += p.text
    return doc

def search(site):
    q = "linux"
    fields = "items/link"
    url = f"https://www.googleapis.com/customsearch/v1?cx={config['SE_ID']}&key={config['API_KEY']}&q={q}&fields={fields}&siteSearch={site}"
    r = requests.get(url)
    links = extract_links(r)

    corpus = []
    for link in links:
        corpus.append(extract_text(link))

    return corpus

corpus = []
corpus.extend(search("stackoverflow.com"))
    
vectorizer = CountVectorizer(binary=True)
vecs = vectorizer.fit_transform(corpus)
df = pd.DataFrame(data=vecs.toarray(), columns=vectorizer.get_feature_names_out())

association_df = pd.DataFrame()
for cmd in commands_df['command']:
    if cmd in df.columns:
        association_df[cmd] = df[cmd]
    else:
        association_df[cmd] = [0] * len(df.index)

association_df.to_csv('association.csv', index=False)