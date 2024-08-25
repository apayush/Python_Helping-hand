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
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('forms', views.forms, name='forms'),
    path('tables', views.tables, name='tables'),
    
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    
    path('feedback', views.feedback, name='feedback'),    
    path('inquiries', views.inquiries, name='inquiries'),
    path('store_inquiry', views.store_inquiry, name='store_inquiry'),
    
    path('users', views.users, name='users'),
    path('more_user/<int:id>', views.more_user, name='more_user'),
   
    path('volunteers', views.volunteers, name='volunteers'),
    path('more_vol/<int:id>', views.more_vol, name='more_vol'),
    path('vol_acceptance', views.vol_acceptance, name='vol_acceptance'),
   
    # path('add_event', views.add_event, name='add_event'),
    path('event_details/<int:id>', views.event_details, name='event_details'),
    path('accept_event/<int:id>', views.accept_event, name='accept_event'),
    path('reject_event/<int:id>', views.reject_event, name='reject_event'),
    path('all_events', views.all_events, name='all_events'),
    path('up_events', views.up_events, name='up_events'),
    path('event_detail/<int:id>', views.event_detail, name='event_detail'),
    
    path('forgot', views.forgot, name='forgot'),
    path('donations', views.donations, name='donations'),
    
    path('create_categories', views.create_categories, name='create_categories'),
    path('store_category', views.store_category, name='store_category'),
    path('read_category', views.read_category, name='read_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),

    path('search', views.search, name='search'),
    path('money', views.money, name='money'),

    path('add_city_store', views.add_city_store, name='add_city_store'),
    path('all_cities', views.all_cities, name='all_cities'),
    path('update_city/<int:id>', views.update_city, name='update_city'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),

    path('add_area_store', views.add_area_store, name='add_area_store'),
    path('all_areas', views.all_areas, name='all_areas'),
    path('update_area/<int:id>', views.update_area, name='update_area'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),

]


