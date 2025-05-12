from django.shortcuts import render,redirect
#importing main from models and forms
from CRUDapp.models import Student
from CRUDapp.forms import StudentForm
from CRUDapp.serializers import StudentSerializer
#importing API
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
def display(request):
    S=Student.objects.all()
    d={'Stud':S}
    return render(request,'myapp/index.html',d)

def insert(request):
    f=StudentForm()
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'form':f}
    return render(request,'myapp/insert.html',d)

def delete(request,id):
    S=Student.objects.get(id=id)
    S.delete()
    return redirect('/')

def update(request,id):
    S=Student.objects.get(id=id)
    f=StudentForm(instance=S)
    if request.method=='POST':
        f=StudentForm(request.POST,instance=S)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'form':f,'Stud':S}
    return render(request,'myapp/update.html',d)

#creating the API's
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)