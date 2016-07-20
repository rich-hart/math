from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory
import json

from .views import ProofViewSet
class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser() 

    def test_proofs(self):
        request = self.factory.get('/api/proofs/', format='json', follow=True)
        request.user = self.user
        data = {   
                   "title": "title",
                   "prove": "prove",
                   "given": "given",
                   #"diagram": None,
                   "plan": "plan",
                   "statements": [],
                   "reasons": [],
               }
        response = self.client.post('/api/proofs/',data, format='json', follow=True)
        #response = ProofViewSet.as_view(request)
        self.assertEqual(response.status_code, 201)
        expected = data
        expected['id'] =1
        expected['diagram']=None 
        returned = json.loads(response.content.decode(response.charset))
        self.assertEqual(expected, returned)
