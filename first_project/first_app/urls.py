from django.urls import  re_path as url
from first_app import views

app_name = 'amitfirstapp'

urlpatterns = [
    
    url('aboutus', views.aboutus, name='aboutus'),
    url('help', views.helppage, name='help'),
    url('', views.index, name='index'),

   
    

]