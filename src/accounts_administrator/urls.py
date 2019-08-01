
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from applications.access import views
# from applications.logger.views import LogOutView



from accounts_administrator import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('applications.logger.urls')),
    # path('logout/', LogOutView.as_view(), name='logout'),
]
