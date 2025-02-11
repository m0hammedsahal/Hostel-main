from django import forms
from .models import *

class CheckInCheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckInCheckOut
        fields = ('check_in', 'check_out')



class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('message',)




class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('attendance_date', 'attendance_status')

