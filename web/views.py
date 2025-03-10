from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from customer.models import *
from web.models import *
from users.models import *
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('web:index')



def forgetpass(request):
    users = User.objects.all()
    user=request.user
    if request.method == 'POST':
        registerid = request.POST.get('registerid')
        email = request.POST.get('email')
        for user in users:
            userregister_id = user.register_id
            useremail = user.email

            if registerid in userregister_id and email in useremail:
                user = User.objects.get(register_id=registerid)
                auth_login(request, user)
                return HttpResponseRedirect(reverse('web:updatepass'))
            else:
                context = {
                    "error" : True,
                    "message" : "Register ID or Email incorrect"
                }
                return render(request, 'faculty/fforgetpass.html', context=context)  
    else:
        return render(request, 'faculty/fforgetpass.html')




def updatepass(request):
    user=request.user
    if request.method == 'POST':
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password == password2:
            user.set_password(password)
            user.second_pass = password
            user.save()
            if user.is_faculty:
                return HttpResponseRedirect(reverse('faculty:login'))
            elif user.is_parents:
                return HttpResponseRedirect(reverse('parents:login'))
            elif user.is_student:
                return HttpResponseRedirect(reverse('student:login'))
            else:
                return HttpResponseRedirect(reverse('faculty:login'))
            
        else:
            context = {
                "error" : True,
                "message" : "Confirm password is Not Same as Password"
            }
            return render(request, 'faculty/fupdatepass.html', context=context)
    else:
        return render(request, 'faculty/fupdatepass.html')



def faculty_access(request):
    return render(request, 'faculty_access.html')

def parent_access(request):
    return render(request, 'parent_access.html')

def student_access(request):
    return render(request, 'student_access.html')
