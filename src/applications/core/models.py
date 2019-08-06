from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """

        Class to create a base user to inherit for
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """

            Function to create and save a user with the given account_no and password.

            :param str email: Email to save on the DB.
            :param str password: Password to save on the DB.
            :param extra_fields: Extra fields to save on the DB.
            :return: The user created
            :rtype: UserManager
        """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """

            Function to create and save a user with the given account_no and password.

            :param str email: Email to save on the DB.
            :param str password: Password to save on the DB.
            :param extra_fields: Extra fields to save on the DB.
            :return: The user created
            :rtype: UserManager:
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """

           Function to create and save a superuser with the given account_no and password and the privileges added.

           :param str email: Email to save on the DB.
           :param str password: Password to save on the DB.
           :param extra_fields: Extra fields to save on the DB.
           :return: The superuser created
           :rtype: UserManager:
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Clients(AbstractUser):
    """

        Class to create a Client user
    """
    username = models.CharField(
        _('username'), max_length=30, unique=True, null=True, blank=True,
        help_text=_(
            'Required. 30 characters or fewer. Letters, digits and '
            '@/./+/-/_ only.'
        ),
        validators=[
            RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. '
                  'This value may contain only letters, numbers '
                  'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    name = models.CharField(max_length=30, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Account(Clients):
    """

            Class to create a Account.
    """

    iban = models.CharField(
        _('IBAN'), max_length=30, unique=False, null=True, blank=True,
        help_text=_(
            'Ex: CC12 XXXX 12XX 1234 1234 1234 1234 1234 123'
            'Required. between 15 and 30 characters. Two first digits for country code(capitalized) , '
            'and account number.'
            ' You must leave the spaces between each numbers group. '
        ),
        validators=[
            RegexValidator(
                r'^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})([ \-]?'
                r'[A-Z0-9]{1,3})?$',
                _('Enter a valid IBAN'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that IBAN already exists."),
        })
