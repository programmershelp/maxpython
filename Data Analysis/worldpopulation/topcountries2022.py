# imports
import pandas as pd
import numpy as np

# Data vislization using plolty graph object(go)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import iplot
import plotly.io as pio

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

top_pop = df.sort_values(by = '2022 Population', ascending = False).head(10)
print(top_pop[['Country/Territory', '2022 Population']])

data = go.Bar(x = top_pop['Country/Territory'], y = top_pop['2022 Population'], text = top_pop['2022 Population'],textposition ='outside',
              textfont = dict(size = 30,
                             color = 'black'),
              marker = dict(color = colors,
                            opacity = 0.7,
                            line_color = 'black',
                            line_width = 2))
layout = go.Layout(title = {'text': "<b>Top 10 Countries with highest population</b>",
                           'x':0.5,
                           'xanchor': 'center'},
                   xaxis = dict(title='Countries' ),
                   yaxis =dict(title='Populations'),
                   width = 900,
                   height = 600,
                   template = 'plotly_white')
fig=go.Figure(data = data, layout = layout)

iplot(fig)