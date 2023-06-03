import pandas as pd

population = {
    'Country':["Cameroon","Canada","Colombia","France"],
    'Capital':["Yaounde","Ottawa","Bogota","Paris"],
    'Continent':["Africa","North America","South America","Europe"],
    'Population':[27914536,38454327,51874024,64626628]
          }
df = pd.DataFrame(population)
print(df)
df.to_csv("countries.csv")
df.to_csv("countries1.csv", header=False)
df.to_csv("countries2.csv", header=False, sep='|')
# Export Selected Columns to CSV File
column_names = ['Country', 'Capital','Population']
df.to_csv("countries3.csv",index=False, columns=column_names)