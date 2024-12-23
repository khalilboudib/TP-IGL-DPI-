from django.db import models
from django.contrib.auth.models import AbstractUser
from .khalil_models import SpecialiteMedicale
from datetime import datetime

#---------------------------------------------------------------------------------------------------------------
# ACTORS

class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=30)
    date_creation = models.DateTimeField(default=datetime.now)
    date_naissance = models.DateTimeField()
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)

    # the role
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("patient", "Patient"),
        ("medecin", "Medecin"),
        ("infirmier", "Infirmier"),
        ("radiologue", "Radiologue"),
        ("laborantin", "Laborantin"),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="patient")
    
    # to prevent conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilisateurs',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilisateurs',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Medecin(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True)

class Infirmier(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True)

class Laboratoire(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True)

class Radiologue(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True)

class admin(models.Model):   
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True)
