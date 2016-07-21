from proof.models import Theorem, Axiom, Definition
from rest_framework import viewsets
from .serializers import TheoremSerializer, AxiomSerializer, DefinitionSerializer

class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

class TheoremViewSet(viewsets.ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer

class AxiomViewSet(viewsets.ModelViewSet):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer
