import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database='demo'
)

mycursor = mydb.cursor()

# sql = 'select * from people where name = "zhang"'
sql = 'select * from people order by id '

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)