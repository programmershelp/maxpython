# imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data vislization using plolty graph object(go)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import iplot
import plotly.io as pio
import plotly.express as px

# For showing plotly plots on notebook
import plotly.offline as py
from plotly.offline import init_notebook_mode
#py.init_notebook_mode()

df = pd.read_csv('world_population.csv')
#data analysis
print(df.head())
print(df.shape)
# Checking if there any missing values are in the data
print(df.isnull().sum())
# checking the duplicates
print(df.duplicated().sum())
colors = ["#1d7874","#679289","#f4c095","#ee2e31","#ffb563","#918450","#f85e00","#a41623","#9a031e","#d6d6d6","#ffee32","#ffd100","#333533","#202020"]



sns.set(rc={"axes.facecolor":"#F2EAC5","figure.facecolor":"#F2EAC5"})
plt.subplots(figsize=(20, 10))
p=sns.barplot(data=df[df["Continent"]=="Europe"],y="Country/Territory", x="2022 Population",order=df[df["Continent"]=="Europe"].sort_values("2022 Population",ascending=False)["Country/Territory"][:11],palette=colors[0:11:2], saturation=1,edgecolor = "#1c1c1c", linewidth = 4)
p.axes.set_title("\nEuropean Population 2022\n",fontsize=25)
p.axes.set_xlabel("Population",fontsize=20)
p.axes.set_ylabel("\nCountry",fontsize=20)
p.axes.set_xticklabels(p.get_xticklabels(),rotation = 90)
for container in p.containers:
    p.bar_label(container,label_type="edge",padding=6,size=25,color="black",rotation=0,
    bbox={"boxstyle": "round", "pad": 0.4, "facecolor": "orange", "edgecolor": "#1c1c1c", "linewidth" : 2, "alpha": 1})

sns.despine(left=True, bottom=True)
plt.show()