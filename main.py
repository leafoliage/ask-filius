import pandas as pd

commands_df = pd.read_csv('commands.csv')
tfidf_df = pd.read_csv('tfidf.csv')
rules_df = pd.read_csv('rules.csv')

def str_to_set(str):
    return frozenset(str.replace("frozenset({\'","").replace("\'})","").split("\', \'"))

def subset(s):
    subs = [[]]
    for el in s:
        subs += [sub+[el] for sub in subs]
    subs = [set(sub) for sub in subs]
    return subs

def search(query):
    res = [0] * len(tfidf_df.index)

    for word in query.split(' '):
        if word in tfidf_df.columns:
            res = res + tfidf_df[word]

    tfidf_score = [list(commands_df['command'][:len(tfidf_df.index)]), list(res)]

    tfidf_score_df = pd.DataFrame(data=tfidf_score, index=['command', 'score']).T

    first_draft = set(tfidf_score_df.sort_values(by='score', ascending=False)[:5]['command'])

    best_set = set()
    best_lift = 0
    for s in subset(first_draft):
        filtered = rules_df[rules_df['antecedents']==s].sort_values(by='lift', ascending=False)
        if len(filtered.index) == 0:
            continue
        top = filtered.iloc[0]
        if top['lift']>best_lift: 
            best_set = top['consequents']
            best_lift = top['lift']

    recommendation = list(first_draft)
    recommendation.extend(best_set.difference(first_draft))

    return recommendation

rules_df['antecedents'] = rules_df['antecedents'].apply(lambda x: str_to_set(x))
rules_df['consequents'] = rules_df['consequents'].apply(lambda x: str_to_set(x))

print("What command are you looking for?")
query = input("Try describe what the command does: ")
print("Hold on...")
recs = search(query)
print("These might be the command you're looking for: ")
for i, cmd in enumerate(recs):
    print(f"{i+1}. {cmd}")
