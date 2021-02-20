from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')


def login_user(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect('/')
			else:
				return HttpResponse('User Is Not Active.')
		else:
			messages.error(request,'Invalid Login Credentials')

		# print(request.POST)
		return redirect('login')


@login_required
def view_profile(request,id):
	return HttpResponse('Hello')


@login_required
def logout_user(request):
	logout(request)
	return redirect('/')