# serializers.py
from rest_framework import serializers

class SetswanaNltkSerializer(serializers.Serializer):
    text = serializers.CharField()
