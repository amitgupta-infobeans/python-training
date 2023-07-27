from django.shortcuts import render
from second_app.models import Users
# Create your views here.


def index(request):
    return render(request, 'second_app/index.html')


def second_app_users(request):
    getallusers = Users.objects.order_by('first_name')
    all_users = {'users':getallusers}
    return render(request, 'second_app/users.html', context=all_users)

