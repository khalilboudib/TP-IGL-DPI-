import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private baseUrl = 'http://localhost:8000'; // Base URL of the backend

  constructor(private http: HttpClient) {}

  // Generic GET request
  getData(endpoint: string): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/${endpoint}`);
  }

  // Generic POST request
  addData(endpoint: string, data: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/${endpoint}`, data);
  }

  // Generic DELETE request
  deleteData(endpoint: string, id: string | number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl}/${endpoint}/${id}`);
  }

  // Methods for specific data models

  // DPI
  getDPI(id: number): Observable<DPI> {
    return this.getData(`dpi/${id}`);
  }

  addDPI(dpi: DPI): Observable<DPI> {
    return this.addData('dpi', dpi);
  }

  deleteDPI(id: number): Observable<void> {
    return this.deleteData('dpi', id);
  }

  // Diagnostic
  getDiagnostic(id: number): Observable<Diagnostic> {
    return this.getData(`diagnostic/${id}`);
  }

  addDiagnostic(diagnostic: Diagnostic): Observable<Diagnostic> {
    return this.addData('diagnostic', diagnostic);
  }

  deleteDiagnostic(id: number): Observable<void> {
    return this.deleteData('diagnostic', id);
  }

  // CompteRendu
  getCompteRendu(id: number): Observable<CompteRendu> {
    return this.getData(`compteRendu/${id}`);
  }

  addCompteRendu(compteRendu: CompteRendu): Observable<CompteRendu> {
    return this.addData('compteRendu', compteRendu);
  }

  deleteCompteRendu(id: number): Observable<void> {
    return this.deleteData('compteRendu', id);
  }

  // CertificatMedical
  getCertificatMedical(id: number): Observable<CertificatMedical> {
    return this.getData(`certificatMedical/${id}`);
  }

  addCertificatMedical(certificatMedical: CertificatMedical): Observable<CertificatMedical> {
    return this.addData('certificatMedical', certificatMedical);
  }

  deleteCertificatMedical(id: number): Observable<void> {
    return this.deleteData('certificatMedical', id);
  }

  // Hospitalisation
  getHospitalisation(id: number): Observable<Hospitalisation> {
    return this.getData(`hospitalisation/${id}`);
  }

  addHospitalisation(hospitalisation: Hospitalisation): Observable<Hospitalisation> {
    return this.addData('hospitalisation', hospitalisation);
  }

  deleteHospitalisation(id: number): Observable<void> {
    return this.deleteData('hospitalisation', id);
  }

  // Soin
  getSoin(id: number): Observable<Soin> {
    return this.getData(`soin/${id}`);
  }

  addSoin(soin: Soin): Observable<Soin> {
    return this.addData('soin', soin);
  }

  deleteSoin(id: number): Observable<void> {
    return this.deleteData('soin', id);
  }

  // Medicament
  getMedicament(id: number): Observable<Medicament> {
    return this.getData(`medicament/${id}`);
  }

  addMedicament(medicament: Medicament): Observable<Medicament> {
    return this.addData('medicament', medicament);
  }

  deleteMedicament(id: number): Observable<void> {
    return this.deleteData('medicament', id);
  }

  // Ordonnance
  getOrdonnance(id: number): Observable<Ordonnance> {
    return this.getData(`ordonnance/${id}`);
  }

  addOrdonnance(ordonnance: Ordonnance): Observable<Ordonnance> {
    return this.addData('ordonnance', ordonnance);
  }

  deleteOrdonnance(id: number): Observable<void> {
    return this.deleteData('ordonnance', id);
  }

  // ExamenConsultation
  getExamenConsultation(id: number): Observable<ExamenConsultation> {
    return this.getData(`examenConsultation/${id}`);
  }

  addExamenConsultation(examenConsultation: ExamenConsultation): Observable<ExamenConsultation> {
    return this.addData('examenConsultation', examenConsultation);
  }

  deleteExamenConsultation(id: number): Observable<void> {
    return this.deleteData('examenConsultation', id);
  }

  // Resume
  getResume(id: number): Observable<Resume> {
    return this.getData(`resume/${id}`);
  }

  addResume(resume: Resume): Observable<Resume> {
    return this.addData('resume', resume);
  }

  deleteResume(id: number): Observable<void> {
    return this.deleteData('resume', id);
  }

  // Consultation
  getConsultation(id: number): Observable<Consultation> {
    return this.getData(`consultation/${id}`);
  }

  addConsultation(consultation: Consultation): Observable<Consultation> {
    return this.addData('consultation', consultation);
  }

  deleteConsultation(id: number): Observable<void> {
    return this.deleteData('consultation', id);
  }

  // ResultatBiologique
  getResultatBiologique(id: number): Observable<ResultatBiologique> {
    return this.getData(`resultatBiologique/${id}`);
  }

  addResultatBiologique(resultatBiologique: ResultatBiologique): Observable<ResultatBiologique> {
    return this.addData('resultatBiologique', resultatBiologique);
  }

  deleteResultatBiologique(id: number): Observable<void> {
    return this.deleteData('resultatBiologique', id);
  }

  // BilanBiologique
  getBilanBiologique(id: number): Observable<BilanBiologique> {
    return this.getData(`bilanBiologique/${id}`);
  }

  addBilanBiologique(bilanBiologique: BilanBiologique): Observable<BilanBiologique> {
    return this.addData('bilanBiologique', bilanBiologique);
  }

  deleteBilanBiologique(id: number): Observable<void> {
    return this.deleteData('bilanBiologique', id);
  }

  // ImageMedicale
  getImageMedicale(id: number): Observable<ImageMedicale> {
    return this.getData(`imageMedicale/${id}`);
  }

  addImageMedicale(imageMedicale: ImageMedicale): Observable<ImageMedicale> {
    return this.addData('imageMedicale', imageMedicale);
  }

  deleteImageMedicale(id: number): Observable<void> {
    return this.deleteData('imageMedicale', id);
  }

  // ExamenRadiologique
  getExamenRadiologique(id: number): Observable<ExamenRadiologique> {
    return this.getData(`examenRadiologique/${id}`);
  }

  addExamenRadiologique(examenRadiologique: ExamenRadiologique): Observable<ExamenRadiologique> {
    return this.addData('examenRadiologique', examenRadiologique);
  }

  deleteExamenRadiologique(id: number): Observable<void> {
    return this.deleteData('examenRadiologique', id);
  }

  // BilanRadiologique
  getBilanRadiologique(id: number): Observable<BilanRadiologique> {
    return this.getData(`bilanRadiologique/${id}`);
  }

  addBilanRadiologique(bilanRadiologique: BilanRadiologique): Observable<BilanRadiologique> {
    return this.addData('bilanRadiologique', bilanRadiologique);
  }

  deleteBilanRadiologique(id: number): Observable<void> {
    return this.deleteData('bilanRadiologique', id);
  }

  // ExamenComplementaire
  getExamenComplementaire(id: number): Observable<ExamenComplementaire> {
    return this.getData(`examenComplementaire/${id}`);
  }

  addExamenComplementaire(examenComplementaire: ExamenComplementaire): Observable<ExamenComplementaire> {
    return this.addData('examenComplementaire', examenComplementaire);
  }

  deleteExamenComplementaire(id: number): Observable<void> {
    return this.deleteData('examenComplementaire', id);
  }

  // DecompteDesFrais
  getDecompteDesFrais(id: number): Observable<DecompteDesFrais> {
    return this.getData(`decompteDesFrais/${id}`);
  }

  addDecompteDesFrais(decompteDesFrais: DecompteDesFrais): Observable<DecompteDesFrais> {
    return this.addData('decompteDesFrais', decompteDesFrais);
  }

  deleteDecompteDesFrais(id: number): Observable<void> {
    return this.deleteData('decompteDesFrais', id);
  }

  // Utilisateur
  getUtilisateur(email: string): Observable<Utilisateur> {
    return this.getData(`utilisateur/${email}`);
  }

  addUtilisateur(utilisateur: Utilisateur): Observable<Utilisateur> {
    return this.addData('utilisateur', utilisateur);
  }

  deleteUtilisateur(email: string): Observable<void> {
    return this.deleteData('utilisateur', email);
  }
}
