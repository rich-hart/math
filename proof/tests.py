from django.test import TestCase
from .models import Proof

class ProofTestCase(TestCase):
    def setUp(self):
        Proof.objects.create(statements=("statement_1","statement_2"),
                                reasons=("reason_1","reason_2"))



    def test_proof_created(self):
        arguments = Proof.objects.all()
        self.assertNotEqual(arguments,[])
   


