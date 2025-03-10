from django import forms
from .models import *
from users.models import Profile

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




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'phone_number', 'hostel_id', 'register_no', 'guardian_name', 'guardian_number', 'department', 'address')



