import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('student3.db')
print("Connection Established")

cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE STUDENT (SID int primary key, name text, age int, marks int)")
    conn.commit()
    print("STUDENT table created.")

def insertor():
    cur.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(1650, 'Rahul', 20, 71)")
    cur.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(1651, 'Sooraj', 21, 80)")
    cur.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(1652, 'Akhil', 21, 78)")
    cur.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(1653, 'Abhishek', 20, 70)")
    conn.commit()
    print("Values inserted into STUDENT Table.")

def DisplayAll():
    print('All Student\'s Data:')
    val = cur.execute('SELECT * FROM STUDENT')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def DisplayQuery():
    print('Students With Marks Less Than 75:')
    val = cur.execute('SELECT * FROM STUDENT WHERE marks<75')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def updator():
    cur.execute('UPDATE STUDENT SET name = "Gaurav" where SID = 1653')
    conn.commit()

def delete():
    cur.execute('DELETE FROM STUDENT WHERE SID = 1652')
    conn.commit()


n=0

while n==0:
    try:
        create_table()
        insertor()
        DisplayAll()
        DisplayQuery()
        updator()
        delete()
        DisplayAll()
    except Error as e:
        print(e)
        n=1
