from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import *
from .sql import *
import mysql.connector
from random import randint, randrange

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vignesh#69757",
    database="mydatabase",
)



user_id = NULL
user_authenticated = False


def home(request):
    return render(request, "index.html")


def home_page(request):
    if(user_authenticated):
        return render(request, "user.html")
    
    return render(request, "index.html")


def intialize_data():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    
    if(mycursor.rowcount == 0):
        retrive_data()
        
    return True


def index(request):
    # intialize_data()
    
    return render(request, "index.html")

def login_id(request):
    form = inp_user()
    assert isinstance(request, HttpRequest)
    global user_authenticated
    if user_authenticated:
        messages.error(request, "You are already logged in.")
        return redirect("Bank:home")

    if request.method == 'POST':
        form = inp_user(request=request, data=request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_id')
            password = form.cleaned_data.get('user_password')
            
            valid_user_details = check_user(user_id, password)
            if(valid_user_details):
                user_authenticated = True
                login(request, user_id)
                username = get_user_name(user_id)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("Bank:home")
            else:       
                messages.error(request, valid_user_details)
           
    # form = inp_user()
    
    context = {}
    
    return render(
        request, 
        "login.html", 
        {
            'form' : form
        }
    )

def login(request, user_id):
    return render(request, "user.html")


     
    
def logout_request(request):
    assert isinstance(request, HttpRequest)
    logout(request)
    messages.success(request, "Logged out successfully!")
    user_authenticated = False
    return redirect("Bank:index")


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def register(request):
    form = Customer_Details()
    if request.method == 'POST':
        form = Customer_Details(request=request, data=request.POST)
        
        if form.is_valid():
            user_dat = Customer_Details()
            # user_dat = form.cleaned_data.get('User Id')
            # password = form.cleaned_data.get('Password')
            m = 1
            
            while(m > 0):
                user_dat.customer_id = random_with_N_digits(8)
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM Customer WHERE customer_id = {user_dat.customer_id}")
                m = mycursor.rowcount
                            
            user_dat.customer_adhar_no = form.cleaned_data.get("customer_adhar_no")
            user_dat.customer_name = form.cleaned_data.get("customer_name")
            user_dat.customer_name_first = form.cleaned_data.get("customer_name_first")
            user_dat.customer_name_middle = form.cleaned_data.get("customer_name_middle")
            user_dat.customer_name_last = form.cleaned_data.get("customer_name_last")
            user_dat.customer_dob = form.cleaned_data.get("customer_dob")
            user_dat.customer_age = form.cleaned_data.get("customer_age")
            user_dat.customer_house_no = form.cleaned_data.get("customer_house_no")
            user_dat.customer_appartment_name = form.cleaned_data.get("customer_appartment_name")
            user_dat.customer_place = form.cleaned_data.get("customer_place")
            user_dat.customer_city = form.cleaned_data.get("customer_city")
            user_dat.customer_state = form.cleaned_data.get("customer_state")
            user_dat.customer_country = form.cleaned_data.get("customer_country")
            user_dat.customer_email = form.cleaned_data.get("customer_email")
            user_dat.customer_recovery_email = form.cleaned_data.get("customer_recovery_email")
            user_dat.customer_security_code = form.cleaned_data.get("customer_security_code")
            user_dat.customer_security_hint = form.cleaned_data.get("customer_security_hint")
            user_dat.customer_phone_no = form.cleaned_data.get("customer_phone_no")
            user_dat.customer_account_id = form.cleaned_data.get("customer_account_id")
            user_dat.customer_balance = form.cleaned_data.get("customer_balance")
            
            if(insert_user_data(user_dat)):
                val = "Account has been Created"
                return redirect("Bank:home")
            else:
                val = "Due to wrong/incorrect information account couldn't be created"
                return redirect("Bank:register")
            
           
    # form = AuthenticationForm()
    context = {}
    
    return render(
        request, 
        "register.html",
        {
            'form' : form
        }
    )


def get_loan(request):
    form = loan()
    if request.method == 'POST':
        form = Customer_Details(request=request, data=request.POST)
        
        if form.is_valid():
            user_loan = loan()
            
            if(issuse_loan(user_id, user_loan)):
                val = "Loan Provided"
            else:
                val = "Loan ca't be provided"
    
    return render(
        request, 
        "Loan/loan.html",
        {
            'form' : form
        }
    )


def profile(request):
    user_dat = get_user_info(user_id)
    return render(request, "profile.html")


def update(request):
    form = Customer_Details()
    form = get_user_info(user_id)
    return render(
        request, 
        "update.html",
        {
            'form' : form
        }
    )


def transaction(request):
    tran = transaction()
    return render(request, "transaction.html")


def remove_account(request):
    if(remove_user(user_id)):
        messages.success(request, "Account Removed successfully!")
    else:
        messages.success(request, "Can't Resmove account due to pending loan(s)")
        
    return render(request, "remove_acc.html")