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

class SetswanaNltkView(APIView):
    def post(self, request):
        serializer = SetswanaNltkSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data['text']
            dtp = Setswana_Nltk.Setswana_Nltk()
            # Process the text using your Setswana_Nltk class
            result = dtp.generator(nltk.sent_tokenize(text))
            # Convert the result (which is a Python dictionary) to JSON
            #json_response = json.dumps(result, ensure_ascii=False, indent=2)
            #data = serialize("json", result, fields=('title', 'content'))
            # Return the JSON data as a response
            print(result)
            return Response(result, content_type="application/json", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)