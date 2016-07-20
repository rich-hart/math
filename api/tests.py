from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase


from rest_framework.test import APIRequestFactory as RequestFactory

# Using the standard RequestFactory API to create a form POST request
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = AnonymousUser() 
    def test_proofs(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/proofs')

        request.user = self.user



