"""eclothstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('register_store', views.register_store, name='register_store'),
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),    
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('events', views.events, name='events'),
    path('events_store', views.events_store, name='events_store'),
    path('moneydonation', views.moneydonation, name='moneydonation'),
    path('moneydonation_store', views.moneydonation_store, name='moneydonation_store'),
    path('donation', views.donation, name='donation'),
    path('donation_store', views.donation_store, name='donation_store'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('success', views.success, name='success'),
    path('process_payment', views.process_payment, name='process_payment'),
    path('demo2', views.demo2, name='demo2'),
    path('demo3', views.demo3, name='demo3'),
]


