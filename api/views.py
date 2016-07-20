from proof.models import Proof
from rest_framework import viewsets
from .serializers import ProofSerializer

class ProofViewSet(viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer


