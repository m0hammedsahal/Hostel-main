from users.models import User
from django.db import models

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_student'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['-id']
    
    def __str__(self):
        return self.user.email
    


class FoodSelection(models.Model):
    user = models.ManyToManyField(User)
    MEAL_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('evening_snacks', 'Evening Snacks'),
        ('dinner', 'Dinner'),
    )

    day = models.ForeignKey('faculty.Day', on_delete=models.CASCADE)
    meal = models.CharField(max_length=15, choices=MEAL_CHOICES, null=True, blank=True)
    selected = models.BooleanField(default=False)


    class Meta:
        db_table = 'student_food_selection'
        verbose_name = 'food_selection'
        verbose_name_plural = 'food_selections'
        ordering = ['id']

    def __str__(self):
        return f"{self.day} - {self.meal}"




class Complaint(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'student_conmplaint'
        verbose_name = 'conmplaint'
        verbose_name_plural = 'conmplaints'
        ordering = ['-id']

    def __str__(self):
        return f"{self.message}"
    

class Slot(models.Model):
    booked_student = models.ForeignKey('student.Student', on_delete=models.CASCADE, null=True, blank=True)
    slot_number = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'student_slote'
        verbose_name = 'slote'
        verbose_name_plural = 'slotes'
        ordering = ['id']

    def __str__(self):
        return f"{self.slot_number} - {self.start_time} - {self.end_time}"
