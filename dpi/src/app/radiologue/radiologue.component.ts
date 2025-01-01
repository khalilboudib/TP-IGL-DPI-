import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-radiologue',
  imports: [],
  templateUrl: './radiologue.component.html',
  styleUrl: './radiologue.component.css'
})
export class RadiologueComponent implements OnInit {
  id: string = '';
  radiologue: any;
  constructor(private router: Router, private route: ActivatedRoute, private dataService: DataService) {
    this.route.params.subscribe(params  => {
      this.id = params['id'];
    });
  }
  ngOnInit(): void {
    this.getRadiologue();
  }
  getRadiologue(): void {
    this.dataService.getData('radiologue' + this.id).subscribe(data => {
      this.radiologue = data;
    },
    error => {
      console.log('Error: ', error);
      this.radiologue = {
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