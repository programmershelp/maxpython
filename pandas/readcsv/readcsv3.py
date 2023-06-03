import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('population.csv', usecols =['Country/Territory','Capital','Continent'])
print(df)