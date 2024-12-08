from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def afficher_patient(request):
    return HttpResponse('hola amigos')