-- 1. name of Customer who live in Janakpuri and have age above 20 and have balance of more than 20000
select CN.name_first from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD  where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id  and CA.age > 20 and CAD.balance > 20000;


-- 2. average loan taken in year 2020 by adults(age > 65) and who's loan is still pending
select avg(L.amount) from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD, Loan L where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id = L.customer_id and L.date_of_issue like "2020%"  and L.no_of_months_due > DATEDIFF(month, GETDATE(), L.date_of_issue) AS DateDiff and CA.age > 65;


-- 3. count of person who have salary above 10000 and have register loan above 200000 and have a saving account
select count(C.customer_id) from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD, Saving_A, SalA Sa SALAlary_Acc where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id = SA.customer_id = SalA.customer_id and SalA.amount > 10000 and L.amount > 200000;


-- 4. number of person per state alphabatically
select count(C.customer_id), distinct(CAD.state) from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id order by CAD.state; 


-- 5. alphabatical list of people who took loan and interset rate more than 10.52% in year 2021
select CN.name_first + " " + CN.name_middle(if not null) + " " + CN.name_last  from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD, Loan L where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id = L.customer_id and L.rate_of_interset > 10.52 and L.date_of_issue like "2021%" order by CN.name_first;


-- 6. number of branches in Delhi with name starting with H
select count(BB.Branch_id) from BB Bank_branch, BA Branch_Address where BB.Branch_id = BA.Branch_id and BA.state = "Delhi" and BB.Branch_name like "H%";


-- 7.
select from Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD  where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id and


-- 8. create a view of rich people
create view Rich_customer as select C.customer_id FROM Customer C, Customer_Name CN, Customer_Age CA, Customer_Address CADA, Customer_Account_Details CAD, Saving_Acc SA, Salary_Acc SALA, Loan L where C.customer_id = CN.customer_id = CA.customer_id = CADA.customer_id = CAD.customer_id = SA.customer_id = SalA.customer_id  and C.customer_id != L.customer_id and SA.amount > 5000 and SA.amount > 50000;

-- 9. Drop option for recovery email for customer
alter Customer_Account_Details drop column recovery_email;


-- 10. Group Data by Year and Quarter
SELECT EXTRACT(YEAR FROM date) AS year, EXTRACT(QUARTER FROM date) AS quarter, COUNT(amount) AS number_of_transactions FROM card_transaction GROUP BY EXTRACT(YEAR FROM date), EXTRACT(QUARTER FROM date) ORDER BY EXTRACT(YEAR FROM date) ASC, EXTRACT(QUARTER FROM date);


-- 11. Calculate Running Totals
SELECT  DISTINCT (ct.date), cty.card_type_name, SUM (ct.amount) OVER (PARTITION BY cty.card_type_name ORDER BY ct.date ASC) AS transaction_running_total FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN card_type cty ON cn.card_type_id = cty.id WHERE date > '2020-11-30' AND date <= '2020-12-31' ORDER BY cty.card_type_name ASC;


-- 12. Calculate Running Averages
SELECT  ct.date, cty.card_type_name, SUM(ct.amount) AS daily_sum, AVG(SUM(ct.amount)) OVER (ORDER BY ct.date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS transaction_running_average FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN card_type cty ON cn.card_type_id = cty.id WHERE ct.date > '2020-11-30' AND date <= '2020-12-31' AND cty.card_type_name = 'visa-electron' GROUP BY ct.date, cty.card_type_name ORDER BY cty.card_type_name;


-- 13. Time Series Analysis
SELECT  ct.date, SUM(ct.amount) AS daily_sum, (SUM(ct.amount)-LAG(SUM(ct.amount)) OVER (ORDER BY ct.date ASC)) AS daily_difference, co.country_name FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN customer_dat cu ON cn.customer_id = cu.id JOIN country co ON cu.country_id = co.id  WHERE ct.date > '2020-11-30' AND date <= '2020-12-31' AND co.country_name = 'China' GROUP BY ct.date, co.country_name;


-- 14. Add Multiple Grouping Levels
SELECT  EXTRACT(YEAR FROM ct.date) AS year, EXTRACT(QUARTER FROM ct.date) AS quarter, COUNT(ct.amount) AS number_of_transactions, cty.card_type_name FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN card_type cty ON cn.card_type_id = cty.id GROUP BY ROLLUP(EXTRACT(YEAR FROM ct.date), EXTRACT(QUARTER FROM ct.date), cty.card_type_name);


-- 15. Create a Revenue Report on a Yearly Level
SELECT  cu.NIN, cu.first_name, cu.last_name, SUM(ct.amount) AS total_revenue_per_customer, CASE WHEN SUM(ct.amount) >= 1000000 THEN 'Platinum' WHEN SUM(ct.amount) < 1000000 THEN 'Gold' END AS customer_category,  SUM(CASE WHEN ct.date >= '2019-01-01' AND ct.date < '2020-01-01' THEN ct.amount ELSE 0 END) AS revenue_2019, SUM(CASE WHEN ct.date >= '2020-01-01' AND ct.date < '2021-01-01' THEN ct.amount ELSE 0 END) AS revenue_2020 FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN customer_dat cu ON cn.customer_id = cu.id GROUP BY cu.NIN, cu.first_name, cu.last_name ORDER BY total_revenue_per_customer DESC;


-- Problem # 1:
-- Write a query to display the customer number, firstname, customer’s date of birth. Display in sorted order of date of birth year and within that sort by firstname.
SELECT custid, fname, mname,dob FROM cus ORDER BY EXTRACT(year FROM dob), fname ASC;


-- Problem # 2:
-- Write a query to display the customer’s number, first name, and middle name. The customer’s who don’t have a middle name, for them display the last name. Give the alias name as Cust_Name.
SELECT custid, fname, IF(mname IS NOT NULL, mname, ltname) AS Cust_Name FROM cus;


-- Problem # 3:
-- Write a query to display account number, customer’s number, customer’s firstname,lastname,account opening date.
SELECT account.acnumber, cus.custid, cus.fname, cus.ltname, account.aod FROM account INNER JOIN cus ON account.custid = cus.custid;


-- Problem # 4:
-- Write a query to display the number of customer’s from Delhi. Give the count an alias name of Cust_Count.
SELECT (SELECT COUNT(city) FROM cus WHERE city='Delhi') AS Cust_Count;


-- Problem # 5:
-- Write a query to display  the customer number, customer firstname,account number for the customer’s whose accounts were created after 15th of any month.
SELECT account.custid, cus.fname, account.acnumber FROM account, cus WHERE account.custid = cus.custid AND day(aod) > 15;


-- Problem # 6:
-- Write a query to display the female customers firstname, city and account number who are not into business, service or studies.
SELECT DISTINCT cus.fname, cus.city, account.acnumber FROM account, cus WHERE account.custid = cus.custid AND NOT(occupation=”business” or occupation=”service” or occupation=”student”);


-- Problem # 7:
-- Write a query to display city name and count of branches in that city. Give the count of branches an alias name of Count_Branch.
SELECT bcity, count(*) AS Count_Branch FROM bran Group By bcity;


-- Problem # 8:
-- Write a query to display account id, customer’s firstname, customer’s lastname for the customer’s whose account is Active.
SELECT account.acnumber, cus.fname, cus.ltname FROM account, cus WHERE account.custid = cus.custid AND astatus = “Active”;


-- Problem # 9:
-- Write a query to display the customer’s number, customer’s firstname, branch id and loan amount for people who have taken loans.
SELECT cus.custid, cus.fname, bran.bid, loan.loan_amount FROM ((loan INNER JOIN cus ON loan.custid=cus.custid) INNER JOIN bran ON loan.bid=bran.bid);


-- Problem # 10:
-- Write a query to display customer number, customer name, account number where the account status is terminated.
SELECT cus.custid, cus.fname, account.acnumber FROM account, cus WHERE account.custid = cus.custid AND astatus = “Terminated”;



SELECT  DISTINCT (ct.date), cty.card_type_name, SUM (ct.amount) OVER (PARTITION BY cty.card_type_name ORDER BY ct.date ASC) AS transaction_running_total FROM card_transaction ct JOIN card_number cn ON ct.card_number_id = cn.id JOIN card_type cty ON cn.card_type_id = cty.id WHERE ct.date > "2020/11/30" AND ct.date <= "2020/12/31" ORDER BY cty.card_type_name ASC; 