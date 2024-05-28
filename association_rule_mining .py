# %% import dataframe from pickle file
import pandas as pd

df = pd.read_pickle("UK.pkl")

df.head()


# %% convert dataframe to invoice-based transactional format
transactions = df.groupby('InvoiceNo')['Description'].apply(list).reset_index(name='Items')
transactions_list = transactions['Items'].tolist()


# %% apply apriori algorithm to find frequent items and association rules
from setuptools import distutils
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

te = TransactionEncoder()
te_ary = te.fit(transactions_list).transform(transactions_list)
df_transactions = pd.DataFrame(te_ary, columns=te.columns_)

frequent_items = apriori(df_transactions, min_support=0.01, use_colnames=True)
print(frequent_items)

rules = association_rules(frequent_items, metric="lift", min_threshold=1)
print(rules)


# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items
frequent_items['num_items'] = frequent_items['itemsets'].apply(lambda x: len(x))
print("Count of frequent itemsets with more than 1 item:", frequent_items[frequent_items['num_items'] > 1].shape[0])
print("Count of frequent itemsets with more than 2 items:", frequent_items[frequent_items['num_items'] > 2].shape[0])
print("Count of frequent itemsets with more than 3 items:", frequent_items[frequent_items['num_items'] > 3].shape[0])
print("Frequent itemsets with the most items:")
print(frequent_items[frequent_items['num_items'] == frequent_items['num_items'].max()])




# %% top 10 lift association rules
print("Top 10 lift association rules:")
print(rules.sort_values(by='lift', ascending=False).head(10))

# %% scatterplot support vs confidence
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["confidence"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Support vs Confidence")
plt.show()

# %% scatterplot support vs lift

sns.scatterplot(x=rules["support"], y=rules["lift"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Lift")
plt.title("Support vs Lift")
plt.show()
# %%
