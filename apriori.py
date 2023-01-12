from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

association_df = pd.read_csv('association.csv')
association_df = association_df.astype(bool)

frequent_sets = apriori(association_df)
rules = association_rules(frequent_sets, metric="lift")

rules.to_csv('rules.csv')