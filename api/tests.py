from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIRequestFactory as RequestFactory, APIClient
import json

from .views import TheoremViewSet

import yaml

from proof.utils import book_to_json 
class APITest(TestCase):
    def setUp(self): 
        self.client = APIClient()
        self.factory = RequestFactory()
        names = ['teacher','student','staff','admin']
        self.users = {}
        for name in names:
              self.users[name]= User.objects.create_user(username=name,
                                              email='{}@…'.format(name),
                                              password=name)
   


class Book(APITest):
    def test_staff_post(self):
        user = self.users['staff']
        book = book_to_json('data/test/book/geometry')
        self.client.force_authenticate(user)
        response = self.client.post('api/statements/',data=book,format='json')
        self.assertEqual(response.status_code,201)

    def test_teacher_post(self):
        user = self.users['teacher']
        book = book_to_json('data/test/book/geometry')

        book = json.loads(book)
        for definition in book['definitions']:
            data = { 'name': definition['name'],
                     'statement': definition['statement'],
                     'label':'DE',
                     'citation':book['citation'],
                     'user':user.pk,
            }
            data = {'name': 'congruent segments',
                         'statement': 'segments that have the same length'}
            response = self.client.post('/api/statements/',data)
            self.assertEqual(response.status_code,201)


class Argument(APITest):
    def test_post(self):
        pass
