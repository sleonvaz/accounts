from django.db import models
from django.conf import settings

class Clients(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)
    iban = models.CharField(max_length=30, unique=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Clients'