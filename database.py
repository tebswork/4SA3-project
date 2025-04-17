#model related programming 
import mysql.connector

mydb = mysql.connector.connect(
    host = "bjkpecnt1b30k3vkcdwf-mysql.services.clever-cloud.com",
    user = "urxyvgja3stsloa5",
    password = "5AX1QJpSmU4AuBaOiEAO",
    database = "bjkpecnt1b30k3vkcdwf"
)

print(mydb)