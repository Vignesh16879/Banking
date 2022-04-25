from socket import MSG_CTRUNC
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vignesh#69757",
    # database="mydatabase",
)

# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("create database mydatabase")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

def insert_new_values(arr):
    sql = 'insert into table vale({})'.format(arr[0], arr[1])
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return True

def insert_data():
    # Databse SQL
    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("USE mydatabase")
        
    # Customer Details
    mycursor.execute("CREATE TABLE Customer (adhar_no INT PRIMARY KEY, customer_id INT PRIMARY KEY)")
    SQL_Query = "INSERT INTO Customer VALUES (%s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Name
    mycursor.execute("CREATE TABLE Customer_Name (customer_id INT PRIMARY KEY, name_first VARCHAR(50) NOT NULL, name_middle VARCHAR(50), name_last VARCHAR(50)")
    SQL_Query = "INSERT INTO Customer_Name VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Age
    mycursor.execute("CREATE TABLE Customer_Age (customer_id INT PRIMARY KEY, dob DATE, age INT")
    SQL_Query = "INSERT INTO Customer_Age VALUES (%s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Address
    mycursor.execute("CREATE TABLE Customer_Address (customer_id INT PRIMARY KEY, house_no INT, apartment_name VARCHAR(100), place VARVHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100)")
    SQL_Query = "INSERT INTO Customer_Address VALUES (%s, %s, %s, %s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Account details
    mycursor.execute("CREATE TABLE Customer_Account_Details (customer_id INT PRIMARY KEY,phone_no VARCHAR(10), email VARCHAR(200), recovery_email VARCHAR(200), passward VARCHAR(50), security_code INT, security_hint VARCHAR(100)")
    SQL_Query = "INSERT INTO Customer_Account_Details VALUES (%s, %s, %s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Current Account
    mycursor.execute("CREATE TABLE Current_Acc (customer_id INT, Account_id INT,balance INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO Current_Acc VALUES (%s, %s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Saving Account
    mycursor.execute("CREATE TABLE Saving_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO Saving_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Salary Account
    mycursor.execute("CREATE TABLE Salary_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO Salary_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # NRI Account(NRO, NRI, FCNR)
    mycursor.execute("CREATE TABLE NRI_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO NRI_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Recurring Deposit Account
    mycursor.execute("CREATE TABLE RD_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO RD_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Fixed Deposit Account
    mycursor.execute("CREATE TABLE FD_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO FD_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Loan
    mycursor.execute("CREATE TABLE Loan (customer_id INT PRIMARY KEY, loan_id INT PRIMARY KEY, amount INT, rate_of_interset FLOAT, date_of_issue DATE, no_of_months_due INT, status boolean")
    SQL_Query = "INSERT INTO Loan VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Bank Branch
    mycursor.execute("CREATE TABLE Bank_branch (Branch_id INT, Branc_name VARCHAR(100),)")
    SQL_Query = "INSERT INTO FD_Acc VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Branch Details: Address
    mycursor.execute("CREATE TABLE Branch_Address (Branch_id INT PRIMARY KEY, building_no INT, location_name VARCHAR(100), place VARVHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100)")
    SQL_Query = "INSERT INTO Branch_Address VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Commit(Saving All Data)
    mydb.commit()
    # print(mycursor.rowcount, "was inserted.")
    
    return True;
    

# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)

# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)





# # import pymongo
# # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# # mydb = myclient["mydatabase"]
# # print(myclient.list_database_names())
# # dblist = myclient.list_database_names()
# # if "mydatabase" in dblist:
# #     print("The database exists.")
# # mycol = mydb["customers"]
# # mydict = { "name": "John", "address": "Highway 37" }
# # x = mycol.insert_one(mydict)
# # print(x.inserted_id)
# # mylist = [
# #   { "name": "Amy", "address": "Apple st 652"},
# #   { "name": "Hannah", "address": "Mountain 21"},
# #   { "name": "Michael", "address": "Valley 345"},
# #   { "name": "Sandy", "address": "Ocean blvd 2"},
# #   { "name": "Betty", "address": "Green Grass 1"},
# #   { "name": "Richard", "address": "Sky st 331"},
# #   { "name": "Susan", "address": "One way 98"},
# #   { "name": "Vicky", "address": "Yellow Garden 2"},
# #   { "name": "Ben", "address": "Park Lane 38"},
# #   { "name": "William", "address": "Central st 954"},
# #   { "name": "Chuck", "address": "Main Road 989"},
# #   { "name": "Viola", "address": "Sideway 1633"}
# # ]
# # x = mycol.insert_many(mylist)
# # #print list of the _id values of the inserted documents:
# # print(x.inserted_ids)
# # mylist = [
# #   { "_id": 1, "name": "John", "address": "Highway 37"},
# #   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
# #   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
# #   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
# #   { "_id": 5, "name": "Michael", "address": "Valley 345"},
# #   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
# #   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
# #   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
# #   { "_id": 9, "name": "Susan", "address": "One way 98"},
# #   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
# #   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
# #   { "_id": 12, "name": "William", "address": "Central st 954"},
# #   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
# #   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# # ]
# # x = mycol.insert_many(mylist)
# # #print list of the _id values of the inserted documents:
# # print(x.inserted_ids)
# # x = mycol.find_one()
# # print(x)
# # for x in mycol.find():
# #     print(x)
# # for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
# #     print(x)