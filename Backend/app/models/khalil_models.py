from django.db import models
from datetime import datetime

class TypeRadio(models.TextChoices):
    IRM = 'IRM'
    ECHOGRAPHIE = 'ECHOGRAPHIE'
    RADIOGRAPHIE = 'RADIOGRAPHIE'
    SCANNER = 'SCANNER'
    AUTRES = 'AUTRES'

class StatutValidationOrdonnance(models.TextChoices):
    EN_ATTENTE = 'EN_ATTENTE'
    VALIDEE = 'VALIDEE'
    REJETEE = 'REJETEE'



class SpecialiteMedicale(models.TextChoices):
    MEDECINE_GENERALE = 'MEDECINE_GENERALE'
    CARDIOLOGIE = 'CARDIOLOGIE'
    PNEUMOLOGIE = 'PNEUMOLOGIE'
    NEUROLOGIE = 'NEUROLOGIE'
    PEDIATRIE = 'PEDIATRIE'
    ONCOLOGIE = 'ONCOLOGIE'
    RADIOLOGIE = 'RADIOLOGIE'
    AUTRE = 'AUTRE'


class TypeCertificat(models.TextChoices):
    ARRET_TRAVAIL = 'ARRET_TRAVAIL'
    APTITUDE = 'APTITUDE'
    INCAPACITE_TEMPORAIRE = 'INCAPACITE_TEMPORAIRE'
    INAPTITUDE = 'INAPTITUDE'
    SUIVI_MEDICAL = 'SUIVI_MEDICAL'
    AUTRE = 'AUTRE'

class Outils(models.TextChoices):
    STETHOSCOPE = 'STETHOSCOPE'
    OTOSCOPE = 'OTOSCOPE'
    THERMOMETRE = 'THERMOMETRE'
    OXYMETRE = 'OXYMETRE'
    AUTRES = 'AUTRES'

class Parametre_biologique(models.TextChoices):
    HEMOGLOBINE = 'HEMOGLOBINE'
    GLYCEMIE = 'GLYCEMIE'
    CHOLESTEROL = 'CHOLESTEROL'
    TRIGLYCERIDES = 'TRIGLYCERIDES'
    ACIDE_URIQUE = 'ACIDE_URIQUE'
    CREATININE = 'CREATININE'
    UREE = 'UREE'
    TSH = 'TSH'
    T4 = 'T4'
    T3 = 'T3'
    PSA = 'PSA'
    CRP = 'CRP'
    FERRITINE = 'FERRITINE'


#---------------------------------------------------------------------------------------------------------------
# MODELES

class Medicament(models.Model):
    id_medicament = models.AutoField(primary_key=True)
    nom_medicament = models.CharField(max_length=100)
    dose = models.CharField(max_length=50)
    duree_traitement = models.CharField(max_length=50)

class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    date_creation = models.DateField(default=datetime.now)
    validated = models.TextField(choices=StatutValidationOrdonnance.choices)
    medicaments = models.ForeignKey(Medicament, on_delete=models.SET_NULL, null=True)

class Examen_Consultation(models.Model):
    id_examen_consultation = models.AutoField(primary_key=True)
    outils = models.CharField(max_length=20, choices=Outils.choices)
    description = models.TextField()

class Resume(models.Model):
    id_resume = models.AutoField(primary_key=True)
    text = models.TextField()
    antecedents = models.JSONField(default=list)

class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    date_consultation = models.DateTimeField()
    resume_consultation = models.OneToOneField(Resume, on_delete=models.SET_NULL, null=True)
    examen_consultation = models.ForeignKey(Examen_Consultation, on_delete=models.SET_NULL, null=True)

class Resultat_Biologique(models.Model):
    id_resultat = models.AutoField(primary_key=True)
    parametre = models.TextField(choices=Parametre_biologique.choices)
    valeur = models.FloatField()
    unite = models.CharField(max_length=20)

class Bilan_Biologique(models.Model):
    id_bilan_biologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField(default=datetime.now)
    laboratoire = models.OneToOneField("app.Laboratoire", on_delete=models.SET_NULL, null=True)
    resultats = models.ForeignKey(Resultat_Biologique, on_delete=models.SET_NULL, null=True)

class ImageMedicale(models.Model):
    id_image = models.AutoField(primary_key=True)
    chemin_fichier = models.CharField(max_length=255)

class Examen_Radiologique(models.Model):
    id_examen = models.AutoField(primary_key=True)
    resultat = models.OneToOneField(ImageMedicale, on_delete=models.SET_NULL, null=True)
    date_examen = models.DateField()
    Radiologue = models.OneToOneField("app.Radiologue", on_delete=models.SET_NULL, null=True)
    TypeRadio = models.TextField(choices=TypeRadio.choices)

class Bilan_Radiologique(models.Model):
    id_bilan_radiologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField(default=datetime.now)
    examens = models.ForeignKey(Examen_Radiologique, on_delete=models.SET_NULL, null=True)

class Examen_Complementaire(models.Model):
    id_examen_complementaire = models.AutoField(primary_key=True)
    description = models.TextField()
    bilan_Biologique = models.OneToOneField(Bilan_Biologique, on_delete=models.SET_NULL, null=True)
    bilan_Radiologique = models.OneToOneField(Bilan_Radiologique, on_delete=models.SET_NULL, null=True)
    

class Diagnostic(models.Model):
    id_diagnostic = models.AutoField(primary_key=True)
    diagnostic = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now)
    medecin = models.OneToOneField("app.Medecin", on_delete=models.SET_NULL, null=True)
    consultations = models.ForeignKey(Consultation, on_delete=models.SET_NULL, null=True)
    ordanance = models.OneToOneField(Ordonnance, on_delete=models.SET_NULL, null=True)
    examen_Complementaire = models.ForeignKey(Examen_Complementaire, on_delete=models.SET_NULL, null=True)

class Compte_Rendu(models.Model):
    id_compte_rendu = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField(default=datetime.now)
    radiologue = models.OneToOneField("app.Radiologue", on_delete=models.SET_NULL, null=True)
    texte = models.TextField()
    examen_Radiologique = models.OneToOneField(Examen_Radiologique, on_delete=models.SET_NULL, null=True)

class CertificatMedical(models.Model):
    id_certificat = models.AutoField(primary_key=True)
    medecin = models.OneToOneField("app.Medecin", on_delete=models.SET_NULL, null=True)
    date_emission = models.DateTimeField()
    date_debut_validite = models.DateField()
    date_fin_validite = models.DateField()
    type_certificat = models.CharField(max_length=21, choices=TypeCertificat.choices)
    duree_arret_travail = models.IntegerField()
    recommandations = models.TextField()
    etablissement = models.CharField(max_length=100)
    signature_numerique = models.CharField(max_length=255)
    chemin_fichier = models.CharField(max_length=255)

class Decompte_des_frais(models.Model):
    id_decompte = models.AutoField(primary_key=True)
    date_decompte = models.DateField()
    montant_total = models.FloatField()
    montant_rembourse = models.FloatField()
    montant_a_payer = models.FloatField()
    admin = models.OneToOneField("app.admin", on_delete=models.SET_NULL, null=True)

class Hospitalisation(models.Model):
    id_hospitalisation = models.AutoField(primary_key=True)
    date_entree = models.DateField()
    date_sortie = models.DateField()
    nbr_chamisation = models.IntegerField()
    etablissement_hospitalier = models.CharField(max_length=100)
    decompte_des_frais = models.OneToOneField(Decompte_des_frais, on_delete=models.SET_NULL, null=True)


