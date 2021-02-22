import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "1234",
    database = "schollDatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE schollDatabase")

# mycursor.execute("CREATE TABLE customers (id VARCHAR(255),studentnumber VARCHAR(255),Name VARCHAR(255),Surname VARCHAR(255),Birthdate VARCHAR(255),Gender VARCHAR(255))")


# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
# print(mydb)