from django.shortcuts import render
from rest_framework import generics
from datetime import datetime
from .models import LongTermPermit
from .serializers import LongTermPermitSerializer, LongTermWorkPermitApprovalSerializer
from rest_framework.response import Response

"""
Long Term permit application,
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

"""
Compute Years Of Residence
"""
class YearsOfResidenceView(generics.RetrieveAPIView):
    serializer_class = LongTermPermitSerializer
    lookup_field = 'passport_number'
    
    def get_queryset(self):
        passport_number = self.kwargs['passport_number']
        queryset = LongTermPermit.objects.filter(approval_status='A', passport_number=passport_number)
        print(queryset)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        years_of_residence = self.calculate_years_of_residence(queryset)
        response_data = {
            'passport_number': queryset.first().passport_number if queryset.exists() else None,
            'years_of_residence': years_of_residence
        }
        return Response(response_data)
    
    def calculate_years_of_residence(self, queryset):
        total_years = 0
        
        for permit in queryset:
            date_from = datetime.strptime(permit.date_from.strftime("%Y-%m-%d"), "%Y-%m-%d").date()
            date_to = datetime.strptime(permit.date_to.strftime("%Y-%m-%d"), "%Y-%m-%d").date()
            years_of_permit = (date_to - date_from).days/365
            total_years += years_of_permit
        return total_years