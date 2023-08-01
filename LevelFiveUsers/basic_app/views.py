from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from basic_app.forms import UserForm, UserProfileInfoForm
# Create your views here.
from django.contrib import messages


#forlogin
from django.contrib.auth import authenticate, login , logout 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'basic_app/index.html')


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
        user_form =  UserForm()
        profile_user_form  =  UserProfileInfoForm()
    return render(request, 'basic_app/register.html', context={'user_form':user_form, 'profile_user_form': profile_user_form, 'register':register})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in..")



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
                return HttpResponse("Account is not active...")
        else:
            print("Someone try to login and failed...")
            print("Username {} and Password {} ".format(username, password) )
            errorss = "Invalid username or password"
            # return HttpResponse("Invalid login details supplied!")    
    
    return render(request, 'basic_app/login.html', context={'errors':errorss})


def aboutus(request):
    return render(request, 'basic_app/aboutus.html')