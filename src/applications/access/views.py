from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from applications.access.form import ClientRegistrationForm
from applications.core.models import Clients, Account
from django.db.models import Max
from django.contrib.auth import get_user_model, login, authenticate



def signup(request):
    """
    Function to sing up user that not are admins

    :param request: This param contain all the information associated to the request
    :param type request: Request
    :return: The URL to render
    :rtype: Render
    """
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            max_id = Clients.objects.all().aggregate(Max('id'))['id__max']
            a = Account.objects.all()
            a = Account.objects.filter(clients_ptr=request.user).iban
            user = Clients.objects.filter(id=max_id)
            user.update(is_staff=False)
            if not Clients.objects.filter(email='admin@rindus.com').exists():
                User = get_user_model()
                superuser = User.objects.create_superuser('admin@rindus.com', 'rindus2019')
                web_group, created = Group.objects.get_or_create(name='web_group')
                web_group.user_set.add(superuser.id)
                web_group.user_set.add(user.get().id)

            else:
                web_group, created = Group.objects.get_or_create(name='web_group')
                web_group.user_set.add(user.get().id)

            return redirect('client_list')
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
@method_decorator(login_required, name='dispatch')
def signup_manager(request):
    """
    Function to sing up user that not are admins

    :param request: This param contain all the information associated to the request
    :param type request: Request
    :return: The URL to render
    :rtype: Render
    """
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            max_id = Clients.objects.all().aggregate(Max('id'))['id__max']
            user = Clients.objects.filter(id=max_id)
            user.update(is_staff=False)
            web_group, created = Group.objects.get_or_create(name=request.user.email)
            web_group.user_set.add(request.user.id)
            web_group.user_set.add(user.get().id)

            return redirect('client_list')
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
