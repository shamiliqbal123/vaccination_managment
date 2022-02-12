from django.contrib import messages
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

def createcomplaint(request):
    form = formregistercomplaint()
    if request.method == "POST":
        form = formregistercomplaint(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewcomplaint_nurse")

    return render(request,'createcomplaint.html',{'form':form})

def viewcomplaint_nurse(request):
    data = Complaint_TBL.objects.all()
    print(data)
    return render(request,'viewcompalint_nurse.html',{'data':data})

def nurse_register(request):
    user_form = loginregister()
    nurse_form = nurseregister()
    if request.method == 'POST':

        user_form = loginregister(request.POST)
        nurse_form = nurseregister(request.POST)
        if user_form.is_valid() and nurse_form.is_valid():
           user = user_form.save(commit=False)
           user.is_nurse = True
           user.save()
           nurse = nurse_form.save(commit=False)
           nurse.user = user
           nurse.save()
           messages.info(request, 'Nurse Registered Successfully')
           return redirect('loginview')
    return render(request,'nurseregister.html',{'user_form': user_form,'nurse_form':nurse_form})

#DELETE

def deletehospital_nurse(request,id=None):
    data = Hospital_TBL.objects.get(id=id)
    data.delete()
    return redirect('viewhospital_nurse')

def deleteuser_nurse(request,id=None):
    data = User_TBL.objects.get(id=id)
    data.delete()
    return redirect('viewuser_nurse')

def deletevaccine_nurse(request,id=None):
    data = Vaccine_TBL.objects.get(id=id)
    data.delete()
    return redirect('viewvaccine_nurse')

