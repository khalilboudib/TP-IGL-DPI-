from django.db import models
from django.contrib.auth.models import AbstractUser
from .khalil_models import SpecialiteMedicale
from datetime import datetime

#---------------------------------------------------------------------------------------------------------------
# ACTORS

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    birth_date = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    # username, password, last login ... are inherited from "AbstractUser"

    # the role
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("patient", "Patient"),
        ("medecin", "Medecin"),
        ("infirmier", "Infirmier"),
        ("radiologue", "Radiologue"),
        ("laborantin", "Laborantin"),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="admin")
    USERNAME_FIELD = 'email' # authenticate using email instead of username
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
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
    def __str__(self):
        return f"{self.email}_{self.role}"

class Medecin(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True, related_name="medecin_profile")

class Infirmier(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True, related_name="infirmier_profile")

class Laboratoire(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True, related_name="laborantin_profile")

class Radiologue(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True, related_name="radiologue_profile")

class admin(models.Model):   
    user = models.OneToOneField(Utilisateur, on_delete=models.SET_NULL, null=True, related_name="admin_profile")
