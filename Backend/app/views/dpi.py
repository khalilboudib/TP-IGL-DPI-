from rest_framework import generics
from app.serializers.dpi import AddDPISerializer
from app.models import Utilisateur
from app.permissions import isAdmin

class AddDPIView(generics.CreateAPIView):
    #permission_classes = [isAdmin]
    queryset = Utilisateur.objects.all()
    serializer_class = AddDPISerializer