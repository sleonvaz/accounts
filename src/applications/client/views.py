from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from applications.core.models import Account


@method_decorator(login_required, name='dispatch')
class ClientList(ListView):
    """

        Class to manage the Accounts list.

        :param request: This param contain all the information associated to the request.
        :param type request: Request
        :return: The view to render.
        :rtype: View
    """

    model = Account


@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    """

         Class to manage the Accounts detail.

         :param request: This param contain all the information associated to the request.
         :param type request: Request
         :return: The view to render.
         :rtype: View
     """
    model = Account


@method_decorator(login_required, name='dispatch')
class ClientCreate(CreateView):
    """

         Class to manage the Accounts create.

         :param request: This param contain all the information associated to the request.
         :param type request: Request
         :return: The view to render.
         :rtype: View
     """
    model = Account
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class ClientUpdate(UpdateView):
    """

         Class to manage the Accounts update.

         :param request: This param contain all the information associated to the request.
         :param type request: Request
         :return: The view to render.
         :rtype: View
     """
    model = Account
    fields = ["name", "last_name", "email", "iban"]

    def get_success_url(self):
        """

        Function to manage the view to render after update.

        :return: The URL to render.
        :rtype: str
        """
        view_name = 'client_list'
        return reverse(view_name)


class ClientDelete(DeleteView):
    """

        Class to manage the Accounts delete.

        :param request: This param contain all the information associated to the request
        :param type request: Request
        :return: The view to render
        :rtype: View
    """
    model = Account

    def get_success_url(self):
        """

           Function to manage the view to render after delete.

           :return: The URL to render.
           :rtype: str
           """
        view_name = 'client_list'
        return reverse(view_name)
