from django.db import models

class Patient :
    def __init__(self,NSS,Nom,Prenom,date_naissance,adresse,tel,mutuel,tel_contact,date_creation):
        self.NSS=NSS
        self.Nom=Nom
        self.Prenom=Prenom
        self.date_naissance=date_naissance
        self.adresse=adresse
        self.tel=tel
        self.mutuel=mutuel
        self.tel_contact=tel_contact
        self.date_creation=date_creation
    

