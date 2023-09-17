from rest_framework import serializers
from .models import Omang

class OmangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omang
        fields = '__all__'