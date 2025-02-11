from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from customer.models import *

from web.models import *

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


def logout(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('faculty:login')