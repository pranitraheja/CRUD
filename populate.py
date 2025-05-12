import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRUD.settings")
django.setup()
from faker import Faker
from CRUDapp.models import Student
f=Faker()
def populate(n):
    for i in range(n):
        fname=f.name()
        fage=f.random_int(min=18,max=30)
        femail=f.email()
        fmarks=f.random_int(min=0,max=80)
        fphno=f.random_int(min=1000000000,max=9000000000)
    e=Student.objects.get_or_create(name=fname,age=fage,emailid=femail,marks=fmarks,phno=fphno)
populate(20)