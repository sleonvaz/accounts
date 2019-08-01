from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from applications.core.models import Clients

# def home(request):
#     if request.user.is_authenticated:
#         count = User.objects.count()
#         return render(request, 'home.html', {
#             'count': count
#         })
#     else:
#         return redirect('/accounts/login/')
#


@method_decorator(login_required, name='dispatch')
class ClientList(ListView):
    model = Clients

@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    model = Clients

@method_decorator(login_required, name='dispatch')
class ClientCreate(CreateView):
    model = Clients
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClientUpdate(UpdateView):
    model = Clients

@method_decorator(login_required, name='dispatch')
class ClientDelete(DeleteView):
    model = Clients
