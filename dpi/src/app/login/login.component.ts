import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataService } from '../data.service';

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


  constructor(private router: Router, private dataService : DataService) {}
  onSubmit() {
    const payload = { username: this.username, password: this.password };

    this.dataService.addData('login', payload).subscribe({
      next: (response: any) => {
        // Handle successful login
        const token = response.token; // Assuming the backend returns a field `token`
        localStorage.setItem('token', token);
        const userType = token.role; // Assuming the backend returns a field `role` in token
        const userId = token.id; // Assuming the backend returns a field `id` in token
        if (userType === 'admin') {
          this.router.navigate(['/dashboard' + userId]);
        } else if (userType === 'patient') {
          this.router.navigate(['/patient/' + userId]);
        } else if(userType === 'medecin'){
          this.router.navigate(['/medecin/' + userId]);
        } else if(userType === 'infirmier'){
          this.router.navigate(['/infirmier/' + userId]);
        } else if(userType === 'radiologue'){
          this.router.navigate(['/radiologue/' + userId]);
        } else if(userType === 'laborantin'){
          this.router.navigate(['/laborantin/' + userId]);
        }
        else {
          alert('Unknown user type');
        }
      },
      error: (error:any) => {
        // Handle errors
        console.error(error);
        alert('Invalid credentials or server error.');
      }
    });

        //This is a temporary solution
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
