from django.http import response
from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

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
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        #Return hello message
        a_viewset=[
            'Uses action (list, create, retreve, update, partial update)',
            'Automatically map to URLs Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})
    
    def create(self, request):
        #Create a hello message
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        #handles getting an object by its ID
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        #Handles updating object
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        #Handles updating part of an object
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request, pk=None):
        #Handles removing object
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    #handles create, read and update profile
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() #listing out all objects in database
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES