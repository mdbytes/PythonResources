import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

## fake pop script

import random
from app.models import User
from faker import Faker

fakegen = Faker()

def add_user(N=25):
    for n in range(N):
        fake_first_name = fakegen

        #create fake data
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        #create new webpage entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, user_email=fake_email)[0]



if __name__ == '__main__':
    print('populating users')
    add_user()
    print("populating complete")
