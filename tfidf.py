from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re

text_df = pd.read_csv('text.csv')

def pre_process(text):
    
    text=text.lower()
    text=re.sub("","",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    
    return text

text_df['document'] = text_df['document'].apply(lambda x: pre_process(x))

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(text_df['document'])

tfidf_df = pd.DataFrame(data=tfidf_vectors.toarray(), index=text_df['command'], columns=tfidf_vectorizer.get_feature_names_out())
tfidf_df.to_csv('tfidf.csv')