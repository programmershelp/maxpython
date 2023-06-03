import pandas as pd

# Read CSV file into DataFrame
columns = ['rank','code','capital','continent' ,'population','area', 'density','growth', 'percentage']
df = pd.read_csv('population.csv', usecols =['code','capital','population'])
print(df)