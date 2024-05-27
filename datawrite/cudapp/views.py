from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Signup
from .serializers import SignupSerializer
from rest_framework import status

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['POST'])
def signupAPI(request):
    data = request.data
    print(data)
    data['SETBX_ID'] = int(data['SETBX_ID'])
    serializer = SignupSerializer(data=data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)