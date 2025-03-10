from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from customer.models import *

from .models import *
from users.models import *
from faculty.models import *
from web.models import *
from .forms import *

from django.db.models import Sum

from decimal import Decimal  # Import Decimal for precise calculations

from django.shortcuts import redirect
from django.contrib import messages
import random
import string
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from django.views.decorators.http import require_http_methods
from main.decorators import allow_student



def login(request):
    if request.method == 'POST':
        register_id = request.POST.get('register_id')
        password = request.POST.get('password')
        try:
            user = User.objects.get(register_id=register_id)
            if user.second_pass == password:
                if user.is_student:
                    auth_login(request, user)
                    print('valid')
                    return HttpResponseRedirect(reverse('student:sdashbord'))
                else:
                    context = {
                        "error": True,
                        "message": "You are not Student"
                    }
                    return render(request, 'parents/plogin.html', context=context)
            else:
                context = {
                    "error": True,
                    "message": "Invalid Register Id or Password"
                }
                return render(request, 'parents/plogin.html', context=context)
        except User.DoesNotExist:
            context = {
                "error": True,
                "message": "Invalid Register Id or Password"
            }
            return render(request, 'parents/plogin.html', context=context)
    else:
        return render(request, 'parents/plogin.html')


@login_required(login_url='student:login')
@allow_student
def sdashbord(request):

    context = {
     
    }
    return render(request, 'student/sdashbord.html', context=context)


@login_required(login_url='student:login')
@allow_student
@require_http_methods(['POST'])
def food_selection_submit(request):
    user = request.user
    checked_checkboxes = request.POST.getlist('checkedCheckboxes')
    unchecked_checkboxes = request.POST.getlist('uncheckedCheckboxes')

    checked_checkbox_ids = [int(id) for id in checked_checkboxes[0].split(',')]
    unchecked_checkbox_ids = [int(id) for id in unchecked_checkboxes[0].split(',')]

    for checkbox_id in checked_checkbox_ids:
        food_selection = FoodSelection.objects.get(id=checkbox_id)
        food_selection.user.add(user)
        food_selection.save()

    for checkbox_id in unchecked_checkbox_ids:
        food_selection = FoodSelection.objects.get(id=checkbox_id)
        food_selection.user.remove(user)
        food_selection.save()

    return JsonResponse({'message': 'Food selections updated successfully'})




@login_required(login_url='student:login')
@allow_student
def sfood(request):
    user=request.user
    food_selections = FoodSelection.objects.all()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = Day.objects.all()
    instances = Menu.objects.all()
    meals = ['breakfast', 'lunch', 'evening_snacks', 'dinner']
    if not days:
        for i in week:
            food = Day.objects.create(
                name=i
            )

            food.save()

    if not food_selections:
        for day in days:
            for meal in meals:
                food = FoodSelection.objects.create(
                    day=day,
                    meal=meal
                )

                food.save()

    context = {
        'food_selections': food_selections, 
        'days': days,
        'instances': instances,
        'user': user,
    }

    return render(request, 'student/sfood.html', context=context)


@login_required(login_url='student:login')
@allow_student
def salert(request):
    all_alerts = Alert.objects.all()
    new_alerts = all_alerts.order_by('-id')[:3]
    previous_alerts = all_alerts.exclude(id__in=new_alerts.values_list('id', flat=True)) 

    context = {
        'new_alerts': new_alerts,
        'previous_alerts': previous_alerts,
    }
    return render(request, 'student/salert.html', context=context)


@login_required(login_url='student:login')
@allow_student
def scomplaint(request):

    return render(request, 'student/scomplaint.html')


@login_required(login_url='student:login')
@allow_student
@require_http_methods(['POST'])
def post_complaint(request):
    user=request.user
    student = get_object_or_404(Student, user=user) 
    complaint_text = request.POST.get('complaint')
    complaint = Complaint(student=student, message=complaint_text)
    complaint.save()
    return JsonResponse({'message': 'Complaint posted successfully'})



@login_required(login_url='student:login')
@allow_student
def sslot(request):
    instances = Slot.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'student/sslot.html', context=context)


@login_required(login_url='student:login')
@allow_student
@login_required
def book_slot(request, pk):
    user=request.user
    student = get_object_or_404(Student, user=user) 
    slot = Slot.objects.get(pk=pk)
    slot.booked_student = student
    slot.save()

    return redirect('student:sslot')



@login_required(login_url='student:login')
@allow_student
def sprofile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    puser = User.objects.get(email=user.email)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        hostel_id = request.POST.get('hostel_id')
        register_no = request.POST.get('register_no')
        department = request.POST.get('department')
        address = request.POST.get('address')
        guardian_name = request.POST.get('guardian_name')
        guardian_number = request.POST.get('guardian_number')

        profile.name = name
        profile.phone_number = phone_number
        profile.hostel_id = hostel_id
        profile.register_no = register_no
        puser.register_id = register_no
        profile.department = department
        profile.address = address
        profile.guardian_name = guardian_name
        profile.guardian_number = guardian_number
        profile.save()
    return render(request, 'student/sprofile.html', {'profile': profile})





