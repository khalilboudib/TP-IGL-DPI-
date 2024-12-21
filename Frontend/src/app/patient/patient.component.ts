import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'; 
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  imports: [FormsModule, CommonModule, HttpClientModule],
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {

  view: string = 'actions';

  
  patient: any = null;
  fetchedPatients: any[] = [];
  id: string = '2';

  constructor(private router: Router, private http: HttpClient) {}

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


  ngOnInit(): void {
    this.fetchPatientById(this.id);
  }
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

  //Mock API call to fetch patients
  fetchPatients() {
    const apiUrl = 'https://6766e47c560fbd14f18c6ca2.mockapi.io/patient';
    this.http.get<any[]>(apiUrl).subscribe({
      next: (data) => {
        this.fetchedPatients = data;
        console.log('Fetched Patients:', this.fetchedPatients);
      },
      error: (err) => {
        console.error('Error fetching patients:', err);
      }
    });
  }

  //Mock API call to fetch a single patient by ID
  fetchPatientById(id: string) {
    const apiUrl = `https://6766e47c560fbd14f18c6ca2.mockapi.io/patient`;
    this.http.get<any>(`${apiUrl}/${id}`).subscribe({
      next: (data) => {
        this.patient = data;
        console.log('Fetched Patient:', data);
      },
      error: (err) => {
        console.error('Error fetching patient:', err);
      }
    });
  }
  
}
