from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo),
    path('register-consultee', views.register_consultee, name='register_consultee'),
    path('view-consultant/<int:pk>', views.view_consultant, name='view_consultant'),
]
