import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='demo'
)

mycursor = mydb.cursor()

# mycursor.execute('show tables')

sql = 'insert into people (name,id,age) values (%s,%s,%s)'
# val = ('jerry','2','23')
val = [('tom','3','24'),('drzhang','4','25'),('hui','5','26')]
# mycursor.execute(sql,val)

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,'记录插入成功')

for x in mycursor:
    print(x)