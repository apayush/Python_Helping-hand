from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	category_name = models.CharField(max_length=30)

	class Meta:
		db_table = 'category'

class Inquiry(models.Model):
	user_name = models.CharField(max_length=30)
	email = models.CharField(max_length=40)
	contact = models.CharField(max_length=10)
	message = models.TextField()
	date = models.DateField()

	class Meta:
		db_table = 'inquiry'

class State(models.Model):
	state_name = models.CharField(max_length=30)

	class Meta:
		db_table = 'state'

class City(models.Model):
	city_name = models.CharField(max_length=30)
	state = models.ForeignKey(State, on_delete=models.CASCADE)

	class Meta:
		db_table = 'city'

class Area(models.Model):
	area_name = models.CharField(max_length=30)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	state = models.ForeignKey(State, on_delete=models.CASCADE)

	class Meta:
		db_table = 'area'

class Customers(models.Model):
	dob = models.DateField()
	address = models.TextField()
	contact = models.CharField(max_length=10,default=None)
	gender = models.CharField(max_length=10)
	reg_date = models.DateField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	state = models.CharField(max_length=10,default=None)
	city = models.CharField(max_length=10,default=None)
	area = models.CharField(max_length=10,default=None)

	class Meta:
		db_table = 'customers'

class Volunteers(models.Model):
	dob = models.DateField()
	address = models.TextField()
	contact = models.CharField(max_length=10,default=None)
	gender = models.CharField(max_length=10)
	reg_date = models.DateField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	state = models.CharField(max_length=10,default=None)
	city = models.CharField(max_length=10,default=None)
	area = models.CharField(max_length=10,default=None)

	class Meta:
		db_table = 'volunteers'


class Feedback(models.Model):
	rating  = models.CharField(max_length=20)
	comment = models.TextField()
	user    = models.OneToOneField(User,on_delete=models.CASCADE)
	date    = models.DateField()

	class Meta:
		db_table = 'feedback'

class Events(models.Model):
	title       = models.CharField(max_length=30)
	description = models.TextField()
	event_type  = models.CharField(max_length=30)
	event_date  = models.DateField()
	reg_date    = models.DateField()
	user        = models.ForeignKey(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'events'

class U_Events(models.Model):
	title       = models.CharField(max_length=30)
	description = models.TextField()
	event_type  = models.CharField(max_length=30)
	event_date  = models.DateField()
	reg_date    = models.DateField()
	user        = models.CharField(max_length=30)

	class Meta:
		db_table = 'upcoming_events'

class Donate(models.Model):
	title       = models.CharField(max_length=30)
	description = models.TextField()
	don_category  = models.CharField(max_length=30)
	contact_person = models.CharField(max_length=30,default=None)
	contact_no  = models.CharField(max_length=30,default=None)
	address 	= models.TextField()
	city       = models.ForeignKey(City,on_delete=models.CASCADE)
	area    = models.ForeignKey(Area,on_delete=models.CASCADE)
	donation_date  = models.DateField(default=None)
	user        = models.ForeignKey(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'donate'

class Vol_acceptance(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	donate = models.OneToOneField(Donate,on_delete=models.CASCADE,default='')
	received_dt = models.CharField(max_length=20)
	received_remarks = models.TextField(default='')
	delivered_dt = models.CharField(max_length=20)
	delivered_remarks = models.TextField(default='')

	class Meta:
		db_table = 'vol_acceptance'

class Money_donation(models.Model):
	ammount = models.CharField(max_length=20)
	description = models.TextField()
	user    = models.ForeignKey(User,on_delete=models.CASCADE)
	date    = models.DateField()

	class Meta:
		db_table = 'money_donation'