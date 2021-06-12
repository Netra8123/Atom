import mysql.connector
#Establishing connection to mysql DB as shown below
mydb=mysql.connector.connect(host='localhost',user='Netra',passwd='anitamom@123')

#curson() which points to particular loaction using which we can work with our code/we can have connection to the DB.
mycursor=mydb.cursor()
mycursor.execute('show databases')#Here all exexuted data(it will fetch all databses and store them in itself) from DB will be stored in cursor itself.
for item in mycursor:
    print(item)
