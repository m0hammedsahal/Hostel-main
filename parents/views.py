from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from customer.models import *

from web.models import *
from users.models import *
from faculty.models import *
from .models import *

from django.db.models import Sum

from decimal import Decimal  # Import Decimal for precise calculations

from django.shortcuts import redirect
from django.contrib import messages
import random
import string
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse




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
            if user.second_pass == password and user.is_parents:
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



def pdashbord(request):
    

    context = {
    }
    return render(request, 'parents/pdashbord.html', context=context)


def pattendance(request):
    instances = Attendance.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'parents/pattendance.html', context=context)

def pcheck(request):
    instances = CheckInCheckOut.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'parents/pcheck.html', context=context)


def pfee(request):
    instances = Fee.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'parents/pfee.html', context=context)



def pnotification(request):
    instances = Notification.objects.all()
    new = instances.order_by('-id')[:3]
    previous = instances.exclude(id__in=new.values_list('id', flat=True))

    context = {
        'new': new,
        'previous': previous,
    }
    return render(request, 'parents/pnotificaton.html', context=context)


def pchangepass(request):
    

    context = {
     
    }
    return render(request, 'parents/pchangepass.html', context=context)


def pforgetpass(request):
    

    context = {
     
    }
    return render(request, 'parents/pforgetpass.html', context=context)
def pupupdatepass(request):
    

    context = {
     
    }
    return render(request, 'parents/pupdatepass.html', context=context)

