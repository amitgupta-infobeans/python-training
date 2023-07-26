from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def testpage(request):
    return HttpResponse("<h1>Hi this is test page..</h1>")

def aboutus(request):
    return HttpResponse("<h1>About Us Page..</h1>")












