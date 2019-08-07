from django import template
from django.db.utils import OperationalError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """

        Function to know if a user belong to a users group inside the template.

        :param User user: User to be check .
        :param str group_name: Name of the group to ask for.
        :return: True or False
        :rtype: bool
    """
    return user.groups.filter(name=group_name).exists()

