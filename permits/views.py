from django.shortcuts import render
from rest_framework import generics
from .models import LongTermPermit
from .serializers import LongTermPermitSerializer, LongTermWorkPermitApprovalSerializer

"""
Long Term permit application, handled by the applicant/CSR
"""
class LongTermPermitListCreateView(generics.ListCreateAPIView):
    queryset = LongTermPermit.objects.all()
    serializer_class = LongTermPermitSerializer

class LongTermPermitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LongTermPermit.objects.all()
    serializer_class = LongTermPermitSerializer

"""
Approval/Rejection, handled by the Intelligence services
"""
class LongTermWorkPermitApprovalView(generics.RetrieveUpdateAPIView):
    queryset = LongTermPermit.objects.all()
    serializer_class = LongTermWorkPermitApprovalSerializer
    lookup_field = 'permit_number'
    lookup_url_kwarg = 'permit_number'