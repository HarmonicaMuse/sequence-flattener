from rest_framework import serializers
from .models import Sequence


class SequenceSerializer(serializers.ModelSerializer):
    items = serializers.JSONField()

    class Meta:
        model = Sequence
        fields = ('items', 'result', 'added_on')