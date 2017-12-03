# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, 'core/index.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			messages.add_message(request, messages.SUCCESS, 'Welcome, {}!'.format(username))
			return redirect('index')
		else:
			pass
			# show error message 
	return render(request, 'core/login.html')

def logout(request):
	auth_logout(request)
	messages.add_message(request, messages.SUCCESS, 'Successfully Logged Out!')
	return redirect('index')
