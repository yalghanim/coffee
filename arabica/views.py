from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout 


def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form
	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save(commit=False) #so we can retrieve the object
			username = user.username
			password = user.password
			email = user.email
			first_name = user.first_name
			last_name = form.last_name
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)
			return redirect("arabica:home")
		else:
			messages.error(request, form.errors)
			return redirect("arabica:signup")

	return render(request, 'signup.html', context)

def userlogout(request):
	logout(request)
	return redirect("arabica:home")

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('arabica:home')

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect("arabica:login")
		messages.error(request, form.errors)
		return redirect("arabica:login")
	return render(request, 'login.html', context)

def home(request):
	return render(request, 'home.html', {})