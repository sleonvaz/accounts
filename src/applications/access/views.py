from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from applications.access.form import ClientRegistrationForm
from applications.core.models import Clients, Account
from django.db.models import Max
from helpers.logger import LoggerManager


def signup(request):
    """
    Function to sing up user that not are admins

    :param request: This param contain all the information associated to the request
    :param type request: Request
    :return: The URL to render
    :rtype: str
    """

    try:
        if request.method == 'POST':
            form = ClientRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                max_id = Account.objects.all().aggregate(Max('id'))['id__max']
                user = Account.objects.filter(id=max_id)
                user.update(is_staff=False)
                web_group, created = Group.objects.get_or_create(name='web_group')
                web_group.user_set.add(user.get().id)

                return redirect('client_list')
        else:
            form = ClientRegistrationForm()

        log = LoggerManager('info', 'singup-info', session=request.session)
        log.write_exception(request.data)

        return render(request, 'registration/signup.html', {
            'form': form
        })
    except Exception as ex:
        log = LoggerManager('exception', 'singup-exception', session=request.session)
        log.write_exception(ex)


@login_required(login_url='/accounts/login/')
def signup_manager(request):
    """
    Function to sing up user that not are admins

    :param request: This param contain all the information associated to the request
    :param type request: Request
    :return: The URL to render
    :rtype: str
    """
    try:
        if request.method == 'POST':
            form = ClientRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                max_id = Account.objects.all().aggregate(Max('id'))['id__max']
                user = Account.objects.filter(id=max_id)
                user.update(is_staff=False)
                web_group, created = Group.objects.get_or_create(name=request.user.email)
                web_group.user_set.add(request.user.id)
                web_group.user_set.add(user.get().id)

                return redirect('client_list')
        else:
            form = ClientRegistrationForm()

        log = LoggerManager('info', 'singup_manager-info', session=request.session)
        log.write_exception(request.data)

        return render(request, 'registration/signup.html', {
            'form': form
        })
    except Exception as ex:
        log = LoggerManager('exception', 'singup_manager-exception', session=request.session)
        log.write_exception(ex)
