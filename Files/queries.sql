-- 1. name of Customer who live in Janakpuri and have age above 20 and have balance of more than 20000
select CN.name_first + " " + CN.name_middle(if not null) + " " + CN.name_last 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details 
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id 
and CA.age > 20 and CAD.balance > 20000;

-- 2. average loan taken in year 2020 by adults(age > 65) and who's loan is still pending
select avg(L.amount)
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details, L Loan
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id = L.customer_id
and L.date_of_issue like "2020%" 
and L.no_of_months_due > DATEDIFF(month, GETDATE(), L.date_of_issue) AS DateDiff and CA.age > 65;

-- 3. count of person who have salary above 10000 and have register loan above 200000 and have a saving account
select count(C.customer_id)
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details, SA Saving_Acc, SalA Salary_Acc
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id = SA.customer_id = SalA.customer_id
and SalA.amount > 10000 and L.amount > 200000;

-- 4. number of person per state alphabatically
select count(C.customer_id), distinct(CAD.state)
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id order by CAD.state;

-- 5. 
select 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details 
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id 
and

-- 6.
select 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details 
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id 
and

-- 7.
select 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details 
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id 
and

-- 8. alphabatical list of people who took loan and interset rate more than 10.52% in year 2021
select CN.name_first + " " + CN.name_middle(if not null) + " " + CN.name_last 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details, L Loan
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id = L.customer_id
and L.rate_of_interset > 10.52 and L.date_of_issue like "2021%" order by CN.name_first;

-- 9. number of branches in Delhi with name starting with H
select count(BB.Branch_id) from BB Bank_branch, BA Branch_Address
where BB.Branch_id = BA.Branch_id and BA.state = "Delhi" and BB.Branch_name like "H%";

-- 10.
select 
from Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details 
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id 
and

-- 11. create a view of rich people
create view Rich_customer as select Customer C, CN Customer_Name, CA Customer_Age, CAd Customer_Address, CAD Customer_Account_Details, SA Saving_Acc, SalA Salary_Acc, L Loan
where C.customer_id = CN.customer_id = CA.customer_id = CAd.customer_id = CAD.customer_id = SA.customer_id = SalA.customer_id 
and C.customer_id != L.customer_id and SA.amount > 5000 and SA.amount > 50000;

-- 12. Drop option for recovery email for customer
alter Customer_Account_Details drop column recovery_email;