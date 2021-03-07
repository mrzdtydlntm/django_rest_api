from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# Create a hello world APIView
class HelloApiView(APIView):
    #test API View
    #HTTP GET to get a list or an object from specific API
    def get(self, request, format=None):
        #return a list of APIView features
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'It is similar to a traditional django view',
            'Give you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})