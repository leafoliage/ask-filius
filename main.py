import pandas as pd

commands_df = pd.read_csv('commands.csv')
tfidf_df = pd.read_csv('tfidf.csv')
rules_df = pd.read_csv('rules.csv')

query = "list directory content"

def subset(s):
    subs = [[]]
    for el in s:
        subs += [sub+[el] for sub in subs]
    return subs

res = [0] * len(tfidf_df.index)

for word in query.split(' '):
    if word in tfidf_df.columns:
        res = res + tfidf_df[word]

res = res

tfidf_score = [list(commands_df['command'][:len(tfidf_df.index)]), list(res)]

tfidf_score_df = pd.DataFrame(data=tfidf_score, index=['command', 'score']).T

first_draft = set(tfidf_score_df.sort_values(by='score', ascending=False)[:5]['command'])

best_set = set()
best_lift = 0
for s in subset(first_draft):
    top = rules_df[rules_df['antecedents']==s].sort_values(by='lift', ascending=False)[0]
    if top['lift']>best_lift: 
        best_set = top['consequence']
        best_lift = top['lift']

recommendation = list(first_draft)
recommendation.extend(list(best_set))

print(recommendation)