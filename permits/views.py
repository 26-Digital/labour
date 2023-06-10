from django.shortcuts import render
from rest_framework import generics
from .models import LongTermPermit
from .serializers import LongTermPermitSerializer

class LongTermPermitListCreateView(generics.ListCreateAPIView):
    queryset = LongTermPermit.objects.all()
    serializer_class = LongTermPermitSerializer

class LongTermPermitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LongTermPermit.objects.all()
    serializer_class = LongTermPermitSerializer