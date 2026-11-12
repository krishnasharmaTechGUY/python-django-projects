from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

def __str__(self):  # this function is wrtiten here to give meaningful output
    return self.name