import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import {FormsModule} from '@angular/forms';

interface Patient {
  NSS: string;
  nom: string;
  prenom: string;
}

interface DPI {
  id_dpi: number;
  date_creation: string;
  commentaire_administratif: string;
  chemin_QR_code: string;
  patient?: Patient;
}

@Component({
  selector: 'app-dpi-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dpi-list.component.html',
  styleUrls: ['./dpi-list.component.css']
})

export class DpiListComponent implements OnInit {

  showSearchOptions: boolean = false;
  dpis: DPI[] = [];
  selectedDpi: DPI | null = null;
  showModal: boolean = false;
  nssInput: string = ''; // Bind to the input field for NSS

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.dpis = [
      {
        id_dpi: 1,
        date_creation: '2024-01-01',
        commentaire_administratif: 'Admin Comment 1',
        chemin_QR_code: '/assets/qrcodes/dpi1.png',
        patient: {
          NSS: '123456789',
          nom: 'John',
          prenom: 'Doe',
        },
      },
      {
        id_dpi: 2,
        date_creation: '2024-01-02',
        commentaire_administratif: 'Admin Comment 2',
        chemin_QR_code: '/assets/qrcodes/dpi2.png',
        patient: {
          NSS: '987654321',
          nom: 'Jane',
          prenom: 'Smith',
        },
      },
      {
        id_dpi: 3,
        date_creation: '2024-01-01',
        commentaire_administratif: 'Admin Comment 3',
        chemin_QR_code: '/assets/qrcodes/dpi1.png',
        patient: {
          NSS: '123456789',
          nom: 'John',
          prenom: 'Doe',
        },
      },
      {
        id_dpi: 4,
        date_creation: '2024-01-02',
        commentaire_administratif: 'Admin Comment 4',
        chemin_QR_code: '/assets/qrcodes/dpi2.png',
        patient: {
          NSS: '987654321',
          nom: 'Jane',
          prenom: 'Smith',
        },
      },
    ];
  }

  searchByNSS(nss: string): void {
    const dpi = this.dpis.find((dpi) => dpi.patient?.NSS === nss);
    if (dpi) {
      this.selectedDpi = dpi;
      this.showModal = true; // Show the modal
    } else {
      alert('No DPI found with this NSS');
    }
  }

  validateNSS(event: any): void {
    // Ensure the input contains only digits and is limited to 9 characters
    const regex = /^[0-9]{0,9}$/; // Only allows numbers up to 9 digits
    if (!regex.test(event.target.value)) {
      event.target.value = event.target.value.slice(0, -1); // Remove invalid character
    }
  }

  closeModal(): void {
    this.showModal = false;
    this.selectedDpi = null;
  }

  searchByQRCode(): void {
    alert('Search by QR Code triggered.');
    this.showSearchOptions = false;
  }

  viewDpiDetails(dpiId: number): void {
    console.log('Navigate to DPI:', dpiId);
  }

  createNewDpi(): void {
    alert('Navigate to Create DPI page.');
  }
}
