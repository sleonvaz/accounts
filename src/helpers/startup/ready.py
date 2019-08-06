from django.db.utils import OperationalError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from applications.core.models import Clients


def create_default_superadmin():
    """ Create a default admin user with password admin """
    try:
        User = get_user_model()
        if  not Clients.objects.filter(email='admin@rindus.com').exists():
            superuser = User.objects.create_superuser('admin@rindus.com', 'rindus2019')
            web_group, created = Group.objects.get_or_create(name='web_group')
            web_group.user_set.add(superuser.id)
    except OperationalError:
        print('error')
