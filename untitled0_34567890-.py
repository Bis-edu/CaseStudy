# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:11:41 2020

@author: shada
"""
from os import system, name 
from time import sleep 
import mysql.connector
def Sign_In():
    clear()
    mydbSI = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="banking")
    ursId=int(input("Give your UserID"))
    psw=str(input("Give your Password"))
    mycursor = mydbSI.cursor()

    sql = "SELECT * FROM login_cred WHERE idLogin_cred=%s AND pswLogin_cred=%s"
    field_adr = (ursId,psw)
    mycursor.execute(sql,field_adr)
    myresult = mycursor.fetchall()
    if len(myresult)>0:
        clear()
        print("________________Welcome__________________")
        print("1. View All Customer")
        print("2. Search Customer")
        print("3. Add Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
    else:
        clear()
        print("Invalid credentials !!!!!!")
    mydbSI.commit()
    sleep(15)
    main()
def main():
    
    print("____________________Banking_System___________________")
    
    print("1:Sign Up")
    print("2:Sign In")
    
    inpSiSu=int(input())
    
    if inpSiSu == 1:
        Sign_Up()

    elif inpSiSu == 2:
        Sign_In()
        
    else:
        print("Invalid input")
        sleep(4)
        
def clear(): 
  
    
    if name == 'nt': 
        _ = system('cls') 
  

    else: 
        _ = system('clear')
        
def Sign_Up():
    clear()
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="banking")
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO login_cred (idLogin_cred, pswLogin_cred) VALUES (%s, %s)"
    idLogin_cred=int(input("Give a login Id"))
    pswLogin_cred=str(input("Give a Password"))
    val = (idLogin_cred, pswLogin_cred)
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")
    sleep(6)
    clear()
    main()
            
if __name__=="__main__":
    main()
    
    