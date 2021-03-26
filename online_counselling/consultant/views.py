from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from administration.models import UserRole
from .forms import UserForm, ConsultantForm
from .models import Portfolio, Consultant

import pandas as pd

# Create your views here.
@login_required
def index(request):
    response = render(request, 'consultant/index.html')
    response.set_cookie('role', 'consultant')
    return response


def register_consultant(request):
    if request.method == 'GET':
        user_form = UserForm()
        consultant_form = ConsultantForm()
        context = {}
        context['user_form'] = user_form
        context['consultant_form'] = consultant_form
        return render(request, 'consultant/registeration-form.html', context)
    else:
        user_form = UserForm(request.POST)
        consultant_form = ConsultantForm(request.POST)
        user_role = UserRole()
        context = {}
        context['user_form'] = user_form
        context['consultant_form'] = consultant_form
        if user_form.is_valid() and consultant_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_role.user = user
            user_role.role = 'Consultant'
            user_role.save()
            consultant = consultant_form.save(commit=False)
            consultant.user = user
            consultant.ratings = 0
            consultant.number_of_reviews = 0
            consultant.number_of_customers = 0
            consultant.save()
            return redirect('login_user')
        else:
            return render(request, 'consultant/registeration-form.html', context)


@login_required
def manage_appointment(request):
    if request.COOKIES['role'] == 'consultant':
        return render(request, 'consultant/manageAppointment.html')
    else:
        print('hello world')


@login_required
def add_portfolio(request):
    if request.COOKIES['role'] == 'consultant':
        if request.method == 'GET':
            return render(request, 'consultant/addPortfolio.html')
        else:
            portfolio = Portfolio()
            portfolio.portfolio_name = request.POST['portfolio-name']
            portfolio.portfolio_description = request.POST['portfolio-description']
            portfolio.consultant = Consultant.objects.get(user=User.objects.get(username=request.user.username))
            try:
                portfolio.save()
            except:
                messages.error(request, 'Portfolio Name should be unique!!')
                return redirect('add_portfolio')

            return redirect('view_portfolio')


@login_required
def view_portfolio(request):
    if request.COOKIES['role'] == 'consultant':
        if request.method == 'GET':
            context = {}
            portfolio = Portfolio.objects.all()
            context['portfolio'] = portfolio
            return render(request, 'consultant/viewPortfolio.html', context)


def xyz(request):
    data = pd.DataFrame(list(Consultant.objects.all().values()))
    print(data)
    data.to_csv('database_data.csv')
    return 'abc'
