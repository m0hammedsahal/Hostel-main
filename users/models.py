from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, 
        max_length=256, 
        error_messages={'unique': 'Email already exists'}
    )
    register_id = models.CharField(
        unique=True, 
        max_length=50, 
        error_messages={'unique': 'Register ID already exists'}
    )

    hostel_id = models.CharField(max_length=255, null=True, blank=True)
    student_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_email = models.EmailField(max_length=255, null=True, blank=True)

    second_pass = models.CharField(max_length=255)
    is_customer = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_parents = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['register_id']

    objects = UserManager()

    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-id']

    def __str__(self):
        return f"{self.register_id} - {self.email}"





class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.ImageField(max_length=255, null=True, blank=True)
    hostel_id = models.ImageField(max_length=255, null=True, blank=True)
    hostel_id = models.ImageField(max_length=255, null=True, blank=True)
    register_no = models.CharField(max_length=255, null=True, blank=True)
    guardian_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_number = models.ImageField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'users_profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}"







# from django.db import models
# from django.contrib.auth.models import AbstractUser

# from users.manager import UserManager


# class User(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True, max_length=256, error_messages={'unique': 'Email already exists'})

#     register_id = models.CharField(
#         unique=True, 
#         max_length=50, 
#         error_messages={'unique': 'Register ID already exists'}
#     )

#     is_customer = models.BooleanField(default=False)
#     is_faculty = models.BooleanField(default=False)
#     is_parents = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     is_manager = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


#     objects = UserManager()

#     class Meta:
#         db_table = 'users_user'
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         ordering = ['-id']
    
#     def __str__(self):
#         return f"{self.register_id} - {self.email}"
    
    