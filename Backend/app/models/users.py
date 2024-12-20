from django.db import models
from .khalil_models import SpecialiteMedicale

#---------------------------------------------------------------------------------------------------------------
# ACTORS

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=30)
    date_creation = models.DateTimeField()
    derniere_connexion = models.DateTimeField()
    telephone = models.CharField(max_length=20)

class Medecin(Utilisateur):
    numero_ordre = models.CharField(max_length=50, unique=True)
    specialite = models.CharField(max_length=20, choices=SpecialiteMedicale.choices)
    etablissement = models.CharField(max_length=100)

class Infirmier(Utilisateur):
    service = models.CharField(max_length=100)

class Laboratoire(Utilisateur):
    nom_etablissement = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)

class Radiologue(Utilisateur):
    etablissement = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

class admin(Utilisateur):
    service = models.CharField(max_length=100)

class Patient(Utilisateur):
    NSS = models.CharField(max_length=15, primary_key=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    mutuelle = models.CharField(max_length=100)
    medecin_traitant = models.ForeignKey(
            Medecin,
            on_delete=models.SET_NULL, null=True        
        )
    personne_contact_nom = models.CharField(max_length=100)
    personne_contact_telephone = models.CharField(max_length=20)
