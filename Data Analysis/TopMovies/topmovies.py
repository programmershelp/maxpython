import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import ast
# In case we want to ignore the warning parts @-@
import warnings
warnings.filterwarnings("ignore")

data= pd.read_csv('movies.csv')
print(data.head(3))


# Drop any duplicate records
data.drop_duplicates(inplace=True)
# drop the column called Unnamed: 0
data.drop('Unnamed: 0', axis=1,inplace=True)
# Replace values of Movie Runtime to an hourly value
runtime= data['Movie Runtime'].str.split(expand=True).iloc[:,[0,2]]
runtime[2].fillna(0,inplace=True)
runtime= runtime.astype('int64')
runtime['hour']= runtime[0]+runtime[2]/60
data['Movie Runtime']= runtime['hour']
# I want the Release Date to be a Datetime
data['Release Date']= pd.to_datetime(data['Release Date'])
# Replace some of column names as I don't like the (in $) part
data.rename(columns={'Domestic Sales (in $)':'Domestic Sales','International Sales (in $)':'International Sales',
                     'World Sales (in $)':'World Sales'}, inplace=True)
# I want to show some columns as millions of dollars
data[['Domestic Sales','International Sales','World Sales']]= data[['Domestic Sales',
                                            'International Sales','World Sales']].apply(lambda x: x/(10**6))
# The Genre column is a string of list, change this
data['Genre']= data['Genre'].apply(lambda x: ast.literal_eval(x))
# New dataset
print(data.head(3))

num_col= ['Domestic Sales', 'International Sales', 'World Sales','Movie Runtime']
cat_col= ['Title','Movie Info', 'Distributor','License','Genre']
date_col='Release Date'

#lets show the sales by year
year_data=data.copy()
year_data['year']=year_data['Release Date'].dt.year
year_data.dropna(subset=['year'],inplace=True)
fig,ax= plt.subplots(figsize=(15,15))
sns.barplot(x='year',y='Title',data=year_data.groupby('year',as_index=False)['Title'].count(),
           palette='viridis',edgecolor='black',ax=ax)
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel('Num of Movies')
ax.set_title('Number of Movies by each year 1972-2021', fontsize=15);
plt.show()

#lets show the movies by genre
Genre= []
for i in range(data.shape[0]):
    Genre.extend(data.loc[i,'Genre'])
Genre[:7]
pd.Series(Genre).unique()

def subset_genre(g):
    mask=data['Genre'].apply(lambda x: g in x)
    return data[mask]

genre_data= pd.DataFrame({'genre':pd.Series(Genre).unique()})
genre_data['num_movie']= genre_data['genre'].apply(lambda g: subset_genre(g).shape[0])
genre_data['average_sale']= genre_data['genre'].apply(lambda g: subset_genre(g)['World Sales'].mean())
genre_data['total_sale']= genre_data['genre'].apply(lambda g: subset_genre(g)['World Sales'].sum())
genre_data

fig,ax= plt.subplots(figsize=(15,15))
sns.barplot(x='genre', y='num_movie', data=genre_data.sort_values('num_movie', ascending=False)
            , palette='mako', edgecolor='black', ax=ax)
ax.tick_params(axis='x', labelrotation=90)
ax.set_title('Number of Movies by Genres', fontsize=15);
plt.show()

#Average movie sales
fig,ax= plt.subplots(figsize=(15,5))
sns.lineplot(data=year_data.groupby('year')[num_col[:-1]].mean(),
           palette='rocket',lw=2.5,ax=ax)
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel('Average of Sale')
ax.set_title('Average Movie Sales 1972-2021', fontsize=15);
plt.show()