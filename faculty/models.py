from users.models import User
from django.db import models


class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_faculty'
        verbose_name = 'faculty'
        verbose_name_plural = 'facultys'
        ordering = ['-id']
    
    def __str__(self):
        return self.user.student_name
    

class Fee(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    fee_date = models.DateField(null=True, blank=True)
    last_date = models.DateField(null=True, blank=True)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], default='unpaid')

    class Meta:
        db_table = 'faculty_fee'
        verbose_name = 'fee'
        verbose_name_plural = 'fees'
        ordering = ['id']

    def __str__(self):
        return f"{self.student.user.last_name} - {self.fee_date}"



class Attendance(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    attendance_date = models.DateField()
    attendance_status = models.CharField(max_length=10, choices=[
        ('present', 'Present'),
        ('absent', 'Absent')
    ])

    def __str__(self):
        return f"{self.student.user.last_name} - {self.attendance_date}- {self.attendance_status}"



class CheckInCheckOut(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='check_in_check_out_records')
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'faculty_checkinout'
        verbose_name = 'checkinout'
        verbose_name_plural = 'checkinouts'
        ordering = ['id']

    def __str__(self):
        return f"{self.student.user.last_name} - {self.check_in} - {self.check_out}"



class Alert(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message


class Day(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    breakfast = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    eveningsnaks = models.CharField(max_length=255)
    dinner = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.day.name}"



class Notification(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'faculty_notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-id']

    def __str__(self):
        return f"{self.message}"