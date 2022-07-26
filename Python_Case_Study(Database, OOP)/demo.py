import mysql.connector

conn = None

conn = mysql.connector.connect(host='localhost',database='student',user='prerana',password='Mumbai#100')


if conn.is_connected():
    print('Connected to Mysql database')

cursor = conn.cursor()

cursor.execute("SELECT DATABASE()")

data = cursor.fetchone()
print("Connection established to: ",data)
cursor.execute("DROP TABLE IF EXISTS student_tbl")
query = "CREATE TABLE student_tbl(PRN VARCHAR(20),FNAME VARCHAR(10),MNAME VARCHAR(10),LNAME VARCHAR(20),ADDR VARCHAR(20),MOB VARCHAR(20),EMAIL VARCHAR(20),AGE VARCHAR(20))"
cursor.execute(query)


# sql = "select `FirstName`,`LastName` from student"
# cursor.execute(sql)

# i.Display the name and ages of all the students
result = cursor.fetchall()
for x in result:
    print(x)
# ii. Take input from the user and add it to the database
records_to_insert = [input("ENTER PRN: "),input("ENTER First_Name: "),input("ENTER Middle_Name: "),input("ENTER Last_Name: "), input("ENTER Address: "),input("ENTER Mobile_No: "),input("ENTER Email_ID: "),input("ENTER AGE: ")]
sql = "INSERT INTO student_tbl(PRN,FNAME,MNAME,LNAME,ADDR,MOB,EMAIL,AGE)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(sql,records_to_insert)
conn.commit()
print(cursor.rowcount, "record inserted.")


# iii. Delete a user by taking the PRN number as input
sql = "DELETE FROM student_tbl WHERE PRN = 1245034"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record deleted")

# iv. Update user details (Phone number and email id.)
sql = "UPDATE student_tbl SET MOB = '9876543211', EMAIL ='prb@gmail.com' WHERE PRN = 1245058"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record updated")

# v. Add a new column “CGPA” to the table and enter CGPA for all students.
query_1 = "ALTER TABLE student_tbl ADD CGPA float(20)"
query_2 = "UPDATE student_tbl SET CGPA = '9.45' where PRN=1245023"
query_3 = "UPDATE student_tbl SET CGPA = '7.35' where PRN=1245028"
query_4 = "UPDATE student_tbl SET CGPA = '9.24' where PRN=1245037"
query_5 = "UPDATE student_tbl SET CGPA = '8.74' where PRN=1245038"
query_6 = "UPDATE student_tbl SET CGPA = '7.84' where PRN=1245078"

cursor.execute(query_1)
cursor.execute(query_2)
cursor.execute(query_3)
cursor.execute(query_4)
cursor.execute(query_5)
cursor.execute(query_6)
conn.commit()

print(cursor.rowcount, "record(s) updated")

# vi. Display the final table.
cursor.execute("select * from student_tbl")
myresult = cursor.fetchall()
for row in myresult:
    print(row)

# Closing the connection
conn.close()