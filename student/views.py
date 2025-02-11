from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from customer.models import *

from .models import *
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



# @login_required(login_url='web:login') 
def index(request):
    

    context = {
     
    }
    return render(request, 'index.html', context=context)

def login(request):
    if request.method == 'POST':
        register_id = request.POST.get('register_id')
        password = request.POST.get('password')
        try:
            user = User.objects.get(register_id=register_id)
            if user.second_pass == password and user.is_student:
                auth_login(request, user)
                print('valid')
                return HttpResponseRedirect(reverse('faculty:fdashbord'))
            else:
                context = {
                    "error": True,
                    "message": "Invalid Register Id or Password"
                }
                return render(request, 'faculty/flogin.html', context=context)
        except User.DoesNotExist:
            context = {
                "error": True,
                "message": "Invalid Register Id or Password"
            }
            return render(request, 'faculty/flogin.html', context=context)
    else:
        return render(request, 'parents/plogin.html')


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




def sfood(request):
    user=request.user
    food_selections = FoodSelection.objects.all()
    instances = Menu.objects.all()
    for instance in instances:
        print(instance)
        
    days = Day.objects.all
    context = {
        'food_selections': food_selections, 
        'days': days,
        'instances': instances,
    }

    return render(request, 'student/sfood.html', context=context)


def salert(request):
    all_alerts = Alert.objects.all()
    new_alerts = all_alerts.order_by('-id')[:3]
    previous_alerts = all_alerts.exclude(id__in=new_alerts.values_list('id', flat=True)) 

    context = {
        'new_alerts': new_alerts,
        'previous_alerts': previous_alerts,
    }
    return render(request, 'student/salert.html', context=context)


def scomplaint(request):

    return render(request, 'student/scomplaint.html')


@require_http_methods(['POST'])
def post_complaint(request):
    user=request.user
    student = get_object_or_404(Student, user=user) 
    complaint_text = request.POST.get('complaint')
    complaint = Complaint(student=student, message=complaint_text)
    complaint.save()
    return JsonResponse({'message': 'Complaint posted successfully'})



def sslot(request):
    instances = Slot.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'student/sslot.html', context=context)


@login_required
def book_slot(request, pk):
    user=request.user
    student = get_object_or_404(Student, user=user) 
    slot = Slot.objects.get(pk=pk)
    slot.booked_student = student
    slot.save()

    return redirect('student:sslot')



def upupdatepass(request):

    context = {
     
    }
    return render(request, 'student/upupdatepass.html', context=context)




def schangepass(request):

    context = {
     
    }
    return render(request, 'student/schangepass.html', context=context)



def sdashbord(request):

    context = {
     
    }
    return render(request, 'student/sdashbord.html', context=context)

def sforgetpass(request):

    context = {
     
    }
    return render(request, 'student/sforgetpass.html', context=context)




def sprofile(request):

    context = {
     
    }
    return render(request, 'student/sprofile.html', context=context)



def supdatepass(request):

    context = {
     
    }
    return render(request, 'student/supdatepass.html', context=context)




