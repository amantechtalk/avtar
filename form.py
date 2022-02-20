from flask import Flask, render_template, request,redirect
from flaskext.mysql import MySQL
import time
import socket
app = Flask(__name__)



@app.route('/')
def student():
             import mysql.connector
             db_connection = mysql.connector.connect(
  	            host="localhost",
  	            user="root",
                passwd="",
                database="mydb"  
                                           )
             print(db_connection)
             db_cursor = db_connection.cursor()
             aman="pok"
             aman1="poi"
             student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
             data=("","")
             #Execute cursor and pass query of employee and data of employee
             db_cursor.execute(student_sql_query,data)
             db_connection.commit()
             student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
             data=("","")
             #Execute cursor and pass query of employee and data of employee
             db_cursor.execute(student_sql_query,data)
             db_connection.commit()
             student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
             data=("","")
             #Execute cursor and pass query of employee and data of employee
             db_cursor.execute(student_sql_query,data)
             db_connection.commit()
             student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
             data=("","")
             #Execute cursor and pass query of employee and data of employee
             db_cursor.execute(student_sql_query,data)
             db_connection.commit()
  

             return render_template('chatbot.html')

@app.route('/chatbot',methods = ['POST', 'GET'])
def result():

    
 if request.method == 'POST':
    
    import csv
    from fuzzywuzzy import fuzz 
    from fuzzywuzzy import process
    import json
    aman5= request.form
    for (key ,value) in aman5.items():
        aman3=str(value)

    matrix = []
    j=0
    i=0
    with open('bot1.csv') as f:
       reader = csv.reader(f)
       matrix.append(list(reader))
    aman9="jh"
    str(aman9)
    print('100')
    for x in range (1,12):
       aman4=matrix[0][i]
       aman5=aman4[0]
       aman6=aman4[1]
       str(aman6)
       str(aman5)
       print(aman6)
       i=i+1
       print('101')
       aman=fuzz.token_sort_ratio(aman3,aman5) 
       print(aman) 
       if aman > 80:
           print(aman6)
           a="mansa"
           b=""
           c="manisha"
           d="mandra"
           e="ifa"
           print('102')
           print("aman")
           j=j+1
           if j>0: 
             fields=[aman3,aman6]
             with open(r'man1.csv', 'a') as f:
                 writer = csv.writer(f)
                 writer.writerow(fields)
             import mysql.connector
             db_connection = mysql.connector.connect(
  	            host="localhost",
  	            user="root",
                passwd="",
                database="mydb"  
                                       )
             print('103')   
             print(db_connection)
             db_cursor = db_connection.cursor()
             aman="pok"
             student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
             data=(aman3,aman6)
             #Execute cursor and pass query of employee and data of employee
             db_cursor.execute(student_sql_query,data)
             db_connection.commit()
             print(db_cursor.rowcount, "Record Inserted")
             sql='''SELECT count(question) FROM myusers'''
#Execute cursor and pass query of employee and data of employee  
             print('104')   
             db_cursor.execute(sql)
             result=db_cursor.fetchall()
             l= result[0][0]
             print(aman3)
             print(l)
             print("aman6")
             print('106')   
             sql='''SELECT * from myusers'''
#Execute cursor and pass query of employee and data of employee
             db_cursor.execute(sql)
             result=db_cursor.fetchall()
             a=result[l-2][0]
             b=result[l-2][1]
             c=result[l-1][0]
             d=result[l-1][1]
             print(a)
             print(b)
             print(c)
             print(d)
             print("aman6")
             db_connection.commit()
             print('107')   
             
             return render_template("chatbot.html",chatbot = aman6,a1=a,b1=b,c1=c,d1=d)
       
           
       aman9=aman6           
   
#Execute cursor and pass query of employee and data of employee
    if aman< 80:
        if j<1: 
           fields=[aman3,'']
           with open(r'man.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        import mysql.connector   
        db_connection = mysql.connector.connect(
  	            host="localhost",
  	            user="root",
                passwd="",
                database="mydb"  
                                           )
        print('108') 
        print(db_connection)
        db_cursor = db_connection.cursor()
        sql='''SELECT count(question) FROM myusers'''
#Execute cursor and pass query of employee and data of employee
        db_cursor.execute(sql)
        result=db_cursor.fetchall()
        l= result[0][0]
        print(l)
        print('109')   

        sql='''SELECT * from myusers'''
#Execute cursor and pass query of employee and data of employee
        db_cursor.execute(sql)
        result=db_cursor.fetchall()
        a=result[l-2][0]
        b=result[l-2][1]
        c=result[l-1][0]
        d=result[l-1][1]
        print(result[5][1])
        db_connection.commit() 
        print('110') 
        return render_template("chatbot.html",chatbot1 = "not in database",a1=a,b1=b,c1=c,d1=d)
       
@app.route('/chatbot2',methods = ['POST', 'GET'])
def student4():

  

   c=socket.socket()   
  
   while True:
       try:
           c.connect(('localhost',9996))
       
           if request.method == 'POST':
    
             aman5= request.form
             for (key ,value) in aman5.items():
                 aman3=str(value)
                 c.send(bytes(aman3, 'utf-8'))
 
           c.settimeout(200.0)
           name=c.recv(1024).decode()
           import mysql.connector
           db_connection = mysql.connector.connect(
  	            host="localhost",
  	            user="root",
                passwd="",
                database="mydb"  
                                           )
           print(db_connection)
           db_cursor = db_connection.cursor()
    
           student_sql_query =( "INSERT INTO myusers(question,answe)" "VALUES(%s, %s)")

             #Execute cursor and pass query as well as student data
           data=(aman3,name)
             #Execute cursor and pass query of employee and data of employee
           db_cursor.execute(student_sql_query,data)
           db_connection.commit()
           print(db_cursor.rowcount, "Record Inserted")
           sql='''SELECT count(question) FROM myusers'''
#Execute cursor and pass query of employee and data of employee
           db_cursor.execute(sql)
           result=db_cursor.fetchall()
           l= result[0][0]
           print(l)


           sql='''SELECT * from myusers'''
#Execute cursor and pass query of employee and data of employee
           db_cursor.execute(sql)
           result=db_cursor.fetchall()
           a=result[l-2][0]
           b=result[l-2][1]
           c=result[l-1][0]
           d=result[l-1][1]
           print(result[5][1])
           db_connection.commit()
           c.close()
           return render_template("chatbot.html",chatbot = name,a1=a,b1=b,c1=c,d1=d)
           
           
       except:
               print("")         
  
   


if __name__ == '__main__':
   app.run()
