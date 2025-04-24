from tkinter import*
import tkinter
import mysql.connector
main = tkinter.Tk()
main.title("Database creation form")
main.geometry("1200x600")
main.config(bg="pink")
con = mysql.connector.connect(host="localhost",username="root",password="root",database="studentdb")


def createtable():
    text.delete('1.0',END)
    text.insert(END,"Table is created!")
    '''try:
        cursor = con.cursor()
        sqlquery1="create table attendance(sid int,sname varchar(255))"
        cursor.execute(sqlquery1)
        con.commit()
        text.insert(END,cursor.rowcount)
        text.insert(END,"Table is created!")
    except Exception as ex:
       print(ex)
       con.rollback()'''
def insert():
    text.delete('1.0',END)
    text.insert(END,"One value is inserted into table!")
    '''try:
        cursor = con.cursor()
        sqlquery2="insert into attendance values(%s,%s)"
        values=(101,"sravani")
        cursor.execute(sqlquery2,values)
        con.commit()
        text.insert(END,cursor.rowcount)
        text.insert(END,"Table is inserted!")
    except Exception as ex:
       print(ex)
       con.rollback()'''


def inserts():
    text.delete('1.0',END)
    text.insert(END,"Some values are inserted into table!")
    '''try:
        cursor = con.cursor()
        sqlquery3="insert into attendance values(%s,%s)"
        values=[(102,"puppy"),(103,"sravs"),(104,"chitti")]
        cursor.executemany(sqlquery3,values)
        con.commit()
        text.insert(END,cursor.rowcount)
        text.insert(END,"values are inserted into table!")
    except Exception as ex:
       print(ex)
       con.rollback()'''



def update():
    text.delete('1.0',END)
    text.insert(END,"values are updated into table!")
    '''try:
        cursor = con.cursor()
        sqlquery4="update attendance set sname=%s where sid=%s"
        values=("leela",103)
        cursor.execute(sqlquery4,values)
        con.commit()
        text.insert(END,cursor.rowcount)
        text.insert(END,"updated value in table!")
    except Exception as ex:
       print(ex)
       con.rollback()'''


def delete():
    text.delete('1.0',END)
    text.insert(END,"values are deleted into table!")
    '''try:
        cursor = con.cursor()
        sqlquery5="delete from attendance where sid=%s"
        values=(103,)
        cursor.execute(sqlquery5,values)
        con.commit()
        text.insert(END,cursor.rowcount)
        text.insert(END,"updated value in table!")
    except Exception as ex:
       print(ex)
       con.rollback()'''

font=('arial',14,'bold')
title=Label(main,text="MYSQL CRUD Operations in the form of buttons")
title.config(bg='purple',fg='orange',font=font,height=3,width=100)
title.place(x=0,y=0)

createtable=Button(main,text="create",command=createtable)
createtable.config(font=font,bg='blue',fg='white')
createtable.place(x=50, y=90)


insert=Button(main,text="insert",command=insert)
insert.config(font=font,bg='blue',fg='white')
insert.place(x=180, y=90)


inserts=Button(main,text="inserts",command=inserts)
inserts.config(font=font,bg='blue',fg='white')
inserts.place(x=350, y=90)


update=Button(main,text="update",command=update)
update.config(font=font,bg='blue',fg='white')
update.place(x=520, y=90)


delete=Button(main,text="delete",command=delete)
delete.config(font=font,bg='blue',fg='white')
delete.place(x=690, y=90)

text=Text(main,height=25,width=90)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50,y=140)
text.config(font=font)
main.mainloop()