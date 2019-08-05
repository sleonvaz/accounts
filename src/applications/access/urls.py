from django.urls import path, include
from applications.access import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('manager/signup/', views.signup_manager, name='signup_manager'),
    path('accounts/', include('django.contrib.auth.urls')),

]