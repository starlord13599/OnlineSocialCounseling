from django.urls import path
from . import views


urlpatterns =[
	path('',views.index, name='index'),
	path('administration',views.administration_index, name='administration_index'),
	path('register/',views.register, name='register'),
	path('login/',views.login_user, name='login_user'),
	path('profile/<int:id>', views.view_profile, name='profile'),
	path('logout/', views.logout_user, name='logout_user'),
	path('administration/approve-consultant',views.approve_consultant, name='approve_consultant'),
	path('administration/view-consultee',views.view_consultee, name='view_consultee'),
	path('administration/view-consultancy-type',views.view_consultancy_type, name='view_consultancy_type'),
	path('administration/add-consultancy-type',views.add_consultancy_type, name='add_consultancy_type'),
	path('administration/add-country',views.add_country, name='add_country'),
	path('administration/view-country',views.view_country, name='view_country'),
	path('administration/edit-country/<int:pk>',views.edit_country, name='edit_country'),
	path('administration/edit-state/<int:pk>',views.edit_state, name='edit_state'),
	path('administration/add-state',views.add_state, name='add_state'),
	path('administration/view-state',views.view_state, name='view_state'),
	path('administration/add-city',views.add_city, name='add_city'),
	path('administration/view-city',views.view_city, name='view_city'),
	path('administration/view-appointments',views.view_appointments, name='view_appointments'),
	path('administration/view-complaints',views.view_complaints, name='view_complaints'),
	path('administration/view-feedbacks',views.view_feedbacks, name='view_feedbacks'),
	path('administration/delete-country/<int:pk>',views.delete_country, name='delete_country'),
	path('administration/delete-state/<int:pk>',views.delete_state, name='delete_state'),
	path('administration/get-states/<int:pk>',views.get_states, name='get_states'),
	path('administration/delete-city/<int:pk>',views.delete_city, name='delete_city'),
	path('administration/edit-city/<int:pk>',views.edit_city, name='edit_city'),
	path('administration/edit-consultancy-type/<int:pk>',views.edit_consultancy_type, name='edit_consultancy_type'),
	path('administration/delete-consultancy-type/<int:pk>',views.delete_consultancy_type, name='delete_consultancy_type'),
]