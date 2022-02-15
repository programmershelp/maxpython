import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('country.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table
sql ='''CREATE TABLE COUNTRY(
   NAME CHAR(30) NOT NULL,
   CAPITAL CHAR(30),
   DOMAIN CHAR(10),
   POPULATION BIGINT
)'''
cursor.execute(sql)
print("Table created successfully........")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()