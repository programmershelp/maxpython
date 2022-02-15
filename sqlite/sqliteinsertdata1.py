import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('country1.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#insert data
cursor.execute('''INSERT INTO COUNTRY(NAME, CAPITAL, DOMAIN, POPULATION) 
   VALUES ('France', 'Paris', 'fr', 67413000)''')

#Commit your changes in the database
conn.commit()

print("Records inserted........")

#Closing the connection
conn.close()