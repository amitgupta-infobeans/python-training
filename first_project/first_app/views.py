from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, WebPage, Topic
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_record":webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)


def aboutus(request):
    return HttpResponse("<h1>About Us Page..</h1>")


def helppage(request):
    return render(request, 'first_app/help.html')
    

def testpage(request):
    return render(request, 'home.html')










