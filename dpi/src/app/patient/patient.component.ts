import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'; 

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  imports: [FormsModule],
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  stat = {
    consultations: 5,
    diagnostiques: 3,
    bilansBiologique: 2,
    bilansRadio: 1,
    soins: 1 
  }
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
  
}
