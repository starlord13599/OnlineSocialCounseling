from django.urls import path
from . import views

urlpatterns =[
	path('',views.demo),
	path('register-consultee',views.register_consultee,name='register_consultee'),
]