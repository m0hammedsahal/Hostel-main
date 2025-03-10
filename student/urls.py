from django.urls import path
from . import views
from parents.views import pattendance
from parents.views import pcheck
from parents.views import pfee
from parents.views import pnotification

app_name = "student"

urlpatterns = [
    path("", views.sdashbord, name="sdashbord"),
    path("login/", views.login, name="login"),
    path('food/', views.sfood, name='sfood'),
    path('food_selection_submit/', views.food_selection_submit, name='food_selection_submit'),
    path("attendance/", pattendance, name="sattendance"),
    path("check/", pcheck, name="scheck"),
    path("alert/", views.salert, name="salert"),
    path("notification/", pnotification, name="snotification"),
    path("complaint/", views.scomplaint, name="scomplaint"),
    path('post_complaint/', views.post_complaint, name='post_complaint'),
    path("fee/", pfee, name="sfee"),
    path("slot/", views.sslot, name="sslot"),
    path("book-slot/<pk>/", views.book_slot, name="book_slot"),
    path("profile/", views.sprofile, name="sprofile"),
    
]