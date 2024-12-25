
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import DiagnosticSerializer, OrdonnanceSerializer, Examen_ComplementaireSerializer
from app.models import Diagnostic
from app.models import dpi



@api_view(['POST'])
def crea_Diagnostic(request):
    #request must have the id of the current dpi and the diagnostic attributes
    # dpi_id = request.data['id_dpi']
    # if not dpi_id:
    #     return Response("id_dpi is required", status=400)
    
    # try:
    #     dpii = dpi.objects.get(id_dpi=dpi_id)
    # except dpii.DoesNotExist:
    #     return Response(f"dpi with id {dpi_id} does not exist", status=404)
    
    diagnostic = request.data
    #diagnostic['dpi'] = dpii
    serializer = DiagnosticSerializer(data=diagnostic)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['POST'])
def ajout_ordanance(request):
    #request must have the id of the current diagnostic and the ordanance attributes
    # diagnostic_id = request.data['id_diagnostic']
    # if not diagnostic_id:
    #     return Response("id_diagnostic is required", status=400)
    
    # try:
    #     diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    # except Diagnostic.DoesNotExist:
    #     return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    ordanance = request.data
    #ordanance['diagnostic'] = diagnostic
    serializer = OrdonnanceSerializer(data=ordanance)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def ajout_diagnostic(request):
    #request must have the id of the current diagnostic and the diagnostic text field
    diagnostic_id = request.data['id_diagnostic']
    if not diagnostic_id:
        return Response("id_diagnostic is required", status=400)
    
    try:
        diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    except Diagnostic.DoesNotExist:
        return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    diagnostic_text = request.data['diagnostic']
    diagnostic['diagnostic'] = diagnostic_text
    serializer = DiagnosticSerializer(data=diagnostic)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

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