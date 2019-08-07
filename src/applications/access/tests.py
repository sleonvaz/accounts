from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from applications.core.models import UserManager
from .forms import *




class User_Views_Test(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser('admin@rindus.com', 'rindus2019')


    def test_add_user_view(self):
        user_login = authenticate(email="admin@rindus.com", password="rindus2019")
        response = self.client.get(reverse("signup_user"))
        self.assertEqual(response.status_code, 302)


    def test_add_admin_view(self):
        user_login = authenticate(email="admin@rindus.com", password="rindus2019")
        response = self.client.get(reverse("signup_manager"))
        self.assertEqual(response.status_code, 302)



class User_Form_Test(TestCase):

    # Valid Form Data
    def test_client_form_valid(self):
        form = ClientRegistrationForm(data={'name': "Juan", 'last_name': 'Jimenez','email': "user@mp.com",
                                            'iban': 'AS12 1234 1234 1234 1234 12',
                                            'password1': "malaga2019",'password2': "malaga2019"
                                            })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_admin_form_valid(self):
        form = AdminRegistrationForm(data={'email': "", 'password': "mp"})
        self.assertFalse(form.is_valid())

