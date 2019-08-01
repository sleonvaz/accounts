from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from applications.core.models import Clients


@method_decorator(login_required, name='dispatch')
class ClientList(ListView):
    """
        Class to manage client list  url view
    """
    model = Clients


@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    """
           Class to manage an specific client url view
    """
    model = Clients


@method_decorator(login_required, name='dispatch')
class ClientCreate(CreateView):
    """
              Class to create client url view
    """
    model = Clients
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class ClientUpdate(UpdateView):
    """
              Class to update an specific client url view
    """
    model = Clients
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class ClientDelete(DeleteView):
    """
              Class to delete an specific client url view
    """
    model = Clients
