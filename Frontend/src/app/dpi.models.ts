export interface DPI {
    id_dpi: number;
    date_creation: string;
    diagnostic?: Diagnostic;
    compte_Rendu?: CompteRendu;
    certificatMedical?: CertificatMedical;
    hospitalisation?: Hospitalisation;
    soin?: Soin;
    patient?: Patient;
    commentaire_administratif: string;
    chemin_QR_code: string;
  }
  
  export interface Diagnostic {
    id_diagnostic: number;
    diagnostic: string;
    date_creation: string;
    medecin?: Medecin;
    consultations?: Consultation;
    ordanance?: Ordonnance;
    examen_Complementaire?: ExamenComplementaire;
  }
  
  export interface CompteRendu {
    id_compte_rendu: number;
    date_creation: string;
    radiologue?: Radiologue;
    texte: string;
    examen_Radiologique?: ExamenRadiologique;
  }
  
  export interface CertificatMedical {
    id_certificat: number;
    medecin?: Medecin;
    date_emission: string;
    date_debut_validite: string;
    date_fin_validite: string;
    type_certificat: string;
    duree_arret_travail: number;
    recommandations: string;
    etablissement: string;
    signature_numerique: string;
    chemin_fichier: string;
  }
  
  export interface Hospitalisation {
    id_hospitalisation: number;
    date_entree: string;
    date_sortie: string;
    nbr_chamisation: number;
    etablissement_hospitalier: string;
    decompte_des_frais?: DecompteDesFrais;
  }
  
  export interface Soin {
    id_soin: number;
    date_soin: string;
    infirmier?: Infirmier;
    description_soin: string;
    observation_patient: string;
    status: string;
  }
  
  export interface Patient {
    NSS: string;
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
    date_creation: string;
    derniere_connexion: string;
    telephone: string;
    date_naissance: string;
    adresse: string;
    mutuelle: string;
    medecin_traitant?: Medecin;
    personne_contact_nom: string;
    personne_contact_telephone: string;
  }
  
  export interface Medicament {
    id_medicament: number;
    nom_medicament: string;
    dose: string;
    duree_traitement: string;
  }
  
  export interface Ordonnance {
    id_ordonnance: number;
    date_creation: string;
    validated: string;
    medicaments?: Medicament;
  }
  
  export interface ExamenConsultation {
    id_examen_consultation: number;
    outils: string;
    description: string;
  }
  
  export interface Resume {
    id_resume: number;
    text: string;
    antecedents: any[];
  }
  
  export interface Consultation {
    id_consultation: number;
    date_consultation: string;
    resume_consultation?: Resume;
    examen_consultation?: ExamenConsultation;
  }
  
  export interface ResultatBiologique {
    id_resultat: number;
    parametre: string;
    valeur: number;
    unite: string;
  }
  
  export interface BilanBiologique {
    id_bilan_biologique: number;
    date_bilan: string;
    laboratoire?: Laboratoire;
    resultats?: ResultatBiologique;
  }
  
  export interface ExamenRadiologique {
    id_examen: number;
    resultat?: ImageMedicale;
    date_examen: string;
    Radiologue?: Radiologue;
    TypeRadio: string;
  }
  
  export interface BilanRadiologique {
    id_bilan_radiologique: number;
    date_bilan: string;
    examens?: ExamenRadiologique;
  }
  
  export interface ExamenComplementaire {
    id_examen_complementaire: number;
    description: string;
    bilan_Biologique?: BilanBiologique;
    bilan_Radiologique?: BilanRadiologique;
  }
  
  export interface ImageMedicale {
    id_image: number;
    chemin_fichier: string;
  }
  
  export interface Radiologue {
    id_radiologue: number;
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
    telephone: string;
  }
  
  export interface DecompteDesFrais {
    id_decompte: number;
    date_decompte: string;
    montant_total: number;
    montant_rembourse: number;
    montant_a_payer: number;
    admin?: Admin;
  }
  
  export interface Admin {
    id_admin: number;
    service: string;
  }
  
  export interface Medecin {
    id_medecin: number;
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
    telephone: string;
  }
  
  export interface Infirmier {
    id_infirmier: number;
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
    telephone: string;
  }
  
  export interface Laboratoire {
    id_laboratoire: number;
    nom: string;
    adresse: string;
    telephone: string;
  }