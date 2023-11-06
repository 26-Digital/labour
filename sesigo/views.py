from django.shortcuts import render
from rest_framework import generics
from .nltk_setswana import Setswana_Nltk
import nltk
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SetswanaNltkSerializer
import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core import serializers

class SetswanaNltkView(APIView):
    def post(self, request):
        serializer = SetswanaNltkSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data['text']
            dtp = Setswana_Nltk.Setswana_Nltk()
            # Process the text using your Setswana_Nltk class
            result = dtp.generator(nltk.sent_tokenize(text))
            
            # TO CREATE A JSON OBJECT.
            # json_object = json.loads(result)
            # print(json_object["S"])
        
            return JsonResponse(json.loads(result), content_type="application/json", status=status.HTTP_200_OK, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)