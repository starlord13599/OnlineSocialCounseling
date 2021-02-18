from django import forms
from .models import Consultee


class DateInput(forms.DateInput):
    input_type = 'date'

class ConsulteeForm(forms.ModelForm):
	class Meta:
		model = Consultee
		exclude = ['user']
		widgets = {
            'date_of_birth': DateInput()
        }