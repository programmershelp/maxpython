from prettytable import PrettyTable  
  
# Creating a new table   
newTable = PrettyTable(["Country", "Capital", "Continent"])  
  
# Add rows  
newTable.add_row(["France", "Paris", "Europe"])  
newTable.add_row(["Germany", "Berlin", "Europe"])  
newTable.add_row(["Japan", "Tokyo", "Asia"])  
newTable.add_row(["Peru", "Lima", "South America"])  
newTable.add_row(["Egypyt", "Cairo", "Africa"])  
newTable.add_row(["China", "Beijing", "Asia"])  
  
print(newTable)  