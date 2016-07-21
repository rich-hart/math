from proof.models import Theorem, Axiom
from rest_framework import serializers

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

