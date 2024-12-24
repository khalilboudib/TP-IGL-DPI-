import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

interface DPI {
  id_dpi: number;
  date_creation: string;
  commentaire_medecin: string;
  chemin_QR_code: string;
}

@Component({
  selector: 'app-dpi-list',
  standalone: true, // Ensure this is marked as standalone
  imports: [CommonModule], // Import CommonModule here
  templateUrl: './dpi-list.component.html',
  styleUrls: ['./dpi-list.component.css']
})

export class DpiListComponent implements OnInit {

  showSearchOptions: boolean = false;  // Flag to control visibility of the search options

  constructor(private router: Router) {}

  dpis: DPI[] = [];

  ngOnInit(): void {
    this.dpis = [
      {
        id_dpi: 1,
        date_creation: '2024-01-01',
        commentaire_medecin: 'Doctor Comment 1',
        chemin_QR_code: '/assets/qrcodes/qrcode1.png',
      },
      {
        id_dpi: 2,
        date_creation: '2024-01-02',
        commentaire_medecin: 'Doctor Comment 2',
        chemin_QR_code: '/assets/qrcodes/qrcode2.png',
      },
    ];
  }

  searchByNSS(): void {
    alert('Search by NSS triggered.');
    this.showSearchOptions = false ;
  }

  searchByQRCode(): void {
    alert('Search by QR Code triggered.');
    this.showSearchOptions = false ;
  }

  viewDpiDetails(dpiId: number): void {
    console.log('Navigate to DPI:', dpiId);
  }

  createNewDpi(): void {
    alert('Navigate to Create DPI page.');
  }
}
