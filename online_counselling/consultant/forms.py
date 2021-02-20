from django import forms
from .models import Consultant, ConsutancyType
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
	def __init__(self, *args, **kwargs):
		super(ConsultantForm, self).__init__(*args, **kwargs)
		obj = ConsutancyType.objects.all()
		consultancy_types = []
		for i in obj:
			consultancy_types.append((i.category_type,i.category_type))
		self.fields["type_of_consultant"].widget = forms.Select(choices=consultancy_types)