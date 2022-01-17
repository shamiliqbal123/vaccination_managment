from django import forms
from .models import *

class formhospital(forms.ModelForm):
    class Meta:
        model = Hospital_TBL
        fields = '__all__'

class fromnurse(forms.ModelForm):
    class Meta:
        model = Nurse_TBL
        fields = '__all__'

class fromuser(forms.ModelForm):
    class Meta:
        model = User_TBL
        fields = '__all__'

class fromvaccine(forms.ModelForm):
    class Meta:
        model = Vaccine_TBL
        fields = '__all__'

class fromcomplaint(forms.ModelForm):
    class Meta:
        model = Complaint_TBL
        fields = '__all__'

class formreport(forms.ModelForm):
    class Meta:
        model = ReportCard_TBL
        fields = ('patient','vaccine')

class formschedule(forms.ModelForm):
    class Meta:
        model = VaccinationSchedule_TBL
        fields = '__all__'

class formregistercomplaint(forms.ModelForm):
    class Meta:
        model = Complaint_TBL
        fields = '__all__'