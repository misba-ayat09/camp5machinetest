from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('flight_list/', views.flight_list, name='flight_list'),
    path('flight_add/', views.flight_add, name='flight_add'),
    path('flight_search/', views.flight_search, name='flight_search'),
    path('flight_edit/<int:pk>/', views.flight_edit, name='flight_edit'),
    path('logout/', views.logout, name='logout'),
]