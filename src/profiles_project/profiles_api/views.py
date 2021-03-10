from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

# Create your views here.

# Create a hello world APIView
class HelloApiView(APIView):
    #test API View
    serializer_class = serializers.HelloSerializer
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
    
    def post(self, request):
        #create a hello message with our name
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        #Handles updating an object
        return Response({'method':'put'})
    
    def patch(self, request, pk=None):
        #Patch request, only updates fields provided in the request
        return Response({'method':'patch'})
    
    def delete(self, request, pk=None):
        #Deletes object
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    #test API viewset
    def list(self, request):
        #Return hello message
        a_viewset=[
            'Uses action (list, create, retreve, update, partial update)',
            'Automatically map to URLs Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})