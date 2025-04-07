# auth_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from django.shortcuts import render


class LoginAPIView(APIView):
    def post(self, request):
        # Obtener el nombre de usuario y la contraseña del cuerpo de la solicitud
        username = request.data.get('username')
        password = request.data.get('password')

        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        
        if user:
            # Si la autenticación es exitosa, generar el token
            payload = {
                'id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            # Retornar el token JWT en la respuesta
            return Response({'token': token})
        
        # Si las credenciales no son correctas
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


def login_page(request):
    return render(request, 'reportes/login.html')