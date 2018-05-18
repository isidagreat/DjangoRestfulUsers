from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
	def basic_validator(self, postData):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = {}
		if len(postData['fname']) < 2:
			errors['fname'] = "First Name should be more than 2 Characters"
		if len(postData['lname']) < 2:
			errors['lname'] = "Last Name should be more than 2 Characters"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Email not correct format"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# connect an instance of BlogManager to our blog Model
	objects = UserManager()