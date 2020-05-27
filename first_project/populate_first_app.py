import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django

django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen=Faker()

topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return(t)
