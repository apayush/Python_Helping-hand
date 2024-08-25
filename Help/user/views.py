from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages

import razorpay
from django.views.decorators.csrf import csrf_exempt

def demo(request):
    context = {}
    return render(request, 'user/demo.html', context)

def home(request):
    result = User.objects.all()
    context = {'result':result}
    return render(request, 'user/home.html', context)

def about(request):
    context = {}
    return render(request, 'user/about.html', context)

def contact(request):
    context = {}
    return render(request, 'user/contact.html', context)

def register(request):
    result = Area.objects.all()
    result1 = City.objects.all()
    result2 = State.objects.all()
    context = {'areas':result,'cities':result1,'states':result2}
    return render(request, 'user/register.html', context)

def register_store(request):
    # User Model
    fname     = request.POST['fname']
    lname     = request.POST['lname']
    email     = request.POST['email']
    username  = request.POST['username']
    password  = request.POST['password']
    cpassword = request.POST['cpassword']

    #Customers Model
    dob = request.POST['dob']
    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area']

    if password == cpassword:
        result = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
        Customers.objects.create(dob=dob,contact=contact,address=address,gender=gender,reg_date=datetime.date.today(),state=state,city=city,area=area,user_id=result.id)
        return redirect('/user/')
    else:
        print('Missmatch Password')

def login(request):
    context = {}
    return render(request, 'user/login.html', context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/user/')
    else:
        if Volunteers.objects.filter(user_id=result.id).exists():
            return redirect('/user/')
        elif Customers.objects.filter(user_id=result.id).exists():
            auth.login(request,result)
            return redirect('/user/home')
        else:
            return redirect('/user/')

def logout(request):
    auth.logout(request)
    return redirect('/user/')

def feedback(request):
    context = {}
    return render(request, 'user/feedback.html', context)

def feedback_store(request):
    rating  = request.POST['rating']
    comment = request.POST['comment']
    id = request.user.id

    Feedback.objects.create(rating=rating,comment=comment,date=datetime.date.today(),user_id=id)
    messages.success(request, 'Thank you for your valuable feedback')

    return redirect('/user/feedback')

def events(request):
    context = {}
    return render(request, 'user/events.html', context)

def events_store(request):
    title  = request.POST['title']
    des = request.POST['des']
    etype = request.POST['etype']
    edate = request.POST['edate']
    id = request.user.id

    Events.objects.create(title=title,description=des,event_type=etype,event_date=edate,reg_date=datetime.date.today(),user_id=id)
    messages.success(request, 'request sent successfully.')

    return redirect('/user/events')

def moneydonation(request):
    context = {}
    return render(request, 'user/moneydonation.html', context)

def moneydonation_store(request):
    amount = request.POST['ammo']
    des = request.POST['des']
    id = request.user.id

    Money_donation.objects.create(ammount=amount,description=des,date=datetime.date.today(),user_id=id)    
    messages.success(request,'Money Donated successfully.')

    request.session['price'] = amount

    return redirect('/user/process_payment')

def donation(request):
    result = Category.objects.all()
    result1 = Area.objects.all()
    result2 = City.objects.all()
    context = {'categories':result,'areas':result1,'cities':result2}
    return render(request, 'user/donation.html', context)

def donation_store(request):
    title  = request.POST['title']
    des = request.POST['des']
    cat = request.POST['cat']
    cper = request.POST['cper']
    cco = request.POST['cco']
    add = request.POST['add']
    city = request.POST['city']
    area = request.POST['area']
    id = request.user.id

    Donate.objects.create(title=title,description=des,address=add,donation_date=datetime.date.today(),don_category=cat,user_id=id,city_id=city,area_id=area,contact_no=cco,contact_person=cper)
    messages.success(request, 'Donation Post sent successfully.')

    return redirect('/user/donation')

def demo2(request):
    context = {}
    return render(request, 'user/demo2.html', context)

def demo3(request):
    context = {}
    return render(request, 'user/demo3.html', context)
    
def profile(request,id):
    fkid = request.user.id
    result1 = User.objects.get(pk=id)
    result = Customers.objects.get(user_id=fkid)
    context = {'result':result}
    return render(request, 'user/profile.html', context)

def profile_store(request):
    myfile = request.FILES['f']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'profile')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name, myfile)

    # Fileinfo.objects.create(file_name=myfile.name)
    return redirect('/user/profile')

def edit_profile(request,id):
    fkid = request.user.id
    result1 = User.objects.get(pk=id)
    result = Customers.objects.get(user_id=fkid)
    context = {'result':result}
    return render(request, 'user/edit_profile.html', context)


def update_profile(request,id):
    user = request.user.id
    result = Customers.objects.get(pk=id)
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
    Customers.objects.update_or_create(pk=id, defaults=data1)

    return redirect('/user/home')


def process_payment(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int(request.session['price']) * 100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"HelpingHand",
        "notes":{
            'name' : 'AK',
            'payment_for':'NGO Test'
        }
    }
    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'user/process_payment.html',context)

@csrf_exempt
def success(request):
    return render(request, "user/success.html")
    