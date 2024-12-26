from rest_framework import generics
from app.permissions import isInfirmier
from app.serializers.soins import AddSoinSerializer

class AddSoinView(generics.CreateAPIView):
    #permission_classes = [isInfirmier]
    serializer_class = AddSoinSerializer