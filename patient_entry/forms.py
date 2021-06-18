from django import forms
from patient_entry.models import Patient,Prescription,Medicines,Prescription_Record


class PatientForm(forms.ModelForm):

    class Meta():
        model = Patient
        fields = ('patient_name','patient_age','patient_address','patient_weight')




class FindForm(forms.Form):
    patient = forms.CharField()


class PrescriptionForm(forms.ModelForm):

    class Meta():
        model = Prescription
        fields = ('patient','gravida','para','abortions','C_O','H_O','blood_pressure','RS','CVS','ut','vx','FHS','PIV','other_comments','fees')



class MedicineForm(forms.ModelForm):

    class Meta():
        model = Medicines
        fields = ('Medicine_name','Tablet_or_Syrup','Ingredient_Drugs')

class PrescriptionRecordForm(forms.ModelForm):
    class Meta():
        model = Prescription_Record
        fields = ('medicine','quantity','dose')

    medicine = forms.ModelChoiceField(queryset=Medicines.objects.order_by('Medicine_name'))

class FindWithAddressForm(forms.Form):
    address = forms.CharField()
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class FindWithNameForm(forms.Form):
    name = forms.CharField()
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class FindCollectionForDurationForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class FindCollectionforDayForm(forms.Form):
    select_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
