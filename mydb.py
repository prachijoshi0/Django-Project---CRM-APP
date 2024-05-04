import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='1234'

)

#Preparing cursor object

cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco2")

print("ALL DONE !!!")