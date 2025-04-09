from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    marks=models.FloatField()
    addr=models.CharField(max_length=30)
    phno=models.IntegerField()

    def __str__(self):
        return self.name