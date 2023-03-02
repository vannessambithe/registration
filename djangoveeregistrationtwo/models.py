from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=True, null=False)
    phone = models.IntegerField()
    city = models.CharField()
    country = models.CharField()

def __str__(self):
    return self.name


