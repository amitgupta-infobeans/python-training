from django.urls import  re_path as url
from art_gallery import views
from django.contrib.auth.decorators import login_required


app_name = 'art_gallery'

urlpatterns = [

    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
    # all gallery at one page..
    url('public_gallery/', views.public_gallery, name='public_gallery'),
    # category wise gallery route
    url('gallery_categorywise/(?P<id>\d+)/$', views.gallery_categorywise, name='gallery_categorywise'),

    # class based view
    url(r'my_gallery/', login_required(views.GalleryListView.as_view()), name='my_gallery'),
    url(r'^create/$', login_required(views.GalleryCreateView.as_view()), name='create'),
    url(r'^update/(?P<pk>\d+)/$', login_required(views.GalleryUpdateView.as_view()), name='update'),
    # public gallery
    url(r'^gallery_details/(?P<pk>\d+)/$', views.GalleryDetailView.as_view(), name='gallery_details'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.GalleryDeleteView.as_view()), name='delete'),    
    
]

