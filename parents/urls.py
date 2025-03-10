from django.urls import path
from . import views

app_name = "parents"

urlpatterns = [
    path("", views.pdashbord, name="pdashbord"),
    path("login/", views.login, name="login"),
    path("check/", views.pcheck, name="pcheck"),
    path("fee/", views.pfee, name="pfee"),
    path("notification/", views.pnotification, name="pnotification"),
    path("attendance/", views.pattendance, name="pattendance"),

]