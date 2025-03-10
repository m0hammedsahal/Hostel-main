from django.urls import path
from . import views
from parents.views import pnotification

app_name = "faculty"

urlpatterns = [
    path("", views.fdashbord, name="fdashbord"),
    path("login/", views.login, name="login"),
    path("register_id/", views.register_id, name="register_id"),
    path("studentadd/", views.fstudentadd, name="fstudentadd"),
    path("alert/", views.falert, name="falert"),
    path("alert/delete/<int:id>/", views.alert_delete, name="alert_delete"),
    path("attendance/", views.attendance, name="fattendance"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path('attendance/<int:id>/update/', views.update_attendance, name='update_attendance'),
    path('update_food_selection/', views.update_food_selection, name='update_food_selection'),
    path("fee/", views.ffee, name="ffee"),
    path("change_date/", views.change_date, name="change_date"),
    path("mark_fee/<pk>/", views.mark_fee, name="mark_fee"),
    path("delete_fee/<pk>/", views.delete_fee, name="delete_fee"),
    path("check/", views.fcheck, name="fcheck"),
    path("check_in/<pk>/", views.check_in, name="check_in"),
    path("check_out/<pk>/", views.check_out, name="check_out"),
    path("cancel_check_in/<pk>/", views.cancel_check_in, name="cancel_check_in"),
    path("cancel_check_out/<pk>/", views.cancel_check_out, name="cancel_check_out"),
    path("notification/", pnotification, name="fnotification"),
    path("slot/", views.fslot, name="fslot"),
    path("complaint/", views.fcomplaint, name="fcomplaint"),
    path("food/", views.ffood, name="ffood"),
    path("profile/", views.fprofile, name="fprofile"),

]