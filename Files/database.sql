
-- CREATE DATABASE mydatabase
-- USE mydatabase
use mydatabase;

    
-- Customer Details
CREATE TABLE Customer (adhar_no INT PRIMARY KEY, customer_id INT);

INSERT INTO Customer VALUES(4388875, 3735642);
INSERT INTO Customer VALUES(4554367, 1803859);
INSERT INTO Customer VALUES(4274685, 7267904);
INSERT INTO Customer VALUES(2456911, 2741817);
INSERT INTO Customer VALUES(5543161, 7670755);
INSERT INTO Customer VALUES(5005656, 6753037);
INSERT INTO Customer VALUES(7007937, 8972002);
INSERT INTO Customer VALUES(3857656, 2523668);
INSERT INTO Customer VALUES(1345633, 5261472);
INSERT INTO Customer VALUES(8442659, 5229046);
INSERT INTO Customer VALUES(4550862, 5312984);
INSERT INTO Customer VALUES(5487443, 7317355);
INSERT INTO Customer VALUES(2579483, 2170045);
INSERT INTO Customer VALUES(6313063, 5029335);
INSERT INTO Customer VALUES(1385520, 8624541);
INSERT INTO Customer VALUES(3896561, 8284674);
INSERT INTO Customer VALUES(2163492, 1832560);
INSERT INTO Customer VALUES(4148418, 2540739);
INSERT INTO Customer VALUES(8791896, 3109444);
INSERT INTO Customer VALUES(4175372, 8827939);
INSERT INTO Customer VALUES(1847581, 1701861);
INSERT INTO Customer VALUES(5415663, 4966196);
INSERT INTO Customer VALUES(3547806, 5429052);
INSERT INTO Customer VALUES(3151129, 8724286);
INSERT INTO Customer VALUES(3787881, 2816802);


-- Customer Details: Name
CREATE TABLE Customer_Name (customer_id INT PRIMARY KEY, name_first VARCHAR(50) NOT NULL, name_middle VARCHAR(50), name_last VARCHAR(50));

INSERT INTO Customer_Name VALUES(3735642, "Etienne", "akj", "adhc");
INSERT INTO Customer_Name VALUES(1803859, "Eben", "djd", "hscv");
INSERT INTO Customer_Name VALUES(7267904, "Latashia", "efbi", "dcvd");
INSERT INTO Customer_Name VALUES(2741817, "Branden", "fhbrf", "dcv");
INSERT INTO Customer_Name VALUES(7670755, "Katie", "aba", "aubsca");
INSERT INTO Customer_Name VALUES(6753037, "Jorey", "john", "aoaha");
INSERT INTO Customer_Name VALUES(8972002, "Margaretha", "hsbc", "akiaa");
INSERT INTO Customer_Name VALUES(2523668, "Abdul", "cbc", "aldhco");
INSERT INTO Customer_Name VALUES(5261472, "Katina", "ahsbd", "xhbd");
INSERT INTO Customer_Name VALUES(5229046, "Rufe", "jbeff", "ahsja");
INSERT INTO Customer_Name VALUES(5312984, "Rab", "uuoa", "ajdhc");
INSERT INTO Customer_Name VALUES(7317355, "Sheffie", "aaja", "akdca");
INSERT INTO Customer_Name VALUES(2170045, "Katharine", "sksn", "cjda");
INSERT INTO Customer_Name VALUES(5029335, "Worthy", "scnc", "dcjbd");
INSERT INTO Customer_Name VALUES(8624541, "Shea", "cjdc", "dcjdbcd");
INSERT INTO Customer_Name VALUES(8284674, "Dirk", "pajas", "ajdcbd");
INSERT INTO Customer_Name VALUES(1832560, "Diann", "snxc", "adkc");
INSERT INTO Customer_Name VALUES(2540739, "Eada", "skcnd", "adkcdc");
INSERT INTO Customer_Name VALUES(3109444, "Myrilla", "scjnd", "adkcbc");
INSERT INTO Customer_Name VALUES(8827939, "Rhianna", "sckan", "ckdcd");
INSERT INTO Customer_Name VALUES(1701861, "Staford", "adjcan", "chvd");
INSERT INTO Customer_Name VALUES(4966196, "Ase", "aishc", "dcjia");
INSERT INTO Customer_Name VALUES(5429052, "Kaylil", "sjcdc", "akdcn");
INSERT INTO Customer_Name VALUES(8724286, "Katina", "adjchd", "aicn");
INSERT INTO Customer_Name VALUES(2816802, "Sloane", "scnd", "cbds");


-- Customer Details: Age
CREATE TABLE Customer_Age (customer_id INT PRIMARY KEY, dob DATE, age INT);

INSERT INTO Customer_Age VALUES(3735642, "2011/12/10", 11);
INSERT INTO Customer_Age VALUES(1803859, "2003/07/18", 19);
INSERT INTO Customer_Age VALUES(7267904, "2001/08/06", 21);
INSERT INTO Customer_Age VALUES(2741817, "2008/10/27", 14);
INSERT INTO Customer_Age VALUES(7670755, "2004/11/01", 18);
INSERT INTO Customer_Age VALUES(6753037, "2011/07/25", 11);
INSERT INTO Customer_Age VALUES(8972002, "2012/11/13", 10);
INSERT INTO Customer_Age VALUES(2523668, "2010/04/08", 12);
INSERT INTO Customer_Age VALUES(5261472, "2001/07/31", 21);
INSERT INTO Customer_Age VALUES(5229046, "2001/09/19", 21);
INSERT INTO Customer_Age VALUES(5312984, "2009/01/21", 13);
INSERT INTO Customer_Age VALUES(7317355, "2014/01/16", 8);
INSERT INTO Customer_Age VALUES(2170045, "2005/08/13", 17);
INSERT INTO Customer_Age VALUES(5029335, "2006/12/09", 16);
INSERT INTO Customer_Age VALUES(8624541, "2007/11/22", 15);
INSERT INTO Customer_Age VALUES(8284674, "2004/08/17", 18);
INSERT INTO Customer_Age VALUES(1832560, "2002/01/17", 20);
INSERT INTO Customer_Age VALUES(2540739, "2006/01/04", 16);
INSERT INTO Customer_Age VALUES(3109444, "2010/06/04", 12);
INSERT INTO Customer_Age VALUES(8827939, "2012/12/13", 10);
INSERT INTO Customer_Age VALUES(1701861, "2002/08/13", 20);
INSERT INTO Customer_Age VALUES(4966196, "2001/12/14", 21);
INSERT INTO Customer_Age VALUES(5429052, "2012/05/09", 10);
INSERT INTO Customer_Age VALUES(8724286, "2002/12/21", 20);
INSERT INTO Customer_Age VALUES(2816802, "2008/03/29", 14);


-- Customer Details: Address
CREATE TABLE Customer_Address (customer_id INT PRIMARY KEY, house_no INT, apartment_name VARCHAR(100), place VARCHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100);

INSERT INTO Customer_Address VALUES(3735642, 1,  "A", "ab", "abc", "delhi",  "India");
INSERT INTO Customer_Address VALUES(1803859, 2,  "B", "bc", "bca", "up",     "India");
INSERT INTO Customer_Address VALUES(7267904, 3,  "C", "cd", "cab", "punjab", "India");
INSERT INTO Customer_Address VALUES(2741817, 4,  "D", "de", "bba", "uk",     "India");
INSERT INTO Customer_Address VALUES(7670755, 5,  "E", "ef", "aaa", "dfs",    "India");
INSERT INTO Customer_Address VALUES(6753037, 6,  "F", "fg", "bbb", "oknh",   "India");
INSERT INTO Customer_Address VALUES(8972002, 7,  "G", "gh", "ccc", "lajds",  "India");
INSERT INTO Customer_Address VALUES(2523668, 8,  "H", "hi", "ddd", "jbc",    "India");
INSERT INTO Customer_Address VALUES(5261472, 9,  "I", "ij", "eee", "aubcd",  "India");
INSERT INTO Customer_Address VALUES(5229046, 10, "J", "jk", "fff", "aoehbc", "India");
INSERT INTO Customer_Address VALUES(5312984, 11, "K", "kl", "ggg", "cbbhc",  "India");
INSERT INTO Customer_Address VALUES(7317355, 12, "L", "lm", "hhh", "cbdcb",  "India");
INSERT INTO Customer_Address VALUES(2170045, 13, "M", "mn", "iii", "cudbie", "India");
INSERT INTO Customer_Address VALUES(5029335, 14, "N", "op", "kkk", "apjdb",  "India");
INSERT INTO Customer_Address VALUES(8624541, 15, "O", "qr", "lll", "ahcvc",  "India");
INSERT INTO Customer_Address VALUES(8284674, 16, "P", "st", "mmm", "achbhc", "India");
INSERT INTO Customer_Address VALUES(1832560, 17, "Q", "uv", "nnn", "cdnc",   "India");
INSERT INTO Customer_Address VALUES(2540739, 18, "R", "wx", "ooo", "cjbdc",  "India");
INSERT INTO Customer_Address VALUES(3109444, 19, "S", "yz", "ppp", "cie",    "India");
INSERT INTO Customer_Address VALUES(8827939, 20, "T", "za", "qqq", "eojd",   "India");
INSERT INTO Customer_Address VALUES(1701861, 21, "U", "ba", "rrr", "ocmm",   "India");
INSERT INTO Customer_Address VALUES(4966196, 22, "V", "cb", "sss", "cbac",   "India");
INSERT INTO Customer_Address VALUES(5429052, 23, "W", "dc", "ttt", "abcck",  "India");
INSERT INTO Customer_Address VALUES(8724286, 24, "X", "ed", "uuu", "cinc",   "India");
INSERT INTO Customer_Address VALUES(2816802, 25, "Y", "fe", "vvv", "acnd",   "India");


-- Customer Details: Account details
CREATE TABLE Customer_Account_Details (customer_id INT PRIMARY KEY,phone_no VARCHAR(10), email VARCHAR(200), recovery_email VARCHAR(200), passward VARCHAR(50), security_code INT, security_hint VARCHAR(100);

INSERT INTO Customer_Account_Details VALUES(3735642, 9116525250, "cgamil0@themeforest.net", "ebenfield0@qq.com", "ATpk4Vat8gYd", 833, "Idaho Bladderpod");
INSERT INTO Customer_Account_Details VALUES(1803859, 3547724471, "ncopeland1@mapquest.com", "tbestman1@zdnet.com", "Nu5JqI1hWv", 435, "Western Halfchaff Sedge");
INSERT INTO Customer_Account_Details VALUES(7267904, 1504385188, "mmcilhone2@reddit.com",  "gcristofolini2@squarespace.com", "25k9UZMME", 333, "'ihi Makole");
INSERT INTO Customer_Account_Details VALUES(2741817, 6118339485, "jspykins3@networkadvertising.org", "dcabena3@seesaa.net", "F6KVDXPkEt2", 736, "Arizona Beard Lichen");
INSERT INTO Customer_Account_Details VALUES(7670755, 3578684750, "adrinkhill4@indiatimes.com",  "tshetliff4@ted.com", "f379bYgX", 634, "Spotted Felt Lichen");
INSERT INTO Customer_Account_Details VALUES(6753037, 5692264395, "kyo5@ibm.com", "mrichel5@seattletimes.com", "6ORsD2pjmcct", 332, "Cleftleaf Phacelia");
INSERT INTO Customer_Account_Details VALUES(8972002, 8914854460, "lcarbry6@prweb.com", "ntottie6@soup.io", "xfd6Y8R", 635, "Hobblebush", "Lyalls Polytrichum Moss");
INSERT INTO Customer_Account_Details VALUES(2523668, 2607736851, "ldimitrov7@rediff.com", "rscholes7@opera.com", "sJ7gjOsTw6NB", 637, "Awned Bedstraw");
INSERT INTO Customer_Account_Details VALUES(5261472, 2789985351, "vwinscomb8@myspace.com", "mshellibeer8@indiegogo.com", "uWPkP5eUs", 937, "Forest False Ohelo");
INSERT INTO Customer_Account_Details VALUES(5229046, 3114555681, "csoldner9@ftc.gov", "ajeandin9@kickstarter.com", "yV0GOJDWy7XP", 734, "Parry's Beargrass");
INSERT INTO Customer_Account_Details VALUES(5312984, 2523337007, "rrowlesa@theglobeandmail.com", "moagera@mlb.com", "Drtgjb",  634, "Bristle Fern, Mallee Saltbush");
INSERT INTO Customer_Account_Details VALUES(7317355, 8534223376, "aowbrickb@chicagotribune.com", "amilazzob@dyndns.org", "665gyIeWj", 333, "Annual Wildrice");
INSERT INTO Customer_Account_Details VALUES(2170045, 7143730454, "jcampeyc@purevolume.com", "kbrabanc@google.cn", "QJsZFmoVOiIw", 636, "Felt Lichen");
INSERT INTO Customer_Account_Details VALUES(5029335, 8762617426, "svonderemptend@chicagotribune.com", "mblundeld@time.com", "Q2Wwj5w", 638, "Slimbristle Sandbur");
INSERT INTO Customer_Account_Details VALUES(8624541, 2291669878, "bheeneye@altervista.org",  "qgippse@arstechnica.com", "lLPmUu", 132, "Coyotethistle");
INSERT INTO Customer_Account_Details VALUES(8284674, 9666966666, "wkinkeadf@xrea.com", "mbazogef@blinklist.com", "Qvn2JlfOk", 233, "Fernaldia");
INSERT INTO Customer_Account_Details VALUES(1832560, 7298684736, "pselewayg@mtv.com", "stwaiteg@hc360.com", "7gUWb6", 436, "African Cornflag");
INSERT INTO Customer_Account_Details VALUES(2540739, 7857239303, "acrummeyh@qq.com", "bkleszinskih@google.nl", "gPWStxvP", 637, "Littleflower Alumroot");
INSERT INTO Customer_Account_Details VALUES(3109444, 2099980823, "ubenedyktowiczi@youku.com", "rpetersoni@hugedomains.com", "u088wIC2Dabr", 635, "Escabon");
INSERT INTO Customer_Account_Details VALUES(8827939, 6476276363, "jbeggj@ning.com", "sgolbornj@e-recht24.de", "H85EbQ",  433, "Coastal Plain Blue-eyed Grass");
INSERT INTO Customer_Account_Details VALUES(1701861, 7009607631, "floughtonk@sogou.com", "adozdillk@google.it", "MSdtu1uH", 637, "Tufted Frasera");
INSERT INTO Customer_Account_Details VALUES(4966196, 3295406110, "ajowittl@bloomberg.com", "orumfordl@infoseek.co.jp", "4oTlinsgwmn5", 233, "Japanese Primrose");
INSERT INTO Customer_Account_Details VALUES(5429052, 7396166679, "sthurberm@jugem.jp", "szannellim@cpanel.net", "QHkOk3jyJT", 132, "Purple-spot Parrot-lily");
INSERT INTO Customer_Account_Details VALUES(8724286, 6912314788, "mwickesn@forbes.com", "kborleacen@skype.com", "tSuuwmNmz", 436, "Fernaldia");
INSERT INTO Customer_Account_Details VALUES(2816802, 8454205588, "mhamsleyo@goodreads.com", "jmattasero@globo.com", "kAtziHi8W", 335, "African Cornflag");


-- Current Account
CREATE TABLE Current_Acc (customer_id INT, Account_id INT,balance INT, Open_date DATE, Close_date DATE);

INSERT INTO Current_Acc VALUES(3735642, 8622347303, 3000, "18/05/2021", "24/04/2022");
INSERT INTO Current_Acc VALUES(1803859, 2068732740, 3000, "04/12/2021", "24/04/2022");
INSERT INTO Current_Acc VALUES(7267904, 4235397923, 3000, "04/03/2022", "24/04/2022");
INSERT INTO Current_Acc VALUES(2741817, 2181951968, 3000, "09/08/2021", "24/04/2022");
INSERT INTO Current_Acc VALUES(7670755, 5142266978, 3000, "09/11/2021", "24/04/2022"),;


-- Saving Account
CREATE TABLE Saving_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE, amount INT);

INSERT INTO Saving_Acc VALUES(6753037, 7246632085, "28/03/2021", "05/04/2022", 2000);
INSERT INTO Saving_Acc VALUES(8972002, 6306347097, "28/03/2021", "16/02/2022", 20;0),
INSERT INTO Saving_Acc VALUES(2523668, 5614012931, "26/07/2021", "16/01/2022", 20;0),
INSERT INTO Saving_Acc VALUES(5261472, 2327308488, "18/12/2021", "25/02/2022", 20;0),
INSERT INTO Saving_Acc VALUES(5229046, 6221841917, "28/07/2021", "10/03/2022", 200;0),


-- Salary Account
CREATE TABLE Salary_Acc (customer_id INT, Account_id INT, amount INT, Open_date DATE, Close_date DATE);

INSERT INTO Salary_Acc VALUES(5312984, 2924698022, 4000, "20/07/2021", "29/03/2022");
INSERT INTO Salary_Acc VALUES(7317355, 4709424489, 4000, "11/10/2021", "12/03/2022");
INSERT INTO Salary_Acc VALUES(2170045, 4231919119, 4000, "09/12/2021", "18/03/2022");
INSERT INTO Salary_Acc VALUES(5029335, 4270432314, 4000, "13/04/2021", "07/03/2022");
INSERT INTO Salary_Acc VALUES(8624541, 5400162428, 4000, "09/07/2021", "04/02/2022"),;


-- NRI Account(NRO, NRI, FCNR)
CREATE TABLE NRI_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE, amount INT);

INSERT INTO NRI_Acc VALUES(8284674, 6504764476, "12/12/2021", "29/03/2022", 40200);
INSERT INTO NRI_Acc VALUES(1832560, 1031856128, "13/04/2021", "04/04/2022", 40200);
INSERT INTO NRI_Acc VALUES(2540739, 3265865301, "10/04/2021", "15/02/2022", 40200);
INSERT INTO NRI_Acc VALUES(3109444, 7015625435, "12/03/2021", "03/03/2022", 40200);
INSERT INTO NRI_Acc VALUES(8827939, 6306881581, "27/08/2021", "19/02/2022", 40200),;


-- Recurring Deposit Account
CREATE TABLE RD_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE, amount INT);

INSERT INTO RD_Acc VALUES(1701861, 8561726210, "17/11/2021", "06/02/2022", 35440);
INSERT INTO RD_Acc VALUES(4966196, 9167059708, "01/05/2021", "17/04/2022", 35440);
INSERT INTO RD_Acc VALUES(5429052, 6584511138, "18/12/2021", "22/03/2022", 35440);
INSERT INTO RD_Acc VALUES(8724286, 9120066562, "12/10/2021", "04/03/2022", 35440);
INSERT INTO RD_Acc VALUES(4816802114, 3467513662, "22/07/2021", "30/03/2022", 35440),;


-- Fixed Deposit Account
CREATE TABLE FD_Acc (customer_id INT, Account_id INT, Open_date DATE, Close_date DATE, amount INT);

INSERT INTO FD_Acc VALUES(8284674, 6504764476, "12/12/2021", "29/03/2022", 35440);
INSERT INTO FD_Acc VALUES(1832560, 1031856128, "13/04/2021", "04/04/2022", 35440);
INSERT INTO FD_Acc VALUES(2540739, 3265865301, "10/04/2021", "15/02/2022", 35440);
INSERT INTO FD_Acc VALUES(3109444, 7015625435, "12/03/2021", "03/03/2022", 35440);
INSERT INTO FD_Acc VALUES(8827939, 6306881581, "27/08/2021", "19/02/2022", 35440);


-- Loan
CREATE TABLE Loan (customer_id INT PRIMARY KEY, loan_id INT PRIMARY KEY, amount INT, rate_of_interset FLOAT, date_of_issue DATE, no_of_months_due INT);

INSERT INTO Loan VALUES(1832560, 1031856128, 45200, 12.23, "13/04/2021", "04/04/2022", 23);
INSERT INTO Loan VALUES(2540739, 3265865301, 45200, 12.23, "10/04/2021", "15/02/2022", 23);
INSERT INTO Loan VALUES(4966196, 9167059708, 45200, 12.23, "01/05/2021", "17/04/2022", 23);
INSERT INTO Loan VALUES(5429052, 6584511138, 45200, 12.23, "18/12/2021", "22/03/2022", 23);

-- Bank Branch
CREATE TABLE Bank_branch (Branch_id INT, Branch_name VARCHAR(100));

INSERT INTO Bank_branch VALUES(4393753,"Huntsville");
INSERT INTO Bank_branch VALUES(1034279,"San Diego");
INSERT INTO Bank_branch VALUES(5776665,"Colinas");
INSERT INTO Bank_branch VALUES(4819682,"Xingguo");
INSERT INTO Bank_branch VALUES(2019060,"Dengfang");
INSERT INTO Bank_branch VALUES(3108111,"Dalang");
INSERT INTO Bank_branch VALUES(6204594,"Lobão");
INSERT INTO Bank_branch VALUES(1291812,"Göteborg");
INSERT INTO Bank_branch VALUES(5393935,"Hetang");
INSERT INTO Bank_branch VALUES(9524941,"Nizhyn");
INSERT INTO Bank_branch VALUES(8598890,"Mamedkala");
INSERT INTO Bank_branch VALUES(2779706,"Trollhättan");
INSERT INTO Bank_branch VALUES(6365089,"Fornos");
INSERT INTO Bank_branch VALUES(4552110,"Tabia");
INSERT INTO Bank_branch VALUES(7765650,"Cankuzo");
INSERT INTO Bank_branch VALUES(3147306,"Fentange");
INSERT INTO Bank_branch VALUES(7816208,"San Agustín");
INSERT INTO Bank_branch VALUES(7442622,"Ulaanbaatar");
INSERT INTO Bank_branch VALUES(3614498,"Tongjin");
INSERT INTO Bank_branch VALUES(9988943,"Bebedouro");
INSERT INTO Bank_branch VALUES(4722239,"Papeete");
INSERT INTO Bank_branch VALUES(2681793,"Lechinkay");
INSERT INTO Bank_branch VALUES(4886416,"Yangqiao");
INSERT INTO Bank_branch VALUES(6199314,"Sunan");
INSERT INTO Bank_branch VALUES(5946171,"Bech");


-- Branch Details: Address
CREATE TABLE Branch_Address (Branch_id INT PRIMARY KEY, building_no INT, location_name VARCHAR(100), place VARCHAR(100), city VARCHAR(100), state VARCHAR(100), country VARCHAR(100);

INSERT INTO Branch_Address VALUES(4393753,717,"Mccormick","Pass","A","North Carolina");
INSERT INTO Branch_Address VALUES(1034279,7757,"Johnson","Pass","B","Pennsylvania","india");
INSERT INTO Branch_Address VALUES(5776665,9442,"Arrowood","Park","C","Virginia","india");
INSERT INTO Branch_Address VALUES(4819682,9519,"Marquette","Circle","D","District of Columbia","india");
INSERT INTO Branch_Address VALUES(2019060,99,"Prairieview","Pass","E","Arizona","india");
INSERT INTO Branch_Address VALUES(3108111,8992,"Bellgrove","Alley","F","Connecticut","india");
INSERT INTO Branch_Address VALUES(6204594,77543,"Riverside","Street","G","Pennsylvania","india");
INSERT INTO Branch_Address VALUES(1291812,1,"Bay","Road","H","Maryland","Virginia","india");
INSERT INTO Branch_Address VALUES(5393935,4934,"Hudson","Trail","I","Florida","india");
INSERT INTO Branch_Address VALUES(9524941,2516,"Elmside","Plaza","J","Pennsylvania","india");
INSERT INTO Branch_Address VALUES(8598890,64,"Moose","Trail","K","Texas","india");
INSERT INTO Branch_Address VALUES(2779706,742,"Fulton","Drive","L","Florida","india");
INSERT INTO Branch_Address VALUES(6365089,75108,"Florence","Avenue","M","Florida","india");
INSERT INTO Branch_Address VALUES(4552110,8,"Boyd","Lane","N","Missouri","Texas","india");
INSERT INTO Branch_Address VALUES(7765650,827,"Starling","Street","O","Florida","india");
INSERT INTO Branch_Address VALUES(3147306,77,"Miller","Center","P","Texas","india");
INSERT INTO Branch_Address VALUES(7816208,87549,"Clove","Drive","Q","Iowa","india");
INSERT INTO Branch_Address VALUES(7442622,4,"Leroy","Alley","R","Alabama","india");
INSERT INTO Branch_Address VALUES(3614498,96049,"Logan","Circle","S","Georgia","india");
INSERT INTO Branch_Address VALUES(9988943,7938,"Twin","PinesHill","T","Texas","india");
INSERT INTO Branch_Address VALUES(4722239,88378,"Thierer","Court","U","Louisiana","india");
INSERT INTO Branch_Address VALUES(2681793,9,"Grim","Point","V","California","india");
INSERT INTO Branch_Address VALUES(4886416,112,"Fallview","Pass","W","Alabama","india");
INSERT INTO Branch_Address VALUES(6199314,6,"Towne","Place","X","Alabama","india");
INSERT INTO Branch_Address VALUES(5946171,90,"hallmark","gatway","Y","Alabama","india");