from django.shortcuts import render,  redirect
from .serializer import UserRegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .tokens import account_activation_token

# UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView, UserActivationView

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "User logged in successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
    
class UserProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserRegistrationSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserActivationView(APIView):
    def get(self, request, uidb64, token):
        User = get_user_model()
        try:
            user = User.objects.get(pk=uidb64)
        except User.DoesNotExist:
            return Response({"error": "Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)

        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            messages.success(request, "Account activated successfully.")
            return redirect('user-login')
        else:
            return Response({"error": "Activation link is invalid."}, status=status.HTTP_400_BAD_REQUEST)