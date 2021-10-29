from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
# from rest_framework import authentication
from rest_framework.decorators import authentication_classes
from .serializers import LibrarySerializer
from .models import LibrarySet
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class LibraryApiView(ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = LibrarySerializer
    queryset = LibrarySet.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
    
        return self.list(request)

    
    def post(self, request, id=None):
        return self.create(request)

    
    def put(self, request, id=None):
        return self.update(request, id)

    
    def delete(self, request, id):
        return self.destroy(request, id)



