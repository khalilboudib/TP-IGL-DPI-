import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


export const routes: Routes = [
    { path: 'login', loadComponent: () => import('./login/login.component').then(m => m.LoginComponent) },
    { path: 'home', loadComponent: () => import('./home/home.component').then(m => m.HomeComponent) },
    { path: 'patient', loadComponent: () => import('./patient/patient.component').then(m => m.PatientComponent) },
    { path: 'dashboard', loadComponent: () => import('./admin-dashboard/admin-dashboard.component').then(m => m.AdminDashboardComponent) },
    { path: 'profil', loadComponent: () => import('./admin-profil/admin-profil.component').then(m => m.AdminProfilComponent) },
    { path: 'dpi-list', loadComponent: () => import('./dpi-list/dpi-list.component').then(m => m.DpiListComponent) },
    { path: 'create-dpi', loadComponent: () => import('./create-dpi/create-dpi.component').then(m => m.CreateDpiComponent) },
    { path: '', redirectTo: '/home', pathMatch: 'full' }
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
