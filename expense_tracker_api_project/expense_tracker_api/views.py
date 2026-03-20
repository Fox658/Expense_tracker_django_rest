from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloWorldView(APIView):

    def get(self, request, format=None):
        """
        Hello world endpoint for Django REST Framework (DRF)
        """
        return Response({"message": "hello world!"})
