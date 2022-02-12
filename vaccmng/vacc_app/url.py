from django.urls import path, include
from vacc_app import views
from vacc_app import nurseview
from vacc_app import userview

urlpatterns = [
    path("admin_home",views.index,name="admin_home"),
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
    path("nurse_home", views.nurse, name="nurse_home"),

    path("viewvaccine_nurse", nurseview.viewvaccine_nurse, name="viewvaccine_nurse"),
    path("viewuser_nurse", nurseview.viewuser_nurse, name="viewuser_nurse"),
    path("viewhospital_nurse", nurseview.viewhospital_nurse, name="viewhospital_nurse"),
    path("createschedule", nurseview.createschedule, name="createschedule"),
    path("viewschedule", nurseview.viewschedule, name="viewschedule"),
    path("viewappointment_nurse", nurseview.viewappointment_nurse, name="viewappointment_nurse"),
    path("createcomplaint", nurseview.createcomplaint, name="createcomplaint"),
    path("report1", views.createreport, name="report1"),
    path("viewcomplaint_nurse", nurseview.viewcomplaint_nurse, name="viewcomplaint_nurse"),

    path("appointmentstatus", views.appointmentstatus, name="appointmentstatus"),
    path("user_home", views.user, name="user_home"),

    path("viewuser_user", userview.viewuser_user, name="viewuser_user"),
    path("viewuser_user", userview.viewuser_user, name="viewuser_user"),
    path("viewschedule_user", userview.viewschedule_user, name="viewschedule_user"),
    path("viewappointment_user", userview.viewappointment_user, name="viewappointment_user"),
    path("registercomplaint_user", userview.registercomplaint_user, name="registercomplaint_user"),
    path("viewreport_user", userview.viewreport_user, name="viewreport_user"),

    path("", views.home, name="home"),
    path("loginview", views.login_view, name="loginview"),

    path("nurseregister", nurseview.nurse_register, name="nurseregister"),

    path("userregister", userview.users_register, name="userregister"),

#DELETE ADMIN
    path('deletehospital/<int:id>/', views.deletehospital, name='deletehospital'),
    path('deletenurse/<int:id>/', views.deletenurse, name='deletenurse'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),
    path('deletevaccine/<int:id>/', views.deletevaccine, name='deletevaccine'),
    path('deletereport/<int:id>/', views.deletereport, name='deletereport'),

#DELETE NURSE

    path('deletehospital_nurse/<int:id>/', nurseview.deletehospital_nurse, name='deletehospital_nurse'),
    path('deleteuser_nurse/<int:id>/', nurseview.deleteuser_nurse, name='deleteuser_nurse'),
    path('deletevaccine_nurse/<int:id>/', nurseview.deletevaccine_nurse, name='deletevaccine_nurse'),



]