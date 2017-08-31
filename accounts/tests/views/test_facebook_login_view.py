from django.test.client import RequestFactory

from accounts.views.facebook_login_view import FacebookProvider2
from common.tests.core import TestCase


class FacebookProvider2Test(TestCase):
    def test_extract_common_fields_always_have_username(self):
        request = RequestFactory()
        provider = FacebookProvider2(request)
        data = provider.extract_common_fields({
            'id': 1
        })
        self.assertEqual(data['username'], 'fb_1')
