from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory
import json

from .views import TheoremViewSet
class TheoremAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser() 

    def test_post(self):
        request = self.factory.get('/api/theorems/', format='json', follow=True)
        request.user = self.user
        data = {   
                   "name": "name",
                   "prove": "prove",
                   "given": "given",
                   "plan": "plan",
                   "statements": [],
                   "reasons": [],
               }
        response = self.client.post('/api/theorems/',data, format='json', follow=True)
        self.assertEqual(response.status_code, 201)
        expected = data
        expected['id'] = 1
        expected['diagram']=None 
        returned = json.loads(response.content.decode(response.charset))
        self.assertEqual(expected, returned)

#    def test_post_with_file(self):
#        request = self.factory.get('/api/proofs/', format='json', follow=True)
#        request.user = self.user
#        with open('api/test_image.jpeg') as fp:
#            data = {   
#                       "title": "title",
#                       "prove": "prove",
#                       "diagram": fp, 
#                       "given": "given",
#                       "plan": "plan",
#                       "statements": [],
#                       "reasons": [],
#                   }
#            response = self.client.post('/api/proofs/',data)
#            self.assertEqual(response.status_code, 201)
#            expected = data
#            expected['id'] = 1
#            expected['diagram']=None 
#            returned = json.loads(response.content.decode(response.charset))
#            self.assertEqual(expected, returned)
