from django.urls import re_path as url
from second_app import views


app_name = 'amitsecondapp'

urlpatterns = [
    url('second_app_users', views.second_app_users, name='second_app_users'),
    url('', views.index, name='index'),
]