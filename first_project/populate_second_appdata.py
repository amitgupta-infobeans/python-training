import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random

from faker import Faker
from second_app.models import Users

fakerOb = Faker()

def populates(N=5):

    for eachuser in range(N):

        fake_name = fakerOb.name().split()
        fake_first_name= fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakerOb.email()
        # fake users seed one by one till N length..
        userss = Users.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]
    

if __name__ == '__main__':
    print("Populating users...")
    populates(20)
    print("Completed....")


