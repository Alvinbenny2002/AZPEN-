from django.db import models
from doctor.models import*
# Create your models here.
class Patient(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    repass=models.TextField(max_length=100,null=True)
class Appointment(models.Model):
    name=models.TextField(max_length=50,null=True)
    date=models.DateField(max_length=50,null=True)
    time=models.TimeField(max_length=50,null=True)
    message=models.TextField(max_length=500,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    status=models.TextField(max_length=20)