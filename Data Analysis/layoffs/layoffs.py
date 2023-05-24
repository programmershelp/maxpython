import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import seaborn as sns
import plotly.express as px 
import warnings

df = pd.read_csv('layoffs.csv')
#show the data
print(df.head())
print(df.describe().T)

#any empty data
print(df.isna().sum())

#fill empty values
df['total_laid_off'] = df['total_laid_off'].fillna(0)
df['percentage_laid_off'] = df['percentage_laid_off'].fillna(0)
df['stage'] = df['stage'].fillna(0)
df['funds_raised'] = df['funds_raised'].fillna(0)
df['industry'] = df['industry'].fillna(0)
#show the data
print(df.head())
print(df.describe().T)
#any empty data
print(df.isna().sum())
# layoffs should be whole numbers not floats
df.total_laid_off = df.total_laid_off.astype(int)

#top 10 companies by layoff numbers
df.groupby('company').total_laid_off.sum().sort_values(ascending=False)[:10]
fig = px.bar(df.groupby('company').total_laid_off.sum().sort_values(ascending=False)[:10],text_auto=True,title='Top 10 companies that laid off from 2020 to 2022',
      labels={"x":"Company","y":"Layoffs"})
fig.show()

#top sectors
sectors = np.array(df.groupby('industry')['total_laid_off'].sum().sort_values(ascending=False).head())
arr = np.array(['transportation','Consumer','Retail','Finance','Food'])
plt.figure(figsize= (8 ,6))
plt.bar(arr,sectors)
plt.xlabel('Sectors',fontdict={'size':12,'color':'orange'})
plt.ylabel('count',fontdict={'size':12,'color':'orange'})
plt.title('Top Sectors by layoffs',fontdict={'size':18,'color':'orange'})
plt.show()

#top countries
data = df.copy()
country_data = data.groupby('country').sum()['total_laid_off'].sort_values(ascending=False).iloc[:15]

fig = px.bar(country_data, text_auto='.2s',
             labels={
                     "country": "Countries",
                     "value": "No. of downsized employees"
                     },template="plotly_white")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.update_xaxes(tickangle=90)
fig.update_layout(height=700,
                  title="15 countries with the highest levels of workforce downsizing"
                  ,showlegend=False)
fig.show()

