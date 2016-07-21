from proof.models import Theorem, Axiom, Definition
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DefinitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Definition
        fields = ('id',
                  'name',
                  'statement',
                          )


class AxiomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Axiom
        fields = ('id',
                  'statement',
                          )


class TheoremSerializer(serializers.HyperlinkedModelSerializer):
    statements = serializers.ListField(child=serializers.CharField())
    reasons = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Theorem
        fields = ('id',
                  'name',
                  'prove', 
                  'given',
                  'diagram',
                  'plan',        
                  'statements', 
                  'reasons',
                          )

