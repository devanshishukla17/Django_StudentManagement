import mysql.connector

dataBase = mysql.connector.connect(

    host='localhost',
    user='root',
    passwd='Root123'
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE student")

print("All done")