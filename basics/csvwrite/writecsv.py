# Python program to demonstrate
# writing to CSV
import csv 

# field names 
fields = ['Entry', 'Country', 'Capital'] 
    
# data rows of csv file 
rows = [ ['1', 'France', 'Paris'], 
         ['2', 'Germany', 'Berlin'], 
         ['3', 'Spain', 'Madrid'], 
         ['4', 'Italy', 'Rome'], 
         ['5', 'UK', 'London']] 
    
# name of csv file 
filename = "countries1.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)