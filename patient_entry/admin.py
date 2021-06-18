from django.contrib import admin
from patient_entry.models import Patient,Prescription,Medicines
# Register your models here.

admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Medicines)
