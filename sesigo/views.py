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
            # Convert the result (which is a Python dictionary) to JSON
            #json_response = json.dumps(result, ensure_ascii=False, indent=2)
            #print(data)
            # Return the JSON data as a response
            print(result)
            #json_res = serialize('json',[result,])
            #return JsonResponse({"S":{"CC4":"O","VRB":"dirisa","NN-T":{"NN":"dilo","lerui":{"L22_0":"tsa","lethalosi":{"L24":"kwa","NN-T":{"NN-T":{"NN":"tirong","lerui":{"L12_1":"ya","L35":"gagwe","leamanyi":{"CC9":"tse","C10":"di","VRB":{"VRB_ng":"rekwang","lethalosi":{"L24":"kwa","NN-T":{"NN":"mmolong","thaodi":{"lethaodi":{"CC4":"o","ADJ1":"motona","lerui":{"L31_2":"wa","NN":"Palapye",".":"."}}}}}}}}}}}}}}}, content_type="application/json", status=status.HTTP_200_OK, safe=False)
            return JsonResponse(json.loads(result), content_type="application/json", status=status.HTTP_200_OK, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)