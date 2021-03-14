from django.contrib.auth.models import User
from django.db import models

from consultant.models import Consultant
from consultee.models import Consultee


# Create your models here.

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=150)

    class Meta:
        db_table = 'user_roles'


class Slot(models.Model):
    date_time_stamp = models.DateTimeField()
    remark = models.CharField(max_length=250)

    class Meta:
        db_table = 'slot'


class Appointment(models.Model):
    date_time_stamp = models.DateTimeField()
    remark = models.CharField(max_length=250)

    class Meta:
        db_table = 'appointment'


class Feedback(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    consultee = models.ForeignKey(Consultee, on_delete=models.CASCADE)
    remark = models.CharField(max_length=250)

    class Meta:
        db_table = 'feedback'


class Country(models.Model):
    country_name = models.CharField(max_length=150, unique=True)
    country_description = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'countries_list'


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=150, unique=True)
    state_description = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'states_list'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=150, unique=True)
    city_description = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'cities_list'
