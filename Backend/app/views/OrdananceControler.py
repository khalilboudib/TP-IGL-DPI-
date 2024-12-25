from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import OrdonnanceSerializer, MedicamentSerializer
from app.models import Ordonnance, Medicament
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError


@api_view(['POST'])
def crea_ordanance(request):
    #request must have the id of the current diagnostic and the ordanance attributes
    
    ordanance = request.data
    serializer = OrdonnanceSerializer(data=ordanance)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class OrdananceListView(ListAPIView):
    serializer_class = OrdonnanceSerializer
    def post(self, request, *args, **kwargs):
        id_diagnostic = request.data.get('id_diagnostic')
        if not id_diagnostic:
            raise ValidationError({"error": "id_diagnostic is required"})
        
        ordanances = Ordonnance.objects.filter(diagnostic=id_diagnostic)
        if not ordanances.exists():
            return Response({"message": "No ordanances found for the given diagnostic_id"}, status=404)

        serializer = self.get_serializer(ordanances, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def ajout_medicament(request):
    #request must have the id of the current ordanance and the medicament attributes
    
    medicament = request.data
    serializer = MedicamentSerializer(data=medicament)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class MedicamentListView(ListAPIView):
    serializer_class = MedicamentSerializer
    def post(self, request, *args, **kwargs):
        id_ordanance = request.data.get('id_ordanance')
        if not id_ordanance:
            raise ValidationError({"error": "id_ordanance is required"})
        
        medicaments = Medicament.objects.filter(ordanance=id_ordanance)
        if not medicaments.exists():
            return Response({"message": "No medicaments found for the given ordanance_id"}, status=404)

        serializer = self.get_serializer(medicaments, many=True)
        return Response(serializer.data)
