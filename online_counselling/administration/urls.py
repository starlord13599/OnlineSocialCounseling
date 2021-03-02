from django.urls import path
from . import views


urlpatterns =[
	path('',views.index, name='index'),
	path('administration',views.admin_index, name='admin_index'),
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
	path('admin/edit-country/<int:pk>',views.edit_country, name='edit_country'),
	path('admin/edit-state/<int:pk>',views.edit_state, name='edit_state'),
	path('admin/add-state',views.add_state, name='add_state'),
	path('admin/view-state',views.view_state, name='view_state'),
	path('admin/add-city',views.add_city, name='add_city'),
	path('admin/view-city',views.view_city, name='view_city'),
	path('admin/view-appointments',views.view_appointments, name='view_appointments'),
	path('admin/view-complaints',views.view_complaints, name='view_complaints'),
	path('admin/view-feedbacks',views.view_feedbacks, name='view_feedbacks'),
	path('admin/delete-country/<int:pk>',views.delete_country, name='delete_country'),
	path('admin/delete-state/<int:pk>',views.delete_state, name='delete_state'),
	path('admin/get-states/<int:pk>',views.get_states, name='get_states'),
	path('admin/delete-city/<int:pk>',views.delete_city, name='delete_city'),
	path('admin/edit-city/<int:pk>',views.edit_city, name='edit_city'),
	path('admin/edit-consultancy-type/<int:pk>',views.edit_consultancy_type, name='edit_consultancy_type'),
	path('admin/delete-consultancy-type/<int:pk>',views.delete_consultancy_type, name='delete_consultancy_type'),
]