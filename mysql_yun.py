import MySQLdb

db = MySQLdb.connect("localhost", "root", "kang", "yun", charset='utf8' )
cursor = db.cursor()
spl_con = "select row from car1 where time = 1 "

cursor.execute(spl_con)
data = cursor.fetchone()
print data[0], type(data), data[0]

d = data[0]
d = int(d)
print d/10
db.close()

