from django.contrib.auth.forms import UserCreationForm
from applications.core.models import Account

class ClientRegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = [
            "name",
            "last_name",
            "email",
            "iban",
            "password1",
            "password2"
        ]
