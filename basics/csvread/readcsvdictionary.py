import csv      
with open('countries.csv', mode='r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)    
    line_count = 0    
    for row in csv_reader:    
        if line_count == 0:    
            print(f'The Column names are as follows {", ".join(row)}')    
            line_count += 1    
        print(f'\t{row["Capital"]} is the capital of {row["Country"]}.')    
        line_count += 1    
    print(f'Processed {line_count} lines.')   