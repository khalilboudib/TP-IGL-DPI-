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

class TypeUtilisateur(models.TextChoices):
    ADMINISTRATIF = 'ADMINISTRATIF'
    MEDECIN = 'MEDECIN'
    INFIRMIER = 'INFIRMIER'
    PHARMACIEN = 'PHARMACIEN'
    LABORATOIRE = 'LABORATOIRE'
    RADIOLOGUE = 'RADIOLOGUE'
    PATIENT = 'PATIENT'
    ADMINISTRATEUR = 'ADMINISTRATEUR'

class SpecialiteMedicale(models.TextChoices):
    MEDECINE_GENERALE = 'MEDECINE_GENERALE'
    CARDIOLOGIE = 'CARDIOLOGIE'
    PNEUMOLOGIE = 'PNEUMOLOGIE'
    NEUROLOGIE = 'NEUROLOGIE'
    PEDIATRIE = 'PEDIATRIE'
    ONCOLOGIE = 'ONCOLOGIE'
    RADIOLOGIE = 'RADIOLOGIE'
    AUTRE = 'AUTRE'

class StatutDPI(models.TextChoices):
    OUVERT = 'OUVERT'
    EN_COURS = 'EN_COURS'
    CLOTURE = 'CLOTURE'
    ARCHIVE = 'ARCHIVE'
    SUSPENDU = 'SUSPENDU'

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
# ACTORS

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(unique=True)
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
    medecin_traitant = models.ForeignKey(Medecin)
    personne_contact_nom = models.CharField(max_length=100)
    personne_contact_telephone = models.CharField(max_length=20)

#---------------------------------------------------------------------------------------------------------------
# MODELES

class Medicament(models.Model):
    id_medicament = models.AutoField(primary_key=True)
    nom_medicament = models.CharField(max_length=100)
    dose = models.CharField(max_length=50)
    duree_traitement = models.CharField(max_length=50)

class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    date_creation = models.DateField(initial=datetime.datetime.now)
    validated = models.TextField(choices=StatutValidationOrdonnance.choices)
    medicaments = models.ForeignKey(Medicament)

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
    resume_consultation = models.OneToOneField(Resume)
    examen_consultation = models.ForeignKey(Examen_Consultation)

class Resultat_Biologique(models.Model):
    id_resultat = models.AutoField(primary_key=True)
    parametre = models.TextField(choices=Parametre_biologique.choices)
    valeur = models.FloatField()
    unite = models.CharField(max_length=20)

class Bilan_Biologique(models.Model):
    id_bilan_biologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField(initial=datetime.datetime.now)
    laboratoire = models.OneToOneField(Laboratoire)
    resultats = models.ForeignKey(Resultat_Biologique)

class ImageMedicale(models.Model):
    id_image = models.AutoField(primary_key=True)
    chemin_fichier = models.CharField(max_length=255)

class Examen_Radiologique(models.Model):
    id_examen = models.AutoField(primary_key=True)
    resultat = models.OneToOneField(ImageMedicale)
    date_examen = models.DateField()
    Radiologue = models.OneToOneField(Radiologue)
    TypeRadio = models.TextField(choices=TypeRadio.choices)

class Bilan_Radiologique(models.Model):
    id_bilan_radiologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField(initial=datetime.datetime.now)
    examens = models.ForeignKey(Examen_Radiologique)

class Examen_Complementaire(models.Model):
    id_examen_complementaire = models.AutoField(primary_key=True)
    description = models.TextField()
    bilan_Biologique = models.OneToOneField(Bilan_Biologique)
    bilan_Radiologique = models.OneToOneField(Bilan_Radiologique)
    

class Diagnostic(models.Model):
    id_diagnostic = models.AutoField(primary_key=True)
    diagnostic = models.TextField()
    date_creation = models.DateTimeField(initial=datetime.datetime.now)
    medecin = models.OneToOneField(Medecin)
    consultations = models.ForeignKey(Consultation)
    ordanance = models.OneToOneField(Ordonnance)
    examen_Complementaire = models.ForeignKey(Examen_Complementaire)

class Compte_Rendu(models.Model):
    id_compte_rendu = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField(initial=datetime.datetime.now)
    radiologue = models.OneToOneField(Radiologue)
    texte = models.TextField()
    examen_Radiologique = models.OneToOneField(Examen_Radiologique)

class CertificatMedical(models.Model):
    id_certificat = models.AutoField(primary_key=True)
    medecin = models.OneToOneField(Medecin)
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
    admin = models.OneToOneField(admin)

class Hospitalisation(models.Model):
    id_hospitalisation = models.AutoField(primary_key=True)
    date_entree = models.DateField()
    date_sortie = models.DateField()
    nbr_chamisation = models.IntegerField()
    etablissement_hospitalier = models.CharField(max_length=100)
    decompte_des_frais = models.OneToOneField(Decompte_des_frais)

class Soin(models.Model):
    id_soin = models.AutoField(primary_key=True)
    date_soin = models.DateTimeField()
    infirmier = models.OneToOneField(Infirmier)
    description_soin = models.TextField()
    observation_patient = models.TextField()
    status = models.CharField(max_length=20)

class DPI(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient)
    date_creation = models.DateTimeField()
    commentaire_administratif = models.TextField()
    chemin_QR_code = models.CharField(max_length=255)
    diagnostic = models.ForeignKey(Diagnostic)
    compte_Rendu = models.ForeignKey(Compte_Rendu)
    certificatMedical = models.ForeignKey(CertificatMedical)
    hospitalisation = models.ForeignKey(Hospitalisation)
    soin = models.ForeignKey(Soin)
