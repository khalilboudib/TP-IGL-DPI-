from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import OrdonnanceSerializer, MedicamentSerializer
from app.models import Ordonnance, Medicament, Diagnostic
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError


@api_view(['POST'])
def crea_ordanance(request):
    #request must have the id of the current diagnostic and the ordanance attributes
    diagnostic_id = request.data['diagnostic']
    if not diagnostic_id:
        return Response("id_diagnostic is required", status=400)
    
    try:
        diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    except Diagnostic.DoesNotExist:
        return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    ordanance = request.data
    serializer = OrdonnanceSerializer(data=ordanance)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class OrdananceListView(ListAPIView):
    serializer_class = OrdonnanceSerializer
    def post(self, request, *args, **kwargs):
        id_diagnostic = request.data.get('diagnostic')
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
    ordanance_id = request.data['ordannance']
    if not ordanance_id:
        return Response("id_ordanance is required", status=400)
    try:
        ordanance = Ordonnance.objects.get(id_ordonnance=ordanance_id)
    except Ordonnance.DoesNotExist:
        return Response(f"Ordonnance with id {ordanance_id} does not exist", status=404)
    
    medicament = request.data
    serializer = MedicamentSerializer(data=medicament)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class MedicamentListView(ListAPIView):
    serializer_class = MedicamentSerializer
    def post(self, request, *args, **kwargs):
        id_ordanance = request.data.get('id_ordonnance')
        if not id_ordanance:
            raise ValidationError({"error": "id_ordanance is required"})
        
        medicaments = Medicament.objects.filter(ordannance=id_ordanance)
        if not medicaments.exists():
            return Response({"message": "No medicaments found for the given ordanance_id"}, status=404)

        serializer = self.get_serializer(medicaments, many=True)
        return Response(serializer.data)
