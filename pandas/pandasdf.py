# Create pandas DataFrame from List
import pandas as pd
capitals = [ ["Tokyo","Japan","37732000"], 
                 ["Seoul","South Korea","23016000"], 
               ]
df=pd.DataFrame(capitals)
column_names=["Capital","Country","Population"]
row_label=["a","b"]
df=pd.DataFrame(capitals,columns=column_names,index=row_label)
types={'Capital': str,'Country':str,'Population':float}
df=df.astype(types)
print(df.dtypes)
print(df)
