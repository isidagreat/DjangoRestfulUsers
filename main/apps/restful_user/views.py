from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
	qs = User.objects.all()
	context = {'users' : qs}
	return render(request, "restful_user/index.html",context)

def new(request):
	# Pass the post data to models method validator
	return render(request, "restful_user/newUser.html")

def edit(request, id):
	print(id)
	qs = User.objects.get(id = id)
	context = {'user' : qs}
	return render(request, "restful_user/editUser.html", context)

def update(request):
	errors = User.objects.basic_validator(request.POST)
	id = request.POST['id']
	# check if there are any errors
	if len(errors):
		# if there are errors loop through key value pairs
		for key, value in errors.items():
			messages.error(request,value)
			# redirect to new user form
		return redirect(edit, id)
	else:
		# if th errors object is empty, there are no errors
		# retrieve the blog and make changes
		updateuser = User.objects.get(id = id)
		print(updateuser)
		updateuser.first_name = request.POST['fname']
		updateuser.last_name = request.POST['lname']
		updateuser.email = request.POST['email']
		updateuser.save()
		messages.success(request,"Added new user")
		return redirect(show, id)

def destroy(request, id):
	qs = User.objects.get(id = id)
	qs.delete()
	return redirect(index)

def show(request, id):
	print(id)
	qs = User.objects.get(id = id)
	context = {'user' : qs}
	return render(request, "restful_user/displayUser.html", context)

def create(request):
	errors = User.objects.basic_validator(request.POST)
	# check if there are any errors
	if len(errors):
		# if there are errors loop through key value pairs
		for key, value in errors.items():
			messages.error(request,value)
		# redirect to new user form
		return redirect(newUser)
	else:
		# if th errors object is empty, there are no errors
		# retrieve the blog and make changes
		newuser = User(first_name = request.POST['fname'], last_name= request.POST['lname'], email = request.POST['email'])
		print(newuser)
		newuser.save()
		messages.success(request,"Added new user")
		return redirect(index)