from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import Examen_ComplementaireSerializer, Examen_ComplementaireSerializer, Bilan_BiologiqueSerializer, Resultat_BiologiqueSerializer, Bilan_RadiologiqueSerializer, Examen_RadiologiqueSerializer
from app.models import Examen_Complementaire, Diagnostic, Bilan_Biologique, Bilan_Radiologique
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError


@api_view(['POST'])
def ajout_ExamenComplementaire(request):
    #request must have the id of the current diagnostic and the examen complementaire attributes
    diagnostic_id = request.data['id_diagnostic']
    if not diagnostic_id:
        return Response("id_diagnostic is required", status=400)
    
    try:
        diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    except Diagnostic.DoesNotExist:
        return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    examen_complementaire = request.data
    examen_complementaire['diagnostic'] = diagnostic
    serializer = Examen_ComplementaireSerializer(data=examen_complementaire)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class ExamenComplementaireListView(ListAPIView):
    serializer_class = Examen_ComplementaireSerializer
    def post(self, request, *args, **kwargs):
        id_diagnostic = request.data.get('id_diagnostic')
        if not id_diagnostic:
            raise ValidationError({"error": "id_diagnostic is required"})
        
        examens_complementaires = Examen_Complementaire.objects.filter(diagnostic=id_diagnostic)
        if not examens_complementaires.exists():
            return Response({"message": "No examens complementaires found for the given diagnostic_id"}, status=404)

        serializer = self.get_serializer(examens_complementaires, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def ajout_Bilan_Biologique(request):
    #request must have the id of the current examen complementaire and the bilan biologique attributes
    
    bilan_biologique = request.data
    serializer = Bilan_BiologiqueSerializer(data=bilan_biologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def ajout_Resultat_Biologique(request):
    #request must have the id of the current bilan biologique and the resultat biologique attributes
    
    resultat_biologique = request.data
    serializer = Resultat_BiologiqueSerializer(data=resultat_biologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class BilanBiologiqueListView(ListAPIView):
    serializer_class = Bilan_BiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_examen_complementaire = request.data.get('id_examen_complementaire')
        if not id_examen_complementaire:
            raise ValidationError({"error": "id_examen_complementaire is required"})
        
        bilans_biologiques = Bilan_Biologique.objects.filter(examen_complementaire=id_examen_complementaire)
        if not bilans_biologiques.exists():
            return Response({"message": "No bilans biologiques found for the given examen_complementaire_id"}, status=404)

        serializer = self.get_serializer(bilans_biologiques, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def ajout_bilan_radiologique(request):
    #request must have the id of the current examen complementaire and the bilan radiologique attributes
    
    bilan_radiologique = request.data
    serializer = Bilan_RadiologiqueSerializer(data=bilan_radiologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def ajout_examen_radiologique(request):
    #request must have the id of the current bilan radiologique and the examen radiologique attributes
    
    examen_radiologique = request.data
    serializer = Examen_RadiologiqueSerializer(data=examen_radiologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class BilanRadiologiqueListView(ListAPIView):
    serializer_class = Bilan_RadiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_examen_complementaire = request.data.get('id_examen_complementaire')
        if not id_examen_complementaire:
            raise ValidationError({"error": "id_examen_complementaire is required"})
        
        bilans_radiologiques = Bilan_Radiologique.objects.filter(examen_complementaire=id_examen_complementaire)
        if not bilans_radiologiques.exists():
            return Response({"message": "No bilans radiologiques found for the given examen_complementaire_id"}, status=404)

        serializer = self.get_serializer(bilans_radiologiques, many=True)
        return Response
