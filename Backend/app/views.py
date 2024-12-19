from django.shortcuts import render
from django.http import HttpResponse
from .models.khalil_models import Medicament

# Create your views here.
def index(request):
    med = Medicament(nom_medicament="dolipran", dose="90", duree_traitement="90")
    med.save()
    return HttpResponse("Hello, world. You're at the polls index.")