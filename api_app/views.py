from django.shortcuts import render
from django.http import JsonResponse
from .models import TLogin, TSession, TUser
import json
from rest_framework import generics
from .serializers import MiModeloSerializer


def login(request):
    return JsonResponse({'message': 'Bienvenidos a NOHBEK!'})

#def mi_vista(request):
 #   return JsonResponse("Hola, soy tu endpoint")

def get_json_data(request):
    with open('data.json') as json_file:
        data=json.load(json_file)
        return JsonResponse(data, safe=False)    

class MiModeloList(generics.ListCreateAPIView):
    queryset = TLogin.objects.all()
    queryset = TUser.objects.all()
    queryset = TSession.objects.all()
    serializer_class = MiModeloSerializer






