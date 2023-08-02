from django.urls import  re_path as url
from cbv_app import views


app_name = 'cbv_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='schoollist'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_details'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]