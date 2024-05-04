import sqlite3 

def connect():
     connection  = sqlite3.connect("database.db")
     cursor = connection.cursor()
     return connection , cursor
     

def createTables():
     
     connection , cursor = connect()
     
     # create users table
     query = "create table users( user_id int primary_key auto increment , username varchar(100) , email varchar(50) , password varchar(20) )"
     cursor.execute(query)
     connection.commit()

     # create admins table

     query = "create table admins(   admin_id int primary_key auto increment , position varchar(100) , email varchar(50) , password varchar(20) )"
     cursor.execute(query)
     connection.commit()

     # create rooms table

     query = "create table rooms ( room_id int primary_key auto increment , room_name varchar(50) , room_location varchar(100) , capacity int  ) "
     cursor.execute(query)
     connection.commit()

    # create bookings table 
     query = "create table bookings( booking_id int primary_key auto increment , user_id int , scheduled_date date, booking_date date , start_time time , end_time time , purpose varchar(500) , status int  )"
     cursor.execute(query)
     connection.commit()


          


def queryMode():
     while True:
        connection , cursor = connect()
        query = input(">>")
        if query == "break":
             break
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        connection.commit()

queryMode()


     
