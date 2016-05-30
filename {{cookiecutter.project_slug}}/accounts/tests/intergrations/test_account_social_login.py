from django.conf import settings
from django.core.urlresolvers import reverse

from common.tests.core import BaseLiveTestCase


class AccountSocialLoginTestCase(BaseLiveTestCase):
    def test_login_facebook(self):
        self.visit(reverse('login'))
        self.find('#facebook').click()

        self.until(lambda: self.assertIn('facebook', self.browser.current_url))

        self.find('#loginbutton').should.be.ok

    def test_login_google(self):
        self.visit(reverse('login'))
        self.find('#google').click()
        self.until(lambda: self.assertIn('google', self.browser.current_url))

        self.should_see_text('Sign in with your Google Account')

    def test_twitter(self):
        self.visit(reverse('login'))
        self.find('#twitter').click()
        self.until(lambda: self.assertIn('twitter', self.browser.current_url))

        self.should_see_text('Authorize')
