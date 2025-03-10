
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from faculty import urls
from parents import urls
from student import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ("web.urls", namespace="web")),
    path('faculty/', include ("faculty.urls", namespace="faculty")),
    path('parent/', include ("parents.urls", namespace="parents")),
    path('student/', include ("student.urls", namespace="student")),

]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

