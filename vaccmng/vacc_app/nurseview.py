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
