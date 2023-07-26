from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<em>My Second App </em>")


def helppage(request):
    cdc = {'help_content':"You are taking Help.."}
    return render(request, "AppTwo/help.html", context = cdc)


   
