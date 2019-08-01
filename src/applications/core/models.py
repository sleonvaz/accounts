from django.db import models
from django.conf import settings


class Clients(models.Model):
    """
        Model to manage the clients
    """
    Admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)
    iban = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'Clients'
