from django.core.urlresolvers import reverse

from common.tests.core import TestCase


class AccountChangePasswordTestCase(TestCase):
    def setUp(self):
        self.login_user()

    def test_show_change_password_link(self):
        self.visit(reverse('accounts:profile'))
        self.assertEqual(reverse('account_change_password'), self.link('Change password').attrs['href'])
