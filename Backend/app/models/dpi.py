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
    
    # relations with objects
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.SET_NULL, null=True)
    compte_Rendu = models.ForeignKey(Compte_Rendu, on_delete=models.SET_NULL, null=True)
    certificatMedical = models.ForeignKey(CertificatMedical, on_delete=models.SET_NULL, null=True)
    hospitalisation = models.ForeignKey(Hospitalisation, on_delete=models.SET_NULL, null=True)
    soin = models.ForeignKey(Soin, on_delete=models.SET_NULL, null=True)
    
    # relations with users
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True)
    
    # TODO -> ask khalil
    commentaire_administratif = models.TextField()
    chemin_QR_code = models.CharField(max_length=255)
    
    
    
    
