from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from customer.models import *

from web.models import *
from users.models import *

from django.db.models import Sum

from decimal import Decimal  # Import Decimal for precise calculations

from django.shortcuts import redirect
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
import random
import string
import hashlib
from datetime import datetime
from datetime import date

from student.models import *
from .models import *
from .forms import *


def generate_unique_order_id(length=7):
    return ''.join(random.choices(string.digits + '25', k=length))

def generate_register_id(previous_id=None):
    last_registered_user = User.objects.latest('id')
    
    if previous_id is None:
        current_id = int(last_registered_user.register_id)
    
    current_id += 1
    return current_id



# @login_required(login_url='web:login') 
def index(request):

    context = {
     
    }
    return render(request, 'index.html', context=context)

def fdashbord(request):
    

    context = {
     
    }
    return render(request, 'faculty/fdashbord.html', context=context)



def login(request):
    if request.method == 'POST':
        register_id = request.POST.get('register_id')
        password = request.POST.get('password')
        users = User.objects.all()

        for user in users:
            userregister_id = user.register_id
            userpassword = user.second_pass
            print(userregister_id, userpassword)

            if register_id in userregister_id and password in userpassword:
                user = User.objects.get(register_id=register_id)
                auth_login(request, user)
                print('valid')
                return HttpResponseRedirect(reverse('faculty:fdashbord'))
            else:
                print('invalid')
                return render(request, 'faculty/flogin.html')

        # user = authenticate(request, email=register_id, password=password)

        # if user is not None:
        #     auth_login(request, user)
        #     return HttpResponseRedirect(reverse('faculty:fprofile'))
        # else:
        #     context = {
        #         "error" : True,
        #         "message" : "Invalid email or pasword"
        #     }
        #     return render(request, 'faculty/flogin.html', context=context)
    else:
        return render(request, 'faculty/flogin.html')
    



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        register_id = request.POST.get('register_id')

        if User.objects.filter(email=email).exists():
            context = {
                "error" : True,
                "message" : "Email already registered"
            }
            return render(request, 'faculty/register.html', context=context)
        else:
            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                second_pass=password,
                register_id=generate_register_id(),
                is_faculty=True
            )

            user.save()

            auth_login(request, user)

           
            return HttpResponseRedirect(reverse('faculty:register_id'))

    else:
        return render(request, 'faculty/register.html')
    
@login_required(login_url='faculty:login') 
def register_id(request):
    user=request.user
    register_id=user.register_id

    context = {
        "register_id": register_id
    }
    return render(request, 'faculty/register_id.html', context=context)


def fstudentadd(request):
    students = Student.objects.all()
    if request.method == 'POST':
        email = request.POST.get('studentemail')
        first_name = request.POST.get('studentname')
        last_name = request.POST.get('studentname')
        studentname = request.POST.get('studentname')
        password = request.POST.get('password')
        register_id = request.POST.get('register_id')
        hostelid = request.POST.get('hostelid')
        guardianemail = request.POST.get('guardianemail')

        if User.objects.filter(email=email).exists():
            context = {
                "error" : True,
                "message" : "Email already registered"
            }
            return render(request, 'faculty/register.html', context=context)
        else:
            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                second_pass=password,
                student_name=studentname,
                register_id=register_id,
                hostel_id=hostelid,
                guardian_email=guardianemail,
                is_student=True
            )

            user.save()

            student = Student.objects.create(user=user)
            
            student.save()
            return HttpResponseRedirect(reverse('faculty:fstudentadd'))
    else:
        return render(request, 'faculty/fstudentadd.html', {"students": students})





def falert(request):
    user=request.user
    alerts= Alert.objects.all()
    if request.method == 'POST':
        message = request.POST.get('message')
        alert = Alert.objects.create(
            message=message,
            user=user,
        )
        alert.save()
        return HttpResponseRedirect(reverse('faculty:falert'))
            
    else:
        return render(request, 'faculty/falert.html', {"alerts": alerts})
    

def alert_delete(request, id):
    alert = Alert.objects.get(id=id)
    alert.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
# def falert(request):
#     if request.method == 'POST':
#         form = AlertForm(request.POST)
#         if form.is_valid():
#             alert = form.save(commit=False)
#             alert.user = request.user
#             alert.save()
#             return redirect('faculty:falert')
#     else:
#         form = AlertForm()
#     alerts = Alert.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'faculty/falert.html', {'form': form, 'alerts': alerts})




@login_required
def attendance(request):
    students = Student.objects.all()
    attendance_records = Attendance.objects.all()
    today = date.today()

    context ={
        'today': today, 
        'students': students, 
        'attendance_records': attendance_records,
    }

    return render(request, 'faculty/attendance.html', context=context)

@login_required
def mark_attendance(request):
    for student in Attendance.objects.all():
        student.delete()
    attendance_date = request.POST.get('attendance_date')
    for student in Student.objects.all():
        attendance_status = request.POST.get(f'attendance_status_{student.id}')
        Attendance.objects.create(
            student=student,
            attendance_date=attendance_date,
            attendance_status=attendance_status
        )
    return redirect('faculty:fattendance')


@login_required
def update_attendance(request, id):
    attendance_record = Attendance.objects.get(id=id)
    attendance_status = request.POST.get('attendance_status')

    attendance_record.attendance_status = attendance_status
    attendance_record.save()

    return redirect('attendance')



def ffood(request):
    days = Day.objects.all()
    meals = Menu.objects.all()
    i = Day.objects.get(id=1)
    food_selection = FoodSelection.objects.filter(day=i)

    if request.method == 'GET':
        day = request.GET.get('day')
        food_selection = FoodSelection.objects.filter(day=day)

    if request.method == 'POST':
        day_id = request.POST.get('day')
        breakfast = request.POST.get('breakfast')
        lunch = request.POST.get('lunch')
        snaks = request.POST.get('snaks')
        dinner = request.POST.get('dinner')

        day = Day.objects.get(id=day_id)

        # Get or create menu for the selected day
        menu, created = Menu.objects.get_or_create(day=day)

        # Update menu fields
        menu.breakfast = breakfast
        menu.lunch = lunch
        menu.eveningsnaks = snaks
        menu.dinner = dinner
        menu.save()

        return redirect('faculty:ffood')
    else:
        return render(request, 'faculty/ffood.html', {'days': days, 'meals': meals, 'food_selection': food_selection})


def update_food_selection(request):
    day = request.GET.get('day')
    food_selection = FoodSelection.objects.filter(day=day)
    
    return render(request, 'faculty/ffood.html', {'food_selection': food_selection,})




def get_current_date(request):
    current_date = date.today().strftime("%Y-%m-%d")
    return JsonResponse({'current_date': current_date})

def ffee(request):
    today = date.today()
    fees = Fee.objects.all()
    students = Student.objects.all()
    paid_students = []
    unpaid_students = []

    for student in students:
        if Fee.objects.filter(student=student).exists():
            paid_students.append(student)
        else:
            unpaid_students.append(student)
    
    if fees:
        pass
    else:
        for student in students:
            Fee.objects.create(student=student)
    
    context = {
        'fees': fees,
        'today': today,
        'unpaid_students': unpaid_students,
        'paid_students': paid_students,
        'students': students,
    }
    return render(request, 'faculty/ffee.html', context=context)


@login_required
def change_date(request):
    last_date = request.POST.get('last_date')
    fees = Fee.objects.all()
    for fee in fees:
        fee.last_date = last_date
        fee.save()
    return redirect('faculty:ffee')


@login_required
def mark_fee(request, pk):
    today = date.today()
    fee = Fee.objects.get(pk=pk)
    fee.fee_date = today
    fee.status = 'paid'
    fee.save()
    return redirect('faculty:ffee')



@login_required
def delete_fee(request, pk):
    fee = Fee.objects.get(pk=pk)
    fee.status = 'unpaid'
    fee.save()

    return redirect('faculty:ffee')




@login_required
def fcheck(request):
    students = Student.objects.all()
    form = CheckInCheckOut.objects.all()

    if form:
        pass
    else:
        for student in students:
            CheckInCheckOut.objects.create(student=student)
            
    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'faculty/fcheck.html', context=context)


@login_required
def check_in(request, pk):
    time = datetime.now()
    instance = CheckInCheckOut.objects.get(pk=pk)

    instance.check_in = time
    instance.save()

    return redirect('faculty:fcheck')


@login_required
def check_out(request, pk):
    time = datetime.now()
    instance = CheckInCheckOut.objects.get(pk=pk)

    instance.check_out = time
    instance.save()

    return redirect('faculty:fcheck')

@login_required
def cancel_check_in(request, pk):
    instance = CheckInCheckOut.objects.get(pk=pk)

    instance.check_in = None
    instance.save()

    return redirect('faculty:fcheck')


@login_required
def cancel_check_out(request, pk):
    instance = CheckInCheckOut.objects.get(pk=pk)

    instance.check_out = None
    instance.save()

    return redirect('faculty:fcheck')


def fcomplaint(request):
    instances = Complaint.objects.all()
    new = instances.order_by('-id')[:3]
    previous = instances.exclude(id__in=new.values_list('id', flat=True)) 
    context = {
        'new': new,
        'previous': previous,
    }
    return render(request, 'faculty/fcomplaint.html', context=context)

def fslot(request):
    instances = Slot.objects.all()
    

    context = {
        'instances': instances,
    }
    return render(request, 'faculty/fslot.html', context=context)



def fchangepass(request):
    

    context = {
     
    }
    return render(request, 'faculty/fchangepass.html', context=context)







def fforgetpass(request):
    

    context = {
     
    }
    return render(request, 'faculty/fforgetpass.html', context=context)

def fprofile(request):
    

    context = {
     
    }
    return render(request, 'faculty/fprofile.html', context=context)

def fupdatepass(request):
    

    context = {
     
    }
    return render(request, 'faculty/fupdatepass.html', context=context)
