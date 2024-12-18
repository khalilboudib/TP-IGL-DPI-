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
    // Implement your authentication logic here
    if (this.username === 'admin' && this.password === 'admin') {
      this.router.navigate(['/']);
    } else {
      alert('Invalid credentials');
    }
  }

  onCancel(){
    this.router.navigate(['/']);
  }
}