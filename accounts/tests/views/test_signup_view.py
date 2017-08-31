from django.urls.base import reverse
from faker import Faker

from common.tests.core import TestCase
from accounts.factories.user_factory import UserFactory

faker = Faker()


class SignUpViewTests(TestCase):
    username = faker.word()
    email = faker.email()
    password = 'randomPassword!@$'

    def test_fail_used_email(self):
        user = UserFactory()
        response = self.client.post(reverse('account_signup'), {
            'email': user.email
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('A user is already registered with this e-mail address.', response.content.decode())

    def test_signup_success(self):

        response = self.client.post(reverse('account_signup'), {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
        })

        self.assertEqual(response.status_code, 302)
