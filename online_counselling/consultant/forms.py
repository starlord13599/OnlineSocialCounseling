from django import forms
from .models import Consultant
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username','email','password','first_name','last_name']


class DateInput(forms.DateInput):
    input_type = 'date'

class ConsultantForm(forms.ModelForm):
	class Meta:
		model = Consultant
		exclude = ['user','ratings','number_of_reviews','number_of_customers']
		widgets = {
            'date_of_birth': DateInput()
        }