
import mysql.connector as m
  
# database which you want to backup
db = 'geeksforgeeks'
  
connection = m.connect(host='localhost', user='root',
                       password='123', database=db)
cursor = connection.cursor()
  
# Getting all the table names
cursor.execute('SHOW TABLES;')
table_names = []
for record in cursor.fetchall():
    table_names.append(record[0])