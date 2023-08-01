from django.shortcuts import render,redirect
# from django.http import HttpResponse
from AppTwo.form import NewUser
from AppTwo.models import UserModel
# Create your views here.


def index(request):

    newUsers = UserModel.objects.order_by('-id' )
    return render(request, "AppTwo/index.html", context={'newUsers':newUsers})


def helppage(request):
    cdc = {'help_content':"You are taking Help.."}
    return render(request, "AppTwo/help.html", context = cdc)


def userform(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print("Error Form Invalid..")
    
    return render(request, 'AppTwo/userform.html', {'form':form} )
   
