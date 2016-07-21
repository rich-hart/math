from proof.models import Theorem, Axiom, Definition
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (TheoremSerializer, 
                          AxiomSerializer, 
                          DefinitionSerializer,
                          UserSerializer, 
                          GroupSerializer,)
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import renderers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

class TheoremHighlight(generics.GenericAPIView):
    queryset = Theorem.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        theorem = self.get_object()
        return Response({'name': theorem.name },template_name="theorem.html")


class TheoremViewSet(viewsets.ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer

class AxiomHighlight(generics.GenericAPIView):
    queryset = Axiom.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        axiom= self.get_object()
        return Response({'name': axiom.name },template_name="axiom.html")


class AxiomViewSet(viewsets.ModelViewSet):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer
