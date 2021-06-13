import mysql.connector
#Establishing connection to mysql DB as shown below
mydb=mysql.connector.connect(host='localhost',user='Netra',passwd='anitamom@123',database='telusko')#Adding database parameter as we need to retrieve stud details from DB.

#curson() which points to particular loaction using which we can work with our code/we can have connection to the DB.
mycursor=mydb.cursor()
mycursor.execute('select * from student')#Here all exexuted data(it will fetch all student details and store them in it itself) from DB will be stored in cursor itself.
result=mycursor.fetchall()#here we are fetching data from cursor and putting it in result and from result we are fetching the data
# if we want to fetch only one record ->result=mycursor.fetchone()
#result=mycursor.fetchone()
for item in result:
    print(item)
