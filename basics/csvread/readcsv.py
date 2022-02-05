# load csv module
import csv

# open file for reading
with open('countries.csv') as csvDataFile:

    # read file as csv file 
    csvReader = csv.reader(csvDataFile)

    # for every row, print the row
    for row in csvReader:
        print(row)