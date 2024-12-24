import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  imageSrc: string = 'assets/doctor.jpg';


  constructor(private router: Router) {}

  onSubmit() {
    // Implement authentication logic
    // send cridentals to api
    // api will return object
    if (this.username === 'admin' && this.password === 'admin') {
      this.router.navigate(['/dashboard']);
    } else if(this.username === 'patient' && this.password === 'patient'){
      this.router.navigate(['/patient']);
    } else {
      alert('Invalid credentials');
    }
  }

  onCancel(){
    this.router.navigate(['/']);
  }
}
