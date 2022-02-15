import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('country1.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
cursor.execute('''INSERT INTO COUNTRY VALUES ('Germany', 'Berlin', 'de', 83190556)''')
cursor.execute('''INSERT INTO COUNTRY VALUES ('Spain', 'Madrid', 'es', 47450795)''')
cursor.execute('''INSERT INTO COUNTRY VALUES ('Italy', 'Rome', 'it', 60317116)''')

#Commit your changes in the database
conn.commit()

print("3 Records inserted........")

#Closing the connection
conn.close()