from distutils.command.clean import clean
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from app.models import Student
from .forms import StudentRegistration
from .models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
import random
from twilio.rest import Client

# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
    return render(request, 'signup.html')

def store(request):
    if request.method=="POST":
        sid = request.POST['sid']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            return redirect('/add')

        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if email and not re.match(EMAIL_REGEX, email):
            return redirect('/add')
       
        student = Student(sid=sid, username=username,fname=fname ,lname=lname,email=email,pass1=pass1,pass2=pass2)
        student.save()
        messages.info(request,'successfully created')
        return redirect('/show')

def login(request):
    return render(request,'login.html')

otps = random.randint(1000,9999)   # global variable define OTP generate

def login_check(request):
    #for OTP
    from twilio.rest import Client 
    account_sid = 'ACa93a52f47e0b0a87eb3e46593a47f1ee' 
    auth_token = "a85a9d300a50a8bc6c2c589a078b5d74" 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(   
                                body = "Your OTP is, {}. ".format(otps),
                                from_= "+18646607829",      
                                to='+917722817023'  
                          ) 
    # print(message.sid)
    # print("Success")

    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')
        student = Student.objects.filter(email=email).first() 
        try:
            e = student.email
            p = student.pass1
            n = student.fname
            id =student.sid
        except:
            return redirect('/add')
        # print(n)
        request.session['user_id'] = id   # session start
        # return HttpResponse(n)
        if e==email and p==passw:
            messages.success(request, 'you are logged in successfully')
            # return redirect('/show',{'n':n})   # this is use ,if you are not use otp verification
            return render(request,'otp.html')
        else:
            return redirect('/login')

def verification(request):
            if request.method == "POST":
                otp = request.POST.get('otp')
                # print("your otps is ",otps)
                # print("otp is",otp)
                ottp = int(otp)
                if otps == ottp:
                    return redirect('/show')
            # messages.error(request,'Wrong OTP')
            return render(request,'otp.html')

def show(request):
    user_id = request.session.get('user_id')    # get session
    # return HttpResponse(user_id)
    if user_id== None:
       return redirect('/login')

    userdetail = Student.objects.filter(sid=user_id).first()
    student = Student.objects.all()
    return render(request,'show.html',{'student':student,'userdetail':userdetail})
    
def edit(request, id):
    student = Student.objects.get(sid=id)
    return render(request,'update.html',{'student':student})
        
def update(request): 
     if request.method == "POST":
        id = request.POST['sid']
        contacts = Student.objects.get(sid=id)
        contacts.username = request.POST['username']
        contacts.fname = request.POST['fname']
        contacts.lname = request.POST['lname']
        contacts.email = request.POST['email']
        contacts.pass1 = request.POST['pass1']
        contacts.pass2 = request.POST['pass2']
        contacts.save()
        return redirect('/show')

def logout(request):
    del request.session['user_id']   # delete session
    return redirect('/login')
       
def delete(request, id):
    student = Student.objects.get(sid=id)
    student.delete()
    return redirect('/show')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pm)
            reg.save()
    else:
        fm = StudentRegistration()
    return render(request,'registration.html',{'form':fm})
    
