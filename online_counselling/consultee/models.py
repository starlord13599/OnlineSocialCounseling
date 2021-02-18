from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def phone_validator(value):
	if len(str(value)) == 10:
		pass
	else:
		raise ValidationError('Phone Number sholud be of 10 digits')



class Consultee(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	phone_no = models.CharField(max_length=10,validators=[phone_validator])
	email_id = models.EmailField()
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	date_of_birth = models.DateField()

	class Meta:
		db_table = 'consultee_details'