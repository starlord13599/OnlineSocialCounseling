from django.urls import path
from . import views


urlpatterns =[
	path('',views.demo),
	path('register-consultant',views.register_consultant,name='register_consultant'),
]