import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

commands_df = pd.read_csv('commands.csv')

def extract_text(link):
    doc = ""
    try:
        r = requests.get(link)
    except requests.exceptions.ConnectionError:
        return doc
    bs = BeautifulSoup(r.text, "html.parser")
    for pre in bs.find_all('pre'):
        doc += pre.text
    for code in bs.find_all('code'):
        doc += code.text
    for span in bs.find_all('span'):
        doc += span.text
    for p in bs.find_all('p'):
        doc += p.text
    return doc


targets = []
for i in range(1,11):
    url = "https://stackoverflow.com/questions/tagged/linux?tab=newest&page=1&pagesize=10"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    targets.extend(bs.find_all(attrs={"class":"s-link"}))

corpus = []
for t in targets:
    if not t.attrs['href'][0] == '/':
        continue
    url = f"https://stackoverflow.com{t.attrs['href']}"
    corpus.append(extract_text(url))

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