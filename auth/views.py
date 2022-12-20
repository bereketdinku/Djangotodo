from django.shortcuts import render
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from . import serializer
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import status


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializer.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)