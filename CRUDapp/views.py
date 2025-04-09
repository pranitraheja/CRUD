from django.shortcuts import render,redirect
from CRUDapp.forms import *
from CRUDapp.models import *
# Create your views here.
def display(request):
    S=Student.objects.all()
    d={'Stud':S}
    return render(request,'CRUDapp/index.html',d)

def insert(request):
    f=Studentform()
    if request.method=='POST':
        f=Studentform(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'forms':f}
    return render(request,'CRUDapp/insert.html',d)

def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/')

def update(request,id):
    s=Student.objects.get(id=id)
    if request.method=="POST":
        f=Studentform(request.POST,instance=s)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'S tud':s}
    return render(request,'CRUDapp/update.html',d)