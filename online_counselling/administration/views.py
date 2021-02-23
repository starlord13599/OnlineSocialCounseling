from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Country


# Create your views here.
def index(request):
	return render(request,'admin/index.html')


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


def approve_consultant(request):
	if request.method == 'GET':
		return render(request,'admin/approveConsultant.html')


def view_consultee(request):
	if request.method == 'GET':
		return render(request,'admin/viewConsultee.html')


def view_consultancy_type(request):
	if request.method == 'GET':
		return render(request,'admin/viewConsultancyType.html')


def add_consultancy_type(request):
	if request.method == 'GET':
		return render(request,'admin/addConsultancyType.html')


def add_country(request):
	if request.method == 'GET':
		return render(request,'admin/addCountry.html')
	else:
		print(request.POST)
		country = Country()
		country.country_name = request.POST['country-name']
		country.country_description = request.POST['country-description']
		country.save()
		messages.success(request,'Country Added Successfully')
		return render(request,'admin/addCountry.html')


def view_country(request):
	if request.method == 'GET':
		countries = Country.objects.all()
		context = {}
		context['countries'] = countries
		return render(request,'admin/viewCountry.html', context)


def add_state(request):
	if request.method == 'GET':
		return render(request,'admin/addState.html')


def view_state(request):
	if request.method == 'GET':
		return render(request,'admin/viewState.html')


def add_city(request):
	if request.method == 'GET':
		return render(request,'admin/addCity.html')


def view_city(request):
	if request.method == 'GET':
		return render(request,'admin/viewCity.html')


def view_appointments(request):
	if request.method == 'GET':
		return render(request,'admin/viewAppointments.html')


def view_complaints(request):
	if request.method == 'GET':
		return render(request,'admin/viewComplaints.html')


def view_feedbacks(request):
	if request.method == 'GET':
		return render(request,'admin/viewFeedbacks.html')


def logout_user(request):
	if request.method == 'GET':
		return render(request,'admin/login.html')


def delete_country(request,pk):
	print('In Delete Country',pk)
	Country.objects.get(id=pk).delete()
	return redirect('view_country')