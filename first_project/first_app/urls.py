from django.urls import  re_path as url
from first_app import views

urlpatterns = [

    url('aboutus', views.aboutus, name='aboutus'),
    url('/', views.index, name='index'),
    

]