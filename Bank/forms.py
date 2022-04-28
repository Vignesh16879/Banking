from django import forms
import datetime
from .sql import *


class inp_user(forms.Form):
    user_id = forms.IntegerField()
    user_password = forms.CharField(max_length = 200)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class Customer_Details(forms.Form):
    customer_id = forms.IntegerField()
    customer_adhar_no = forms.IntegerField()
    customer_name = forms.CharField(max_length = 200, required = False)
    customer_name_first = forms.CharField(max_length = 200, required = False)
    customer_name_middle = forms.CharField(max_length = 200, required = False)
    customer_name_last = forms.CharField(max_length = 200, required = False)
    customer_dob = forms.DateField(widget = forms.SelectDateWidget(), initial = datetime.date.today)
    customer_age = forms.IntegerField()
    customer_house_no = forms.IntegerField()
    customer_appartment_name = forms.CharField(max_length = 200, required = False)
    customer_place = forms.CharField(max_length = 200, required = False)
    customer_city = forms.CharField(max_length = 200, required = False)
    customer_state = forms.CharField(max_length = 200, required = False)
    customer_country = forms.CharField(max_length = 200, required = False)
    customer_email = forms.CharField(max_length = 200, required = False)
    customer_recovery_email = forms.CharField(max_length = 200, required = False)
    customer_password = forms.CharField(max_length = 200, required = False)
    customer_confirm_password = forms.CharField(max_length = 200, required = False)
    customer_security_code = forms.IntegerField()
    customer_security_hint = forms.CharField(max_length = 200, required = False)
    customer_phone_no = forms.IntegerField()
    customer_account_id = forms.IntegerField()
    customer_balance = forms.DecimalField(decimal_places = 2)
    customer_open_date = forms.DateField(widget = forms.SelectDateWidget(),initial = datetime.date.today)
    customer_close_date = forms.DateField(widget = forms.SelectDateWidget(),initial = datetime.date.today)
    

class loan(forms.Form):
    loan_id = 3
    loan_balance = forms.IntegerField()
    loan_interset_charge = forms.DecimalField(decimal_places = 2)
    loan_issue_date = forms.DateField(widget = forms.SelectDateWidget(),initial = datetime.date.today)
    loan_due_date = forms.DateField(widget = forms.SelectDateWidget(),initial = datetime.date.today)
    
    
class transaction(forms.Form):
    tranc_id_1 = forms.IntegerField()
    password = forms.CharField(max_length = 200, required = False)
    tranc_id_2 = forms.IntegerField()
    amount = forms.DecimalField(decimal_places = 2)
    
    def make_transfer(self):
        val = transaction_by_id(self.tranc_id_1, self.tranc_id_2, self.amount)
        
        if(val):
            return "Transaction Succesful"
        else:
            return "Due to {val} or some technical issue transaction couldn't be made"