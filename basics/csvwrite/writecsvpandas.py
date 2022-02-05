from pandas import DataFrame
C = {'Entry': ['1','2', '3', '4', '5'],
        'Country': ['France', 'Germany', 'Spain', 'Italy', 'UK'],
        'Capital': ['Paris', 'Berlin', 'Madrid', 'Rome', 'London'],
    }
df = DataFrame(C, columns= ['Entry', 'Country', 'Capital'])
export_csv = df.to_csv (r'countriespandas.csv', index = None, header=True) # here you have to write path, where result file will be stored
print (df)