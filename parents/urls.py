from django.urls import path
from . import views

app_name = "parents"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.pdashbord, name="pdashbord"),
    path("login/", views.login, name="login"),
    path("check/", views.pcheck, name="pcheck"),
    path("fee/", views.pfee, name="pfee"),
    path("notification/", views.pnotification, name="pnotification"),
    path("attendance/", views.pattendance, name="pattendance"),


    path("changepass/", views.pchangepass, name="pchangepass"),
    path("forgetpass/", views.pforgetpass, name="pforgetpass"),
    path("upupdatepass/", views.pupupdatepass, name="pupupdatepass"),

]