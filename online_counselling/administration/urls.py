from django.urls import path
from . import views


urlpatterns =[
	path('',views.index, name='index'),
	path('register/',views.register, name='register'),
	path('login/',views.login_user, name='login'),
	path('profile/<int:id>', views.view_profile, name='profile'),
	path('logout/', views.logout_user, name='logout'),
]