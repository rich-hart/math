from proof.models import Theorem, Axiom
from rest_framework import viewsets
from .serializers import TheoremSerializer, AxiomSerializer

class TheoremViewSet(viewsets.ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer

class AxiomViewSet(viewsets.ModelViewSet):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer
