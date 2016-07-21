from proof.models import Proof, Axiom
from rest_framework import serializers

class AxiomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Axiom
        fields = ('id',
                  'statement',
                          )


class ProofSerializer(serializers.HyperlinkedModelSerializer):
    statements = serializers.ListField(child=serializers.CharField())
    reasons = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Proof
        fields = ('id',
                  'title',
                  'prove', 
                  'given',
                  'diagram',
                  'plan',        
                  'statements', 
                  'reasons',
                          )

