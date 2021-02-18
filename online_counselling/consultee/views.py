from django.shortcuts import render, HttpResponse, redirect
from .forms import ConsulteeForm
from consultant.forms import UserForm

# Create your views here.
def demo(request):
	return HttpResponse('In Consultee')

def register_consultee(request):
	if request.method == 'GET':
		user_form = UserForm()
		consultee_form = ConsulteeForm()
		context = {}
		context['user_form'] = user_form
		context['consultee_form'] = consultee_form
		return render(request,'consultee/registeration-form.html',context)
	else:
		user_form = UserForm(request.POST)
		consultee_form = ConsulteeForm(request.POST)
		context = {}
		context['user_form'] = user_form
		context['consultee_form'] = consultee_form
		if user_form.is_valid() and consultee_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			consultee = consultee_form.save(commit=False)
			consultee.user = user
			consultee.ratings = 0
			consultee.number_of_reviews = 0
			consultee.number_of_customers = 0
			consultee.save()
			return redirect('index')
		else:
			return render(request,'consultee/registeration-form.html',context)