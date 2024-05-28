# %% Import excel to dataframe
import pandas as pd

df = pd.read_excel("Online Retail.xlsx")


# %%  Show the first 10 rows
df.head(10)


# %% Generate descriptive statistics regardless the datatypes
df.describe(include='all')

# %% Remove all the rows with null value and generate stats again
df.dropna(inplace=True)
df.describe(include='all')


# %% Remove rows with invalid Quantity (Quantity being less than 0)
df = df[df['Quantity'] > 0]


# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
df = df[df['UnitPrice'] > 0]


# %% Only Retain rows with 5-digit StockCode
df = df[df['StockCode'].apply(lambda x: len(str(x)) == 5)]


# %% strip all description
df['Description'] = df['Description'].str.strip()


# %% Generate stats again and check the number of rows
print(df.describe(include='all'))
print('Number of rows:', len(df))


# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description
top20_selling_products = df['Description'].value_counts()[:20]
plt.figure(figsize=(10,6))
sns.barplot(y=top20_selling_products.index, x=top20_selling_products.values, orient='h')
plt.xlabel("Amount")
plt.ylabel("Product")
plt.title("Top 20 Selling Products")
plt.tight_layout()


# %% Focus on sales in UK
df_uk = df[df['Country'] == 'United Kingdom']


#%% Show gross revenue by year-month
from datetime import datetime
df_uk["YearMonth"] = df["InvoiceDate"].apply(lambda dt: datetime(year=dt.year, month=dt.month, day=1))
df_uk['Revenue'] = df_uk['Quantity'] * df_uk['UnitPrice']
revenue_by_month = df_uk.groupby('YearMonth')['Revenue'].sum()
print(revenue_by_month)


revenue_by_month = df_uk.groupby("YearMonth")["Revenue"].sum()
plt.figure(figsize=(12, 6))
sns.lineplot(x=revenue_by_month.index, y=revenue_by_month.values)
plt.xlabel("Year-Month")
plt.ylabel("Gross Revenue")
plt.title("Gross Revenue by Month and Year")
plt.xticks(rotation=45)
plt.show()

# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
df_uk[['InvoiceNo', 'StockCode', 'Description']].to_pickle('UK.pkl')

# %%
df = pd.read_pickle('UK.pkl')
print(df)

# %%
