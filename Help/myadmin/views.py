from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages


def dashboard(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Customers.objects.all()
    result2 = Volunteers.objects.all()
    result5 = State.objects.all()
    result6 = City.objects.all()
    result3 = Area.objects.all()
    context = {'result':result,'result1':result1,'result2':result2,'areas':result3,'states':result5,'cities':result6}
    return render(request, 'myadmin/dashboard.html', context)

def forms(request):
    context = {}
    return render(request, 'myadmin/forms.html', context)

def tables(request):
    context = {}
    return render(request, 'myadmin/tables.html', context)

def login(request):
    context = {}
    return render(request, 'myadmin/login.html', context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    result1 = User.objects.get(username=username)

    result = auth.authenticate(request, username=username, password=password)

    if result.is_staff == 0:
        print('Invalid Username Or Password')
        messages.success(request, 'Invalid Username Or Password!!')
        return redirect('/myadmin/')
    else:
        auth.login(request, result)
        return redirect('/myadmin/dashboard')

def logout(request):
    auth.logout(request)
    return redirect('/myadmin/')

def feedback(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Feedback.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'myadmin/feedback.html', context)

def store_feedback(request):
    rating  = request.POST['rating']
    comment = request.POST['comment']
    id = request.user.id

    Feedback.objects.create(rating=rating,comment=comment,date=datetime.date.today(),user_id=id)
    messages.success(request, 'Thank you for your valuable feedback')

    return redirect('/myadmin/feedback') 

def inquiries(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Inquiry.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'myadmin/inquiries.html', context)

def store_inquiry(request):
    myuser = request.POST['uname']
    email = request.POST['email']
    contact  = request.POST['co']
    mymsg = request.POST['msg']

    Inquiry.objects.create(user_name=myuser,email=email,contact=contact,message=mymsg,date=datetime.date.today())
    return redirect('/user/contact')    

def users(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    context = {'result':result}

    result1 = Customers.objects.all()
    result2 = User.objects.all()
    context = {'result':result,'result1':result1,'result2':result2}
    return render(request, 'myadmin/users.html',context)

def more_user(request,id):
    result = Customers.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/more.html',context)

def volunteers(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    context = {'result':result}

    result1 = Volunteers.objects.all()
    result2 = User.objects.all()
    context = {'result':result,'result1':result1,'result2':result2}

    return render(request, 'myadmin/volunteers.html',context)

def more_vol(request,id):
    result = Volunteers.objects.get(pk=id)
    context = {'result':result}

    return render(request,'myadmin/more_vol.html',context)

def vol_acceptance(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Vol_acceptance.objects.all()
    context = {'result':result,'result1':result1}
    return render(request,'myadmin/vol_acceptance.html',context)

# def add_event(request):
#     context = {}
#     return render(request, 'myadmin/add_event.html', context)

def all_events(request):
    id = request.user.id
    result = User.objects.get(pk=id)

    result1 = Events.objects.all()
    result2 = User.objects.all()
    context = {'result':result,'result1':result1,'result2':result2,}
    return render(request, 'myadmin/all_events.html', context)

def accept_event(request,id):
    result = Events.objects.get(pk=id)

    title  = result.title
    des = result.description
    etype = result.event_type
    edate = result.event_date
    rdate = result.reg_date
    user = result.user.username

    U_Events.objects.create(title=title,description=des,event_type=etype,event_date=edate,reg_date=rdate,user=user)
    result.delete()
    messages.success(request, 'Event Accepted Successfully')
    return redirect('/myadmin/all_events')

def reject_event(request,id):
    result = Events.objects.get(pk=id)
    result.delete()
    messages.error(request, 'Event Rejected !!!')
    return redirect('/myadmin/all_events')

def event_details(request,id):
    result = Events.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/event_details.html',context) 

def up_events(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result2 = User.objects.all()
    result1 = U_Events.objects.all()
    context = {'result':result,'result1':result1,'result2':result2}
    return render(request,'myadmin/up_events.html',context) 

def event_detail(request,id):
    result = U_Events.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/event_detail.html',context) 

def donations(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Donate.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'myadmin/donations.html', context)  

def forgot(request):
    context = {}
    return render(request, 'myadmin/forgot.html', context)  

def more1(request):
    context = {}
    return render(request, 'myadmin/more1.html', context)   


def create_categories(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/create_categories.html',context)

def store_category(request):
    cn = request.POST['catname']

    Category.objects.create(category_name=cn)
    messages.success(request, 'Category Added Successfully')
    return redirect('/myadmin/create_categories')

def read_category(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    result1 = Category.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'myadmin/read_category.html',context)

def delete_category(request,id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/read_category')

def edit_category(request, id):
    result  = Category.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_category.html',context)

def update_category(request,id):
    data = {
                'category_name' : request.POST['catname']
           }
    Category.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/read_category')

def search(request):
    query = request.POST['search']
    result = User.objects.filter(username=query)
    context = {'result':result}
    return render(request, 'myadmin/users.html',context)

#=================================================================

def add_city_store(request):
    mycity = request.POST['city']
    mystate = request.POST['statename']

    City.objects.create(city_name = mycity,state_id=mystate)
    return redirect('/myadmin/dashboard')

def all_cities(request):
    result = City.objects.all()
    context = {'cities':result}
    return render(request, 'myadmin/all_cities.html' ,context)

def delete_city(request,id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_cities')

def edit_city(request,id):
    result = City.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_city.html', context)

def update_city(request,id):
    data = {
            'city_name' : request.POST['city']
           }

    City.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/all_cities')

#=========================================================================

def add_area_store(request):
    myarea = request.POST['area']
    mycity = request.POST['city']
    mystate = request.POST['statename']

    Area.objects.create(area_name=myarea,city_id = mycity,state_id=mystate)
    return redirect('/myadmin/dashboard')

def all_areas(request):
    result = Area.objects.all()
    context = {'areas':result}
    return render(request, 'myadmin/all_areas.html' ,context)

def delete_area(request,id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/dashboard')

def edit_area(request,id):
    result = Area.objects.get(pk=id)
    result1 = City.objects.all()
    context = {'result':result,'city':result1}
    return render(request, 'myadmin/edit_area.html', context)

def update_area(request,id):
    data = {
            'area_name' : request.POST['area'],
            'city_name' : request.POST['city']
           }

    Area.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/all_areas')


#========================================================================

def money(request):
    id = request.user.id
    result = User.objects.get(pk=id)

    result1 = Money_donation.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'myadmin/money.html', context)

