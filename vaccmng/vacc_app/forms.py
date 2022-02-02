from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class formhospital(forms.ModelForm):
    class Meta:
        model = Hospital_TBL
        fields = '__all__'


# class fromnurse(forms.ModelForm):
#     class Meta:
#         model = Nurse_TBL
#         fields = '__all__'

# class fromuser(forms.ModelForm):
#     class Meta:
#         model = User_TBL
#         fields = '__all__'

class fromvaccine(forms.ModelForm):
    class Meta:
        model = Vaccine_TBL
        fields = '__all__'


class fromcomplaint(forms.ModelForm):
    class Meta:
        model = Complaint_TBL
        fields = '__all__'


class formreport(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User_TBL.objects.all())
    vaccine = forms.ModelChoiceField(queryset=Vaccine_TBL.objects.all())

    class Meta:
        model = ReportCard_TBL
        fields = ('patient', 'vaccine')


class formschedule(forms.ModelForm):
    class Meta:
        model = VaccinationSchedule_TBL
        fields = '__all__'


class formregistercomplaint(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User_TBL.objects.all())

    class Meta:
        model = Complaint_TBL
        fields = '__all__'


class loginregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class nurseregister(forms.ModelForm):
    hospital = forms.ModelChoiceField(queryset=Hospital_TBL.objects.all())

    class Meta:
        model = Nurse_TBL
        fields = ('name', 'contactno', 'address', 'email', 'hospital')


class usersregister(forms.ModelForm):
    class Meta:
        model = User_TBL
        fields = ('name', 'contact_no', 'child_name', 'child_age', 'child_gender', 'recent_vaccinations')
