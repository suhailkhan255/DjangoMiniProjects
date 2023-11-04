from django.db import models

# Create your models here.


class Patient(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAME = [('HW', 'Height/Weight'), ('BP', 'blood Pressure'), ('HR', 'heart rate')]
    componentName = models.CharField(choices=COMPONENT_NAME, max_length=20)
    componentValue = models.CharField(max_length=20)
    measureDateTime = models.DateTimeField(auto_now_add=True)
    Patient = models.ForeignKey(Patient, on_delete= models.CASCADE)

