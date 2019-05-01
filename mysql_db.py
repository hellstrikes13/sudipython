import MySQLdb
import csv
db = MySQLdb.connect("localhost","root","root123","devices")
cursor = db.cursor()
#qr = "select * from device"
qr = raw_input("SQL query: ")
cursor.execute(qr)
data = cursor.fetchall()
#print data
db.close()
c = csv.writer(open("temp.csv","wb"))
for i in data:
    c.writerow(i)
print '\ncontents are written in csv format in temp.csv...'
