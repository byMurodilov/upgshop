from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('register', views.register, name='register'),
    path('log-in', views.log_in, name='log_in'),
    path('log-out', views.log_out, name='log_out')
]