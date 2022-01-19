from django.urls import path, include
from vacc_app import views
from vacc_app import nurseview

urlpatterns = [
    path("",views.index,name="dashboard"),
    path("createhospital",views.createhospital,name="createhospital"),
    path("viewhospital",views.viewhospital,name="viewhospital"),
    path("viewnurse", views.viewnurse, name="viewnurse"),
    path("viewuser", views.viewuser, name="viewuser"),
    path("createvaccine", views.createvaccine, name="createvaccine"),
    path("viewvaccine", views.viewvaccine, name="viewvaccine"),
    # path("createreport", views.createreport, name="createreport"),
    path("viewreport", views.viewreport, name="viewreport"),
    path("viewcomplaint", views.viewcomplaint, name="viewcomplaint"),
    path("viewappointment", views.viewappointment, name="viewappointment"),
    path("index2", views.index2, name="index2"),
    path("nurse", views.nurse, name="nurse"),
    path("viewvaccine_nurse", nurseview.viewvaccine_nurse, name="viewvaccine_nurse"),
    path("viewuser_nurse", nurseview.viewuser_nurse, name="viewuser_nurse"),
    path("viewhospital_nurse", nurseview.viewhospital_nurse, name="viewhospital_nurse"),
    path("createschedule", nurseview.createschedule, name="createschedule"),
    path("viewschedule", nurseview.viewschedule, name="viewschedule"),
    path("viewappointment_nurse", nurseview.viewappointment_nurse, name="viewappointment_nurse"),
    path("registercomplaint", nurseview.registercomplaint, name="registercomplaint"),
    path("report1", views.createreport, name="report1"),
    path("viewcomplaint_nurse", nurseview.viewcomplaint_nurse, name="viewcomplaint_nurse"),
    path("appointmentstatus", views.appointmentstatus, name="appointmentstatus"),
    path("user", views.user, name="user"),
]