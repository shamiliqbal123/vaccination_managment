from django.contrib import admin
from .models import *
admin.site.register(Login)
admin.site.register(Hospital_TBL)
admin.site.register(Nurse_TBL)
admin.site.register(User_TBL)
admin.site.register(Vaccine_TBL)
admin.site.register(VaccinationSchedule_TBL)
admin.site.register(Complaint_TBL)
admin.site.register(Appointment_TBL)
admin.site.register(ReportCard_TBL)

# Register your models here.
