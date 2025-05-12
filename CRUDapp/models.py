from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    emailid=models.EmailField()
    marks=models.IntegerField()
    phno=models.IntegerField()

    def get_name(self):
        return self.name