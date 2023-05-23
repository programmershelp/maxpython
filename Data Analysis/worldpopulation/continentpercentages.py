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

cont_pop = df.groupby('Continent',)[['World Population Percentage']].sum().sort_values(by = 'World Population Percentage', ascending = False)
cont_pop
fig = go.Figure(data = go.Pie(labels = cont_pop.index, values = cont_pop['World Population Percentage'].values))
fig.update_traces(hoverinfo='label',
                  hole = 0.4,
                  textfont_size = 18,
                  textposition ='auto',
                  marker=dict(colors = colors,
                              line = dict(color = 'white',
                                          width = 2)))
fig.update_layout(title ={'text' : '<b>Continent Population Percentage</b>', 
                          'x' : 0.21},
                          template = 'xgridoff',
                          width = 900, height = 600,
                     legend=dict(
                        title_font_family="Times New Roman",
                        font=dict(
                        family="Courier",
                        size=20,
                        color="black" 
                        ),
                        bgcolor="white",
                        bordercolor="Black",
                        borderwidth=2.5)
                 )
iplot(fig)