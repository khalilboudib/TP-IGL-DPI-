from rest_framework import generics
from app.serializers.dpi import AddDPISerializer, ListDPIsSerializer, GetDPISerializer
from app.models import Utilisateur, DPI
from app.permissions import isAdmin

class AddDPIView(generics.CreateAPIView):
    #permission_classes = [isAdmin]
    queryset = Utilisateur.objects.all()
    serializer_class = AddDPISerializer

class ListDPIsView(generics.ListAPIView):
    queryset = DPI.objects.all()
    serializer_class = ListDPIsSerializer

class GetDPIView(generics.RetrieveAPIView):
    queryset = DPI.objects.all()
    serializer_class = GetDPISerializer