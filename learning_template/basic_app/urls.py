from django.urls import re_path as url
from basic_app import views

# TEMPLATE TAGGING....
app_name = 'basic_app'

urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),
]