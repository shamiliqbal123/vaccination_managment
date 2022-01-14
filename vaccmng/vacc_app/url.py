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
    path("createreport", views.createreport, name="createreport"),
    path("viewreport", views.viewreport, name="viewreport"),
    path("viewcomplaint", views.viewcomplaint, name="viewcomplaint"),
    path("viewappointment", views.viewappointment, name="viewappointment"),
    path("index2", views.index2, name="index2"),
    path("nurse", views.nurse, name="nurse"),
    path("viewvaccine_nurse", nurseview.viewvaccine_nurse, name="viewvaccine_nurse"),
    path("viewuser_nurse", nurseview.viewuser_nurse, name="viewuser_nurse"),
]