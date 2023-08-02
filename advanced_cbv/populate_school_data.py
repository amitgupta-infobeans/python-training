import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_cbv.settings')
import django 
django.setup()

## Fake script:
from cbv_app.models import School
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        #create fake data for that entry:
        fake_principal = fakegen.name()
        fake_location = fakegen.city()
        fake_name = fakegen.name().split()
        fake_first_name= fake_name[0]
        fake_last_name = fake_name[1]


        # new School entry:
        webpage = School.objects.get_or_create(name= fake_first_name+' '+fake_last_name, principal = fake_principal, location=fake_location)[0]


if __name__ == '__main__':
    print('Populating...')
    populate(2)
    print("Populating completed...")


