import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse


def allow_faculty(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_faculty:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status": "error",
                    "title": "Unauthorized Access",
                    "message": "You can't perform this action."
                }
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return HttpResponseRedirect(reverse("web:faculty_access"))
        return function(request, *args, **kwargs)
    return wrapper




def allow_parent(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_parents:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status": "error",
                    "title": "Unauthorized Access",
                    "message": "You can't perform this action."
                }
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return HttpResponseRedirect(reverse("web:parent_access"))
        return function(request, *args, **kwargs)
    return wrapper




def allow_student(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_student:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status": "error",
                    "title": "Unauthorized Access",
                    "message": "You can't perform this action."
                }
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return HttpResponseRedirect(reverse("web:student_access"))
        return function(request, *args, **kwargs)
    return wrapper



