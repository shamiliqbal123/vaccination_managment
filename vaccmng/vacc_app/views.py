from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    return render(request,'dashboard.html')

def createhospital(request):
    if request.method == "POST":
        form = formhospital(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewhospital")
    else:
        form = formhospital()
        return render(request,'createhospital.html',{'form':form})
def viewhospital(request):
    data = Hospital_TBL.objects.all()
    print(data)
    return render(request,'viewhospital.html',{'data':data})



def viewnurse(request):
    data = Nurse_TBL.objects.all()
    print(data)
    return render(request,'viewnurse.html',{'data':data})


def viewuser(request):
    data = User_TBL.objects.all()
    print(data)
    return render(request,'viewuser.html',{'data':data})
def createvaccine(request):
    if request.method == "POST":
        form = fromvaccine(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewvaccine")
    else:
        form = fromvaccine()
        return render(request,'createvaccine.html',{'form':form})

def viewvaccine(request):
    data = Vaccine_TBL.objects.all()
    print(data)
    return render(request,'viewvaccine.html',{'data':data})

def createcomplaint(request):
    if request.method == "POST":
        form = fromcomplaint(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewcomplaint")
    else:
        form = fromcomplaint()
        return render(request,'createvcomplaint.html',{'form':form})

# def createreport(request):
#     data = User_TBL.objects.all()
#     data1 = Vaccine_TBL.objects.all()
#     if request.method == "POST":
#         form = formreport(request.POST)
#         if form.is_valid():
#             print("hi...")
#             form.save()
#             return redirect("viewreport")
#     else:
#         form = formreport()
#     return render(request,'createreport.html',{'form':form,'data':data,'data1':data1})

def createreport(request):
    form = formreport()
    if request.method=='POST':
        form=formreport(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewreport')
    return render(request,'report1.html',{'form':form})

def viewreport(request):
    data = ReportCard_TBL.objects.all()
    print(data)
    return render(request,'viewreport.html',{'data':data})

def viewcomplaint(request):
    data = Complaint_TBL.objects.all()
    print(data)
    return render(request,'viewcomplaint.html',{'data':data})

def viewappointment(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request,'viewappointment.html',{'data':data})

def index2(request):
    return render(request,'index2.html')

def appointmentstatus(request):
    data = Appointment_TBL.objects.all()
    print(data)
    return render(request,'appointmentstatus.html',{'data':data})

#NURSE.

def nurse(request):
    return render(request,'nurse.html')

#user
def user(request):
    return render(request,'user.html')
# Create your views here.
