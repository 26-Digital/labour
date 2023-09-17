from django.shortcuts import render
from rest_framework import viewsets
from .models import Omang
from .serializers import OmangSerializer

class OmangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Omang.objects.all()
    serializer_class = OmangSerializer

    def get_queryset(self):
        id_number = self.request.query.params.get('ID_Number', None)
        if id_number is not None:
            return Omang.objects.filter(ID_Number=id_number)
        return super().get_queryset()
