from django.shortcuts import render, redirect
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# Create a data register form 
def home(request):
    serializer = UserSerializer(data = request.POST) # Create an instance of the serializer
    if serializer.is_valid():
        serializer.save()  # Save the data to the database
        return redirect('signin_list')
    
    context = {'serializer': serializer}
    return render(request, 'signup.html', context)


# Register JSON using Django Rest API
class UserListCreateAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  # Use request.data for DRF
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def signin_list(request):
    return render(request, 'signin.html')
