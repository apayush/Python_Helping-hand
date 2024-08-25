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
from volunteer import views

urlpatterns = [
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
        path('forget', views.forget, name='forget'),
        path('profile', views.profile, name='profile'),
        path('donate', views.donate, name='donate'),
        path('profile/<int:id>', views.profile, name='profile'),
        path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
        path('update_profile/<int:id>', views.update_profile, name='update_profile'),
        path('store_inquiry', views.store_inquiry, name='store_inquiry'),
        path('vol_accept/<int:id>', views.vol_accept, name='vol_accept'),
        path('accepted_post', views.accepted_post, name='accepted_post'),
        path('ac_post/<int:id>', views.ac_post, name='ac_post'),
        path('received_post/<int:id>', views.received_post, name='received_post'),
        path('received/<int:id>', views.received, name='received'),
        path('delivered_post/<int:id>', views.delivered_post, name='delivered_post'),
        path('delivered/<int:id>', views.delivered, name='delivered'),
        
]


