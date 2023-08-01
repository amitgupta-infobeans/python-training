from django.urls import  re_path as url
from basic_app import views


app_name = 'basic_app'

urlpatterns = [

    url('register/', views.register, name='register'),
    url('aboutus/', views.aboutus, name='aboutus'),
    url('user_login/', views.user_login, name='user_login'),
]