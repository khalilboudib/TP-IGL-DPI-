from django.db import models


class Patient:
    def __init__(self, NSS, Nom, Prenom, date_naissance, adresse, tel, mutuel, tel_contact, date_creation):
        self.NSS = NSS
        self.Nom = Nom
        self.Prenom = Prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.tel = tel
        self.mutuel = mutuel
        self.tel_contact = tel_contact
        self.date_creation = date_creation


class Laborantin:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom


class admin:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom


class radiologue:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom


class medecin:
    def __init__(self, id, nom, prenom, service):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.service = service


class infirmier:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom
