from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def viewuser_user(request):
    data = User_TBL.objects.all()
    print(data)
    return render(request,'viewuser_user.html',{'data':data})

def viewschedule_user(request):
    data = VaccinationSchedule_TBL.objects.all()
    print(data)
    return render(request,'viewschedule_user.html',{'data':data})

def viewappointment_user(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request,'viewappointment_user.html',{'data':data})

def registercomplaint_user(request):
    data = User_TBL.objects.all()
    if request.method == "POST":
        form = formregistercomplaint(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewcomplaint_user")
    else:
        form = formregistercomplaint()
    return render(request,'registercomplaint_user.html',{'form':form,'data':data})

def viewcomplaint_user(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request,'viewappointment_user.html',{'data':data})

def viewreport_user(request):
    data = ReportCard_TBL.objects.all()
    print(data)
    return render(request,'viewreport_user.html',{'data':data})

def users_register(request):
    user_form = loginregister()
    users_form = usersregister()
    if request.method == 'POST':

        user_form = loginregister(request.POST)
        users_form = usersregister(request.POST)
        if user_form.is_valid() and users_form.is_valid():
           user = user_form.save(commit=False)
           user.is_user =True
           user.save()
           users = users_form.save(commit=False)
           users.user = user
           users.save()
           messages.info(request, 'User Registered Successfully')
           return redirect('loginview')
    return render(request,'userregister.html',{'user_form': user_form,'users_form':users_form})


