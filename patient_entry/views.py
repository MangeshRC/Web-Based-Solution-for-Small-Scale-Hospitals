from django.shortcuts import render,get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                CreateView,DetailView,
                                UpdateView,DeleteView)
from patient_entry.models import Patient,Prescription,Medicines,Prescription_Record
from patient_entry.forms import (PatientForm,FindForm,PrescriptionForm,
                                MedicineForm,PrescriptionRecordForm,
                                FindWithAddressForm,FindWithNameForm,
                                FindCollectionForDurationForm,
                                FindCollectionforDayForm)
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'

class CreatePatientView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = PatientForm
    model = Patient

class PatientListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Patient

    def get_queryset(self):
        return Patient.objects.order_by('-first_visit_date')

class PatientDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Patient

class PrescriptionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    form_class = PrescriptionForm
    model = Prescription

class PrescriptionDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Prescription


class CreateMedicineView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    form_class = MedicineForm
    model = Medicines


class PrescriptionRecordUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    form_class = PrescriptionRecordForm
    model = Prescription_Record

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Medicine1']= Prescription_Record.objects.filter(prescription_id__exact=self.object.prescription_id)
        return context

class PrescriptionRecordDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Prescription_Record

    def get_success_url(self):
        prescription = get_object_or_404(Prescription, pk=self.object.prescription_id)
        return reverse_lazy('redirect_to_prescriptionrecord',kwargs={'pk': prescription.pk})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MedicineListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Medicines

    def get_queryset(self):
        return Medicines.objects.order_by('Medicine_name')

class MedicinesDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    model = Medicines

class MedicineUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'nextpage'
    form_class = MedicineForm
    model = Medicines

@login_required
def redirect_to_prescription(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    pres = Prescription.objects.create(patient_id = pk,fees=0)
    return HttpResponseRedirect('prescription_update/'+str(pres.pk))

@login_required
def redirect_to_prescriptionrecord(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    med = Prescription_Record.objects.create(prescription_id = pk,medicine_id = 1)
    return HttpResponseRedirect('medicine_record_update/'+str(med.pk))

@login_required
def print_prescription(request, pk):
    med = get_object_or_404(Prescription_Record, pk=pk)
    pres = get_object_or_404(Prescription, pk=med.prescription_id)
    pat = get_object_or_404(Patient, pk=pres.patient_id)
    my_dict = { 'patient_id':pat.pk,
                'prescripion_id':pres.pk,
                'patient_name':pat.patient_name,
                'patient_address':pat.patient_address,
                'patient_age':pat.patient_age,
                'patient_weight':pat.patient_weight,
                'blood_pressure':pres.blood_pressure,
                'medics': Prescription_Record.objects.filter(prescription_id__exact=pres.pk),
                'pres':pres}
    return render(request,'patient_entry/print_prescription.html',context=my_dict)

@login_required
def find_patient_id(request):
    if request.method == 'POST':
        form = FindForm(request.POST)

        if form.is_valid():
            # obj = Prescription.objects.create(patient_id=form.cleaned_data['patient'])
            return HttpResponseRedirect('patient/'+form.cleaned_data['patient'])


    else:
        form = FindForm()

    return render(request,'patient_entry/find_patient.html',{'form':form})

@login_required
def search_by_address(request):
    if request.method == 'POST':
        form = FindWithAddressForm(request.POST)

        if form.is_valid():
            address = form.cleaned_data['address']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            obj = Prescription.objects.select_related('patient').filter(visit_date__lte = to_date.strftime("%Y-%m-%d"),
                                         visit_date__gte = from_date.strftime("%Y-%m-%d"), patient__patient_address__iexact=address)
            my_dict = { 'address':address,
                        'from_date':from_date,
                        'to_date':to_date,
                        'obj':obj,
                        'form':form
                        }
            return render(request,'data_processed_templates/search_by_address.html',context=my_dict)
    else:
        form = FindWithAddressForm()
    my_dict = { 'address':'',
                'from_date':'',
                'to_date':'',
                'obj':'',
                'form':form
                }
    return render(request,'data_processed_templates/search_by_address.html',context=my_dict)

class Options(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'data_processed_templates/options.html'

@login_required
def search_by_name(request):
    if request.method == 'POST':
        form = FindWithNameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            obj = Prescription.objects.select_related('patient').filter(visit_date__lte = to_date.strftime("%Y-%m-%d"),
                                         visit_date__gte = from_date.strftime("%Y-%m-%d"), patient__patient_name__iexact=name)
            my_dict = { 'name':name,
                        'from_date':from_date,
                        'to_date':to_date,
                        'obj':obj,
                        'form':form
                        }
            return render(request,'data_processed_templates/search_by_name.html',context=my_dict)
    else:
        form = FindWithNameForm()
    my_dict = { 'name':'',
                'from_date':'',
                'to_date':'',
                'obj':'',
                'form':form
                }
    return render(request,'data_processed_templates/search_by_name.html',context=my_dict)


@login_required
def see_collection_for_duration(request):
    if request.method == 'POST':
        form = FindCollectionForDurationForm(request.POST)

        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            obj = Prescription.objects.select_related('patient').filter(visit_date__lte = to_date.strftime("%Y-%m-%d"),
                                         visit_date__gte = from_date.strftime("%Y-%m-%d"),fees__isnull=False)

            patient_count = obj.count()
            total_collection = 0

            for temp in obj:
                    total_collection = total_collection + temp.fees


            my_dict = { 'from_date':from_date,
                        'to_date':to_date,
                        'obj':obj,
                        'total_collection':total_collection,
                        'form':form
                        }
            return render(request,'data_processed_templates/collection_for_duration.html',context=my_dict)
    else:
        form = FindCollectionForDurationForm()
    my_dict = { 'from_date':'',
                'to_date':'',
                'obj':'',
                'total_collection':'',
                'form':form
                }
    return render(request,'data_processed_templates/collection_for_duration.html',context=my_dict)

@login_required
def collection_for_day(request):
    if request.method == 'POST':
        form = FindCollectionforDayForm(request.POST)

        if form.is_valid():
            select_date = form.cleaned_data['select_date']
            obj = Prescription.objects.select_related('patient').filter(
                visit_date__year = select_date.strftime("%Y"),
                visit_date__day= select_date.strftime("%d"),
                visit_date__month= select_date.strftime("%m"),fees__isnull=False)

            patient_count = obj.count()
            total_collection = 0

            for temp in obj:
                    total_collection = total_collection + temp.fees


            my_dict = { 'patient_count':patient_count,
                        'obj':obj,
                        'total_collection':total_collection,
                        'form':form
                        }
            return render(request,'data_processed_templates/collection_for_day.html',context=my_dict)
    else:
        form = FindCollectionforDayForm()
    my_dict = { 'obj':'',
                'total_collection':'',
                'form':form
                }
    return render(request,'data_processed_templates/collection_for_day.html',context=my_dict)
