import mysql.connector
con = mysql.connector.connect(host="localhost",username="root",password="root",database="employee")
try:
 cursor=con.cursor()
 #sqlquery1 = "create table data(sid int,sname varchar(255),address varchar(255))" the query is to create table in empbd
 #sqlquery2 = "insert into data values(%s,%s,%s)"
 #values = (101, "sravani","tvr") this is the insert for only one record into data table
 #sqlquery3 = "insert into data values(%s,%s,%s)"
 #values = [(102, "puppy","hyd"), (103, "sravs","bangalore"), (104, "chitti","chennai")] this the insert many records into data table of employeedb
 #sqlquery4="update data set sname=%s where sid=%s"
 #values=("sravani",102) this is the update values of query sname puppy to sravani where sid is 102
 sqlquery5="delete from data where sid=%s"
 values=(102,)
 cursor.execute(sqlquery5, values)
 con.commit()
 print(cursor.rowcount,"some values are inserted sucssesfully into data table!")
except Exception as ex:
       print(ex)
       con.rollback()
finally:
    con.close()