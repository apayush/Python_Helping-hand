from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages
from datetime import datetime

def home(request):
    context = {}
    return render(request, 'volunteer/home.html', context)

def about(request):
    context = {}
    return render(request, 'volunteer/about.html', context)

def contact(request):
    context = {}
    return render(request, 'volunteer/contact.html', context)

def register(request):
    result = Area.objects.all()
    result1 = City.objects.all()
    result2 = State.objects.all()
    context = {'areas':result,'cities':result1,'states':result2}
    return render(request, 'volunteer/register.html', context)

def register_store(request):
    # User Model
    fname     = request.POST['fname']
    lname     = request.POST['lname']
    email     = request.POST['email']
    username  = request.POST['username']
    password  = request.POST['password']
    cpassword = request.POST['cpassword']

    #Volunteers Model
    dob = request.POST['dob']
    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area']

    if password == cpassword:
        result = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
        Volunteers.objects.create(dob=dob,contact=contact,address=address,gender=gender,reg_date=datetime.today(),state=state,city=city,area=area,user_id=result.id)
        return redirect('/volunteer/')
    else:
        print('Missmatch Password')

def login(request):
    context = {}
    return render(request, 'volunteer/login.html', context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/volunteer/')
    else:
        if Customers.objects.filter(user_id=result.id).exists():
            return redirect('/volunteer/')
        elif Volunteers.objects.filter(user_id=result.id).exists():
            auth.login(request,result)
            return redirect('/volunteer/home')
        else:
            return redirect('/volunteer/')

def logout(request):
    auth.logout(request)
    return redirect('/volunteer/')

def feedback(request):
    context = {}
    return render(request, 'volunteer/feedback.html', context)

def feedback_store(request):
    rating  = request.POST['rating']
    comment = request.POST['comment']
    id = request.user.id

    Feedback.objects.create(rating=rating,comment=comment,date=datetime.today(),user_id=id)
    messages.success(request, 'Thank you for your valuable feedback')

    return redirect('/volunteer/feedback')


def forget(request):
    context = {}
    return render(request, 'volunteer/forget.html', context)

def profile(request,id):
    fkid = request.user.id
    result1 = User.objects.get(pk=id)
    result = Volunteers.objects.get(user_id=fkid)
    context = {'result':result}
    return render(request, 'volunteer/profile.html', context)

def edit_profile(request,id):
    fkid = request.user.id
    result1 = User.objects.get(pk=id)
    result = Volunteers.objects.get(user_id=fkid)
    context = {'result':result}
    return render(request, 'volunteer/edit_profile.html', context)


def update_profile(request,id):
    user = request.user.id
    result = Volunteers.objects.get(pk=id)
    data = {
                'fname': request.POST['fname'],
                'lname': request.POST['lname'],
                'email': request.POST['email'],
                'username': request.POST['username']

            }

    data1 = {
                'contact': request.POST['contact'],
                'address': request.POST['address'],  
                'dob': request.POST['dob'],
                'gender': request.POST['gender']
    }

    result = User.objects.update_or_create(pk=user, defaults=data)
    Volunteers.objects.update_or_create(pk=id, defaults=data1)
    return redirect('/volunteer/home')

def donate(request):
    result = Donate.objects.all()
    context = {'result':result}
    return render(request, 'volunteer/donate.html', context)

def vol_accept(request,id):
    user_id = request.user.id
    Vol_acceptance.objects.create(donate_id=id,user_id=user_id,received_dt='',delivered_dt='')
    context = {}
    return redirect('/volunteer/accepted_post')

def accepted_post(request):
    results = Vol_acceptance.objects.all()
    context = {'results':results}
    return render(request, 'volunteer/accepted_post.html', context)

def ac_post(request,id):
    result = Vol_acceptance.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'volunteer/ac_post.html', context)

def received(request,id):
    context = {'donation_id':id}
    return render(request, 'volunteer/received.html', context)

def received_post(request,id):
    received_dt = datetime.today()
    received_remarks = request.POST['remarks']

    data = {
              'received_dt':received_dt,
              'received_remarks':received_remarks
           }

    Vol_acceptance.objects.update_or_create(pk=id,defaults=data)
    messages.success(request, 'Remarks updated Successfully.')
    return redirect('/volunteer/accepted_post')

def delivered(request,id):
    context = {'donation_id':id}
    return render(request, 'volunteer/delivered.html', context)

def delivered_post(request,id):
    delivered_dt = datetime.today()
    delivered_remarks = request.POST['remarks']

    data = {
              'delivered_dt':delivered_dt,
              'delivered_remarks':delivered_remarks
           }

    Vol_acceptance.objects.update_or_create(pk=id,defaults=data)
    messages.success(request, 'Remarks updated Successfully.')
    return redirect('/volunteer/accepted_post')

def store_inquiry(request):
    myuser = request.POST['uname']
    email = request.POST['email']
    contact  = request.POST['co']
    mymsg = request.POST['msg']

    Inquiry.objects.create(user_name=myuser,email=email,contact=contact,message=mymsg,date=datetime.today())
    return redirect('/volunteer/contact') 


