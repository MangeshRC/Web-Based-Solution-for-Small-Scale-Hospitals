from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=128,blank=False)
    patient_age = models.IntegerField(blank=False)
    first_visit_date = models.DateTimeField(default=timezone.now)
    patient_address = models.CharField(max_length=256)
    patient_weight = models.IntegerField()


    def get_absolute_url(self):
        return reverse('patient_detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.patient_name


class Prescription(models.Model):
    patient = models.ForeignKey('patient_entry.Patient',related_name='prescriptions',on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)
    other_comments = models.CharField(max_length=256,blank=True,default='None')
    blood_pressure = models.CharField(max_length=64,blank=True)
    RS = models.CharField(max_length=128,blank=True,default='NAD')
    CVS = models.CharField(max_length=128,blank=True,default='NAD')
    ut = models.CharField(max_length=64,blank=True)
    vx = models.CharField(max_length=64,blank=True)
    FHS = models.CharField(max_length=64,blank=True)
    PIV = models.CharField(max_length=64,blank=True)
    H_O = models.TextField(max_length=256,blank=True)
    C_O = models.TextField(max_length=256,blank=True)
    gravida = models.CharField(max_length=2,blank=True)
    para = models.CharField(max_length=2,blank=True)
    abortions = models.CharField(max_length=2,blank=True)
    fees = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('redirect_to_prescriptionrecord', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.patient)


class Medicines(models.Model):
    Medicine_name = models.CharField(max_length=128)
    T_or_S = (('Cap','Capsule'),
             ('Syr','Syrup'),
             ('Tab','Tablet'),
             ('Susp','Susp'),
             ('Oint','Ointment'),
             ('Drop','Drop'),
             ('Pow','Powder'),
             ('Inj','Injection'),
             ('O','Other'))
    Tablet_or_Syrup = models.CharField(max_length=5,choices=T_or_S)
    Ingredient_Drugs = models.CharField(max_length=128,blank=True)

    def get_absolute_url(self):
        return reverse('medicine_list')

    def __str__(self):
        return self.Medicine_name

class Prescription_Record(models.Model):
    dose_choice = (('1','Once a day'),
               ('2','2 times/day'),
               ('3','3 times/day'),
               ('0','Other'))
    medicine = models.ForeignKey('patient_entry.Medicines',related_name='medicines_prescription_record',on_delete=models.CASCADE,blank=True)
    prescription = models.ForeignKey('patient_entry.Prescription',related_name='prescription_prescription_record',on_delete=models.CASCADE)
    prescribed_date = models.DateTimeField(default=timezone.now)
    quantity = models.CharField(max_length=100,blank=True)
    dose = models.CharField(max_length=1,blank=True,choices=dose_choice)

    def get_absolute_url(self):
        return reverse('redirect_to_prescriptionrecord', kwargs={'pk':self.prescription_id})
