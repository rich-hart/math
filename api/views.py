from proof.models import Proof, Axiom
from rest_framework import viewsets
from .serializers import ProofSerializer, AxiomSerializer

class ProofViewSet(viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer

class AxiomViewSet(viewsets.ModelViewSet):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer
