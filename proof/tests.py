from django.test import TestCase
from .models import Argument

class ArgumentTestCase(TestCase):
    def setUp(self):
        Argument.objects.create(statements=("statement_1","statement_2"),
                                reasons=("reason_1","reason_2"))



    def test_arguments_created(self):
        import ipdb; ipdb.set_trace()
        arguments = Argument.objects.all()
        self.assertNotEqual(arguments,[])
   


