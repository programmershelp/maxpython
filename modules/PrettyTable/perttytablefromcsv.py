from prettytable import from_csv
with open("countries.csv") as fp:
    mytable = from_csv(fp)
print(mytable)