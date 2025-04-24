#model related programming 
import mysql.connector

import view_file as vf

mydb = mysql.connector.connect(
    host = "bjkpecnt1b30k3vkcdwf-mysql.services.clever-cloud.com",
    user = "urxyvgja3stsloa5",
    password = "5AX1QJpSmU4AuBaOiEAO",
    database = "bjkpecnt1b30k3vkcdwf"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS journal")
sql = "CREATE TABLE journal (date VARCHAR(255), log VARCHAR(255))"
sql = "INSERT INTO journal (date, log) VALUES (%s, %s)"
mycursor.execute(sql, vf.entry)
mydb.commit()

mycursor.execute("DROP TABLE IF EXISTS emotions")

sql = "CREATE TABLE emotions (feeling VARCHAR(255), response VARCHAR(255))"
mycursor.execute(sql)

sql = "INSERT INTO emotions (feeling, response) VALUES (%s, %s)"
val = ("Happy", "Spend time with friends or family!")
mycursor.execute(sql, val)
mydb.commit()

sql2 = "INSERT INTO emotions (feeling, response) VALUES (%s, %s)"
val2 = ('Sad', 'Go on a walk')
mycursor.execute(sql2, val2)
mydb.commit()

sql3 = "INSERT into emotions (feeling, response) VALUES (%s, %s)"
val3 = ('Angry', 'Do a breathing exercise')
mycursor.execute(sql3, val3)
mydb.commit()

sql = "UPDATE emotions SET response = 'Work on a fun hobby' WHERE feeling = 'Happy'"
mycursor.execute(sql)
mydb.commit()

sql = "DELETE FROM emotions WHERE feeling ='Angry'"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM emotions")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
