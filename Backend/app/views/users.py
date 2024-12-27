from rest_framework import generics
from app.serializers.users import RegisterSerializer, ListUsersSerializer
from app.models import Utilisateur
from app.permissions import isAdmin

class RegisterView(generics.CreateAPIView):
    #permission_classes = [isAdmin]
    serializer_class = RegisterSerializer

class ListUsersView(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = ListUsersSerializer