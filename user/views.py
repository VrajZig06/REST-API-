from constants.django import HttpResponse
from authenticationtoken.jwtToken import generateToken
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializer import UserSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
import logging
from django.views.decorators.csrf import csrf_exempt
import datetime

class ListUsers(APIView):

    def get(self, request, format=None):
        usernames = [{"first_name":user.first_name,"last_name":user.last_name,"email":user.email,"phone":user.phone,"address":user.address,"city":user.city,"state":user.state,"zip_code":user.zip_code} for user in User.objects.all()]
        return Response(usernames)
    
    def post(self, request, format=None):
        try:
            body = request.data.copy()

            body['auth_token'] = generateToken(body)
            body['password'] = make_password(body.get('password'))

            # Serialize and validate
            serializer = UserSerializer(data=body)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"detail": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoginAPI(APIView):
    def post(self, request, format=None):
        try:
            body = request.data.copy()
            email = body.get('email')
            raw_password = body.get('password')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            if not check_password(raw_password, user.password):
                return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

            # Auth success — serialize and return full user data
            user_data = UserSerializer(user).data
            return Response({
                **user_data,
                "status": status.HTTP_200_OK,
                "message": "User logged in successfully."
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print("Login error:", e)
            return Response({"detail": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)