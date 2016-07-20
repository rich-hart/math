from proof.models import Proof
from rest_framework import serializers


class ProofSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proof
        fields = ('id',
                  'title',
                  'prove', 
                  'given', 
#                  'diagram',
#                  'plan',
                          )

