from rest_framework import generics
from app.permissions import isInfirmier
from app.serializers.soins import AddSoinSerializer, ListSoinsSerializer
from app.models import Soin

class AddSoinView(generics.CreateAPIView):
    #permission_classes = [isInfirmier]
    serializer_class = AddSoinSerializer

class ListSoinsView(generics.ListAPIView):
    serializer_class = ListSoinsSerializer


    def get_queryset(self):
        # list all 'soins' for the 'infirmier' that logged-in
        queryset = Soin.objects.filter(infirmier=self.request.user.infirmier_profile)
        return queryset