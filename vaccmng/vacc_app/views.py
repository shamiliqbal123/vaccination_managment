from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'dashboard.html')


def createhospital(request):
    if request.method == "POST":
        form = formhospital(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewhospital")
    else:
        form = formhospital()
        return render(request, 'createhospital.html', {'form': form})


def viewhospital(request):
    data = Hospital_TBL.objects.all()
    print(data)
    return render(request, 'viewhospital.html', {'data': data})


def viewnurse(request):
    data = Nurse_TBL.objects.all()
    print(data)
    return render(request, 'viewnurse.html', {'data': data})


def viewuser(request):
    data = User_TBL.objects.all()
    print(data)
    return render(request, 'viewuser.html', {'data': data})


def createvaccine(request):
    if request.method == "POST":
        form = fromvaccine(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewvaccine")
    else:
        form = fromvaccine()
        return render(request, 'createvaccine.html', {'form': form})


def viewvaccine(request):
    data = Vaccine_TBL.objects.all()
    print(data)
    return render(request, 'viewvaccine.html', {'data': data})


def createcomplaint(request):
    if request.method == "POST":
        form = fromcomplaint(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewcomplaint")
    else:
        form = fromcomplaint()
        return render(request, 'createcomplaint.html', {'form': form})


def createreport(request):
    data = User_TBL.objects.all()
    data1 = Vaccine_TBL.objects.all()
    if request.method == "POST":
        form = formreport(request.POST)
        if form.is_valid():
            print("hi...")
            form.save()
            return redirect("viewreport")
    else:
        form = formreport()
    return render(request, 'report1.html', {'form': form, 'data': data, 'data1': data1})


# def createreport(request):
#     form = formreport()
#     if request.method=='POST':
#         form=formreport(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('viewreport')
#     return render(request,'report2.html',{'form':form})

def viewreport(request):
    data = ReportCard_TBL.objects.all()
    print(data)
    return render(request, 'viewreport.html', {'data': data})


def viewcomplaint(request):
    data = Complaint_TBL.objects.all()
    print(data)
    return render(request, 'viewcomplaint.html', {'data': data})


def viewappointment(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request, 'viewappointment.html', {'data': data})


def appointmentstatus(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request, 'appointmentstatus.html', {'data': data})


# NURSE.

def nurse(request):
    return render(request, 'nurse.html')


# user
def user(request):
    return render(request, 'user.html')


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admin_home")
            elif user.is_nurse:
                return redirect("nurse_home")
            elif user.is_user:
                return redirect("user_home")
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')

# def nurseregister(request):
#     return render(request,'nurseregister.html')


# Create your views here.
