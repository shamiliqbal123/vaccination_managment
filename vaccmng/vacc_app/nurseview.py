from django.shortcuts import render, redirect
from .models import *
from .forms import *

def viewvaccine_nurse(request):
    data = Vaccine_TBL.objects.all()
    print(data)
    return render(request,'viewvaccine_nurse.html',{'data':data})

def viewuser_nurse(request):
    data = User_TBL.objects.all()
    print(data)
    return render(request,'viewuser_nurse.html',{'data':data})

def viewhospital_nurse(request):
    data = Hospital_TBL.objects.all()
    print(data)
    return render(request,'viewhospital_nurse.html',{'data':data})

def createschedule(request):
    if request.method == "POST":
        form = formschedule(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewschedule")
    else:
        form = formschedule()
        return render(request,'createschedule.html',{'form':form})

def viewschedule(request):
    data = VaccinationSchedule_TBL.objects.all()
    print(data)
    return render(request,'viewschedule.html',{'data':data})

def viewappointment_nurse(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request,'viewappointment_nurse.html',{'data':data})

def registercomplaint(request):
    data = User_TBL.objects.all()
    if request.method == "POST":
        form = formreport(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewcomplaint")
    else:
        form = formregistercomplaint()
    return render(request,'registercomplaint.html',{'form':form,'data':data})

def viewcomplaint_nurse(request):
    data = Complaint_TBL.objects.all()
    print(data)
    return render(request,'viewcompalint_nurse.html',{'data':data})