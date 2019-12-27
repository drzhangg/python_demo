import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='demo'
)
mycursor = mydb.cursor()

sql = 'select * from people'

sql1 = 'select name,age from people'

# mycursor.execute(sql)

result1 = mycursor.execute(sql1)

#fetchall()获取所有记录
# myresult = mycursor.fetchall()

myresult = mycursor.fetchone()

for x in myresult:
    print(x)

for x in result1:
    print(x)
