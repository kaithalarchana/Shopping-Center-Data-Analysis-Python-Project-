import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\Dell\Downloads\unclean_shopping_center_data_1000x10.xlsx")
df

df.shape       #.shape function show how many rows and columns in data.

df.info()

df.isnull().sum() #.isnull() represented the null values in data.

df.head() #.head show the strating five rows data.

df.tail()
df

df drop_duplicates()  # it is delete the duplicaes rows present in data.

df_clean = df.dropna()
df

num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df
cat_cols = df.select_dtypes(include=['object']).columns

for col in cat_cols:
df[col] = df[col].fillna(df[col].mode()[0])
df

df['Opening_Year'] = pd.to_numeric(df['Opening_Year'], errors='coerce')
df['Opening_Year'] = df['Opening_Year'].fillna(df['Opening_Year'].median())
df

df.describe()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with pd.ExcelWriter(r'C:\Users\Dell\Desktop\projectfile.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

plt.figure(figsize=(8,5))    # 1) Histogram — Monthly Sales
plt.hist(df['Monthly_Sales'].dropna(), bins=20)
plt.title("Distribution of Monthly Sales")
plt.xlabel("Monthly Sales")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))     # 2) Boxplot-Monthly Sales (ti detect outliers)
plt.boxplot(df['Monthly_Sales'].dropna())
plt.title("Boxplot of Monthly Sales")
plt.ylabel("Monthly Sales")
plt.show()

avg_sales = df.groupby('Category')['Monthly_Sales'].mean() # 3) Bar Chart — Average Sales by Category

plt.figure(figsize=(8,5))
avg_sales.plot(kind='bar')
plt.title("Average Monthly Sales by Category")
plt.xlabel("Category")
plt.ylabel("Average Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))   # 4) Seaborn Histogram + KDE (Sales Distribution)
sns.histplot(df['Monthly_Sales'].dropna(), kde=True)
plt.title("Monthly Sales Distribution")
plt.show()

plt.figure(figsize=(8,5))  # 5) Seaborn Boxplot — Category vs Sales
sns.boxplot(x='Category', y='Monthly_Sales', data=df)
plt.xticks(rotation=45)
plt.title("Category vs Monthly Sales")
plt.show()

plt.figure(figsize=(8,5)) # 6) Seaborn Barplot — Floor vs Average Sales
sns.barplot(x='Floor_No', y='Monthly_Sales', data=df)
plt.title("Floor vs Monthly Sales")
plt.show()

plt.figure(figsize=(8,5)) # OPTIONAL: Heatmap of Missing Values
sns.heatmap(df.isnull(), cmap="viridis", cbar=False)
plt.title("Missing Values Heatmap")
plt.show()

