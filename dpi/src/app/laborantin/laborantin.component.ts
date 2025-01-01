import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-laborantin',
  imports: [],
  templateUrl: './laborantin.component.html',
  styleUrl: './laborantin.component.css'
})
export class LaborantinComponent implements OnInit {
  id: string = '';
  laborantin: any;
  constructor(private router: Router, private route: ActivatedRoute, private dataService: DataService) {
    this.route.params.subscribe(params  => {
      this.id = params['id'];
    });
  }
  ngOnInit(): void {
    this.getLaborantin();
  }
  getLaborantin(): void {
    this.dataService.getData('laborantin' + this.id).subscribe(data => {
      this.laborantin = data;
    },
    error => {
      console.log('Error: ', error);
      this.laborantin = {
        id: '0',
        nom: 'Inconnu',
        prenom: 'Inconnu',
        date_naissance: 'Inconnu',
        adresse: 'Inconnu',
        telephone: 'Inconnu',
        email: 'Inconnu',
        password: 'Inconnu',
      }
    });
  }
}
