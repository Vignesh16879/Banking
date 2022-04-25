from django import forms
import datetime
from .sql import *


class inp_user(forms.Form):
    user_id = forms.IntegerField(max_value = 1e13)
    user_password = forms.CharField(max_length = 200)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class Customer_Details(forms.Form):
    customer_id = forms.IntegerField(max_value = 1e9 - 1, min_value = 1e8)
    customer_adhar_no = forms.IntegerField(max_value = 1e13 - 1, min_value = 1e12)
    customer_name = forms.CharField(max_length = 200, required = False)
    customer_name_first = forms.CharField(max_length = 200, required = False)
    customer_name_middle = forms.CharField(max_length = 200, required = False)
    customer_name_last = forms.CharField(max_length = 200, required = False)
    customer_dob = forms.DateField(initial = datetime.date.today)
    customer_age = forms.IntegerField(max_value = 200)
    customer_house_no = forms.IntegerField(max_value = 1e9 - 1, min_value = 1e8)
    customer_appartment_name = forms.CharField(max_length = 200, required = False)
    customer_place = forms.CharField(max_length = 200, required = False)
    customer_city = forms.CharField(max_length = 200, required = False)
    customer_state = forms.CharField(max_length = 200, required = False)
    customer_country = forms.CharField(max_length = 200, required = False)
    customer_email = forms.CharField(max_length = 200, required = False)
    customer_recovery_email = forms.CharField(max_length = 200, required = False)
    customer_password = forms.CharField(max_length = 200, required = False)
    customer_confirm_password = forms.CharField(max_length = 200, required = False)
    customer_security_code = forms.IntegerField(max_value = 1e7 - 1, min_value = 1e6)
    customer_security_hint = forms.CharField(max_length = 200, required = False)
    customer_phone_no = forms.IntegerField(max_value = 1e11 - 1, min_value = 1e10)
    customer_account_id = forms.IntegerField(max_value = 1e11 - 1, min_value = 1e10)
    customer_balance = forms.DecimalField(decimal_places = 2)
    customer_open_date = forms.DateField(initial = datetime.date.today)
    customer_close_date = forms.DateField(initial = datetime.date.today)
    

class loan(forms.Form):
    loan_id = 3
    loan_balance = forms.IntegerField()
    loan_interset_charge = forms.DecimalField(decimal_places = 2)
    loan_issue_date = forms.DateField(initial = datetime.date.today)
    loan_due_date = forms.DateField(initial = datetime.date.today)
    
class transaction(forms.Form):
    tranc_id_1 = forms.IntegerField(max_value = 1e11 - 1, min_value = 1e10)
    password = forms.CharField(max_length = 200, required = False)
    tranc_id_2 = forms.IntegerField(max_value = 1e11 - 1, min_value = 1e10)
    amount = forms.DecimalField(decimal_places = 2)
    
    def make_transfer(self):
        val = transaction_by_id(self.tranc_id_1, self.tranc_id_2, self.amount)
        
        if(val):
            return "Transaction Succesful"
        else:
            return "Due to {val} or some technical issue transaction couldn't be made"