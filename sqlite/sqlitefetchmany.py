import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('country1.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#insert data
cursor.execute('''SELECT * FROM COUNTRY''')

#fetch 3 results
print("Limited data")
output = cursor.fetchmany(3)
for row in output:
  print(row)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()