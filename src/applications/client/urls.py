from django.urls import path
from applications.client import views

urlpatterns = [

    path('clients', views.ClientList.as_view(), name='client_list'),
    path('client/<int:pk>', views.ClientDetail.as_view(), name='clients_detail'),
    path('create', views.ClientCreate.as_view(), name='clients_create'),
    path('update/<int:pk>', views.ClientUpdate.as_view(), name='clients_update'),
    path('delete/<int:pk>', views.ClientDelete.as_view(), name='clients_delete'),
]