import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('population.csv', index_col='Rank')
print(df)
df = pd.read_csv('population.csv', header=None, skiprows=5)
print(df)