import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django 
django.setup()

## Fake script:
import random
from first_app.models import WebPage, AccessRecord, Topic
from faker import Faker


fakegen = Faker()

topic = ['Search', 'Social', 'Market', 'News', "Game"]


def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic..
        top = add_topic()

        #create fake data for that entry:
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        # new web page entry:
        webpage = WebPage.objects.get_or_create(topic = top, url=fake_url, name = fake_name)[0]

        # fake access records:
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating...')
    populate(20)
    print("Populating completed...")


