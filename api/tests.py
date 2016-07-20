from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser() 

    def test_proofs(self):
        request = self.factory.get('/api/proofs')
        request.user = self.user



