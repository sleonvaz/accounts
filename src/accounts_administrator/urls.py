
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import auth_logout

from accounts_administrator import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),
    path('clients/', 'applications.clients.urls'),
]
