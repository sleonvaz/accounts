from django.contrib import admin
from django.urls import path, include
from helpers.startup import create_default_superadmin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('applications.access.urls')),
    path('', include('applications.client.urls')),
]

create_default_superadmin()
