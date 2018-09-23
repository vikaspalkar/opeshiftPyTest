#This is a temporary script fil


import os

print("This is a simple Python....!")
username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_ROOT_PASSWORD']
print("Running with user: ",username)
print("Password is: ",password)
