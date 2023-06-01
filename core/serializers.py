from rest_framework import serializers
from .models import saveData


class saveDataSerializer(serializers.Serializer):
    class Meta:
        models = saveData
        fields = ['id', 'key', 'value', 'user', 'created_on', 'updated_on']