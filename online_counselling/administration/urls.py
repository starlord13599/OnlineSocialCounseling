from django.urls import path
from . import views


urlpatterns =[
	path('',views.index, name='index'),
	path('register/',views.register, name='register'),
	path('login/',views.login_user, name='login'),
	path('profile/<int:id>', views.view_profile, name='profile'),
	path('logout/', views.logout_user, name='logout'),
	path('admin/approve-consultant',views.approve_consultant, name='approve_consultant'),
	path('admin/view-consultee',views.view_consultee, name='view_consultee'),
	path('admin/view-consultancy-type',views.view_consultancy_type, name='view_consultancy_type'),
	path('admin/add-consultancy-type',views.add_consultancy_type, name='add_consultancy_type'),
	path('admin/add-country',views.add_country, name='add_country'),
	path('admin/view-country',views.view_country, name='view_country'),
	path('admin/add-state',views.add_state, name='add_state'),
	path('admin/view-state',views.view_state, name='view_state'),
	path('admin/add-city',views.add_city, name='add_city'),
	path('admin/view-city',views.view_city, name='view_city'),
	path('admin/view-appointments',views.view_appointments, name='view_appointments'),
	path('admin/view-complaints',views.view_complaints, name='view_complaints'),
	path('admin/view-feedbacks',views.view_feedbacks, name='view_feedbacks'),
	path('admin/logout',views.logout_user, name='logout_user'),
	path('admin/delete-country/<int:pk>',views.delete_country, name='delete_country'),
]