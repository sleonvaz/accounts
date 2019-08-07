from django.urls import path, include
from applications.access import views
from helpers.startup import create_default_superadmin

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('manager/signup/', views.signup_manager, name='signup_manager'),
    path('user/signup/', views.signup_user, name='signup_user'),
    path('accounts/', include('django.contrib.auth.urls')),

]