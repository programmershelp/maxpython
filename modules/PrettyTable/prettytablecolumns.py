from prettytable import PrettyTable  
  
columns = ["Country", "Capital", "Continent"]  
  
newTable = PrettyTable()  
  
# Add Columns  
newTable.add_column(columns[0], ["France", "Germany", "Japan",  
                    "Peru", "Egypt", "China"])  
newTable.add_column(columns[1], ["Paris", "Berlin", "Tokyo", "Lima", "Cairo", "Beijing"])  
newTable.add_column(columns[2], ["Europe", "Europe", "Asia", "South America", "Africa", "Asia"])  

  
print(newTable)
