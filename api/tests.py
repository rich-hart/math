from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory, APIClient
import json

from .views import TheoremViewSet

DEFINITION = {'name': 'congruent segments',
              'statement': 'segments that have the same length'}

AXIOM = {'name':'symmetric property of equality',
         'statement': 'if line segment length AB is equal to line segment length CD '
                      'then line segment length CD is equal to line segment length AB',}
THEOREM = {"name": "symmetric property of congruent segments",
            "statement": "if line segment AB is equal to line segment CD"
                          " then line segment CD is equal to line segment AB",
            "prove": "line segment XY is congruent to line segment PQ",
            "given": "line segment PQ is congruent to line segment XY",
            "diagram": None,
            "plan": "Should be note",
            "statements": [
              "line segment PQ is congruent to line segment XY",
              "length of line segment PQ is equal to the length of line segment XY",
              "length of line segment XY is equal to the length of line segment PQ",
              "line segment XY is congruent to line segment PQ",
            ],
            "reasons": [
              "given",
              "congruent segments", # defnition 
              "symmetric property of equality", # axiom
              "congruent segments",
            ],
          }

class POST(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='teacher', 
                                             email='teacher@…', 
                                             password='teacher')
        self.client.force_authenticate(user=self.user)
    def test_definition(self):
        response = self.client.post('/definitionS/', data=DEFINITION, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_axiom(self):
        response = self.client.post('/axioms/', data=AXIOM, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_theorem(self):
        response = self.client.post('/theorems/', data=THEOREM, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GET(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='teacher', 
                                             email='teacher@…', 
                                             password='teacher')
        self.client.force_authenticate(user=self.user)
        self.client.post('/definitionS/', data=DEFINITION, format='json')
        self.client.post('/axioms/', data=AXIOM, format='json')
        self.client.post('/theorems/', data=THEOREM, format='json')

    def test_theorem_search(self):
        response = self.client.get('/theorems?search={name}'.format(**THEOREM), format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = THEOREM
        search = json.loads(response.content.decode(response.charset))[0]
        returned = dict((k, search[k]) for k in expected.keys() if k in search)
        self.assertEqual(returned,expected)    

