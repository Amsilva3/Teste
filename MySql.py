import mysql.connector

# Acessar pelo browser 127.0.0.1

mydb = mysql.connector.connect(
    host="localhost",
    user="andre",
    password="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
# sql = """CREATE TABLE pessoas (
# nome VARCHAR(255),
# idade INT(2)
# )"""
# mycursor.execute(sql)
# sql = """
# ALTER TABLE pessoas ADD sobrenome VARCHAR(255)
# """
# sql = "ALTER TABLE pessoas DROP sobrenome"
# sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"
# sql = "ALTER TABLE pessoas ADD sobrenomeVARCHAR(255) FIRST "
# sql = """CREATE TABLE pessoas (
# id INT AUTO_INCREMENT PRIMARY KEY
# nome VARCHAR(255),
# idade INT(2)
# )"""
sql = """ ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"""
mycursor.execute(sql)
# mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

