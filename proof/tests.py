from django.test import TestCase
from .models import Theorem

import yaml

from .utils import book_to_json
class Utils(TestCase):
    def test_book_to_json(self):
        import ipdb; ipdb.set_trace()
        returned = book_to_json('data/test/book/geometry/')
        self.assertIsNone(returned) 
    

