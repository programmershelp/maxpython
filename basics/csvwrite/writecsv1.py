#import modules
import csv

with open('Countries2.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #way to write to csv file
    writer.writerow(['Entry', 'Country', 'Capital'])
    writer.writerow(['1', 'France', 'Paris'])
    writer.writerow(['2', 'Germany', 'Berlin'])
    writer.writerow(['3', 'Spain', 'Madrid'])
    writer.writerow(['4', 'Italy', 'Rome'])
    writer.writerow(['5', 'UK', 'London'])