import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Top500Songs.csv",sep=",", encoding='Latin-1')

print(df.head())
print(df.tail())
# checking null values if exist
df.isnull().sum()
# modify a few columns
df['position']=df['position'].str[3:]
df['Year']=df['released'].str[-4:]
df['streaklg']=df['streak'].str[:-6]
print(df.head())

#top songs
df_top=df.groupby('Year').count().reset_index()
df_top
plt.figure(figsize=(20,10))
plt.bar(df_top['Year'],df_top['title'])
plt.xticks(rotation = 'vertical')
plt.xlabel('Years')
plt.ylabel('Recurrences')
plt.title('Numbers of Top Song By Year')
plt.show()

#top artists
df_artists =df.groupby('artist').count().sort_values(by='description',ascending = False).reset_index()
df_artists = df_artists[:10]

plt.figure(figsize=(15,8))
plt.pie(df_artists['title'],labels = df_artists['artist'],autopct='%.2f',shadow=True)
plt.title("Top Artists")

j=0
for i in df_artists['artist']:
    print("The",j+1,"Artist is :",df_artists['artist'][j])
    j=j+1
plt.show()

#top writers
df_writers=df.groupby('writers').count().sort_values(by='description',ascending = False).reset_index()
df_writers = df_writers[:10]
plt.figure(figsize=(15,8))
plt.pie(df_writers['title'],labels = df_writers['writers'], autopct = "%.2f",shadow = True)
plt.title("Top Writers")

j=0
for i in df_writers['writers']:
    print("The",j+1,"Writer is :",df_writers['writers'][j])
    j=j+1
plt.show()

#top producers
df_producers = df.groupby('producer').count().sort_values(by='description',ascending = False).reset_index()
df_producers = df_producers[:10]
plt.figure(figsize=(15,8))
plt.pie(df_producers['title'],labels = df_producers['producer'],autopct = '%.2f',shadow = True)
plt.title("Top Producers")
j=0
for i in df_producers['producer']:
    print("The",j+1,"Producer is :",df_producers['producer'][j])
    j=j+1
plt.show()