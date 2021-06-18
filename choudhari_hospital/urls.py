"""choudhari_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from patient_entry import views
from django.contrib.auth import views as a_views

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('create_patient/',views.CreatePatientView.as_view(),name='create_patient'),
    path('redirect_to_prescription/<int:pk>',views.redirect_to_prescription,name='redirect_to_prescription'),
    path('redirect_to_prescription/prescription_update/<int:pk>',views.PrescriptionUpdateView.as_view(),name='prescription_update'),
    path('redirect_to_prescriptionrecord/<int:pk>',views.redirect_to_prescriptionrecord,name='redirect_to_prescriptionrecord'),
    path('redirect_to_prescriptionrecord/medicine_record_update/<int:pk>',views.PrescriptionRecordUpdateView.as_view(),name='prescription_record_update'),
    path('prescription_record_delete/<int:pk>',views.PrescriptionRecordDeleteView.as_view(),name='prescription_record_delete'),
    path('list',views.PatientListView.as_view(),name='list'),
    path('patient/<int:pk>',views.PatientDetailView.as_view(),name='patient_detail'),
    path('find/',views.find_patient_id,name='find'),
    path('find/patient/<int:pk>',views.PatientDetailView.as_view(),name='find_patient_detail'),
    path('prescription_details/<int:pk>',views.PrescriptionDetailView.as_view(),name='prescripion_detail'),
    path('add_medicine/',views.CreateMedicineView.as_view(),name='add_medicine'),
    path('medicine_list/',views.MedicineListView.as_view(),name='medicine_list'),
    path('medicine_detail/<int:pk>',views.MedicinesDetailView.as_view(),name='medicine_detail'),
    path('medicine_update/<int:pk>',views.MedicineUpdateView.as_view(),name='medicine_update'),
    path('print_prescription/<int:pk>',views.print_prescription,name='print_prescription'),
    path('login/', a_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', a_views.LogoutView.as_view(), name='logout', kwargs={'next_page': 'index.html'}),
    path('fetched_data/',include('patient_entry.urls')),
    path('admin/', admin.site.urls),
]
