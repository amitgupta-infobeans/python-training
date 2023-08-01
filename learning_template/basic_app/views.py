from django.shortcuts import render

# Create your views here.


def index(request):
    contentt = {'user_name':"amit gupta", 'random_number':'200'}
    return render(request, "basic_app/index.html", context=contentt)

def other(request):
    return render(request, "basic_app/other.html")

def relative(request):
    return render(request, "basic_app/relative_url_template.html")    

