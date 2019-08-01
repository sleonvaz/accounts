
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout

# from applications.logger.views import LogOutView



from accounts_administrator import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('applications.access.urls')),
    path('', include('applications.client.urls')),
    # path('logout/', LogOutView.as_view(), name='logout'),
]
