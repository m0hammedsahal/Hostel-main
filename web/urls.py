from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path('logout/', views.logout, name='logout'),
    path("forgetpass/", views.forgetpass, name="forgetpass"),
    path("updatepass/", views.updatepass, name="updatepass"),
    path("faculty-access/", views.faculty_access, name="faculty_access"),
    path("parent-access/", views.parent_access, name="parent_access"),
    path("student-access/", views.student_access, name="student_access"),

]