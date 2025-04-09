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
        frollno=f.random_int(min=1,max=100)
        fmarks=f.random_int(min=35,max=100)
        faddr=f.address()
        fphoneno=f.random_int(min=1000000000000,max=9000000000000)
    e=Student.objects.get_or_create(name=fname,rollno=frollno,marks=fmarks,addr=faddr,phno=fphoneno)
populate(20)