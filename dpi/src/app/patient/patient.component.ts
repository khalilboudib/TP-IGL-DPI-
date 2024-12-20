import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'; 
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  imports: [FormsModule, CommonModule],
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  view: string = 'actions';
  bilansBiologique = [
    { title: 'Bilan Biologique 1', details: 'Details of Bilan Biologique 1' },
    { title: 'Bilan Biologique 2', details: 'Details of Bilan Biologique 2' }
  ];

  bilansRadio = [
    { title: 'Bilan Radio 1', details: 'Details of Bilan Radio 1' },
    { title: 'Bilan Radio 2', details: 'Details of Bilan Radio 2' }
  ];

  soins = [
    { title: 'Soin 1', details: 'Details of Soin 1' },
    { title: 'Soin 2', details: 'Details of Soin 2' }
  ];
  consultations = [
    { title: 'Consultation 1', details: 'Details of Consultation 1' },
    { title: 'Consultation 2', details: 'Details of Consultation 2' }
  ];

  diagnostiques = [
    { title: 'Diagnostique 1', details: 'Details of Diagnostique 1' },
    { title: 'Diagnostique 2', details: 'Details of Diagnostique 2' }
  ];
  stat = {
    consultations: this.consultations.length,
    diagnostiques: this.diagnostiques.length,
    bilansBiologique: this.bilansBiologique.length,
    bilansRadio: this.bilansRadio.length,
    soins: this.soins.length
  };
  patient = {
    numero_securite_sociale: '123456789012345',
    nom: 'Doe',
    prenom: 'John',
    date_naissance: new Date('1990-01-01'),
    adresse: '123 Main St, Anytown, USA',
    telephone: '123-456-7890',
    mutuelle: 'Mutuelle XYZ',
    medecin_traitant: 'Dr. Smith',
    personne_contact_nom: 'Jane Doe',
    personne_contact_telephone: '098-765-4321'
  };

  constructor(private router: Router) {}

  navigateTo(page: string) {
    this.router.navigate([`/${page}`]);
  }
  showDetails(section: string) {
    this.view = section;
  }

  showActions() {
    this.view = 'actions';
  }
  viewDetails(item: any) {
    alert(item.details);
  }
  
}
