from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Country, State, City
import json


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
		# print(request.POST)
		country = Country()
		country.country_name = request.POST['country-name']
		country.country_description = request.POST['country-description']
		country.save()
		messages.success(request,'Country Added Successfully')
		return redirect('view_country')


def view_country(request):
	if request.method == 'GET':
		countries = Country.objects.all()
		context = {}
		context['countries'] = countries
		return render(request,'admin/viewCountry.html', context)


def add_state(request):
	if request.method == 'GET':
		countries = Country.objects.all()
		context = {}
		context['countries'] = countries
		return render(request, 'admin/addState.html', context)
	else:
		country = Country.objects.get(id=request.POST['country'])
		state = State()
		state.country = country
		state.state_name = request.POST['state-name']
		state.state_description = request.POST['state-description']
		state.save()
		return redirect('view_state')


def view_state(request):
	if request.method == 'GET':
		states = State.objects.all()
		context = {}
		context['states'] = states
		return render(request, 'admin/viewState.html', context)


def add_city(request):
	if request.method == 'GET':
		countries = Country.objects.all()
		context = {}
		context['countries'] = countries
		return render(request, 'admin/addCity.html', context)
	else:
		print(request.POST)
		country = Country.objects.get(id=request.POST['country'])
		state = State.objects.get(id=request.POST['state'])
		city = City()
		city.country = country
		city.state = state
		city.city_name = request.POST['city-name']
		city.city_description = request.POST['city-description']
		city.save()
		return redirect('view_city')



def view_city(request):
	if request.method == 'GET':
		cities = City.objects.all()
		context = {}
		context['cities'] = cities
		return render(request,'admin/viewCity.html', context)


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


def edit_country(request,pk):
	country = Country.objects.get(id=pk)
	if request.method == 'GET':
		context = {}
		context['country'] = country
		return render(request, 'admin/editCountry.html', context)
	else:
		country.country_name = request.POST['country-name']
		country.country_description = request.POST['country-description']
		country.save()
		return redirect('view_country')


def delete_state(request,pk):
	State.objects.get(id=pk).delete()
	return redirect('view_state')


def edit_state(request,pk):
	countries = Country.objects.all()
	state = State.objects.get(id=pk)
	if request.method == 'GET':
		context = {}
		context['countries'] = countries
		context['state'] = state
		return render(request, 'admin/editState.html', context)
	else:
		state.country = Country.objects.get(id=request.POST['country'])
		state.state_name = request.POST['state-name']
		state.state_description = request.POST['state-description']
		state.save()
		return redirect('view_state')



def get_states(request, pk):
	country = Country.objects.get(id=pk)
	states = list(State.objects.filter(country=country).values())
	return HttpResponse(json.dumps(states))



def delete_city(request,pk):
	City.objects.get(id=pk).delete()
	return redirect('view_city')



def edit_city(request,pk):
	countries = Country.objects.all()
	states = State.objects.all()
	city = City.objects.get(id=pk)
	if request.method == 'GET':
		context = {}
		context['countries'] = countries
		context['states'] = states
		context['city'] = city
		return render(request, 'admin/editCity.html', context)
	else:
		city.country = Country.objects.get(id=request.POST['country'])
		city.state = State.objects.get(id=request.POST['state'])
		city.city_name = request.POST['city-name']
		city.city_description = request.POST['city-description']
		city.save()
		return redirect('view_city')
