from django.db import models

class Login_TBL(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class Hospital_TBL(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    e_mail = models.CharField(max_length=20)

class Nurse_TBL (models.Model):
    name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=20)
    login_id = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital_TBL, on_delete=models.CASCADE)

class User_TBL (models.Model):
    name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    child_name = models.CharField(max_length=20)
    login_id = models.ForeignKey(Login_TBL, on_delete=models.CASCADE)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=20)
    recent_vaccinations = models.CharField(max_length=20)

class Vaccine_TBL(models.Model):
    vaccine_name = models.CharField(max_length=20)
    vaccine_type = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    approval_status = models.IntegerField()


class VaccinationSchedule_TBL(models.Model):
    hospital = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Complaint_TBL(models.Model):
    user = models.ForeignKey(User_TBL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    complaint = models.CharField(max_length=20)
    date = models.DateTimeField()
    reply = models.CharField(max_length=20,blank=True)

class Appointment_TBL(models.Model):
    user = models.ForeignKey(Vaccine_TBL, on_delete=models.CASCADE)
    schedule = models.TimeField()
    status = models.IntegerField()
    vaccine_name = models.ForeignKey(User_TBL, on_delete=models.CASCADE)
    vaccinated = models.CharField(max_length=20)

class ReportCard_TBL(models.Model):
    patient = models.ForeignKey(User_TBL, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine_TBL, on_delete=models.CASCADE)


# Create your models here.
