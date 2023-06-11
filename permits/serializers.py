from rest_framework import serializers
from .models import LongTermPermit

class LongTermPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTermPermit
        fields = '__all__'

class LongTermWorkPermitApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTermPermit
        fields = ['approval_status']