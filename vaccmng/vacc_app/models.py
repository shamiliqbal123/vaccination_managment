from django.contrib.auth.models import AbstractUser
from django.db import models


class Hospital_TBL(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    e_mail = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Nurse_TBL(models.Model):
    name = models.CharField(max_length=20)
    contactno = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital_TBL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User_TBL(models.Model):
    name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    child_name = models.CharField(max_length=20)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=20)
    recent_vaccinations = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Vaccine_TBL(models.Model):
    vaccine_name = models.CharField(max_length=20)
    vaccine_type = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    approval_status = models.IntegerField()

    def __str__(self):
        return self.vaccine_name


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
    reply = models.CharField(max_length=20, blank=True)


class Appointment_TBL(models.Model):
    user = models.ForeignKey(Vaccine_TBL, on_delete=models.CASCADE)
    schedule = models.TimeField()
    status = models.IntegerField()
    vaccine_name = models.ForeignKey(User_TBL, on_delete=models.CASCADE)
    vaccinated = models.CharField(max_length=20)


class ReportCard_TBL(models.Model):
    patient = models.ForeignKey(User_TBL, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine_TBL, on_delete=models.CASCADE)


class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

# Create your models here.
