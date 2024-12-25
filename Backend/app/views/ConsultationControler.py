from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers.khalil_serializers import ConsultationSerializer
from app.models import Consultation, Diagnostic


@api_view(['POST'])
def crea_Consultation(request):
    #request must have the id of the current diagnostic and the consultation attributes
    diagnostic_id = request.data['id_diagnostic']
    if not diagnostic_id:
        return Response("id_diagnostic is required", status=400)
    
    try:
        diagnostic = Diagnostic.objects.get(id_diagnostic=diagnostic_id)
    except Diagnostic.DoesNotExist:
        return Response(f"Diagnostic with id {diagnostic_id} does not exist", status=404)
    
    consultation = request.data
    consultation['diagnostic'] = diagnostic
    serializer = ConsultationSerializer(data=consultation)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)