from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import Examen_ComplementaireSerializer, Examen_ComplementaireSerializer, Bilan_BiologiqueSerializer, Resultat_BiologiqueSerializer, Bilan_RadiologiqueSerializer, Examen_RadiologiqueSerializer, ImageMedicaleSerializer
from app.models import Examen_Complementaire, Diagnostic, Bilan_Biologique, Bilan_Radiologique, Resultat_Biologique, Examen_Radiologique, ImageMedicale
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError


@api_view(['POST'])
def ajout_ExamenComplementaire(request):
    #request must have the id of the current diagnostic and the examen complementaire attributes
    diagnostic_id = request.data['diagnostic']
    if not diagnostic_id:
        return Response("id_diagnostic is required", status=400)
    
    try:
        diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    except Diagnostic.DoesNotExist:
        return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    examen_complementaire = request.data
    serializer = Examen_ComplementaireSerializer(data=examen_complementaire)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class ExamenComplementaireListView(ListAPIView):
    serializer_class = Examen_ComplementaireSerializer
    def post(self, request, *args, **kwargs):
        id_diagnostic = request.data.get('diagnostic')
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
    examen_comp_id = request.data['examen_complementaire']
    if not examen_comp_id:
        return Response("id_examen_complementaire is required", status=400)
    try:
        examen_complementaire = Examen_Complementaire.objects.get(id_examen_complementaire=examen_comp_id)
    except Examen_Complementaire.DoesNotExist:
        return Response(f"Examen complementaire with id {examen_comp_id} does not exist", status=404)
    
    bilan_biologique = request.data
    serializer = Bilan_BiologiqueSerializer(data=bilan_biologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def ajout_Resultat_Biologique(request):
    #request must have the id of the current bilan biologique and the resultat biologique attributes
    bilan_biologique_id = request.data['bilan_biologique']
    if not bilan_biologique_id:
        return Response("id_bilan_biologique is required", status=400)
    try:
        bilan_biologique = Bilan_Biologique.objects.get(id_bilan_biologique=bilan_biologique_id)
    except Bilan_Biologique.DoesNotExist:
        return Response(f"Bilan biologique with id {bilan_biologique_id} does not exist", status=404)
    
    resultat_biologique = request.data
    serializer = Resultat_BiologiqueSerializer(data=resultat_biologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class BilanBiologiqueListView(ListAPIView):
    serializer_class = Bilan_BiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_examen_complementaire = request.data.get('examen_complementaire')
        if not id_examen_complementaire:
            raise ValidationError({"error": "id_examen_complementaire is required"})
        
        bilans_biologiques = Bilan_Biologique.objects.filter(examen_complementaire=id_examen_complementaire)
        if not bilans_biologiques.exists():
            return Response({"message": "No bilans biologiques found for the given examen_complementaire_id"}, status=404)

        serializer = self.get_serializer(bilans_biologiques, many=True)
        return Response(serializer.data)
    
class ResultatBiologiqueListView(ListAPIView):
    serializer_class = Resultat_BiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_bilan_biologique = request.data.get('bilan_biologique')
        if not id_bilan_biologique:
            raise ValidationError({"error": "id_bilan_biologique is required"})
        
        resultats_biologiques = Resultat_Biologique.objects.filter(bilan_biologique=id_bilan_biologique)
        if not resultats_biologiques.exists():
            return Response({"message": "No resultats biologiques found for the given bilan_biologique_id"}, status=404)

        serializer = self.get_serializer(resultats_biologiques, many=True)
        return Response(serializer.data)
    



@api_view(['POST'])
def ajout_bilan_radiologique(request):
    #request must have the id of the current examen complementaire and the bilan radiologique attributes
    
    examen_comp_id = request.data['examen_complementaire']
    if not examen_comp_id:
        return Response("id_examen_complementaire is required", status=400)
    try:
        examen_complementaire = Examen_Complementaire.objects.get(id_examen_complementaire=examen_comp_id)
    except Examen_Complementaire.DoesNotExist:
        return Response(f"Examen complementaire with id {examen_comp_id} does not exist", status=404)
    
    bilan_radiologique = request.data
    serializer = Bilan_RadiologiqueSerializer(data=bilan_radiologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def ajout_examen_radiologique(request):
    #request must have the id of the current bilan radiologique and the examen radiologique attributes

    bilan_radiologique_id = request.data['bilan_radiologique']
    if not bilan_radiologique_id:
        return Response("id_bilan_radiologique is required", status=400)
    try:
        bilan_radiologique = Bilan_Radiologique.objects.get(id_bilan_radiologique=bilan_radiologique_id)
    except Bilan_Radiologique.DoesNotExist:
        return Response(f"Bilan radiologique with id {bilan_radiologique_id} does not exist", status=404)
    
    examen_radiologique = request.data
    serializer = Examen_RadiologiqueSerializer(data=examen_radiologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def ajout_resultat_radiologique(request):
    #request must have the id of the current examen radiologique and the resultat radiologique attributes

    examen_radiologique_id = request.data['examen_radiologique']
    if not examen_radiologique_id:
        return Response("id_examen_radiologique is required", status=400)
    try:
        examen_radiologique = Examen_Radiologique.objects.get(id_examen=examen_radiologique_id)
    except Examen_Radiologique.DoesNotExist:
        return Response(f"Examen radiologique with id {examen_radiologique_id} does not exist", status=404)
    
    resultat_radiologique = request.data
    serializer = ImageMedicaleSerializer(data=resultat_radiologique)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class BilanRadiologiqueListView(ListAPIView):
    serializer_class = Bilan_RadiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_examen_complementaire = request.data.get('examen_complementaire')
        if not id_examen_complementaire:
            raise ValidationError({"error": "id_examen_complementaire is required"})
        
        bilans_radiologiques = Bilan_Radiologique.objects.filter(examen_complementaire=id_examen_complementaire)
        if not bilans_radiologiques.exists():
            return Response({"message": "No bilans radiologiques found for the given examen_complementaire_id"}, status=404)

        serializer = self.get_serializer(bilans_radiologiques, many=True)
        return Response(serializer.data)

class ExamenRadiologiqueListView(ListAPIView):
    serializer_class = Examen_RadiologiqueSerializer
    def post(self, request, *args, **kwargs):
        id_bilan_radiologique = request.data.get('bilan_radiologique')
        if not id_bilan_radiologique:
            raise ValidationError({"error": "id_bilan_radiologique is required"})
        
        examens_radiologiques = Examen_Radiologique.objects.filter(bilan_radiologique=id_bilan_radiologique)
        if not examens_radiologiques.exists():
            return Response({"message": "No examens radiologiques found for the given bilan_radiologique_id"}, status=404)

        serializer = self.get_serializer(examens_radiologiques, many=True)
        return Response(serializer.data)
    
class ResultatRadiologiqueListView(ListAPIView):
    serializer_class = ImageMedicaleSerializer
    def post(self, request, *args, **kwargs):
        id_examen_radiologique = request.data.get('examen_radiologique')
        if not id_examen_radiologique:
            raise ValidationError({"error": "id_examen_radiologique is required"})
        
        resultats_radiologiques = ImageMedicale.objects.filter(examen_radiologique=id_examen_radiologique)
        if not resultats_radiologiques.exists():
            return Response({"message": "No resultats radiologiques found for the given examen_radiologique_id"}, status=404)

        serializer = self.get_serializer(resultats_radiologiques, many=True)
        return Response(serializer.data)
