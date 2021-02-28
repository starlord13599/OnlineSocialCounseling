from django.urls import path
from . import views


urlpatterns =[
	path('',views.index),
	path('register-consultant', views.register_consultant, name='register_consultant'),
	path('manage-appointment', views.manage_appointment, name='manage_appointment'),
]