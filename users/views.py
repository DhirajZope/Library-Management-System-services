# from django.shortcuts import render
# from rest_framework import mixins
# from rest_framework.generics import GenericAPIView
# from django.contrib.auth.models import User
from http.client import OK
from django.http import response
# from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import csrf_exempt
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.utils.decorators import method_decorator


# Create your views here.
class UserRegistration(APIView):
    
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # print(serializer._validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # email = serialiser_data.data.get('email')
        # password = serialiser_data.data.get('password')
        # # password2 = serialiser_data.data.get('password2')
        # first_name = serialiser_data.data.get('first_name')
        # last_name = serialiser_data.data.get('last_name')

        # if email and password:
        #     user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        #     return user

        # else:
        #     return Response('404 Something Went Wrong')

class UserAuthentication(APIView):
    
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                
                data = {
                    'user': {
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                    },
                    'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
                }

                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(msg="User is inactive", status=status.HTTP_404_NOT_FOUND)
        return Response("Invalid Username or Password", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user_logout(request):
  request.user.auth_token.delete()
  logout(request)
  return Response("Logged out", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user(request):
    user = request.user
    if user:
        data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name 
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)