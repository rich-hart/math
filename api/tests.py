from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory, APIClient
import json

from .views import TheoremViewSet


class POST(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='teacher', 
                                             email='teacher@…', 
                                             password='teacher')
        self.client.force_authenticate(user=self.user)
    def test_post_definition(self):
        url = '/definitionS/'
        data = {'name': 'congruent segments',
                      'statement': 'segments that have the same length'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_post_axiom(self):
        url = '/axioms/'
        data = {'name':'symmetric property of equality',
                  'statement': 'if line segment length AB is equal to line segment length CD '
                               'then line segment length CD is equal to line segment length AB',}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_post_theorem(self):
        url = '/theorems/'
        data = {
                "name": "symmetric property of congruent segments",
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
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




