from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('', views.LOGIN, name='login'),
    path('registration_page', views.Registration, name='registration_page'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    path('save_profile', views.save_user_profile, name='save_profile')




]