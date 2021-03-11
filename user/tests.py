from django.test import TestCase

from .models import User

class UserModelTests(TestCase):

    def test_if_username_can_be_obtained(self):
        user = User(username='monke', password='apple')
        self.assertEqual(user.username, 'monke')