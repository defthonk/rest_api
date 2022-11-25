from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class helloApiView(APIView):
    """Clase de un api view de prueba"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """retornar lista de caracteristicas del apiview"""
        an_apiview = [
            'Usamos metodos HTTP como funciones(get post, patch, put, delete)',
            'Es similar a una vista tradicional de django',
            'Nos da el mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los URls',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name') 
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """lo que hace el put es que maneja actulizar un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Maneja actualizacion parcial de un objecto"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Borrar un objeto """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test ai viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Mensae de hola mundo"""

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update)',
            'Automaticamente mapea a los URLS usando Routers',
            'Provee mas funcionalidad con menos codigo',
        ]

        return Response({'message': 'Hola', 'a_viewset': a_viewset})

    def create(self, request):
        """Crear nuevo mensaje de hola mundo """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})      
        else: 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

        
    def retrieve(self, request, pk=None):
        """ Obtener un obejto y su id """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """retorna un response que es un http put"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Actualizar parcialmente el bjeto"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destruye un objeto, osea como delete"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Crear y acrtualizar perfiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', 'email',)



