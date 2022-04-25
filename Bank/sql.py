from socket import MSG_CTRUNC
import mysql.connector
from .forms import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vignesh#69757",
    database="mydatabase",
)


def check_user(user_id, password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT C.customer_id, A.passward FROM C Customer, A Customer_Account_Details WHERE C.customer_id = {user_id}")
    
    if(mycursor.rowcount == 0):
        mycursor.execute("SELECT C.adhar_no, A.passward FROM C Customer, A Customer_Account_Details WHERE C.adhar_no = {user_id}")
        
        if(mycursor.rowcount == 0):
            return "User Id Not Found"

    mycursor.execute("SELECT C.customer_id, A.passward FROM C Customer, A Customer_Account_Details WHERE C.customer_id = {user_id} AND A.passward = {password}")
    
    if(mycursor.rowcount == 0):
        return "Incorrect Password"
    
    return True
    
def get_user_name(user_id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT C.customer_id, A.passward FROM C Customer, A Customer_Account_Details WHERE C.customer_id = {user_id}")
    
    return mycursor.name_first + mycursor.name_middle + mycursor.name_last


def get_user_info(user_id):
    user_dat = Customer_Details()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Customer WHERE customer_id = {user_id}")
    user_dat.customer_id = mycursor.customer_id
    user_dat.customer_adhar_no = mycursor.adhar_no
    mycursor.execute("SELECT * FROM Customer_Name WHERE customer_id = {user_id}")
    user_dat.customer_name = get_user_name(user_id)
    user_dat.customer_name_first = mycursor.name_first
    user_dat.customer_name_middle = mycursor.name_middle
    user_dat.customer_name_last = mycursor.name_last
    mycursor.execute("SELECT * FROM Customer_Age WHERE customer_id = {user_id}")
    user_dat.customer_dob = mycursor.dob
    user_dat.customer_age = mycursor.age
    mycursor.execute("SELECT * FROM Customer_Address WHERE customer_id = {user_id}")
    user_dat.customer_house_no = mycursor.hous_no
    user_dat.customer_appartment_name = mycursor.appartment_name
    user_dat.customer_place = mycursor.place
    user_dat.customer_city = mycursor.city
    user_dat.customer_state = mycursor.state
    user_dat.customer_country = mycursor.country
    mycursor.execute("SELECT * FROM Customer_Account_Details WHERE customer_id = {user_id}")
    mycursor.execute("SELECT * FROM Current_Acc WHERE customer_id = {user_id}")
    
    return user_dat


def update_user_details(user_id, a):
    user_dat = get_user_info(user_id)
    
    if(a == 1): #Address
        mycursor = mydb.cursor()
        SQL_Query = "UPDATE Customer_Address SET house_no = %s, apartment_name = %s, place = %s, city =%s, state = %s, country =%s WHERE customer_id = {user_id}"
        Table_Values = [()]
        mycursor.execute(SQL_Query, Table_Values)

    if(a == 2): #Email / Recovery Email
        mycursor = mydb.cursor()
        SQL_Query = "UPDATE Customer_Account_Details SET email = %s, recovery_email = %s WHERE customer_id = {user_id}"
        Table_Values = [()]
        mycursor.execute(SQL_Query, Table_Values)
        
    if(a == 3): #Password / Security Code / Secuirty Hint
        mycursor = mydb.cursor()
        SQL_Query = "UPDATE Customer_Account_Details SET passward = %s, security_code = %s, security_hint = %s WHERE customer_id = {user_id}"
        Table_Values = [()]
        mycursor.execute(SQL_Query, Table_Values)
        
    mydb.commit()
    
    return True


def transaction_by_id(id1, id2, bal):
    user1 = get_user_info(id1)
    user1.balance -= bal
    user2 = get_user_info(id2)
    user2.balance += bal
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE Current_Acc SET balance = {user1.balance} WHERE customer_id = {id1}")
    
    if(mycursor.rowcount == 0):
        return "wrong Account Id"
    
    mycursor.execute("UPDATE Current_Acc SET balance = {user2.balance} WHERE customer_id = {id2}")
    
    if(mycursor.rowcount == 0):
        return "Wrong Transfer Account Id"
    
    mydb.commit()
    
    return True


def remove_user(user_id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Loan WHERE customer_id = {user_id}")
    
    if(mycursor.status or mycursor.rowcount == 0):
        mycursor.execute("DELETE FROM Customer WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Customer_Name WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Customer_Age WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Customer_Address WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Customer_Account_Details WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Current_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Saving_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Salary_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM NRI_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM RD_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM FD_Acc WHERE customer_id = {user_id}")
        mycursor.execute("DELETE FROM Loan WHERE customer_id = {user_id}")
        mydb.commit()
        return True
    
    return False


def insert_user_data(user_dat):
    # Databse SQL
    mycursor = mydb.cursor()
    
    # Customer Details
    SQL_Query = "INSERT INTO Customer VALUES (%s, %s)"
    Table_Values = [
        (),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Name
    SQL_Query = "INSERT INTO Customer_Name VALUES (%s, %s, %s, %s)"
    Table_Values = [
        
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Age
    SQL_Query = "INSERT INTO Customer_Age VALUES (%s, %s, %s)"
    Table_Values = [
        
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Address
    SQL_Query = "INSERT INTO Customer_Address VALUES (%s, %s, %s, %s, %s, %s, %s)"
    Table_Values = [
        
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Account details
    SQL_Query = "INSERT INTO Customer_Account_Details VALUES (%s, %s, %s, %s, %s, %s)"
    Table_Values = [
        
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    mydb.commit()
    # print(mycursor.rowcount, "was inserted.")
    
    return True


def retrive_data():
    # Databse SQL
    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE mydatabase")
    # mycursor.execute("USE mydatabase")
        
    # Customer Details
    mycursor.execute("CREATE TABLE Customer (adhar_no INT PRIMARY KEY, customer_id INT PRIMARY KEY)")
    SQL_Query = "INSERT INTO Customer VALUES (%s, %s)"
    Table_Values = [
        (4388874175, 3735642047),
        (4554369447, 1803859546),
        (4274683435, 7267904734),
        (2456913361, 2741817197),
        (5543167091, 7670755962),
        (5005651136, 6753037217),
        (7007939147, 8972002151),
        (3857655356, 2523668955),
        (1345633563, 5261472288),
        (8442658459, 5229046864),
        (4550867892, 5312984477),
        (5487444943, 7317355615),
        (2579482903, 2170045651),
        (6313061683, 5029335625),
        (1385527560, 8624541050),
        (3896569651, 8284674653),
        (2163492362, 1832560783),
        (4148413238, 2540739458),
        (8791898366, 3109444755),
        (4175372792, 8827939725),
        (1847583121, 1701861461),
        (5415666443, 4966196663),
        (3547805716, 5429052698),
        (3151121179, 8724286591),
        (3787889531, 2816802114),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Name
    mycursor.execute("CREATE TABLE Customer_Name (customer_id INT PRIMARY KEY, name_first VARCHAR(50) NOT NULL, name_middle VARCHAR(50), name_last VARCHAR(50)")
    SQL_Query = "INSERT INTO Customer_Name VALUES (%s, %s, %s, %s)"
    Table_Values = [
        (3735642047, "Etienne", "akj", "adhc"),
        (1803859546, "Eben", "djd", "hscv"),
        (7267904734, "Latashia", "efbi", "dcvd"),
        (2741817197, "Branden", "fhbrf", "dcv"),
        (7670755962, "Katie", "aba", "aubsca"),
        (6753037217, "Jorey", "john", "aoaha"),
        (8972002151, "Margaretha", "hsbc", "akiaa"),
        (2523668955, "Abdul", "cbc", "aldhco"),
        (5261472288, "Katina", "ahsbd", "xhbd"),
        (5229046864, "Rufe", "jbeff", "ahsja"),
        (5312984477, "Rab", "uuoa", "ajdhc"),
        (7317355615, "Sheffie", "aaja", "akdca"),
        (2170045651, "Katharine", "sksn", "cjda"),
        (5029335625, "Worthy", "scnc", "dcjbd"),
        (8624541050, "Shea", "cjdc", "dcjdbcd"),
        (8284674653, "Dirk", "pajas", "ajdcbd"),
        (1832560783, "Diann", "snxc", "adkc"),
        (2540739458, "Eada", "skcnd", "adkcdc"),
        (3109444755, "Myrilla", "scjnd", "adkcbc"),
        (8827939725, "Rhianna", "sckan", "ckdcd"),
        (1701861461, "Staford", "adjcan", "chvd"),
        (4966196663, "Ase", "aishc", "dcjia"),
        (5429052698, "Kaylil", "sjcdc", "akdcn"),
        (8724286591, "Katina", "adjchd", "aicn"),
        (2816802114, "Sloane", "scnd", "cbds"),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Age
    mycursor.execute("CREATE TABLE Customer_Age (customer_id INT PRIMARY KEY, dob DATE, age INT")
    SQL_Query = "INSERT INTO Customer_Age VALUES (%s, %s, %s)"
    Table_Values = [
        (3735642047, "10/12/2011", 11),
        (1803859546, "18/07/2003", 19),
        (7267904734, "06/08/2001", 21),
        (2741817197, "27/10/2008", 14),
        (7670755962, "01/11/2004", 18),
        (6753037217, "25/07/2011", 11),
        (8972002151, "13/11/2012", 10),
        (2523668955, "08/04/2010", 12),
        (5261472288, "31/07/2001", 21),
        (5229046864, "19/09/2001", 21),
        (5312984477, "21/01/2009", 13),
        (7317355615, "16/01/2014", 8),
        (2170045651, "13/08/2005", 17),
        (5029335625, "09/12/2006", 16),
        (8624541050, "22/11/2007", 15),
        (8284674653, "17/08/2004", 18),
        (1832560783, "17/01/2002", 20),
        (2540739458, "04/01/2006", 16),
        (3109444755, "04/06/2010", 12),
        (8827939725, "13/12/2012", 10),
        (1701861461, "13/08/2002", 20),
        (4966196663, "14/12/2001", 21),
        (5429052698, "09/05/2012", 10),
        (8724286591, "21/12/2002", 20),
        (2816802114, "29/03/2008", 14),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Address
    mycursor.execute("CREATE TABLE Customer_Address (customer_id INT PRIMARY KEY, house_no INT, apartment_name VARCHAR(100), place VARVHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100)")
    SQL_Query = "INSERT INTO Customer_Address VALUES (%s, %s, %s, %s, %s, %s, %s)"
    Table_Values = [
        (3735642047, 1,  "A", "ab", "abc", "delhi",  "India"),
        (1803859546, 2,  "B", "bc", "bca", "up",     "India"),
        (7267904734, 3,  "C", "cd", "cab", "punjab", "India"),
        (2741817197, 4,  "D", "de", "bba", "uk",     "India"),
        (7670755962, 5,  "E", "ef", "aaa", "dfs",    "India"),
        (6753037217, 6,  "F", "fg", "bbb", "oknh",   "India"),
        (8972002151, 7,  "G", "gh", "ccc", "lajds",  "India"),
        (2523668955, 8,  "H", "hi", "ddd", "jbc",    "India"),
        (5261472288, 9,  "I", "ij", "eee", "aubcd",  "India"),
        (5229046864, 10, "J", "jk", "fff", "aoehbc", "India"),
        (5312984477, 11, "K", "kl", "ggg", "cbbhc",  "India"),
        (7317355615, 12, "L", "lm", "hhh", "cbdcb",  "India"),
        (2170045651, 13, "M", "mn", "iii", "cudbie", "India"),
        (5029335625, 14, "N", "op", "kkk", "apjdb",  "India"),
        (8624541050, 15, "O", "qr", "lll", "ahcvc",  "India"),
        (8284674653, 16, "P", "st", "mmm", "achbhc", "India"),
        (1832560783, 17, "Q", "uv", "nnn", "cdnc",   "India"),
        (2540739458, 18, "R", "wx", "ooo", "cjbdc",  "India"),
        (3109444755, 19, "S", "yz", "ppp", "cie",    "India"),
        (8827939725, 20, "T", "za", "qqq", "eojd",   "India"),
        (1701861461, 21, "U", "ba", "rrr", "ocmm",   "India"),
        (4966196663, 22, "V", "cb", "sss", "cbac",   "India"),
        (5429052698, 23, "W", "dc", "ttt", "abcck",  "India"),
        (8724286591, 24, "X", "ed", "uuu", "cinc",   "India"),
        (2816802114, 25, "Y", "fe", "vvv", "acnd",   "India"),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Customer Details: Account details
    mycursor.execute("CREATE TABLE Customer_Account_Details (customer_id INT PRIMARY KEY,phone_no VARCHAR(10), email VARCHAR(200), recovery_email VARCHAR(200), passward VARCHAR(50), security_code INT, security_hint VARCHAR(100)")
    SQL_Query = "INSERT INTO Customer_Account_Details VALUES (%s, %s, %s, %s, %s, %s)"
    Table_Values = [
        (3735642047, 9116525250, "cgamil0@themeforest.net", "ebenfield0@qq.com", "ATpk4Vat8gYd", 833, "Idaho Bladderpod"),
        (1803859546, 3547724471, "ncopeland1@mapquest.com", "tbestman1@zdnet.com", "Nu5JqI1hWv", 435, "Western Halfchaff Sedge"),
        (7267904734, 1504385188, "mmcilhone2@reddit.com",  "gcristofolini2@squarespace.com", "25k9UZMME", 333, "'ihi Makole"),
        (2741817197, 6118339485, "jspykins3@networkadvertising.org", "dcabena3@seesaa.net", "F6KVDXPkEt2", 736, "Arizona Beard Lichen"),
        (7670755962, 3578684750, "adrinkhill4@indiatimes.com",  "tshetliff4@ted.com", "f379bYgX", 634, "Spotted Felt Lichen"),
        (6753037217, 5692264395, "kyo5@ibm.com", "mrichel5@seattletimes.com", "6ORsD2pjmcct", 332, "Cleftleaf Phacelia"),
        (8972002151, 8914854460, "lcarbry6@prweb.com", "ntottie6@soup.io", "xfd6Y8R", 635, "Hobblebush", "Lyall's Polytrichum Moss"),
        (2523668955, 2607736851, "ldimitrov7@rediff.com", "rscholes7@opera.com", "sJ7gjOsTw6NB", 637, "Awned Bedstraw"),
        (5261472288, 2789985351, "vwinscomb8@myspace.com", "mshellibeer8@indiegogo.com", "uWPkP5eUs", 937, "Forest False Ohelo"),
        (5229046864, 3114555681, "csoldner9@ftc.gov", "ajeandin9@kickstarter.com", "yV0GOJDWy7XP", 734, "Parry's Beargrass"),
        (5312984477, 2523337007, "rrowlesa@theglobeandmail.com", "moagera@mlb.com", "Drtgjb",  634, "Bristle Fern, Mallee Saltbush"),
        (7317355615, 8534223376, "aowbrickb@chicagotribune.com", "amilazzob@dyndns.org", "665gyIeWj", 333, "Annual Wildrice"),
        (2170045651, 7143730454, "jcampeyc@purevolume.com", "kbrabanc@google.cn", "QJsZFmoVOiIw", 636, "Felt Lichen"),
        (5029335625, 8762617426, "svonderemptend@chicagotribune.com", "mblundeld@time.com", "Q2Wwj5w", 638, "Slimbristle Sandbur"),
        (8624541050, 2291669878, "bheeneye@altervista.org",  "qgippse@arstechnica.com", "lLPmUu", 132, "Coyotethistle"),
        (8284674653, 9666966666, "wkinkeadf@xrea.com", "mbazogef@blinklist.com", "Qvn2JlfOk", 233, "Fernaldia"),
        (1832560783, 7298684736, "pselewayg@mtv.com", "stwaiteg@hc360.com", "7gUWb6", 436, "African Cornflag"),
        (2540739458, 7857239303, "acrummeyh@qq.com", "bkleszinskih@google.nl", "gPWStxvP", 637, "Littleflower Alumroot"),
        (3109444755, 2099980823, "ubenedyktowiczi@youku.com", "rpetersoni@hugedomains.com", "u088wIC2Dabr", 635, "Escabon"),
        (8827939725, 6476276363, "jbeggj@ning.com", "sgolbornj@e-recht24.de", "H85EbQ",  433, "Coastal Plain Blue-eyed Grass"),
        (1701861461, 7009607631, "floughtonk@sogou.com", "adozdillk@google.it", "MSdtu1uH", 637, "Tufted Frasera"),
        (4966196663, 3295406110, "ajowittl@bloomberg.com", "orumfordl@infoseek.co.jp", "4oTlinsgwmn5", 233, "Japanese Primrose"),
        (5429052698, 7396166679, "sthurberm@jugem.jp", "szannellim@cpanel.net", "QHkOk3jyJT", 132, "Purple-spot Parrot-lily"),
        (8724286591, 6912314788, "mwickesn@forbes.com", "kborleacen@skype.com", "tSuuwmNmz", 436, "Fernaldia"),
        (2816802114, 8454205588, "mhamsleyo@goodreads.com", "jmattasero@globo.com", "kAtziHi8W", 335, "African Cornflag"),
        ]
    mycursor.executemany(SQL_Query, Table_Values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")

    # Current Account
    mycursor.execute("CREATE TABLE Current_Acc (customer_id INT, Account_id INT,balance INT, Open_date DATE, Close_date DATE)")
    SQL_Query = "INSERT INTO Current_Acc VALUES (%s, %s, %s, %s, %s)"
    Table_Values = [
        (3735642047, 8622347303, "18/05/2021", "24/04/2022"),
        (1803859546, 2068732740, "04/12/2021", "24/04/2022"),
        (7267904734, 4235397923, "04/03/2022", "24/04/2022"),
        (2741817197, 2181051968, "09/08/2021", "24/04/2022"),
        (7670755962, 5142266978, "09/11/2021", "24/04/2022"),
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
    mycursor.execute("CREATE TABLE Loan (customer_id INT PRIMARY KEY, loan_id INT PRIMARY KEY, amount INT, rate_of_interset FLOAT, date_of_issue DATE, no_of_months_due INT")
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