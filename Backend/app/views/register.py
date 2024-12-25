from rest_framework import generics
from app.serializers.users import RegisterSerializer
from app.models import Utilisateur
from app.permissions import isAdmin

class RegisterView(generics.CreateAPIView):
    #permission_classes = [isAdmin]
    queryset = Utilisateur.objects.all()
    serializer_class = RegisterSerializer
