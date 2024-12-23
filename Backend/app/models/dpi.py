from django.db import models
from .users import Patient
from .khalil_models import Diagnostic, Compte_Rendu, CertificatMedical, Hospitalisation, Soin
from datetime import datetime

# TODO -> ask khalil
# class StatutDPI(models.TextChoices):
#     OUVERT = 'OUVERT'
#     EN_COURS = 'EN_COURS'
#     CLOTURE = 'CLOTURE'
#     ARCHIVE = 'ARCHIVE'
#     SUSPENDU = 'SUSPENDU'


class DPI(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField(default=datetime.now)
    
    # relations with users
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True)
    
    # TODO -> ask khalil
    commentaire_administratif = models.TextField()
    chemin_QR_code = models.CharField(max_length=255)
    
    
    
    
