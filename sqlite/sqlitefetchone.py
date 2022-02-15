import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('country1.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#insert data
cursor.execute('''SELECT * FROM COUNTRY''')

#fetch 1 results
print("One item of a data")
output = cursor.fetchone()
print(output)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()