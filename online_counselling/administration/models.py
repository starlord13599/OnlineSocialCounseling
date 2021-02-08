from django.db import models
from consultant.models import Consultant
from consultee.models import Consultee

# Create your models here.


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
	consultant = models.ForeignKey(Consultant,on_delete=models.CASCADE)
	consultee = models.ForeignKey(Consultee,on_delete=models.CASCADE)
	remark = models.CharField(max_length=250)

	class Meta:
		db_table = 'feedback'