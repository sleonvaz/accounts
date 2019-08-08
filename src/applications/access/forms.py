from django.contrib.auth.forms import UserCreationForm
from applications.core.models import Account


class ClientRegistrationForm(UserCreationForm):
    """

        Class to create a Client and Account registration.
    """
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


class AdminRegistrationForm(UserCreationForm):
    """

        Class to create an Admin Form registration.
    """
    class Meta:
        model = Account
        fields = [
            "name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]
