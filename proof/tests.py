from django.test import TestCase
from .models import Theorem

class TheoremTestCase(TestCase):
    def setUp(self):
        Theorem.objects.create(title='title',
                             prove='prove',
                             given='given',
                             diagram='test_image.jpeg',
                             plan='plan',
                             statements=("statement_1","statement_2"),
                             reasons=("reason_1","reason_2"))



    def test_class_setup(self):
        pass
   


