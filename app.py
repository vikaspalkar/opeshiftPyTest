#This is a temporary script fil

import MySQLdb
import os

print("This is a simple Python MySQL Connectivity code")
username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_ROOT_PASSWORD']
print("Running with user: ",username)
# Open database connection

db = MySQLdb.connect("172.30.88.85","username","password","sampledb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : ", data)

sql = "SELECT * FROM EMP;"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      emp_id = row[0]
      name = row[1]
      sal = row[2]
      
      # Now print fetched result
      print (emp_id, name, sal )
except:
   print ("Error: unable to fecth data")


# disconnect from server
db.close()

