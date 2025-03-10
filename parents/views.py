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
from main.decorators import allow_parent
from datetime import datetime
from datetime import date




def login(request):
    if request.method == 'POST':
        register_id = request.POST.get('register_id')
        password = request.POST.get('password')
        try:
            user = User.objects.get(register_id=register_id)
            if user.second_pass == password:
                if user.is_parents:
                    auth_login(request, user)
                    print('valid')
                    return HttpResponseRedirect(reverse('parents:pdashbord'))
                else:
                    context = {
                        "error": True,
                        "message": "You are not Parent"
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




@login_required(login_url='parents:login')
@allow_parent
def pdashbord(request):
    context = {
    }
    return render(request, 'parents/pdashbord.html', context=context)

@login_required(login_url='parents:login')
@allow_parent
def pattendance(request):
    instances = Attendance.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'parents/pattendance.html', context=context)

@login_required(login_url='parents:login')
@allow_parent
def pcheck(request):
    instances = CheckInCheckOut.objects.all()

    context = {
        'instances': instances,
    }
    return render(request, 'parents/pcheck.html', context=context)


@login_required(login_url='parents:login')
@allow_parent
def pfee(request):
    instances = Fee.objects.all()
    month=datetime.now().strftime("%b")
    context = {
        'instances': instances,
        'month': month,
    }
    return render(request, 'parents/pfee.html', context=context)



@login_required(login_url='parents:login')
@allow_parent
def pnotification(request):
    instances = Notification.objects.all()
    new = instances.order_by('-id')[:3]
    previous = instances.exclude(id__in=new.values_list('id', flat=True))

    context = {
        'new': new,
        'previous': previous,
    }
    return render(request, 'parents/pnotificaton.html', context=context)



