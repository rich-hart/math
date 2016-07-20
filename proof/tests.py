from django.test import TestCase
from .models import Proof

class ProofTestCase(TestCase):
    def setUp(self):
        Proof.objects.create(title='title',
                             prove='prove',
                             given='given',
                             diagram='test_image.jpeg',
                             plan='plan',
                             statements=("statement_1","statement_2"),
                             reasons=("reason_1","reason_2"))



    def test_class_setup(self):
        pass
   


