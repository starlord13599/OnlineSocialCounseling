from django.urls import path
from . import views


urlpatterns =[
	path('',views.index, name='consultant_index'),
	path('register-consultant', views.register_consultant, name='register_consultant'),
	path('manage-appointment', views.manage_appointment, name='manage_appointment'),
	path('add-portfolio', views.add_portfolio, name='add_portfolio'),
	path('view-portfolio', views.view_portfolio, name='view_portfolio'),
]