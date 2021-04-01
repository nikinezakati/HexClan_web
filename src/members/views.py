from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import SignupForm
import re 

def Home(request):
	return render(request, 'members/home.html')

def Signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'form' : form}
	return render(request, 'members/signup.html',context)

def Login(request):
	if request.method == 'POST':
		username = request.POST.get('username');
		password = request.POST.get('password');
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return Dashboard(request, user.username);
		else:
			messages.info(request, 'Username or password is not correct')

	context = {}
	return render(request, 'members/login.html', context)

@login_required(login_url = 'login')
def Dashboard(request, pk1):
	member = User.objects.get(username = pk1) 
	context = {'member' : member}
	return render(request, 'members/dashboard.html',context)

@login_required(login_url = 'login')
def Logout(request):
	logout(request)
	return redirect('login')