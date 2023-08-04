from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from art_gallery.models import Category,GalleryModel
from . import models
from art_gallery.forms import UserForm, UserProfileInfoForm

from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                  CreateView, DeleteView, UpdateView)

from django.urls import reverse_lazy


#forlogin
from django.contrib.auth import authenticate, login , logout 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#  home page method
def index(request):

    all_category = Category.objects.order_by('name')
    return render(request, 'index.html', context={'category':all_category})

#  Registeration method
def register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_user_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and  profile_user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_user_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            register = True        
        else:
            print(user_form.errors, profile_user_form.errors)
    else:
        user_form          =  UserForm()
        profile_user_form  =  UserProfileInfoForm()
    return render(request, 'register.html', context={'user_form':user_form, 'profile_user_form': profile_user_form, 'register':register})


# login method
def user_login(request):

    errorss = ""
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password )

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                errorss = "Account is not active..."
        else:
            print("Someone try to login and failed...")
            print("Username {} and Password {} ".format(username, password) )
            errorss = "Invalid username or password"
    
    return render(request, 'login.html', context={'errors':errorss})


#  logout method
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# public gallery method
def public_gallery(request):
    all_gallery_data = GalleryModel.objects.all()
    return render(request, 'public_gallery.html', context={'all_data':all_gallery_data})



# CBV based section----------
# Create a new gallery method
class GalleryCreateView(CreateView):
    fields = ('desc', 'gallery_img', 'categoryid')
    model = GalleryModel

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userid = request.user 
            obj.save()

        return redirect('art_gallery:my_gallery')  

    
# Update Gallery Method
class GalleryUpdateView(UpdateView):
    fields = ('desc', 'gallery_img', 'categoryid')
    model = models.GalleryModel


# List all the gallery method
class GalleryListView(ListView):
    context_object_name = 'gallerymodel_list'
    template_name = 'gallerymodel_list.html'

    def get_queryset(self, *args, **kwargs):
       return GalleryModel.objects.filter(userid = self.request.user.id)


# view one gallery in details method.
class GalleryDetailView(DetailView):
    context_object_name = 'gallery_details'
    model = models.GalleryModel
    template_name = 'art_gallery/gallerymodel_details.html'


# to delete gallery
class GalleryDeleteView(DeleteView):    
    model = models.GalleryModel
    success_url = reverse_lazy('art_gallery:my_gallery')
    template_name = 'art_gallery/gallery_confirm_delete.html'


# Show all gallery category wise..
def gallery_categorywise(request, id):
    all_gallery_data = GalleryModel.objects.filter(categoryid = id )
    return render(request, 'public_gallery.html', context={'all_data':all_gallery_data})

